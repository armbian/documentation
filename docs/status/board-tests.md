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

**64** boards — **44** passed, **20** failed. Each card is the board's most recent test.

??? failure "Arduino UNO Q 01 — fail"

    `arduino-uno-q` · **inplace** · image `26.11.0-trunk.54` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 61.7 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 51.3 s | warm · up 34 s |
    | kernel-switch | ❌ | 46.5 s | branch=edge · family=qrb2210 · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=7.2.3-edge-qrb2210 |
    | reboot | ✅ | 52.8 s | warm · up 35 s |
    | hw-performance | ✅ | 25.9 s | AES 940 · mem 5100 · disk W 162 / R 223 MB/s · 42.1 °C · 2016 MHz |
    | dvfs | ✅ | 31.6 s | schedutil · 300–2016 MHz (peak 2016) |
    | network-iperf | ✅ | 50.7 s | wlan0 ↑25/↓20 (Wi-Fi 5) · usb0 ↑?/↓? Mbps |
    | store-versions | ✅ | 7.0 s | 26.11.0-trunk.54 · 7.2.3-edge-qrb2210 |

??? success "Banana Pi CM4IO 01 — pass"

    `bananapicm4io` · **inplace** · image `26.8.3` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 17.3 s | — |
    | reboot | ✅ | 44.8 s | power-cycle · up 18 s |
    | kernel-switch | ✅ | 52.2 s | branch=current · family=meson64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-meson64 · kernel_before=6.18.52-current-meson64 |
    | reboot | ✅ | 123.8 s | power-cycle · 4/4 boots · up 18 s |
    | hw-performance | ✅ | 18.4 s | AES 852 · mem 3900 · disk W 35 / R 160 MB/s · 51.9 °C · 2016 MHz |
    | dvfs | ✅ | 18.0 s | ondemand · 1000–1512 MHz (peak 1512) |
    | network-iperf | ❌ | 548.1 s | eth0 ↑938/↓939 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) · wlx00e032c00694 ↑0/↓0 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 11.5 s | 26.8.3 · 6.18.52-current-meson64 |

??? failure "Banana Pi M2 Ultra 01 — fail"

    `bananapim2ultra` · **inplace** · image `26.11.0-trunk.54` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 25.6 s | — |
    | reboot | ✅ | 48.5 s | warm · up 25 s |
    | kernel-switch | ❌ | 66.9 s | branch=current · family=sunxi · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-sunxi |
    | reboot | ✅ | 151.3 s | warm · 4/4 boots · up 21 s |
    | hw-performance | ✅ | 38.5 s | AES 23 · mem 2100 · disk W 1 / R 42 MB/s · 51.1 °C · 1200 MHz |
    | dvfs | ✅ | 34.0 s | ondemand · 720–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 71.8 s | end0 ↑805/↓942 (1GE) · wlan0 ↑30/↓31 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 8.4 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi |

??? success "Banana Pi M2Pro 01 — pass"

    `bananapim2pro` · **inplace** · image `26.11.0-trunk.52` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 236.4 s | nightly · 26.11.0-trunk.52 → 26.11.0-trunk.56 |
    | reboot | ✅ | 50.6 s | power-cycle · up 23 s |
    | kernel-switch | ✅ | 37.9 s | branch=current · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=6.18.53-current-meson64 |
    | reboot | ✅ | 144.3 s | power-cycle · 4/4 boots · up 23 s |
    | hw-performance | ✅ | 34.2 s | AES 976 · mem 5300 · disk W 12 / R 15 MB/s · 50.4 °C · 2100 MHz |
    | dvfs | ✅ | 19.7 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 56.5 s | end0 ↑938/↓939 (1GE) · wlx60fb00480eb0 ↑171/↓202 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.3 s | 26.11.0-trunk.56 · 6.18.53-current-meson64 |
    | kernel-switch | ✅ | 134.7 s | branch=edge · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-meson64 · kernel_before=6.18.53-current-meson64 |
    | reboot | ✅ | 162.6 s | power-cycle · 4/4 boots · up 23 s |
    | hw-performance | ✅ | 42.5 s | AES 980 · mem 5300 · disk W 13 / R 15 MB/s · 50.6 °C · 2100 MHz |
    | dvfs | ✅ | 19.9 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 56.8 s | end0 ↑939/↓939 (1GE) · wlx60fb00480eb0 ↑189/↓222 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.1 s | 26.11.0-trunk.56 · 7.2.7-edge-meson64 |
    | kernel-switch | ✅ | 132.6 s | branch=current · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=7.2.7-edge-meson64 |
    | reboot | ✅ | 49.3 s | power-cycle · up 22 s |

??? success "Banana Pi M5 01 — pass"

    `bananapim5` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 304.0 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 169.2 s | warm · up 154 s |
    | kernel-switch | ✅ | 49.8 s | branch=current · family=meson64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-meson64 · kernel_before=6.18.52-current-meson64 |
    | reboot | ✅ | 160.1 s | warm · up 145 s |
    | hw-performance | ✅ | 38.5 s | AES 977 · mem 5300 · disk W 9 / R 16 MB/s · 55.6 °C · 2100 MHz |
    | dvfs | ✅ | 21.3 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 103.1 s | end0 ↑940/↓941 (1GE) · wlx000f13960190 ↑30/↓24 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 5.3 s | 26.11.0-trunk.54 · 6.18.52-current-meson64 |

??? success "Banana Pi M7 01 — pass"

    `bananapim7` · **inplace** · image `26.11.0-trunk.54` · 22 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 50.1 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.56 |
    | reboot | ✅ | 50.2 s | power-cycle · up 15 s |
    | kernel-switch | ✅ | 19.1 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 103.2 s | power-cycle · 4/4 boots · up 15 s |
    | hw-performance | ✅ | 13.4 s | AES 1255 · mem 13700 · disk W 927 / R 1559 MB/s · 61.9 °C · 1800 MHz |
    | dvfs | ✅ | 17.1 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 28.3 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.1 s | 26.11.0-trunk.56 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 51.0 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 845.0 s | power-cycle · 3/4 boots · up 98 s |
    | hw-performance | ✅ | 14.1 s | AES 1253 · mem 9900 · disk W 1062 / R 1558 MB/s · 63.8 °C · 1800 MHz |
    | dvfs | ✅ | 14.7 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 30.8 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.56 · 6.18.53-current-rockchip64 |
    | kernel-switch | ✅ | 41.9 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-rockchip64 · kernel_before=6.18.53-current-rockchip64 |
    | reboot | ✅ | 437.0 s | power-cycle · 4/4 boots · up 97 s |
    | hw-performance | ✅ | 13.7 s | AES 1255 · mem 8000 · disk W 880 / R 1607 MB/s · 64.7 °C · 1800 MHz |
    | dvfs | ✅ | 15.0 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 29.0 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.56 · 7.2.7-edge-rockchip64 |
    | kernel-switch | ✅ | 36.1 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=7.2.7-edge-rockchip64 |
    | reboot | ✅ | 42.5 s | power-cycle · up 15 s |

    **Power** — min 1.00 W · avg 5.85 W · peak 12.20 W · 1480 samples

    ```mermaid
    xychart-beta
        title "Power — Banana Pi M7 01"
        x-axis "sample" 1 --> 1480
        y-axis "W" 0.5 --> 12.5
        line [5.65, 5.23, 5.68, 6.70, 5.74, 6.19, 6.34, 5.86, 5.65, 5.54, 6.23, 5.50, 5.50, 5.50, 5.50, 5.50, 5.50, 5.51, 5.51, 5.77, 5.49, 5.61, 5.48, 6.29, 5.50, 5.49, 6.79, 6.74, 6.04, 5.50, 6.25, 5.50, 5.88, 5.50, 5.62, 5.89, 5.45, 7.05, 6.55, 6.72]
    ```

??? success "Banana Pi R3 Mini 01 — pass"

    `bananapir3mini` · **inplace** · image `26.11.0-trunk` · 4 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 17.4 s | — |
    | reboot | ✅ | 60.7 s | power-cycle · up 31 s |
    | hw-performance | ✅ | 26.7 s | AES 935 · mem 3100 · disk W 78 / R 91 MB/s · 61.5 °C · None MHz |
    | dvfs | ➖ | 2.9 s | no cpufreq |
    | network-iperf | ✅ | 113.2 s | eth0 ↑938/↓919 (1GE) · eth1 ↑938/↓908 (1GE) · wlan0 ↑27/↓31 (Wi-Fi 6) · wlan1 ↑453/↓381 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk · 6.18.52-current-filogic-mt7986 |

    **Power** — min 3.00 W · avg 7.73 W · peak 13.40 W · 190 samples

    ```mermaid
    xychart-beta
        title "Power — Banana Pi R3 Mini 01"
        x-axis "sample" 1 --> 190
        y-axis "W" 2.5 --> 13.5
        line [5.80, 5.80, 5.96, 6.24, 6.25, 6.10, 5.80, 6.00, 4.95, 3.50, 3.60, 4.00, 5.60, 8.24, 8.74, 8.70, 8.78, 8.50, 8.18, 8.04, 8.30, 8.22, 8.20, 8.36, 8.40, 8.40, 8.30, 8.20, 8.40, 8.40, 8.48, 9.62, 9.00, 8.52, 8.46, 10.84, 12.90, 11.68, 9.14, 9.00]
    ```

