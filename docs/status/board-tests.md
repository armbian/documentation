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

**65** boards — **54** passed, **11** failed. Most recent test of every board; failures first.

## ❌ Failed (11)

### ❌ Banana Pi M2 Ultra 01

`bananapim2ultra` · **inplace** · image `26.11.0-trunk.62` · 0 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| reachable | ❌ | 0.0 s | ip=10.0.50.83 · reachable=False · port=22 |

### ❌ Inovato Quadra 01

`inovato-quadra` · **inplace** · image `26.11.0-trunk.62` · 13 ✅ · 3 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ❌ | 75.4 s | nightly · ? → ? |
| reboot | ✅ | 73.3 s | power-cycle · up 41 s |
| kernel-switch | ✅ | 45.8 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 173.8 s | power-cycle · 4/4 boots · up 42 s |
| hw-performance | ✅ | 29.8 s | AES 795 · mem 2900 · disk W 14 / R 28 MB/s · 63.4 °C · 1704 MHz |
| dvfs | ✅ | 24.0 s | ondemand · 480–1704 MHz (peak 1704) |
| network-iperf | ❌ | 336.0 s | eth0 ↑94/↓94 (10/100ME) · wlan0 ↑0/↓0 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.6 s | 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 110.2 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 148.7 s | power-cycle · 4/4 boots · up 29 s |
| hw-performance | ✅ | 30.3 s | AES 795 · mem 2800 · disk W 14 / R 23 MB/s · 64.6 °C · 1704 MHz |
| dvfs | ✅ | 22.0 s | ondemand · 480–1704 MHz (peak 1704) |
| network-iperf | ❌ | 300.5 s | eth0 ↑94/↓94 (10/100ME) · wlan0 ↑0/↓0 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 7.2.8-edge-sunxi64 |
| kernel-switch | ✅ | 116.6 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=7.2.8-edge-sunxi64 |
| reboot | ✅ | 57.7 s | power-cycle · up 27 s |

**Power** — min 2.20 W · avg 3.81 W · peak 6.60 W · 1238 samples

```mermaid
xychart-beta
    title "Power — Inovato Quadra 01"
    x-axis "sample" 1 --> 1238
    y-axis "W" 2.0 --> 7.0
    line [3.46, 4.09, 3.42, 3.57, 4.03, 3.73, 4.08, 3.78, 3.73, 3.90, 4.45, 3.71, 3.53, 3.47, 3.45, 3.45, 3.63, 3.67, 3.46, 3.85, 4.01, 4.07, 3.74, 4.17, 4.45, 3.90, 3.99, 4.39, 3.57, 3.54, 3.60, 3.63, 3.70, 3.64, 3.47, 4.09, 4.03, 4.28, 3.94, 3.85]
```

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

### ❌ NanoPi M4V2 01

`nanopim4v2` · **inplace** · image `26.11.0-trunk.62` · 13 ✅ · 3 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 73.5 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 57.5 s | power-cycle · up 25 s |
| kernel-switch | ✅ | 30.6 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 164.1 s | power-cycle · 4/4 boots · up 27 s |
| hw-performance | ✅ | 21.6 s | AES 1016 · mem 6600 · disk W 54 / R 60 MB/s · 45 °C · 1416 MHz |
| dvfs | ✅ | 37.2 s | ondemand · 408–1416 MHz (peak 1800) |
| network-iperf | ❌ | 528.9 s | end0 ↑927/↓925 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) · wlx803f5d16af63 ↑0/↓0 (Wi-Fi 5) Mbps |
| store-versions | ❌ | 23.5 s | — |
| kernel-switch | ❌ | 37.1 s | branch=edge · phase=install · dpkg_state=absent |
| reboot | ✅ | 387.3 s | power-cycle · 3/4 boots · up 25 s |
| hw-performance | ✅ | 20.9 s | AES 1019 · mem 6600 · disk W 54 / R 60 MB/s · 38.1 °C · 1416 MHz |
| dvfs | ✅ | 20.2 s | ondemand · 408–1416 MHz (peak 1800) |
| network-iperf | ✅ | 86.0 s | end0 ↑877/↓913 (1GE) · wlan0 ↑148/↓202 (Wi-Fi 5) · wlx803f5d16af63 ↑118/↓191 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 29.4 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 56.0 s | power-cycle · up 25 s |

**Power** — min 2.60 W · avg 7.01 W · peak 13.60 W · 639 samples

```mermaid
xychart-beta
    title "Power — NanoPi M4V2 01"
    x-axis "sample" 1 --> 639
    y-axis "W" 2.5 --> 14.0
    line [6.77, 6.29, 6.79, 6.96, 6.15, 5.66, 6.89, 8.09, 6.53, 5.15, 8.19, 4.74, 5.26, 8.07, 6.08, 6.54, 8.42, 9.30, 8.51, 9.22, 9.10, 7.70, 5.79, 7.80, 5.02, 6.52, 5.59, 6.01, 6.97, 8.84, 8.98, 7.41, 6.64, 7.25, 7.07, 7.62, 7.25, 6.60, 5.44, 7.07]
```

### ❌ Orange Pi 5 01

`orangepi5` · **inplace** · image `26.8.3` · 0 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| reachable | ❌ | 0.0 s | ip=10.0.50.46 · reachable=False · port=22 |

### ❌ Orange Pi One+ 01

`orangepioneplus` · **inplace** · image `26.11.0-trunk.62` · 15 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 61.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 40.9 s | warm · up 25 s |
| kernel-switch | ✅ | 45.1 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 139.3 s | warm · 4/4 boots · up 23 s |
| hw-performance | ✅ | 29.4 s | AES 839 · mem 4600 · disk W 21 / R 1 MB/s · 62.4 °C · 1800 MHz |
| dvfs | ✅ | 22.5 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 59.5 s | end0 ↑912/↓939 (1GE) · wlx00e04c881724 ↑153/↓195 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.0 s | 26.11.0-trunk.62 · 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 123.4 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 158.6 s | warm · 4/4 boots · up 20 s |
| hw-performance | ✅ | 29.7 s | AES 839 · mem 4600 · disk W 21 / R 23 MB/s · 65.7 °C · 1800 MHz |
| dvfs | ✅ | 23.3 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 64.1 s | end0 ↑917/↓940 (1GE) · wlx00e04c881724 ↑153/↓127 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.3 s | 26.11.0-trunk.62 · 7.2.8-edge-sunxi64 |
| kernel-switch | ❌ | 25.2 s | branch=current · phase=install · dpkg_state=absent |
| reboot | ✅ | 38.8 s | warm · up 21 s |

### ❌ Orange Pi Prime 01

`orangepiprime` · **inplace** · image `26.11.0-trunk.59` · 0 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| reachable | ❌ | 0.0 s | ip=10.0.50.46 · reachable=False · port=22 |

### ❌ Orange Pi Zero2 01

`orangepizero2` · **inplace** · image `26.11.0-trunk.62` · 0 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| reachable | ❌ | 0.0 s | ip=10.0.50.74 · reachable=False · port=22 |

### ❌ ROCK 2F 01

`rock-2f` · **inplace** · image `26.8.1` · 0 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| reachable | ❌ | 0.0 s | ip=10.0.20.164 · reachable=False · port=22 |

### ❌ Rock 5B 02

`rock-5b` · **inplace** · image `26.11.0-trunk.62` · 0 ✅ · 1 ❌ · 21 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 9.1 s | — |
| reboot | ❌ | 135.5 s | power-cycle · up 103 s |
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

**Power** — min 2.80 W · avg 3.64 W · peak 5.70 W · 107 samples

```mermaid
xychart-beta
    title "Power — Rock 5B 02"
    x-axis "sample" 1 --> 107
    y-axis "W" 2.5 --> 6.0
    line [2.90, 2.83, 3.20, 4.00, 3.40, 3.27, 3.60, 3.13, 3.23, 3.90, 3.77, 4.33, 5.60, 5.67, 5.03, 3.70, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.97]
```

### ❌ SpacemiT MusePi Pro 01

`musepipro` · **inplace** · image `26.11.0-trunk.61` · 1 ✅ · 1 ❌ · 4 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 64.3 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ❌ | 221.9 s | power-cycle |
| hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| dvfs | ⏭️ | 0.0 s | — |
| net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
| store-versions | ⏭️ | 0.0 s | — |

**Power** — min 2.00 W · avg 3.24 W · peak 5.00 W · 227 samples

```mermaid
xychart-beta
    title "Power — SpacemiT MusePi Pro 01"
    x-axis "sample" 1 --> 227
    y-axis "W" 1.5 --> 5.5
    line [4.00, 4.00, 4.52, 4.70, 4.77, 4.50, 4.50, 4.63, 4.37, 4.72, 4.70, 4.00, 4.36, 2.47, 2.37, 2.76, 2.70, 2.67, 2.66, 2.68, 2.65, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.70, 2.67, 2.60, 2.70, 2.70, 2.70, 2.70]
```

## ✅ Passed (54)

### ✅ Arduino UNO Q 01

`arduino-uno-q` · **inplace** · image `26.11.0-trunk.57` · 8 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 254.5 s | nightly · 26.11.0-trunk.57 → 26.11.0-trunk.62 |
| reboot | ✅ | 55.2 s | warm · up 36 s |
| kernel-switch | ✅ | 46.5 s | branch=edge · family=qrb2210 · installed=26.11.0-trunk.62 · boot_image=? · kernel_before=7.2.3-edge-qrb2210 |
| reboot | ✅ | 198.6 s | warm · 4/4 boots · up 35 s |
| hw-performance | ✅ | 24.6 s | AES 939 · mem 5100 · disk W 168 / R 223 MB/s · 38.4 °C · 2016 MHz |
| dvfs | ✅ | 32.1 s | schedutil · 300–2016 MHz (peak 2016) |
| network-iperf | ✅ | 46.1 s | wlan0 ↑24/↓21 (Wi-Fi 5) · usb0 ↑?/↓? Mbps |
| store-versions | ✅ | 7.0 s | 26.11.0-trunk.62 · 7.2.3-edge-qrb2210 |

### ✅ Banana Pi CM4IO 01

`bananapicm4io` · **inplace** · image `26.8.3` · 14 ✅ · 2 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 55.6 s | nightly · 26.8.3 → 26.8.3 |
| reboot | ✅ | 48.7 s | power-cycle · up 23 s |
| kernel-switch | ✅ | 40.5 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 136.5 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 17.6 s | AES 852 · mem 3900 · disk W 43 / R 151 MB/s · 52.5 °C · 2016 MHz |
| dvfs | ✅ | 18.1 s | ondemand · 1000–1512 MHz (peak 1512) |
| network-iperf | ❌ | 297.0 s | eth0 ↑940/↓941 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.0 s | 26.8.3 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 195.0 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 143.2 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 18.9 s | AES 852 · mem 3900 · disk W 38 / R 158 MB/s · 53.5 °C · 2016 MHz |
| dvfs | ✅ | 18.3 s | ondemand · 1000–1512 MHz (peak 1512) |
| network-iperf | ❌ | 283.5 s | eth0 ↑941/↓0 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.0 s | 26.8.3 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 194.4 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 52.9 s | power-cycle · up 22 s |

### ✅ Banana Pi M2Pro 01

`bananapim2pro` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 45.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 57.0 s | power-cycle · up 22 s |
| kernel-switch | ✅ | 31.4 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 138.4 s | power-cycle · 4/4 boots · up 21 s |
| hw-performance | ✅ | 19.3 s | AES 981 · mem 5300 · disk W 43 / R 150 MB/s · 49.2 °C · 2100 MHz |
| dvfs | ✅ | 19.3 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 30.6 s | end0 ↑940/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.4 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 94.0 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 138.7 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 19.4 s | AES 979 · mem 5300 · disk W 42 / R 157 MB/s · 50 °C · 2100 MHz |
| dvfs | ✅ | 19.9 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 33.2 s | end0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.6 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 93.0 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 55.3 s | power-cycle · up 23 s |

**Power** — min 1.50 W · avg 3.12 W · peak 4.80 W · 623 samples

```mermaid
xychart-beta
    title "Power — Banana Pi M2Pro 01"
    x-axis "sample" 1 --> 623
    y-axis "W" 1.0 --> 5.0
    line [3.11, 3.12, 3.15, 2.02, 3.36, 3.14, 3.24, 2.51, 3.31, 2.81, 3.01, 2.84, 2.42, 3.26, 3.19, 3.36, 3.17, 3.19, 3.62, 3.31, 3.25, 3.23, 3.14, 3.10, 3.04, 3.33, 3.29, 2.30, 3.53, 3.11, 3.62, 3.09, 3.19, 3.19, 3.83, 3.19, 3.35, 3.13, 2.46, 3.29]
```

