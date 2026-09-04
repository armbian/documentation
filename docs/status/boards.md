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

**73** boards — **38** operational, **35** broken.

Reconcile made: 2026-09-04 15:55 UTC

**Operational**

| Board | IP address | Boot | Link | Switch |
|:--|:--|:--|--:|:--|
| Banana Pi CM4IO 01 | 10.0.50.51 | local | 1 GbE | Netgear S3300 (43) |
| Banana Pi M2 Ultra 01 | 10.0.50.83 | local | 1 GbE | TP-Link SG3428X (13) |
| Banana Pi M2Pro 01 | 10.0.50.80 | local | 1 GbE | Netgear S3300 (47) |
| BananaPi BPI-F3 01 | 10.0.50.53 | local | 1 GbE | Netgear S3300 (46) |
| BigTreeTech CB1 01 | 10.0.50.62 | local | Wi-Fi 4 | Zyxel NWA130BE |
| Clearfog Pro 01 | 10.0.50.24 | local | 1 GbE | TP-Link SG3428X (12) |
| Cubie A5E 01 | 10.0.50.72 | local | 1 GbE | Netgear S3300 (4) |
| Cubietruck 01 | 10.0.50.82 | local | 1 GbE | TP-Link SG3428X (14) |
| Espressobin 01 | 10.0.50.56 | local | 1 GbE | TP-Link SG3428X (11) |
| Khadas VIM4 01 | 10.0.50.14 | local | 1 GbE | Netgear S3300 (40) |
| Mekotronics R58HD 01 | 10.0.50.21 | local | 1 GbE | — |
| Mekotronics R58S2 01 | 10.0.50.38 | local | 1 GbE | Aruba 2540 (46) |
| NanoPi M4V2 01 | 10.0.50.49 | local | 1 GbE | Aruba 2540 (5) |
| NanoPi M5 01 | 10.0.50.54 | local | 1 GbE | Aruba 2540 (44) |
| NanoPi M6 01 | 10.0.50.64 | local | 1 GbE | Aruba 2540 (45) |
| NanoPi Neo 3 01 | 10.0.50.70 | local | 1 GbE | TP-Link SG3428X (17) |
| NanoPi R6S 01 | 10.0.50.35 | local | 1 GbE | Aruba 2540 (41) |
| Odroid C4 01 | 10.0.50.26 | local | 1 GbE | TP-Link SG3428X (10) |
| Odroid M1 01 | 10.0.50.50 | local | 1 GbE | Netgear S3300 (38) |
| Odroid N2 01 | 10.0.50.15 | local | 1 GbE | Netgear S3300 (29) |
| Odroid XU4 01 | 10.0.50.68 | local | 1 GbE | Netgear S3300 (19) |
| Orange Pi 3 01 | 10.0.50.41 | local | 1 GbE | Netgear S3300 (31) |
| Orange Pi 5 Plus 01 | 10.0.50.55 | local | 1 GbE | Netgear S3300 (8) |
| Orange Pi One+ 01 | 10.0.50.37 | local | 1 GbE | TP-Link SG3428X (18) |
| Orange Pi PC2 01 | 10.0.50.58 | local | 1 GbE | TP-Link SG3428X (22) |
| Orange Pi Prime 01 | 10.0.50.16 | local | 1 GbE | Netgear S3300 (23) |
| Orange Pi Zero Plus 01 | 10.0.50.78 | local | 1 GbE | TP-Link SG3428X (20) |
| Orange Pi Zero2 01 | 10.0.50.74 | local | 1 GbE | Netgear S3300 (45) |
| OrangePi 3 LTS 01 | 10.0.50.60 | local | 1 GbE | TP-Link SG3428X (19) |
| Radxa Dragon Q6A 01 | 10.0.50.11 | local | 1 GbE | Netgear S3300 (9) |
| Raspberry Pi 01 | 10.0.50.10 | local | 1 GbE | Netgear S3300 (1) |
| Rock 5B 01 | 10.0.50.13 | local | 2.5 GbE | Netgear XS508M (6) |
| Rock 5B 02 | 10.0.50.32 | local | 2.5 GbE | Netgear XS508M (5) |
| Rock 5B Plus 01 | 10.0.50.47 | local | 2.5 GbE | Netgear XS508M (4) |
| Rockpi E 01 | 10.0.50.66 | local | 1 GbE | TP-Link SG3428X (16) |
| SpacemiT K3 Pico-ITX 01 | 10.0.50.44 | local | 1 GbE | Netgear S3300 (52) |
| Tinker Board 01 | 10.0.50.33 | local | 1 GbE | Netgear S3300 (15) |
| UEFI x86 01 | 10.0.50.40 | local | 1 GbE | Netgear S3300 (2) |

