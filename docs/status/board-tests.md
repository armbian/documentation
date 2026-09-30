---
title: Tested boards
seo_title: "Armbian tested boards: automated fleet test results"
description: "Automated per-board test results from the Armbian autotests fleet — upgrade, reboot, performance, DVFS and network checks across single-board computers."
---
# Tested boards

Every board in the Armbian test datacenter runs an automated pipeline — a nightly **upgrade**, a **reboot**, hardware **performance** and **DVFS** checks and a **network** throughput test — before being restored to the stable release. Boards are grouped **failures first**, each with its per-module results, timings and power shown inline; use the table of contents on the right to jump straight to a board. The set is the **current status**: the most recent test of every board.

The list is refreshed automatically by the Armbian autotests fleet: a scheduled job reads the fleet's rolling test results and opens a pull request to update this page — the same mechanism used for the [datacenter boards](/status/boards/) and [Wi-Fi performance](/status/wifi-performance/) pages.

Legend: ✅ pass · ❌ fail · ⏭️ skipped · ➖ not run.

<!-- FLEET-START -->

**66** boards — **32** passed, **34** failed. Most recent test of every board; failures first.

## ❌ Failed (34)

### ❌ Banana Pi M5 01

`bananapim5` · **inplace** · image `26.11.0-trunk.62` · 13 ✅ · 2 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 18.3 s | — |
| reboot | ✅ | 202.1 s | warm · up 182 s |
| kernel-switch | ❌ | 29.2 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 765.7 s | warm · 4/4 boots · up 179 s |
| hw-performance | ✅ | 38.4 s | AES 979 · mem 5300 · disk W 9 / R 15 MB/s · 57.8 °C · 2100 MHz |
| dvfs | ✅ | 21.2 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 59.7 s | end0 ↑940/↓941 (1GE) · wlx000f13960190 ↑29/↓26 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 42.9 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 766.5 s | warm · 4/4 boots · up 179 s |
| hw-performance | ✅ | 38.2 s | AES 980 · mem 5300 · disk W 9 / R 15 MB/s · 58 °C · 2100 MHz |
| dvfs | ✅ | 21.1 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 74.2 s | end0 ↑940/↓941 (1GE) · wlx000f13960190 ↑25/↓15 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ❌ | 26.9 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 195.4 s | warm · up 179 s |

### ❌ Khadas VIM1 01

`khadas-vim1` · **inplace** · image `26.8.3` · 14 ✅ · 2 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 319.2 s | nightly · 26.8.3 → 26.11.0-trunk.65 |
| reboot | ✅ | 36.8 s | warm · up 19 s |
| kernel-switch | ❌ | 55.6 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 94.9 s | warm · 4/4 boots · up 10 s |
| hw-performance | ✅ | 30.9 s | AES 660 · mem 3500 · disk W 106 / R 168 MB/s · 51 °C · 2208 MHz |
| dvfs | ✅ | 26.5 s | ondemand · 500–2208 MHz (peak 2208) |
| network-iperf | ✅ | 81.9 s | end0 ↑94/↓939 (10/100ME) · wlan0 ↑25/↓21 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.2 s | 26.11.0-trunk.65 · 5.15.137-legacy-meson-s4t7 |
| kernel-switch | ❌ | 40.2 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 128.2 s | warm · 4/4 boots · up 61 s |
| hw-performance | ✅ | 23.0 s | AES 658 · mem 3600 · disk W 42 / R 140 MB/s · 49 °C · 1512 MHz |
| dvfs | ✅ | 79.8 s | ondemand · 500–1512 MHz (peak 1512) |
| network-iperf | ✅ | 124.9 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑17/↓10 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.2 s | 26.11.0-trunk.65 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 66.4 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 56.9 s | warm · up 11 s |

### ❌ Khadas VIM1S 01

`khadas-vim1s` · **inplace** · image `26.11.0-trunk` · 3 ✅ · 1 ❌ · 4 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 281.1 s | nightly · 26.11.0-trunk → 26.11.0-trunk.58 |
| reboot | ✅ | 68.9 s | power-cycle · up 31 s |
| kernel-switch | ✅ | 153.1 s | branch=legacy · family=meson-s4t7 · installed=26.11.0-trunk.58 · boot_image=/boot/vmlinuz-5.15.137-legacy-meson-s4t7 · kernel_before=7.1.13-current-meson-s4t7 |
| reboot | ❌ | 1488.7 s | power-cycle · 0/4 boots |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |

**Power** — min 1.00 W · avg 1.94 W · peak 2.70 W · 1608 samples

```mermaid
xychart-beta
    title "Power — Khadas VIM1S 01"
    x-axis "sample" 1 --> 1608
    y-axis "W" 0.5 --> 3.0
    line [2.06, 2.12, 2.12, 2.25, 2.19, 2.11, 1.84, 2.16, 2.12, 2.13, 1.89, 1.90, 1.90, 1.90, 1.75, 1.86, 1.91, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.91, 1.91, 1.90, 1.90, 1.90, 1.91, 1.83, 1.90, 1.90, 1.90, 1.90, 1.79, 1.90, 1.91, 1.90]
```

### ❌ Khadas VIM3 01

`khadas-vim3` · **inplace** · image `26.11.0-trunk.62` · 9 ✅ · 1 ❌ · 6 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 249.1 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 32.2 s | warm · up 17 s |
| kernel-switch | ✅ | 25.1 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 115.3 s | warm · 4/4 boots · up 16 s |
| hw-performance | ✅ | 16.6 s | AES 852 · mem 3900 · disk W 71 / R 151 MB/s · 61.3 °C · 2016 MHz |
| dvfs | ✅ | 17.6 s | ondemand · 1000–1512 MHz (peak 1512) |
| network-iperf | ✅ | 56.2 s | end0 ↑940/↓941 (1GE) · wlan0 ↑44/↓42 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.65 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 73.2 s | branch=edge · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ❌ | 256.9 s | warm · 2/4 boots · up 17 s |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |

### ❌ NanoPi Neo 2 Black 01

`nanopineo2black` · **inplace** · image `26.11.0-trunk.62` · 13 ✅ · 2 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 15.5 s | — |
| reboot | ✅ | 52.5 s | power-cycle · up 21 s |
| kernel-switch | ❌ | 23.6 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 587.5 s | power-cycle · 2/4 boots · up 22 s |
| hw-performance | ✅ | 31.2 s | AES 620 · mem 3500 · disk W 18 / R 0 MB/s · 62.9 °C · 1368 MHz |
| dvfs | ✅ | 24.0 s | ondemand · 480–1368 MHz (peak 1368) |
| network-iperf | ✅ | 37.4 s | end0 ↑870/↓402 (1GE) Mbps |
| store-versions | ✅ | 6.3 s | 26.11.0-trunk.62 · 7.2.8-edge-sunxi64 |
| kernel-switch | ✅ | 44.1 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi64 · kernel_before=7.2.8-edge-sunxi64 |
| reboot | ✅ | 804.2 s | power-cycle · 1/4 boots · up 23 s |
| hw-performance | ✅ | 32.3 s | AES 638 · mem 3500 · disk W 18 / R 23 MB/s · 63.3 °C · 1368 MHz |
| dvfs | ✅ | 23.6 s | ondemand · 480–1368 MHz (peak 1368) |
| network-iperf | ✅ | 34.1 s | end0 ↑884/↓925 (1GE) Mbps |
| store-versions | ✅ | 5.9 s | 26.11.0-trunk.62 · 7.2.8-edge-sunxi64 |
| kernel-switch | ❌ | 23.8 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 56.4 s | power-cycle · up 23 s |

**Power** — min 0.90 W · avg 2.24 W · peak 5.30 W · 1413 samples

```mermaid
xychart-beta
    title "Power — NanoPi Neo 2 Black 01"
    x-axis "sample" 1 --> 1413
    y-axis "W" 0.5 --> 5.5
    line [2.46, 3.50, 3.09, 2.84, 1.43, 1.40, 1.40, 1.39, 3.28, 2.52, 1.40, 1.40, 1.40, 2.03, 2.93, 3.08, 3.10, 2.93, 3.36, 2.14, 1.45, 1.40, 1.40, 1.82, 3.00, 1.50, 1.50, 1.50, 1.50, 3.08, 2.76, 1.50, 1.49, 1.40, 1.55, 3.09, 3.28, 3.47, 3.31, 2.34]
```

### ❌ Odroid C4 01

`odroidc4` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 10.9 s | — |
| reboot | ✅ | 47.0 s | power-cycle · up 17 s |
| kernel-switch | ✅ | 29.3 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 130.8 s | power-cycle · 4/4 boots · up 18 s |
| hw-performance | ✅ | 22.0 s | AES 980 · mem 5200 · disk W 29 / R 73 MB/s · 42.4 °C · 2100 MHz |
| dvfs | ✅ | 18.8 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 56.8 s | end0 ↑938/↓939 (1GE) · wlx24050fdd332b ↑114/↓126 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.5 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ❌ | 17.0 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 132.0 s | power-cycle · 4/4 boots · up 17 s |
| hw-performance | ✅ | 23.4 s | AES 977 · mem 5200 · disk W 31 / R 76 MB/s · 43.1 °C · 2100 MHz |
| dvfs | ✅ | 20.0 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 78.3 s | end0 ↑609/↓936 (1GE) · wlx24050fdd332b ↑86/↓115 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 5.0 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 29.2 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 47.0 s | power-cycle · up 16 s |

**Power** — min 1.00 W · avg 3.41 W · peak 5.00 W · 527 samples

```mermaid
xychart-beta
    title "Power — Odroid C4 01"
    x-axis "sample" 1 --> 527
    y-axis "W" 0.5 --> 5.5
    line [3.17, 2.98, 2.15, 3.86, 3.75, 3.37, 3.34, 3.42, 3.46, 3.12, 3.73, 2.21, 3.45, 3.76, 3.85, 3.63, 3.48, 4.13, 4.38, 3.60, 3.46, 3.15, 3.37, 3.40, 3.23, 3.61, 2.45, 2.95, 3.68, 3.61, 3.62, 3.42, 3.58, 3.46, 4.00, 3.72, 3.64, 3.41, 2.82, 2.90]
```

### ❌ Odroid N2 01

`odroidn2` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 8.9 s | — |
| reboot | ✅ | 60.7 s | power-cycle · up 29 s |
| kernel-switch | ✅ | 23.4 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 161.1 s | power-cycle · 4/4 boots · up 28 s |
| hw-performance | ✅ | 18.5 s | AES 1085 · mem 4900 · disk W 27 / R 138 MB/s · 40.2 °C · 1992 MHz |
| dvfs | ✅ | 17.0 s | performance · 1000–1992 MHz (peak 1992) |
| network-iperf | ✅ | 27.5 s | end0 ↑940/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.8 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ❌ | 14.8 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 166.5 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 18.5 s | AES 1085 · mem 4900 · disk W 27 / R 136 MB/s · 40.8 °C · 1992 MHz |
| dvfs | ✅ | 17.1 s | performance · 1000–1992 MHz (peak 1992) |
| network-iperf | ✅ | 36.0 s | end0 ↑939/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 23.4 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 62.5 s | power-cycle · up 28 s |

**Power** — min 1.00 W · avg 4.63 W · peak 11.00 W · 521 samples

```mermaid
xychart-beta
    title "Power — Odroid N2 01"
    x-axis "sample" 1 --> 521
    y-axis "W" 0.5 --> 11.5
    line [4.06, 4.09, 2.06, 5.24, 5.46, 5.82, 3.58, 5.06, 2.98, 4.37, 5.39, 3.58, 4.88, 4.32, 5.25, 4.88, 6.06, 5.82, 4.50, 4.67, 4.95, 3.00, 5.98, 3.42, 5.72, 4.31, 4.63, 5.18, 3.65, 4.65, 5.45, 7.07, 5.72, 4.51, 4.67, 5.13, 4.52, 2.52, 2.77, 5.16]
```

### ❌ Odroid XU4 01

`odroidxu4` · **inplace** · image `26.11.0-trunk.62` · 0 ✅ · 2 ❌ · 14 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ❌ | 179.3 s | — |
| reboot | ❌ | 221.9 s | power-cycle |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |

### ❌ Orange Pi 5 01

`orangepi5` · **inplace** · image `26.8.3` · 0 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| reachable | ❌ | 0.0 s | ip=10.0.50.46 · reachable=False · port=22 |

### ❌ Orange Pi 5 Plus 01