??? success "BananaPi BPI-F3 01 — pass"

    `bananapif3` · **inplace** · image `26.11.0-trunk.51` · 6 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 179.2 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 46.1 s | power-cycle · up 17 s |
    | hw-performance | ✅ | 22.9 s | AES 30 · mem 3400 · disk W 62 / R 83 MB/s · 59 °C · 1800 MHz |
    | dvfs | ✅ | 23.1 s | performance · 614–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 88.8 s | eth0 ↑939/↓939 (1GE) · wlan0 ↑295/↓290 (Wi-Fi 6) · wlan1 ↑268/↓233 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.2 s | 26.11.0-trunk.54 · 6.18.52-current-spacemit |

??? failure "BigTreeTech CB1 01 — fail"

    `bigtreetech-cb1` · **inplace** · image `26.11.0-trunk.54` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.62 · reachable=False · port=22 |

    **Power** — min 2.10 W · avg 2.10 W · peak 2.10 W · 44 samples

    ```mermaid
    xychart-beta
        title "Power — BigTreeTech CB1 01"
        x-axis "sample" 1 --> 44
        y-axis "W" 2.0 --> 2.5
        line [2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10, 2.10]
    ```

??? failure "Clearfog Pro 01 — fail"

    `clearfogpro` · **inplace** · image `26.11.0-trunk.54` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 62.8 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 39.2 s | warm · up 22 s |
    | kernel-switch | ❌ | 39.7 s | branch=current · family=mvebu · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-mvebu |
    | reboot | ✅ | 37.5 s | warm · up 20 s |
    | hw-performance | ✅ | 41.4 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 63.2 °C · None MHz |
    | dvfs | ➖ | 2.9 s | no cpufreq |
    | network-iperf | ✅ | 38.5 s | lan2 ↑936/↓936 Mbps |
    | store-versions | ✅ | 6.0 s | 26.11.0-trunk.54 · 6.18.52-current-mvebu |

??? failure "Cubie A5E 01 — fail"

    `radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.54` · 10 ✅ · 3 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 303.3 s | — |
    | reboot | ✅ | 66.9 s | power-cycle · up 32 s |
    | kernel-switch | ❌ | 119.2 s | branch=current · phase=install · dpkg_state=absent |
    | reboot | ✅ | 180.2 s | power-cycle · 4/4 boots · up 32 s |
    | hw-performance | ✅ | 42.8 s | AES 358 · mem 2000 · disk W 1 / R 23 MB/s · 65.5 °C · None MHz |
    | dvfs | ➖ | 2.9 s | no cpufreq |
    | network-iperf | ✅ | 96.9 s | end0 ↑820/↓941 (1GE) · end1 ↑941/↓941 (1GE) · wlan0 ↑120/↓127 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 6.1 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi64 |
    | kernel-switch | ❌ | 119.3 s | branch=edge · phase=install · dpkg_state=absent |
    | reboot | ✅ | 179.3 s | power-cycle · 4/4 boots · up 32 s |
    | hw-performance | ✅ | 42.8 s | AES 358 · mem 2000 · disk W 21 / R 23 MB/s · 65.2 °C · None MHz |
    | dvfs | ➖ | 3.3 s | no cpufreq |
    | network-iperf | ✅ | 93.5 s | end0 ↑820/↓941 (1GE) · end1 ↑939/↓938 (1GE) · wlan0 ↑120/↓129 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 6.8 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi64 |
    | kernel-switch | ❌ | 118.8 s | branch=current · phase=install · dpkg_state=absent |
    | reboot | ✅ | 64.1 s | power-cycle · up 31 s |

    **Power** — min 1.70 W · avg 3.51 W · peak 5.00 W · 1165 samples

    ```mermaid
    xychart-beta
        title "Power — Cubie A5E 01"
        x-axis "sample" 1 --> 1165
        y-axis "W" 1.5 --> 5.5
        line [3.39, 3.56, 3.61, 3.58, 3.57, 3.54, 3.76, 4.10, 3.64, 3.24, 3.31, 3.63, 3.55, 3.52, 3.27, 3.44, 3.61, 3.52, 2.90, 3.63, 3.55, 3.73, 3.78, 3.61, 3.62, 3.58, 3.59, 3.21, 3.34, 3.21, 3.08, 3.66, 3.58, 3.65, 3.63, 3.64, 3.58, 3.59, 3.54, 2.81]
    ```

??? failure "Cubietruck 01 — fail"

    `cubietruck` · **inplace** · image `26.11.0-trunk.54` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 135.4 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 60.4 s | warm · up 42 s |
    | kernel-switch | ❌ | 90.8 s | branch=current · family=sunxi · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-sunxi |
    | reboot | ✅ | 60.8 s | warm · up 41 s |
    | hw-performance | ✅ | 60.3 s | AES 18 · mem 1700 · disk W 13 / R 22 MB/s · 48.3 °C · 960 MHz |
    | dvfs | ✅ | 56.4 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 95.7 s | end0 ↑706/↓860 (1GE) · wlan0 ↑21/↓24 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 11.8 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi |

??? failure "Cubox i2eX/i4 01 — fail"

    `cubox-i` · **inplace** · image `26.11.0-trunk.54` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 108.4 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 56.4 s | power-cycle · up 29 s |
    | kernel-switch | ❌ | 72.0 s | branch=current · family=imx6 · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-imx6 |
    | reboot | ✅ | 56.6 s | power-cycle · up 30 s |
    | hw-performance | ✅ | 46.8 s | AES 26 · mem 742 · disk W 19 / R 20 MB/s · 50.3 °C · 996 MHz |
    | dvfs | ✅ | 40.3 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 113.2 s | end0 ↑395/↓226 (1GE) · wlan0 ↑19/↓9 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 8.6 s | 26.11.0-trunk.54 · 6.18.52-current-imx6 |

??? success "Espressobin 01 — pass"

    `espressobin` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 32.5 s | AES 369 · mem 2000 · disk W 36 / R 131 MB/s · None °C · 800 MHz |
    | dvfs | ✅ | 33.7 s | ondemand · 200–800 MHz (peak 800) |
    | network-iperf | ✅ | 38.1 s | lan0 ↑936/↓737 (1GE) Mbps |
    | store-versions | ✅ | 7.2 s | 26.8.3 · 6.18.44-current-mvebu64 |

??? failure "Helios4 01 — fail"

    `helios4` · **inplace** · image `26.11.0-trunk.54` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 52.9 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 117.2 s | warm · up 102 s |
    | kernel-switch | ❌ | 34.2 s | branch=current · family=mvebu · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-mvebu |
    | reboot | ✅ | 117.6 s | warm · up 102 s |
    | hw-performance | ✅ | 36.4 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 56.1 °C · None MHz |
    | dvfs | ➖ | 2.3 s | no cpufreq |
    | network-iperf | ✅ | 34.2 s | end1 ↑568/↓477 (1GE) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.54 · 6.18.52-current-mvebu |

??? failure "Inovato Quadra 01 — fail"

    `inovato-quadra` · **inplace** · image `26.8.0-trunk.314` · 2 ✅ · 4 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 241.7 s | nightly · 26.8.0-trunk.314 → 26.8.0-trunk.314 |
    | reboot | ❌ | 213.8 s | power-cycle |
    | hw-performance | ✅ | 154.8 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 7.2 s | no cpufreq |
    | network-iperf | ⏭️ | 19.6 s | no iperf3 on board |
    | restore-stable | ❌ | 7.1 s | stable |
    | reboot | ❌ | 233.6 s | power-cycle |
    | store-versions | ❌ | 13.3 s | — |

??? success "Khadas VIM1 01 — pass"

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

??? success "Khadas VIM2 01 — pass"

    `khadas-vim2` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 263.4 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 35.3 s | warm · up 17 s |
    | hw-performance | ✅ | 24.2 s | AES 652 · mem 3600 · disk W 42 / R 149 MB/s · 56 °C · 1512 MHz |
    | dvfs | ✅ | 26.0 s | ondemand · 500–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 72.2 s | eth0 ↑904/↓847 (1GE) · wlan0 ↑106/↓102 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 136.8 s | stable |
    | reboot | ✅ | 35.4 s | warm · up 17 s |
    | store-versions | ✅ | 5.7 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? success "Khadas VIM3 01 — pass"

    `khadas-vim3` · **inplace** · image `26.8.3` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 337.0 s | nightly · 26.8.3 → 26.11.0-trunk.35 |
    | reboot | ✅ | 38.9 s | warm · up 20 s |
    | hw-performance | ✅ | 31.1 s | AES 852 · mem 3900 · disk W 12 / R 22 MB/s · 45.2 °C · 2016 MHz |
    | dvfs | ✅ | 17.7 s | ondemand · 1000–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 54.1 s | end0 ↑940/↓941 (1GE) · wlan0 ↑40/↓39 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 103.1 s | stable |
    | reboot | ✅ | 38.1 s | warm · up 20 s |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.35 · 6.18.44-current-meson64 |