### ✅ Banana Pi M5 01

`bananapim5` · **inplace** · image `26.11.0-trunk.56` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 316.6 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.58 |
| reboot | ✅ | 179.3 s | warm · up 154 s |
| kernel-switch | ✅ | 50.7 s | branch=current · family=meson64 · installed=26.11.0-trunk.58 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=6.18.53-current-meson64 |
| reboot | ✅ | 639.9 s | warm · 4/4 boots · up 149 s |
| hw-performance | ✅ | 38.7 s | AES 979 · mem 5300 · disk W 10 / R 15 MB/s · 53.2 °C · 2100 MHz |
| dvfs | ✅ | 20.9 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 60.1 s | end0 ↑940/↓941 (1GE) · wlx000f13960190 ↑1/↓5 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.58 · 6.18.53-current-meson64 |
| kernel-switch | ✅ | 168.5 s | branch=edge · family=meson64 · installed=26.11.0-trunk.58 · boot_image=/boot/vmlinuz-7.2.7-edge-meson64 · kernel_before=6.18.53-current-meson64 |
| reboot | ✅ | 763.3 s | warm · 4/4 boots · up 178 s |
| hw-performance | ✅ | 38.8 s | AES 969 · mem 5300 · disk W 10 / R 15 MB/s · 53.3 °C · 2100 MHz |
| dvfs | ✅ | 21.1 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 67.2 s | end0 ↑941/↓941 (1GE) · wlx000f13960190 ↑1/↓5 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.58 · 7.2.7-edge-meson64 |
| kernel-switch | ✅ | 166.5 s | branch=current · family=meson64 · installed=26.11.0-trunk.58 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=7.2.7-edge-meson64 |
| reboot | ✅ | 172.0 s | warm · up 148 s |

### ✅ Banana Pi M7 01

`bananapim7` · **inplace** · image `26.11.0-trunk.62` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 27.2 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 47.6 s | power-cycle · up 13 s |
| kernel-switch | ✅ | 18.5 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 99.6 s | power-cycle · 4/4 boots · up 16 s |
| hw-performance | ✅ | 13.3 s | AES 1262 · mem 13700 · disk W 921 / R 964 MB/s · 53.6 °C · 1800 MHz |
| dvfs | ✅ | 17.2 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ✅ | 29.2 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 47.8 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 668.8 s | power-cycle · 3/4 boots · up 98 s |
| hw-performance | ✅ | 13.4 s | AES 1256 · mem 10100 · disk W 956 / R 1607 MB/s · 60.1 °C · 1800 MHz |
| dvfs | ✅ | 15.2 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 29.9 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 40.2 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 435.2 s | power-cycle · 4/4 boots · up 96 s |
| hw-performance | ✅ | 14.1 s | AES 1256 · mem 8000 · disk W 958 / R 1598 MB/s · 62.8 °C · 1800 MHz |
| dvfs | ✅ | 14.1 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 28.9 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 38.0 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 42.2 s | power-cycle · up 15 s |

**Power** — min 4.00 W · avg 5.89 W · peak 12.80 W · 1297 samples

```mermaid
xychart-beta
    title "Power — Banana Pi M7 01"
    x-axis "sample" 1 --> 1297
    y-axis "W" 3.5 --> 13.0
    line [5.27, 5.75, 6.63, 6.06, 6.50, 6.15, 5.71, 6.38, 5.40, 5.41, 5.66, 5.41, 5.40, 5.40, 5.40, 5.75, 5.40, 5.40, 5.87, 5.40, 5.61, 5.98, 5.40, 6.73, 6.39, 6.94, 5.66, 5.49, 6.10, 6.02, 5.45, 6.61, 5.44, 5.41, 6.21, 5.41, 5.62, 6.85, 7.07, 6.75]
```

### ✅ Banana Pi R3 Mini 01

`bananapir3mini` · **inplace** · image `26.11.0-trunk` · 4 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 18.3 s | — |
| reboot | ✅ | 67.6 s | power-cycle · up 36 s |
| hw-performance | ✅ | 26.6 s | AES 935 · mem 3200 · disk W 77 / R 90 MB/s · 64.8 °C · None MHz |
| dvfs | ➖ | 2.2 s | no cpufreq |
| network-iperf | ✅ | 110.0 s | eth0 ↑939/↓918 (1GE) · eth1 ↑938/↓919 (1GE) · wlan0 ↑20/↓22 (Wi-Fi 6) · wlan1 ↑469/↓378 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk · 6.18.52-current-filogic-mt7986 |

**Power** — min 3.10 W · avg 6.20 W · peak 11.20 W · 190 samples

```mermaid
xychart-beta
    title "Power — Banana Pi R3 Mini 01"
    x-axis "sample" 1 --> 190
    y-axis "W" 3.0 --> 11.5
    line [5.90, 5.96, 6.24, 6.40, 6.40, 5.90, 5.90, 6.50, 3.10, 3.50, 3.40, 3.90, 4.12, 5.34, 6.34, 6.38, 6.30, 6.34, 6.24, 6.12, 6.30, 6.28, 6.18, 6.12, 6.20, 6.20, 6.10, 6.10, 6.20, 6.20, 6.32, 7.18, 7.00, 6.26, 6.24, 8.14, 10.98, 10.34, 6.88, 6.62]
```

### ✅ BananaPi BPI-F3 01

`musepipro` · **inplace** · image `26.8.3` · 6 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 381.7 s | nightly · 26.8.3 → 26.11.0-trunk.62 |
| reboot | ✅ | 56.0 s | power-cycle · up 20 s |
| hw-performance | ✅ | 24.8 s | AES 27 · mem 3000 · disk W 71 / R 82 MB/s · 45 °C · 1600 MHz |
| dvfs | ✅ | 23.9 s | performance · 614–1600 MHz (peak 1600) |
| network-iperf | ✅ | 89.9 s | eth0 ↑941/↓941 (1GE) · wlan0 ↑128/↓298 (Wi-Fi 6) · wlan1 ↑256/↓219 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.4 s | 26.11.0-trunk.62 · 6.18.54-current-spacemit |

**Power** — min 2.30 W · avg 5.21 W · peak 8.60 W · 471 samples

```mermaid
xychart-beta
    title "Power — BananaPi BPI-F3 01"
    x-axis "sample" 1 --> 471
    y-axis "W" 2.0 --> 9.0
    line [4.60, 5.14, 5.11, 4.99, 4.97, 5.04, 5.02, 5.03, 5.07, 5.00, 5.20, 5.33, 5.08, 5.18, 5.07, 5.10, 5.13, 7.07, 5.13, 5.05, 5.42, 5.30, 5.05, 5.17, 5.06, 4.97, 4.88, 4.74, 3.94, 5.27, 5.38, 4.97, 7.03, 5.20, 5.14, 5.53, 5.57, 5.51, 5.70, 5.43]
```

### ✅ Clearfog Pro 01

`clearfogpro` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 73.5 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 39.6 s | warm · up 21 s |
| kernel-switch | ✅ | 40.9 s | branch=current · family=mvebu · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu · kernel_before=6.18.54-current-mvebu |
| reboot | ✅ | 137.6 s | warm · 4/4 boots · up 21 s |
| hw-performance | ✅ | 41.4 s | AES 43 · mem 3800 · disk W 20 / R 23 MB/s · 62.7 °C · None MHz |
| dvfs | ➖ | 2.9 s | no cpufreq |
| network-iperf | ✅ | 34.6 s | lan2 ↑936/↓936 Mbps |
| store-versions | ✅ | 6.0 s | 26.11.0-trunk.62 · 6.18.54-current-mvebu |
| kernel-switch | ✅ | 104.8 s | branch=edge · family=mvebu · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-mvebu · kernel_before=6.18.54-current-mvebu |
| reboot | ✅ | 136.6 s | warm · 4/4 boots · up 19 s |
| hw-performance | ✅ | 42.4 s | AES 43 · mem 3800 · disk W 20 / R 22 MB/s · 63.7 °C · None MHz |
| dvfs | ➖ | 2.9 s | no cpufreq |
| network-iperf | ✅ | 42.8 s | lan2 ↑935/↓936 Mbps |
| store-versions | ✅ | 6.0 s | 26.11.0-trunk.62 · 7.2.8-edge-mvebu |
| kernel-switch | ✅ | 107.2 s | branch=current · family=mvebu · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu · kernel_before=7.2.8-edge-mvebu |
| reboot | ✅ | 40.5 s | warm · up 20 s |

### ✅ Cubie A5E 01

`radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.61` · 12 ✅ · 2 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 86.5 s | nightly · 26.11.0-trunk.61 → 26.11.0-trunk.61 |
| reboot | ✅ | 63.4 s | power-cycle · up 29 s |
| kernel-switch | ✅ | 63.9 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.61 · boot_image=? · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 176.9 s | power-cycle · 4/4 boots · up 31 s |
| hw-performance | ✅ | 41.4 s | AES 358 · mem 2000 · disk W 20 / R 23 MB/s · 62.2 °C · None MHz |
| dvfs | ➖ | 2.7 s | no cpufreq |
| network-iperf | ❌ | 88.8 s | end0 ↑825/↓941 (1GE) · end1 ↑941/↓940 (1GE) · wlan0 ↑123/↓0 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 5.9 s | 26.11.0-trunk.61 · 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 570.4 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.61 · boot_image=? · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 189.9 s | power-cycle · 4/4 boots · up 32 s |
| hw-performance | ✅ | 41.6 s | AES 358 · mem 2000 · disk W 21 / R 23 MB/s · 66.5 °C · None MHz |
| dvfs | ➖ | 2.8 s | no cpufreq |
| network-iperf | ❌ | 89.8 s | end0 ↑828/↓941 (1GE) · end1 ↑941/↓940 (1GE) · wlan0 ↑123/↓0 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 5.9 s | 26.11.0-trunk.61 · 7.2.8-edge-sunxi64 |
| kernel-switch | ✅ | 558.2 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.61 · boot_image=? · kernel_before=7.2.8-edge-sunxi64 |
| reboot | ✅ | 79.1 s | power-cycle · up 31 s |

**Power** — min 1.80 W · avg 3.87 W · peak 5.80 W · 1682 samples

```mermaid
xychart-beta
    title "Power — Cubie A5E 01"
    x-axis "sample" 1 --> 1682
    y-axis "W" 1.5 --> 6.0
    line [3.59, 3.54, 3.13, 3.55, 3.37, 3.20, 2.93, 3.67, 3.50, 3.56, 3.54, 3.60, 3.51, 4.07, 3.71, 5.00, 4.17, 3.93, 5.17, 3.83, 3.58, 3.37, 3.77, 3.57, 3.30, 3.72, 3.87, 3.81, 3.86, 3.77, 3.94, 4.28, 4.84, 5.17, 3.94, 5.52, 4.89, 3.90, 3.78, 3.37]
```

### ✅ Cubietruck 01

`cubietruck` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 138.5 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 67.6 s | warm · up 43 s |
| kernel-switch | ✅ | 91.9 s | branch=current · family=sunxi · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 243.3 s | warm · 4/4 boots · up 42 s |
| hw-performance | ✅ | 59.3 s | AES 18 · mem 1700 · disk W 14 / R 22 MB/s · 48.3 °C · 960 MHz |
| dvfs | ✅ | 56.5 s | ondemand · 528–960 MHz (peak 960) |
| network-iperf | ✅ | 100.3 s | end0 ↑714/↓852 (1GE) · wlan0 ↑21/↓23 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 11.9 s | 26.11.0-trunk.62 · 6.18.54-current-sunxi |
| kernel-switch | ✅ | 233.3 s | branch=edge · family=sunxi · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 239.8 s | warm · 4/4 boots · up 41 s |
| hw-performance | ✅ | 57.9 s | AES 19 · mem 1700 · disk W 15 / R 22 MB/s · 49 °C · 960 MHz |
| dvfs | ✅ | 57.3 s | ondemand · 528–960 MHz (peak 960) |
| network-iperf | ✅ | 108.8 s | end0 ↑771/↓891 (1GE) · wlan0 ↑20/↓27 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 11.5 s | 26.11.0-trunk.62 · 7.2.8-edge-sunxi |
| kernel-switch | ✅ | 227.4 s | branch=current · family=sunxi · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=7.2.8-edge-sunxi |
| reboot | ✅ | 67.9 s | warm · up 43 s |

### ✅ Cubox i2eX/i4 01