**Broken**

| Board | IP address | Boot | Link | Switch |
|:--|:--|:--|--:|:--|
| Arduino UNO Q 01 | 10.0.20.131 | local | Wi-Fi 5 | Zyxel NWA130BE |
| Banana Pi M5 01 | 10.0.50.63 | local | 1 GbE | Netgear GS348 (19) |
| Banana Pi M7 01 | 10.0.50.12 | local | 2.5 GbE | TP-Link SG3218XP-M2 (10) |
| Banana Pi Pro 01 | 10.0.50.43 | local | 100 MbE | Netgear GS348 (8) |
| Banana Pi R2 01 | 10.0.50.76 | local | 1 GbE | Netgear S3300 (24) |
| Cubox i2eX/i4 01 | 10.0.50.81 | local | 1 GbE | Netgear GS348 (32) |
| Helios4 01 | 10.0.50.42 | local | 1 GbE | Netgear GS348 (11) |
| Inovato Quadra 01 | 10.0.50.39 | local | 100 MbE | Netgear GS348 (17) |
| Khadas Edge2 01 | 10.0.20.134 | local | — | — |
| Khadas VIM1 01 | 10.0.50.71 | local | 100 MbE | Netgear GS348 (3) |
| Khadas VIM1S 01 | 10.0.50.48 | local | Wi-Fi 5 | Zyxel NWA130BE |
| Khadas VIM2 01 | 10.0.50.28 | local | 1 GbE | Netgear GS348 (13) |
| Khadas VIM3 01 | 10.0.50.46 | local | 1 GbE | Netgear GS348 (36) |
| Le potato 01 | 10.0.50.23 | local | 100 MbE | Netgear GS348 (12) |
| NanoPC T6 LTS 01 | 10.0.50.30 | local | 2.5 GbE | TP-Link SG3218XP-M2 (8) |
| NanoPi 6 series 01 | 10.0.50.79 | local | 1 GbE | Aruba 2540 (4) |
| NanoPi Duo 01 | 10.0.50.84 | local | 100 MbE | Netgear GS348 (31) |
| NanoPi K2 01 | 10.0.50.29 | local | 1 GbE | Netgear GS348 (20) |
| NanoPi Neo 2 Black 01 | 10.0.50.19 | local | 1 GbE | — |
| NanoPi R1 01 | 10.0.50.59 | local | 1 GbE | Netgear GS348 (14) |
| Nanopi R2S 01 | 10.0.50.65 | local | 1 GbE | — |
| NanoPi R76S 01 | 10.0.50.20 | local | 2.5 GbE | TP-Link SG3218XP-M2 (9) |
| Odroid C1 01 | 10.0.50.27 | local | 1 GbE | Netgear GS348 (28) |
| Odroid C2 01 | 10.0.50.22 | local | 1 GbE | Netgear GS348 (7) |
| Orange Pi 5 01 | 10.0.50.18 | local | 1 GbE | TP-Link SG3218XP-M2 (5) |
| Orange Pi Lite 2 01 | 10.0.20.125 | local | Wi-Fi 5 | Zyxel NWA130BE |
| Orange Pi Zero 01 | 10.0.50.85 | local | 100 MbE | Netgear GS348 (6) |
| Pine H64 01 | 10.0.50.34 | local | 1 GbE | TP-Link SG3428X (9) |
| Radxa ZERO 3 01 | 10.0.20.185 | local | Wi-Fi 6 | Zyxel NWA130BE |
| Raspberry Pi 02 | 10.0.50.17 | local | 100 MbE | Netgear GS348 (21) |
| ROCK 2F 01 | 10.0.20.164 | local | Wi-Fi 6 | Zyxel NWA130BE |
| Rock 5T 01 | 10.0.50.52 | local | 2.5 GbE | TP-Link SG3218XP-M2 (12) |
| Rockpi 4B 01 | 10.0.50.69 | local | 1 GbE | Netgear S3300 (27) |
| Udoo 01 | 10.0.50.67 | local | 1 GbE | Netgear S3300 (37) |
| UEFI arm64 01 | 10.0.50.45 | local | 10 GbE | Netgear XS712T (6) |

<!-- BOARDS-STOP -->
