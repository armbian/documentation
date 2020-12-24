#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Created by Lane Jennison on 2016-02-05.
"""

import sys,os
import fnmatch
import re
from collections import defaultdict
import logging as log
import jinja2
from jinja2 import Template, BaseLoader, Environment



def parse_arguments():
    """ Arguments parsing function. """
    import argparse
    parser = argparse.ArgumentParser(description='generate mkdocs.yml based on file naming covention: [ParentCategory]-Subtopic.md')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    parser.add_argument('-i', '--indir', metavar='INPUT_DIRECTORY', default='./docs', help='directory containing markdown files [default: ./docs]')
    parser.add_argument('-o', '--outdir', metavar='OUTPUT_DIRECTORY', default='./', help='directory to store mkdocs.yml [default: ./]')

    return parser.parse_args()

#locate markdown files in path and return list
def findFiles(indir):

    assert os.path.isdir(indir), "Provided directory path is not a directory"

    validFileList = list()

    log.info("looking for files in %s", indir)
    #find markdown files
    for file in os.listdir(indir):
        if os.path.isdir(os.path.join(indir,file)):
            log.info("%s is a directory, skipping", file)
        elif fnmatch.fnmatch(file,'*.md'):
            log.info("adding %s as markdown file", file)
            validFileList.append(file)

    return validFileList

#verify file is markdown and split file name to Parent and Child topics
def parseFiles(validFileList, indir):

    assert validFileList, "No valid markdown files to parse"
    assert os.path.isdir(indir), "Provided directory path is not a directory"

    parsedFileList = dict()
    tocTree = defaultdict(set)
    tocRegex = re.compile(r"(?P<parent>[\w-]+?(?=_))_(?P<child>[\w-].*(?=\.md))")
##FIXME add Try catch or finaly
    for file in sorted(validFileList):
        filepath = os.path.join(indir,file)
        log.info("trying to match %s ", file )
        tocResult = tocRegex.search(file)
        if tocResult:
            #convert hypens to space for Parent topic name
            tocParent = tocResult.group('parent').replace("-", " ", 3)
            #convert hypens to space for Child topic name
            tocChild = tocResult.group('child').replace("-", " ", 3)
            tocPair = (tocChild, file)
            tocTree[tocParent].add(tocPair)
            log.info("added %s %s %s", tocParent, tocChild, file)

    log.info(tocTree)
    return tocTree

#generte  mkdocs.yml using jinja template and dict of markdown files
def generateSite(parsedFileList):

    mkdocsTemplate = """

site_name: Armbian Documentation WIP

repo_url: https://github.com/armbian/documentation
repo_name: Github

site_author: "Armbian team"

theme: readthedocs

markdown_extensions:
  - smarty
  - footnotes
  - toc:
      permalink: True

pages:
  - Home: index.md
{% for tocParent in tocDict.keys() %}  - '{{ tocParent }}' :
    {% for title, file in dict.fromkeys(tocDict[tocParent]) %}    - '{{ title }}' : '{{ file }}'
    {% endfor %}
{% endfor %}

"""
    template = Template(mkdocsTemplate)
    return template.render(tocDict=parsedFileList)

def writeSiteFile(content,outdir):
    assert os.path.isdir(outdir), "Provided output directory path is not a directory"

    file = "mkdocs.yml"
    filepath = os.path.join(outdir,file)
    fp = open(filepath,'w')

    fp.write(content)
    fp.close()
    log.info("%s generated", file)

def main():
    """ Main function. """
    args = parse_arguments()

    if args.verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    log.info("mkArmbianDocs version 0.100002, created by Lane Jennison.")

    indir = args.indir
    outdir = args.outdir

    writeSiteFile(generateSite(parseFiles(findFiles(indir),indir)),outdir)


if __name__ == "__main__":
    main()