`cubox-i` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 108.0 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 80.8 s | power-cycle · up 42 s |
| kernel-switch | ✅ | 72.0 s | branch=current · family=imx6 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-imx6 · kernel_before=6.18.54-current-imx6 |
| reboot | ✅ | 243.2 s | power-cycle · 4/4 boots · up 45 s |
| hw-performance | ✅ | 46.9 s | AES 26 · mem 740 · disk W 19 / R 20 MB/s · 51.4 °C · 996 MHz |
| dvfs | ✅ | 40.5 s | ondemand · 396–996 MHz (peak 996) |
| network-iperf | ✅ | 92.8 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑19/↓15 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 9.5 s | 26.11.0-trunk.62 · 6.18.54-current-imx6 |
| kernel-switch | ✅ | 266.1 s | branch=edge · family=imx6 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.1.13-edge-imx6 · kernel_before=6.18.54-current-imx6 |
| reboot | ✅ | 252.5 s | power-cycle · 4/4 boots · up 46 s |
| hw-performance | ✅ | 47.8 s | AES 26 · mem 745 · disk W 19 / R 20 MB/s · 52.6 °C · 996 MHz |
| dvfs | ✅ | 44.3 s | ondemand · 396–996 MHz (peak 996) |
| network-iperf | ✅ | 82.7 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑19/↓14 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 8.8 s | 26.11.0-trunk.62 · 7.1.13-edge-imx6 |
| kernel-switch | ✅ | 265.2 s | branch=current · family=imx6 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-imx6 · kernel_before=7.1.13-edge-imx6 |
| reboot | ✅ | 78.3 s | power-cycle · up 42 s |

**Power** — min 1.90 W · avg 3.39 W · peak 5.80 W · 1385 samples

```mermaid
xychart-beta
    title "Power — Cubox i2eX/i4 01"
    x-axis "sample" 1 --> 1385
    y-axis "W" 1.5 --> 6.0
    line [3.35, 3.62, 2.97, 3.57, 3.58, 3.47, 3.40, 3.29, 3.89, 3.95, 3.23, 3.33, 3.33, 3.16, 3.00, 3.09, 3.66, 3.89, 3.48, 3.25, 3.25, 3.46, 3.30, 3.01, 3.97, 3.83, 2.96, 3.29, 3.34, 3.07, 3.37, 3.36, 3.51, 3.58, 3.44, 3.44, 3.11, 3.46, 2.87, 3.56]
```

### ✅ Espressobin 01

`espressobin` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 165.1 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 80.7 s | power-cycle · up 46 s |
| kernel-switch | ✅ | 88.6 s | branch=current · family=mvebu64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu64 · kernel_before=6.18.54-current-mvebu64 |
| reboot | ✅ | 237.8 s | power-cycle · 4/4 boots · up 46 s |
| hw-performance | ✅ | 33.2 s | AES 371 · mem 2000 · disk W 43 / R 130 MB/s · None °C · 800 MHz |
| dvfs | ✅ | 34.6 s | ondemand · 200–800 MHz (peak 800) |
| network-iperf | ✅ | 38.8 s | lan0 ↑936/↓755 (1GE) Mbps |
| store-versions | ✅ | 7.4 s | 26.11.0-trunk.62 · 6.18.54-current-mvebu64 |
| kernel-switch | ✅ | 349.0 s | branch=edge · family=mvebu64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.1.13-edge-mvebu64 · kernel_before=6.18.54-current-mvebu64 |
| reboot | ✅ | 234.3 s | power-cycle · 4/4 boots · up 45 s |
| hw-performance | ✅ | 33.1 s | AES 370 · mem 2000 · disk W 29 / R 139 MB/s · None °C · 800 MHz |
| dvfs | ✅ | 35.2 s | ondemand · 200–800 MHz (peak 800) |
| network-iperf | ✅ | 39.0 s | lan0 ↑936/↓762 (1GE) · end0 ↑?/↓? Mbps |
| store-versions | ✅ | 7.5 s | 26.11.0-trunk.62 · 7.1.13-edge-mvebu64 |
| kernel-switch | ✅ | 387.4 s | branch=current · family=mvebu64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu64 · kernel_before=7.1.13-edge-mvebu64 |
| reboot | ✅ | 74.4 s | power-cycle · up 45 s |

### ✅ Helios4 01

`helios4` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 52.3 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 127.3 s | warm · up 103 s |
| kernel-switch | ✅ | 35.1 s | branch=current · family=mvebu · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu · kernel_before=6.18.54-current-mvebu |
| reboot | ✅ | 469.9 s | warm · 4/4 boots · up 102 s |
| hw-performance | ✅ | 44.5 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 53.7 °C · None MHz |
| dvfs | ➖ | 2.4 s | no cpufreq |
| network-iperf | ✅ | 31.3 s | end1 ↑939/↓939 (1GE) Mbps |
| store-versions | ✅ | 12.6 s | 26.11.0-trunk.62 · 6.18.54-current-mvebu |
| kernel-switch | ✅ | 95.9 s | branch=edge · family=mvebu · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-mvebu · kernel_before=6.18.54-current-mvebu |
| reboot | ✅ | 463.7 s | warm · 4/4 boots · up 103 s |
| hw-performance | ✅ | 36.8 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 54.6 °C · None MHz |
| dvfs | ➖ | 2.4 s | no cpufreq |
| network-iperf | ✅ | 31.6 s | end1 ↑939/↓939 (1GE) Mbps |
| store-versions | ✅ | 5.1 s | 26.11.0-trunk.62 · 7.2.8-edge-mvebu |
| kernel-switch | ✅ | 99.4 s | branch=current · family=mvebu · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-mvebu · kernel_before=7.2.8-edge-mvebu |
| reboot | ✅ | 121.2 s | warm · up 104 s |

### ✅ Khadas Edge2 01

`khadas-edge2` · **inplace** · image `26.8.3` · 14 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 112.6 s | nightly · 26.8.3 → 26.11.0-trunk.62 |
| reboot | ✅ | 30.0 s | warm · up 12 s |
| kernel-switch | ✅ | 21.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 95.6 s | warm · 4/4 boots · up 16 s |
| hw-performance | ✅ | 15.4 s | AES 1274 · mem 14000 · disk W 105 / R 261 MB/s · 35.2 °C · 1800 MHz |
| dvfs | ✅ | 17.8 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ⏭️ | 6.7 s | no cabled interfaces |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 67.4 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 82.0 s | warm · 4/4 boots · up 8 s |
| hw-performance | ✅ | 15.5 s | AES 1276 · mem 10000 · disk W 104 / R 210 MB/s · 37.9 °C · 1800 MHz |
| dvfs | ✅ | 16.3 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ⏭️ | 6.5 s | no cabled interfaces |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 53.6 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 27.7 s | warm · up 9 s |

### ✅ Khadas VIM1 01

`khadas-vim1` · **inplace** · image `26.8.0-trunk.236` · 7 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 182.5 s | nightly · 26.8.0-trunk.236 → 26.8.0-trunk.236 |
| reboot | ✅ | 32.7 s | warm · up 18 s |
| hw-performance | ✅ | 22.5 s | AES 658 · mem 3500 · disk W 43 / R 151 MB/s · 55 °C · 1512 MHz |
| dvfs | ✅ | 19.2 s | ondemand · 500–1512 MHz (peak 1512) |
| network-iperf | ❌ | 371.3 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑0/↓39 (Wi-Fi 5) Mbps |
| restore-stable | ✅ | 163.1 s | stable |
| reboot | ✅ | 33.1 s | warm · up 18 s |
| store-versions | ✅ | 5.3 s | 26.8.0-trunk.236 · 6.18.34-current-meson64 |

### ✅ Khadas VIM2 01

`khadas-vim2` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 96.1 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 39.6 s | warm · up 22 s |
| kernel-switch | ✅ | 52.8 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 150.6 s | warm · 4/4 boots · up 25 s |
| hw-performance | ✅ | 24.3 s | AES 659 · mem 3600 · disk W 42 / R 143 MB/s · 51 °C · 1512 MHz |
| dvfs | ✅ | 25.4 s | ondemand · 500–1512 MHz (peak 1512) |
| network-iperf | ✅ | 64.2 s | eth0 ↑940/↓941 (1GE) · wlan0 ↑104/↓90 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.6 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 157.8 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 150.9 s | warm · 4/4 boots · up 25 s |
| hw-performance | ✅ | 25.4 s | AES 658 · mem 3600 · disk W 42 / R 151 MB/s · 52 °C · 1512 MHz |
| dvfs | ✅ | 26.2 s | ondemand · 500–1512 MHz (peak 1512) |
| network-iperf | ✅ | 70.4 s | eth0 ↑940/↓941 (1GE) · wlan0 ↑88/↓82 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.6 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 157.4 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 37.6 s | warm · up 20 s |

### ✅ Khadas VIM3 01

`khadas-vim3` · **inplace** · image `26.11.0-trunk.61` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 34.6 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 32.2 s | warm · up 17 s |
| kernel-switch | ✅ | 22.8 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 114.0 s | warm · 4/4 boots · up 17 s |
| hw-performance | ✅ | 16.4 s | AES 852 · mem 3900 · disk W 63 / R 160 MB/s · 55.9 °C · 2016 MHz |
| dvfs | ✅ | 17.6 s | ondemand · 1000–1512 MHz (peak 1512) |
| network-iperf | ✅ | 56.0 s | end0 ↑940/↓941 (1GE) · wlan0 ↑44/↓40 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 69.5 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 113.2 s | warm · 4/4 boots · up 15 s |
| hw-performance | ✅ | 16.6 s | AES 852 · mem 3800 · disk W 66 / R 150 MB/s · 57.7 °C · 2016 MHz |
| dvfs | ✅ | 17.6 s | ondemand · 1000–1512 MHz (peak 1512) |
| network-iperf | ✅ | 58.7 s | end0 ↑941/↓941 (1GE) · wlan0 ↑42/↓40 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.0 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 68.5 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 32.3 s | warm · up 16 s |

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

`mekotronics-r58hd` · **inplace** · image `26.11.0-trunk.62` · 5 ✅ · 1 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 23.8 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 46.1 s | power-cycle · up 15 s |
| hw-performance | ✅ | 13.6 s | AES 1297 · mem 9200 · disk W 248 / R 289 MB/s · 44.4 °C · 1800 MHz |
| dvfs | ✅ | 16.0 s | ondemand · 1200–1800 MHz (peak 2304) |
| network-iperf | ❌ | 741.0 s | end0 ↑495/↓0 (1GE) · enP3p49s0 ↑0/↓939 (1GE) Mbps |
| store-versions | ✅ | 100.2 s | 6.1.172-vendor-rk35xx |

**Power** — min 3.50 W · avg 5.22 W · peak 12.10 W · 774 samples

```mermaid
xychart-beta
    title "Power — Mekotronics R58HD 01"
    x-axis "sample" 1 --> 774
    y-axis "W" 3.0 --> 12.5
    line [5.11, 5.99, 4.71, 6.51, 7.38, 5.33, 5.13, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.10, 5.13, 5.10, 5.10, 5.43, 5.10, 5.10, 5.10, 5.13]
```

### ✅ Mekotronics R58S2 01

`mekotronics-r58s2` · **inplace** · image `26.8.2` · 5 ✅ · 0 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 184.9 s | — |
| reboot | ✅ | 45.1 s | power-cycle · up 15 s |
| hw-performance | ✅ | 14.8 s | AES 1272 · mem 15000 · disk W 223 / R 274 MB/s · 45.3 °C · 1800 MHz |
| dvfs | ✅ | 18.0 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ✅ | 56.8 s | end1 ↑909/↓914 (1GE) · wlan0 ↑55/↓126 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.1 s | 26.8.3 · 6.1.172-vendor-rk35xx |

### ✅ NanoPi Fire3 01

`nanopifire3` · **inplace** · image `26.11.0-trunk.58` · 7 ✅ · 0 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 434.0 s | nightly · 26.11.0-trunk.58 → 26.11.0-trunk.62 |
| reboot | ✅ | 57.1 s | power-cycle · up 17 s |
| kernel-switch | ✅ | 70.3 s | branch=edge · family=s5p6818 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-s5p6818 · kernel_before=7.2.8-edge-s5p6818 |
| reboot | ✅ | 178.0 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 43.1 s | AES 372 · mem 2000 · disk W 1 / R 22 MB/s · 65 °C · None MHz |
| dvfs | ➖ | 3.0 s | no cpufreq |
| network-iperf | ✅ | 39.4 s | eth0 ↑938/↓939 (1GE) Mbps |
| store-versions | ✅ | 6.1 s | 26.11.0-trunk.62 · 7.2.8-edge-s5p6818 |

### ✅ NanoPi K2 01

