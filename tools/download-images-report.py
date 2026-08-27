#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-2.0
#
# Report on the images we actually provide for download, from the source of
# truth armbian-images.json, and surface anomalies. Output is GitHub-flavoured
# Markdown written to $GITHUB_STEP_SUMMARY (and stdout).
#
# Channels (download_repository) -- what each actually is:
#   archive       -> the per-board DOWNLOAD on dl.armbian.com/<board>/archive/
#                    (all released versions per board). THIS is "the download".
#   distribution  -> appliance images on github.com/armbian/distribution
#                    (kali / omv / homeassistant), a separate product.
#   community     -> community nightly (github.com/armbian/os or community).
#   ci            -> CI nightly (github.com/armbian/ci).
#
# Anomalies reported (checks 1-3 are scoped to the real download = archive;
# check 4 scans all channels, since a desktop image for a no-video board is an
# anomaly wherever it is published):
#   1. Outdated boards        - newest download release behind the current line.
#   2. Non-standard on download- csc/wip/tvb boards on the per-board download.
#   3. Supported not on download- conf boards with NO per-board download image.
#   4. Desktop w/o video      - desktop-variant images (any channel) for boards
#                               whose inventory BOARD_HAS_VIDEO is false.

import argparse
import collections
import datetime as dt
import json
import os
import re
import sys
import urllib.request

IMAGES_URL = "https://github.armbian.com/armbian-images.json"
INFO_URL = "https://github.armbian.com/image-info.json"

# The real per-board download (dl.armbian.com). Named "archive" in the JSON.
DOWNLOAD_REPO = "archive"
# human labels for the overview (also documents what each channel really is)
REPO_LABELS = {
    "archive": "Download (dl.armbian.com, per-board releases)",
    "distribution": "Appliance images (kali/omv/homeassistant)",
    "community": "Community nightly",
    "ci": "CI nightly",
    "": "(orphaned — no repo)",
}
# variants that are NOT a desktop
NON_DESKTOP_VARIANTS = {"minimal", "cli", "server", ""}


def load(src, what):
    try:
        if re.match(r"^https?://", src):
            with urllib.request.urlopen(src, timeout=60) as r:
                return json.load(r)
        with open(src) as f:
            return json.load(f)
    except Exception as e:
        print(f"::warning::could not load {what} from {src}: {e}", file=sys.stderr)
        return None


def rel_key(v):
    """(major, minor, patch) for a X.Y.Z RELEASE; (0,0,0) for nightly/unknown.
    Used for release-line logic (nightly must not count as a release)."""
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)$", str(v or ""))
    return tuple(int(x) for x in m.groups()) if m else (0, 0, 0)


def version_sort_key(v):
    """Total order for display sorting: handles X.Y.Z and X.Y.Z-trunk.N
    (a release sorts above the same-numbered trunk build)."""
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)(?:-trunk\.(\d+))?$", str(v or ""))
    if not m:
        return (0, 0, 0, 0, str(v))
    maj, mnr, pat, trunk = m.groups()
    return (int(maj), int(mnr), int(pat), int(trunk) if trunk is not None else 10 ** 9, "")


# tz-aware sentinel so assets with an unparseable file_date still compare
MIN_DT = dt.datetime.min.replace(tzinfo=dt.timezone.utc)


def parse_date(s):
    """Parse an ISO timestamp to a tz-aware UTC datetime (or None). Always
    returns aware so it can be compared/subtracted against `now`/MIN_DT."""
    try:
        d = dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        d = d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
        return d.astimezone(dt.timezone.utc)  # normalize any offset to UTC
    except Exception:
        return None


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    # leading blank line so the table is always separated from the heading/prose
    # above it (Markdown needs it to render, and it keeps MD058 happy)
    return "\n" + "\n".join(out)


