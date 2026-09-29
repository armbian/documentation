---
title: If something goes wrong
seo_title: "Armbian first-boot troubleshooting"
description: "What to do when a step in the Armbian Getting Started guide fails: collect a debug log with armbian-debug, where the troubleshooting and recovery guide lives, and how to report a real bug."
---
# If something goes wrong

If you experience an issue during any of the steps mentioned in this section, please first check out our [_Troubleshooting and Recovery_](../user-guide/troubleshooting.md) guide.

## Collecting debug information

Whenever you ask for help — in the [forum](https://forum.armbian.com/), on a
bug report, or in chat — you will be asked for a debug log. Armbian ships a tool
that gathers everything a maintainer needs in one go:

```bash
sudo armbian-debug
```

It collects the kernel ring buffer (`dmesg`), the hardware-monitor log, board
and userspace identity, installed Armbian/kernel packages, loaded modules,
install logs and current system state, then uploads the result to
`paste.armbian.com` and prints a URL. **Post that URL** where you were asked for
it. IPv4 addresses are masked in the report before it leaves the board.

- Run it as `root` (it re-invokes itself with `sudo` if needed).
- On a terminal it gives you a short countdown — **press any key to print the
  report to the screen instead of uploading** (useful on an offline board; copy
  it to a pastebin yourself). If the upload fails, it prints the report too.
- Run non-interactively (e.g. over a pipe), it always prints instead of
  uploading, so nothing is sent without you seeing it.

!!! note "`armbian-debug: command not found`"
    Images that predate `armbian-debug` produce the same log with
    `sudo armbianmonitor -u`. On newer images that command still works and
    hands over to `armbian-debug`.

<!--
      * community / search forum || how to get help
      * FAQ (maybe feature is not developed)
-->

## How to report bugs

If you are certain you have found a bug, fill out our [bug reporting form](https://armbian.com/bugs/) and follow its instructions to collect the necessary information and how/where to provide them depending on the type of issue. Please understand that any reports lacking these fundamental diagnostics might be ignored.

---

**Previous:** [Keeping Armbian up to date](updating.md)

Back to the [Getting Started](index.md) overview.
