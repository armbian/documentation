---
title: Project status
seo_title: "Armbian project status: boards, downloads & infrastructure"
description: "Live status of the Armbian project: tested boards, Wi-Fi performance, download images, package repository health and the mirror network — regenerated automatically."
---
# Project status

This section collects the **live, automatically generated** views of the
project — the state of the hardware we test, the images and packages we
publish, and the infrastructure that delivers them. Unlike the rest of the
documentation, these pages describe *how things are right now* and are
refreshed by scheduled jobs, not written by hand.

!!! info "Auto-generated"

    Each page below is regenerated from a source of truth (the autotest
    fleet, NetBox, `armbian-images.json`, the apt indices, ...). Numbers move
    over time; treat them as a snapshot, not a promise.

## Hardware

<div class="grid cards" markdown>

- :material-check-decagram: **[Wi-Fi performance](wifi-performance.md)**

    Measured throughput per board and wireless chip, from the autotest fleet.

- :material-developer-board: **Tested boards** *(planned)*

    Functional test matrix — what boots, what passes, per board.

- :material-database: **[Datacenter boards](boards.md)**

    The test-datacenter fleet — which boards are operational or broken.

</div>

## Downloads & repository

<div class="grid cards" markdown>

- :material-server-network: **[Mirror network](mirrors.md)**

    The download redirector and every active mirror, with what each serves.

- :material-download: **[Download images](download-images.md)**

    Which images we publish per board, and anomalies (outdated, missing,
    non-standard).

- :material-package-variant: **[Package repository](package-repository.md)**

    `apt.armbian.com` status — package and kernel versions, kernel-family
    drift and header gaps.

- :material-server: **[Build machinery](build-machinery.md)**

    The build servers — CPU-thread capacity, memory, location and runner count.

</div>

!!! note "Prototype"

    This is the first cut of the section. The **planned** entries above already
    have generators (autotests, `armbian.github.io`, the apt report) that
    currently write to CI job summaries; wiring them into pages here is the next
    step.
