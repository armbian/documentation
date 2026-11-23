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

_Source: `https://github.armbian.com/armbian-images.json` — 2545 image assets across 437 boards, generated 2026-11-23 06:42 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Community nightly | 952 | 254 | 26.11.0-trunk.137, 26.11.0-trunk.138 |
| Download (dl.armbian.com, per-board releases) | 872 | 179 | 11 versions (…26.11.2) |
| CI nightly | 403 | 182 | 26.11.0-trunk.139 |
| Appliance images (kali/omv/homeassistant) | 310 | 119 | 26.11.2 |
| (orphaned — no repo) | 8 | 2 | 26.8.14 |

Current download release line: **26.11.2**.

## Outdated boards

_**124** boards whose newest `dl.armbian.com` image is behind the current 26.11.2 line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| mekotronics-r58-4x4 | `conf` | 26.5.1 | 2026-05-24 | 182 d |
| aml-c400-plus | `conf` | 26.8.1 | 2026-08-15 | 99 d |
| bananapi | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| bananapicm4io | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| bananapim2s | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| bananapim4berry | `conf` | 26.8.1 | 2026-08-16 | 98 d |
| bananapim5 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| bananapim5pro | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| bananapim7 | `conf` | 26.8.1 | 2026-08-05 | 109 d |
| beaglebadge | `conf` | 26.8.1 | 2026-08-09 | 106 d |
| beagleplay | `conf` | 26.8.1 | 2026-08-09 | 106 d |
| bigtreetech-cb1 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| bigtreetech-cb2 | `conf` | 26.8.1 | 2026-08-14 | 100 d |
| dg-svr-865-tiny | `conf` | 26.8.1 | 2026-08-09 | 106 d |
| easepi-a2 | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| easepi-r2 | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| gateway-gz80x | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| helios64 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| inovato-quadra | `conf` | 26.8.1 | 2026-08-10 | 104 d |
| khadas-edge2 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| khadas-vim2 | `conf` | 26.8.1 | 2026-08-12 | 102 d |
| khadas-vim3 | `conf` | 26.8.1 | 2026-08-12 | 102 d |
| lafrite | `conf` | 26.8.1 | 2026-08-16 | 98 d |
| lepotato | `conf` | 26.8.1 | 2026-08-12 | 102 d |
| lubancat-5io | `conf` | 26.8.1 | 2026-08-16 | 98 d |
| nanopi-m5 | `conf` | 26.8.1 | 2026-08-14 | 100 d |
| nanopi-r3s-lts | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| nanopi-r4s | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| nanopi-r76s | `conf` | 26.8.1 | 2026-08-11 | 104 d |
| nanopik1plus | `conf` | 26.8.1 | 2026-08-16 | 99 d |
| nanopik2-s905 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| nanopim4v2 | `conf` | 26.8.1 | 2026-08-10 | 105 d |
| odroidc1 | `conf` | 26.8.1 | 2026-08-15 | 100 d |
| odroidc2 | `conf` | 26.8.1 | 2026-08-15 | 100 d |
| odroidc4 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| odroidhc4 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| odroidm2 | `conf` | 26.8.1 | 2026-08-16 | 98 d |
| odroidn2 | `conf` | 26.8.1 | 2026-08-07 | 107 d |
| oneplus-kebab | `conf` | 26.8.1 | 2026-08-09 | 106 d |
| orangepi4-lts | `conf` | 26.8.1 | 2026-08-14 | 100 d |
| orangepione | `conf` | 26.8.1 | 2026-08-16 | 98 d |
| orangepipc2 | `conf` | 26.8.1 | 2026-08-16 | 98 d |
| orangepizero3w | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| pine64 | `csc` | 26.8.1 | 2026-08-09 | 105 d |
| qidi-x6 | `conf` | 26.8.1 | 2026-08-14 | 100 d |
| qidi-x7 | `csc` | 26.8.1 | 2026-08-14 | 100 d |
| qidi-x4 | `csc` | 26.8.1 | 2026-08-14 | 100 d |
| radxa-e24c | `conf` | 26.8.1 | 2026-08-14 | 100 d |
| radxa-zero3 | `conf` | 26.8.1 | 2026-08-12 | 102 d |
| renegade | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| rock-2a | `conf` | 26.8.1 | 2026-08-15 | 100 d |
| rock-2f | `conf` | 26.8.1 | 2026-08-15 | 100 d |
| rock-3a | `conf` | 26.8.1 | 2026-08-15 | 99 d |
| rock-s0 | `conf` | 26.8.1 | 2026-08-15 | 100 d |
| rockpi-4bplus | `conf` | 26.8.1 | 2026-08-10 | 105 d |
| rockpi-e | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| rockpi-s | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| rockpro64 | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| sakurapi-rk3308b | `conf` | 26.8.1 | 2026-08-16 | 98 d |
| sovol-zero | `conf` | 26.8.1 | 2026-08-09 | 106 d |
| sweet-potato | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| tinkerboard | `conf` | 26.8.1 | 2026-08-09 | 105 d |
| udoo | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| xiaomi-elish | `conf` | 26.8.1 | 2026-08-05 | 109 d |
| youyeetoo-r1-v3 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| youyeetoo-yy3588 | `conf` | 26.8.1 | 2026-08-08 | 106 d |
| nanopi-r6s | `conf` | 26.8.10 | 2026-10-11 | 42 d |
| nanopi-r6c | `csc` | 26.8.10 | 2026-10-11 | 42 d |
| nanopi-m6v2 | `conf` | 26.8.10 | 2026-10-11 | 42 d |
| nanopct6-lts-plus | `conf` | 26.8.10 | 2026-10-11 | 42 d |
| nanopi-m6 | `conf` | 26.8.10 | 2026-10-11 | 42 d |
| nanopct6-lts | `conf` | 26.8.10 | 2026-10-11 | 42 d |
| nanopct6 | `conf` | 26.8.10 | 2026-10-11 | 42 d |
| tanix-tx6s | `conf` | 26.8.10 | 2026-10-10 | 43 d |
| verdin-imx8mm | `conf` | 26.8.10 | 2026-10-10 | 43 d |
| boardcon-sbc3568 | `conf` | 26.8.11 | 2026-10-18 | 35 d |
| khadas-vim1 | `conf` | 26.8.11 | 2026-10-18 | 35 d |
| mekotronics-r58hd | `conf` | 26.8.2 | 2026-08-17 | 97 d |
| mekotronics-r58s2 | `conf` | 26.8.2 | 2026-08-17 | 97 d |
| orangepi3-lts | `conf` | 26.8.2 | 2026-08-16 | 98 d |

_…and 44 more._

## Non-standard boards

_**1** `csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| pine64 | `csc` | 26.8.1 | Pine A64 / A64+ |

## Missing download images

_**4** `conf` (standard-support) boards absent from `dl.armbian.com` — only nightly/appliance, or nowhere._

| board | name | present in |
| --- | --- | --- |
| bananapipro | Banana Pi Pro | CI |
| boardcon-em3588 | EM3588 | CI |
| mba62xx-tqma62xx | MBa62xx | CI, Appliance |
| mba67xx-tqma67xx | MBa67xx | CI, Appliance |

<!-- download-images:end -->
