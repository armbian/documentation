---
title: Tested boards
seo_title: "Armbian tested boards: automated fleet test results"
description: "Automated per-board test results from the Armbian autotests fleet — upgrade, reboot, performance, DVFS and network checks across single-board computers."
---
# Tested boards

Every board in the Armbian test datacenter runs an automated pipeline — a nightly **upgrade**, a **reboot**, hardware **performance** and **DVFS** checks and a **network** throughput test — before being restored to the stable release. Each board below is a **card** — collapsed to its name and pass/fail; expand it for the per-module results, timings and power. The set is the **current status**: the most recent test of every board.

The list is refreshed automatically by the Armbian autotests fleet: a scheduled job reads the fleet's rolling test results and opens a pull request to update this page — the same mechanism used for the [datacenter boards](/status/boards/) and [Wi-Fi performance](/status/wifi-performance/) pages.

Legend: ✅ pass · ❌ fail · ⏭️ skipped · ➖ not run.

<!-- FLEET-START -->

**82** boards — **45** passed, **37** failed. Each row is the board's most recent test.

| Board | Status | Upgrade | Reboot | Perf | DVFS | Network | Kernel | Tested |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--|--:|
| Arduino UNO Q 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 7.1.7-edge-qrb2210 | 2026-08-11 |
| Banana Pi CM4IO 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-meson64 | 2026-08-11 |
| Banana Pi M2 Ultra 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.12.93-legacy-sunxi | 2026-08-11 |
| Banana Pi M2Pro 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-meson64 | 2026-08-11 |
| Banana Pi M5 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-meson64 | 2026-08-11 |
| Banana Pi Pro 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.12.93-legacy-sunxi | 2026-08-11 |
| BananaPi BPI-F3 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| BigTreeTech CB1 01 | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | — | 2026-08-11 |
| Clearfog Pro 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Cubie A5E 01 | ❌ | ⏭️ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-06-23 |
| Cubietruck 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-sunxi | 2026-08-11 |
| Espressobin 01 | ✅ | ⏭️ | ⏭️ | ✅ | ✅ | ✅ | 6.18.42-current-mvebu64 | 2026-08-11 |
| Helios4 01 | ✅ | ✅ | ✅ | ✅ | ➖ | ✅ | 6.6.142-current-mvebu | 2026-08-11 |
| Inovato Quadra 01 | ❌ | ✅ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-08-09 |
| Khadas VIM1 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 6.18.34-current-meson64 | 2026-06-26 |
| Khadas VIM2 01 | ❌ | ✅ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-08-09 |
| Khadas VIM3 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-meson64 | 2026-08-11 |
| Mekotronics R58S2 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Minisforum MS R1 | ✅ | ⏭️ | ⏭️ | ✅ | ❌ | ✅ | 7.0.11-edge-arm64 | 2026-07-03 |
| NanoPC T6 LTS 01 | ❌ | ⏭️ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-07-04 |
| NanoPi Duo 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.12.93-legacy-sunxi | 2026-08-11 |
| NanoPi K2 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-meson64 | 2026-08-11 |
| NanoPi M4V2 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-rockchip64 | 2026-08-11 |
| NanoPi M5 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-10 |
| NanoPi Neo 2 Black 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| NanoPi Neo 3 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-rockchip64 | 2026-08-11 |
| NanoPi R1 01 | ✅ | ⏭️ | ⏭️ | ✅ | ✅ | ✅ | 6.18.38-current-sunxi | 2026-08-11 |
| NanoPi R1 02 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-sunxi | 2026-06-24 |
| NanoPi R1 05 | ❌ | ⏭️ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-06-19 |
| NanoPi R1 06 | ❌ | ✅ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-06-20 |
| Nanopi R2S 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-rockchip64 | 2026-08-11 |
| Nanopi R2S 03 | ✅ | ⏭️ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-rockchip64 | 2026-06-21 |
| Nanopi R2S 04 | ✅ | ⏭️ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-rockchip64 | 2026-06-23 |
| NanoPi R4S 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-rockchip64 | 2026-07-04 |
| NanoPi R6S 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-rockchip64 | 2026-08-11 |
| NanoPi R76S 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| NanoPi R76S 02 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.1.115-vendor-rk35xx | 2026-06-20 |
| Odroid C1 01 | ❌ | ⏭️ | ⏭️ | ✅ | ➖ | ⏭️ | — | 2026-08-11 |
| Odroid C2 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-meson64 | 2026-08-11 |
| Odroid C4 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-meson64 | 2026-08-11 |
| Odroid M1 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-rockchip64 | 2026-08-12 |
| Odroid N2 02 | ✅ | ✅ | ⏭️ | ✅ | ✅ | ✅ | 6.18.34-current-meson64 | 2026-07-04 |
| Odroid N2 03 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-meson64 | 2026-08-11 |
| Odroid XU4 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.6.141-current-odroidxu4 | 2026-08-11 |
| Orange Pi 3 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Orange Pi 5 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-rockchip64 | 2026-08-11 |
| Orange Pi 5 Plus 01 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.43-current-rockchip64 | 2026-08-11 |
| Orange Pi One+ 01 | ❌ | ⏭️ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Orange Pi PC + 01 | ❌ | ⏭️ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-07-04 |
| Orange Pi PC2 01 | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | — | 2026-08-11 |
| Orange Pi Prime 01 | ✅ | ⏭️ | ⏭️ | ✅ | ➖ | ✅ | 6.18.38-current-sunxi64 | 2026-08-11 |
| Orange Pi R1 01 | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | — | 2026-08-11 |
| Orange Pi Win 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Orange Pi Zero 02 | ❌ | ✅ | ✅ | ✅ | ➖ | ⏭️ | 6.18.44-current-sunxi | 2026-08-11 |
| Orange Pi Zero Plus 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Orange Pi Zero2 01 | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | — | 2026-08-11 |
| OrangePi 3 LTS 01 | ✅ | ⏭️ | ⏭️ | ✅ | ✅ | ✅ | 7.0.14-edge-sunxi64 | 2026-08-11 |
| Pine H64 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Radxa Dragon Q6A 01 | ✅ | ⏭️ | ✅ | ✅ | ✅ | ✅ | 6.18.10-edge-qcs6490 | 2026-06-20 |
| Radxa ZERO 3 01 | ✅ | ⏭️ | ⏭️ | ✅ | ✅ | ✅ | 6.18.24-current-rockchip64 | 2026-08-11 |
| Raspberry Pi 01 | ❌ | ❌ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Raspberry Pi 02 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-bcm2711 | 2026-07-04 |
| ROCK 2F 01 | ❌ | ⏭️ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-06-23 |
| Rock 5B 01 | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | — | 2026-08-11 |
| Rock 5B 02 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Rock 5B 05 | ❌ | ✅ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-06-20 |
| Rock 5B 06 | ❌ | ✅ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-06-20 |
| Rock 5B 07 | ✅ | ⏭️ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-rockchip64 | 2026-06-23 |
| Rock 5B 08 | ✅ | ⏭️ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-rockchip64 | 2026-06-23 |
| Rock 5B Plus 01 | ❌ | ⏭️ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Rock 5T 01 | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | — | 2026-08-11 |
| Rock 5T 02 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.18.35-current-rockchip64 | 2026-06-20 |
| Rockpi 4B+ 01 | ❌ | ✅ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-10 |
| Rockpi E 01 | ✅ | ✅ | ⏭️ | ✅ | ✅ | ✅ | 6.18.33-current-rockchip64 | 2026-07-04 |
| SpacemiT K3 Pico-ITX 01 | ✅ | ⏭️ | ⏭️ | ✅ | ✅ | ✅ | 6.18.3-legacy-spacemit-k3 | 2026-08-11 |
| Tanix TX6 01 | ❌ | ❌ | ✅ | ❌ | ❌ | ⏭️ | 6.18.44-current-sunxi64 | 2026-08-11 |
| Tinker Board 01 | ❌ | ❌ | ❌ | ⏭️ | ⏭️ | ⏭️ | — | 2026-08-11 |
| Tinker Board 2 01 | ❌ | ⏭️ | ⏭️ | ✅ | ➖ | ⏭️ | — | 2026-07-04 |
| Udoo 01 | ❌ | ✅ | ❌ | ✅ | ➖ | ⏭️ | — | 2026-08-08 |
| UEFI arm64 01 | ✅ | ⏭️ | ⏭️ | ✅ | ✅ | ✅ | 7.1.2-edge-arm64 | 2026-08-08 |
| UEFI x86 01 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 6.18.32-current-x86 | 2026-07-04 |
| Z28 PRO 01 | ✅ | ✅ | ✅ | ✅ | ➖ | ✅ | 6.18.43-current-rockchip64 | 2026-08-08 |

<!-- FLEET-STOP -->
