# Matthew G. Galarza - Academic Website

This repository contains the source for [mattgalarza.github.io](https://mattgalarza.github.io), an academic website built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## The easiest way to make a change

You can edit the site entirely in GitHub without installing anything:

1. Open the file you want to change in this repository.
2. Click the pencil icon labeled **Edit this file**.
3. Make the change and use the **Preview** tab when editing Markdown.
4. Click **Commit changes**.
5. Choose **Create a new branch for this commit and start a pull request**.
6. Open the pull request and wait for the automated checks to pass.
7. Review the **Files changed** tab, then merge the pull request into `main`.

Working through a branch and pull request keeps the public site stable while you edit and makes every change reversible in Git history.

## Where to edit

- `_pages/about.md` - homepage biography and research interests
- `_pages/research.md` - research overview
- `_pages/blog.md` - research notes and longer-form updates
- `_bibliography/papers.bib` - journal and conference publications
- `_data/cv.yml` - web CV
- `_data/socials.yml` - professional profile links
- `_data/repositories.yml` - featured GitHub repositories
- `_news/` - homepage announcements
- `_config.yml` - site metadata, navigation, and theme settings
- `assets/img/` - profile photos, publication figures, and other images
- `assets/js/theme.js` - default light/dark appearance
- `_sass/_layout.scss` - homepage, news, publication-row, and responsive layout styling
- `_sass/_themes.scss` - light- and dark-mode accent colors

Markdown files contain a settings block at the top between `---` lines, followed by the page text. Keep the settings block intact and edit the text below it. YAML files are indentation-sensitive, so use spaces rather than tabs.

## Common updates

### Change the homepage

Edit `_pages/about.md`. The `profile.image` value near the top names the profile image stored in `assets/img/`.

To replace the photo, upload the new image to `assets/img/` and update the filename:

```yaml
profile:
  align: right
  image: your-photo.jpg
```

The current homepage uses `assets/img/headshot.jpeg`. A square or portrait image with the subject centered works best. To replace it, upload a new image and update both `_pages/about.md` and the `og_image` setting in `_config.yml`.

### Add an announcement

Copy an existing file in `_news/`, give the copy a descriptive filename, and update its contents:

```markdown
---
layout: post
date: 2026-07-29 12:00:00-0400
inline: true
related_posts: false
---

Your announcement goes here.
```

The date controls the order. Use a full date and time with your time-zone offset.

### Add a publication

Add a BibTeX record to `_bibliography/papers.bib`. Use a unique citation key and include `selected={true}` if the work should appear in the selected-publications section:

```bibtex
@article{galarza2026example,
  title={Example publication title},
  author={Galarza, Matthew G. and Collaborator, A.},
  journal={Example Journal},
  year={2026},
  doi={10.0000/example},
  bibtex_show={true},
  html={https://doi.org/10.0000/example},
  preview={your-publication-image.png},
  abstract={A concise summary of the motivation, methods, and principal findings.},
  code={https://github.com/MattGalarza/repository-name},
  selected={true}
}
```

Use the exact author order and metadata from the paper. A DOI is preferred when available. Optional fields automatically create the publication buttons: `abstract` creates **ABS**, `bibtex_show={true}` creates **BIB**, `html` creates **HTML**, and `code` creates **CODE**.

### Replace a publication thumbnail

The temporary thumbnails are stored in `assets/img/publication_preview/`:

- `placeholder-dynamics.svg`
- `placeholder-thermal.svg`
- `placeholder-mems.svg`

Upload a cropped paper figure or schematic to that folder, preferably with a 4:3 aspect ratio. Then change the corresponding `preview` field in `_bibliography/papers.bib`:

```bibtex
preview={your-paper-figure.png}
```

The selected publications currently contain clearly labeled placeholder abstracts. Search `_bibliography/papers.bib` for `Abstract placeholder` and replace those sentences when final abstracts are ready.

### Change the navigation

Each page's settings block contains `title`, `nav`, and `nav_order`. For example, `_pages/repositories.md` uses `title: software`, while its `nav_order` determines where it appears in the navigation. Smaller numbers appear first.

The intended navigation is **About, Publications, Research, Software, Blog, CV**. About is added automatically because `_pages/about.md` is the homepage. The other five pages use `nav: true`; secondary pages such as News remain accessible by links but are deliberately excluded from the top navigation.

### Update the CV

Edit `_data/cv.yml`. Each top-level entry is a section such as `Education`, `Experience`, or `Awards`, and the indented items beneath it become entries on the CV page. Copying a nearby entry is the safest starting point.

The downloadable PDF is configured in `_pages/cv.md`:

```yaml
cv_pdf: Matthew_G_Galarza_CV.pdf
```

The file itself is stored at `assets/pdf/Matthew_G_Galarza_CV.pdf`. Replace that file while keeping the same filename to update the download without editing the page configuration.

### Add a featured repository

Edit `_data/repositories.yml` and add the repository in `owner/name` format:

```yaml
github_repos:
  - MattGalarza/repository-name
```

### Change the color mode

Dark mode is enabled and is the default for new visitors. The sun/moon button in the navigation still cycles through light, dark, and system modes, and the browser remembers each visitor's choice.

To change the first-visit default, edit `assets/js/theme.js` and find:

```javascript
themeSetting = "dark";
```

Change `dark` to `light` or `system`. Do not change `enable_darkmode: true` in `_config.yml` unless you want to remove the theme toggle.

## Preview locally

For larger changes, preview the site on your computer before opening a pull request.

1. Install Git, Ruby, Bundler, and ImageMagick.
2. Clone the repository and enter its directory:

   ```bash
   git clone https://github.com/MattGalarza/MattGalarza.github.io.git
   cd MattGalarza.github.io
   ```

3. Install the Ruby dependencies:

   ```bash
   bundle install
   ```

4. Create a branch:

   ```bash
   git switch -c update/about-page
   ```

5. Start the preview server:

   ```bash
   bundle exec jekyll serve
   ```

6. Open `http://localhost:4000` in a browser. Jekyll will rebuild the preview as you save most files.
7. Commit and push your changes:

   ```bash
   git add .
   git commit -m "Update about page"
   git push -u origin update/about-page
   ```

8. Open the link GitHub prints to create a pull request.

## Publishing

The source of truth is the `main` branch. Merging a pull request into `main` automatically runs `.github/workflows/deploy.yml`. The workflow:

1. Builds the Jekyll site.
2. Checks the generated site.
3. Publishes the generated `_site` directory to the `gh-pages` branch.
4. Lets GitHub Pages update [mattgalarza.github.io](https://mattgalarza.github.io).

Deployment normally takes a few minutes after the merge. Check the repository's **Actions** tab if the site does not update. Do not edit the generated `gh-pages` branch directly because the next deployment will replace those changes.

## Before merging

- Confirm that every check on the pull request is green.
- Review the **Files changed** tab for accidental edits.
- Open external links and verify new publication metadata.
- Check the mobile and desktop layouts when changing images or page structure.
- Keep the pull request as a draft until the content is ready to publish.

## Privacy

Review all files before merging. Do not commit phone numbers, private email addresses, reference contact details, unpublished confidential work, or an unsanitized CV.
