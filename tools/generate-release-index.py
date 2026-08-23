#!/usr/bin/env python3
"""Regenerate docs/releases/index.md from the release pages beside it.

The release pages are written by the quarterly digest workflow in
armbian/armbian.github.io, one per quarter. This keeps the landing page in step
with them without anyone having to remember to edit it, and it is safe to run
repeatedly: the output depends only on the pages present.

Pages are named by quarter (MAJOR.MINOR), not by patch release, so every
patch inside a quarter rewrites one page instead of adding another.

Only the newest few releases get a full entry; older ones roll over to a
compact line as new releases publish, so the page stays short indefinitely.
They keep their own pages either way — those URLs are the only indexed copy of
a release note, since GitHub serves its release pages noindex, so retiring one
would throw away the reason these pages exist.
"""

import argparse
import os
import re
import sys

RE_FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
RE_RELEASED = re.compile(r"^\*Released ([^*]+)\*\s*$", re.MULTILINE)
RE_VERSION_FILE = re.compile(r"^(\d+)\.(\d+)(?:\.(\d+))?\.md$")

# Releases beyond this many roll over to the compact list.
FEATURED = 4

INDEX_DESCRIPTION = (
    "Release notes for every Armbian stable release, newest first: what "
    "changed, which boards moved support tier, and the full list of merged "
    "pull requests."
)


def parse_front_matter(text):
    """Read the title and description out of a page's YAML front matter.

    Deliberately not a YAML parser: the front matter these pages carry is two
    scalar fields, and the docs build has no YAML dependency of its own.
    """
    match = RE_FRONT_MATTER.match(text)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if not sep:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        fields[key.strip()] = value
    return fields


def collect(releases_dir):
    entries = []
    for name in sorted(os.listdir(releases_dir)):
        match = RE_VERSION_FILE.match(name)
        if not match:
            continue
        text = open(os.path.join(releases_dir, name), encoding="utf-8").read()
        fields = parse_front_matter(text)
        released = RE_RELEASED.search(text)
        version = name[: -len(".md")]
        entries.append(
            {
                "sort": tuple(int(p) for p in match.groups(default="0")),
                "version": version,
                "file": name,
                "title": fields.get("title") or "Armbian {}".format(version),
                "description": fields.get("description", ""),
                "released": released.group(1).strip() if released else "",
            }
        )
    entries.sort(key=lambda e: e["sort"], reverse=True)
    return entries


def render(entries, has_history, featured=FEATURED):
    out = [
        "---",
        "title: Armbian releases",
        'description: "{}"'.format(" ".join(INDEX_DESCRIPTION.split())),
        "---",
        "",
        "# Armbian releases",
        "",
        "Notes for each Armbian stable release, newest first. Each page carries "
        "the release summary, any board support-tier changes, and the full list "
        "of merged pull requests.",
        "",
    ]

    if not entries:
        out.append("_No release pages have been published yet._")
        out.append("")

    for entry in entries[:featured]:
        line = "* **[{title}]({file})**".format(**entry)
        if entry["released"]:
            line += " &mdash; {}".format(entry["released"])
        out.append(line)
        if entry["description"]:
            out.append("")
            out.append("    {}".format(entry["description"]))
            out.append("")

    older = entries[featured:]
    if older or has_history:
        out.append("")
        out.append("## Earlier releases")
        out.append("")

    for entry in older:
        line = "* [{title}]({file})".format(**entry)
        if entry["released"]:
            line += " &mdash; {}".format(entry["released"])
        out.append(line)
    if older:
        out.append("")

    if has_history:
        out.append(
            "Releases before 25.x are collected in the "
            "[release history](history.md) archive."
        )

    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs", help="path to the docs/ directory")
    ap.add_argument("--featured", type=int, default=FEATURED,
                    help="releases shown with a full entry (default: %(default)s)")
    args = ap.parse_args()

    releases_dir = os.path.join(args.docs, "releases")
    if not os.path.isdir(releases_dir):
        print("no {} directory; nothing to do".format(releases_dir), file=sys.stderr)
        return 1

    entries = collect(releases_dir)
    page = render(
        entries,
        os.path.exists(os.path.join(releases_dir, "history.md")),
        featured=args.featured,
    )
    with open(os.path.join(releases_dir, "index.md"), "w", encoding="utf-8") as fh:
        fh.write(page)

    print("wrote {}/index.md with {} release(s), {} featured".format(
        releases_dir, len(entries), min(len(entries), args.featured)))
    for position, entry in enumerate(entries):
        print("  {:<10} {:<20} {}".format(
            entry["version"], entry["released"],
            "featured" if position < args.featured else "earlier"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
