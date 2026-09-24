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

**65** boards — **57** operational, **8** broken.

Reconcile made: 2026-09-24 19:14 UTC

**Operational**

| Board | IP address | Boot | Link | Switch |
|:--|:--|:--|--:|:--|
| Arduino UNO Q 01 | 10.0.20.131 | local | Wi-Fi 5 | Zyxel NWA130BE |
| Banana Pi CM4IO 01 | 10.0.50.51 | local | 1 GbE | Netgear S3300 (41) |
| Banana Pi M2 Ultra 01 | 10.0.50.83 | local | 1 GbE | TP-Link SG3428X (13) |
| Banana Pi M2Pro 01 | 10.0.50.23 | local | 1 GbE | Aruba 2540 (23) |
| Banana Pi M5 01 | 10.0.50.63 | local | 1 GbE | Netgear S3300 (6) |
| Banana Pi M7 01 | 10.0.50.12 | local | 1 GbE | TP-Link SG3218XP-M2 (10) |
| Banana Pi R2 01 | 10.0.50.64 | local | 1 GbE | Netgear S3300 (27) |
| Banana Pi R3 Mini 01 | 10.0.50.42 | local | 1 GbE | Aruba 2540 (45) |
| BananaPi BPI-F3 01 | 10.0.50.30 | local | 1 GbE | Netgear S3300 (46) |
| Clearfog Pro 01 | 10.0.50.67 | local | 1 GbE | TP-Link SG3428X (12) |
| Cubie A5E 01 | 10.0.50.47 | local | 1 GbE | Netgear S3300 (4) |
| Cubietruck 01 | 10.0.50.82 | local | 1 GbE | Netgear S3300 (24) |
| Cubox i2eX/i4 01 | 10.0.50.81 | local | 1 GbE | TP-Link SG3428X (9) |
| Espressobin 01 | 10.0.50.56 | local | 1 GbE | TP-Link SG3428X (11) |
| Helios4 01 | 10.0.50.75 | local | 1 GbE | Aruba 2540 (40) |
| Inovato Quadra 01 | 10.0.50.58 | local | 100 MbE | Netgear S3300 (21) |
| Khadas Edge2 01 | 10.0.20.134 | local | — | — |
| Khadas VIM2 01 | 10.0.50.28 | local | 1 GbE | Netgear S3300 (28) |
| Khadas VIM4 01 | 10.0.50.14 | local | 1 GbE | Aruba 2540 (21) |
| Mekotronics R58HD 01 | 10.0.50.21 | local | 1 GbE | Aruba 2540 (38) |
| NanoPi Fire3 01 | 10.0.50.16 | local | 1 GbE | Aruba 2540 (33) |
| NanoPi K2 01 | 10.0.50.34 | local | 1 GbE | Netgear S3300 (7) |
| NanoPi M4V2 01 | 10.0.50.49 | local | 1 GbE | Aruba 2540 (5) |
| NanoPi M5 01 | 10.0.50.54 | local | 1 GbE | Aruba 2540 (14) |
| NanoPi M6 01 | 10.0.50.24 | local | 1 GbE | Aruba 2540 (9) |
| NanoPi Neo 2 Black 01 | 10.0.50.19 | local | 1 GbE | Aruba 2540 (6) |
| NanoPi Neo 3 01 | 10.0.50.43 | local | 1 GbE | TP-Link SG3428X (17) |
| NanoPi R6S 01 | 10.0.50.35 | local | 1 GbE | Aruba 2540 (41) |
| NanoPi R76S 01 | 10.0.50.20 | local | 1 GbE | Aruba 2540 (31) |
| Odroid C2 01 | 10.0.50.22 | local | 1 GbE | Netgear S3300 (5) |
| Odroid C4 01 | 10.0.50.26 | local | 1 GbE | Aruba 2540 (39) |
| Odroid M1 01 | 10.0.50.50 | local | 1 GbE | Netgear S3300 (13) |
| Odroid N2 01 | 10.0.50.15 | local | 1 GbE | Netgear S3300 (14) |
| Odroid XU4 01 | 10.0.50.36 | local | 1 GbE | Netgear S3300 (40) |
| Orange Pi 3 01 | 10.0.50.41 | local | 1 GbE | Aruba 2540 (3) |
| Orange Pi 5 Plus 01 | 10.0.50.55 | local | 1 GbE | Netgear S3300 (20) |
| Orange Pi Lite 2 01 | 10.0.20.125 | local | Wi-Fi 5 | Zyxel NWA130BE |
| Orange Pi One+ 01 | 10.0.50.37 | local | 1 GbE | Netgear S3300 (31) |
| Orange Pi Zero2 01 | 10.0.50.74 | local | 1 GbE | Netgear S3300 (45) |
| Radxa Dragon Q6A 01 | 10.0.50.11 | local | 1 GbE | Netgear S3300 (9) |
| Radxa ZERO 3 01 | 10.0.20.185 | local | Wi-Fi 6 | Zyxel NWA130BE |
| Raspberry Pi 3B | 10.0.50.17 | local | 100 MbE | Netgear S3300 (8) |
| Raspberry Pi 5B | 10.0.50.10 | local | 1 GbE | Netgear S3300 (1) |
| Raspberry Pi Zero 2W | 10.0.20.187 | local | Wi-Fi 4 | Zyxel NWA130BE |
| ROCK 2F 01 | 10.0.20.164 | local | Wi-Fi 6 | Zyxel NWA130BE |
| Rock 5B 02 | 10.0.50.32 | local | 1 GbE | Netgear S3300 (19) |
| Rock 5B Plus 01 | 10.0.50.59 | local | 1 GbE | Netgear S3300 (22) |
| Rock 5T 01 | 10.0.50.52 | local | 1 GbE | Aruba 2540 (48) |
| Rockpi E 01 | 10.0.50.66 | local | 100 MbE | TP-Link SG3428X (15) |
| Rockpi S 01 | 10.0.50.18 | local | 100 MbE | Netgear S3300 (25) |
| RockPro 64 01 | 10.0.50.31 | local | 1 GbE | Netgear S3300 (30) |
| SpacemiT K3 Pico-ITX 01 | 10.0.50.44 | local | 10 GbE | Aruba 2540 (52) |
| Tinker Board 01 | 10.0.50.33 | local | 1 GbE | Netgear S3300 (15) |
| Udoo 01 | 10.0.50.25 | local | 1 GbE | Netgear S3300 (44) |
| UEFI arm64 01 | 10.0.50.45 | local | 10 GbE | Netgear XS712T (6) |
| UEFI x86 01 | 10.0.50.40 | local | 1 GbE | Netgear S3300 (2) |
| ZeroPi 01 | 10.0.50.57 | local | 1 GbE | Aruba 2540 (36) |

**Broken**

| Board | IP address | Boot | Link | Switch |
|:--|:--|:--|--:|:--|
| BigTreeTech CB1 01 | 10.0.50.62 | local | 100 MbE | Netgear S3300 (10) |
| Khadas VIM1 01 | 10.0.50.71 | local | 100 MbE | Netgear S3300 (29) |
| Khadas VIM1S 01 | 10.0.50.48 | local | 100 MbE | Netgear S3300 (33) |
| Khadas VIM3 01 | 10.0.50.39 | local | 1 GbE | Netgear S3300 (37) |
| Mekotronics R58S2 01 | 10.0.50.38 | local | 1 GbE | Aruba 2540 (34) |
| Orange Pi 5 01 | 10.0.50.46 | local | 1 GbE | Netgear S3300 (23) |
| OrangePi 3 LTS 01 | 10.0.50.60 | local | 1 GbE | Netgear S3300 (32) |
| Rock 5B 01 | 10.0.50.13 | local | 1 GbE | Netgear S3300 (18) |

<!-- BOARDS-STOP -->
