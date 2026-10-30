---
title: Datacenter boards
seo_title: "Armbian datacenter boards: fleet inventory & status"
description: "The boards in the Armbian test datacenter — which are operational or broken — reconciled automatically from the datacenter inventory."
---
# Datacenter boards

The boards in the Armbian [test datacenter](/contribute/datacenter/). This
inventory is refreshed by the reconcile action (`Inventory: scan & reconcile`
in the autotests repo): it scans the datacenter and opens a pull request to
update the table — the same mechanism behind the
[Wi-Fi performance](wifi-performance.md) results.

<!-- BOARDS-START -->

**83** boards — **80** operational, **3** broken.

Reconcile made: 2026-10-30 19:13 UTC

**Operational**

| Board | IP address | Boot | Link | Switch |
|:--|:--|:--|--:|:--|
| A64 OLinuXino 01 | 10.0.50.78 | local | 1 GbE | TP-Link SG3428X (13) |
| Banana Pi CM4IO 01 | 10.0.50.64 | local | 1 GbE | Netgear S3300 (41) |
| Banana Pi M2 Ultra 01 | 10.0.50.83 | local | 1 GbE | Netgear S3300 (46) |
| Banana Pi M2Pro 01 | 10.0.50.13 | local | 1 GbE | Netgear S3300 (47) |
| Banana Pi M5 01 | 10.0.50.63 | local | 1 GbE | Netgear S3300 (6) |
| Banana Pi M7 01 | 10.0.50.12 | local | 2.5 GbE | Netgear XS508M (4) |
| Banana Pi R2 01 | 10.0.50.46 | local | 1 GbE | Netgear S3300 (27) |
| Banana Pi R3 Mini 01 | 10.0.50.42 | local | 2.5 GbE | Netgear XS508M (5) |
| Banana Pi R4 01 | 10.0.50.66 | local | 1 GbE | TP-Link SG3428X (12) |
| BananaPi BPI-F3 01 | 10.0.50.23 | local | 1 GbE | Netgear S3300 (16) |
| BananaPi BPI-M4-Zero 01 | 10.0.20.129 | local | Wi-Fi 5 | Zyxel NWA130BE |
| BananaPi M4 01 | 10.0.50.84 | local | 100 MbE | Aruba 2540 (4) |
| BananaPi W2 01 | 10.0.50.24 | local | 1 GbE | TP-Link SG3428X (22) |
| Cubie A5E 01 | 10.0.50.47 | local | 1 GbE | Netgear S3300 (4) |
| Cubieboard 1 01 | 10.0.50.86 | local | 100 MbE | Aruba 2540 (30) |
| Cubieboard 4 01 | 10.0.50.72 | local | 1 GbE | TP-Link SG3428X (7) |
| Cubietruck 01 | 10.0.50.82 | local | 1 GbE | Netgear S3300 (24) |
| Dragon Q6A 01 | 10.0.50.11 | local | 1 GbE | Netgear S3300 (9) |
| Edge2 01 | 10.0.50.120 | local | Wi-Fi 6 | Zyxel NWA130BE |
| Espressobin 01 | 10.0.50.56 | local | 1 GbE | TP-Link SG3428X (11) |
| Helios4 01 | 10.0.50.75 | local | 1 GbE | TP-Link SG3428X (5) |
| K3 Pico-ITX 01 | 10.0.50.44 | local | 10 GbE | TP-Link SG3428XPP-M2 (25) |
| MUSE Book 01 | 10.0.50.89 | local | 100 MbE | Netgear XS712T (2) |
| MusePi Pro 01 | 10.0.50.14 | local | 1 GbE | Netgear S3300 (10) |
| NanoPC T6 Plus 01 | 10.0.50.36 | local | 2.5 GbE | TP-Link SG3428XPP-M2 (18) |
| NanoPi Fire3 01 | 10.0.50.16 | local | 100 MbE | Aruba 2540 (33) |
| NanoPi K2 01 | 10.0.50.34 | local | 1 GbE | Netgear S3300 (7) |
| NanoPi M4 03 | 10.0.50.71 | local | 1 GbE | Aruba 2540 (24) |
| NanoPi M4V2 01 | 10.0.50.49 | local | 1 GbE | Aruba 2540 (10) |
| NanoPi M5 01 | 10.0.50.59 | local | 1 GbE | TP-Link SG3428X (9) |
| Nanopi M6 01 | 10.0.50.68 | local | 1 GbE | Aruba 2540 (8) |
| Nanopi M6 V2 01 | 10.0.50.76 | local | 1 GbE | Netgear S3300 (20) |
| NanoPi Neo 2 Black 01 | 10.0.50.62 | local | 1 GbE | Aruba 2540 (6) |
| NanoPi Neo 3 01 | 10.0.50.43 | local | 1 GbE | Netgear S3300 (48) |
| NanoPi R3S LTS 01 | 10.0.50.70 | local | 1 GbE | TP-Link SG3428X (18) |
| NanoPi R6S 01 | 10.0.50.35 | local | 2.5 GbE | Netgear XS508M (1) |
| NanoPi R76S 01 | 10.0.50.54 | local | 2.5 GbE | Netgear XS508M (2) |
| Odroid C2 01 | 10.0.50.22 | local | 1 GbE | Netgear S3300 (5) |
| Odroid C4 01 | 10.0.50.26 | local | 1 GbE | TP-Link SG3428X (14) |
| Odroid M1 01 | 10.0.50.50 | local | 1 GbE | Netgear S3300 (13) |
| Odroid N2 01 | 10.0.50.15 | local | 1 GbE | Netgear S3300 (14) |
| Odroid XU4 01 | 10.0.50.20 | local | 1 GbE | Netgear S3300 (40) |
| Orange Pi 3 01 | 10.0.50.41 | local | 1 GbE | Aruba 2540 (3) |
| Orange Pi 4 02 | 10.0.50.77 | local | 1 GbE | Aruba 2540 (39) |
| Orange Pi 4 LTS 01 | 10.0.50.80 | local | 1 GbE | Aruba 2540 (41) |
| Orange Pi 5 01 | 10.0.50.60 | local | 1 GbE | Netgear S3300 (18) |
| Orange Pi 5+ 01 | 10.0.50.55 | local | 2.5 GbE | Netgear XS508M (7) |
| Orange Pi Lite 2 01 | 10.0.20.125 | local | Wi-Fi 5 | Flasher |
| Orange Pi One+ 01 | 10.0.50.37 | local | 1 GbE | Netgear S3300 (31) |
| Orange Pi PC + 01 | 10.0.50.38 | local | 100 MbE | Netgear S3300 (38) |
| Orange Pi Prime 01 | 10.0.50.87 | local | 1 GbE | Aruba 2540 (35) |
| Orange Pi Zero2 01 | 10.0.50.74 | local | 1 GbE | Netgear S3300 (45) |
| Orange Pi+ 2E 02 | 10.0.50.85 | local | 1 GbE | Aruba 2540 (29) |
| OrangePi 3 LTS 01 | 10.0.50.30 | local | 1 GbE | Netgear S3300 (32) |
| Quadra 01 | 10.0.50.58 | local | 100 MbE | Netgear S3300 (2) |
| R58HD 01 | 10.0.50.21 | local | 1 GbE | Aruba 2540 (38) |
| R58S2 01 | 10.0.50.52 | local | 1 GbE | Aruba 2540 (34) |
| Raspberry Pi 3B | 10.0.50.17 | local | 100 MbE | Netgear S3300 (8) |
| Raspberry Pi 5B | 10.0.50.10 | local | 1 GbE | Netgear S3300 (1) |
| Raspberry Pi Zero 2W | 10.0.20.187 | local | Wi-Fi 4 | Zyxel NWA130BE |
| ROCK 2F 01 | 10.0.20.164 | local | — | — |
| Rock 5B 01 | 10.0.50.53 | local | 2.5 GbE | TP-Link SG3428XPP-M2 (4) |
| Rock 5B 02 | 10.0.50.65 | local | 2.5 GbE | TP-Link SG3428XPP-M2 (6) |
| Rock 5B+ 01 | 10.0.50.27 | local | 2.5 GbE | TP-Link SG3428XPP-M2 (2) |
| Rock 5T 01 | 10.0.50.51 | local | 2.5 GbE | TP-Link SG3428XPP-M2 (22) |
| Rockpi 4B 01 | 10.0.50.73 | local | 1 GbE | Netgear S3300 (35) |
| Rockpi 4C 01 | 10.0.50.79 | local | 1 GbE | Aruba 2540 (43) |
| Rockpi E 01 | 10.0.50.67 | local | 100 MbE | TP-Link SG3428X (15) |
| Rockpi S 01 | 10.0.50.18 | local | 100 MbE | Netgear S3300 (25) |
| RockPro 64 01 | 10.0.50.31 | local | 1 GbE | Netgear S3300 (30) |
| Tinker Board 01 | 10.0.50.33 | local | 1 GbE | Netgear S3300 (15) |
| Tinker Board 2 01 | 10.0.50.88 | local | 1 GbE | Aruba 2540 (25) |
| UEFI arm64 01 | 10.0.50.45 | local | 10 GbE | Netgear XS712T (6) |
| UEFI x86 01 | 10.0.50.40 | local | 1 GbE | Netgear S3300 (17) |
| VIM1 01 | 10.0.50.48 | local | 100 MbE | Netgear S3300 (29) |
| VIM1S 01 | 10.0.50.32 | local | 100 MbE | Netgear S3300 (33) |
| VIM2 01 | 10.0.50.28 | local | 1 GbE | Netgear S3300 (28) |
| VIM4 01 | 10.0.50.19 | local | 1 GbE | Aruba 2540 (21) |
| ZERO 3 01 | 10.0.20.185 | local | Wi-Fi 6 | Zyxel NWA130BE |
| ZeroPi 01 | 10.0.50.57 | local | 1 GbE | Aruba 2540 (36) |

**Broken**

| Board | IP address | Boot | Link | Switch |
|:--|:--|:--|--:|:--|
| UEFI/DT arm64 01 | 10.0.50.69 | local | 1 GbE | TP-Link SG3428X (21) |
| UNO Q 01 | 10.0.20.131 | local | Wi-Fi 5 | Zyxel NWA130BE |
| VIM3 01 | 10.0.50.39 | local | 1 GbE | Netgear S3300 (42) |

<!-- BOARDS-STOP -->
