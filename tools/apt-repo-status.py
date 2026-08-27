#!/usr/bin/env python3
"""Generate a Markdown status report for the apt.armbian.com repository.

Runs locally, downloads the repository indices and prints Markdown to stdout
(or --output FILE) that can be pasted / spliced into the documentation.

Examples:
    tools/apt-repo-status.py                 # arm64, component main, all suites
    tools/apt-repo-status.py --arch amd64
    tools/apt-repo-status.py --suites bookworm trixie noble --output status.md
"""
import argparse
import gzip
import io
import re
import sys
import urllib.request
from datetime import datetime, timezone

DEFAULT_BASE = "https://apt.armbian.com"

# Active / supported suites shown by default (override with --suites, or --all).
DEFAULT_SUITES = ["bookworm", "trixie", "sid", "jammy", "noble"]

# Armbian's own non board-specific packages (component `main`).
CORE_PACKAGES = [
    "armbian-firmware",
    "armbian-firmware-full",
    "armbian-zsh",
    "armbian-plymouth-theme",
]
# Kernel branches to summarise (in display order); anything else is "other".
KERNEL_BRANCHES = ["current", "edge", "legacy", "vendor"]


def util_family(name):
    """Fold split/variant util packages into one representative family row."""
    if name.startswith("zulu"):
        return re.match(r"(zulu\d+)", name).group(1) + " (JDK)"
    if re.match(r"^(zfs|libzfs|libzpool|libnvpair|libuutil)", name):
        return "zfs (OpenZFS)"
    if name.startswith("libraspberrypi"):
        return "libraspberrypi"
    if name.startswith("python3-libcamera"):
        return "libcamera"
    return name


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "armbian-apt-status/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


# --- Debian version comparison -------------------------------------------------
try:
    import apt_pkg
    apt_pkg.init_system()

    def version_gt(a, b):
        return apt_pkg.version_compare(a, b) > 0
except Exception:
    def _split(v):
        # crude but serviceable fallback: split into numeric / non-numeric runs
        import re
        parts = re.findall(r"\d+|\D+", v)
        key = []
        for p in parts:
            key.append((0, int(p)) if p.isdigit() else (1, p))
        return key

    def version_gt(a, b):
        return _split(a) > _split(b)


def version_max(versions):
    best = None
    for v in versions:
        if best is None or version_gt(v, best):
            best = v
    return best


# --- Repository access ---------------------------------------------------------
def discover_suites(base):
    try:
        html = fetch(base + "/dists/").decode("utf-8", "replace")
    except Exception:
        return []
    import re
    out = []
    for m in re.findall(r'href="([^"?/]+)/"', html):
        if m not in ("..", ".") and m not in out:
            out.append(m)
    return out


def get_release(base, suite):
    try:
        text = fetch(f"{base}/dists/{suite}/Release").decode("utf-8", "replace")
    except Exception:
        return {}
    fields = {}
    for line in text.splitlines():
        if line and not line[0].isspace() and ":" in line:
            k, _, v = line.partition(":")
            fields[k.strip()] = v.strip()
    return fields


def get_packages(base, suite, component, arch):
    """Return list of {Package, Version, Architecture, Section} stanzas."""
    url = f"{base}/dists/{suite}/{component}/binary-{arch}/Packages.gz"
    try:
        raw = fetch(url)
    except Exception:
        return None
    data = gzip.GzipFile(fileobj=io.BytesIO(raw)).read().decode("utf-8", "replace")
    stanzas = []
    cur = {}
    for line in data.splitlines():
        if not line.strip():
            if cur:
                stanzas.append(cur)
                cur = {}
            continue
        if line[0].isspace() or ":" not in line:
            continue
        k, _, v = line.partition(":")
        cur[k.strip()] = v.strip()
    if cur:
        stanzas.append(cur)
    return stanzas


