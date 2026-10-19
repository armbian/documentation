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

_Source: `https://github.armbian.com/armbian-images.json` — 1870 image assets across 406 boards, generated 2026-10-19 14:41 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Download (dl.armbian.com, per-board releases) | 793 | 169 | 14 versions (…26.8.11) |
| Community nightly | 532 | 235 | 26.11.0-trunk.100 |
| Appliance images (kali/omv/homeassistant) | 417 | 133 | 26.8.1 |
| CI nightly | 124 | 54 | 26.11.0-trunk.102 |
| (orphaned — no repo) | 4 | 2 | 26.8.12 |

Current download release line: **26.8.11/26.8.10/26.8.9**.

## Outdated boards

_**3** boards whose newest `dl.armbian.com` image is behind the current 26.8.11/26.8.10/26.8.9 line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| khadas-vim1 | `conf` | 26.2.5 | 2026-04-25 | 176 d |
| khadas-vim1s | `conf` | 26.2.5 | 2026-04-25 | 176 d |
| mekotronics-r58-4x4 | `conf` | 26.5.1 | 2026-05-24 | 147 d |

## Non-standard boards

_**1** `csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| pine64 | `csc` | 26.8.1 | Pine64 |

<!-- download-images:end -->
