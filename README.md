# Matthew G. Galarza - Academic Website

This repository contains the source for [mattgalarza.github.io](https://mattgalarza.github.io), an academic website built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## Main content

- `_pages/about.md` - homepage biography and research interests
- `_pages/research.md` - research overview
- `_bibliography/papers.bib` - journal and conference publications
- `_data/cv.yml` - web CV
- `_data/socials.yml` - professional profile links
- `_data/repositories.yml` - featured GitHub repositories
- `_news/` - homepage announcements
- `_config.yml` - site metadata, navigation, and theme settings

## Publishing

1. Create a branch from `main`.
2. Edit the relevant Markdown, YAML, or BibTeX files.
3. Open a pull request into `main`.
4. Confirm that the Jekyll build, formatter, and link checks pass.
5. Merge the pull request.

Merging into `main` automatically runs `.github/workflows/deploy.yml`. The workflow builds the site and publishes the generated `_site` directory to the `gh-pages` branch. GitHub Pages then updates the public website.

## Privacy

Review all files before merging. Do not commit phone numbers, private email addresses, reference contact details, unpublished confidential work, or an unsanitized CV.