`orangepi5-plus` · **inplace** · image `26.11.0-trunk.62` · 18 ✅ · 3 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 8.7 s | — |
| reboot | ✅ | 61.7 s | power-cycle · up 27 s |
| kernel-switch | ✅ | 17.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 159.7 s | power-cycle · 4/4 boots · up 26 s |
| hw-performance | ✅ | 17.7 s | AES 1251 · mem 15100 · disk W 53 / R 62 MB/s · 59.2 °C · 1800 MHz |
| dvfs | ✅ | 16.2 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ❌ | 176.0 s | enP3p49s0 ↑941/↓0 (1GE) · wlxe0e1a9380c53 ↑128/↓118 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 3.6 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ❌ | 12.4 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 164.9 s | power-cycle · 4/4 boots · up 28 s |
| hw-performance | ✅ | 17.3 s | AES 1263 · mem 15300 · disk W 54 / R 62 MB/s · 59.2 °C · 1800 MHz |
| dvfs | ✅ | 16.5 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ✅ | 55.3 s | enP3p49s0 ↑941/↓940 (1GE) · wlxe0e1a9380c53 ↑694/↓430 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 3.7 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ❌ | 13.0 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 165.0 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 17.3 s | AES 1261 · mem 13400 · disk W 54 / R 62 MB/s · 60.1 °C · 1800 MHz |
| dvfs | ✅ | 17.2 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ✅ | 56.8 s | enP3p49s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑500/↓359 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 19.7 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 55.8 s | power-cycle · up 28 s |

**Power** — min 0.60 W · avg 5.47 W · peak 11.50 W · 846 samples

```mermaid
xychart-beta
    title "Power — Orange Pi 5 Plus 01"
    x-axis "sample" 1 --> 846
    y-axis "W" 0.5 --> 12.0
    line [5.46, 2.57, 6.53, 4.96, 4.98, 4.77, 4.60, 5.37, 4.01, 6.00, 7.61, 6.21, 5.27, 5.00, 5.00, 4.98, 5.47, 6.10, 3.89, 4.85, 5.56, 4.43, 4.22, 5.48, 6.97, 6.15, 7.32, 6.79, 4.51, 5.36, 5.64, 3.89, 5.55, 4.85, 7.45, 6.77, 6.99, 6.49, 5.93, 4.90]
```

### ❌ Orange Pi Lite 2 01

`orangepilite2` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 14.0 s | — |
| reboot | ✅ | 43.7 s | warm · up 27 s |
| kernel-switch | ✅ | 38.6 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 145.1 s | warm · 4/4 boots · up 24 s |
| hw-performance | ✅ | 32.6 s | AES 772 · mem 4300 · disk W 22 / R 23 MB/s · 75.3 °C · 1800 MHz |
| dvfs | ✅ | 26.9 s | ondemand · 480–1704 MHz (peak 1704) |
| network-iperf | ✅ | 82.0 s | wlan0 ↑4/↓21 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.5 s | 26.11.0-trunk.62 · 6.18.54-current-sunxi64 |
| kernel-switch | ❌ | 21.0 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 149.0 s | warm · 4/4 boots · up 25 s |
| hw-performance | ✅ | 31.7 s | AES 760 · mem 4300 · disk W 14 / R 23 MB/s · 77.2 °C · 1800 MHz |
| dvfs | ✅ | 26.1 s | ondemand · 480–1704 MHz (peak 1800) |
| network-iperf | ✅ | 48.0 s | wlan0 ↑14/↓9 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 6.3 s | 26.11.0-trunk.62 · 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 38.6 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 41.0 s | warm · up 24 s |

### ❌ Orange Pi One+ 01

`orangepioneplus` · **inplace** · image `26.11.0-trunk.62` · 13 ✅ · 2 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 15.7 s | — |
| reboot | ✅ | 40.1 s | warm · up 24 s |
| kernel-switch | ❌ | 21.9 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 138.0 s | warm · 4/4 boots · up 23 s |
| hw-performance | ✅ | 29.4 s | AES 839 · mem 4600 · disk W 21 / R 1 MB/s · 63.9 °C · 1800 MHz |
| dvfs | ✅ | 23.1 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 93.0 s | end0 ↑914/↓940 (1GE) · wlx00e04c881724 ↑73/↓91 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.1 s | 26.11.0-trunk.62 · 7.2.8-edge-sunxi64 |
| kernel-switch | ✅ | 36.6 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi64 · kernel_before=7.2.8-edge-sunxi64 |
| reboot | ✅ | 132.4 s | warm · 4/4 boots · up 21 s |
| hw-performance | ✅ | 29.7 s | AES 839 · mem 4600 · disk W 21 / R 23 MB/s · 65.9 °C · 1800 MHz |
| dvfs | ✅ | 23.3 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 65.6 s | end0 ↑910/↓941 (1GE) · wlx00e04c881724 ↑148/↓113 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.8 s | 26.11.0-trunk.62 · 7.2.8-edge-sunxi64 |
| kernel-switch | ❌ | 21.8 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 37.1 s | warm · up 20 s |

### ❌ Orange Pi PC + 01

`orangepipcplus` · **inplace** · image `26.08.0-trunk` · 1 ✅ · 4 ❌ · 3 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 13.3 s | — |
| reboot | ❌ | 203.7 s | warm |
| hw-performance | ✅ | 98.0 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
| dvfs | ➖ | 9.1 s | no cpufreq |
| network-iperf | ⏭️ | 34.0 s | no iperf3 on board |
| restore-stable | ❌ | 30.3 s | stable |
| reboot | ❌ | 202.9 s | warm |
| store-versions | ❌ | 16.4 s | — |

### ❌ Orange Pi Prime 01

`orangepiprime` · **inplace** · image `26.11.0-trunk.62` · 0 ✅ · 1 ❌ · 15 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 23.7 s | — |
| reboot | ❌ | 204.3 s | warm |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |

### ❌ Orange Pi Zero2 01

`orangepizero2` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 44.7 s | — |
| reboot | ✅ | 41.7 s | warm · up 24 s |
| kernel-switch | ✅ | 67.7 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 149.8 s | warm · 4/4 boots · up 23 s |
| hw-performance | ✅ | 33.2 s | AES 699 · mem 3000 · disk W 21 / R 23 MB/s · 68.7 °C · 1512 MHz |
| dvfs | ✅ | 26.7 s | ondemand · 480–1512 MHz (peak 1512) |
| network-iperf | ✅ | 64.1 s | end0 ↑885/↓937 (1GE) · wlx7c023a625db1 ↑35/↓33 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.9 s | 26.11.0-trunk.62 · 6.18.54-current-sunxi64 |
| kernel-switch | ❌ | 51.6 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 149.5 s | warm · 4/4 boots · up 25 s |
| hw-performance | ✅ | 32.5 s | AES 705 · mem 3000 · disk W 21 / R 22 MB/s · 69.4 °C · 1512 MHz |
| dvfs | ✅ | 26.2 s | ondemand · 480–1512 MHz (peak 1512) |
| network-iperf | ✅ | 79.3 s | end0 ↑859/↓936 (1GE) · wlx7c023a625db1 ↑36/↓35 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.8 s | 26.11.0-trunk.62 · 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 67.8 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 41.6 s | warm · up 24 s |

### ❌ OrangePi 3 LTS 01

`orangepi3-lts` · **inplace** · image `26.11.0-trunk.62` · 0 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| reachable | ❌ | 0.0 s | ip=10.0.50.60 · reachable=False · port=22 |

**Power** — min 2.60 W · avg 2.60 W · peak 2.60 W · 41 samples

```mermaid
xychart-beta
    title "Power — OrangePi 3 LTS 01"
    x-axis "sample" 1 --> 41
    y-axis "W" 2.5 --> 3.0
    line [2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60, 2.60]
```

### ❌ Radxa Dragon Q6A 01

`radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 9.0 s | — |
| reboot | ✅ | 139.0 s | power-cycle · up 106 s |
| kernel-switch | ✅ | 17.1 s | branch=current · family=qcs6490 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.2-current-qcs6490 · kernel_before=6.18.2-current-qcs6490 |
| reboot | ✅ | 478.1 s | power-cycle · 4/4 boots · up 112 s |
| hw-performance | ✅ | 13.2 s | AES 1493 · mem 15400 · disk W 241 / R 1142 MB/s · 50.8 °C · 1958 MHz |
| dvfs | ✅ | 14.1 s | ondemand · 300–1958 MHz (peak 2707) |
| network-iperf | ✅ | 30.4 s | enp1s0 ↑941/↓940 (1GE) Mbps |
| store-versions | ✅ | 3.7 s | 26.11.0-trunk.62 · 6.18.2-current-qcs6490 |
| kernel-switch | ❌ | 10.5 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 476.8 s | power-cycle · 4/4 boots · up 112 s |
| hw-performance | ✅ | 13.8 s | AES 1500 · mem 15200 · disk W 228 / R 1095 MB/s · 50.8 °C · 1958 MHz |
| dvfs | ✅ | 13.6 s | ondemand · 300–1958 MHz (peak 2707) |
| network-iperf | ✅ | 27.5 s | enp1s0 ↑941/↓940 (1GE) Mbps |
| store-versions | ✅ | 3.6 s | 26.11.0-trunk.62 · 6.18.2-current-qcs6490 |
| kernel-switch | ✅ | 16.9 s | branch=current · family=qcs6490 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.2-current-qcs6490 · kernel_before=6.18.2-current-qcs6490 |
| reboot | ✅ | 139.7 s | power-cycle · up 105 s |

**Power** — min 1.10 W · avg 2.15 W · peak 7.60 W · 1125 samples

```mermaid
xychart-beta
    title "Power — Radxa Dragon Q6A 01"
    x-axis "sample" 1 --> 1125
    y-axis "W" 1.0 --> 8.0
    line [1.64, 2.35, 1.94, 1.81, 2.39, 2.84, 1.87, 1.94, 2.46, 1.71, 1.70, 2.35, 1.79, 1.85, 1.86, 2.87, 1.85, 1.95, 3.69, 2.22, 2.80, 2.03, 1.70, 1.99, 2.41, 1.85, 1.83, 2.49, 1.78, 1.76, 1.93, 2.31, 1.80, 1.80, 3.73, 2.55, 2.16, 2.26, 1.87, 1.98]
```

### ❌ Raspberry Pi 3B

`rpi4b` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 31.4 s | — |
| reboot | ✅ | 53.5 s | warm · up 33 s |
| kernel-switch | ✅ | 74.6 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 186.4 s | warm · 4/4 boots · up 30 s |
| hw-performance | ✅ | 43.7 s | AES 21 · mem 1400 · disk W 20 / R 22 MB/s · 58 °C · 1200 MHz |
| dvfs | ✅ | 39.6 s | ondemand · 600–1200 MHz (peak 1200) |
| network-iperf | ✅ | 85.2 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑28/↓37 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 8.9 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ❌ | 43.6 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 184.9 s | warm · 4/4 boots · up 32 s |
| hw-performance | ✅ | 43.1 s | AES 22 · mem 1400 · disk W 20 / R 22 MB/s · 58 °C · 1200 MHz |
| dvfs | ✅ | 39.3 s | ondemand · 600–1200 MHz (peak 1200) |
| network-iperf | ✅ | 88.0 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑21/↓36 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 9.3 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ✅ | 70.6 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 51.5 s | warm · up 32 s |

### ❌ Raspberry Pi 5B

`rpi4b` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 5.0 s | — |
| reboot | ✅ | 48.0 s | power-cycle · up 22 s |
| kernel-switch | ✅ | 13.3 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 127.5 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 14.8 s | AES 1368 · mem 12100 · disk W 53 / R 87 MB/s · 70 °C · 2400 MHz |
| dvfs | ✅ | 13.4 s | ondemand · 1500–2400 MHz (peak 2400) |
| network-iperf | ✅ | 51.4 s | end0 ↑936/↓941 (1GE) · wlan0 ↑42/↓34 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.2 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ❌ | 7.8 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 122.2 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 14.8 s | AES 1368 · mem 12100 · disk W 55 / R 83 MB/s · 72.2 °C · 2400 MHz |
| dvfs | ✅ | 13.6 s | ondemand · 1500–2400 MHz (peak 2400) |
| network-iperf | ✅ | 52.5 s | end0 ↑936/↓941 (1GE) · wlan0 ↑39/↓36 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.1 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ✅ | 13.3 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 46.9 s | power-cycle · up 19 s |

**Power** — min 2.40 W · avg 6.05 W · peak 10.30 W · 427 samples

```mermaid
xychart-beta
    title "Power — Raspberry Pi 5B"
    x-axis "sample" 1 --> 427
    y-axis "W" 2.0 --> 10.5
    line [5.98, 5.65, 5.55, 6.59, 6.87, 5.21, 7.54, 4.99, 7.34, 4.80, 5.42, 4.38, 3.98, 6.15, 6.55, 7.92, 7.46, 6.94, 6.84, 5.35, 6.35, 5.02, 5.99, 5.45, 5.97, 4.84, 7.15, 4.38, 5.14, 6.02, 6.84, 8.15, 7.03, 6.55, 6.01, 5.35, 7.01, 5.92, 5.62, 5.75]