??? success "Khadas VIM4 01 — pass"

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

??? success "Mekotronics R58HD 01 — pass"

    `mekotronics-r58hd` · **inplace** · image `26.11.0-trunk.51` · 6 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 82.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 44.5 s | power-cycle · up 14 s |
    | hw-performance | ✅ | 14.1 s | AES 1300 · mem 9300 · disk W 248 / R 289 MB/s · 51.8 °C · 1800 MHz |
    | dvfs | ✅ | 16.7 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 51.7 s | end0 ↑925/↓919 (1GE) · enP3p49s0 ↑938/↓909 (1GE) Mbps |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |

    **Power** — min 3.60 W · avg 6.10 W · peak 11.80 W · 180 samples

    ```mermaid
    xychart-beta
        title "Power — Mekotronics R58HD 01"
        x-axis "sample" 1 --> 180
        y-axis "W" 3.5 --> 12.0
        line [5.20, 5.20, 5.55, 6.22, 6.80, 6.86, 5.90, 6.28, 6.45, 6.80, 6.55, 5.94, 7.05, 10.22, 6.70, 6.40, 6.80, 6.40, 5.47, 5.38, 4.75, 3.96, 4.75, 5.60, 5.85, 6.00, 5.85, 5.80, 8.80, 9.20, 5.45, 5.80, 5.40, 5.40, 5.60, 5.52, 5.20, 5.40, 5.70, 5.52]
    ```

??? failure "Mekotronics R58S2 01 — fail"

    `mekotronics-r58s2` · **inplace** · image `26.8.3` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 222.3 s | — |
    | reboot | ❌ | 208.1 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "NanoPi Fire3 01 — pass"

    `nanopifire3` · **inplace** · image `26.11.0-trunk.51` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 418.0 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 53.7 s | power-cycle · up 23 s |
    | kernel-switch | ✅ | 69.4 s | branch=edge · family=s5p6818 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-7.2.6-edge-s5p6818 · kernel_before=7.2.6-edge-s5p6818 |
    | reboot | ✅ | 52.6 s | power-cycle · up 17 s |
    | hw-performance | ✅ | 43.1 s | AES 373 · mem 2000 · disk W 20 / R 22 MB/s · 68 °C · None MHz |
    | dvfs | ➖ | 2.9 s | no cpufreq |
    | network-iperf | ✅ | 43.1 s | eth0 ↑821/↓833 (1GE) Mbps |
    | store-versions | ✅ | 6.1 s | 26.11.0-trunk.54 · 7.2.6-edge-s5p6818 |

??? success "NanoPi K2 01 — pass"

    `nanopik2-s905` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 293.8 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 44.0 s | warm · up 29 s |
    | kernel-switch | ✅ | 40.1 s | branch=current · family=meson64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-meson64 · kernel_before=6.18.52-current-meson64 |
    | reboot | ✅ | 32.9 s | warm · up 18 s |
    | hw-performance | ✅ | 31.3 s | AES 51 · mem 3700 · disk W 11 / R 41 MB/s · 62 °C · 2016 MHz |
    | dvfs | ✅ | 21.4 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 73.6 s | end0 ↑936/↓941 (1GE) · wlan0 ↑12/↓23 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 5.7 s | 26.11.0-trunk.54 · 6.18.52-current-meson64 |

??? success "NanoPi M4V2 01 — pass"

    `nanopim4v2` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 281.3 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 60.7 s | power-cycle · up 30 s |
    | kernel-switch | ✅ | 30.2 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 55.7 s | power-cycle · up 28 s |
    | hw-performance | ✅ | 22.0 s | AES 1020 · mem 6600 · disk W 54 / R 28 MB/s · 49.4 °C · 1416 MHz |
    | dvfs | ✅ | 24.4 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 105.0 s | end0 ↑937/↓786 (1GE) · wlan0 ↑138/↓155 (Wi-Fi 5) · wlx803f5d16af63 ↑140/↓203 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |

    **Power** — min 3.20 W · avg 7.60 W · peak 14.10 W · 472 samples

    ```mermaid
    xychart-beta
        title "Power — NanoPi M4V2 01"
        x-axis "sample" 1 --> 472
        y-axis "W" 3.0 --> 14.5
        line [5.93, 6.46, 6.13, 5.84, 6.73, 5.87, 7.28, 6.94, 7.26, 7.71, 7.81, 6.36, 6.55, 5.93, 6.05, 6.15, 8.69, 6.83, 7.47, 7.45, 6.60, 5.71, 6.18, 8.71, 7.90, 7.97, 6.42, 5.09, 6.62, 9.16, 7.45, 10.88, 10.22, 9.53, 9.17, 9.24, 10.08, 9.36, 10.88, 11.01]
    ```

??? failure "NanoPi M5 01 — fail"

    `nanopi-m5` · **inplace** · image `26.11.0-trunk.54` · 15 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 31.8 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 132.3 s | power-cycle · up 109 s |
    | kernel-switch | ✅ | 22.7 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 139.6 s | power-cycle · up 110 s |
    | hw-performance | ✅ | 17.9 s | AES 1279 · mem 8100 · disk W 68 / R 77 MB/s · 42.5 °C · 2016 MHz |
    | dvfs | ✅ | 18.8 s | ondemand · 2016–2016 MHz (peak 2208) |
    | network-iperf | ✅ | 88.5 s | end0 ↑449/↓619 (1GE) · end1 ↑919/↓912 (1GE) · wlx44334c47dec3 ↑39/↓10 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ❌ | 14.1 s | branch=current · phase=install · dpkg_state=absent |
    | reboot | ✅ | 132.7 s | power-cycle · up 109 s |
    | hw-performance | ✅ | 17.7 s | AES 1279 · mem 8000 · disk W 68 / R 77 MB/s · 42.5 °C · 2016 MHz |
    | dvfs | ✅ | 19.6 s | ondemand · 2016–2016 MHz (peak 2208) |
    | network-iperf | ✅ | 79.8 s | end0 ↑939/↓939 (1GE) · end1 ↑939/↓939 (1GE) · wlx44334c47dec3 ↑38/↓16 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 4.2 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 22.6 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 130.9 s | power-cycle · up 107 s |

    **Power** — min 0.60 W · avg 4.19 W · peak 7.30 W · 712 samples

    ```mermaid
    xychart-beta
        title "Power — NanoPi M5 01"
        x-axis "sample" 1 --> 712
        y-axis "W" 0.5 --> 7.5
        line [4.98, 5.84, 3.91, 4.23, 3.92, 3.90, 3.90, 3.92, 4.74, 2.52, 3.64, 4.17, 3.84, 3.90, 3.83, 4.58, 5.84, 4.20, 4.32, 4.24, 4.07, 4.52, 2.97, 4.34, 3.97, 3.94, 3.90, 4.24, 5.29, 4.65, 4.39, 4.39, 4.23, 4.76, 4.02, 3.49, 4.30, 3.90, 3.90, 3.93]
    ```

??? success "NanoPi M6 01 — pass"

    `nanopi-m6` · **inplace** · image `26.8.3` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 139.8 s | nightly · 26.8.3 → 26.11.0-trunk.54 |
    | reboot | ✅ | 47.8 s | power-cycle · up 23 s |
    | kernel-switch | ✅ | 20.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 52.8 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 17.1 s | AES 1269 · mem 13600 · disk W 51 / R 78 MB/s · 48.1 °C · 1800 MHz |
    | dvfs | ✅ | 17.7 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 61.5 s | lan ↑908/↓937 (1GE) · wlP3p49s0 ↑3/↓27 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 95.6 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 52.6 s | power-cycle · up 21 s |
    | hw-performance | ✅ | 19.5 s | AES 1214 · mem 9900 · disk W 47 / R 58 MB/s · 49.9 °C · 1800 MHz |
    | dvfs | ✅ | 16.1 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 57.3 s | lan ↑937/↓892 (1GE) · wlP3p49s0 ↑127/↓185 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 66.5 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 53.3 s | power-cycle · up 20 s |

    **Power** — min 0.80 W · avg 3.82 W · peak 10.30 W · 569 samples

    ```mermaid
    xychart-beta
        title "Power — NanoPi M6 01"
        x-axis "sample" 1 --> 569
        y-axis "W" 0.5 --> 10.5
        line [3.32, 3.74, 3.46, 3.06, 3.75, 4.60, 3.69, 3.54, 3.19, 2.22, 4.24, 3.91, 2.94, 2.34, 4.08, 4.29, 5.25, 3.50, 3.58, 3.52, 3.47, 3.53, 3.62, 3.77, 2.96, 3.84, 2.01, 4.19, 5.24, 6.44, 5.06, 4.45, 4.76, 3.92, 4.65, 4.39, 4.60, 4.23, 2.51, 3.38]
    ```

