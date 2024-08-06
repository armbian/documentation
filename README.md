# Armbian Documentation

[![Create offline documentation to release](https://github.com/armbian/documentation/actions/workflows/release.yaml/badge.svg)](https://github.com/armbian/documentation/actions/workflows/release.yaml)

<p align="center">
  <a target="_blank" href="https://docs.armbian.com">
    <img alt="logo" src="./docs/images/logo.png">
  </a>
</p>

## Overview

Documentation is written in [markdown](https://www.markdownguide.org/basic-syntax/) and stored in the `docs/` subfolder.  Images go in `docs/images`.

This repo is meant for storing and quick glances.  Official output is [https://docs.armbian.com](https://docs.armbian.com).

Armbian Documentation is available in the following formats:

* [Official document website](https://docs.armbian.com),
* [PDF document](https://github.com/armbian/documentation/releases/latest)

## Contributing

This site is built with [mkdocs](https://github.com/mkdocs/mkdocs/) and depends on [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

Armbian Documentation naming of document files follows this rules:

`[Parent-Topic-Example]_[Child-Topic]-example.md`

`Parent-Topic-Name` and `Child-Topic-Name` are separated by an underscore `_`.  Hyphens `-` are automatically converted to space.

Please try to avoid creating new parent topics unless absolutely necessary.

Current Parent Topics:

* User Guide
* Hardware notes
* Developer Guide
* Contributor Process
* Release management
* Community

See the [document template](.github/DOCUMENT_TEMPLATE.md) before you writing any content.

## Working on the content

### Prerequisites

Ensure you have Python and the necessary development packages installed:

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv python3.11-dev
```
### Cloning the Repository

Next, clone the Armbian documentation repository:

```bash
git clone https://github.com/armbian/documentation
cd documentation
```

### Setting Up the Environment

Set up a Python virtual environment to isolate the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --use-pep517 -r requirements.txt
```

### Building and Serving the Documentation

To build and serve the documentation locally, allowing you to make edits and observe the results in real time, use:

```bash
mkdocs build --clean && mkdocs serve
```

You will be able to make edits to existing files and observe the results in real time.

## Generate tools
After adding a new file, either hand-edit `mkdocs.yml`, or re-run `tools/mkArmbianDocs.py` **unless making changes to the structure of the `docs/` folder**. (See below)

### mkArmbianDocs.py
Generate `mkdocs.yml` based on the contents of `docs/` folder

* Command-line options for input and output directories
* Requires install requirement
* You don't need to run it every time unless making changes to the structure of the `docs/` folder
* See `mkArmbianDocs.py -h` for help

From the parent folder of the repo, run:

`python3 tools/mkArmbianDocs.py && mkdocs build`

This will generate the `mkdocs.yml` and publish built HTML to the `site/` folder.
