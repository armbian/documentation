---
title: Download images
seo_title: "Armbian download images: coverage & anomalies"
description: "Which Armbian images are published per board on dl.armbian.com, plus anomalies: outdated boards, non-standard boards on the download, and supported boards missing an image."
---
# Download images

What we publish for download, from the source of truth
[`armbian-images.json`](https://github.armbian.com/armbian-images.json): image
counts per channel, and anomalies worth acting on — boards whose newest
download is behind the release, non-standard boards on the per-board download,
supported boards with no download image, and desktop images for boards without
video.

<!-- download-images:start -->

## Download images report

_Source: `https://github.armbian.com/armbian-images.json` — 1762 image assets across 383 boards, generated 2026-09-07 13:30 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Download (dl.armbian.com, per-board releases) | 737 | 156 | 10 versions (…26.8.5) |
| Community nightly | 516 | 223 | 26.11.0-trunk.36 |
| Appliance images (kali/omv/homeassistant) | 417 | 133 | 26.8.1 |
| CI nightly | 84 | 39 | 26.11.0-trunk.40 |
| (orphaned — no repo) | 8 | 2 | 26.8.6 |

Current download release line: **26.8.5/26.8.4/26.8.3**.

## Outdated boards

_**20** boards whose newest `dl.armbian.com` image is behind the current 26.8.5/26.8.4/26.8.3 line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| pocketbeagle2 | `conf` | 26.2.1 | 2026-02-20 | 199 d |
| beaglebone-ai64 | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| khadas-vim1 | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| khadas-vim1s | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| mba8mpxl-ras314 | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| mba8mpxl | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| radxa-nio-12l | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| radxa-rock-4d | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| sk-am68 | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| sk-am69 | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| sk-tda4vm | `conf` | 26.2.5 | 2026-04-25 | 134 d |
| mekotronics-r58-4x4 | `conf` | 26.5.1 | 2026-05-24 | 105 d |
| rock-5-itx | `conf` | 26.5.1 | 2026-06-09 | 90 d |
| sk-am62-lp | `conf` | 26.5.1 | 2026-06-18 | 81 d |
| sk-am62-sip | `conf` | 26.5.1 | 2026-06-18 | 80 d |
| sk-am62b | `conf` | 26.5.1 | 2026-06-18 | 80 d |
| sk-am62p | `conf` | 26.5.1 | 2026-06-18 | 80 d |
| sk-am64b | `conf` | 26.5.1 | 2026-06-18 | 80 d |
| tmds62levm | `conf` | 26.5.1 | 2026-06-18 | 80 d |
| tmds64evm | `conf` | 26.5.1 | 2026-06-18 | 80 d |

## Non-standard boards

_**3** `csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| orangepi6-plus | `csc` | 26.8.3 | Orangepi 6 Plus |
| qidi-x4 | `csc` | 26.8.1 | Qidi X4 |
| qidi-x7 | `csc` | 26.8.1 | Qidi X7 |

## Missing download images

_**4** `conf` (standard-support) boards absent from `dl.armbian.com` — only nightly/appliance, or nowhere._

| board | name | present in |
| --- | --- | --- |
| beagley-ai | BeagleY-AI | Appliance |
| mba93xxca-tqma93xx | MBa93xxCA | CI |
| mba93xxla-mini | MBa93xxLA-MINI | CI, Appliance |
| tq-smarc2-tqma8mpxs | TQ-SMARC2-TQMa8MPxS | CI, Appliance |

<!-- download-images:end -->
