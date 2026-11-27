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

_Source: `https://github.armbian.com/armbian-images.json` — 2649 image assets across 437 boards, generated 2026-11-27 11:40 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Download (dl.armbian.com, per-board releases) | 967 | 184 | 26.8.1, 26.8.2, 26.11.3 |
| Community nightly | 952 | 254 | 26.11.0-trunk.137, 26.11.0-trunk.138 |
| CI nightly | 403 | 182 | 26.11.0-trunk.140 |
| Appliance images (kali/omv/homeassistant) | 319 | 120 | 26.11.2 |
| (orphaned — no repo) | 8 | 2 | 26.8.14 |

Current download release line: **26.11.3**.

## Non-standard boards

_**2** `csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| orangepi-cm5 | `wip` | 26.11.3 | OrangePi CM5 |
| ztl-a568 | `wip` | 26.11.3 | A568 |

<!-- download-images:end -->
