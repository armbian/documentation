# Armbian Documentation #

## Overview ##

Documentation is written in markdown and stored in the `docs/` subfolder.  Images go in `docs/images`

This repo is meant for storing and quick glances.  Official output is http://docs.armabian.com

Armbian Documentation is available in the following formats:
* mkdocs site http://docs.armbian.com
* PDF user guides \(in progress\)

Armbian Documentation relies on a file naming convention:

`_Parent Topic_Child-Topic-Name.md`

Please try to avoid creating new parent topics unless absoultely necesssary.

Current Parent Topics:

* Hardware
* Process
* Release
* Developer Guide
* User Guide
* Howto

### .gitignore ###
For easier testing and commits `.gitignore` is configured to ignore `site/`

`mkdocs.yml` should probably be added, but we can commit for now

## Tools ##

### mkArmbianDocs.py ###
generates mkdocs.yml file based on contents of `docs/`

* option paramters for input and output directories
* see `mkArmbianDocs.py -h` for help

### missing tools ###
* html2doc output to PDF user manual
* automated mkdocs deployment to http://docs.armbian.com

## generating ##
From the parent folder of the repo, run:

`tools/mkArmbianDocs.py && mkdocs build`

This will generate the mkdocs.yml configuration file and then generate the mkdocs site to the `site/` folder

## testing ##
To preview locally. Excute the preview server `mkdocs serve`

You will be able to make realtime edits to exist files.  If you add a new file, you will need to rerun `tools/mkArmbianDocs.py`
## Quick Start ##

```
pip install mkdocs
git clone git@github.com:igorpecovnik/lib.docs.git
#vim docs/[Parent Topic Example]-child-topic-example.md
#generate config, build, launch local preview server
tools/mkArmbianDocs.py && mkdocs build --clean && mkdocs serve
git add docs/*.md
git commit -m "added new howto on exampling"
git push
```