??? success "NanoPi Neo 2 Black 01 — pass"

    `nanopineo2black` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 214.1 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 47.2 s | power-cycle · up 21 s |
    | kernel-switch | ✅ | 45.5 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-sunxi64 · kernel_before=6.18.52-current-sunxi64 |
    | reboot | ✅ | 48.9 s | power-cycle · up 19 s |
    | hw-performance | ✅ | 32.3 s | AES 575 · mem 3300 · disk W 18 / R 23 MB/s · 68.9 °C · 1368 MHz |
    | dvfs | ✅ | 23.6 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 34.9 s | end0 ↑796/↓923 (1GE) Mbps |
    | store-versions | ✅ | 5.4 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi64 |

??? success "NanoPi Neo 3 01 — pass"

    `nanopineo3` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 286.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 52.1 s | power-cycle · up 26 s |
    | kernel-switch | ✅ | 58.8 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 51.4 s | power-cycle · up 25 s |
    | hw-performance | ✅ | 28.4 s | AES 551 · mem 2300 · disk W 52 / R 63 MB/s · 81.5 °C · 1296 MHz |
    | dvfs | ✅ | 30.2 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 185.2 s | end0 ↑919/↓941 (1GE) · wlx7cdd905518f9 ↑29/↓19 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 6.4 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |

??? success "NanoPi R6S 01 — pass"

    `nanopi-r6s` · **inplace** · image `26.11.0-trunk.51` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 72.7 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 38.2 s | power-cycle · up 14 s |
    | kernel-switch | ✅ | 18.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 35.1 s | power-cycle · up 11 s |
    | hw-performance | ✅ | 14.3 s | AES 1280 · mem 15300 · disk W 213 / R 274 MB/s · 37.9 °C · 1800 MHz |
    | dvfs | ✅ | 17.0 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 29.1 s | lan2 ↑939/↓939 (1GE) Mbps |
    | store-versions | ✅ | 4.2 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 52.0 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 33.8 s | power-cycle · up 10 s |
    | hw-performance | ✅ | 15.5 s | AES 1278 · mem 10300 · disk W 139 / R 155 MB/s · 38.8 °C · 1800 MHz |
    | dvfs | ✅ | 15.3 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 28.6 s | lan2 ↑938/↓926 (1GE) Mbps |
    | store-versions | ✅ | 5.0 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 46.7 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 33.7 s | power-cycle · up 10 s |

    **Power** — min 2.20 W · avg 4.34 W · peak 9.30 W · 357 samples

    ```mermaid
    xychart-beta
        title "Power — NanoPi R6S 01"
        x-axis "sample" 1 --> 357
        y-axis "W" 2.0 --> 9.5
        line [3.02, 4.39, 4.72, 4.70, 4.36, 4.42, 4.66, 3.59, 3.77, 4.50, 4.70, 4.27, 2.86, 3.15, 4.66, 3.88, 6.66, 3.51, 3.51, 3.63, 3.27, 3.82, 4.32, 4.56, 4.53, 3.11, 3.49, 5.48, 4.63, 6.63, 4.86, 4.17, 4.31, 4.03, 4.94, 5.09, 5.29, 4.89, 3.93, 4.81]
    ```

??? failure "NanoPi R76S 01 — fail"

    `nanopi-r76s` · **inplace** · image `26.11.0-trunk.27` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.77 · reachable=False · port=22 |

??? failure "Odroid C1 01 — fail"

    `odroidc1` · **inplace** · image `26.8.0-trunk.314` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.27 · reachable=False · port=22 |

??? success "Odroid C2 01 — pass"

    `odroidc2` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 205.8 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.56 |
    | reboot | ✅ | 33.7 s | warm · up 17 s |
    | kernel-switch | ✅ | 37.4 s | branch=current · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=6.18.53-current-meson64 |
    | reboot | ✅ | 114.9 s | warm · 4/4 boots · up 15 s |
    | hw-performance | ✅ | 22.4 s | AES 51 · mem 3500 · disk W 32 / R 152 MB/s · 45 °C · 1536 MHz |
    | dvfs | ✅ | 22.1 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 34.0 s | end0 ↑940/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.56 · 6.18.53-current-meson64 |
    | kernel-switch | ✅ | 114.9 s | branch=edge · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-meson64 · kernel_before=6.18.53-current-meson64 |
    | reboot | ✅ | 117.7 s | warm · 4/4 boots · up 17 s |
    | hw-performance | ✅ | 22.5 s | AES 51 · mem 3500 · disk W 33 / R 152 MB/s · 47 °C · 1536 MHz |
    | dvfs | ✅ | 22.3 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 31.2 s | end0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 5.1 s | 26.11.0-trunk.56 · 7.2.7-edge-meson64 |
    | kernel-switch | ✅ | 113.0 s | branch=current · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=7.2.7-edge-meson64 |
    | reboot | ✅ | 33.2 s | warm · up 16 s |

??? success "Odroid C4 01 — pass"

    `odroidc4` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 187.8 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.56 |
    | reboot | ✅ | 47.5 s | power-cycle · up 17 s |
    | kernel-switch | ✅ | 30.0 s | branch=current · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=6.18.53-current-meson64 |
    | reboot | ✅ | 129.0 s | power-cycle · 4/4 boots · up 17 s |
    | hw-performance | ✅ | 21.7 s | AES 980 · mem 5200 · disk W 31 / R 78 MB/s · 41.5 °C · 2100 MHz |
    | dvfs | ✅ | 19.1 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 57.2 s | end0 ↑938/↓871 (1GE) · wlx24050fdd332b ↑118/↓127 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.56 · 6.18.53-current-meson64 |
    | kernel-switch | ✅ | 108.2 s | branch=edge · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-meson64 · kernel_before=6.18.53-current-meson64 |
    | reboot | ✅ | 131.5 s | power-cycle · 4/4 boots · up 17 s |
    | hw-performance | ✅ | 21.8 s | AES 980 · mem 5200 · disk W 30 / R 77 MB/s · 41.4 °C · 2100 MHz |
    | dvfs | ✅ | 19.7 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 57.5 s | end0 ↑891/↓917 (1GE) · wlx24050fdd332b ↑102/↓129 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 4.3 s | 26.11.0-trunk.56 · 7.2.7-edge-meson64 |
    | kernel-switch | ✅ | 105.5 s | branch=current · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=7.2.7-edge-meson64 |
    | reboot | ✅ | 50.6 s | power-cycle · up 17 s |

    **Power** — min 1.00 W · avg 3.47 W · peak 5.20 W · 805 samples

    ```mermaid
    xychart-beta
        title "Power — Odroid C4 01"
        x-axis "sample" 1 --> 805
        y-axis "W" 0.5 --> 5.5
        line [3.32, 3.49, 3.52, 3.45, 3.50, 3.62, 3.48, 3.50, 2.54, 3.61, 3.40, 3.28, 3.54, 3.27, 3.12, 2.91, 3.69, 3.82, 3.65, 4.34, 3.76, 3.65, 3.61, 3.66, 3.52, 3.41, 3.50, 3.42, 2.50, 3.34, 3.66, 3.40, 3.66, 4.19, 3.83, 3.75, 3.59, 3.61, 3.39, 2.36]
    ```

??? success "Odroid M1 01 — pass"

    `odroidm1` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 143.0 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.56 |
    | reboot | ✅ | 55.9 s | power-cycle · up 24 s |
    | kernel-switch | ✅ | 31.5 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip64 · kernel_before=6.18.53-current-rockchip64 |
    | reboot | ✅ | 137.8 s | power-cycle · 4/4 boots · up 24 s |
    | hw-performance | ✅ | 17.0 s | AES 916 · mem 5100 · disk W 1025 / R 1012 MB/s · 35.6 °C · 1992 MHz |
    | dvfs | ✅ | 20.9 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 58.9 s | eth0 ↑556/↓941 (1GE) · wlx40a5eff39254 ↑207/↓227 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.56 · 6.18.53-current-rockchip64 |
    | kernel-switch | ✅ | 86.1 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-rockchip64 · kernel_before=6.18.53-current-rockchip64 |
    | reboot | ✅ | 142.2 s | power-cycle · 4/4 boots · up 24 s |
    | hw-performance | ✅ | 17.8 s | AES 915 · mem 5100 · disk W 1047 / R 1025 MB/s · 35.6 °C · 1992 MHz |
    | dvfs | ✅ | 22.8 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 59.2 s | eth0 ↑941/↓941 (1GE) · wlx40a5eff39254 ↑207/↓221 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.56 · 7.2.7-edge-rockchip64 |
    | kernel-switch | ✅ | 86.9 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip64 · kernel_before=7.2.7-edge-rockchip64 |
    | reboot | ✅ | 57.7 s | power-cycle · up 22 s |

    **Power** — min 0.60 W · avg 6.39 W · peak 11.50 W · 752 samples

    ```mermaid
    xychart-beta
        title "Power — Odroid M1 01"
        x-axis "sample" 1 --> 752
        y-axis "W" 0.5 --> 12.0
        line [6.06, 7.28, 6.54, 5.93, 7.77, 6.90, 5.38, 6.06, 6.65, 6.51, 5.99, 7.35, 6.07, 7.15, 5.89, 6.42, 6.53, 5.86, 5.73, 5.95, 6.42, 7.82, 6.59, 5.83, 5.54, 7.09, 6.72, 6.21, 6.08, 7.16, 6.88, 5.63, 5.77, 6.23, 6.09, 7.57, 5.96, 6.26, 5.44, 6.43]
    ```

