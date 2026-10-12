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

_Source: `https://github.armbian.com/armbian-images.json` — 1848 image assets across 398 boards, generated 2026-10-12 16:44 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Download (dl.armbian.com, per-board releases) | 789 | 168 | 13 versions (…26.8.10) |
| Community nightly | 517 | 228 | 26.11.0-trunk.83 |
| Appliance images (kali/omv/homeassistant) | 417 | 133 | 26.8.1 |
| CI nightly | 120 | 53 | 26.11.0-trunk.90 |
| (orphaned — no repo) | 5 | 2 | 26.8.11 |

Current download release line: **26.8.10/26.8.9/26.8.8**.

## Outdated boards

_**3** boards whose newest `dl.armbian.com` image is behind the current 26.8.10/26.8.9/26.8.8 line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| khadas-vim1 | `conf` | 26.2.5 | 2026-04-25 | 169 d |
| khadas-vim1s | `conf` | 26.2.5 | 2026-04-25 | 169 d |
| mekotronics-r58-4x4 | `conf` | 26.5.1 | 2026-05-24 | 140 d |

## Missing download images

_**1** `conf` (standard-support) boards absent from `dl.armbian.com` — only nightly/appliance, or nowhere._

| board | name | present in |
| --- | --- | --- |
| boardcon-sbc3568 | SBC3568 | CI |

<!-- download-images:end -->
