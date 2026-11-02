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

_Source: `https://github.armbian.com/armbian-images.json` — 2224 image assets across 415 boards, generated 2026-11-02 17:04 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Community nightly | 873 | 241 | 26.11.0-trunk.108 |
| Download (dl.armbian.com, per-board releases) | 795 | 170 | 14 versions (…26.8.12) |
| Appliance images (kali/omv/homeassistant) | 420 | 134 | 26.8.1 |
| CI nightly | 128 | 56 | 26.11.0-trunk.118 |
| (orphaned — no repo) | 8 | 2 | 26.8.14 |

Current download release line: **26.8.12/26.8.11/26.8.10**.

## Outdated boards

_**2** boards whose newest `dl.armbian.com` image is behind the current 26.8.12/26.8.11/26.8.10 line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| khadas-vim1s | `conf` | 26.2.5 | 2026-04-25 | 190 d |
| mekotronics-r58-4x4 | `conf` | 26.5.1 | 2026-05-24 | 161 d |

## Non-standard boards

_**1** `csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| pine64 | `csc` | 26.8.1 | Pine A64 / A64+ |

## Missing download images

_**3** `conf` (standard-support) boards absent from `dl.armbian.com` — only nightly/appliance, or nowhere._

| board | name | present in |
| --- | --- | --- |
| boardcon-em3588 | EM3588 | CI |
| odroidu2 | Odroid U2 | CI |
| turris-omnia | Turris Omnia | CI |

<!-- download-images:end -->
