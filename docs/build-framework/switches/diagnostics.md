---
seo_title: "Armbian build output & diagnostics switches"
description: "Diagnostics for Armbian builds: SHARE_LOG to upload full build logs, SHOW_LOG to stream command output live, and SHOW_DEBUG for verbose messages."
---

# Diagnostics

Logs and diagnostic output for a build.

#### SHARE_LOG

`string`

- `yes`
- `no` (default)

At the end of the build the framework assembles the whole run into a single ANSI log file; with `SHARE_LOG=yes` it uploads that file to Armbian's paste servers — trying `paste.armbian.com` and its mirrors in turn until one succeeds — and prints the resulting share URL (also exposed as a `logs_url` output under GitHub Actions). It defaults to `no` because uploading is a network action and the log embeds local paths and environment details, so when left off the build instead prints the ready-made `curl` commands to upload it yourself. Turn it on when reporting a build issue, so maintainers can open the complete log from the link.

```sh
./compile.sh SHARE_LOG=yes
```

#### SHOW_LOG

`string` · default: `yes` when attached to a terminal

Streams the output of every command to the terminal as the build runs, prefixed and interleaved with the high-level progress messages, instead of quietly capturing it into the per-section files under `output/logs`. It defaults to `yes` whenever stdout is a terminal (and is also forced on under CI and when `DEBUG=yes`), on the assumption that an interactive user wants to watch the build; with it off you get only the concise section markers, and the captured output is surfaced only if a command fails. Set it to `no` for a cleaner console — the full logs are still written to disk either way — or `yes` to force live streaming when output is being redirected to a file or pipe.

#### SHOW_DEBUG

`string` · default: `no`

Raises the verbosity of the build to debug level: it lets the many `debug`-severity `display_alert` messages through, triggers extra state and variable dumps throughout the pipeline, un-quiets `apt` inside the chroot (dropping its `-qq` flag so package `Conf`/`Inst` lines appear), and bumps the log level of the Python configuration-aggregation helpers. It defaults to `no` to keep the log readable and focused on the high-level flow, and is automatically turned on when `DEBUG=yes`. Enable it when you are diagnosing the build framework itself and need to see exactly what each step is doing.
