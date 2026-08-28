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

**74** boards — **58** operational, **16** broken.

Reconcile made: 2026-08-28 10:18 UTC

**Operational**

| Board | IP address | Boot | Link | Switch |
|:--|:--|:--|--:|:--|
| Arduino UNO Q 01 | 10.0.20.131 | local | Wi-Fi 5 | Zyxel NWA130BE |
| Banana Pi CM4IO 01 | 10.0.50.12 | local | 1 GbE | Netgear S3300-52X-PoE+ (43) |
| Banana Pi M2 Ultra 01 | 10.0.50.47 | local | 1 GbE | TP-Link TL-SG3428X (13) |
| Banana Pi M2Pro 01 | 10.0.50.43 | local | 1 GbE | Netgear S3300-52X-PoE+ (47) |
| Banana Pi M5 01 | 10.0.50.55 | local | 1 GbE | Netgear GS348 (19) |
| Banana Pi Pro 01 | 10.0.50.52 | local | 100 MbE | Netgear GS348 (8) |
| BananaPi BPI-F3 01 | 10.0.50.70 | local | 1 GbE | Netgear S3300-52X-PoE+ (46) |
| Clearfog Pro 01 | 10.0.50.42 | local | 1 GbE | TP-Link TL-SG3428X (12) |
| Cubie A5E 01 | 10.0.50.72 | local | 1 GbE | Netgear S3300-52X-PoE+ (4) |
| Cubietruck 01 | 10.0.50.49 | local | 1 GbE | TP-Link TL-SG3428X (14) |
| Cubox i2eX/i4 01 | 10.0.50.63 | local | 1 GbE | Netgear GS348 (32) |
| Espressobin 01 | 10.0.50.56 | local | 1 GbE | TP-Link TL-SG3428X (11) |
| Helios4 01 | 10.0.50.58 | local | 1 GbE | Netgear GS348 (11) |
| Khadas VIM2 01 | 10.0.50.28 | local | 1 GbE | Netgear GS348 (13) |
| Khadas VIM3 01 | 10.0.50.38 | local | 1 GbE | Netgear GS348 (36) |
| Le potato 01 | 10.0.50.75 | local | 100 MbE | Netgear GS348 (12) |
| Mekotronics R58S2 01 | 10.0.50.19 | local | 1 GbE | Netgear GS348 (48) |
| NanoPi Duo 01 | 10.0.50.48 | local | 100 MbE | Netgear GS348 (31) |
| NanoPi K2 01 | 10.0.50.76 | local | 1 GbE | Netgear GS348 (20) |
| NanoPi M4V2 01 | 10.0.50.97 | local | 1 GbE | Netgear S3300-52X-PoE+ (7) |
| NanoPi M5 01 | 10.0.50.35 | local | 1 GbE | Netgear S3300-52X-PoE+ (5) |
| NanoPi Neo 2 Black 01 | 10.0.50.14 | local | 1 GbE | — |
| NanoPi Neo 3 01 | 10.0.50.20 | local | 1 GbE | TP-Link TL-SG3428X (17) |
| NanoPi R1 01 | 10.0.50.59 | local | 1 GbE | Netgear GS348 (14) |
| Nanopi R2S 01 | 10.0.50.65 | local | 1 GbE | Netgear S3300-52X-PoE+ (12) |
| NanoPi R6S 01 | 10.0.50.40 | local | 1 GbE | Netgear S3300-52X-PoE+ (44) |
| NanoPi R76S 01 | 10.0.50.77 | local | 2.5 GbE | Netgear XS508M (7) |
| Odroid C1 01 | 10.0.50.27 | local | 1 GbE | Netgear GS348 (28) |
| Odroid C2 01 | 10.0.50.87 | local | 1 GbE | Netgear GS348 (7) |
| Odroid C4 01 | 10.0.50.26 | local | 1 GbE | TP-Link TL-SG3428X (10) |
| Odroid M1 01 | 10.0.50.50 | local | 1 GbE | Netgear S3300-52X-PoE+ (38) |
| Odroid N2 01 | 10.0.60.10 | local | 1 GbE | Netgear S3300-52X-PoE+ (14) |
| Odroid XU4 01 | 10.0.50.51 | local | 1 GbE | Netgear S3300-52X-PoE+ (19) |
| Orange Pi 3 01 | 10.0.50.57 | local | 1 GbE | Netgear S3300-52X-PoE+ (31) |
| Orange Pi 5 01 | 10.0.50.39 | local | 1 GbE | TP-Link SG3218XP-M2 (5) |
| Orange Pi 5 Plus 02 | 10.0.50.33 | local | 2.5 GbE | — |
| Orange Pi One+ 01 | 10.0.50.37 | local | 1 GbE | TP-Link TL-SG3428X (18) |
| Orange Pi PC2 01 | 10.0.50.68 | local | 1 GbE | TP-Link TL-SG3428X (22) |
| Orange Pi Prime 01 | 10.0.50.16 | local | 1 GbE | Netgear S3300-52X-PoE+ (23) |
| Orange Pi R1 01 | 10.0.50.25 | local | Wi-Fi 4 | Zyxel NWA130BE |
| Orange Pi Win 01 | 10.0.50.24 | local | 1 GbE | Netgear S3300-52X-PoE+ (13) |
| Orange Pi Zero 02 | 10.0.50.46 | local | Wi-Fi 4 | Zyxel NWA130BE |
| Orange Pi Zero2 01 | 10.0.50.74 | local | 1 GbE | Netgear S3300-52X-PoE+ (45) |
| OrangePi 3 LTS 01 | 10.0.50.60 | local | 1 GbE | TP-Link TL-SG3428X (19) |
| Radxa Dragon Q6A 01 | 10.0.50.11 | local | 1 GbE | Netgear S3300-52X-PoE+ (9) |
| Radxa ZERO 3 01 | 10.0.20.185 | local | Wi-Fi 6 | Zyxel NWA130BE |
| Raspberry Pi 01 | 10.0.50.15 | local | 1 GbE | Netgear S3300-52X-PoE+ (1) |
| Raspberry Pi 02 | 10.0.50.22 | local | 100 MbE | Netgear GS348 (21) |
| ROCK 2F 01 | 10.0.20.164 | local | Wi-Fi 6 | Zyxel NWA130BE |
| Rock 5B 01 | 10.0.50.69 | local | 2.5 GbE | Netgear XS508M (6) |
| Rock 5B 02 | 10.0.50.17 | local | 2.5 GbE | Netgear XS508M (5) |
| Rock 5B Plus 01 | 10.0.50.41 | local | 2.5 GbE | Netgear XS508M (4) |
| Rock 5T 01 | 10.0.50.66 | local | 2.5 GbE | TP-Link SG3218XP-M2 (12) |
| Rockpi E 01 | 10.0.50.61 | local | 1 GbE | TP-Link TL-SG3428X (16) |
| SpacemiT K3 Pico-ITX 01 | 10.0.50.44 | local | 1 GbE | Netgear S3300-52X-PoE+ (52) |
| Tanix TX6 01 | 10.0.50.21 | local | 100 MbE | Netgear GS348 (46) |
| Tinker Board 01 | 10.0.50.29 | local | 1 GbE | Netgear S3300-52X-PoE+ (15) |
| UEFI x86 01 | 10.0.50.53 | local | 1 GbE | Netgear S3300-52X-PoE+ (2) |