```

### ❌ Raspberry Pi Zero 2W

`rpi4b` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 24.6 s | — |
| reboot | ✅ | 41.8 s | warm · up 22 s |
| kernel-switch | ✅ | 53.2 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 150.2 s | warm · 4/4 boots · up 22 s |
| hw-performance | ✅ | 33.5 s | AES 33 · mem 2200 · disk W 1 / R 23 MB/s · 58 °C · 1000 MHz |
| dvfs | ✅ | 27.0 s | ondemand · 600–1000 MHz (peak 1000) |
| network-iperf | ✅ | 44.3 s | wlan0 ↑35/↓35 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 6.2 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ❌ | 34.9 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 151.5 s | warm · 4/4 boots · up 25 s |
| hw-performance | ✅ | 33.8 s | AES 33 · mem 2200 · disk W 20 / R 22 MB/s · 59.1 °C · 1000 MHz |
| dvfs | ✅ | 26.7 s | ondemand · 600–1000 MHz (peak 1000) |
| network-iperf | ✅ | 43.6 s | wlan0 ↑35/↓35 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 5.8 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ✅ | 52.7 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 44.6 s | warm · up 24 s |

### ❌ ROCK 2F 01

`rock-2f` · **inplace** · image `26.8.1` · 0 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| reachable | ❌ | 0.0 s | ip=10.0.20.164 · reachable=False · port=22 |

### ❌ Rock 5B 01

`rock-5b` · **inplace** · image `26.11.0-trunk.62` · 19 ✅ · 2 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 8.2 s | — |
| reboot | ✅ | 45.2 s | power-cycle · up 19 s |
| kernel-switch | ✅ | 22.5 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 128.5 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 20.5 s | AES 1291 · mem 14000 · disk W 25 / R 86 MB/s · 55 °C · 1800 MHz |
| dvfs | ✅ | 17.7 s | ondemand · 1800–1800 MHz (peak 2352) |
| network-iperf | ✅ | 57.5 s | enP4p65s0 ↑941/↓939 (1GE) · wlP2p33s0 ↑107/↓93 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.0 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ❌ | 14.7 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 125.4 s | power-cycle · 4/4 boots · up 19 s |
| hw-performance | ✅ | 19.7 s | AES 1292 · mem 15500 · disk W 27 / R 83 MB/s · 57.3 °C · 1800 MHz |
| dvfs | ✅ | 17.3 s | ondemand · 1800–1800 MHz (peak 2352) |
| network-iperf | ✅ | 56.6 s | enP4p65s0 ↑941/↓939 (1GE) · wlP2p33s0 ↑706/↓420 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ❌ | 14.3 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 128.2 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 19.7 s | AES 1291 · mem 15500 · disk W 25 / R 86 MB/s · 58.2 °C · 1800 MHz |
| dvfs | ✅ | 16.4 s | ondemand · 1800–1800 MHz (peak 2352) |
| network-iperf | ✅ | 55.5 s | enP4p65s0 ↑941/↓939 (1GE) · wlP2p33s0 ↑390/↓385 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 22.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 48.5 s | power-cycle · up 22 s |

**Power** — min 0.70 W · avg 4.11 W · peak 9.10 W · 662 samples

```mermaid
xychart-beta
    title "Power — Rock 5B 01"
    x-axis "sample" 1 --> 662
    y-axis "W" 0.5 --> 9.5
    line [3.41, 3.55, 4.49, 3.69, 4.76, 3.78, 4.39, 4.05, 2.92, 3.72, 3.69, 5.81, 3.52, 4.24, 3.63, 3.31, 3.88, 4.12, 4.32, 3.91, 4.41, 4.08, 5.69, 3.54, 4.39, 4.19, 3.60, 3.99, 4.29, 4.25, 5.21, 4.76, 4.36, 5.76, 3.51, 3.89, 3.88, 4.06, 3.22, 4.30]
```

### ❌ Rock 5B 02

`rock-5b` · **inplace** · image `26.11.0-trunk.62` · 0 ✅ · 1 ❌ · 21 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 10.0 s | — |
| reboot | ❌ | 133.3 s | power-cycle · up 102 s |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |
| kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
| reboot | ⏭️ | 0.0 s | reboot |

**Power** — min 2.90 W · avg 3.32 W · peak 4.90 W · 109 samples

```mermaid
xychart-beta
    title "Power — Rock 5B 02"
    x-axis "sample" 1 --> 109
    y-axis "W" 2.5 --> 5.0
    line [3.50, 3.50, 3.80, 4.40, 3.80, 3.73, 3.57, 3.50, 4.00, 4.00, 4.00, 4.00, 3.67, 3.97, 4.90, 3.97, 3.33, 3.00, 2.90, 2.93, 3.00, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 2.90, 3.40]
```

### ❌ Rock 5B Plus 01

`rock-5b-plus` · **inplace** · image `26.11.0-trunk.62` · 19 ✅ · 2 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 9.7 s | — |
| reboot | ✅ | 50.0 s | power-cycle · up 23 s |
| kernel-switch | ✅ | 18.7 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 150.9 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 17.2 s | AES 1279 · mem 14000 · disk W 66 / R 81 MB/s · 56.4 °C · 1800 MHz |
| dvfs | ✅ | 16.7 s | ondemand · 1800–1800 MHz (peak 2352) |
| network-iperf | ✅ | 29.0 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.0 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ❌ | 11.9 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 153.1 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 17.5 s | AES 1278 · mem 15500 · disk W 69 / R 81 MB/s · 57.3 °C · 1800 MHz |
| dvfs | ✅ | 17.6 s | ondemand · 1800–1800 MHz (peak 2304) |
| network-iperf | ✅ | 31.2 s | enP4p65s0 ↑940/↓941 (1GE) Mbps |
| store-versions | ✅ | 5.1 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ❌ | 11.8 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 150.2 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 17.5 s | AES 1278 · mem 11400 · disk W 69 / R 81 MB/s · 58.2 °C · 1800 MHz |
| dvfs | ✅ | 16.6 s | ondemand · 1800–1800 MHz (peak 2304) |
| network-iperf | ✅ | 29.3 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 20.2 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 51.8 s | power-cycle · up 24 s |

**Power** — min 1.50 W · avg 3.91 W · peak 10.70 W · 646 samples

```mermaid
xychart-beta
    title "Power — Rock 5B Plus 01"
    x-axis "sample" 1 --> 646
    y-axis "W" 1.0 --> 11.0
    line [3.99, 3.18, 3.92, 3.90, 2.94, 3.56, 3.47, 3.14, 3.54, 3.26, 4.51, 5.21, 5.62, 3.87, 4.23, 2.93, 4.22, 3.14, 3.33, 3.11, 3.64, 4.22, 4.64, 5.71, 3.78, 3.85, 3.35, 3.20, 3.51, 4.76, 4.09, 3.95, 3.34, 4.35, 5.74, 4.51, 3.70, 4.11, 3.02, 4.08]
```

### ❌ Rock 5T 01

`rock-5t` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 1 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 9.8 s | — |
| reboot | ✅ | 56.7 s | power-cycle · up 23 s |
| kernel-switch | ✅ | 20.8 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 142.5 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 18.3 s | AES 1251 · mem 10000 · disk W 52 / R 78 MB/s · 58.2 °C · 1800 MHz |
| dvfs | ✅ | 16.2 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 58.3 s | enP4p65s0 ↑941/↓941 (1GE) · wlP2p33s0 ↑507/↓252 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ❌ | 14.1 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 142.8 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 17.9 s | AES 1251 · mem 10000 · disk W 53 / R 80 MB/s · 59.2 °C · 1800 MHz |
| dvfs | ✅ | 16.1 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 70.3 s | enP4p65s0 ↑941/↓942 (1GE) · wlP2p33s0 ↑445/↓236 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 20.3 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 57.7 s | power-cycle · up 23 s |

**Power** — min 1.80 W · avg 6.87 W · peak 14.30 W · 517 samples

```mermaid
xychart-beta
    title "Power — Rock 5T 01"
    x-axis "sample" 1 --> 517
    y-axis "W" 1.5 --> 14.5
    line [7.20, 7.08, 3.42, 8.63, 7.95, 7.24, 5.11, 6.01, 6.72, 5.36, 7.72, 4.95, 4.88, 7.53, 7.59, 9.25, 7.28, 7.47, 8.90, 7.69, 7.54, 4.25, 7.66, 4.82, 7.19, 5.09, 6.56, 3.08, 6.77, 8.06, 11.35, 7.73, 7.41, 8.46, 7.62, 7.18, 7.77, 7.51, 3.51, 7.47]
```

### ❌ Rockpi E 01

`rockpi-e` · **inplace** · image `26.11.0-trunk.62` · 15 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 332.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 52.4 s | power-cycle · up 25 s |
| kernel-switch | ✅ | 64.8 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 156.3 s | power-cycle · 4/4 boots · up 26 s |
| hw-performance | ✅ | 35.3 s | AES 600 · mem 3300 · disk W 15 / R 23 MB/s · 59.1 °C · 1296 MHz |
| dvfs | ✅ | 25.2 s | ondemand · 408–1296 MHz (peak 1296) |
| network-iperf | ✅ | 91.3 s | end0 ↑940/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑181/↓207 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.5 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ❌ | 25.9 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 157.8 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 31.7 s | AES 603 · mem 3300 · disk W 21 / R 23 MB/s · 59.5 °C · 1296 MHz |
| dvfs | ✅ | 25.5 s | ondemand · 408–1296 MHz (peak 1296) |
| network-iperf | ✅ | 97.6 s | end0 ↑940/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑166/↓207 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.7 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 41.5 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 56.3 s | power-cycle · up 25 s |

### ❌ Rockpi S 01

`rockpi-s` · **inplace** · image `26.11.0-trunk.62` · 13 ✅ · 3 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 418.2 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 66.6 s | power-cycle · up 31 s |
| kernel-switch | ✅ | 74.6 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 193.6 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 41.2 s | AES 218 · mem 1300 · disk W 21 / R 22 MB/s · 52.9 °C · 1008 MHz |
| dvfs | ✅ | 35.5 s | ondemand · 408–1008 MHz (peak 1008) |
| network-iperf | ❌ | 80.2 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑0/↓1 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 7.7 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ❌ | 43.9 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 196.2 s | power-cycle · 4/4 boots · up 33 s |
| hw-performance | ✅ | 41.7 s | AES 219 · mem 1300 · disk W 21 / R 22 MB/s · 52.9 °C · 1008 MHz |
| dvfs | ✅ | 35.7 s | ondemand · 408–1008 MHz (peak 1008) |
| network-iperf | ❌ | 81.7 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑0/↓1 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 7.8 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 70.7 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 66.3 s | power-cycle · up 31 s |

**Power** — min 1.00 W · avg 1.48 W · peak 2.20 W · 1167 samples

```mermaid
xychart-beta
    title "Power — Rockpi S 01"
    x-axis "sample" 1 --> 1167
    y-axis "W" 0.5 --> 2.5
    line [1.42, 1.44, 1.59, 1.48, 1.44, 1.41, 1.40, 1.70, 1.68, 1.41, 1.39, 1.38, 1.55, 1.67, 1.43, 1.30, 1.64, 1.66, 1.57, 1.42, 1.47, 1.43, 1.34, 1.31, 1.38, 1.41, 1.26, 1.71, 1.71, 1.57, 1.33, 1.54, 1.43, 1.48, 1.35, 1.52, 1.53, 1.47, 1.37, 1.64]
```

### ❌ RockPro 64 01

`rockpro64` · **inplace** · image `26.11.0-trunk.62` · 15 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 314.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 63.5 s | power-cycle · up 28 s |
| kernel-switch | ✅ | 29.4 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 847.6 s | power-cycle · 1/4 boots · up 31 s |
| hw-performance | ✅ | 20.8 s | AES 1020 · mem 6600 · disk W 64 / R 115 MB/s · 48.1 °C · 1416 MHz |
| dvfs | ✅ | 21.6 s | ondemand · 408–1416 MHz (peak 1800) |
| network-iperf | ✅ | 59.8 s | end0 ↑940/↓941 (1GE) · wlan0 ↑115/↓112 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.9 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ❌ | 18.4 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 848.7 s | power-cycle · 1/4 boots · up 29 s |
| hw-performance | ✅ | 21.0 s | AES 1020 · mem 6500 · disk W 65 / R 116 MB/s · 48.8 °C · 1416 MHz |
| dvfs | ✅ | 21.4 s | ondemand · 408–1416 MHz (peak 1800) |
| network-iperf | ✅ | 59.9 s | end0 ↑939/↓941 (1GE) · wlan0 ↑108/↓105 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.2 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 29.2 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 65.7 s | power-cycle · up 30 s |

**Power** — min 2.90 W · avg 4.81 W · peak 10.30 W · 1899 samples

```mermaid
xychart-beta
    title "Power — RockPro 64 01"
    x-axis "sample" 1 --> 1899
    y-axis "W" 2.5 --> 10.5
    line [4.06, 4.29, 5.16, 4.29, 5.36, 4.71, 4.76, 4.79, 4.80, 4.85, 4.71, 5.02, 4.90, 4.90, 4.59, 4.95, 4.90, 4.93, 4.95, 4.24, 5.28, 4.98, 4.48, 5.00, 5.00, 5.00, 4.52, 4.91, 4.91, 4.93, 4.98, 4.45, 4.91, 4.97, 4.98, 4.62, 4.61, 5.46, 5.21, 4.09]
