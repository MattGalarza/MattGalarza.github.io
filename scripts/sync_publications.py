#!/usr/bin/env python3
"""Import newly indexed publications from OpenAlex into papers.bib.

The script resolves the site owner's OpenAlex author profile from an optional
ORCID iD and from DOI-bearing publications already present in the bibliography.
Only new works with a DOI are imported. The scheduled GitHub workflow places
the result in a pull request so metadata and custom al-folio fields can be
reviewed before publication.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


API_BASE = "https://api.openalex.org"
ALLOWED_WORK_TYPES = {"article", "book-chapter", "conference-paper", "preprint"}
DOI_RE = re.compile(r"\bdoi\s*=\s*[\{\"]([^}\"]+)", re.IGNORECASE)
TITLE_RE = re.compile(r"\btitle\s*=\s*\{(.+?)\}\s*,?\s*$", re.IGNORECASE | re.MULTILINE)
KEY_RE = re.compile(r"^\s*@\w+\s*\{\s*([^,]+),", re.MULTILINE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bibliography", default="_bibliography/papers.bib")
    parser.add_argument("--author-name", required=True)
    parser.add_argument("--institution", default="")
    parser.add_argument("--orcid", default="")
    parser.add_argument("--min-year", type=int, default=2020)
    parser.add_argument("--api-key", default=os.environ.get("OPENALEX_API_KEY", ""))
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(character for character in value if not unicodedata.combining(character))
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def normalize_doi(value: str) -> str:
    value = (value or "").strip().casefold()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    return value.rstrip(" .")


def same_person(candidate: str, target: str) -> bool:
    candidate_parts = normalize_text(candidate).split()
    target_parts = normalize_text(target).split()
    if not candidate_parts or not target_parts:
        return False
    if candidate_parts == target_parts:
        return True
    if candidate_parts[-1] != target_parts[-1]:
        return False
    candidate_first = candidate_parts[0]
    target_first = target_parts[0]
    if len(candidate_first) == 1 or len(target_first) == 1:
        return candidate_first[0] == target_first[0]
    return candidate_first == target_first


class OpenAlexClient:
    def __init__(self, api_key: str = "") -> None:
        self.api_key = api_key

    def get(self, endpoint: str, **params: Any) -> dict[str, Any]:
        if self.api_key:
            params["api_key"] = self.api_key
        query = urllib.parse.urlencode(params)
        url = f"{API_BASE}/{endpoint.lstrip('/')}"
        if query:
            url = f"{url}?{query}"
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "MattGalarza.github.io-publication-sync/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenAlex request failed ({error.code}): {detail}") from error

    def all_results(self, endpoint: str, **params: Any) -> list[dict[str, Any]]:
        params.setdefault("per-page", 200)
        params["cursor"] = "*"
        results: list[dict[str, Any]] = []
        while params["cursor"]:
            payload = self.get(endpoint, **params)
            results.extend(payload.get("results", []))
            params["cursor"] = payload.get("meta", {}).get("next_cursor")
        return results


def author_institution_matches(author: dict[str, Any], institution: str) -> bool:
    if not institution:
        return True
    expected = normalize_text(institution)
    affiliations = (author.get("affiliations") or []) + (author.get("last_known_institutions") or [])
    for affiliation in affiliations:
        record = affiliation.get("institution", affiliation) if isinstance(affiliation, dict) else {}
        if expected in normalize_text(record.get("display_name", "")):
            return True
    return False


def matching_author_ids(work: dict[str, Any], author_name: str) -> set[str]:
    matches: set[str] = set()
    for authorship in work.get("authorships", []):
        author = authorship.get("author", {})
        if same_person(author.get("display_name", ""), author_name) and author.get("id"):
            matches.add(author["id"].rsplit("/", 1)[-1])
    return matches


def resolve_author_ids(
    client: OpenAlexClient,
    author_name: str,
    institution: str,
    orcid: str,
    existing_dois: set[str],
) -> set[str]:
    author_ids: set[str] = set()

    if orcid:
        payload = client.get("authors", filter=f"orcid:{orcid}", **{"per-page": 5})
        for author in payload.get("results", []):
            if author.get("id"):
                author_ids.add(author["id"].rsplit("/", 1)[-1])

    for doi in sorted(existing_dois):
        payload = client.get("works", filter=f"doi:{doi}", **{"per-page": 1})
        for work in payload.get("results", []):
            author_ids.update(matching_author_ids(work, author_name))

    search = client.get("authors", search=author_name, **{"per-page": 50})
    for author in search.get("results", []):
        if not same_person(author.get("display_name", ""), author_name):
            continue
        if not author_institution_matches(author, institution):
            continue
        if author.get("id"):
            author_ids.add(author["id"].rsplit("/", 1)[-1])

    if not author_ids:
        raise RuntimeError(
            "No matching OpenAlex author profile was found. Add an ORCID iD to the workflow "
            "or confirm that at least one DOI-bearing publication is already in papers.bib."
        )
    return author_ids


def bibtex_escape(value: Any) -> str:
    text = str(value or "").strip()
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
    }
    return "".join(replacements.get(character, character) for character in text)


def month_name(publication_date: str) -> str:
    try:
        return dt.date.fromisoformat(publication_date).strftime("%B")
    except (TypeError, ValueError):
        return ""


def venue_for(work: dict[str, Any]) -> tuple[str, str]:
    location = work.get("primary_location") or {}
    source = location.get("source") or {}
    venue = source.get("display_name") or location.get("raw_source_name") or ""
    crossref_type = (work.get("type_crossref") or "").casefold()
    raw_type = (location.get("raw_type") or "").casefold()
    is_conference = (
        work.get("type") == "conference-paper"
        or "proceedings" in crossref_type
        or "proceedings" in raw_type
    )
    entry_type = "inproceedings" if is_conference else "article"
    return entry_type, venue


def citation_key(work: dict[str, Any], used_keys: set[str]) -> str:
    year = str(work.get("publication_year") or "undated")
    words = [
        word
        for word in normalize_text(work.get("title", "")).split()
        if word not in {"a", "an", "and", "for", "in", "of", "on", "the", "to", "with"}
    ]
    stem = re.sub(r"[^a-z0-9]", "", words[0] if words else "publication")
    base = f"galarza{year}{stem}"
    key = base
    suffix = ord("a")
    while key.casefold() in used_keys:
        key = f"{base}{chr(suffix)}"
        suffix += 1
    used_keys.add(key.casefold())
    return key


def pages_for(work: dict[str, Any]) -> str:
    biblio = work.get("biblio") or {}
    first = biblio.get("first_page") or ""
    last = biblio.get("last_page") or ""
    if first and last and first != last:
        return f"{first}--{last}"
    return first or last


def work_to_bibtex(work: dict[str, Any], used_keys: set[str]) -> str:
    entry_type, venue = venue_for(work)
    authors = []
    for authorship in work.get("authorships", []):
        name = authorship.get("raw_author_name") or authorship.get("author", {}).get("display_name")
        if name:
            authors.append(bibtex_escape(name))

    doi = normalize_doi(work.get("doi", ""))
    biblio = work.get("biblio") or {}
    fields: list[tuple[str, Any]] = [
        ("bibtex_show", "true"),
        ("title", bibtex_escape(work.get("title", ""))),
        ("author", " and ".join(authors)),
        ("journal" if entry_type == "article" else "booktitle", bibtex_escape(venue)),
        ("volume", biblio.get("volume")),
        ("number", biblio.get("issue")),
        ("pages", pages_for(work)),
        ("year", work.get("publication_year")),
        ("month", month_name(work.get("publication_date", ""))),
        ("doi", doi),
        ("html", f"https://doi.org/{doi}"),
    ]
    fields = [(name, value) for name, value in fields if value not in (None, "")]

    lines = [
        "% AUTO-IMPORTED FROM OPENALEX. Review metadata and add preview, abstract, code,",
        "% and selected fields as appropriate before merging this pull request.",
        f"@{entry_type}{{{citation_key(work, used_keys)},",
    ]
    for index, (name, value) in enumerate(fields):
        comma = "," if index < len(fields) - 1 else ""
        lines.append(f"  {name}={{{value}}}{comma}")
    lines.append("}")
    return "\n".join(lines)


def load_existing_bibliography(path: Path) -> tuple[str, set[str], set[str], set[str]]:
    text = path.read_text(encoding="utf-8")
    dois = {normalize_doi(value) for value in DOI_RE.findall(text)}
    titles = {normalize_text(value.replace("{", "").replace("}", "")) for value in TITLE_RE.findall(text)}
    keys = {value.strip().casefold() for value in KEY_RE.findall(text)}
    return text, dois, titles, keys


def main() -> int:
    args = parse_args()
    bibliography = Path(args.bibliography)
    text, existing_dois, existing_titles, used_keys = load_existing_bibliography(bibliography)
    client = OpenAlexClient(args.api_key)
    author_ids = resolve_author_ids(
        client,
        args.author_name,
        args.institution,
        args.orcid,
        existing_dois,
    )

    works_by_id: dict[str, dict[str, Any]] = {}
    for author_id in sorted(author_ids):
        for work in client.all_results("works", filter=f"author.id:{author_id}", sort="publication_date:desc"):
            works_by_id[work.get("id", f"missing-{len(works_by_id)}")] = work

    candidates: list[dict[str, Any]] = []
    for work in works_by_id.values():
        doi = normalize_doi(work.get("doi", ""))
        title = normalize_text(work.get("title", ""))
        year = work.get("publication_year") or 0
        if not doi or doi in existing_dois or title in existing_titles:
            continue
        if year < args.min_year or work.get("is_retracted"):
            continue
        if work.get("type") not in ALLOWED_WORK_TYPES:
            continue
        if not matching_author_ids(work, args.author_name):
            continue
        candidates.append(work)

    candidates.sort(key=lambda work: (work.get("publication_date") or "", work.get("title") or ""))
    if not candidates:
        print(f"No new DOI-bearing publications found across OpenAlex author IDs: {', '.join(sorted(author_ids))}")
        return 0

    entries = [work_to_bibtex(work, used_keys) for work in candidates]
    addition = "\n\n" + "\n\n".join(entries) + "\n"
    if args.dry_run:
        print(addition.lstrip())
    else:
        bibliography.write_text(text.rstrip() + addition, encoding="utf-8")
        print(f"Added {len(entries)} publication(s) from OpenAlex: {', '.join(sorted(author_ids))}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError) as error:
        print(f"publication sync failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
