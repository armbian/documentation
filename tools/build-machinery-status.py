#!/usr/bin/env python3
"""Generate a Markdown status report for the Armbian build machinery — the
build servers — from NetBox, with the live runner count from GitHub.

Reads the build servers (NetBox VMs tagged github-runner) and reports
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
import re
import sys
import urllib.request

DEFAULT_API = "https://netbox.armbian.com/api"
# Build runners are identified by a tag (a VM may have the mirror/other role
# yet also host runners), not by role.
TAG = "github-runner"
DEFAULT_ORG = "armbian"
# Runners are named "<server>-01", "<server>-02", ...; strip the trailing index
# to group a server's runners (e.g. insa-trixie-01 -> insa-trixie).
RUNNER_INDEX = re.compile(r"-\d+$")


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
    # NetBox stores memory in MB (binary: 512 GB -> 524288 MB).
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
    per_server, online_server = collections.Counter(), collections.Counter()
    for r in runners:
        # a server's runners are named "<server>-NN"; group by the prefix
        key = RUNNER_INDEX.sub("", r.get("name", "")).lower()
        per_server[key] += 1
        if r.get("status") == "online":
            online_server[key] += 1
    online = sum(1 for r in runners if r.get("status") == "online")
    return {"servers": per_server, "online_servers": online_server,
            "total": len(runners), "online": online}


def build_report(api, token, gh_org=None, gh_token=None):
    vms = netbox_get(api, token, f"/virtualization/virtual-machines/?tag={TAG}&limit=500")
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

    # Resolve a runner count (and online count) per server: live from GitHub
    # matched by the label when we can query it, otherwise the NetBox value.
    gh = github_runner_counts(gh_org or DEFAULT_ORG, gh_token) if gh_token else None
    for r in rows:
        key = (r["label"] or r["name"] or "").lower()
        if gh is not None and key in gh["servers"]:
            r["rcount"] = gh["servers"][key]
            r["ronline"] = gh["online_servers"].get(key, 0)
        else:
            r["rcount"] = r.get("nb_runners")   # NetBox fallback (may be None)
            r["ronline"] = None

    total_runners = sum(r["rcount"] for r in rows if r["rcount"] is not None)
    online_runners = sum(r["ronline"] for r in rows if r["ronline"] is not None)

    out = []
    out.append("## Build servers")
    out.append("")
    n_off = len(rows) - len(active)
    servers = f"**{len(rows)}** servers" + (f" (**{n_off}** offline)" if n_off else "")
    threads = f"**{total_threads}** threads" + (
        f" (**{active_threads}** active)" if active_threads != total_threads else "")
    runners = f"**{total_runners}** runners" + (
        f" (**{online_runners}** online)" if gh is not None else "")
    out.append(" · ".join([servers, threads, f"**{total_ram}** GB RAM", runners]) + ".")
    out.append("")
    out.append("| Server | Location | Threads | RAM | Runners | Status |")
    out.append("|:-------|:---------|--------:|----:|--------:|:------:|")
    for r in rows:
        # status always from NetBox: some servers are powered on demand, so
        # their runners can read offline on GitHub while the server is fine
        status = "active" if r["status"] == "active" else f"⚠️ {r['status']}"
        name = r["label"] or r["name"]
        runners = str(r["rcount"]) if r["rcount"] is not None else "—"
        out.append(f"| `{name}` | {r['loc']} | {r['threads']} | {r['ram']} GB "
                   f"| {runners} | {status} |")
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