```

### ❌ SpacemiT MusePi Pro 01

`musepipro` · **inplace** · image `26.11.0-trunk.62` · 1 ✅ · 1 ❌ · 4 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 179.5 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ❌ | 218.1 s | power-cycle |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |

**Power** — min 0.70 W · avg 3.75 W · peak 9.10 W · 312 samples

```mermaid
xychart-beta
    title "Power — SpacemiT MusePi Pro 01"
    x-axis "sample" 1 --> 312
    y-axis "W" 0.5 --> 9.5
    line [4.11, 4.95, 4.74, 4.61, 4.71, 4.79, 4.90, 4.50, 4.50, 4.62, 4.76, 4.78, 4.95, 6.85, 4.62, 4.80, 4.73, 4.62, 4.73, 4.52, 4.63, 1.38, 2.58, 2.77, 2.70, 2.64, 2.75, 2.70, 2.70, 2.70, 2.70, 2.66, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70]
```

### ❌ Tinker Board 01

`tinkerboard` · **inplace** · image `26.11.0-trunk.62` · 15 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 165.2 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 63.8 s | power-cycle · up 29 s |
| kernel-switch | ✅ | 29.7 s | branch=current · family=rockchip · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip · kernel_before=6.18.54-current-rockchip |
| reboot | ✅ | 164.8 s | power-cycle · 4/4 boots · up 31 s |
| hw-performance | ✅ | 28.2 s | AES 67 · mem 3300 · disk W 12 / R 63 MB/s · 58.2 °C · 1800 MHz |
| dvfs | ✅ | 19.7 s | ondemand · 600–1800 MHz (peak 1800) |
| network-iperf | ✅ | 66.8 s | end0 ↑940/↓941 (1GE) · wlan0 ↑17/↓21 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.5 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip |
| kernel-switch | ❌ | 17.0 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 174.3 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 28.2 s | AES 67 · mem 3300 · disk W 14 / R 63 MB/s · 58.6 °C · 1800 MHz |
| dvfs | ✅ | 20.4 s | ondemand · 600–1800 MHz (peak 1800) |
| network-iperf | ✅ | 61.9 s | end0 ↑940/↓941 (1GE) · wlan0 ↑30/↓29 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.5 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip |
| kernel-switch | ✅ | 30.3 s | branch=current · family=rockchip · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip · kernel_before=6.18.54-current-rockchip |
| reboot | ✅ | 57.8 s | power-cycle · up 29 s |

**Power** — min 1.30 W · avg 3.81 W · peak 8.50 W · 737 samples

```mermaid
xychart-beta
    title "Power — Tinker Board 01"
    x-axis "sample" 1 --> 737
    y-axis "W" 1.0 --> 9.0
    line [3.87, 3.78, 4.38, 4.89, 3.95, 3.49, 3.98, 3.94, 3.12, 3.31, 3.99, 3.26, 3.12, 3.28, 3.18, 3.37, 3.07, 3.16, 4.23, 5.37, 3.59, 3.96, 4.14, 4.13, 3.47, 4.29, 3.11, 4.19, 3.66, 3.55, 2.86, 3.87, 4.09, 5.39, 4.14, 4.22, 4.35, 3.93, 3.24, 3.42]
```

### ❌ Udoo 01

`udoo` · **inplace** · image `26.11.0-trunk.62` · 15 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 449.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 72.4 s | power-cycle · up 35 s |
| kernel-switch | ✅ | 77.9 s | branch=current · family=imx6 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-imx6 · kernel_before=6.18.54-current-imx6 |
| reboot | ✅ | 209.1 s | power-cycle · 4/4 boots · up 34 s |
| hw-performance | ✅ | 51.0 s | AES 26 · mem 722 · disk W 13 / R 20 MB/s · 48.6 °C · 996 MHz |
| dvfs | ✅ | 43.4 s | ondemand · 396–996 MHz (peak 996) |
| network-iperf | ✅ | 85.6 s | end0 ↑399/↓234 (1GE) · wlx7cdd903aa418 ↑32/↓32 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 10.1 s | 26.11.0-trunk.62 · 6.18.54-current-imx6 |
| kernel-switch | ❌ | 51.1 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 206.3 s | power-cycle · 4/4 boots · up 34 s |
| hw-performance | ✅ | 51.2 s | AES 26 · mem 665 · disk W 13 / R 20 MB/s · 49.8 °C · 996 MHz |
| dvfs | ✅ | 43.7 s | ondemand · 396–996 MHz (peak 996) |
| network-iperf | ✅ | 82.1 s | end0 ↑399/↓242 (1GE) · wlx7cdd903aa418 ↑30/↓29 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 9.4 s | 26.11.0-trunk.62 · 6.18.54-current-imx6 |
| kernel-switch | ✅ | 77.7 s | branch=current · family=imx6 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-imx6 · kernel_before=6.18.54-current-imx6 |
| reboot | ✅ | 71.8 s | power-cycle · up 34 s |

**Power** — min 1.30 W · avg 5.94 W · peak 8.30 W · 1278 samples

```mermaid
xychart-beta
    title "Power — Udoo 01"
    x-axis "sample" 1 --> 1278
    y-axis "W" 1.0 --> 8.5
    line [6.02, 5.63, 5.29, 5.09, 5.08, 5.13, 6.48, 6.18, 5.88, 5.96, 6.25, 5.94, 6.26, 5.93, 6.08, 5.38, 6.10, 6.13, 6.17, 5.45, 5.99, 6.38, 5.88, 6.14, 6.18, 6.04, 5.50, 6.84, 6.51, 6.13, 5.44, 6.25, 5.93, 6.61, 6.15, 5.98, 6.39, 6.14, 5.31, 5.56]
```

### ❌ UEFI arm64 01

`uefi-arm64` · **inplace** · image `26.11.0-trunk.62` · 15 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 133.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 54.1 s | warm · up 33 s |
| kernel-switch | ✅ | 17.5 s | branch=current · family=arm64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-arm64 · kernel_before=6.18.54-current-arm64 |
| reboot | ✅ | 179.7 s | warm · 4/4 boots · up 32 s |
| hw-performance | ✅ | 15.8 s | AES 1402 · mem 12000 · disk W 1545 / R 2268 MB/s · 44 °C · 2600 MHz |
| dvfs | ✅ | 15.1 s | ondemand · 800–2600 MHz (peak 2600) |
| network-iperf | ✅ | 80.3 s | enp1s0 ↑7899/↓2722 (10GE) · enp49s0 ↑7670/↓9369 (10GE) · wlp97s0 ↑97/↓67 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.3 s | 26.11.0-trunk.65 · 6.18.54-current-arm64 |
| kernel-switch | ❌ | 11.5 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 183.2 s | warm · 4/4 boots · up 32 s |
| hw-performance | ✅ | 15.4 s | AES 1402 · mem 12000 · disk W 1585 / R 2268 MB/s · 44 °C · 2600 MHz |
| dvfs | ✅ | 15.0 s | ondemand · 800–2600 MHz (peak 2600) |
| network-iperf | ✅ | 79.4 s | enp1s0 ↑7916/↓2689 (10GE) · enp49s0 ↑8062/↓9367 (10GE) · wlp97s0 ↑104/↓96 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.3 s | 26.11.0-trunk.65 · 6.18.54-current-arm64 |
| kernel-switch | ✅ | 16.6 s | branch=current · family=arm64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-arm64 · kernel_before=6.18.54-current-arm64 |
| reboot | ✅ | 55.1 s | warm · up 34 s |

### ❌ UEFI x86 01

`uefi-x86` · **inplace** · image `26.11.0-trunk.62` · 13 ✅ · 1 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 231.6 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 92.4 s | power-cycle · up 61 s |
| kernel-switch | ✅ | 35.3 s | branch=current · family=x86 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-x86 · kernel_before=6.18.54-current-x86 |
| reboot | ✅ | 240.8 s | power-cycle · 4/4 boots · up 57 s |
| hw-performance | ✅ | 25.3 s | AES 235 · mem 5300 · disk W 25 / R 106 MB/s · 62 °C · 1920 MHz |
| dvfs | ➖ | 23.7 s | schedutil · 480–1920 MHz (peak 1686) · max_khz is single-core turbo, not an all-core target |
| network-iperf | ✅ | 72.0 s | enp1s0 ↑902/↓941 (1GE) · wlan0 ↑21/↓22 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 6.0 s | 26.11.0-trunk.62 · 6.18.54-current-x86 |
| kernel-switch | ❌ | 23.1 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 236.8 s | power-cycle · 4/4 boots · up 56 s |
| hw-performance | ✅ | 24.9 s | AES 237 · mem 5100 · disk W 26 / R 113 MB/s · 63 °C · 1920 MHz |
| dvfs | ➖ | 23.4 s | schedutil · 480–1920 MHz (peak 1729) · max_khz is single-core turbo, not an all-core target |
| network-iperf | ✅ | 62.5 s | enp1s0 ↑921/↓941 (1GE) · wlan0 ↑23/↓21 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.4 s | 26.11.0-trunk.62 · 6.18.54-current-x86 |
| kernel-switch | ✅ | 35.2 s | branch=current · family=x86 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-x86 · kernel_before=6.18.54-current-x86 |
| reboot | ✅ | 88.7 s | power-cycle · up 56 s |

**Power** — min 1.80 W · avg 4.09 W · peak 8.70 W · 979 samples

```mermaid
xychart-beta
    title "Power — UEFI x86 01"
    x-axis "sample" 1 --> 979
    y-axis "W" 1.5 --> 9.0
    line [3.40, 3.77, 3.60, 3.87, 4.16, 3.94, 4.38, 3.46, 3.73, 4.20, 5.06, 3.50, 3.80, 4.60, 4.60, 4.54, 5.61, 3.83, 4.64, 4.55, 3.46, 3.38, 3.53, 3.14, 3.63, 4.32, 4.17, 5.32, 4.35, 4.88, 4.20, 4.89, 3.59, 3.78, 3.94, 3.53, 3.63, 3.54, 3.87, 5.12]
```

### ❌ ZeroPi 01

`zeropi` · **inplace** · image `26.11.0-trunk.58` · 15 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 202.2 s | nightly · 26.11.0-trunk.58 → 26.11.0-trunk.58 |
| reboot | ✅ | 59.6 s | power-cycle · up 25 s |
| kernel-switch | ✅ | 62.5 s | branch=current · family=sunxi · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 167.5 s | power-cycle · 4/4 boots · up 27 s |
| hw-performance | ✅ | 40.4 s | AES 25 · mem 1500 · disk W 16 / R 23 MB/s · 46.6 °C · 1296 MHz |
| dvfs | ✅ | 34.1 s | ondemand · 480–1296 MHz (peak 1296) |
| network-iperf | ✅ | 38.5 s | end0 ↑645/↓935 (1GE) Mbps |
| store-versions | ✅ | 7.4 s | 26.11.0-trunk.58 · 6.18.54-current-sunxi |
| kernel-switch | ❌ | 38.3 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 165.8 s | power-cycle · 4/4 boots · up 27 s |
| hw-performance | ✅ | 39.4 s | AES 25 · mem 1500 · disk W 21 / R 23 MB/s · 47.3 °C · 1296 MHz |
| dvfs | ✅ | 34.1 s | ondemand · 480–1296 MHz (peak 1296) |
| network-iperf | ✅ | 46.4 s | end0 ↑630/↓886 (1GE) Mbps |
| store-versions | ✅ | 7.3 s | 26.11.0-trunk.58 · 6.18.54-current-sunxi |
| kernel-switch | ✅ | 62.3 s | branch=current · family=sunxi · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 60.9 s | power-cycle · up 24 s |

**Power** — min 1.10 W · avg 2.21 W · peak 3.10 W · 848 samples

```mermaid
xychart-beta
    title "Power — ZeroPi 01"
    x-axis "sample" 1 --> 848
    y-axis "W" 1.0 --> 3.5
    line [1.94, 2.01, 2.27, 2.10, 2.10, 2.08, 2.17, 1.99, 1.76, 2.40, 2.27, 2.10, 2.03, 2.60, 2.42, 2.31, 2.34, 2.22, 2.38, 2.07, 2.57, 1.97, 2.45, 2.24, 2.02, 2.53, 2.31, 2.49, 2.35, 2.00, 2.55, 2.03, 2.29, 2.10, 2.30, 2.36, 2.22, 2.12, 1.70, 2.35]
