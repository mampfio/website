# Mampfio website

A German placeholder page for mampfio.de, using the original [Mampfio design system](https://design.mampfio.de/). Plain HTML and CSS, with locally hosted fonts and logos. No dependencies or build step.

## Preview

Run from the repository root:

```sh
python3 -m http.server 8000 --directory site
```

Open [localhost:8000](http://localhost:8000).

## Deploy to GitHub Pages

1. In the repository's **Settings → Pages**, set **Source** to **GitHub Actions**.
2. Push these files to `main`. The included workflow checks and deploys `site/`.
3. Open the URL shown by the **Deploy to GitHub Pages** workflow.

All asset paths are relative, so the page works at both a project URL such as `https://mampfio.github.io/website/` and a custom domain. To use `mampfio.de`, configure the custom domain in GitHub Pages and its DNS records separately.

The deployment follows [GitHub's static-site workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Check

```sh
python3 scripts/check_site.py
```

## Design assets

The unmodified CSS tokens, logos, and Latin-subset fonts in `site/assets/design-system/` come from `https://design.mampfio.de/webjar/` (retrieved 6 November 2026). The page uses the lightweight tokens stylesheet rather than Bootstrap. The illustration follows the geometric composition in the brand book's cover; the original logo is unmodified.

Baloo 2 and Nunito Sans are distributed under the SIL Open Font License. Their licence files are included in `site/assets/design-system/licenses/`.

The locally hosted primer cover in `site/assets/scs-primer-cover.jpg` is the official image from [INNOQ's Self-contained Systems primer page](https://www.innoq.com/de/books/self-contained-systems/).
