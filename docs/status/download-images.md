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

_Source: `https://github.armbian.com/armbian-images.json` — 2402 image assets across 437 boards, generated 2026-11-26 19:14 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Community nightly | 952 | 254 | 26.11.0-trunk.137, 26.11.0-trunk.138 |
| Download (dl.armbian.com, per-board releases) | 729 | 173 | 26.8.1, 26.8.2, 26.11.3 |
| CI nightly | 403 | 182 | 26.11.0-trunk.140 |
| Appliance images (kali/omv/homeassistant) | 310 | 119 | 26.11.2 |
| (orphaned — no repo) | 8 | 2 | 26.8.14 |

Current download release line: **26.11.3**.

## Outdated boards

_**1** boards whose newest `dl.armbian.com` image is behind the current 26.11.3 line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| pine64 | `csc` | 26.8.1 | 2026-08-09 | 109 d |

## Non-standard boards

_**2** `csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| orangepi-cm5 | `wip` | 26.11.3 | OrangePi CM5 |
| pine64 | `csc` | 26.8.1 | Pine A64 / A64+ |

## Missing download images

_**11** `conf` (standard-support) boards absent from `dl.armbian.com` — only nightly/appliance, or nowhere._

| board | name | present in |
| --- | --- | --- |
| thinkpad-x13s | ThinkPad X13s | CI, Appliance |
| tinkerboard | Tinker Board | CI |
| tmds62levm | TMDS62LEVM | CI, Appliance |
| tmds64evm | TMDS64EVM | CI, Appliance |
| tq-smarc2-tqma8mpxs | TQ-SMARC2-TQMa8MPxS | CI, Appliance |
| turris-omnia | Turris Omnia | CI |
| udoo | Udoo | CI |
| verdin-imx8mm | Verdin iMX8M Mini | CI, Appliance |
| xiaomi-elish | Elish | CI |
| youyeetoo-r1-v3 | R1 v3 | CI |
| youyeetoo-yy3588 | YY3588 | CI |

<!-- download-images:end -->