```

## ✅ Passed (32)

### ✅ Arduino UNO Q 01

`arduino-uno-q` · **inplace** · image `26.11.0-trunk.62` · 8 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 270.6 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 58.6 s | warm · up 40 s |
| kernel-switch | ✅ | 58.2 s | branch=edge · family=qrb2210 · installed=26.11.0-trunk.65 · boot_image=? · kernel_before=7.2.3-edge-qrb2210 |
| reboot | ✅ | 201.3 s | warm · 4/4 boots · up 35 s |
| hw-performance | ✅ | 24.5 s | AES 934 · mem 5100 · disk W 173 / R 225 MB/s · 40 °C · 2016 MHz |
| dvfs | ✅ | 32.3 s | schedutil · 300–2016 MHz (peak 2016) |
| network-iperf | ✅ | 49.2 s | wlan0 ↑12/↓19 (Wi-Fi 5) · usb0 ↑?/↓? Mbps |
| store-versions | ✅ | 7.2 s | 26.11.0-trunk.65 · 7.2.3-edge-qrb2210 |

### ✅ Banana Pi CM4IO 01

`bananapicm4io` · **inplace** · image `26.8.3` · 14 ✅ · 2 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 291.4 s | nightly · 26.8.3 → 26.8.3 |
| reboot | ✅ | 48.3 s | power-cycle · up 22 s |
| kernel-switch | ✅ | 43.0 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 137.4 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 18.1 s | AES 852 · mem 3900 · disk W 32 / R 152 MB/s · 53.1 °C · 2016 MHz |
| dvfs | ✅ | 18.0 s | ondemand · 1000–1512 MHz (peak 1512) |
| network-iperf | ❌ | 273.2 s | eth0 ↑0/↓0 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.6 s | 26.8.3 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 202.6 s | branch=edge · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 137.9 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 18.0 s | AES 852 · mem 3900 · disk W 36 / R 149 MB/s · 53.1 °C · 2016 MHz |
| dvfs | ✅ | 18.3 s | ondemand · 1000–1512 MHz (peak 1512) |
| network-iperf | ❌ | 297.8 s | eth0 ↑941/↓941 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.8 s | 26.8.3 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 200.6 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 52.9 s | power-cycle · up 23 s |

### ✅ Banana Pi M2 Ultra 01

`bananapim2ultra` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 392.1 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 43.9 s | warm · up 25 s |
| kernel-switch | ✅ | 68.6 s | branch=current · family=sunxi · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 161.0 s | warm · 4/4 boots · up 26 s |
| hw-performance | ✅ | 39.6 s | AES 23 · mem 2100 · disk W 9 / R 42 MB/s · 54.4 °C · 1200 MHz |
| dvfs | ✅ | 33.9 s | ondemand · 720–1200 MHz (peak 1200) |
| network-iperf | ✅ | 72.3 s | end0 ↑824/↓936 (1GE) · wlan0 ↑30/↓35 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 7.4 s | 26.11.0-trunk.65 · 6.18.54-current-sunxi |
| kernel-switch | ✅ | 192.4 s | branch=edge · family=sunxi · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 168.2 s | warm · 4/4 boots · up 31 s |
| hw-performance | ✅ | 42.4 s | AES 23 · mem 2100 · disk W 7 / R 42 MB/s · 52.8 °C · 1200 MHz |
| dvfs | ✅ | 37.1 s | ondemand · 720–1200 MHz (peak 1200) |
| network-iperf | ✅ | 87.7 s | end0 ↑817/↓941 (1GE) · wlan0 ↑33/↓17 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 8.3 s | 26.11.0-trunk.65 · 7.2.8-edge-sunxi |
| kernel-switch | ✅ | 194.1 s | branch=current · family=sunxi · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=7.2.8-edge-sunxi |
| reboot | ✅ | 45.1 s | warm · up 26 s |

### ✅ Banana Pi M2Pro 01

`bananapim2pro` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 167.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 139.0 s | power-cycle · up 104 s |
| kernel-switch | ✅ | 34.5 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 465.0 s | power-cycle · 4/4 boots · up 104 s |
| hw-performance | ✅ | 19.4 s | AES 977 · mem 5300 · disk W 43 / R 157 MB/s · 48.4 °C · 2100 MHz |
| dvfs | ✅ | 19.4 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 32.3 s | end0 ↑940/↓941 (1GE) Mbps |
| store-versions | ✅ | 5.0 s | 26.11.0-trunk.65 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 101.2 s | branch=edge · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 466.7 s | power-cycle · 4/4 boots · up 104 s |
| hw-performance | ✅ | 20.2 s | AES 978 · mem 5300 · disk W 42 / R 150 MB/s · 48 °C · 2100 MHz |
| dvfs | ✅ | 20.8 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 30.2 s | end0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 5.1 s | 26.11.0-trunk.65 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 99.7 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 138.8 s | power-cycle · up 104 s |

**Power** — min 1.40 W · avg 2.89 W · peak 4.70 W · 1412 samples

```mermaid
xychart-beta
    title "Power — Banana Pi M2Pro 01"
    x-axis "sample" 1 --> 1412
    y-axis "W" 1.0 --> 5.0
    line [3.84, 3.86, 3.93, 3.91, 2.99, 2.65, 2.53, 3.19, 2.90, 2.50, 2.64, 2.82, 2.47, 2.91, 2.46, 2.43, 2.84, 2.47, 2.81, 3.12, 3.27, 3.31, 2.93, 2.77, 2.45, 2.84, 2.46, 2.57, 2.90, 2.45, 2.66, 2.61, 2.50, 3.17, 3.12, 3.36, 3.34, 2.71, 2.59, 2.47]
```

### ✅ Banana Pi M7 01

`bananapim7` · **inplace** · image `26.11.0-trunk.62` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 74.6 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 42.0 s | power-cycle · up 16 s |
| kernel-switch | ✅ | 19.2 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 102.4 s | power-cycle · 4/4 boots · up 15 s |
| hw-performance | ✅ | 13.6 s | AES 1260 · mem 15200 · disk W 960 / R 1293 MB/s · 56.4 °C · 1800 MHz |
| dvfs | ✅ | 17.0 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ✅ | 28.4 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.65 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 50.9 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 662.6 s | power-cycle · 3/4 boots · up 97 s |
| hw-performance | ✅ | 13.4 s | AES 1257 · mem 10200 · disk W 1010 / R 1568 MB/s · 59.2 °C · 1800 MHz |
| dvfs | ✅ | 14.2 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 28.4 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 40.6 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 442.7 s | power-cycle · 4/4 boots · up 97 s |
| hw-performance | ✅ | 14.0 s | AES 1257 · mem 8100 · disk W 817 / R 1590 MB/s · 59.2 °C · 1800 MHz |
| dvfs | ✅ | 14.0 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 29.9 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.65 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 38.6 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 49.5 s | power-cycle · up 16 s |

**Power** — min 1.00 W · avg 5.79 W · peak 11.40 W · 1340 samples

```mermaid
xychart-beta
    title "Power — Banana Pi M7 01"
    x-axis "sample" 1 --> 1340
    y-axis "W" 0.5 --> 11.5
    line [5.52, 6.30, 5.45, 5.93, 5.16, 5.54, 6.16, 6.25, 5.97, 5.40, 5.40, 5.68, 5.50, 5.50, 5.50, 5.50, 6.12, 5.40, 5.38, 5.77, 5.67, 6.43, 5.40, 5.40, 7.08, 6.29, 6.58, 5.45, 5.40, 6.27, 5.40, 5.56, 5.53, 5.40, 5.80, 5.62, 5.60, 6.68, 7.10, 5.45]
```

### ✅ Banana Pi R3 Mini 01

`bananapir3mini` · **inplace** · image `26.11.0-trunk` · 4 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 18.5 s | — |
| reboot | ✅ | 65.6 s | power-cycle · up 34 s |
| hw-performance | ✅ | 25.8 s | AES 933 · mem 3200 · disk W 76 / R 91 MB/s · 66.3 °C · None MHz |
| dvfs | ➖ | 2.2 s | no cpufreq |
| network-iperf | ✅ | 108.7 s | eth0 ↑939/↓939 (1GE) · eth1 ↑938/↓916 (1GE) · wlan0 ↑10/↓13 (Wi-Fi 6) · wlan1 ↑359/↓261 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk · 6.18.52-current-filogic-mt7986 |

**Power** — min 3.00 W · avg 7.59 W · peak 13.10 W · 192 samples

```mermaid
xychart-beta
    title "Power — Banana Pi R3 Mini 01"
    x-axis "sample" 1 --> 192
    y-axis "W" 2.5 --> 13.5
    line [5.90, 6.00, 5.90, 6.30, 6.32, 6.30, 6.06, 5.96, 5.82, 3.84, 4.00, 4.56, 5.88, 6.06, 7.64, 8.20, 8.10, 8.60, 8.60, 8.70, 8.60, 8.68, 8.54, 8.42, 8.46, 8.50, 8.26, 8.06, 8.26, 8.00, 7.78, 8.20, 8.88, 8.40, 8.30, 7.90, 13.10, 10.70, 9.20, 7.90]
```

### ✅ BananaPi BPI-F3 01

`musepipro` · **inplace** · image `26.11.0-trunk.62` · 6 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 201.6 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 54.0 s | power-cycle · up 18 s |
| hw-performance | ✅ | 25.5 s | AES 27 · mem 3000 · disk W 71 / R 82 MB/s · 48 °C · 1600 MHz |
| dvfs | ✅ | 24.0 s | performance · 614–1600 MHz (peak 1600) |
| network-iperf | ✅ | 90.4 s | eth0 ↑941/↓942 (1GE) · wlan0 ↑305/↓296 (Wi-Fi 6) · wlan1 ↑271/↓251 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 6.8 s | 26.11.0-trunk.65 · 6.18.54-current-spacemit |

**Power** — min 3.20 W · avg 5.24 W · peak 8.40 W · 320 samples

```mermaid
xychart-beta
    title "Power — BananaPi BPI-F3 01"
    x-axis "sample" 1 --> 320
    y-axis "W" 3.0 --> 8.5
    line [4.76, 5.33, 5.16, 5.16, 5.12, 5.10, 5.00, 5.00, 5.15, 5.05, 5.15, 5.05, 5.15, 5.08, 6.29, 5.51, 5.05, 5.29, 5.05, 5.05, 4.99, 4.76, 4.48, 3.30, 4.30, 5.35, 5.20, 5.20, 6.92, 6.04, 5.08, 5.01, 5.30, 5.51, 6.08, 6.06, 5.32, 6.15, 5.67, 5.45]
```

### ✅ Clearfog Pro 01

`clearfogpro` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 192.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 42.1 s | warm · up 22 s |
| kernel-switch | ✅ | 42.4 s | branch=current · family=mvebu · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu · kernel_before=6.18.54-current-mvebu |
| reboot | ✅ | 143.8 s | warm · 4/4 boots · up 22 s |
| hw-performance | ✅ | 41.6 s | AES 43 · mem 3800 · disk W 20 / R 23 MB/s · 65.1 °C · None MHz |
| dvfs | ➖ | 2.9 s | no cpufreq |
| network-iperf | ✅ | 35.7 s | lan2 ↑936/↓936 Mbps |
| store-versions | ✅ | 6.2 s | 26.11.0-trunk.65 · 6.18.54-current-mvebu |
| kernel-switch | ✅ | 106.7 s | branch=edge · family=mvebu · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-mvebu · kernel_before=6.18.54-current-mvebu |
| reboot | ✅ | 140.7 s | warm · 4/4 boots · up 21 s |
| hw-performance | ✅ | 41.7 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 66.1 °C · None MHz |
| dvfs | ➖ | 3.1 s | no cpufreq |
| network-iperf | ✅ | 35.1 s | lan2 ↑936/↓936 Mbps |
| store-versions | ✅ | 6.2 s | 26.11.0-trunk.65 · 7.2.8-edge-mvebu |
| kernel-switch | ✅ | 106.6 s | branch=current · family=mvebu · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu · kernel_before=7.2.8-edge-mvebu |
| reboot | ✅ | 40.5 s | warm · up 21 s |

### ✅ Cubie A5E 01

`radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 597.2 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 64.3 s | power-cycle · up 32 s |
| kernel-switch | ✅ | 59.0 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.65 · boot_image=? · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 185.2 s | power-cycle · 4/4 boots · up 32 s |
| hw-performance | ✅ | 41.3 s | AES 358 · mem 2000 · disk W 21 / R 23 MB/s · 61.8 °C · None MHz |
| dvfs | ➖ | 2.8 s | no cpufreq |
| network-iperf | ✅ | 94.7 s | end0 ↑839/↓941 (1GE) · end1 ↑941/↓940 (1GE) · wlan0 ↑120/↓129 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 5.8 s | 26.11.0-trunk.65 · 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 577.0 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.65 · boot_image=? · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 188.0 s | power-cycle · 4/4 boots · up 32 s |
| hw-performance | ✅ | 41.7 s | AES 358 · mem 2000 · disk W 21 / R 23 MB/s · 66.2 °C · None MHz |
| dvfs | ➖ | 2.8 s | no cpufreq |
| network-iperf | ✅ | 119.3 s | end0 ↑836/↓940 (1GE) · end1 ↑941/↓940 (1GE) · wlan0 ↑120/↓127 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 5.9 s | 26.11.0-trunk.65 · 7.2.8-edge-sunxi64 |
| kernel-switch | ✅ | 565.9 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.65 · boot_image=? · kernel_before=7.2.8-edge-sunxi64 |
| reboot | ✅ | 64.7 s | power-cycle · up 33 s |

