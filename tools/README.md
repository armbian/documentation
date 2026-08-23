Tools for documentation creation go here

`mkArmbianDocs.py` - generates a mkdocs.yml file based on the contents of docs folder

`build-software-nav.py` - regenerates the software section of the mkdocs.yml nav

`generate-release-index.py` - regenerates `docs/releases/index.md` from the release
pages beside it. Run it after adding a release page by hand; the quarterly digest
workflow in `armbian/armbian.github.io` runs it automatically when it publishes one.