`nanopik2-s905` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 55.6 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 45.5 s | warm · up 29 s |
| kernel-switch | ✅ | 40.6 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 126.5 s | warm · 4/4 boots · up 19 s |
| hw-performance | ✅ | 31.2 s | AES 51 · mem 3700 · disk W 10 / R 41 MB/s · 58 °C · 2016 MHz |
| dvfs | ✅ | 21.3 s | ondemand · 500–1536 MHz (peak 1536) |
| network-iperf | ✅ | 83.2 s | end0 ↑936/↓941 (1GE) · wlan0 ↑14/↓27 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 161.6 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 136.0 s | warm · 4/4 boots · up 24 s |
| hw-performance | ✅ | 31.3 s | AES 51 · mem 3800 · disk W 9 / R 42 MB/s · 60 °C · 2016 MHz |
| dvfs | ✅ | 21.9 s | ondemand · 500–1536 MHz (peak 1536) |
| network-iperf | ✅ | 58.8 s | end0 ↑935/↓941 (1GE) · wlan0 ↑15/↓29 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 155.9 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 36.0 s | warm · up 19 s |

### ✅ NanoPi M5 01

`nanopi-m5` · **inplace** · image `26.11.0-trunk.56` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 39.8 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.56 |
| reboot | ✅ | 48.1 s | power-cycle · up 23 s |
| kernel-switch | ✅ | 22.9 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 137.9 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 18.1 s | AES 1275 · mem 8000 · disk W 68 / R 77 MB/s · 43.5 °C · 2016 MHz |
| dvfs | ✅ | 19.1 s | ondemand · 2016–2016 MHz (peak 2208) |
| network-iperf | ✅ | 106.1 s | end0 ↑939/↓939 (1GE) · end1 ↑939/↓939 (1GE) · wlan0 ↑44/↓87 (Wi-Fi 5) · wlx44334c47dec3 ↑39/↓22 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.3 s | 26.11.0-trunk.56 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 100.2 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 152.5 s | power-cycle · 4/4 boots · up 29 s |
| hw-performance | ✅ | 26.4 s | AES 1326 · mem 9000 · disk W 20 / R 21 MB/s · 42.5 °C · 2016 MHz |
| dvfs | ✅ | 16.9 s | ondemand · 408–2016 MHz (peak 2208) |
| network-iperf | ✅ | 105.2 s | end0 ↑930/↓935 (1GE) · end1 ↑938/↓880 (1GE) · wlan0 ↑71/↓196 (Wi-Fi 5) · wlx44334c47dec3 ↑39/↓20 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.56 · 6.18.53-current-rockchip64 |
| kernel-switch | ✅ | 98.2 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-rockchip64 · kernel_before=6.18.53-current-rockchip64 |
| reboot | ✅ | 156.3 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 26.5 s | AES 1333 · mem 9000 · disk W 20 / R 21 MB/s · 43.5 °C · 2016 MHz |
| dvfs | ✅ | 18.1 s | ondemand · 408–2016 MHz (peak 2208) |
| network-iperf | ✅ | 107.3 s | end0 ↑927/↓936 (1GE) · end1 ↑922/↓883 (1GE) · wlan0 ↑113/↓108 (Wi-Fi 5) · wlx44334c47dec3 ↑40/↓12 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.6 s | 26.11.0-trunk.56 · 7.2.7-edge-rockchip64 |
| kernel-switch | ✅ | 103.6 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.7-edge-rockchip64 |
| reboot | ✅ | 131.8 s | power-cycle · up 108 s |

**Power** — min 0.70 W · avg 4.86 W · peak 9.30 W · 1176 samples

```mermaid
xychart-beta
    title "Power — NanoPi M5 01"
    x-axis "sample" 1 --> 1176
    y-axis "W" 0.5 --> 9.5
    line [5.62, 4.30, 4.97, 4.06, 4.59, 4.20, 4.12, 6.17, 5.20, 5.23, 5.10, 5.58, 5.45, 5.25, 3.84, 3.92, 4.32, 4.22, 6.09, 5.43, 5.39, 5.20, 5.57, 5.28, 5.87, 4.02, 3.98, 4.27, 2.68, 5.25, 6.19, 5.31, 5.33, 5.17, 5.29, 5.37, 5.07, 3.77, 3.92, 3.92]
```

### ✅ NanoPi M6 01

`nanopi-m6` · **inplace** · image `26.11.0-trunk.62` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 27.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 53.1 s | power-cycle · up 20 s |
| kernel-switch | ✅ | 20.1 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 135.4 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 17.8 s | AES 1259 · mem 13800 · disk W 52 / R 77 MB/s · 44.4 °C · 1800 MHz |
| dvfs | ✅ | 17.3 s | ondemand · 1800–1800 MHz (peak 2256) |
| network-iperf | ✅ | 55.5 s | lan ↑939/↓939 (1GE) · wlP3p49s0 ↑240/↓243 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 94.2 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 127.5 s | power-cycle · 4/4 boots · up 21 s |
| hw-performance | ✅ | 18.5 s | AES 1205 · mem 9600 · disk W 49 / R 57 MB/s · 47.2 °C · 1800 MHz |
| dvfs | ✅ | 16.2 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 55.2 s | lan ↑939/↓937 (1GE) · wlP3p49s0 ↑257/↓289 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 72.2 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 134.6 s | power-cycle · 4/4 boots · up 21 s |
| hw-performance | ✅ | 19.1 s | AES 1215 · mem 7800 · disk W 47 / R 56 MB/s · 48.1 °C · 1800 MHz |
| dvfs | ✅ | 14.9 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 59.4 s | lan ↑938/↓936 (1GE) · wlP3p49s0 ↑181/↓124 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 70.9 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 49.9 s | power-cycle · up 23 s |

**Power** — min 0.90 W · avg 4.01 W · peak 10.70 W · 835 samples

```mermaid
xychart-beta
    title "Power — NanoPi M6 01"
    x-axis "sample" 1 --> 835
    y-axis "W" 0.5 --> 11.0
    line [3.64, 3.25, 2.80, 3.87, 2.69, 3.14, 3.64, 3.50, 3.47, 6.04, 3.24, 3.91, 3.45, 4.45, 3.54, 3.41, 2.42, 3.01, 4.02, 4.06, 4.39, 7.32, 4.57, 4.74, 4.87, 4.52, 5.11, 3.20, 3.54, 3.62, 3.21, 3.69, 4.80, 5.10, 4.87, 4.64, 4.54, 4.64, 4.24, 3.35]
```

### ✅ NanoPi Neo 2 Black 01

`nanopineo2black` · **inplace** · image `26.11.0-trunk.56` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 80.5 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.56 |
| reboot | ✅ | 46.2 s | power-cycle · up 20 s |
| kernel-switch | ✅ | 45.5 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-sunxi64 · kernel_before=6.18.53-current-sunxi64 |
| reboot | ✅ | 364.1 s | power-cycle · 3/4 boots · up 22 s |
| hw-performance | ✅ | 30.6 s | AES 638 · mem 3500 · disk W 19 / R 0 MB/s · 63.5 °C · 1368 MHz |
| dvfs | ✅ | 23.4 s | ondemand · 480–1368 MHz (peak 1368) |
| network-iperf | ✅ | 34.7 s | end0 ↑847/↓879 (1GE) Mbps |
| store-versions | ✅ | 5.0 s | 26.11.0-trunk.56 · 6.18.53-current-sunxi64 |
| kernel-switch | ✅ | 122.3 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-sunxi64 · kernel_before=6.18.53-current-sunxi64 |
| reboot | ✅ | 354.4 s | power-cycle · 3/4 boots · up 21 s |
| hw-performance | ✅ | 31.0 s | AES 637 · mem 3500 · disk W 18 / R 0 MB/s · 64.2 °C · 1368 MHz |
| dvfs | ✅ | 24.0 s | ondemand · 480–1368 MHz (peak 1368) |
| network-iperf | ✅ | 34.9 s | end0 ↑874/↓903 (1GE) Mbps |
| store-versions | ✅ | 5.3 s | 26.11.0-trunk.56 · 7.2.7-edge-sunxi64 |
| kernel-switch | ✅ | 124.2 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-sunxi64 · kernel_before=7.2.7-edge-sunxi64 |
| reboot | ✅ | 49.1 s | power-cycle · up 21 s |

### ✅ NanoPi Neo 3 01

`nanopineo3` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 87.2 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 53.8 s | power-cycle · up 25 s |
| kernel-switch | ✅ | 58.1 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 167.3 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 28.5 s | AES 599 · mem 2400 · disk W 1 / R 63 MB/s · 76.5 °C · 1296 MHz |
| dvfs | ✅ | 29.9 s | ondemand · 408–1296 MHz (peak 1296) |
| network-iperf | ✅ | 101.6 s | end0 ↑920/↓940 (1GE) · wlx7cdd905518f9 ↑38/↓38 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 6.8 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 174.8 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 162.3 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 28.8 s | AES 598 · mem 2300 · disk W 52 / R 63 MB/s · 80 °C · 1296 MHz |
| dvfs | ✅ | 30.9 s | ondemand · 408–1296 MHz (peak 1296) |
| network-iperf | ✅ | 68.3 s | end0 ↑899/↓941 (1GE) · wlx7cdd905518f9 ↑36/↓32 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 6.6 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 172.5 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 57.2 s | power-cycle · up 28 s |

### ✅ NanoPi R6S 01

`nanopi-r6s` · **inplace** · image `26.11.0-trunk.62` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 26.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 40.0 s | power-cycle · up 15 s |
| kernel-switch | ✅ | 17.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 94.8 s | power-cycle · 4/4 boots · up 11 s |
| hw-performance | ✅ | 14.7 s | AES 1281 · mem 14000 · disk W 208 / R 274 MB/s · 35.2 °C · 1800 MHz |
| dvfs | ✅ | 17.3 s | ondemand · 1800–1800 MHz (peak 2352) |
| network-iperf | ✅ | 29.2 s | lan2 ↑939/↓939 (1GE) Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 48.9 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 98.8 s | power-cycle · 4/4 boots · up 16 s |
| hw-performance | ✅ | 15.5 s | AES 1279 · mem 10100 · disk W 147 / R 148 MB/s · 37 °C · 1800 MHz |
| dvfs | ✅ | 16.0 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 55.9 s | lan2 ↑939/↓938 (1GE) Mbps |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 44.0 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 105.6 s | power-cycle · 4/4 boots · up 16 s |
| hw-performance | ✅ | 15.7 s | AES 1273 · mem 8200 · disk W 144 / R 149 MB/s · 37.9 °C · 1800 MHz |
| dvfs | ✅ | 14.7 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 31.0 s | lan2 ↑938/↓939 (1GE) Mbps |
| store-versions | ✅ | 4.0 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 39.6 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 45.2 s | power-cycle · up 21 s |

**Power** — min 1.00 W · avg 4.70 W · peak 10.30 W · 612 samples

```mermaid
xychart-beta
    title "Power — NanoPi R6S 01"
    x-axis "sample" 1 --> 612
    y-axis "W" 0.5 --> 10.5
    line [3.85, 4.60, 3.24, 4.58, 4.74, 4.11, 4.56, 4.20, 2.79, 4.24, 7.62, 3.72, 3.84, 5.04, 4.91, 4.08, 4.08, 4.00, 4.55, 4.53, 4.93, 8.37, 4.46, 4.46, 4.70, 4.90, 5.57, 5.23, 5.30, 4.53, 5.30, 2.85, 4.79, 6.61, 4.93, 4.70, 4.95, 5.59, 4.09, 4.45]
```

### ✅ NanoPi R76S 01

`nanopi-r76s` · **inplace** · image `26.11.0-trunk.57` · 15 ✅ · 0 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 14.7 s | — |
| reboot | ✅ | 70.5 s | power-cycle · up 28 s |
| kernel-switch | ✅ | 30.1 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 178.1 s | power-cycle · 4/4 boots · up 31 s |
| hw-performance | ✅ | 22.3 s | AES 1276 · mem 7400 · disk W 66 / R 76 MB/s · 39.8 °C · 2016 MHz |
| dvfs | ✅ | 21.1 s | ondemand · 2016–2016 MHz (peak 2208) |
| network-iperf | ✅ | 131.7 s | end0 ↑844/↓862 (1GE) · end1 ↑906/↓932 (1GE) · wlan0 ↑34/↓86 (Wi-Fi 5) · wlxe0e1a933de37 ↑140/↓154 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.57 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 154.2 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 194.9 s | power-cycle · 4/4 boots · up 29 s |
| hw-performance | ✅ | 23.0 s | AES 1304 · mem 8800 · disk W 18 / R 69 MB/s · 40.7 °C · 2016 MHz |
| dvfs | ✅ | 19.3 s | ondemand · 408–2016 MHz (peak 2208) |
| network-iperf | ✅ | 115.5 s | end0 ↑939/↓939 (1GE) · end1 ↑939/↓893 (1GE) · wlan0 ↑92/↓80 (Wi-Fi 5) · wlxe0e1a933de37 ↑171/↓217 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.57 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 90.2 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 71.2 s | power-cycle · up 28 s |