**Power** — min 1.70 W · avg 3.84 W · peak 6.10 W · 2102 samples

```mermaid
xychart-beta
    title "Power — Cubie A5E 01"
    x-axis "sample" 1 --> 2102
    y-axis "W" 1.5 --> 6.5
    line [3.45, 3.54, 3.56, 3.84, 3.54, 4.82, 3.87, 3.57, 3.63, 3.27, 3.42, 3.40, 3.22, 3.32, 3.51, 3.63, 3.58, 3.56, 3.66, 3.91, 4.98, 3.93, 4.84, 4.01, 3.61, 3.40, 3.48, 3.34, 3.78, 3.80, 3.83, 3.80, 3.85, 4.20, 5.14, 4.47, 5.08, 4.67, 3.90, 3.36]
```

### ✅ Cubietruck 01

`cubietruck` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 432.8 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 71.6 s | warm · up 46 s |
| kernel-switch | ✅ | 93.1 s | branch=current · family=sunxi · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 255.4 s | warm · 4/4 boots · up 47 s |
| hw-performance | ✅ | 59.3 s | AES 17 · mem 1700 · disk W 14 / R 22 MB/s · 48.9 °C · 960 MHz |
| dvfs | ✅ | 56.5 s | ondemand · 528–960 MHz (peak 960) |
| network-iperf | ✅ | 167.8 s | end0 ↑730/↓826 (1GE) · wlan0 ↑19/↓24 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 11.6 s | 26.11.0-trunk.65 · 6.18.54-current-sunxi |
| kernel-switch | ✅ | 238.2 s | branch=edge · family=sunxi · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 249.9 s | warm · 4/4 boots · up 43 s |
| hw-performance | ✅ | 57.8 s | AES 19 · mem 1700 · disk W 14 / R 22 MB/s · 48.8 °C · 960 MHz |
| dvfs | ✅ | 56.9 s | ondemand · 528–960 MHz (peak 960) |
| network-iperf | ✅ | 117.1 s | end0 ↑774/↓928 (1GE) · wlan0 ↑18/↓24 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 11.6 s | 26.11.0-trunk.65 · 7.2.8-edge-sunxi |
| kernel-switch | ✅ | 228.5 s | branch=current · family=sunxi · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=7.2.8-edge-sunxi |
| reboot | ✅ | 70.5 s | warm · up 46 s |

### ✅ Cubox i2eX/i4 01

`cubox-i` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 452.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 82.3 s | power-cycle · up 45 s |
| kernel-switch | ✅ | 73.0 s | branch=current · family=imx6 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-imx6 · kernel_before=6.18.54-current-imx6 |
| reboot | ✅ | 255.2 s | power-cycle · 4/4 boots · up 43 s |
| hw-performance | ✅ | 46.9 s | AES 26 · mem 766 · disk W 19 / R 20 MB/s · 50.9 °C · 996 MHz |
| dvfs | ✅ | 40.6 s | ondemand · 396–996 MHz (peak 996) |
| network-iperf | ✅ | 108.5 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑20/↓15 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 8.8 s | 26.11.0-trunk.65 · 6.18.54-current-imx6 |
| kernel-switch | ✅ | 267.6 s | branch=edge · family=imx6 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.1.13-edge-imx6 · kernel_before=6.18.54-current-imx6 |
| reboot | ✅ | 279.8 s | power-cycle · 4/4 boots · up 43 s |
| hw-performance | ✅ | 47.3 s | AES 26 · mem 704 · disk W 19 / R 20 MB/s · 52 °C · 996 MHz |
| dvfs | ✅ | 45.6 s | ondemand · 396–996 MHz (peak 996) |
| network-iperf | ✅ | 82.4 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑19/↓20 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 8.7 s | 26.11.0-trunk.65 · 7.1.13-edge-imx6 |
| kernel-switch | ✅ | 266.3 s | branch=current · family=imx6 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-imx6 · kernel_before=7.1.13-edge-imx6 |
| reboot | ✅ | 77.7 s | power-cycle · up 42 s |

**Power** — min 1.80 W · avg 3.43 W · peak 6.00 W · 1725 samples

```mermaid
xychart-beta
    title "Power — Cubox i2eX/i4 01"
    x-axis "sample" 1 --> 1725
    y-axis "W" 1.5 --> 6.5
    line [3.19, 3.43, 3.34, 3.10, 3.42, 3.91, 3.47, 3.02, 3.05, 3.13, 3.65, 3.29, 3.71, 3.46, 3.75, 3.70, 3.44, 3.51, 3.31, 2.92, 3.47, 3.58, 3.49, 2.97, 3.40, 3.51, 3.79, 2.91, 4.02, 3.85, 3.37, 3.43, 3.37, 3.20, 3.68, 3.42, 3.34, 3.25, 3.06, 4.18]
```

### ✅ Espressobin 01

`espressobin` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 722.3 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 72.7 s | power-cycle · up 42 s |
| kernel-switch | ✅ | 109.1 s | branch=current · family=mvebu64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu64 · kernel_before=6.18.54-current-mvebu64 |
| reboot | ✅ | 236.8 s | power-cycle · 4/4 boots · up 42 s |
| hw-performance | ✅ | 36.8 s | AES 366 · mem 1900 · disk W 20 / R 138 MB/s · None °C · 800 MHz |
| dvfs | ✅ | 34.9 s | ondemand · 200–800 MHz (peak 800) |
| network-iperf | ✅ | 43.9 s | lan0 ↑936/↓740 (1GE) Mbps |
| store-versions | ✅ | 8.2 s | 26.11.0-trunk.65 · 6.18.54-current-mvebu64 |
| kernel-switch | ✅ | 417.2 s | branch=edge · family=mvebu64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.1.13-edge-mvebu64 · kernel_before=6.18.54-current-mvebu64 |
| reboot | ✅ | 235.1 s | power-cycle · 4/4 boots · up 42 s |
| hw-performance | ✅ | 38.1 s | AES 357 · mem 1900 · disk W 17 / R 131 MB/s · None °C · 800 MHz |
| dvfs | ✅ | 35.6 s | ondemand · 200–800 MHz (peak 800) |
| network-iperf | ✅ | 39.8 s | lan0 ↑936/↓766 (1GE) Mbps |
| store-versions | ✅ | 8.2 s | 26.11.0-trunk.65 · 7.1.13-edge-mvebu64 |
| kernel-switch | ✅ | 412.9 s | branch=current · family=mvebu64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu64 · kernel_before=7.1.13-edge-mvebu64 |
| reboot | ✅ | 71.6 s | power-cycle · up 41 s |

### ✅ Helios4 01

`helios4` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 183.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 120.0 s | warm · up 103 s |
| kernel-switch | ✅ | 36.3 s | branch=current · family=mvebu · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu · kernel_before=6.18.54-current-mvebu |
| reboot | ✅ | 463.3 s | warm · 4/4 boots · up 102 s |
| hw-performance | ✅ | 36.5 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 55.1 °C · None MHz |
| dvfs | ➖ | 3.1 s | no cpufreq |
| network-iperf | ✅ | 31.5 s | end1 ↑939/↓939 (1GE) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.65 · 6.18.54-current-mvebu |
| kernel-switch | ✅ | 101.3 s | branch=edge · family=mvebu · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-mvebu · kernel_before=6.18.54-current-mvebu |
| reboot | ✅ | 464.7 s | warm · 4/4 boots · up 103 s |
| hw-performance | ✅ | 37.3 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 54.2 °C · None MHz |
| dvfs | ➖ | 2.4 s | no cpufreq |
| network-iperf | ✅ | 46.4 s | end1 ↑939/↓936 (1GE) Mbps |
| store-versions | ✅ | 5.0 s | 26.11.0-trunk.65 · 7.2.8-edge-mvebu |
| kernel-switch | ✅ | 95.7 s | branch=current · family=mvebu · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu · kernel_before=7.2.8-edge-mvebu |
| reboot | ✅ | 121.6 s | warm · up 104 s |

### ✅ Inovato Quadra 01

`inovato-quadra` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 206.1 s | nightly · ? → 26.11.0-trunk.65 |
| reboot | ✅ | 55.1 s | power-cycle · up 24 s |
| kernel-switch | ✅ | 43.2 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 151.7 s | power-cycle · 4/4 boots · up 24 s |
| hw-performance | ✅ | 30.3 s | AES 794 · mem 2800 · disk W 22 / R 23 MB/s · 66.5 °C · 1704 MHz |
| dvfs | ✅ | 21.7 s | ondemand · 480–1704 MHz (peak 1704) |
| network-iperf | ✅ | 60.6 s | eth0 ↑94/↓94 (10/100ME) · wlan0 ↑13/↓21 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.65 · 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 114.4 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 150.8 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 30.9 s | AES 794 · mem 2800 · disk W 14 / R 23 MB/s · 67.6 °C · 1704 MHz |
| dvfs | ✅ | 22.3 s | ondemand · 480–1704 MHz (peak 1704) |
| network-iperf | ✅ | 59.1 s | eth0 ↑94/↓94 (10/100ME) · wlan0 ↑7/↓18 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.65 · 7.2.8-edge-sunxi64 |
| kernel-switch | ✅ | 119.3 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=7.2.8-edge-sunxi64 |
| reboot | ✅ | 54.9 s | power-cycle · up 24 s |

**Power** — min 1.90 W · avg 4.05 W · peak 6.70 W · 912 samples

```mermaid
xychart-beta
    title "Power — Inovato Quadra 01"
    x-axis "sample" 1 --> 912
    y-axis "W" 1.5 --> 7.0
    line [3.98, 3.96, 4.22, 4.14, 4.10, 4.39, 4.13, 3.99, 3.26, 4.47, 4.24, 3.26, 3.91, 3.67, 4.33, 4.08, 4.49, 4.86, 4.08, 3.86, 4.28, 4.49, 4.06, 4.17, 3.91, 3.35, 4.22, 4.17, 3.44, 3.97, 4.15, 4.73, 3.87, 3.81, 4.29, 4.05, 4.29, 4.16, 3.66, 3.46]
```

### ✅ Khadas Edge2 01

`khadas-edge2` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 120.1 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 29.6 s | warm · up 12 s |
| kernel-switch | ✅ | 25.3 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 118.2 s | warm · 4/4 boots · up 15 s |
| hw-performance | ✅ | 15.5 s | AES 1277 · mem 15000 · disk W 104 / R 259 MB/s · 37.9 °C · 1800 MHz |
| dvfs | ✅ | 18.3 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ⏭️ | 6.9 s | no cabled interfaces |
| store-versions | ✅ | 4.3 s | 26.11.0-trunk.65 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 75.2 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 106.1 s | warm · 4/4 boots · up 9 s |
| hw-performance | ✅ | 15.5 s | AES 1273 · mem 8600 · disk W 103 / R 240 MB/s · 40.7 °C · 1800 MHz |
| dvfs | ✅ | 14.4 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ⏭️ | 6.5 s | no cabled interfaces |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 59.9 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 28.3 s | warm · up 10 s |

### ✅ Khadas VIM2 01

`khadas-vim2` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 307.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 41.6 s | warm · up 24 s |
| kernel-switch | ✅ | 70.1 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 152.5 s | warm · 4/4 boots · up 25 s |
| hw-performance | ✅ | 24.1 s | AES 653 · mem 3500 · disk W 41 / R 151 MB/s · 55 °C · 1512 MHz |
| dvfs | ✅ | 24.9 s | ondemand · 500–1512 MHz (peak 1512) |
| network-iperf | ✅ | 64.5 s | eth0 ↑939/↓941 (1GE) · wlan0 ↑103/↓89 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.8 s | 26.11.0-trunk.65 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 196.4 s | branch=edge · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 154.6 s | warm · 4/4 boots · up 26 s |
| hw-performance | ✅ | 25.2 s | AES 654 · mem 3500 · disk W 41 / R 137 MB/s · 55 °C · 1512 MHz |
| dvfs | ✅ | 26.0 s | ondemand · 500–1512 MHz (peak 1512) |
| network-iperf | ✅ | 69.9 s | eth0 ↑941/↓941 (1GE) · wlan0 ↑88/↓62 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.7 s | 26.11.0-trunk.65 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 196.1 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 39.0 s | warm · up 22 s |

