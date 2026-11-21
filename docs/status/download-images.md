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

_Source: `https://github.armbian.com/armbian-images.json` — 2494 image assets across 432 boards, generated 2026-11-21 17:27 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Community nightly | 952 | 254 | 26.11.0-trunk.137, 26.11.0-trunk.138 |
| Download (dl.armbian.com, per-board releases) | 842 | 174 | 11 versions (…26.11.2) |
| CI nightly | 387 | 175 | 26.11.0-trunk.135 |
| Appliance images (kali/omv/homeassistant) | 305 | 114 | 26.11.2 |
| (orphaned — no repo) | 8 | 2 | 26.8.14 |

Current download release line: **26.11.2**.

## Outdated boards

_**134** boards whose newest `dl.armbian.com` image is behind the current 26.11.2 line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| mekotronics-r58-4x4 | `conf` | 26.5.1 | 2026-05-24 | 180 d |
| aml-c400-plus | `conf` | 26.8.1 | 2026-08-15 | 97 d |
| anbernic-rg-ds | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| anbernic-rg-vita-pro | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| bananapi | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| bananapicm4io | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| bananapim2s | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| bananapim4berry | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| bananapim5 | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| bananapim5pro | `conf` | 26.8.1 | 2026-08-08 | 104 d |
| bananapim7 | `conf` | 26.8.1 | 2026-08-05 | 107 d |
| beaglebadge | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| beagleplay | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| bigtreetech-cb1 | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| bigtreetech-cb2 | `conf` | 26.8.1 | 2026-08-14 | 99 d |
| cix-acpi | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| dg-svr-865-tiny | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| easepi-a2 | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| easepi-r2 | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| gateway-gz80x | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| helios64 | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| inovato-quadra | `conf` | 26.8.1 | 2026-08-10 | 103 d |
| jethubj100 | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| jethubj200 | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| jethubj80 | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| khadas-edge2 | `conf` | 26.8.1 | 2026-08-08 | 104 d |
| khadas-vim2 | `conf` | 26.8.1 | 2026-08-12 | 101 d |
| khadas-vim3 | `conf` | 26.8.1 | 2026-08-12 | 101 d |
| lafrite | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| lepotato | `conf` | 26.8.1 | 2026-08-12 | 101 d |
| lubancat-5io | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| mksklipad50 | `conf` | 26.8.1 | 2026-08-15 | 98 d |
| nanopi-m5 | `conf` | 26.8.1 | 2026-08-14 | 98 d |
| nanopi-r3s-lts | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| nanopi-r4s | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| nanopi-r76s | `conf` | 26.8.1 | 2026-08-11 | 102 d |
| nanopik1plus | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| nanopik2-s905 | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| nanopim4v2 | `conf` | 26.8.1 | 2026-08-10 | 103 d |
| odroidc1 | `conf` | 26.8.1 | 2026-08-15 | 98 d |
| odroidc2 | `conf` | 26.8.1 | 2026-08-15 | 98 d |
| odroidc4 | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| odroidhc4 | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| odroidm1 | `conf` | 26.8.1 | 2026-08-07 | 106 d |
| odroidm2 | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| odroidn2 | `conf` | 26.8.1 | 2026-08-07 | 105 d |
| odroidxu4 | `conf` | 26.8.1 | 2026-08-11 | 102 d |
| oneplus-kebab | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| orangepi4-lts | `conf` | 26.8.1 | 2026-08-14 | 98 d |
| orangepione | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| orangepipc2 | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| orangepizero3w | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| pine64 | `csc` | 26.8.1 | 2026-08-09 | 103 d |
| qidi-x6 | `conf` | 26.8.1 | 2026-08-14 | 99 d |
| qidi-x7 | `csc` | 26.8.1 | 2026-08-14 | 99 d |
| qidi-x4 | `csc` | 26.8.1 | 2026-08-14 | 99 d |
| radxa-e24c | `conf` | 26.8.1 | 2026-08-14 | 98 d |
| radxa-zero3 | `conf` | 26.8.1 | 2026-08-12 | 100 d |
| renegade | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| rock-2a | `conf` | 26.8.1 | 2026-08-15 | 98 d |
| rock-2f | `conf` | 26.8.1 | 2026-08-15 | 98 d |
| rock-3a | `conf` | 26.8.1 | 2026-08-15 | 98 d |
| rock-s0 | `conf` | 26.8.1 | 2026-08-15 | 98 d |
| rockpi-4bplus | `conf` | 26.8.1 | 2026-08-10 | 103 d |
| rockpi-e | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| rockpi-s | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| rockpro64 | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| sakurapi-rk3308b | `conf` | 26.8.1 | 2026-08-16 | 97 d |
| sovol-zero | `conf` | 26.8.1 | 2026-08-09 | 104 d |
| sweet-potato | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| tinkerboard | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| udoo | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| uefi-loong64 | `conf` | 26.8.1 | 2026-08-12 | 101 d |
| xiaomi-elish | `conf` | 26.8.1 | 2026-08-05 | 107 d |
| youyeetoo-r1-v3 | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| youyeetoo-yy3588 | `conf` | 26.8.1 | 2026-08-08 | 105 d |
| nanopi-r6s | `conf` | 26.8.10 | 2026-10-11 | 41 d |
| nanopi-r6c | `csc` | 26.8.10 | 2026-10-11 | 41 d |
| nanopi-m6v2 | `conf` | 26.8.10 | 2026-10-11 | 41 d |
| nanopct6-lts-plus | `conf` | 26.8.10 | 2026-10-11 | 41 d |

_…and 54 more._

## Non-standard boards

_**1** `csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| pine64 | `csc` | 26.8.1 | Pine A64 / A64+ |

## Missing download images

_**4** `conf` (standard-support) boards absent from `dl.armbian.com` — only nightly/appliance, or nowhere._

| board | name | present in |
| --- | --- | --- |
| boardcon-em3588 | EM3588 | CI |
| mba62xx-tqma62xx | MBa62xx | CI, Appliance |
| mba67xx-tqma67xx | MBa67xx | CI, Appliance |
| turris-omnia | Turris Omnia | CI |

<!-- download-images:end -->