**Power** — min 1.60 W · avg 3.80 W · peak 8.40 W · 897 samples

```mermaid
xychart-beta
    title "Power — NanoPi R76S 01"
    x-axis "sample" 1 --> 897
    y-axis "W" 1.5 --> 8.5
    line [3.74, 3.01, 2.40, 4.65, 2.80, 3.19, 3.08, 2.61, 3.60, 2.47, 4.47, 5.40, 3.90, 4.05, 4.27, 4.38, 4.33, 4.31, 4.26, 4.05, 3.70, 3.99, 3.52, 3.04, 2.36, 3.37, 2.25, 3.47, 3.32, 4.56, 5.01, 4.15, 4.39, 4.64, 4.67, 4.55, 4.63, 4.84, 3.53, 3.06]
```

### ✅ Odroid C2 01

`odroidc2` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 55.0 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 33.4 s | warm · up 16 s |
| kernel-switch | ✅ | 37.5 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 116.9 s | warm · 4/4 boots · up 17 s |
| hw-performance | ✅ | 22.5 s | AES 51 · mem 3500 · disk W 32 / R 142 MB/s · 43 °C · 1536 MHz |
| dvfs | ✅ | 22.1 s | ondemand · 500–1536 MHz (peak 1536) |
| network-iperf | ✅ | 34.2 s | end0 ↑939/↓941 (1GE) Mbps |
| store-versions | ✅ | 5.1 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 114.8 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 117.8 s | warm · 4/4 boots · up 17 s |
| hw-performance | ✅ | 22.4 s | AES 50 · mem 3400 · disk W 33 / R 152 MB/s · 44 °C · 1536 MHz |
| dvfs | ✅ | 22.6 s | ondemand · 500–1536 MHz (peak 1536) |
| network-iperf | ✅ | 34.2 s | end0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 113.6 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 34.2 s | warm · up 17 s |

### ✅ Odroid C4 01

`odroidc4` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 42.7 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 49.5 s | power-cycle · up 17 s |
| kernel-switch | ✅ | 30.0 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 136.6 s | power-cycle · 4/4 boots · up 24 s |
| hw-performance | ✅ | 21.5 s | AES 980 · mem 5200 · disk W 31 / R 79 MB/s · 39.4 °C · 2100 MHz |
| dvfs | ✅ | 20.7 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 70.8 s | end0 ↑863/↓923 (1GE) · wlx24050fdd332b ↑111/↓124 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.4 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 108.2 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 593.0 s | power-cycle · 2/4 boots · up 18 s |
| hw-performance | ✅ | 21.8 s | AES 980 · mem 5300 · disk W 30 / R 80 MB/s · 34.5 °C · 2100 MHz |
| dvfs | ✅ | 19.2 s | ondemand · 1000–2100 MHz (peak 2100) |
| network-iperf | ✅ | 56.3 s | end0 ↑939/↓939 (1GE) · wlx24050fdd332b ↑120/↓126 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 107.1 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 55.1 s | power-cycle · up 21 s |

**Power** — min 0.90 W · avg 2.90 W · peak 5.10 W · 1055 samples

```mermaid
xychart-beta
    title "Power — Odroid C4 01"
    x-axis "sample" 1 --> 1055
    y-axis "W" 0.5 --> 5.5
    line [3.34, 3.28, 2.80, 3.73, 3.27, 3.39, 3.38, 3.09, 3.54, 3.39, 3.85, 3.69, 3.84, 3.57, 3.48, 3.13, 1.97, 1.97, 1.99, 1.99, 2.00, 2.00, 1.80, 2.77, 1.92, 1.92, 1.96, 1.94, 1.94, 1.92, 2.25, 2.54, 3.57, 3.63, 4.17, 3.68, 3.80, 3.54, 3.43, 2.34]
```

### ✅ Odroid M1 01

`odroidm1` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 48.3 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 58.0 s | power-cycle · up 23 s |
| kernel-switch | ✅ | 31.6 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 146.9 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 17.0 s | AES 917 · mem 5100 · disk W 1038 / R 1014 MB/s · 34.4 °C · 1992 MHz |
| dvfs | ✅ | 21.6 s | ondemand · 408–1992 MHz (peak 1992) |
| network-iperf | ✅ | 77.9 s | eth0 ↑582/↓941 (1GE) · wlx40a5eff39254 ↑197/↓177 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.9 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 86.2 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 151.6 s | power-cycle · 4/4 boots · up 20 s |
| hw-performance | ✅ | 18.9 s | AES 917 · mem 5000 · disk W 1032 / R 1011 MB/s · 35 °C · 1992 MHz |
| dvfs | ✅ | 23.3 s | ondemand · 408–1992 MHz (peak 1992) |
| network-iperf | ✅ | 62.9 s | eth0 ↑941/↓941 (1GE) · wlx40a5eff39254 ↑205/↓220 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 86.6 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 56.4 s | power-cycle · up 24 s |

**Power** — min 1.90 W · avg 6.24 W · peak 10.60 W · 678 samples

```mermaid
xychart-beta
    title "Power — Odroid M1 01"
    x-axis "sample" 1 --> 678
    y-axis "W" 1.5 --> 11.0
    line [6.21, 6.07, 5.52, 6.08, 6.92, 6.99, 4.92, 7.46, 6.28, 6.15, 7.00, 5.79, 5.74, 6.91, 5.91, 5.71, 5.73, 5.60, 7.09, 7.09, 5.89, 6.59, 4.96, 6.76, 5.82, 6.55, 6.06, 5.31, 6.96, 6.61, 6.32, 5.68, 6.25, 5.88, 6.76, 7.51, 5.97, 6.51, 4.36, 7.62]
```

### ✅ Odroid N2 01

`odroidn2` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 44.0 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 66.6 s | power-cycle · up 28 s |
| kernel-switch | ✅ | 24.7 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 175.0 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 18.7 s | AES 1085 · mem 4900 · disk W 26 / R 134 MB/s · 37.1 °C · 1992 MHz |
| dvfs | ✅ | 17.4 s | performance · 1000–1992 MHz (peak 1992) |
| network-iperf | ✅ | 67.9 s | end0 ↑939/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.6 s | 26.11.0-trunk.62 · 6.18.54-current-meson64 |
| kernel-switch | ✅ | 81.6 s | branch=edge · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-meson64 · kernel_before=6.18.54-current-meson64 |
| reboot | ✅ | 177.6 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 19.6 s | AES 1085 · mem 4900 · disk W 27 / R 135 MB/s · 37.9 °C · 1992 MHz |
| dvfs | ✅ | 18.4 s | performance · 1000–1992 MHz (peak 1992) |
| network-iperf | ✅ | 30.4 s | end0 ↑940/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.62 · 7.2.8-edge-meson64 |
| kernel-switch | ✅ | 80.7 s | branch=current · family=meson64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-meson64 · kernel_before=7.2.8-edge-meson64 |
| reboot | ✅ | 57.7 s | power-cycle · up 23 s |

**Power** — min 1.00 W · avg 4.67 W · peak 10.70 W · 700 samples

```mermaid
xychart-beta
    title "Power — Odroid N2 01"
    x-axis "sample" 1 --> 700
    y-axis "W" 0.5 --> 11.0
    line [4.62, 5.05, 3.97, 2.13, 4.52, 5.64, 3.84, 4.72, 4.36, 5.58, 3.74, 5.28, 3.93, 4.63, 5.81, 7.09, 4.29, 4.79, 4.25, 5.64, 4.71, 4.98, 4.70, 3.74, 4.72, 3.64, 4.22, 4.57, 4.67, 3.89, 5.40, 7.20, 5.01, 4.26, 5.42, 4.87, 4.92, 4.89, 2.62, 4.26]
```

### ✅ Odroid XU4 01

`odroidxu4` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 54.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 55.1 s | power-cycle · up 30 s |
| kernel-switch | ✅ | 38.5 s | branch=current · family=odroidxu4 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.6.155-current-odroidxu4 · kernel_before=6.6.155-current-odroidxu4 |
| reboot | ✅ | 182.2 s | power-cycle · 4/4 boots · up 31 s |
| hw-performance | ✅ | 33.9 s | AES 69 · mem 5400 · disk W 17 / R 60 MB/s · 61 °C · 1400 MHz |
| dvfs | ✅ | 30.2 s | ondemand · 600–1400 MHz (peak 2000) |
| network-iperf | ✅ | 37.1 s | end0 ↑922/↓941 (1GE) Mbps |
| store-versions | ✅ | 6.7 s | 26.11.0-trunk.62 · 6.6.155-current-odroidxu4 |
| kernel-switch | ✅ | 99.8 s | branch=edge · family=odroidxu4 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-odroidxu4 · kernel_before=6.6.155-current-odroidxu4 |
| reboot | ✅ | 172.0 s | power-cycle · 4/4 boots · up 29 s |
| hw-performance | ✅ | 35.2 s | AES 65 · mem 5500 · disk W 1 / R 61 MB/s · 65 °C · 1400 MHz |
| dvfs | ✅ | 31.8 s | ondemand · 600–1400 MHz (peak 1900) |
| network-iperf | ✅ | 37.7 s | end0 ↑919/↓941 (1GE) Mbps |
| store-versions | ✅ | 5.9 s | 26.11.0-trunk.62 · 7.2.8-edge-odroidxu4 |
| kernel-switch | ✅ | 103.2 s | branch=current · family=odroidxu4 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.6.155-current-odroidxu4 · kernel_before=7.2.8-edge-odroidxu4 |
| reboot | ✅ | 55.6 s | power-cycle · up 31 s |

### ✅ Orange Pi 3 01

`orangepi3` · **inplace** · image `26.11.0-trunk.58` · 15 ✅ · 0 ❌ · 1 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 21.3 s | — |
| reboot | ✅ | 60.5 s | power-cycle · up 30 s |
| kernel-switch | ✅ | 94.6 s | branch=current · family=sunxi64 · installed=26.8.0-trunk.61 · boot_image=/boot/vmlinuz-6.18.33-current-sunxi64 · kernel_before=6.18.53-current-sunxi64 |
| reboot | ✅ | 829.5 s | power-cycle · 1/4 boots · up 24 s |
| hw-performance | ✅ | 28.8 s | AES 835 · mem 4600 · disk W 20 / R 23 MB/s · 42.1 °C · 1800 MHz |
| dvfs | ✅ | 20.4 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 62.3 s | end0 ↑912/↓926 (1GE) · wlan0 ↑42/↓107 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.58 · 6.18.33-current-sunxi64 |
| kernel-switch | ✅ | 101.7 s | branch=edge · family=sunxi64 · installed=26.8.0-trunk.61 · boot_image=/boot/vmlinuz-7.0.10-edge-sunxi64 · kernel_before=6.18.33-current-sunxi64 |
| reboot | ✅ | 810.2 s | power-cycle · 1/4 boots · up 23 s |
| hw-performance | ✅ | 29.0 s | AES 839 · mem 4600 · disk W 21 / R 23 MB/s · 42.4 °C · 1800 MHz |
| dvfs | ✅ | 21.1 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 66.4 s | end0 ↑913/↓939 (1GE) · wlan0 ↑58/↓106 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.58 · 7.0.10-edge-sunxi64 |
| kernel-switch | ✅ | 98.4 s | branch=current · family=sunxi64 · installed=26.8.0-trunk.61 · boot_image=/boot/vmlinuz-6.18.33-current-sunxi64 · kernel_before=7.0.10-edge-sunxi64 |
| reboot | ✅ | 53.4 s | power-cycle · up 23 s |

### ✅ Orange Pi 5 Plus 01

`orangepi5-plus` · **inplace** · image `26.11.0-trunk.62` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 38.1 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 58.8 s | power-cycle · up 33 s |
| kernel-switch | ✅ | 18.1 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 160.8 s | power-cycle · 4/4 boots · up 28 s |
| hw-performance | ✅ | 17.4 s | AES 1256 · mem 13500 · disk W 54 / R 62 MB/s · 52.7 °C · 1800 MHz |
| dvfs | ✅ | 16.5 s | ondemand · 1800–1800 MHz (peak 2304) |
| network-iperf | ✅ | 54.5 s | enP3p49s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑502/↓336 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 3.7 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 96.3 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 179.0 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 18.6 s | AES 1254 · mem 10200 · disk W 53 / R 57 MB/s · 55.5 °C · 1800 MHz |
| dvfs | ✅ | 14.5 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 56.5 s | enP3p49s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑111/↓127 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.0 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 65.8 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 157.1 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 18.8 s | AES 1253 · mem 8100 · disk W 51 / R 55 MB/s · 57.3 °C · 1800 MHz |
| dvfs | ✅ | 14.3 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 57.1 s | enP3p49s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑125/↓89 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 63.7 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 62.3 s | power-cycle · up 29 s |