### ✅ Khadas VIM4 01

`khadas-vim4` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 131.8 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
| reboot | ✅ | 53.6 s | power-cycle · up 20 s |
| kernel-switch | ✅ | 24.3 s | branch=legacy · family=meson-s4t7 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-5.15.137-legacy-meson-s4t7 · kernel_before=5.15.137-legacy-meson-s4t7 |
| reboot | ✅ | 52.8 s | power-cycle · up 19 s |
| hw-performance | ✅ | 19.8 s | AES 1246 · mem 6800 · disk W 106 / R 169 MB/s · 47.4 °C · 2208 MHz |
| dvfs | ✅ | 22.4 s | ondemand · 500–2208 MHz (peak 2208) |
| network-iperf | ✅ | 106.6 s | eth0 ↑927/↓935 (1GE) · wlan0 ↑5/↓2 (Wi-Fi 6) · wlan1 ↑77/↓3 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 5.0 s | 26.11.0-trunk.54 · 5.15.137-legacy-meson-s4t7 |

**Power** — min 0.60 W · avg 3.93 W · peak 8.40 W · 336 samples

```mermaid
xychart-beta
    title "Power — Khadas VIM4 01"
    x-axis "sample" 1 --> 336
    y-axis "W" 0.5 --> 8.5
    line [3.20, 3.85, 4.13, 4.23, 4.00, 4.31, 4.14, 4.14, 4.20, 4.04, 3.90, 3.86, 4.10, 4.08, 3.38, 2.85, 2.74, 3.68, 4.25, 4.27, 4.16, 3.50, 3.47, 3.75, 4.59, 4.41, 4.10, 4.94, 5.27, 3.80, 3.73, 3.88, 3.91, 3.47, 3.60, 3.65, 3.51, 4.26, 4.00, 3.63]
```

### ✅ Mekotronics R58HD 01

`mekotronics-r58hd` · **inplace** · image `26.11.0-trunk.62` · 6 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 93.2 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 45.4 s | power-cycle · up 14 s |
| hw-performance | ✅ | 14.1 s | AES 1303 · mem 16000 · disk W 250 / R 288 MB/s · 47.2 °C · 1800 MHz |
| dvfs | ✅ | 16.9 s | ondemand · 1800–1800 MHz (peak 2304) |
| network-iperf | ✅ | 53.2 s | end0 ↑936/↓928 (1GE) · enP3p49s0 ↑783/↓823 (1GE) Mbps |
| store-versions | ✅ | 3.7 s | 26.11.0-trunk.65 · 6.1.172-vendor-rk35xx |

**Power** — min 3.90 W · avg 6.12 W · peak 12.00 W · 189 samples

```mermaid
xychart-beta
    title "Power — Mekotronics R58HD 01"
    x-axis "sample" 1 --> 189
    y-axis "W" 3.5 --> 12.5
    line [5.20, 5.20, 5.48, 6.10, 6.62, 6.16, 5.78, 6.50, 6.20, 7.00, 6.80, 6.48, 5.44, 6.72, 6.75, 6.16, 6.32, 6.98, 6.40, 5.20, 4.94, 3.90, 4.30, 5.90, 6.40, 5.40, 5.80, 6.22, 10.86, 10.12, 6.86, 5.46, 5.55, 5.60, 5.78, 5.72, 5.78, 5.48, 5.80, 5.78]
```

### ✅ Mekotronics R58S2 01

`mekotronics-r58s2` · **inplace** · image `26.8.3` · 5 ✅ · 0 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 146.7 s | — |
| reboot | ✅ | 44.2 s | power-cycle · up 14 s |
| hw-performance | ✅ | 14.6 s | AES 1279 · mem 15000 · disk W 237 / R 274 MB/s · 45.3 °C · 1800 MHz |
| dvfs | ✅ | 17.7 s | ondemand · 1800–1800 MHz (peak 2352) |
| network-iperf | ✅ | 58.1 s | end1 ↑917/↓922 (1GE) · wlan0 ↑56/↓163 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.2 s | 26.8.3 · 6.1.172-vendor-rk35xx |

### ✅ NanoPi Fire3 01

`nanopifire3` · **inplace** · image `26.11.0-trunk.62` · 7 ✅ · 0 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 493.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 66.1 s | power-cycle · up 32 s |
| kernel-switch | ✅ | 91.4 s | branch=edge · family=s5p6818 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-s5p6818 · kernel_before=7.2.8-edge-s5p6818 |
| reboot | ✅ | 170.8 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 44.0 s | AES 373 · mem 2000 · disk W 1 / R 22 MB/s · 66 °C · None MHz |
| dvfs | ➖ | 3.0 s | no cpufreq |
| network-iperf | ✅ | 52.9 s | eth0 ↑845/↓875 (1GE) Mbps |
| store-versions | ✅ | 6.2 s | 26.11.0-trunk.65 · 7.2.8-edge-s5p6818 |

### ✅ NanoPi K2 01

`nanopik2-s905` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 298.0 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 44.6 s | warm · up 29 s |
| kernel-switch | ✅ | 46.8 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 134.0 s | warm · 4/4 boots · up 20 s |
| hw-performance | ✅ | 30.6 s | AES 51 · mem 3700 · disk W 11 / R 1 MB/s · 60 °C · 2016 MHz |
| dvfs | ✅ | 21.2 s | ondemand · 500–1536 MHz (peak 1536) |
| network-iperf | ✅ | 69.3 s | end0 ↑934/↓941 (1GE) · wlan0 ↑15/↓31 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.65 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 159.7 s | branch=edge · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 143.6 s | warm · 4/4 boots · up 24 s |
| hw-performance | ✅ | 32.1 s | AES 51 · mem 3800 · disk W 1 / R 41 MB/s · 61 °C · 2016 MHz |
| dvfs | ✅ | 21.6 s | ondemand · 500–1536 MHz (peak 1536) |
| network-iperf | ✅ | 58.8 s | end0 ↑936/↓941 (1GE) · wlan0 ↑13/↓29 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.65 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 162.3 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 36.2 s | warm · up 19 s |

### ✅ NanoPi M4V2 01

`nanopim4v2` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 214.5 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 58.7 s | power-cycle · up 31 s |
| kernel-switch | ✅ | 31.1 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 167.2 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 21.2 s | AES 1020 · mem 6600 · disk W 54 / R 60 MB/s · 46.9 °C · 1416 MHz |
| dvfs | ✅ | 20.8 s | ondemand · 408–1416 MHz (peak 1800) |
| network-iperf | ✅ | 100.3 s | end0 ↑924/↓914 (1GE) · wlan0 ↑134/↓85 (Wi-Fi 5) · wlx803f5d16af63 ↑13/↓30 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.3 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 95.2 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 164.1 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 21.8 s | AES 1018 · mem 6600 · disk W 53 / R 60 MB/s · 46.9 °C · 1416 MHz |
| dvfs | ✅ | 68.9 s | ondemand · 408–1416 MHz (peak 1800) |
| network-iperf | ✅ | 88.9 s | end0 ↑939/↓939 (1GE) · wlan0 ↑74/↓65 (Wi-Fi 5) · wlx803f5d16af63 ↑126/↓202 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.65 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 97.6 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 56.8 s | power-cycle · up 25 s |

**Power** — min 2.50 W · avg 7.20 W · peak 12.80 W · 964 samples

```mermaid
xychart-beta
    title "Power — NanoPi M4V2 01"
    x-axis "sample" 1 --> 964
    y-axis "W" 2.0 --> 13.0
    line [6.48, 6.50, 9.20, 9.30, 9.96, 10.40, 9.44, 9.82, 5.80, 8.22, 5.93, 6.25, 5.96, 5.69, 7.06, 7.88, 8.53, 6.67, 6.98, 6.74, 6.45, 8.05, 7.28, 7.40, 5.29, 5.87, 6.53, 6.49, 6.30, 7.95, 6.34, 6.53, 6.27, 6.87, 6.94, 6.85, 6.87, 7.57, 7.24, 6.22]
```

### ✅ NanoPi M5 01

`nanopi-m5` · **inplace** · image `26.11.0-trunk.58` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 152.5 s | nightly · 26.11.0-trunk.58 → 26.11.0-trunk.65 |
| reboot | ✅ | 48.7 s | power-cycle · up 23 s |
| kernel-switch | ✅ | 23.5 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 309.4 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 17.8 s | AES 1271 · mem 8000 · disk W 67 / R 77 MB/s · 43.5 °C · 2016 MHz |
| dvfs | ✅ | 19.4 s | ondemand · 2016–2016 MHz (peak 2208) |
| network-iperf | ✅ | 106.1 s | end0 ↑939/↓939 (1GE) · end1 ↑939/↓939 (1GE) · wlan0 ↑43/↓88 (Wi-Fi 5) · wlx44334c47dec3 ↑29/↓18 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.65 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 100.7 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 149.4 s | power-cycle · 4/4 boots · up 24 s |
| hw-performance | ✅ | 26.3 s | AES 1328 · mem 9000 · disk W 20 / R 21 MB/s · 42.5 °C · 2016 MHz |
| dvfs | ✅ | 17.2 s | ondemand · 408–2016 MHz (peak 2208) |
| network-iperf | ✅ | 105.7 s | end0 ↑939/↓866 (1GE) · end1 ↑741/↓777 (1GE) · wlan0 ↑99/↓182 (Wi-Fi 5) · wlx44334c47dec3 ↑35/↓17 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 103.5 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 155.8 s | power-cycle · 4/4 boots · up 26 s |
| hw-performance | ✅ | 26.3 s | AES 1329 · mem 9000 · disk W 20 / R 21 MB/s · 43.5 °C · 2016 MHz |
| dvfs | ✅ | 17.5 s | ondemand · 408–2016 MHz (peak 2208) |
| network-iperf | ✅ | 109.4 s | end0 ↑931/↓848 (1GE) · end1 ↑939/↓939 (1GE) · wlan0 ↑79/↓172 (Wi-Fi 5) · wlx44334c47dec3 ↑38/↓20 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.65 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 104.4 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 133.5 s | power-cycle · up 107 s |

**Power** — min 1.80 W · avg 4.80 W · peak 8.70 W · 1385 samples

```mermaid
xychart-beta
    title "Power — NanoPi M5 01"
    x-axis "sample" 1 --> 1385
    y-axis "W" 1.5 --> 9.0
    line [5.22, 5.19, 5.90, 5.28, 4.45, 4.35, 4.06, 3.90, 3.69, 4.16, 3.90, 3.70, 5.90, 5.43, 5.21, 5.22, 5.68, 5.26, 4.19, 4.12, 3.93, 5.04, 5.64, 5.26, 4.95, 5.73, 5.34, 4.81, 4.11, 4.28, 4.19, 5.80, 5.10, 5.43, 5.06, 5.16, 5.47, 3.78, 4.03, 3.91]
```

### ✅ NanoPi M6 01

`nanopi-m6` · **inplace** · image `26.11.0-trunk.62` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 136.3 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 51.2 s | power-cycle · up 22 s |
| kernel-switch | ✅ | 21.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 137.2 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 17.6 s | AES 1256 · mem 13900 · disk W 51 / R 78 MB/s · 47.2 °C · 1800 MHz |
| dvfs | ✅ | 18.0 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ✅ | 57.1 s | lan ↑835/↓874 (1GE) · wlP3p49s0 ↑118/↓227 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.65 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 97.4 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 135.3 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 19.1 s | AES 1214 · mem 9900 · disk W 46 / R 56 MB/s · 49 °C · 1800 MHz |
| dvfs | ✅ | 15.9 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 61.7 s | lan ↑937/↓694 (1GE) · wlP3p49s0 ↑227/↓252 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.8 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 80.6 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 135.9 s | power-cycle · 4/4 boots · up 19 s |
| hw-performance | ✅ | 18.6 s | AES 1203 · mem 7800 · disk W 49 / R 57 MB/s · 50.8 °C · 1800 MHz |
| dvfs | ✅ | 14.5 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 57.9 s | lan ↑936/↓933 (1GE) · wlP3p49s0 ↑171/↓199 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.65 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 78.5 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 48.2 s | power-cycle · up 21 s |

**Power** — min 0.90 W · avg 3.98 W · peak 10.10 W · 953 samples

