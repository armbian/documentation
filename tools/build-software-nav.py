#!/usr/bin/env python3
# Rebuild the "ARMBIAN SOFTWARE" nav in mkdocs.yml so each category is a section
# (its hub page as the section index, via navigation.indexes) with the per-app
# pages nested beneath it. App pages and their `category:` come from the configng
# generator (docs/software/<slug>.md); this only groups them for the left nav —
# the /software/<slug>/ URLs are unaffected.
#
# Idempotent: rewrites only the region between the BEGIN/END markers. Category
# labels + order are curated here (rarely change); a new category needs one line.
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MKDOCS = ROOT / "mkdocs.yml"
APPS_DIR = ROOT / "docs" / "software"
HUB_DIR = "User-Guide_Armbian-Software"

BEGIN = "# BEGIN software-nav"
END = "# END software-nav"
IND = " " * 8   # category entries sit 8 spaces in, under 'ARMBIAN SOFTWARE'

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
    """Return (title, category) from a page's YAML front-matter, or (None, None)."""
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None, None
    fm = m.group(1)
    title = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
    cat = re.search(r'^category:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
    return (title.group(1) if title else None,
            cat.group(1) if cat else None)


def collect_apps():
    """category_id -> sorted list of (title, slug)."""
    by_cat = {}
    for md in sorted(APPS_DIR.glob("*.md")):
        title, cat = read_front_matter(md)
        if not title or not cat:
            continue
        by_cat.setdefault(cat, []).append((title, md.stem))
    for cat in by_cat:
        by_cat[cat].sort(key=lambda t: t[0].lower())
    return by_cat


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
        # (kept for SEO / the old URL) is intentionally NOT listed here — it is
        # redundant with the app list and is marked not_in_nav in mkdocs.yml.
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


def main():
    text = MKDOCS.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        sys.exit(f"markers {BEGIN!r}/{END!r} not found in {MKDOCS}")
    by_cat = collect_apps()
    if not by_cat:
        # No per-app pages present (e.g. the configng generator that emits
        # docs/software/<slug>.md with title/category hasn't run/synced yet).
        # Leave the existing nav block untouched rather than blanking it.
        print(f"software-nav: no app pages found under {APPS_DIR} — nav left unchanged.")
        return
    block = build_block(by_cat)
    new = re.sub(
        rf"({re.escape(IND)}{re.escape(BEGIN)}[^\n]*\n).*?(\n{re.escape(IND)}{re.escape(END)})",
        lambda m: m.group(1) + block + m.group(2),
        text, count=1, flags=re.DOTALL)
    MKDOCS.write_text(new, encoding="utf-8")
    total = sum(len(v) for v in by_cat.values())
    print(f"software-nav: {total} app pages grouped under {len(CATEGORIES)} categories.")


if __name__ == "__main__":
    main()