??? success "Odroid N2 01 — pass"

    `odroidn2` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 143.2 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.56 |
    | reboot | ✅ | 58.9 s | power-cycle · up 29 s |
    | kernel-switch | ✅ | 24.5 s | branch=current · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=6.18.53-current-meson64 |
    | reboot | ✅ | 169.1 s | power-cycle · 4/4 boots · up 25 s |
    | hw-performance | ✅ | 19.0 s | AES 1085 · mem 4900 · disk W 26 / R 135 MB/s · 38.1 °C · 1992 MHz |
    | dvfs | ✅ | 17.1 s | performance · 1000–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 29.1 s | end0 ↑940/↓941 (1GE) Mbps |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.56 · 6.18.53-current-meson64 |
    | kernel-switch | ✅ | 78.8 s | branch=edge · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-meson64 · kernel_before=6.18.53-current-meson64 |
    | reboot | ✅ | 172.0 s | power-cycle · 4/4 boots · up 25 s |
    | hw-performance | ✅ | 20.5 s | AES 1085 · mem 4900 · disk W 26 / R 137 MB/s · 38.1 °C · 1992 MHz |
    | dvfs | ✅ | 18.3 s | performance · 1000–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 31.5 s | end0 ↑940/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.56 · 7.2.7-edge-meson64 |
    | kernel-switch | ✅ | 79.3 s | branch=current · family=meson64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-meson64 · kernel_before=7.2.7-edge-meson64 |
    | reboot | ✅ | 63.0 s | power-cycle · up 29 s |

    **Power** — min 1.00 W · avg 3.67 W · peak 9.80 W · 748 samples

    ```mermaid
    xychart-beta
        title "Power — Odroid N2 01"
        x-axis "sample" 1 --> 748
        y-axis "W" 0.5 --> 10.0
        line [4.02, 4.45, 3.95, 3.78, 4.31, 3.88, 3.47, 3.09, 3.50, 3.71, 2.80, 3.47, 3.31, 3.37, 3.65, 2.98, 2.99, 4.18, 5.73, 3.38, 3.81, 3.81, 4.13, 3.78, 3.00, 3.23, 4.00, 3.07, 3.14, 2.73, 4.16, 4.73, 4.45, 3.41, 3.63, 4.12, 3.95, 3.75, 2.05, 3.75]
    ```

??? failure "Odroid XU4 01 — fail"

    `odroidxu4` · **inplace** · image `26.11.0-trunk.54` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 64.1 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 56.6 s | power-cycle · up 31 s |
    | kernel-switch | ❌ | 43.2 s | branch=current · family=odroidxu4 · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.6.155-current-odroidxu4 |
    | reboot | ✅ | 59.0 s | power-cycle · up 33 s |
    | hw-performance | ✅ | 38.7 s | AES 71 · mem 4900 · disk W 2 / R 55 MB/s · 61 °C · 1400 MHz |
    | dvfs | ✅ | 29.9 s | ondemand · 600–1400 MHz (peak 2000) |
    | network-iperf | ✅ | 38.7 s | enx001e0636e380 ↑923/↓941 (1GE) Mbps |
    | store-versions | ✅ | 6.2 s | 26.11.0-trunk.54 · 6.6.155-current-odroidxu4 |

??? failure "Orange Pi 3 01 — fail"

    `orangepi3` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.41 · reachable=False · port=22 |

??? failure "Orange Pi 5 01 — fail"

    `orangepi5` · **inplace** · image `26.8.3` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 119.6 s | nightly · 26.8.3 → 26.11.0-trunk.35 |
    | reboot | ✅ | 77.4 s | power-cycle · up 51 s |
    | hw-performance | ✅ | 17.3 s | AES 1316 · mem 14200 · disk W 54 / R 66 MB/s · 42.5 °C · 1800 MHz |
    | dvfs | ✅ | 16.7 s | ondemand · 1800–1800 MHz (peak 2352) |
    | network-iperf | ✅ | 28.5 s | end1 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 68.0 s | stable |
    | reboot | ❌ | 205.8 s | power-cycle |
    | store-versions | ⏭️ | 0.0 s | — |

    **Power** — min 1.70 W · avg 2.91 W · peak 8.90 W · 213 samples

??? success "Orange Pi 5 Plus 01 — pass"

    `orangepi5-plus` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 23.6 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 59.5 s | power-cycle · up 33 s |
    | kernel-switch | ✅ | 21.4 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 53.7 s | power-cycle · up 28 s |
    | hw-performance | ✅ | 17.3 s | AES 1255 · mem 15200 · disk W 53 / R 62 MB/s · 55.5 °C · 1800 MHz |
    | dvfs | ✅ | 16.3 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 53.8 s | enP3p49s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑545/↓417 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 3.7 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 95.7 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 51.0 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 18.3 s | AES 1252 · mem 6000 · disk W 45 / R 57 MB/s · 57.3 °C · 1800 MHz |
    | dvfs | ✅ | 15.5 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 61.1 s | enP3p49s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑157/↓68 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 4.3 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 66.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 61.0 s | power-cycle · up 28 s |

    **Power** — min 0.60 W · avg 6.29 W · peak 13.60 W · 495 samples

    ```mermaid
    xychart-beta
        title "Power — Orange Pi 5 Plus 01"
        x-axis "sample" 1 --> 495
        y-axis "W" 0.5 --> 14.0
        line [5.38, 6.63, 5.18, 3.91, 4.78, 5.75, 6.42, 5.15, 3.48, 5.04, 6.16, 7.80, 6.91, 5.98, 7.58, 7.82, 5.80, 6.04, 5.80, 6.23, 5.45, 5.58, 5.82, 4.60, 4.72, 8.12, 7.66, 9.42, 7.01, 7.09, 7.80, 7.21, 7.68, 9.69, 7.15, 8.05, 8.39, 3.65, 2.92, 6.22]
    ```

??? success "Orange Pi Lite 2 01 — pass"

    `orangepilite2` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 441.3 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 49.2 s | warm · up 32 s |
    | kernel-switch | ✅ | 168.8 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-sunxi64 · kernel_before=6.12.110-legacy-sunxi64 |
    | reboot | ✅ | 48.3 s | warm · up 31 s |
    | hw-performance | ✅ | 32.7 s | AES 721 · mem 4400 · disk W 17 / R 23 MB/s · 77.3 °C · 1800 MHz |
    | dvfs | ✅ | 25.3 s | ondemand · 480–1704 MHz (peak 1704) |
    | network-iperf | ✅ | 42.9 s | wlan0 ↑25/↓22 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.7 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi64 |

??? success "Orange Pi One+ 01 — pass"

    `orangepioneplus` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 227.1 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.56 |
    | reboot | ✅ | 39.7 s | warm · up 20 s |
    | kernel-switch | ✅ | 45.4 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-sunxi64 · kernel_before=6.18.53-current-sunxi64 |
    | reboot | ✅ | 123.5 s | warm · 4/4 boots · up 18 s |
    | hw-performance | ✅ | 29.4 s | AES 835 · mem 4600 · disk W 21 / R 23 MB/s · 59.3 °C · 1800 MHz |
    | dvfs | ✅ | 22.4 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 59.4 s | end0 ↑917/↓942 (1GE) · wlx00e04c881724 ↑133/↓177 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.0 s | 26.11.0-trunk.56 · 6.18.53-current-sunxi64 |
    | kernel-switch | ✅ | 124.9 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-sunxi64 · kernel_before=6.18.53-current-sunxi64 |
    | reboot | ✅ | 123.6 s | warm · 4/4 boots · up 17 s |
    | hw-performance | ✅ | 30.1 s | AES 835 · mem 4600 · disk W 20 / R 23 MB/s · 59.3 °C · 1800 MHz |
    | dvfs | ✅ | 22.7 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 66.1 s | end0 ↑912/↓942 (1GE) · wlx00e04c881724 ↑128/↓116 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.0 s | 26.11.0-trunk.56 · 7.2.7-edge-sunxi64 |
    | kernel-switch | ✅ | 126.7 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-sunxi64 · kernel_before=7.2.7-edge-sunxi64 |
    | reboot | ✅ | 37.6 s | warm · up 18 s |

??? failure "Orange Pi PC2 01 — fail"

    `orangepipc2` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.58 · reachable=False · port=22 |

??? success "Orange Pi Prime 01 — pass"

    `orangepiprime` · **inplace** · image `26.11.0-trunk.51` · 3 ✅ · 0 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 45.2 s | AES 377 · mem 2100 · disk W 21 / R 23 MB/s · 40.5 °C · None MHz |
    | dvfs | ➖ | 3.7 s | no cpufreq |
    | network-iperf | ✅ | 167.5 s | end0 ↑879/↓886 (1GE) · wlan0 ↑22/↓21 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 6.1 s | 26.11.0-trunk.51 · 6.18.52-current-sunxi64 |