```mermaid
xychart-beta
    title "Power — NanoPi M6 01"
    x-axis "sample" 1 --> 953
    y-axis "W" 0.5 --> 10.5
    line [3.58, 4.24, 3.30, 3.88, 3.55, 2.39, 3.98, 2.77, 3.83, 4.00, 2.40, 4.61, 4.79, 3.51, 4.03, 3.50, 3.82, 3.26, 2.96, 3.46, 4.35, 2.67, 4.89, 6.43, 4.69, 4.61, 4.48, 4.85, 4.12, 4.08, 4.12, 3.40, 3.27, 5.49, 4.39, 4.43, 4.59, 4.74, 4.72, 2.97]
```

### ✅ NanoPi Neo 3 01

`nanopineo3` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 282.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 56.4 s | power-cycle · up 27 s |
| kernel-switch | ✅ | 61.3 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 168.8 s | power-cycle · 4/4 boots · up 28 s |
| hw-performance | ✅ | 28.5 s | AES 599 · mem 2400 · disk W 52 / R 63 MB/s · 80 °C · 1296 MHz |
| dvfs | ✅ | 30.2 s | ondemand · 408–1296 MHz (peak 1296) |
| network-iperf | ✅ | 79.5 s | end0 ↑920/↓941 (1GE) · wlx7cdd905518f9 ↑27/↓26 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 7.2 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 178.2 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 162.8 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 28.7 s | AES 599 · mem 2300 · disk W 51 / R 63 MB/s · 80.8 °C · 1296 MHz |
| dvfs | ✅ | 31.1 s | ondemand · 408–1296 MHz (peak 1296) |
| network-iperf | ✅ | 68.4 s | end0 ↑918/↓941 (1GE) · wlx7cdd905518f9 ↑28/↓29 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 6.6 s | 26.11.0-trunk.65 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 181.1 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 56.9 s | power-cycle · up 28 s |

### ✅ NanoPi R6S 01

`nanopi-r6s` · **inplace** · image `26.11.0-trunk.62` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 82.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 39.9 s | power-cycle · up 15 s |
| kernel-switch | ✅ | 19.1 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 100.8 s | power-cycle · 4/4 boots · up 15 s |
| hw-performance | ✅ | 14.1 s | AES 1274 · mem 13200 · disk W 208 / R 274 MB/s · 36.1 °C · 1800 MHz |
| dvfs | ✅ | 17.6 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ✅ | 43.9 s | lan2 ↑939/↓536 (1GE) Mbps |
| store-versions | ✅ | 4.0 s | 26.11.0-trunk.65 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 51.0 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 97.7 s | power-cycle · 4/4 boots · up 12 s |
| hw-performance | ✅ | 15.4 s | AES 1273 · mem 10400 · disk W 149 / R 150 MB/s · 37.9 °C · 1800 MHz |
| dvfs | ✅ | 14.9 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 30.5 s | lan2 ↑833/↓590 (1GE) Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 43.6 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 99.9 s | power-cycle · 4/4 boots · up 14 s |
| hw-performance | ✅ | 15.3 s | AES 1277 · mem 8200 · disk W 149 / R 146 MB/s · 37.9 °C · 1800 MHz |
| dvfs | ✅ | 15.4 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 30.6 s | lan2 ↑521/↓656 (1GE) Mbps |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.65 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 39.4 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 45.6 s | power-cycle · up 14 s |

**Power** — min 1.00 W · avg 4.68 W · peak 10.10 W · 646 samples

```mermaid
xychart-beta
    title "Power — NanoPi R6S 01"
    x-axis "sample" 1 --> 646
    y-axis "W" 0.5 --> 10.5
    line [3.51, 4.23, 4.79, 4.75, 4.28, 4.36, 4.75, 4.44, 4.79, 4.22, 2.91, 3.95, 4.99, 5.14, 4.00, 3.76, 5.90, 4.57, 4.09, 4.81, 4.75, 4.22, 4.37, 6.25, 6.38, 4.70, 4.94, 5.48, 4.66, 4.93, 4.72, 4.38, 4.58, 5.24, 6.89, 4.65, 5.09, 5.64, 4.11, 3.19]
```

### ✅ NanoPi R76S 01

`nanopi-r76s` · **inplace** · image `26.11.0-trunk.57` · 15 ✅ · 0 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 11.4 s | — |
| reboot | ✅ | 70.8 s | power-cycle · up 29 s |
| kernel-switch | ✅ | 148.4 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 282.8 s | power-cycle · 4/4 boots · up 31 s |
| hw-performance | ✅ | 25.2 s | AES 1274 · mem 7500 · disk W 18 / R 77 MB/s · 40.7 °C · 2016 MHz |
| dvfs | ✅ | 21.4 s | ondemand · 2016–2016 MHz (peak 2208) |
| network-iperf | ✅ | 125.4 s | end0 ↑808/↓839 (1GE) · end1 ↑927/↓864 (1GE) · wlan0 ↑39/↓90 (Wi-Fi 5) · wlxe0e1a933de37 ↑176/↓184 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.57 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 167.4 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 184.4 s | power-cycle · 4/4 boots · up 26 s |
| hw-performance | ✅ | 22.4 s | AES 1314 · mem 8800 · disk W 19 / R 71 MB/s · 41.6 °C · 2016 MHz |
| dvfs | ✅ | 19.5 s | ondemand · 408–2016 MHz (peak 2208) |
| network-iperf | ✅ | 112.4 s | end0 ↑938/↓939 (1GE) · end1 ↑939/↓939 (1GE) · wlan0 ↑71/↓175 (Wi-Fi 5) · wlxe0e1a933de37 ↑196/↓215 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.4 s | 26.11.0-trunk.57 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 100.1 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 72.2 s | power-cycle · up 29 s |

**Power** — min 1.60 W · avg 3.74 W · peak 8.10 W · 1076 samples

```mermaid
xychart-beta
    title "Power — NanoPi R76S 01"
    x-axis "sample" 1 --> 1076
    y-axis "W" 1.5 --> 8.5
    line [3.78, 2.23, 4.33, 3.95, 3.81, 4.00, 4.26, 2.72, 2.88, 3.05, 3.21, 2.63, 2.68, 2.43, 3.31, 4.72, 4.20, 4.06, 4.09, 4.71, 4.47, 4.51, 4.31, 3.66, 4.13, 3.06, 2.88, 3.73, 3.10, 2.35, 4.13, 5.13, 4.24, 4.31, 4.70, 4.67, 4.31, 4.74, 3.58, 2.69]
```

### ✅ Odroid C2 01

`odroidc2` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 208.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 33.6 s | warm · up 17 s |
| kernel-switch | ✅ | 39.8 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 119.0 s | warm · 4/4 boots · up 17 s |
| hw-performance | ✅ | 22.5 s | AES 51 · mem 3500 · disk W 32 / R 145 MB/s · 45 °C · 1536 MHz |
| dvfs | ✅ | 22.1 s | ondemand · 500–1536 MHz (peak 1536) |
| network-iperf | ✅ | 49.0 s | end0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.65 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 118.1 s | branch=edge · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 118.1 s | warm · 4/4 boots · up 17 s |
| hw-performance | ✅ | 22.5 s | AES 51 · mem 3500 · disk W 33 / R 152 MB/s · 46 °C · 1536 MHz |
| dvfs | ✅ | 22.4 s | ondemand · 500–1536 MHz (peak 1536) |
| network-iperf | ✅ | 32.8 s | end0 ↑939/↓941 (1GE) Mbps |
| store-versions | ✅ | 5.1 s | 26.11.0-trunk.65 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 116.8 s | branch=current · family=meson64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 34.3 s | warm · up 16 s |

### ✅ Odroid M1 01

`odroidm1` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 144.8 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 54.9 s | power-cycle · up 20 s |
| kernel-switch | ✅ | 33.5 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 141.7 s | power-cycle · 4/4 boots · up 20 s |
| hw-performance | ✅ | 17.0 s | AES 917 · mem 5000 · disk W 1065 / R 1007 MB/s · 35 °C · 1992 MHz |
| dvfs | ✅ | 21.2 s | ondemand · 408–1992 MHz (peak 1992) |
| network-iperf | ✅ | 58.3 s | eth0 ↑629/↓941 (1GE) · wlx40a5eff39254 ↑13/↓160 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.65 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 89.2 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 143.6 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 17.8 s | AES 916 · mem 5100 · disk W 1044 / R 1017 MB/s · 35.6 °C · 1992 MHz |
| dvfs | ✅ | 23.7 s | ondemand · 408–1992 MHz (peak 1992) |
| network-iperf | ✅ | 59.7 s | eth0 ↑941/↓941 (1GE) · wlx40a5eff39254 ↑191/↓216 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.6 s | 26.11.0-trunk.65 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 89.4 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 52.8 s | power-cycle · up 20 s |

**Power** — min 1.90 W · avg 6.35 W · peak 10.90 W · 749 samples

```mermaid
xychart-beta
    title "Power — Odroid M1 01"
    x-axis "sample" 1 --> 749
    y-axis "W" 1.5 --> 11.0
    line [5.48, 8.57, 5.94, 6.04, 8.04, 5.93, 5.99, 6.68, 6.90, 6.11, 5.30, 7.92, 5.37, 6.14, 5.66, 6.55, 6.17, 5.84, 5.74, 5.71, 6.55, 6.92, 5.92, 5.61, 5.99, 7.29, 7.22, 7.19, 4.97, 6.29, 7.02, 5.53, 5.77, 6.03, 7.14, 8.14, 5.90, 6.59, 5.04, 6.55]
```

### ✅ Orange Pi 3 01

`orangepi3` · **inplace** · image `26.11.0-trunk.58` · 15 ✅ · 0 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 20.8 s | — |
| reboot | ✅ | 55.6 s | power-cycle · up 33 s |
| kernel-switch | ✅ | 37.5 s | branch=current · family=sunxi64 · installed=26.8.0-trunk.61 · boot_image=/boot/vmlinuz-6.18.33-current-sunxi64 · kernel_before=6.18.33-current-sunxi64 |
| reboot | ✅ | 838.2 s | power-cycle · 1/4 boots · up 25 s |
| hw-performance | ✅ | 28.8 s | AES 833 · mem 4600 · disk W 20 / R 0 MB/s · 46.7 °C · 1800 MHz |
| dvfs | ✅ | 20.7 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 133.3 s | end0 ↑913/↓938 (1GE) · wlan0 ↑59/↓111 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.58 · 6.18.33-current-sunxi64 |
| kernel-switch | ✅ | 103.7 s | branch=edge · family=sunxi64 · installed=26.8.0-trunk.61 · boot_image=/boot/vmlinuz-7.0.10-edge-sunxi64 · kernel_before=6.18.33-current-sunxi64 |
| reboot | ✅ | 802.3 s | power-cycle · 1/4 boots · up 24 s |
| hw-performance | ✅ | 29.1 s | AES 839 · mem 4600 · disk W 21 / R 23 MB/s · 45.2 °C · 1800 MHz |
| dvfs | ✅ | 20.9 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 59.5 s | end0 ↑918/↓939 (1GE) · wlan0 ↑59/↓115 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.58 · 7.0.10-edge-sunxi64 |
| kernel-switch | ✅ | 96.6 s | branch=current · family=sunxi64 · installed=26.8.0-trunk.61 · boot_image=/boot/vmlinuz-6.18.33-current-sunxi64 · kernel_before=7.0.10-edge-sunxi64 |
| reboot | ✅ | 57.7 s | power-cycle · up 28 s |

### ✅ Radxa ZERO 3 01

`radxa-zero3` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 0.0 s | — |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-performance | ✅ | 33.7 s | AES 722 · mem 3900 · disk W 20 / R 23 MB/s · 46.7 °C · 1416 MHz |
| dvfs | ✅ | 26.6 s | ondemand · 408–1416 MHz (peak 1416) |
| network-iperf | ✅ | 45.0 s | wlan0 ↑1/↓16 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 6.0 s | 26.5.1 · 6.18.44-current-rockchip64 |

### ✅ SpacemiT K3 Pico-ITX 01

`k3picoitx` · **inplace** · image `26.11.0-trunk.62` · 8 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 75.0 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.65 |
| reboot | ✅ | 45.0 s | power-cycle · up 22 s |
| kernel-switch | ✅ | 18.9 s | branch=legacy · family=spacemit-k3 · installed=26.11.0-trunk.65 · boot_image=/boot/vmlinuz-6.18.3-legacy-spacemit-k3 · kernel_before=6.18.3-legacy-spacemit-k3 |
| reboot | ✅ | 136.0 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 13.2 s | AES 778 · mem 12500 · disk W 1358 / R 1473 MB/s · 43 °C · 2150 MHz |
| dvfs | ✅ | 15.3 s | performance · 614–2150 MHz (peak 2150) |
| network-iperf | ✅ | 75.9 s | eth0 ↑939/↓938 (1GE) · eth1 ↑939/↓939 (10GE) · wlan0 ↑72/↓126 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 3.7 s | 26.11.0-trunk.65 · 6.18.3-legacy-spacemit-k3 |


<!-- FLEET-STOP -->