**Broken**

| Board | IP address | Boot | Link | Switch |
|:--|:--|:--|--:|:--|
| A64 OLinuXino 01 | 10.0.20.150 | local | 1 GbE | — |
| BigTreeTech CB1 01 | 10.0.50.62 | local | Wi-Fi 4 | Zyxel NWA130BE |
| Inovato Quadra 01 | 10.0.50.36 | local | 100 MbE | Netgear GS348 (17) |
| Khadas VIM1 01 | 10.0.50.71 | local | 100 MbE | Netgear GS348 (3) |
| NanoPC T6 LTS 01 | 10.0.50.30 | local | 2.5 GbE | TP-Link SG3218XP-M2 (8) |
| NanoPi M6 01 | 10.0.50.18 | local | 1 GbE | Netgear S3300-52X-PoE+ (39) |
| NanoPi M6 03 | 10.0.50.67 | local | Wi-Fi 5 | Zyxel NWA130BE |
| NanoPi M6 04 | 10.0.50.164 | local | 1 GbE | — |
| Orange Pi Lite 2 01 | 10.0.20.125 | local | Wi-Fi 5 | Zyxel NWA130BE |
| Orange Pi Zero Plus 01 | 10.0.50.54 | local | 1 GbE | TP-Link TL-SG3428X (20) |
| Pine H64 01 | 10.0.50.34 | local | 1 GbE | TP-Link TL-SG3428X (9) |
| Rockpi 4B+ 01 | 10.0.50.64 | local | Wi-Fi 5 | Zyxel NWA130BE |
| Tinker Board 2 01 | 10.0.50.23 | local | 1 GbE | TP-Link TL-SG3428X (15) |
| Udoo 01 | 10.0.50.13 | local | 1 GbE | Netgear S3300-52X-PoE+ (37) |
| UEFI arm64 01 | 10.0.50.45 | local | 10 GbE | Netgear XS712T (6) |
| Z28 PRO 01 | 10.0.50.73 | local | 1 GbE | Netgear S3300-52X-PoE+ (17) |

<!-- BOARDS-STOP -->