def build_video_map(info):
    vid = {}
    if not info:
        return vid
    entries = info["assets"] if isinstance(info, dict) and "assets" in info else info
    for e in entries:
        inv = (e.get("in") or {}).get("inventory") or {}
        b, hv = inv.get("BOARD"), inv.get("BOARD_HAS_VIDEO")
        if b is not None and hv is not None:
            vid[b] = bool(hv)
    return vid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", default=IMAGES_URL, help="armbian-images.json URL or local path")
    ap.add_argument("--image-info", default=INFO_URL, help="image-info.json URL or local path (BOARD_HAS_VIDEO map)")
    ap.add_argument("--top", type=int, default=80, help="max rows in the outdated table")
    args = ap.parse_args()

    data = load(args.images, "armbian-images.json")
    if not data:
        print("::error::armbian-images.json unavailable; cannot report", file=sys.stderr)
        return 1
    assets = data["assets"] if isinstance(data, dict) and "assets" in data else data
    video = build_video_map(load(args.image_info, "image-info.json"))

    now = dt.datetime.now(dt.timezone.utc)
    all_boards = {a["board_slug"] for a in assets}
    board_support = {a["board_slug"]: a.get("board_support", "?") for a in assets}
    board_name = {a["board_slug"]: a.get("board_name", a["board_slug"]) for a in assets}

    # per-board newest RELEASE on the download channel
    dl_newest = {}      # board -> (rel_key, version, date)
    for a in assets:
        if a.get("download_repository") != DOWNLOAD_REPO:
            continue
        v = a.get("armbian_version", "")
        k = rel_key(v)
        d = parse_date(a.get("file_date"))
        cur = dl_newest.get(a["board_slug"])
        # keep the highest release; within the same release keep the newest date
        if cur is None or (k, d or MIN_DT) > (cur[0], cur[2] or MIN_DT):
            dl_newest[a["board_slug"]] = (k, v, d)

    # current release line = highest (major, minor) among real RELEASES on the
    # download (ignore any non-release/nightly entry, rel_key (0,0,0)).
    current_line = max((k[:2] for k, _, _ in dl_newest.values() if k != (0, 0, 0)), default=(0, 0))
    current_examples = sorted({v for k, v, _ in dl_newest.values()
                               if k != (0, 0, 0) and k[:2] == current_line},
                              key=version_sort_key, reverse=True)
    current_str = "/".join(current_examples[:3]) or "n/a"

    out = [""]
    out.append("## Download images report")
    out.append("")
    out.append(f"_Source: `{args.images}` — {len(assets)} image assets across "
               f"{len(all_boards)} boards, generated {now:%Y-%m-%d %H:%M UTC}._\n")

    # ---- overview ----
    by_repo = collections.Counter(a.get("download_repository", "") for a in assets)
    repo_versions = collections.defaultdict(set)
    repo_boards = collections.defaultdict(set)
    for a in assets:
        r = a.get("download_repository", "")
        repo_versions[r].add(a.get("armbian_version", ""))
        repo_boards[r].add(a["board_slug"])
    out.append("## Overview")
    out.append(md_table(
        ["channel", "images", "boards", "version(s)"],
        [[REPO_LABELS.get(r, r or "(empty)"), n, len(repo_boards[r]),
          ", ".join(sorted(repo_versions[r], key=version_sort_key)) if len(repo_versions[r]) <= 3
          else f"{len(repo_versions[r])} versions (…{sorted(repo_versions[r], key=version_sort_key)[-1]})"]
         for r, n in by_repo.most_common()]))
    out.append(f"\nCurrent download release line: **{current_str}**.")
    out.append("")

    # ---- CHECK 1: outdated boards on the download ----
    outdated = []
    for b, (k, v, d) in dl_newest.items():
        if k == (0, 0, 0):        # non-release (nightly/unknown) on the download; skip
            continue
        if k[:2] < current_line:  # behind the current major.minor line
            age = (now - d).days if d else None
            outdated.append((current_line[0]*100 + current_line[1] - (k[0]*100 + k[1]),  # minors behind
                             b, board_support.get(b, "?"), v, d.strftime("%Y-%m-%d") if d else "?", age))
    outdated.sort(key=lambda t: (-t[0], t[3]))
    if outdated:
        out.append("## Outdated boards")
        out.append("")
        out.append(f"_**{len(outdated)}** boards whose newest `dl.armbian.com` image is behind "
                   f"the current {current_str} line._")
        rows = [[b, f"`{s}`", v, d, f"{age} d" if age is not None else "?"]
                for _, b, s, v, d, age in outdated[:args.top]]
        out.append(md_table(["board", "support", "newest download version", "date", "age"], rows))
        if len(outdated) > args.top:
            out.append(f"\n_…and {len(outdated) - args.top} more._")
        out.append("")

    # ---- CHECK 2: non-standard boards on the download ----
    nonconf = collections.defaultdict(set)
    for a in assets:
        if a.get("download_repository") == DOWNLOAD_REPO and a.get("board_support") != "conf":
            nonconf[a["board_slug"]].add(a.get("board_support", "?"))
    if nonconf:
        out.append("## Non-standard boards")
        out.append("")
        out.append(f"_**{len(nonconf)}** `csc`/`wip`/`tvb` boards with images on "
                   f"`dl.armbian.com` (the main per-board download)._")
        rows = [[b, f"`{'/'.join(sorted(s))}`", dl_newest.get(b, (0, '?', 0))[1], board_name.get(b, b)]
                for b, s in sorted(nonconf.items())]
        out.append(md_table(["board", "support", "newest version", "name"], rows))
        out.append("")

    # ---- CHECK 3: supported boards with no download image ----
    conf_boards = {b for b, s in board_support.items() if s == "conf"}
    on_download = set(dl_newest)
    missing = sorted(conf_boards - on_download)
    if missing:
        out.append("## Missing download images")
        out.append("")
        out.append(f"_**{len(missing)}** `conf` (standard-support) boards absent from "
                   f"`dl.armbian.com` — only nightly/appliance, or nowhere._")
        rows = []
        for b in missing:
            where = sorted({a.get("download_repository", "") for a in assets
                            if a["board_slug"] == b and a.get("download_repository") != DOWNLOAD_REPO})
            rows.append([b, board_name.get(b, b),
                         ", ".join(("orphaned" if r == "" else REPO_LABELS.get(r, r).split(" ")[0]) for r in where) or "—"])
        out.append(md_table(["board", "name", "present in"], rows))
        out.append("")

    # ---- CHECK 4: desktop images for no-video boards ----
    novideo = collections.defaultdict(set)
    for a in assets:
        b = a["board_slug"]
        if a.get("variant") not in NON_DESKTOP_VARIANTS and video.get(b) is False:
            novideo[b].add(f"{a.get('variant')}·{a.get('branch')}·{a.get('download_repository') or '?'}")
    if novideo:
        out.append("## Desktop images without video")
        out.append("")
        out.append(f"_**{len(novideo)}** boards whose inventory reports no video output "
                   f"yet have a desktop-variant image._")
        out.append(md_table(["board", "name", "desktop images (variant·branch·channel)"],
                            [[b, board_name.get(b, b), ", ".join(sorted(s))] for b, s in sorted(novideo.items())]))
        out.append("")

    report = "\n".join(out)
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write(report + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
