#!/usr/bin/env python3
"""Generate a Markdown status report for the Armbian build machinery — the
build servers — from NetBox, with the live runner count from GitHub.

Reads the build servers (NetBox VMs with role=userlevel-runner) and reports
each server's location, CPU thread count and memory, plus the fleet totals
(the CPU-thread capacity). The number of GitHub runner processes on each
server is read from GitHub by matching the server name to a runner label.

It can also list the org's GitHub Actions self-hosted runners grouped by
label (keyword), when a token with the runners permission is available.

Environment:
    NETBOX_TOKEN       required — a read-only NetBox API token
    NETBOX_API         NetBox API base (default https://netbox.armbian.com/api)
    GH_RUNNERS_TOKEN   optional — GitHub token with admin:org (or the
                       fine-grained "self-hosted runners" org permission);
                       falls back to GITHUB_TOKEN. When absent, the GitHub
                       section is skipped.
    GH_ORG             GitHub org for the runner listing (default: armbian)

Prints Markdown to stdout (or --output FILE).
"""
import argparse
import collections
import json
import os
import sys
import urllib.request

DEFAULT_API = "https://netbox.armbian.com/api"
ROLE = "userlevel-runner"
DEFAULT_ORG = "armbian"
# GitHub-assigned default labels; the runner's own name comes from what's left.
GH_DEFAULT_LABELS = {"self-hosted", "linux", "macos", "windows",
                     "x64", "x86", "arm", "arm64"}


def netbox_get(api, token, path):
    """GET an API path, following pagination, returning all results."""
    results = []
    url = f"{api}{path}"
    while url:
        req = urllib.request.Request(url, headers={
            "Authorization": f"Token {token}",
            "Accept": "application/json",
        })
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
        results.extend(data.get("results", []))
        url = data.get("next")
    return results


def gb(mb):
    return round((mb or 0) / 1024)


def github_runners(org, token):
    """All self-hosted runners registered to the org (needs admin:org / the
    runners permission). Returns [] and re-raises nothing on failure."""
    runners, page = [], 1
    while True:
        url = f"https://api.github.com/orgs/{org}/actions/runners?per_page=100&page={page}"
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        })
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
        batch = data.get("runners", [])
        runners.extend(batch)
        if not batch or len(runners) >= data.get("total_count", 0):
            break
        page += 1
    return runners


def github_runner_counts(org, token):
    """Map a machine name (via its runner label) to the number of registered
    GitHub runners carrying it. Returns None when the org runners can't be read
    (no/insufficient token), so the caller can leave the column blank.

    A machine hosts one or more runner processes, each registered with the
    machine's name as a label; counting runners per label gives runners-per-machine.
    """
    try:
        runners = github_runners(org, token)
    except Exception as e:
        print(f"::warning::GitHub runners unavailable: {e}", file=sys.stderr)
        return None
    per_label = collections.Counter()
    for r in runners:
        for lbl in r.get("labels", []):
            name = lbl["name"].lower()
            if name not in GH_DEFAULT_LABELS:
                per_label[name] += 1
    online = sum(1 for r in runners if r.get("status") == "online")
    return {"labels": per_label, "total": len(runners), "online": online}


def build_report(api, token, gh_org=None, gh_token=None):
    vms = netbox_get(api, token, f"/virtualization/virtual-machines/?role={ROLE}&limit=500")
    rows = []
    for v in vms:
        loc = (v.get("site") or {}).get("name") or (v.get("cluster") or {}).get("name") or "—"
        cf = v.get("custom_fields") or {}
        rows.append({
            "name": v["name"],
            # the GitHub runners label lives in a NetBox custom field; it is the
            # server's display name here and the key to count runners on GitHub
            "label": cf.get("github_label"),
            # NetBox's stored runner count, used when GitHub can't be queried
            "nb_runners": cf.get("runners"),
            "status": v["status"]["value"],
            "threads": int(v.get("vcpus") or 0),
            "ram": gb(v.get("memory")),
            "loc": loc,
        })
    # biggest machines first; the capacity view
    rows.sort(key=lambda r: (-r["threads"], r["name"]))

    active = [r for r in rows if r["status"] == "active"]
    total_threads = sum(r["threads"] for r in rows)
    active_threads = sum(r["threads"] for r in active)
    total_ram = sum(r["ram"] for r in rows)

    # Runners-per-machine from GitHub (needs the runners token); None -> "—".
    gh = github_runner_counts(gh_org or DEFAULT_ORG, gh_token) if gh_token else None

    def runners_cell(row):
        # live GitHub answer (0 if the label carries none) when we can query it,
        # otherwise NetBox's stored count as a fallback
        if gh is not None and row["label"]:
            return str(gh["labels"].get(row["label"].lower(), 0))
        nb = row.get("nb_runners")
        return str(nb) if nb is not None else "—"

    out = []
    out.append("## Build servers")
    out.append("")
    out.append(f"_Build servers from [NetBox](https://netbox.armbian.com/), "
               f"role `{ROLE}`. The **Runners** column is the number of GitHub "
               f"runner processes registered on that server (matched by its label), "
               f"falling back to the value recorded in NetBox when GitHub can't be queried._")
    out.append("")
    summary = (f"**{len(rows)}** servers — **{len(active)}** active, "
               f"**{len(rows) - len(active)}** offline · "
               f"**{total_threads}** CPU threads (**{active_threads}** active) · "
               f"**{total_ram}** GB RAM")
    if gh is not None:
        summary += f" · **{gh['total']}** GitHub runners (**{gh['online']}** online)"
    out.append(summary + ".")
    out.append("")
    out.append("| Server | Location | Threads | RAM | Runners | Status |")
    out.append("|:-------|:---------|--------:|----:|--------:|:------:|")
    for r in rows:
        status = "active" if r["status"] == "active" else f"⚠️ {r['status']}"
        name = r["label"] or r["name"]
        out.append(f"| `{name}` | {r['loc']} | {r['threads']} | {r['ram']} GB "
                   f"| {runners_cell(r)} | {status} |")
    out.append("")

    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--api", default=os.environ.get("NETBOX_API") or DEFAULT_API)
    ap.add_argument("--org", default=os.environ.get("GH_ORG") or DEFAULT_ORG)
    ap.add_argument("--output", help="write Markdown here (default: stdout)")
    args = ap.parse_args()

    token = os.environ.get("NETBOX_TOKEN")
    if not token:
        sys.exit("error: NETBOX_TOKEN is required (read-only NetBox API token)")
    gh_token = os.environ.get("GH_RUNNERS_TOKEN") or os.environ.get("GITHUB_TOKEN")

    report = build_report(args.api.rstrip("/"), token, gh_org=args.org, gh_token=gh_token)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(report + "\n")
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()
