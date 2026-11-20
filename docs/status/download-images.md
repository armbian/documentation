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

_Source: `https://github.armbian.com/armbian-images.json` — 2139 image assets across 429 boards, generated 2026-11-20 11:09 UTC._

## Overview

| channel | images | boards | version(s) |
| --- | --- | --- | --- |
| Community nightly | 935 | 250 | 26.11.0-trunk.130 |
| Download (dl.armbian.com, per-board releases) | 809 | 171 | 13 versions (…26.11.2) |
| CI nightly | 387 | 175 | 26.11.0-trunk.135 |
| (orphaned — no repo) | 8 | 2 | 26.8.14 |

Current download release line: **26.11.2**.

## Outdated boards

_**151** boards whose newest `dl.armbian.com` image is behind the current 26.11.2 line._

| board | support | newest download version | date | age |
| --- | --- | --- | --- | --- |
| mekotronics-r58-4x4 | `conf` | 26.5.1 | 2026-05-24 | 179 d |
| aml-c400-plus | `conf` | 26.8.1 | 2026-08-15 | 96 d |
| anbernic-rg-ds | `conf` | 26.8.1 | 2026-08-16 | 96 d |
| anbernic-rg-vita-pro | `conf` | 26.8.1 | 2026-08-16 | 96 d |
| arduino-uno-q | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| bananapi | `conf` | 26.8.1 | 2026-08-09 | 102 d |
| bananapicm4io | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| bananapim2s | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| bananapim4berry | `conf` | 26.8.1 | 2026-08-16 | 95 d |
| bananapim5 | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| bananapim5pro | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| bananapim7 | `conf` | 26.8.1 | 2026-08-05 | 106 d |
| beaglebadge | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| beagleplay | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| bigtreetech-cb1 | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| bigtreetech-cb2 | `conf` | 26.8.1 | 2026-08-14 | 98 d |
| cix-acpi | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| clearfogpro | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| cubox-i | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| dg-svr-865-tiny | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| easepi-a2 | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| easepi-r2 | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| espressobin | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| gateway-gz80x | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| helios4 | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| helios64 | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| inovato-quadra | `conf` | 26.8.1 | 2026-08-10 | 102 d |
| jethubj100 | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| jethubj200 | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| jethubj80 | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| khadas-edge2 | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| khadas-vim2 | `conf` | 26.8.1 | 2026-08-12 | 100 d |
| khadas-vim3 | `conf` | 26.8.1 | 2026-08-12 | 100 d |
| lafrite | `conf` | 26.8.1 | 2026-08-16 | 95 d |
| lepotato | `conf` | 26.8.1 | 2026-08-12 | 99 d |
| lubancat-5io | `conf` | 26.8.1 | 2026-08-16 | 95 d |
| mksklipad50 | `conf` | 26.8.1 | 2026-08-15 | 97 d |
| nanopi-m5 | `conf` | 26.8.1 | 2026-08-14 | 97 d |
| nanopi-r3s-lts | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| nanopi-r4s | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| nanopi-r76s | `conf` | 26.8.1 | 2026-08-11 | 101 d |
| nanopik1plus | `conf` | 26.8.1 | 2026-08-16 | 96 d |
| nanopik2-s905 | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| nanopim4v2 | `conf` | 26.8.1 | 2026-08-10 | 102 d |
| odroidc1 | `conf` | 26.8.1 | 2026-08-15 | 97 d |
| odroidc2 | `conf` | 26.8.1 | 2026-08-15 | 97 d |
| odroidc4 | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| odroidhc4 | `conf` | 26.8.1 | 2026-08-08 | 103 d |
| odroidm1 | `conf` | 26.8.1 | 2026-08-07 | 104 d |
| odroidm2 | `conf` | 26.8.1 | 2026-08-16 | 95 d |
| odroidn2 | `conf` | 26.8.1 | 2026-08-07 | 104 d |
| odroidxu4 | `conf` | 26.8.1 | 2026-08-11 | 101 d |
| oneplus-kebab | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| orangepi4-lts | `conf` | 26.8.1 | 2026-08-14 | 97 d |
| orangepione | `conf` | 26.8.1 | 2026-08-16 | 95 d |
| orangepipc2 | `conf` | 26.8.1 | 2026-08-16 | 95 d |
| orangepizero3w | `conf` | 26.8.1 | 2026-08-09 | 102 d |
| pine64 | `csc` | 26.8.1 | 2026-08-09 | 102 d |
| qidi-x6 | `conf` | 26.8.1 | 2026-08-14 | 98 d |
| qidi-x7 | `csc` | 26.8.1 | 2026-08-14 | 98 d |
| qidi-x4 | `csc` | 26.8.1 | 2026-08-14 | 98 d |
| radxa-dragon-q6a | `conf` | 26.8.1 | 2026-08-14 | 97 d |
| radxa-dragon-q8b | `conf` | 26.8.1 | 2026-08-14 | 97 d |
| radxa-e24c | `conf` | 26.8.1 | 2026-08-14 | 97 d |
| radxa-zero3 | `conf` | 26.8.1 | 2026-08-12 | 99 d |
| renegade | `conf` | 26.8.1 | 2026-08-09 | 102 d |
| rock-2a | `conf` | 26.8.1 | 2026-08-15 | 97 d |
| rock-2f | `conf` | 26.8.1 | 2026-08-15 | 97 d |
| rock-3a | `conf` | 26.8.1 | 2026-08-15 | 97 d |
| rock-s0 | `conf` | 26.8.1 | 2026-08-15 | 97 d |
| rockpi-4bplus | `conf` | 26.8.1 | 2026-08-10 | 102 d |
| rockpi-e | `conf` | 26.8.1 | 2026-08-09 | 102 d |
| rockpi-s | `conf` | 26.8.1 | 2026-08-09 | 102 d |
| rockpro64 | `conf` | 26.8.1 | 2026-08-09 | 102 d |
| sakurapi-rk3308b | `conf` | 26.8.1 | 2026-08-16 | 95 d |
| sovol-zero | `conf` | 26.8.1 | 2026-08-09 | 103 d |
| sweet-potato | `conf` | 26.8.1 | 2026-08-09 | 102 d |
| thinkpad-x13s | `conf` | 26.8.1 | 2026-08-14 | 97 d |
| tinkerboard | `conf` | 26.8.1 | 2026-08-09 | 102 d |
| udoo | `conf` | 26.8.1 | 2026-08-08 | 103 d |

_…and 71 more._

## Non-standard boards

_**1** `csc`/`wip`/`tvb` boards with images on `dl.armbian.com` (the main per-board download)._

| board | support | newest version | name |
| --- | --- | --- | --- |
| pine64 | `csc` | 26.8.1 | Pine A64 / A64+ |

## Missing download images

_**8** `conf` (standard-support) boards absent from `dl.armbian.com` — only nightly/appliance, or nowhere._

| board | name | present in |
| --- | --- | --- |
| bananapipro | Banana Pi Pro | Community |
| boardcon-em3588 | EM3588 | CI |
| mba62xx-tqma62xx | MBa62xx | CI |
| mba67xx-tqma67xx | MBa67xx | CI |
| milkv-duos-arm | Duo S (ARM) | CI |
| milkv-duos-riscv | Duo S (RISC-V) | CI |
| odroidu2 | Odroid U2 | CI |
| turris-omnia | Turris Omnia | CI |

<!-- download-images:end -->