??? success "Orange Pi Zero2 01 — pass"

    `orangepizero2` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 257.2 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.54 |
    | reboot | ✅ | 46.5 s | power-cycle · up 20 s |
    | kernel-switch | ✅ | 146.4 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-sunxi64 · kernel_before=7.2.6-edge-sunxi64 |
    | reboot | ✅ | 43.8 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 32.9 s | AES 705 · mem 3000 · disk W 21 / R 23 MB/s · 59.8 °C · 1512 MHz |
    | dvfs | ✅ | 26.1 s | ondemand · 480–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 69.3 s | end0 ↑875/↓885 (1GE) · wlx7c023a625db1 ↑19/↓24 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.7 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi64 |

??? success "OrangePi 3 LTS 01 — pass"

    `orangepi3-lts` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 20.8 s | AES 750 · mem 4100 · disk W 55 / R 127 MB/s · 64.6 °C · 1608 MHz |
    | dvfs | ✅ | 21.8 s | ondemand · 480–1608 MHz (peak 1608) |
    | network-iperf | ✅ | 58.5 s | end0 ↑914/↓941 (1GE) · wlan0 ↑142/↓133 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.9 s | 26.8.3 · 7.1.8-edge-sunxi64 |

    **Power** — min 2.50 W · avg 3.45 W · peak 4.30 W · 97 samples

    ```mermaid
    xychart-beta
        title "Power — OrangePi 3 LTS 01"
        x-axis "sample" 1 --> 97
        y-axis "W" 2.0 --> 4.5
        line [2.60, 2.55, 2.50, 2.50, 2.60, 2.95, 3.30, 3.40, 3.50, 3.47, 3.40, 3.80, 2.80, 2.80, 4.30, 4.30, 3.37, 2.90, 3.40, 3.20, 3.20, 3.80, 3.40, 3.40, 3.40, 3.40, 3.70, 3.70, 3.80, 3.75, 3.90, 4.30, 4.17, 3.95, 3.80, 3.67, 3.45, 3.30, 3.80, 3.73]
    ```

??? success "Radxa Dragon Q6A 01 — pass"

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

??? success "Radxa ZERO 3 01 — pass"

    `radxa-zero3` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 38.1 s | AES 720 · mem 3900 · disk W 20 / R 22 MB/s · 49.4 °C · 1416 MHz |
    | dvfs | ✅ | 38.0 s | ondemand · 408–1416 MHz (peak 1416) |
    | network-iperf | ✅ | 55.1 s | wlan0 ↑1/↓6 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 6.8 s | 26.5.1 · 6.18.44-current-rockchip64 |

??? success "Raspberry Pi 3B — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 348.7 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 50.5 s | warm · up 33 s |
    | kernel-switch | ✅ | 75.5 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-bcm2711 · kernel_before=6.18.52-current-bcm2711 |
    | reboot | ✅ | 48.2 s | warm · up 31 s |
    | hw-performance | ✅ | 44.7 s | AES 20 · mem 1400 · disk W 20 / R 22 MB/s · 54.8 °C · 1200 MHz |
    | dvfs | ✅ | 40.2 s | ondemand · 600–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 90.6 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑23/↓31 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 8.2 s | 26.11.0-trunk.54 · 6.18.52-current-bcm2711 |

??? success "Raspberry Pi 5B — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.55` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 143.3 s | nightly · 26.11.0-trunk.55 → 26.11.0-trunk.56 |
    | reboot | ✅ | 46.6 s | power-cycle · up 21 s |
    | kernel-switch | ✅ | 13.4 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.52-current-bcm2711 · kernel_before=6.18.52-current-bcm2711 |
    | reboot | ✅ | 119.2 s | power-cycle · 4/4 boots · up 18 s |
    | hw-performance | ✅ | 14.5 s | AES 1368 · mem 12100 · disk W 54 / R 84 MB/s · 66.7 °C · 2400 MHz |
    | dvfs | ✅ | 13.4 s | ondemand · 1500–2400 MHz (peak 2400) |
    | network-iperf | ✅ | 50.6 s | end0 ↑936/↓941 (1GE) · wlan0 ↑42/↓33 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 3.1 s | 26.11.0-trunk.56 · 6.18.52-current-bcm2711 |
    | kernel-switch | ✅ | 126.4 s | branch=edge · family=bcm2711 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.6-edge-bcm2711 · kernel_before=6.18.52-current-bcm2711 |
    | reboot | ✅ | 126.5 s | power-cycle · 4/4 boots · up 19 s |
    | hw-performance | ✅ | 14.8 s | AES 1368 · mem 9200 · disk W 51 / R 84 MB/s · 67.2 °C · 2400 MHz |
    | dvfs | ✅ | 13.3 s | ondemand · 1500–2400 MHz (peak 2400) |
    | network-iperf | ✅ | 51.4 s | end0 ↑936/↓941 (1GE) · wlan0 ↑45/↓34 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 3.1 s | 26.11.0-trunk.56 · 7.2.6-edge-bcm2711 |
    | kernel-switch | ✅ | 119.0 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.52-current-bcm2711 · kernel_before=7.2.6-edge-bcm2711 |
    | reboot | ✅ | 43.5 s | power-cycle · up 18 s |

    **Power** — min 2.50 W · avg 6.17 W · peak 10.60 W · 726 samples

    ```mermaid
    xychart-beta
        title "Power — Raspberry Pi 5B"
        x-axis "sample" 1 --> 726
        y-axis "W" 2.0 --> 11.0
        line [6.13, 5.71, 6.08, 8.63, 6.09, 6.47, 6.31, 5.77, 6.49, 5.12, 5.97, 5.69, 6.06, 5.53, 6.08, 7.49, 6.13, 5.58, 6.07, 5.59, 6.77, 8.47, 6.06, 6.03, 5.78, 4.40, 5.02, 6.57, 4.16, 6.39, 8.22, 6.09, 5.66, 5.91, 5.49, 7.49, 8.08, 6.54, 6.14, 4.66]
    ```

??? success "Raspberry Pi Zero 2W — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.56` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 88.7 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.56 |
    | reboot | ✅ | 40.2 s | warm · up 23 s |
    | kernel-switch | ✅ | 56.3 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.52-current-bcm2711 · kernel_before=6.18.52-current-bcm2711 |
    | reboot | ✅ | 147.7 s | warm · 4/4 boots · up 25 s |
    | hw-performance | ✅ | 33.4 s | AES 33 · mem 2200 · disk W 20 / R 23 MB/s · 56.4 °C · 1000 MHz |
    | dvfs | ✅ | 27.2 s | ondemand · 600–1000 MHz (peak 1000) |
    | network-iperf | ✅ | 40.0 s | wlan0 ↑37/↓34 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 6.0 s | 26.11.0-trunk.56 · 6.18.52-current-bcm2711 |
    | kernel-switch | ✅ | 188.3 s | branch=edge · family=bcm2711 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.6-edge-bcm2711 · kernel_before=6.18.52-current-bcm2711 |
    | reboot | ✅ | 151.1 s | warm · 4/4 boots · up 25 s |
    | hw-performance | ✅ | 33.5 s | AES 33 · mem 2100 · disk W 20 / R 23 MB/s · 55.8 °C · 1000 MHz |
    | dvfs | ✅ | 27.2 s | ondemand · 600–1000 MHz (peak 1000) |
    | network-iperf | ✅ | 46.6 s | wlan0 ↑35/↓38 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 5.7 s | 26.11.0-trunk.56 · 7.2.6-edge-bcm2711 |
    | kernel-switch | ✅ | 189.0 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.52-current-bcm2711 · kernel_before=7.2.6-edge-bcm2711 |
    | reboot | ✅ | 41.4 s | warm · up 23 s |

??? success "ROCK 2F 01 — pass"

    `rock-2f` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 33.0 s | AES 824 · mem 5900 · disk W 15 / R 65 MB/s · 47.8 °C · 2016 MHz |
    | dvfs | ✅ | 25.8 s | ondemand · 408–2016 MHz (peak 2016) |
    | network-iperf | ✅ | 41.8 s | wlan0 ↑54/↓61 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 5.6 s | 26.5.1 · 6.1.115-vendor-rk35xx |

??? success "Rock 5B 01 — pass"

    `rock-5b` · **inplace** · image `26.11.0-trunk.51` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 135.8 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 46.6 s | power-cycle · up 18 s |
    | kernel-switch | ✅ | 76.5 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 53.4 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 20.8 s | AES 1286 · mem 15000 · disk W 26 / R 85 MB/s · 63.8 °C · 1800 MHz |
    | dvfs | ✅ | 18.1 s | ondemand · 1800–1800 MHz (peak 2352) |
    | network-iperf | ✅ | 34.2 s | enP4p65s0 ↑941/↓938 (1GE) Mbps |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 98.3 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 53.7 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 20.4 s | AES 1287 · mem 11000 · disk W 26 / R 80 MB/s · 62.8 °C · 1800 MHz |
    | dvfs | ✅ | 15.5 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 39.9 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.5 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 73.0 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 55.4 s | power-cycle · up 23 s |

    **Power** — min 0.70 W · avg 5.18 W · peak 13.80 W · 596 samples

    ```mermaid
    xychart-beta
        title "Power — Rock 5B 01"
        x-axis "sample" 1 --> 596
        y-axis "W" 0.5 --> 14.0
        line [5.81, 6.19, 5.87, 6.49, 6.33, 6.43, 6.09, 5.85, 4.34, 5.99, 5.83, 5.90, 6.01, 6.95, 5.21, 2.09, 4.32, 3.80, 6.76, 3.58, 3.56, 3.77, 3.77, 3.73, 4.11, 3.70, 3.04, 1.70, 5.35, 5.79, 9.48, 5.93, 5.86, 5.94, 6.19, 5.75, 6.29, 5.90, 3.06, 4.67]
    ```

