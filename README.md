<h2 align="center">
  <a href=#><img src="https://raw.githubusercontent.com/armbian/.github/master/profile/logosmall.png" alt="Armbian logo"></a>
  <br><br>
</h2>

# Armbian Documentation

## Purpose of This Repository

This repository holds the source for the Armbian documentation site published at [docs.armbian.com](https://docs.armbian.com). It is the central knowledge base for the Armbian OS, the `armbian-config` utility, per-application software pages, and the Armbian build framework.

## Rendered output

The content in this repo is meant for storage and quick glances; the official rendered output is:

- Website: [https://docs.armbian.com](https://docs.armbian.com)
- Offline PDF: [Latest release](https://github.com/armbian/documentation/releases/latest)

## How it is built

The site is built with [MkDocs](https://github.com/mkdocs/mkdocs/) using the [Material for MkDocs](https://github.com/squidfunk/mkdocs-material) theme. Pages are written in Markdown and stored under `docs/`; images live under `docs/images/`. Site configuration is in `mkdocs.yml` and theme overrides in `overrides/`.

Automation is written in Python (`tools/`) and orchestrated with GitHub Actions workflows under `.github/workflows/`. A local convenience wrapper `serve-docs-local.sh` (Bash) reproduces the CI staging steps for offline preview.

## Repository layout

```text
docs/                  Markdown sources (organised by topic)
  images/              Images referenced by the docs
  build-framework/     Armbian build framework guide
  config/              armbian-config pages
  software/            Per-application SEO pages
  status/              Auto-generated status pages (mirrors, apt repo, etc.)
  releases/            Release notes and release model
overrides/             MkDocs Material theme overrides (main.html)
tools/                 Python helpers (see tools/README.md)
.github/workflows/     CI/automation
mkdocs.yml             Site configuration
requirements.txt       Python dependencies for building the site
serve-docs-local.sh    Local preview wrapper (Bash)
```

See [`.github/DOCUMENT_TEMPLATE.md`](.github/DOCUMENT_TEMPLATE.md) before writing new content.

## Contribute

You can contribute to Armbian Documentation directly on GitHub by editing files under [`docs/`](docs/) and opening a pull request. To enjoy a fully rendered local preview with proper styling and live reload, set up MkDocs locally as shown below.

### Prerequisites

Ensure Python and the necessary development packages are installed:

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv python3-dev
```

On Debian you may also need the following packages for `mkdocs-material`:

```bash
sudo apt-get install libcairo2 pango1.0-tools
```

### Clone the repository

```bash
git clone https://github.com/armbian/documentation
cd documentation
```

### Set up the environment

Set up a Python virtual environment to isolate the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --use-pep517 -r requirements.txt
```

### Build and serve locally

```bash
mkdocs build --clean
mkdocs serve -a 0.0.0.0:8000
```

Then open <http://localhost:8000>. The site reloads automatically when you edit `.md` files.

> 💡 Tip: use the local preview to verify formatting and layout before committing your changes.

### One-shot offline preview

The `serve-docs-local.sh` helper reproduces the CI "Pull from Armbian config" staging steps locally, generates the software pages from a sibling `armbian/configng` checkout, stages them into `docs/`, and serves the site:

```bash
./serve-docs-local.sh           # generate + stage + serve at http://127.0.0.1:8000
./serve-docs-local.sh build     # generate + stage + one-shot build into ./site
./serve-docs-local.sh clean     # revert staged generated pages
```

## Generator tools

After adding a new page, either hand-edit `mkdocs.yml`, or re-run `tools/mkArmbianDocs.py` **unless you are changing the structure of the `docs/` folder**.

```bash
python3 tools/mkArmbianDocs.py && mkdocs build
```

This regenerates `mkdocs.yml` from the current contents of `docs/` and publishes the built HTML to `site/`.

Additional helpers in `tools/` (see [`tools/README.md`](tools/README.md)):

- `build-software-nav.py` — regenerates the software section of the `mkdocs.yml` nav.
- `generate-release-index.py` — regenerates `docs/releases/index.md` from the release pages beside it.
- `apt-repo-status.py`, `build-machinery-status.py`, `download-images-report.py` — generate the auto-updated status pages under `docs/status/`.

## Continuous integration

Automation (PR previews, site release, status-page refreshes, label sync, mirror list pulls, extensions list pulls, etc.) is implemented as GitHub Actions workflows under `.github/workflows/`. For a live overview of all runs in this repository, see the Armbian CI dashboard:

- <https://actions.armbian.com/?repo=documentation>

## Community

- Website: <https://www.armbian.com>
- Documentation: <https://docs.armbian.com>
- Source: <https://github.com/armbian/documentation>

## License

This project is licensed under the GNU General Public License v3.0. See [`LICENSE`](LICENSE) for details.