**Power** — min 0.60 W · avg 6.10 W · peak 12.70 W · 929 samples

```mermaid
xychart-beta
    title "Power — Orange Pi 5 Plus 01"
    x-axis "sample" 1 --> 929
    y-axis "W" 0.5 --> 13.0
    line [5.62, 5.68, 4.04, 6.17, 4.02, 4.95, 5.01, 4.76, 3.75, 6.98, 7.47, 6.21, 7.40, 5.88, 5.99, 5.68, 4.38, 5.87, 5.13, 4.74, 6.30, 5.25, 8.25, 7.19, 7.63, 7.43, 7.55, 7.36, 5.36, 4.78, 4.48, 6.03, 7.17, 8.50, 7.31, 7.70, 7.72, 7.78, 5.65, 4.81]
```

### ✅ Orange Pi Lite 2 01

`orangepilite2` · **inplace** · image `26.11.0-trunk.59` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 316.5 s | nightly · 26.11.0-trunk.59 → 26.11.0-trunk.62 |
| reboot | ✅ | 36.7 s | warm · up 21 s |
| kernel-switch | ✅ | 38.2 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 148.2 s | warm · 4/4 boots · up 24 s |
| hw-performance | ✅ | 31.8 s | AES 808 · mem 4500 · disk W 21 / R 23 MB/s · 73.6 °C · 1800 MHz |
| dvfs | ✅ | 25.1 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 41.2 s | wlan0 ↑25/↓20 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.4 s | 26.11.0-trunk.62 · 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 116.2 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 147.4 s | warm · 4/4 boots · up 26 s |
| hw-performance | ✅ | 31.0 s | AES 771 · mem 4500 · disk W 14 / R 23 MB/s · 70.5 °C · 1800 MHz |
| dvfs | ✅ | 21.6 s | ondemand · 480–1800 MHz (peak 1800) |
| network-iperf | ✅ | 57.3 s | wlan0 ↑38/↓30 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.62 · 7.2.8-edge-sunxi64 |
| kernel-switch | ✅ | 121.5 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=7.2.8-edge-sunxi64 |
| reboot | ✅ | 37.3 s | warm · up 21 s |

### ✅ OrangePi 3 LTS 01

`orangepi3-lts` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 143.7 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 57.8 s | power-cycle · up 23 s |
| kernel-switch | ✅ | 127.5 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 155.0 s | power-cycle · 4/4 boots · up 24 s |
| hw-performance | ✅ | 20.8 s | AES 750 · mem 4100 · disk W 46 / R 128 MB/s · 65.6 °C · 1608 MHz |
| dvfs | ✅ | 21.6 s | ondemand · 480–1608 MHz (peak 1608) |
| network-iperf | ✅ | 58.4 s | end0 ↑915/↓937 (1GE) · wlan0 ↑142/↓131 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.8 s | 26.11.0-trunk.62 · 6.18.54-current-sunxi64 |
| kernel-switch | ✅ | 127.6 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi64 · kernel_before=6.18.54-current-sunxi64 |
| reboot | ✅ | 151.0 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 20.5 s | AES 750 · mem 4100 · disk W 50 / R 126 MB/s · 65.9 °C · 1608 MHz |
| dvfs | ✅ | 21.8 s | ondemand · 480–1608 MHz (peak 1608) |
| network-iperf | ✅ | 58.8 s | end0 ↑915/↓940 (1GE) · wlan0 ↑135/↓127 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.62 · 7.2.8-edge-sunxi64 |
| kernel-switch | ✅ | 122.8 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi64 · kernel_before=7.2.8-edge-sunxi64 |
| reboot | ✅ | 58.1 s | power-cycle · up 22 s |

**Power** — min 1.00 W · avg 3.24 W · peak 4.80 W · 914 samples

```mermaid
xychart-beta
    title "Power — OrangePi 3 LTS 01"
    x-axis "sample" 1 --> 914
    y-axis "W" 0.5 --> 5.0
    line [3.09, 3.25, 3.27, 3.38, 3.25, 2.69, 2.87, 3.44, 3.24, 3.37, 3.41, 3.08, 3.35, 2.94, 2.75, 2.93, 3.21, 3.76, 3.33, 3.63, 3.24, 3.45, 3.34, 3.53, 3.34, 2.90, 3.10, 3.10, 3.02, 2.79, 3.49, 3.69, 3.61, 3.48, 3.50, 3.30, 3.40, 3.48, 2.64, 2.82]
```

### ✅ Radxa Dragon Q6A 01

`radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.51` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 65.9 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
| reboot | ✅ | 137.3 s | power-cycle · up 105 s |
| kernel-switch | ✅ | 16.8 s | branch=current · family=qcs6490 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.2-current-qcs6490 · kernel_before=6.18.2-current-qcs6490 |
| reboot | ✅ | 137.8 s | power-cycle · up 105 s |
| hw-performance | ✅ | 13.3 s | AES 1495 · mem 18700 · disk W 237 / R 1100 MB/s · 47.7 °C · 1958 MHz |
| dvfs | ✅ | 14.2 s | ondemand · 300–1958 MHz (peak 2707) |
| network-iperf | ✅ | 30.5 s | enp1s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.7 s | 26.11.0-trunk.54 · 6.18.2-current-qcs6490 |
| kernel-switch | ✅ | 80.0 s | branch=edge · family=qcs6490 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-7.2.3-edge-qcs6490 · kernel_before=6.18.2-current-qcs6490 |
| reboot | ✅ | 139.6 s | power-cycle · up 107 s |
| hw-performance | ✅ | 13.4 s | AES 1523 · mem 15300 · disk W 253 / R 1182 MB/s · 49.6 °C · 1958 MHz |
| dvfs | ✅ | 15.4 s | ondemand · 300–1958 MHz (peak 2707) |
| network-iperf | ✅ | 27.5 s | enp1s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 3.6 s | 26.11.0-trunk.54 · 7.2.3-edge-qcs6490 |
| kernel-switch | ✅ | 82.7 s | branch=current · family=qcs6490 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.2-current-qcs6490 · kernel_before=7.2.3-edge-qcs6490 |
| reboot | ✅ | 138.2 s | power-cycle · up 105 s |

**Power** — min 1.00 W · avg 2.61 W · peak 8.70 W · 735 samples

```mermaid
xychart-beta
    title "Power — Radxa Dragon Q6A 01"
    x-axis "sample" 1 --> 735
    y-axis "W" 0.5 --> 9.0
    line [2.48, 4.88, 5.20, 2.28, 2.47, 1.88, 1.88, 1.90, 1.88, 2.78, 2.05, 3.36, 1.88, 1.82, 1.91, 2.18, 3.82, 2.35, 2.76, 4.15, 3.53, 2.68, 1.64, 2.79, 1.80, 1.86, 1.96, 2.13, 4.02, 2.27, 2.86, 3.18, 4.23, 3.04, 2.19, 2.41, 2.19, 1.80, 1.83, 2.05]
```

### ✅ Radxa ZERO 3 01

`radxa-zero3` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ⏭️ | 0.0 s | — |
| reboot | ⏭️ | 0.0 s | reboot |
| hw-performance | ✅ | 34.1 s | AES 723 · mem 4000 · disk W 21 / R 22 MB/s · 45.6 °C · 1416 MHz |
| dvfs | ✅ | 27.7 s | ondemand · 408–1416 MHz (peak 1416) |
| network-iperf | ✅ | 41.2 s | wlan0 ↑5/↓25 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 5.9 s | 26.5.1 · 6.18.44-current-rockchip64 |

### ✅ Raspberry Pi 3B

`rpi4b` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 148.2 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 51.9 s | warm · up 31 s |
| kernel-switch | ✅ | 74.8 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 186.6 s | warm · 4/4 boots · up 31 s |
| hw-performance | ✅ | 44.5 s | AES 20 · mem 1400 · disk W 20 / R 22 MB/s · 52.1 °C · 1200 MHz |
| dvfs | ✅ | 40.2 s | ondemand · 600–1200 MHz (peak 1200) |
| network-iperf | ✅ | 110.8 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑18/↓20 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 8.7 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ✅ | 237.4 s | branch=edge · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.7-edge-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 184.5 s | warm · 4/4 boots · up 29 s |
| hw-performance | ✅ | 45.0 s | AES 20 · mem 1400 · disk W 20 / R 22 MB/s · 52.1 °C · 1200 MHz |
| dvfs | ✅ | 40.6 s | ondemand · 600–1200 MHz (peak 1200) |
| network-iperf | ✅ | 86.0 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑24/↓26 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 8.8 s | 26.11.0-trunk.62 · 7.2.7-edge-bcm2711 |
| kernel-switch | ✅ | 235.7 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=7.2.7-edge-bcm2711 |
| reboot | ✅ | 51.1 s | warm · up 31 s |

### ✅ Raspberry Pi 5B

`rpi4b` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 93.3 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 47.2 s | power-cycle · up 21 s |
| kernel-switch | ✅ | 13.2 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 120.4 s | power-cycle · 4/4 boots · up 18 s |
| hw-performance | ✅ | 14.6 s | AES 1368 · mem 12100 · disk W 54 / R 86 MB/s · 63.4 °C · 2400 MHz |
| dvfs | ✅ | 13.9 s | ondemand · 1500–2400 MHz (peak 2400) |
| network-iperf | ✅ | 50.2 s | end0 ↑936/↓941 (1GE) · wlan0 ↑34/↓26 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.0 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ✅ | 120.1 s | branch=edge · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.7-edge-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 123.8 s | power-cycle · 4/4 boots · up 21 s |
| hw-performance | ✅ | 14.9 s | AES 1368 · mem 9200 · disk W 50 / R 82 MB/s · 63.9 °C · 2400 MHz |
| dvfs | ✅ | 13.5 s | ondemand · 1500–2400 MHz (peak 2400) |
| network-iperf | ✅ | 53.4 s | end0 ↑936/↓941 (1GE) · wlan0 ↑40/↓31 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 3.9 s | 26.11.0-trunk.62 · 7.2.7-edge-bcm2711 |
| kernel-switch | ✅ | 122.2 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=7.2.7-edge-bcm2711 |
| reboot | ✅ | 43.8 s | power-cycle · up 18 s |

**Power** — min 2.40 W · avg 5.98 W · peak 10.50 W · 675 samples

```mermaid
xychart-beta
    title "Power — Raspberry Pi 5B"
    x-axis "sample" 1 --> 675
    y-axis "W" 2.0 --> 11.0
    line [5.74, 5.54, 6.02, 8.44, 6.46, 4.76, 6.16, 5.66, 6.18, 5.05, 5.08, 3.95, 6.03, 7.48, 6.61, 5.96, 5.59, 6.47, 5.53, 7.06, 7.86, 6.48, 6.29, 5.17, 4.79, 5.77, 5.19, 4.59, 5.95, 6.84, 5.86, 5.58, 5.80, 5.74, 5.49, 8.41, 6.82, 6.45, 5.31, 4.91]
```

### ✅ Raspberry Pi Zero 2W

`rpi4b` · **inplace** · image `26.11.0-trunk.58` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 89.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 43.9 s | warm · up 25 s |
| kernel-switch | ✅ | 55.4 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 144.5 s | warm · 4/4 boots · up 23 s |
| hw-performance | ✅ | 33.7 s | AES 33 · mem 2100 · disk W 1 / R 23 MB/s · 53.7 °C · 1000 MHz |
| dvfs | ✅ | 27.1 s | ondemand · 600–1000 MHz (peak 1000) |
| network-iperf | ✅ | 39.6 s | wlan0 ↑27/↓34 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 5.8 s | 26.11.0-trunk.62 · 6.18.53-current-bcm2711 |
| kernel-switch | ✅ | 191.8 s | branch=edge · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.7-edge-bcm2711 · kernel_before=6.18.53-current-bcm2711 |
| reboot | ✅ | 149.5 s | warm · 4/4 boots · up 22 s |
| hw-performance | ✅ | 35.2 s | AES 33 · mem 2200 · disk W 1 / R 22 MB/s · 54.2 °C · 1000 MHz |
| dvfs | ✅ | 28.9 s | ondemand · 600–1000 MHz (peak 1000) |
| network-iperf | ✅ | 46.2 s | wlan0 ↑23/↓27 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 6.2 s | 26.11.0-trunk.62 · 7.2.7-edge-bcm2711 |
| kernel-switch | ✅ | 190.5 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.53-current-bcm2711 · kernel_before=7.2.7-edge-bcm2711 |
| reboot | ✅ | 41.3 s | warm · up 23 s |