??? success "Rock 5B 02 — pass"

    `rock-5b` · **inplace** · image `26.11.0-trunk.51` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 115.0 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 51.7 s | power-cycle · up 17 s |
    | kernel-switch | ✅ | 68.9 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 52.3 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 17.7 s | AES 1283 · mem 15000 · disk W 64 / R 81 MB/s · 65.6 °C · 1800 MHz |
    | dvfs | ✅ | 17.1 s | ondemand · 1800–1800 MHz (peak 2352) |
    | network-iperf | ✅ | 54.8 s | enP4p65s0 ↑941/↓941 (1GE) · wlP2p33s0 ↑453/↓241 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 88.2 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 52.3 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 18.0 s | AES 1297 · mem 11000 · disk W 59 / R 73 MB/s · 64.7 °C · 1800 MHz |
    | dvfs | ✅ | 15.6 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 65.6 s | enP4p65s0 ↑941/↓942 (1GE) · wlP2p33s0 ↑543/↓177 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 67.5 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 54.9 s | power-cycle · up 22 s |

    **Power** — min 2.50 W · avg 5.83 W · peak 13.90 W · 565 samples

    ```mermaid
    xychart-beta
        title "Power — Rock 5B 02"
        x-axis "sample" 1 --> 565
        y-axis "W" 2.0 --> 14.0
        line [5.91, 5.91, 5.99, 6.81, 6.36, 5.96, 6.64, 5.04, 4.71, 6.40, 7.06, 6.23, 6.65, 5.64, 4.60, 4.91, 8.43, 5.68, 4.43, 5.36, 4.70, 5.46, 4.51, 4.83, 4.53, 4.30, 3.88, 7.30, 5.99, 9.77, 5.51, 5.77, 6.97, 5.74, 6.17, 7.13, 6.11, 6.59, 4.39, 5.16]
    ```

??? success "Rock 5B Plus 01 — pass"

    `rock-5b-plus` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 27.3 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 62.5 s | power-cycle · up 29 s |
    | kernel-switch | ✅ | 23.1 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 52.4 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 16.4 s | AES 1284 · mem 15700 · disk W 69 / R 81 MB/s · 51.8 °C · 1800 MHz |
    | dvfs | ✅ | 16.6 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 32.0 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.5 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 649.6 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 55.5 s | power-cycle · up 30 s |
    | hw-performance | ✅ | 27.9 s | AES 1289 · mem 7100 · disk W 20 / R 2 MB/s · 60.1 °C · 1800 MHz |
    | dvfs | ✅ | 16.2 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 31.5 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.1 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 509.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 47.8 s | power-cycle · up 22 s |

    **Power** — min 0.90 W · avg 6.99 W · peak 14.30 W · 1272 samples

    ```mermaid
    xychart-beta
        title "Power — Rock 5B Plus 01"
        x-axis "sample" 1 --> 1272
        y-axis "W" 0.5 --> 14.5
        line [3.65, 3.19, 3.86, 3.78, 4.37, 3.55, 3.76, 5.60, 9.56, 7.96, 11.25, 10.73, 5.08, 4.96, 9.51, 8.80, 9.34, 9.33, 6.59, 4.18, 3.49, 3.51, 3.59, 5.19, 7.01, 5.76, 6.12, 7.19, 6.61, 10.69, 11.74, 12.13, 8.48, 6.12, 9.78, 8.90, 11.61, 11.15, 6.78, 4.91]
    ```

??? success "Rock 5T 01 — pass"

    `rock-5t` · **inplace** · image `26.11.0-trunk.30` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 127.1 s | nightly · 26.11.0-trunk.30 → 26.11.0-trunk.56 |
    | reboot | ✅ | 51.2 s | power-cycle · up 20 s |
    | kernel-switch | ✅ | 78.3 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.53-current-rockchip64 |
    | reboot | ✅ | 134.3 s | power-cycle · 4/4 boots · up 22 s |
    | hw-performance | ✅ | 18.8 s | AES 1262 · mem 15000 · disk W 52 / R 80 MB/s · 53.6 °C · 1800 MHz |
    | dvfs | ✅ | 17.5 s | ondemand · 1800–1800 MHz (peak 2352) |
    | network-iperf | ✅ | 104.4 s | enP3p49s0 ↑939/↓939 (1GE) · enP4p65s0 ↑939/↓939 (1GE) · wlP2p33s0 ↑391/↓248 (Wi-Fi 6) · wlx7cdd90ebf00a ↑114/↓120 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 4.2 s | 26.11.0-trunk.56 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 111.8 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 129.7 s | power-cycle · 4/4 boots · up 17 s |
    | hw-performance | ✅ | 18.1 s | AES 1261 · mem 10000 · disk W 52 / R 81 MB/s · 51.8 °C · 1800 MHz |
    | dvfs | ✅ | 15.3 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 113.5 s | enP3p49s0 ↑939/↓939 (1GE) · enP4p65s0 ↑932/↓927 (1GE) · wlP2p33s0 ↑172/↓206 (Wi-Fi 6) · wlx7cdd90ebf00a ↑81/↓122 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.56 · 6.18.53-current-rockchip64 |
    | kernel-switch | ✅ | 76.2 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.53-current-rockchip64 |
    | reboot | ✅ | 56.4 s | power-cycle · up 22 s |

    **Power** — min 1.40 W · avg 8.75 W · peak 15.80 W · 862 samples

    ```mermaid
    xychart-beta
        title "Power — Rock 5T 01"
        x-axis "sample" 1 --> 862
        y-axis "W" 1.0 --> 16.0
        line [9.59, 9.98, 9.72, 10.39, 9.67, 8.82, 6.56, 9.80, 9.51, 9.75, 6.70, 6.22, 7.86, 6.75, 7.53, 10.63, 9.43, 9.32, 9.80, 9.62, 9.46, 9.31, 9.50, 8.79, 9.10, 6.89, 7.19, 6.57, 4.47, 8.77, 10.79, 9.24, 9.32, 9.84, 10.22, 9.72, 9.89, 9.96, 7.42, 5.96]
    ```

??? success "Rockpi E 01 — pass"

    `rockpi-e` · **inplace** · image `26.11.0-trunk.56` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 73.8 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.56 |
    | reboot | ✅ | 55.3 s | power-cycle · up 24 s |
    | kernel-switch | ✅ | 50.9 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip64 · kernel_before=6.18.53-current-rockchip64 |
    | reboot | ✅ | 156.3 s | power-cycle · 4/4 boots · up 24 s |
    | hw-performance | ✅ | 31.8 s | AES 600 · mem 3300 · disk W 21 / R 23 MB/s · 60.4 °C · 1296 MHz |
    | dvfs | ✅ | 25.2 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 92.1 s | end0 ↑940/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑91/↓211 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.6 s | 26.11.0-trunk.56 · 6.18.53-current-rockchip64 |
    | kernel-switch | ✅ | 177.9 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-rockchip64 · kernel_before=6.18.53-current-rockchip64 |
    | reboot | ✅ | 152.3 s | power-cycle · 4/4 boots · up 24 s |
    | hw-performance | ✅ | 32.1 s | AES 602 · mem 3300 · disk W 21 / R 23 MB/s · 61.2 °C · 1296 MHz |
    | dvfs | ✅ | 26.4 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 90.2 s | end0 ↑941/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑84/↓181 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.9 s | 26.11.0-trunk.56 · 7.2.7-edge-rockchip64 |
    | kernel-switch | ✅ | 175.0 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip64 · kernel_before=7.2.7-edge-rockchip64 |
    | reboot | ✅ | 55.6 s | power-cycle · up 24 s |

??? failure "RockPro 64 01 — fail"

    `rockpro64` · **inplace** · image `26.11.0-trunk.55` · 1 ✅ · 1 ❌ · 14 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 205.9 s | nightly · 26.11.0-trunk.55 → 26.11.0-trunk.56 |
    | reboot | ❌ | 205.2 s | power-cycle |
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

??? failure "SpacemiT K3 Pico-ITX 01 — fail"

    `k3picoitx` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.29 · reachable=False · port=22 |