# --- Report --------------------------------------------------------------------
def build_report(base, suites, component, arch, kernels=False):
    out = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out.append("## Armbian apt repository status")
    out.append("")
    out.append(f"_Generated {now} from [`{base}`]({base}) "
               f"— component `{component}`, architecture `{arch}`._")
    out.append("")

    def latest_map(stanzas):
        latest = {}
        for st in stanzas or []:
            name, ver = st.get("Package"), st.get("Version")
            if not name or not ver:
                continue
            if name not in latest or version_gt(ver, latest[name]):
                latest[name] = ver
        return latest

    suite_data = {}
    for suite in suites:
        rel = get_release(base, suite)
        pkgs = get_packages(base, suite, component, arch)
        if pkgs is None:
            continue
        latest = latest_map(pkgs)
        # 3rd-party / utility tools live in the suite-prefixed "-utils" component.
        utils = latest_map(get_packages(base, suite, f"{suite}-utils", arch))
        suite_data[suite] = {"release": rel, "latest": latest,
                             "count": len(latest), "utils": utils}

    # --- Suite overview
    out.append("### Suites")
    out.append("")
    out.append("| Suite | Codename | Updated | Packages | Latest Armbian version |")
    out.append("|:------|:---------|:--------|--------:|:----------------------|")
    for suite in suites:
        d = suite_data.get(suite)
        if not d:
            continue
        rel = d["release"]
        updated = rel.get("Date", "—")[:16]
        newest = version_max(d["latest"].values()) or "—"
        out.append(f"| `{suite}` | {rel.get('Codename', suite)} | {updated} "
                   f"| {d['count']} | `{newest}` |")
    out.append("")

    active = [s for s in suites if s in suite_data]

    # Armbian's `main` content is identical across suites, so merge it into a
    # single view (newest version seen for each package across all suites).
    merged = {}
    for suite in active:
        for name, ver in suite_data[suite]["latest"].items():
            if name not in merged or version_gt(ver, merged[name]):
                merged[name] = ver

    # --- Core packages (single column — same across every suite)
    out.append("### Core package versions")
    out.append("")
    out.append("Armbian's own base packages (component `main`) — identical across all suites.")
    out.append("")
    out.append("| Package | Version |")
    out.append("|:--------|:--------|")
    for pkg in CORE_PACKAGES:
        v = merged.get(pkg)
        out.append(f"| `{pkg}` | {('`'+v+'`') if v else '—'} |")
    out.append("")

    # --- Kernel branches (distinct families + newest version per branch)
    out.append("### Kernel branches")
    out.append("")
    out.append("Distinct kernel families and the newest Armbian version published "
               "per branch (from `linux-image-<branch>-*`).")
    out.append("")
    out.append("| Branch | Families | Latest version |")
    out.append("|:-------|--------:|:--------------|")
    for branch in KERNEL_BRANCHES:
        fams, vers = set(), []
        for name, ver in merged.items():
            if name.startswith(f"linux-image-{branch}-"):
                fams.add(name)
                vers.append(ver)
        if fams:
            out.append(f"| {branch} | {len(fams)} | `{version_max(vers)}` |")
        else:
            out.append(f"| {branch} | 0 | — |")
    out.append("")

    # --- Per-family kernel drift (opt-in): every family, newest version, and
    #     whether it lags the current release. Answers "which kernels drift".
    if kernels:
        fam_latest = {n: v for n, v in merged.items() if n.startswith("linux-image-")}
        ref = version_max(fam_latest.values())
        rows = []
        for name, ver in fam_latest.items():
            parts = name.split("-")           # linux-image-<branch>-<family...>
            branch = parts[2] if len(parts) > 2 else "?"
            family = "-".join(parts[3:]) if len(parts) > 3 else "?"
            rows.append((version_gt(ref, ver), branch, family, ver))
        n_behind = sum(1 for r in rows if r[0])
        out.append("### Kernel families")
        out.append("")
        out.append(f"Newest version published per kernel family. The current release "
                   f"line is `{ref}`; families below it were not rebuilt for it.")
        out.append("")
        out.append(f"**{n_behind} of {len(rows)} families behind `{ref}`.**")
        out.append("")
        out.append("| Branch | Family | Version | Status |")
        out.append("|:-------|:-------|:--------|:-------|")
        # behind families first (most useful), then by branch and family name
        for behind, branch, family, ver in sorted(rows, key=lambda r: (not r[0], r[1], r[2])):
            status = f"⚠️ behind `{ref}`" if behind else "✅ current"
            out.append(f"| {branch} | `{family}` | `{ver}` | {status} |")
        out.append("")

    # --- Third-party / utility packages (the "-utils" component), per suite,
    #     with split/variant packages folded into one family row.
    out.append("### Third-party & utility packages")
    out.append("")
    out.append("Upstream tools imported per suite (component `<suite>-utils`); "
               "split families (JDK, OpenZFS, ...) are folded to their newest member, "
               "and `-dbgsym` debug packages omitted.")
    out.append("")
    # family -> {suite -> newest version among that family's members}
    fam_versions = {}
    for suite in active:
        for name, ver in suite_data[suite]["utils"].items():
            if name.endswith("-dbgsym"):
                continue
            fam = util_family(name)
            cur = fam_versions.setdefault(fam, {}).get(suite)
            if cur is None or version_gt(ver, cur):
                fam_versions[fam][suite] = ver
    out.append("| Package | " + " | ".join(f"`{s}`" for s in active) + " |")
    out.append("|:--------|" + "|".join(":-:" for _ in active) + "|")
    for fam in sorted(fam_versions):
        row = [f"| `{fam}` " if "(" not in fam else f"| {fam} "]
        for suite in active:
            v = fam_versions[fam].get(suite)
            row.append(f"| {('`'+v+'`') if v else '—'} ")
        out.append("".join(row) + "|")
    out.append("")

    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-url", default=DEFAULT_BASE)
    ap.add_argument("--suites", nargs="*",
                    help=f"suites to include (default: {' '.join(DEFAULT_SUITES)})")
    ap.add_argument("--all", action="store_true",
                    help="include every suite present in the repository")
    ap.add_argument("--arch", default="arm64")
    ap.add_argument("--component", default="main")
    ap.add_argument("--kernels", action="store_true",
                    help="add a per-family kernel table flagging versions that lag the release")
    ap.add_argument("--output", help="write Markdown here (default: stdout)")
    args = ap.parse_args()

    if args.suites:
        suites = args.suites
    elif args.all:
        suites = discover_suites(args.base_url)
    else:
        suites = DEFAULT_SUITES
    if not suites:
        sys.exit("no suites found (network issue?)")

    report = build_report(args.base_url, suites, args.component, args.arch,
                          kernels=args.kernels)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(report + "\n")
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()