### ✅ Rock 5B 01

`rock-5b` · **inplace** · image `26.8.3` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 142.5 s | nightly · 26.8.3 → 26.11.0-trunk.62 |
| reboot | ✅ | 44.7 s | power-cycle · up 18 s |
| kernel-switch | ✅ | 21.3 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 123.7 s | power-cycle · 4/4 boots · up 18 s |
| hw-performance | ✅ | 19.7 s | AES 1295 · mem 15600 · disk W 26 / R 83 MB/s · 53 °C · 1800 MHz |
| dvfs | ✅ | 16.9 s | ondemand · 1800–1800 MHz (peak 2352) |
| network-iperf | ✅ | 55.9 s | enP4p65s0 ↑941/↓940 (1GE) · wlP2p33s0 ↑619/↓404 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.5 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 84.1 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 451.0 s | power-cycle · 4/4 boots · up 102 s |
| hw-performance | ✅ | 20.3 s | AES 1291 · mem 10200 · disk W 26 / R 82 MB/s · 57.3 °C · 1800 MHz |
| dvfs | ✅ | 14.7 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 29.7 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.0 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 66.4 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 460.4 s | power-cycle · 4/4 boots · up 102 s |
| hw-performance | ✅ | 20.4 s | AES 1290 · mem 8100 · disk W 25 / R 82 MB/s · 59.2 °C · 1800 MHz |
| dvfs | ✅ | 14.5 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 28.3 s | end0 ↑941/↓941 Mbps |
| store-versions | ✅ | 4.1 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 67.6 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 56.6 s | power-cycle · up 22 s |

**Power** — min 0.70 W · avg 4.92 W · peak 11.70 W · 1393 samples

```mermaid
xychart-beta
    title "Power — Rock 5B 01"
    x-axis "sample" 1 --> 1393
    y-axis "W" 0.5 --> 12.0
    line [3.42, 3.84, 3.75, 3.82, 4.00, 4.61, 4.18, 4.48, 4.57, 4.00, 3.68, 3.68, 5.32, 5.10, 5.19, 5.10, 5.16, 5.27, 5.12, 5.31, 5.10, 5.13, 6.90, 5.74, 6.10, 5.23, 5.20, 5.01, 5.26, 5.18, 4.97, 5.18, 5.20, 4.15, 5.14, 5.32, 6.71, 5.72, 6.23, 3.88]
```

### ✅ Rock 5B Plus 01

`rock-5b-plus` · **inplace** · image `26.11.0-trunk.62` · 22 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 190.8 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 61.5 s | power-cycle · up 34 s |
| kernel-switch | ✅ | 25.0 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 149.9 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 16.9 s | AES 1285 · mem 14000 · disk W 69 / R 81 MB/s · 49.9 °C · 1800 MHz |
| dvfs | ✅ | 16.6 s | ondemand · 1800–1800 MHz (peak 2352) |
| network-iperf | ✅ | 29.9 s | enP4p65s0 ↑940/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.2 s | 26.11.0-trunk.62 · 6.1.172-vendor-rk35xx |
| kernel-switch | ✅ | 648.4 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
| reboot | ✅ | 165.1 s | power-cycle · 4/4 boots · up 26 s |
| hw-performance | ✅ | 17.6 s | AES 1279 · mem 10500 · disk W 66 / R 72 MB/s · 56.4 °C · 1800 MHz |
| dvfs | ✅ | 16.0 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 40.1 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
| store-versions | ✅ | 4.4 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 497.5 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 136.2 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 18.4 s | AES 1272 · mem 5600 · disk W 64 / R 71 MB/s · 64.7 °C · 1800 MHz |
| dvfs | ✅ | 15.5 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 28.9 s | end0 ↑941/↓942 Mbps |
| store-versions | ✅ | 5.6 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 476.9 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 50.5 s | power-cycle · up 24 s |

**Power** — min 0.90 W · avg 6.94 W · peak 14.20 W · 2105 samples

```mermaid
xychart-beta
    title "Power — Rock 5B Plus 01"
    x-axis "sample" 1 --> 2105
    y-axis "W" 0.5 --> 14.5
    line [3.44, 3.39, 4.41, 3.46, 3.56, 3.34, 4.38, 3.82, 5.09, 9.22, 11.11, 5.91, 8.08, 9.50, 9.14, 3.88, 3.47, 3.81, 4.63, 5.30, 6.51, 6.67, 9.28, 12.10, 10.69, 8.25, 10.91, 11.38, 6.54, 4.61, 4.94, 6.33, 6.29, 8.85, 10.52, 10.41, 8.40, 10.18, 10.41, 5.32]
```

### ✅ Rock 5T 01

`rock-5t` · **inplace** · image `26.8.3` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 127.1 s | nightly · 26.8.3 → 26.11.0-trunk.62 |
| reboot | ✅ | 52.4 s | power-cycle · up 22 s |
| kernel-switch | ✅ | 22.0 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 144.6 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 18.1 s | AES 1254 · mem 6000 · disk W 52 / R 82 MB/s · 54.5 °C · 1800 MHz |
| dvfs | ✅ | 16.4 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 57.9 s | enP4p65s0 ↑941/↓942 (1GE) · wlP2p33s0 ↑479/↓275 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.0 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 78.0 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 151.1 s | power-cycle · 4/4 boots · up 23 s |
| hw-performance | ✅ | 18.3 s | AES 1254 · mem 4900 · disk W 50 / R 80 MB/s · 54.5 °C · 1800 MHz |
| dvfs | ✅ | 15.1 s | ondemand · 408–1800 MHz (peak 2400) |
| network-iperf | ✅ | 57.3 s | end0 ↑941/↓941 · wlP2p33s0 ↑557/↓235 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.6 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 78.9 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 56.3 s | power-cycle · up 22 s |

**Power** — min 1.80 W · avg 7.32 W · peak 14.80 W · 706 samples

```mermaid
xychart-beta
    title "Power — Rock 5T 01"
    x-axis "sample" 1 --> 706
    y-axis "W" 1.5 --> 15.0
    line [7.51, 7.44, 7.91, 7.98, 8.82, 7.97, 7.11, 8.36, 8.08, 6.45, 5.59, 6.36, 6.11, 6.35, 3.89, 7.92, 10.66, 7.57, 8.41, 7.78, 7.95, 7.48, 8.20, 7.41, 6.57, 5.73, 7.36, 7.05, 4.31, 6.37, 7.95, 9.65, 7.48, 8.30, 7.45, 7.67, 7.86, 8.45, 5.40, 5.89]
```

### ✅ Rockpi E 01

`rockpi-e` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 90.1 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 55.7 s | power-cycle · up 24 s |
| kernel-switch | ✅ | 50.2 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 154.8 s | power-cycle · 4/4 boots · up 24 s |
| hw-performance | ✅ | 32.1 s | AES 602 · mem 3300 · disk W 21 / R 23 MB/s · 56.8 °C · 1296 MHz |
| dvfs | ✅ | 25.4 s | ondemand · 408–1296 MHz (peak 1296) |
| network-iperf | ✅ | 91.8 s | end0 ↑940/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑130/↓197 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.6 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 176.0 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 148.1 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 31.9 s | AES 601 · mem 3300 · disk W 21 / R 23 MB/s · 59.1 °C · 1296 MHz |
| dvfs | ✅ | 25.7 s | ondemand · 408–1296 MHz (peak 1296) |
| network-iperf | ✅ | 88.3 s | end0 ↑941/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑149/↓205 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.7 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 170.3 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 56.0 s | power-cycle · up 25 s |

### ✅ Rockpi S 01

`rockpi-s` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 142.4 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 65.9 s | power-cycle · up 31 s |
| kernel-switch | ✅ | 70.8 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 185.9 s | power-cycle · 4/4 boots · up 31 s |
| hw-performance | ✅ | 40.9 s | AES 219 · mem 1300 · disk W 21 / R 22 MB/s · 50.8 °C · 1008 MHz |
| dvfs | ✅ | 35.8 s | ondemand · 408–1008 MHz (peak 1008) |
| network-iperf | ✅ | 75.1 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑7/↓6 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 7.8 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 233.6 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 184.1 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 41.4 s | AES 219 · mem 1300 · disk W 21 / R 22 MB/s · 51.7 °C · 1008 MHz |
| dvfs | ✅ | 36.4 s | ondemand · 408–1008 MHz (peak 1008) |
| network-iperf | ✅ | 93.3 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑7/↓1 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 7.9 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 234.2 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 66.9 s | power-cycle · up 31 s |

**Power** — min 0.80 W · avg 1.48 W · peak 2.60 W · 1220 samples

```mermaid
xychart-beta
    title "Power — Rockpi S 01"
    x-axis "sample" 1 --> 1220
    y-axis "W" 0.5 --> 3.0
    line [1.38, 1.45, 1.43, 1.42, 1.24, 1.64, 1.48, 1.35, 1.64, 1.56, 1.47, 1.48, 1.53, 1.45, 1.29, 1.75, 1.52, 1.46, 1.61, 1.44, 1.46, 1.46, 1.37, 1.61, 1.58, 1.51, 1.59, 1.55, 1.54, 1.36, 1.28, 1.49, 1.45, 1.57, 1.56, 1.47, 1.41, 1.43, 1.29, 1.44]
```

### ✅ RockPro 64 01

`rockpro64` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 54.2 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 66.3 s | power-cycle · up 31 s |
| kernel-switch | ✅ | 49.0 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 860.2 s | power-cycle · 1/4 boots · up 30 s |
| hw-performance | ✅ | 20.7 s | AES 1020 · mem 6600 · disk W 66 / R 120 MB/s · 44.4 °C · 1416 MHz |
| dvfs | ✅ | 21.6 s | ondemand · 408–1416 MHz (peak 1800) |
| network-iperf | ✅ | 62.8 s | end0 ↑940/↓941 (1GE) · wlan0 ↑71/↓98 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.4 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip64 |
| kernel-switch | ✅ | 107.0 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip64 · kernel_before=6.18.54-current-rockchip64 |
| reboot | ✅ | 836.8 s | power-cycle · 1/4 boots · up 30 s |
| hw-performance | ✅ | 21.0 s | AES 1021 · mem 6500 · disk W 66 / R 115 MB/s · 45.6 °C · 1416 MHz |
| dvfs | ✅ | 21.7 s | ondemand · 408–1416 MHz (peak 1800) |
| network-iperf | ✅ | 60.1 s | end0 ↑941/↓941 (1GE) · wlan0 ↑106/↓93 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 13.5 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip64 |
| kernel-switch | ✅ | 105.5 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip64 · kernel_before=7.2.8-edge-rockchip64 |
| reboot | ✅ | 63.0 s | power-cycle · up 28 s |

**Power** — min 2.90 W · avg 4.54 W · peak 8.90 W · 1863 samples

```mermaid
xychart-beta
    title "Power — RockPro 64 01"
    x-axis "sample" 1 --> 1863
    y-axis "W" 2.5 --> 9.0
    line [4.80, 3.86, 4.09, 4.49, 4.41, 4.48, 4.44, 4.33, 4.20, 4.20, 4.22, 4.66, 4.24, 4.25, 4.27, 4.11, 4.50, 5.63, 4.76, 4.46, 5.01, 4.65, 4.78, 4.77, 4.57, 5.16, 4.80, 4.81, 4.80, 4.74, 4.45, 4.40, 4.40, 4.09, 4.42, 5.04, 4.61, 4.20, 4.95, 4.68]
```

### ✅ SpacemiT K3 Pico-ITX 01

`k3picoitx` · **inplace** · image `26.11.0-trunk.58` · 8 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 29.3 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 47.6 s | power-cycle · up 21 s |
| kernel-switch | ✅ | 19.6 s | branch=legacy · family=spacemit-k3 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.3-legacy-spacemit-k3 · kernel_before=6.18.3-legacy-spacemit-k3 |
| reboot | ✅ | 138.3 s | power-cycle · 4/4 boots · up 22 s |
| hw-performance | ✅ | 13.9 s | AES 778 · mem 12200 · disk W 1324 / R 1436 MB/s · 43 °C · 2150 MHz |
| dvfs | ✅ | 15.5 s | performance · 614–2150 MHz (peak 2150) |
| network-iperf | ✅ | 80.2 s | eth0 ↑925/↓924 (1GE) · eth1 ↑939/↓939 (10GE) · wlan0 ↑115/↓191 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.6 s | 26.11.0-trunk.62 · 6.18.3-legacy-spacemit-k3 |

### ✅ Tinker Board 01