??? success "Tinker Board 01 — pass"

    `tinkerboard` · **inplace** · image `26.11.0-trunk.56` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 48.9 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.56 |
    | reboot | ✅ | 65.1 s | power-cycle · up 30 s |
    | kernel-switch | ✅ | 30.0 s | branch=current · family=rockchip · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip · kernel_before=6.18.53-current-rockchip |
    | reboot | ✅ | 165.4 s | power-cycle · 4/4 boots · up 30 s |
    | hw-performance | ✅ | 28.2 s | AES 67 · mem 3300 · disk W 13 / R 63 MB/s · 59.5 °C · 1800 MHz |
    | dvfs | ✅ | 20.0 s | ondemand · 600–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 57.8 s | end0 ↑941/↓941 (1GE) · wlan0 ↑27/↓26 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.56 · 6.18.53-current-rockchip |
    | kernel-switch | ✅ | 79.2 s | branch=edge · family=rockchip · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-rockchip · kernel_before=6.18.53-current-rockchip |
    | reboot | ✅ | 173.6 s | power-cycle · 4/4 boots · up 30 s |
    | hw-performance | ✅ | 28.5 s | AES 67 · mem 3300 · disk W 13 / R 1 MB/s · 61.2 °C · 1800 MHz |
    | dvfs | ✅ | 21.5 s | ondemand · 600–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 57.6 s | end0 ↑941/↓941 (1GE) · wlan0 ↑26/↓28 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.56 · 7.2.7-edge-rockchip |
    | kernel-switch | ✅ | 80.8 s | branch=current · family=rockchip · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-rockchip · kernel_before=7.2.7-edge-rockchip |
    | reboot | ✅ | 57.6 s | power-cycle · up 29 s |

    **Power** — min 2.30 W · avg 3.91 W · peak 9.20 W · 735 samples

    ```mermaid
    xychart-beta
        title "Power — Tinker Board 01"
        x-axis "sample" 1 --> 735
        y-axis "W" 2.0 --> 9.5
        line [3.96, 4.19, 3.27, 2.89, 4.14, 4.08, 3.26, 3.85, 2.94, 4.62, 3.47, 2.98, 4.07, 4.31, 5.47, 4.00, 4.22, 3.90, 4.16, 3.84, 4.43, 3.99, 3.48, 3.72, 3.28, 3.63, 3.76, 3.93, 3.24, 4.01, 5.31, 3.93, 4.20, 4.22, 3.91, 5.08, 4.27, 4.33, 2.71, 3.49]
    ```

??? failure "Udoo 01 — fail"

    `udoo` · **inplace** · image `26.11.0-trunk.54` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 120.3 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 66.3 s | power-cycle · up 34 s |
    | kernel-switch | ❌ | 77.4 s | branch=current · family=imx6 · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-imx6 |
    | reboot | ✅ | 65.7 s | power-cycle · up 34 s |
    | hw-performance | ✅ | 51.6 s | AES 26 · mem 827 · disk W 15 / R 20 MB/s · 49.2 °C · 996 MHz |
    | dvfs | ✅ | 43.6 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 102.6 s | end0 ↑398/↓232 (1GE) · wlx7cdd903aa418 ↑36/↓32 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 9.4 s | 26.11.0-trunk.54 · 6.18.52-current-imx6 |

    **Power** — min 1.30 W · avg 5.96 W · peak 8.30 W · 437 samples

    ```mermaid
    xychart-beta
        title "Power — Udoo 01"
        x-axis "sample" 1 --> 437
        y-axis "W" 1.0 --> 8.5
        line [4.93, 6.02, 6.23, 6.21, 5.91, 5.86, 5.93, 5.79, 5.75, 6.06, 5.53, 5.09, 5.53, 7.69, 6.32, 6.38, 5.85, 6.17, 5.89, 5.85, 5.02, 4.52, 4.45, 7.23, 6.65, 5.71, 5.91, 5.31, 5.68, 6.83, 5.91, 6.06, 5.57, 6.47, 6.45, 6.45, 6.57, 6.01, 6.12, 6.53]
    ```

??? success "UEFI arm64 01 — pass"

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

??? success "UEFI x86 01 — pass"

    `uefi-x86` · **inplace** · image `26.11.0-trunk.56` · 14 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 49.7 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.56 |
    | reboot | ✅ | 91.0 s | power-cycle · up 60 s |
    | kernel-switch | ✅ | 34.2 s | branch=current · family=x86 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-x86 · kernel_before=6.18.53-current-x86 |
    | reboot | ✅ | 260.8 s | power-cycle · 4/4 boots · up 55 s |
    | hw-performance | ✅ | 25.6 s | AES 237 · mem 5700 · disk W 25 / R 101 MB/s · 61 °C · 1920 MHz |
    | dvfs | ➖ | 23.4 s | schedutil · 480–1920 MHz (peak 1680) · max_khz is single-core turbo, not an all-core target |
    | network-iperf | ✅ | 61.5 s | enp1s0 ↑901/↓941 (1GE) · wlan0 ↑37/↓27 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.1 s | 26.11.0-trunk.56 · 6.18.53-current-x86 |
    | kernel-switch | ✅ | 179.1 s | branch=edge · family=x86 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-x86 · kernel_before=6.18.53-current-x86 |
    | reboot | ✅ | 244.6 s | power-cycle · 4/4 boots · up 57 s |
    | hw-performance | ✅ | 32.8 s | AES 237 · mem 6200 · disk W 28 / R 106 MB/s · 63 °C · 1920 MHz |
    | dvfs | ➖ | 31.6 s | schedutil · 480–1920 MHz (peak 1896) · max_khz is single-core turbo, not an all-core target |
    | network-iperf | ✅ | 61.8 s | enp1s0 ↑898/↓941 (1GE) · wlan0 ↑35/↓26 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.3 s | 26.11.0-trunk.56 · 7.2.7-edge-x86 |
    | kernel-switch | ✅ | 185.7 s | branch=current · family=x86 · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-x86 · kernel_before=7.2.7-edge-x86 |
    | reboot | ✅ | 89.4 s | power-cycle · up 57 s |

    **Power** — min 0.80 W · avg 4.02 W · peak 8.40 W · 1129 samples

    ```mermaid
    xychart-beta
        title "Power — UEFI x86 01"
        x-axis "sample" 1 --> 1129
        y-axis "W" 0.5 --> 8.5
        line [3.64, 3.77, 3.49, 4.12, 4.94, 3.32, 4.72, 3.66, 4.86, 3.78, 4.39, 3.76, 5.21, 3.79, 3.66, 3.65, 3.40, 3.70, 3.77, 4.22, 3.73, 3.49, 4.81, 4.08, 4.61, 4.56, 3.97, 4.84, 3.84, 3.36, 3.99, 3.49, 3.80, 4.02, 3.86, 4.09, 4.05, 3.19, 3.94, 5.24]
    ```

??? success "ZeroPi 01 — pass"

    `zeropi` · **inplace** · image `26.11.0-trunk.56` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 97.3 s | nightly · 26.11.0-trunk.56 → 26.11.0-trunk.56 |
    | reboot | ✅ | 59.1 s | power-cycle · up 25 s |
    | kernel-switch | ✅ | 62.7 s | branch=current · family=sunxi · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-sunxi · kernel_before=6.18.53-current-sunxi |
    | reboot | ✅ | 166.7 s | power-cycle · 4/4 boots · up 25 s |
    | hw-performance | ✅ | 39.4 s | AES 25 · mem 1500 · disk W 21 / R 23 MB/s · 49.2 °C · 1296 MHz |
    | dvfs | ✅ | 34.1 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 38.6 s | end0 ↑640/↓939 (1GE) Mbps |
    | store-versions | ✅ | 7.3 s | 26.11.0-trunk.56 · 6.18.53-current-sunxi |
    | kernel-switch | ✅ | 176.5 s | branch=edge · family=sunxi · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-7.2.7-edge-sunxi · kernel_before=6.18.53-current-sunxi |
    | reboot | ✅ | 164.1 s | power-cycle · 4/4 boots · up 25 s |
    | hw-performance | ✅ | 39.8 s | AES 25 · mem 1600 · disk W 21 / R 23 MB/s · 51.8 °C · 1296 MHz |
    | dvfs | ✅ | 37.5 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 38.8 s | end0 ↑628/↓939 (1GE) Mbps |
    | store-versions | ✅ | 7.3 s | 26.11.0-trunk.56 · 7.2.7-edge-sunxi |
    | kernel-switch | ✅ | 171.6 s | branch=current · family=sunxi · installed=26.11.0-trunk.56 · boot_image=/boot/vmlinuz-6.18.53-current-sunxi · kernel_before=7.2.7-edge-sunxi |
    | reboot | ✅ | 60.1 s | power-cycle · up 25 s |

    **Power** — min 1.20 W · avg 2.17 W · peak 3.10 W · 976 samples

    ```mermaid
    xychart-beta
        title "Power — ZeroPi 01"
        x-axis "sample" 1 --> 976
        y-axis "W" 1.0 --> 3.5
        line [1.98, 2.13, 2.08, 1.93, 1.87, 2.35, 2.13, 1.94, 2.43, 2.29, 2.35, 2.13, 2.40, 2.02, 2.18, 2.11, 2.24, 2.18, 2.03, 2.06, 2.12, 2.16, 2.12, 2.16, 2.22, 2.39, 2.16, 2.26, 2.25, 2.17, 2.35, 2.26, 2.18, 2.28, 2.26, 2.16, 2.11, 2.12, 1.87, 2.20]
    ```


<!-- FLEET-STOP -->
