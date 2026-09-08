#!/usr/bin/env python3
# Rebuild the "ARMBIAN SOFTWARE" nav in mkdocs.yml so each category is a section
# with its per-app pages nested beneath it. App pages and their `category:` come
# from the configng generator (docs/software/<slug>.md); this only groups them
# for the left nav — the /software/<slug>/ URLs are unaffected.
#
# The generator also emits one hub page per category (`hub: true` front-matter,
# e.g. docs/software/web-hosting.md). Those stay out of the nav — their apps are
# already listed there — so this also refreshes the `not_in_nav` list that keeps
# `mkdocs build --strict` quiet about them.
#
# Idempotent: rewrites only the regions between the BEGIN/END markers. Category
# labels + order are curated here (rarely change); a new category needs one line.
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MKDOCS = ROOT / "mkdocs.yml"
APPS_DIR = ROOT / "docs" / "software"

BEGIN = "# BEGIN software-nav"
END = "# END software-nav"
IND = " " * 8   # category entries sit 8 spaces in, under 'ARMBIAN SOFTWARE'

HUB_BEGIN = "# BEGIN software-hubs"
HUB_END = "# END software-hubs"
HUB_IND = " " * 2   # not_in_nav is a block scalar indented 2 spaces

# Curated label + order, mapped to the category id used by the hub file name and
# the app pages' `category:` field.
CATEGORIES = [
    ("Armbian", "Armbian"),
    ("Backup", "Backup"),
    ("Containers", "Containers"),
    ("Database", "Database"),
    ("Development tools", "DevTools"),
    ("DNS blockers", "DNS"),
    ("Downloaders", "Downloaders"),
    ("Finance", "Finance"),
    ("Home automation", "HomeAutomation"),
    ("Management", "Management"),
    ("Media", "Media"),
    ("Monitoring", "Monitoring"),
    ("Netconfig", "Netconfig"),
    ("Printing", "Printing"),
    ("VPN", "VPN"),
    ("Web hosting", "WebHosting"),
]


def read_front_matter(md_path):
    """Return (title, category, is_hub) from a page's YAML front-matter."""
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None, None, False
    fm = m.group(1)
    title = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
    cat = re.search(r'^category:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
    hub = re.search(r'^hub:\s*true\s*$', fm, re.MULTILINE)
    return (title.group(1) if title else None,
            cat.group(1) if cat else None,
            bool(hub))


def collect_apps():
    """Return (category_id -> sorted [(title, slug)], sorted list of hub slugs)."""
    by_cat, hubs = {}, []
    for md in sorted(APPS_DIR.glob("*.md")):
        title, cat, is_hub = read_front_matter(md)
        if is_hub:
            hubs.append(md.stem)
            continue
        if not title or not cat:
            continue
        by_cat.setdefault(cat, []).append((title, md.stem))
    for cat in by_cat:
        by_cat[cat].sort(key=lambda t: t[0].lower())
    return by_cat, hubs


def yq(s):
    return "'" + s.replace("'", "''") + "'"


def build_block(by_cat):
    lines = []
    seen = set()
    for label, cat_id in CATEGORIES:
        seen.add(cat_id)
        apps = by_cat.get(cat_id, [])
        if not apps:
            # Defunct/phantom category (no app pages generated) — skip it, so a
            # category that was removed or merged upstream can't linger in the nav.
            continue
        # Category is a collapsible toggle with its apps under it. The hub page
        # (kept for SEO and as the app pages' back-link target) is intentionally
        # NOT listed here — it is redundant with the app list, and is written to
        # not_in_nav instead.
        lines.append(f"{IND}- {yq(label)}:")
        for title, slug in apps:
            lines.append(f"{IND}    - {yq(title)}: {yq(f'software/{slug}.md')}")
    # Any category with app pages but no curated label still gets rendered (with
    # a prettified id as the label) so new upstream categories never silently
    # vanish; warn so a nicer label can be added.
    for cat in sorted(set(by_cat) - seen):
        label = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', cat)
        print(f"::warning:: software-nav: category {cat!r} has app pages but no "
              f"curated label — using {label!r}; add one in tools/build-software-nav.py",
              file=sys.stderr)
        lines.append(f"{IND}- {yq(label)}:")
        for title, slug in by_cat[cat]:
            lines.append(f"{IND}    - {yq(title)}: {yq(f'software/{slug}.md')}")
    return "\n".join(lines)


def replace_region(text, begin, end, ind, block):
    """Swap the body between two marker lines, leaving the markers in place.
    Matches whole lines lazily, so an already-empty region is filled too."""
    pattern = (rf"({re.escape(ind)}{re.escape(begin)}[^\n]*\n)"
               rf"(?:.*\n)*?({re.escape(ind)}{re.escape(end)})")
    body = block + "\n" if block else ""
    return re.sub(pattern, lambda m: m.group(1) + body + m.group(2), text, count=1)


def main():
    text = MKDOCS.read_text(encoding="utf-8")
    for begin, end in ((BEGIN, END), (HUB_BEGIN, HUB_END)):
        if begin not in text or end not in text:
            sys.exit(f"markers {begin!r}/{end!r} not found in {MKDOCS}")
    by_cat, hubs = collect_apps()
    if not by_cat:
        # No per-app pages present (e.g. the configng generator that emits
        # docs/software/<slug>.md with title/category hasn't run/synced yet).
        # Leave the existing nav block untouched rather than blanking it.
        print(f"software-nav: no app pages found under {APPS_DIR} — nav left unchanged.")
        return
    text = replace_region(text, BEGIN, END, IND, build_block(by_cat))
    hub_block = "\n".join(f"{HUB_IND}/software/{slug}.md" for slug in sorted(hubs))
    text = replace_region(text, HUB_BEGIN, HUB_END, HUB_IND, hub_block)
    MKDOCS.write_text(text, encoding="utf-8")
    total = sum(len(v) for v in by_cat.values())
    print(f"software-nav: {total} app pages grouped under {len(CATEGORIES)} categories, "
          f"{len(hubs)} category hubs kept out of the nav.")


if __name__ == "__main__":
    main()
