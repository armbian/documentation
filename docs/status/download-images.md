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

_Source: `https://github.armbian.com/armbian-images.json` — 1762 image assets across 381 boards, generated 2026-08-27 20:11 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Download (dl.armbian.com, per-board releases) | 737 | 155 | 10 versions (…26.8.3) |
| Community nightly | 522 | 222 | 26.11.0-trunk.19 |
| Appliance images (kali/omv/homeassistant) | 417 | 133 | 26.8.1 |
| CI nightly | 78 | 35 | 26.11.0-trunk.25 |
| (orphaned — no repo) | 8 | 2 | 26.8.5 |

Current download release line: **26.8.3/26.8.2/26.8.1**.

## ⏳ Outdated boards on the download — behind the current 26.8.3/26.8.2/26.8.1 line (22)

_Newest per-board image on `dl.armbian.com` is older than the current release line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| pocketbeagle2 | `conf` | 26.2.1 | 2026-02-20 | 188 d |
| beaglebone-ai64 | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| khadas-vim1 | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| khadas-vim1s | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| mba8mpxl-ras314 | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| mba8mpxl | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| radxa-nio-12l | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| radxa-rock-4d | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| sk-am68 | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| sk-am69 | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| sk-tda4vm | `conf` | 26.2.5 | 2026-04-25 | 124 d |
| mekotronics-r58-4x4 | `conf` | 26.5.1 | 2026-05-24 | 94 d |
| rock-5-itx | `conf` | 26.5.1 | 2026-06-09 | 79 d |
| sk-am62-lp | `conf` | 26.5.1 | 2026-06-18 | 70 d |
| sk-am62-sip | `conf` | 26.5.1 | 2026-06-18 | 70 d |
| sk-am62b | `conf` | 26.5.1 | 2026-06-18 | 70 d |
| sk-am62p | `conf` | 26.5.1 | 2026-06-18 | 70 d |
| sk-am64b | `conf` | 26.5.1 | 2026-06-18 | 70 d |
| tmds62levm | `conf` | 26.5.1 | 2026-06-18 | 70 d |
| tmds64evm | `conf` | 26.5.1 | 2026-06-18 | 70 d |
| mekotronics-r58hd | `conf` | 26.5.2 | 2026-07-08 | 50 d |
| mekotronics-r58s2 | `conf` | 26.5.2 | 2026-07-06 | 52 d |

## ⚠️ Non-standard boards on the download (3)

_`csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| orangepi6-plus | `csc` | 26.8.3 | Orangepi 6 Plus |
| qidi-x4 | `csc` | 26.8.1 | Qidi X4 |
| qidi-x7 | `csc` | 26.8.1 | Qidi X7 |

## ❓ Supported boards with no download image (3)

_`conf` (standard-support) boards absent from `dl.armbian.com` — only nightly/appliance, or nowhere._

| board | name | present in |
| --- | --- | --- |
| beagley-ai | BeagleY-AI | Appliance |
| mba93xxla-mini | MBa93xxLA-MINI | CI, Appliance |
| tq-smarc2-tqma8mpxs | TQ-SMARC2-TQMa8MPxS | CI, Appliance |

## 🖥️ Desktop images for boards without video output (0)

_None._

<!-- download-images:end -->