`tinkerboard` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 65.9 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 63.7 s | power-cycle · up 28 s |
| kernel-switch | ✅ | 29.6 s | branch=current · family=rockchip · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip · kernel_before=6.18.54-current-rockchip |
| reboot | ✅ | 170.7 s | power-cycle · 4/4 boots · up 29 s |
| hw-performance | ✅ | 28.5 s | AES 67 · mem 3300 · disk W 12 / R 63 MB/s · 56.4 °C · 1800 MHz |
| dvfs | ✅ | 19.9 s | ondemand · 600–1800 MHz (peak 1800) |
| network-iperf | ✅ | 61.5 s | end0 ↑940/↓941 (1GE) · wlan0 ↑13/↓18 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.62 · 6.18.54-current-rockchip |
| kernel-switch | ✅ | 83.3 s | branch=edge · family=rockchip · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-rockchip · kernel_before=6.18.54-current-rockchip |
| reboot | ✅ | 171.6 s | power-cycle · 4/4 boots · up 30 s |
| hw-performance | ✅ | 28.5 s | AES 67 · mem 3200 · disk W 13 / R 63 MB/s · 57.3 °C · 1800 MHz |
| dvfs | ✅ | 21.1 s | ondemand · 600–1800 MHz (peak 1800) |
| network-iperf | ✅ | 61.3 s | end0 ↑941/↓941 (1GE) · wlan0 ↑23/↓29 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 4.7 s | 26.11.0-trunk.62 · 7.2.8-edge-rockchip |
| kernel-switch | ✅ | 81.5 s | branch=current · family=rockchip · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-rockchip · kernel_before=7.2.8-edge-rockchip |
| reboot | ✅ | 63.3 s | power-cycle · up 29 s |

**Power** — min 2.00 W · avg 3.83 W · peak 8.40 W · 754 samples

```mermaid
xychart-beta
    title "Power — Tinker Board 01"
    x-axis "sample" 1 --> 754
    y-axis "W" 1.5 --> 8.5
    line [3.57, 3.88, 3.88, 3.19, 3.09, 4.57, 4.17, 3.46, 4.46, 3.31, 3.07, 3.78, 2.86, 4.03, 3.66, 5.14, 3.99, 4.24, 4.30, 3.54, 3.98, 4.07, 2.69, 4.25, 3.51, 3.85, 3.92, 2.94, 3.19, 3.87, 5.82, 3.79, 3.68, 4.23, 4.15, 3.97, 4.36, 3.72, 3.36, 3.74]
```

### ✅ Udoo 01

`udoo` · **inplace** · image `26.11.0-trunk.62` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 161.6 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 70.5 s | power-cycle · up 34 s |
| kernel-switch | ✅ | 79.0 s | branch=current · family=imx6 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-imx6 · kernel_before=6.18.54-current-imx6 |
| reboot | ✅ | 203.9 s | power-cycle · 4/4 boots · up 34 s |
| hw-performance | ✅ | 49.6 s | AES 26 · mem 799 · disk W 19 / R 20 MB/s · 47.5 °C · 996 MHz |
| dvfs | ✅ | 44.3 s | ondemand · 396–996 MHz (peak 996) |
| network-iperf | ✅ | 90.2 s | end0 ↑400/↓235 (1GE) · wlx7cdd903aa418 ↑22/↓9 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 9.4 s | 26.11.0-trunk.62 · 6.18.54-current-imx6 |
| kernel-switch | ✅ | 476.3 s | branch=edge · family=imx6 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.1.13-edge-imx6 · kernel_before=6.18.54-current-imx6 |
| reboot | ✅ | 201.9 s | power-cycle · 4/4 boots · up 34 s |
| hw-performance | ✅ | 51.2 s | AES 26 · mem 732 · disk W 19 / R 20 MB/s · 48.1 °C · 996 MHz |
| dvfs | ✅ | 47.1 s | ondemand · 396–996 MHz (peak 996) |
| network-iperf | ✅ | 82.3 s | end0 ↑398/↓227 (1GE) · wlx7cdd903aa418 ↑23/↓16 (Wi-Fi 4) Mbps |
| store-versions | ✅ | 9.5 s | 26.11.0-trunk.62 · 7.1.13-edge-imx6 |
| kernel-switch | ✅ | 458.5 s | branch=current · family=imx6 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-imx6 · kernel_before=7.1.13-edge-imx6 |
| reboot | ✅ | 70.6 s | power-cycle · up 33 s |

**Power** — min 1.30 W · avg 5.87 W · peak 8.60 W · 1695 samples

```mermaid
xychart-beta
    title "Power — Udoo 01"
    x-axis "sample" 1 --> 1695
    y-axis "W" 1.0 --> 9.0
    line [6.07, 6.21, 6.26, 5.65, 6.60, 5.93, 6.10, 5.86, 5.55, 6.69, 6.04, 6.29, 5.82, 6.15, 5.10, 5.00, 5.06, 5.22, 6.22, 6.09, 5.80, 6.16, 5.49, 6.23, 5.77, 5.90, 6.14, 5.82, 6.33, 6.15, 6.04, 5.11, 5.17, 5.05, 5.33, 6.45, 5.99, 5.91, 5.89, 6.03]
```

### ✅ UEFI arm64 01

`uefi-arm64` · **inplace** · image `26.11.0-trunk.56` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 23.4 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.56 |
| reboot | ✅ | 50.7 s | warm · up 29 s |
| kernel-switch | ✅ | 76.8 s | branch=current · family=arm64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-arm64 · kernel_before=7.2.7-edge-arm64 |
| reboot | ✅ | 180.2 s | warm · 4/4 boots · up 30 s |
| hw-performance | ✅ | 15.0 s | AES 1458 · mem 13000 · disk W 1545 / R 2363 MB/s · 45 °C · 2600 MHz |
| dvfs | ✅ | 15.0 s | ondemand · 800–2600 MHz (peak 2600) |
| network-iperf | ✅ | 79.3 s | enp1s0 ↑6907/↓2757 (10GE) · enp49s0 ↑7786/↓9371 (10GE) · wlp97s0 ↑121/↓101 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.3 s | 26.11.0-trunk.56 · 6.18.53-current-arm64 |
| kernel-switch | ✅ | 70.8 s | branch=edge · family=arm64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-arm64 · kernel_before=6.18.53-current-arm64 |
| reboot | ✅ | 182.8 s | warm · 4/4 boots · up 32 s |
| hw-performance | ✅ | 15.5 s | AES 1402 · mem 13000 · disk W 1556 / R 2112 MB/s · 45 °C · 2600 MHz |
| dvfs | ✅ | 18.4 s | ondemand · 800–2600 MHz (peak 2600) |
| network-iperf | ✅ | 80.3 s | enp1s0 ↑8544/↓2770 (10GE) · enp49s0 ↑8845/↓8876 (10GE) · wlp97s0 ↑122/↓87 (Wi-Fi 6) Mbps |
| store-versions | ✅ | 4.4 s | 26.11.0-trunk.56 · 7.2.7-edge-arm64 |
| kernel-switch | ✅ | 73.5 s | branch=current · family=arm64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-arm64 · kernel_before=7.2.7-edge-arm64 |
| reboot | ✅ | 50.6 s | warm · up 30 s |

### ✅ UEFI x86 01

`uefi-x86` · **inplace** · image `26.11.0-trunk.62` · 14 ✅ · 0 ❌ · 2 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 236.0 s | nightly · 26.11.0-trunk.62 → 26.11.0-trunk.62 |
| reboot | ✅ | 89.3 s | power-cycle · up 56 s |
| kernel-switch | ✅ | 34.4 s | branch=current · family=x86 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-x86 · kernel_before=6.18.54-current-x86 |
| reboot | ✅ | 239.2 s | power-cycle · 4/4 boots · up 60 s |
| hw-performance | ✅ | 25.8 s | AES 237 · mem 5100 · disk W 19 / R 111 MB/s · 59 °C · 1920 MHz |
| dvfs | ➖ | 23.6 s | schedutil · 480–1920 MHz (peak 1729) · max_khz is single-core turbo, not an all-core target |
| network-iperf | ✅ | 68.3 s | enp1s0 ↑920/↓941 (1GE) · wlan0 ↑31/↓31 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.5 s | 26.11.0-trunk.62 · 6.18.54-current-x86 |
| kernel-switch | ✅ | 181.5 s | branch=edge · family=x86 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-x86 · kernel_before=6.18.54-current-x86 |
| reboot | ✅ | 254.4 s | power-cycle · 4/4 boots · up 60 s |
| hw-performance | ✅ | 25.0 s | AES 235 · mem 4900 · disk W 26 / R 106 MB/s · 59 °C · 1920 MHz |
| dvfs | ➖ | 23.9 s | schedutil · 480–1920 MHz (peak 1680) · max_khz is single-core turbo, not an all-core target |
| network-iperf | ✅ | 62.1 s | enp1s0 ↑912/↓941 (1GE) · wlan0 ↑34/↓33 (Wi-Fi 5) Mbps |
| store-versions | ✅ | 5.9 s | 26.11.0-trunk.62 · 7.2.8-edge-x86 |
| kernel-switch | ✅ | 185.6 s | branch=current · family=x86 · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-x86 · kernel_before=7.2.8-edge-x86 |
| reboot | ✅ | 90.2 s | power-cycle · up 58 s |

**Power** — min 0.80 W · avg 4.07 W · peak 7.90 W · 1237 samples

```mermaid
xychart-beta
    title "Power — UEFI x86 01"
    x-axis "sample" 1 --> 1237
    y-axis "W" 0.5 --> 8.0
    line [3.87, 4.23, 3.42, 4.23, 3.89, 3.33, 4.16, 4.25, 4.49, 3.75, 4.52, 4.76, 4.22, 4.47, 4.31, 4.45, 4.40, 3.86, 3.58, 3.76, 3.87, 4.26, 4.03, 3.99, 4.78, 4.43, 4.44, 4.56, 4.12, 4.10, 3.95, 3.48, 3.29, 3.70, 3.69, 3.81, 4.04, 3.83, 3.72, 4.92]
```

### ✅ ZeroPi 01

`zeropi` · **inplace** · image `26.11.0-trunk.58` · 16 ✅ · 0 ❌ · 0 ⏭️

| Module | Status | Time | Detail |
|:--|:--:|--:|:--|
| upgrade | ✅ | 309.7 s | nightly · 26.11.0-trunk.58 → 26.11.0-trunk.58 |
| reboot | ✅ | 60.7 s | power-cycle · up 26 s |
| kernel-switch | ✅ | 63.1 s | branch=current · family=sunxi · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 162.6 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 39.3 s | AES 25 · mem 1500 · disk W 21 / R 23 MB/s · 44.9 °C · 1296 MHz |
| dvfs | ✅ | 34.3 s | ondemand · 480–1296 MHz (peak 1296) |
| network-iperf | ✅ | 58.3 s | end0 ↑630/↓939 (1GE) Mbps |
| store-versions | ✅ | 7.4 s | 26.11.0-trunk.58 · 6.18.54-current-sunxi |
| kernel-switch | ✅ | 172.6 s | branch=edge · family=sunxi · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-7.2.8-edge-sunxi · kernel_before=6.18.54-current-sunxi |
| reboot | ✅ | 164.6 s | power-cycle · 4/4 boots · up 25 s |
| hw-performance | ✅ | 39.8 s | AES 25 · mem 1600 · disk W 1 / R 23 MB/s · 45.3 °C · 1296 MHz |
| dvfs | ✅ | 36.5 s | ondemand · 480–1296 MHz (peak 1296) |
| network-iperf | ✅ | 47.9 s | end0 ↑632/↓939 (1GE) Mbps |
| store-versions | ✅ | 8.1 s | 26.11.0-trunk.58 · 7.2.8-edge-sunxi |
| kernel-switch | ✅ | 174.1 s | branch=current · family=sunxi · installed=26.11.0-trunk.62 · boot_image=/boot/vmlinuz-6.18.54-current-sunxi · kernel_before=7.2.8-edge-sunxi |
| reboot | ✅ | 58.9 s | power-cycle · up 24 s |

**Power** — min 0.90 W · avg 2.15 W · peak 3.10 W · 1158 samples

```mermaid
xychart-beta
    title "Power — ZeroPi 01"
    x-axis "sample" 1 --> 1158
    y-axis "W" 0.5 --> 3.5
    line [1.98, 2.13, 2.14, 2.07, 2.10, 2.12, 2.53, 2.15, 2.09, 1.81, 2.26, 2.05, 2.03, 2.36, 2.14, 1.97, 2.34, 2.11, 2.24, 2.12, 2.18, 2.24, 2.19, 2.22, 2.10, 2.00, 2.10, 2.21, 2.35, 2.44, 2.09, 2.46, 2.06, 2.39, 2.10, 2.14, 2.09, 2.10, 1.92, 1.95]
```


<!-- FLEET-STOP -->
