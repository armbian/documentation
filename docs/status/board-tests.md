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

**65** boards — **41** passed, **24** failed. Each card is the board's most recent test.

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

    `bananapicm4io` · **inplace** · image `26.8.3` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 280.8 s | nightly · 26.8.3 → 26.8.3 |
    | reboot | ✅ | 43.3 s | power-cycle · up 19 s |
    | kernel-switch | ✅ | 41.0 s | branch=current · family=meson64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-meson64 · kernel_before=6.18.52-current-meson64 |
    | reboot | ✅ | 47.2 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 18.3 s | AES 852 · mem 3900 · disk W 43 / R 157 MB/s · 54.7 °C · 2016 MHz |
    | dvfs | ✅ | 18.0 s | ondemand · 1000–1512 MHz (peak 1512) |
    | network-iperf | ❌ | 552.0 s | eth0 ↑0/↓0 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) · wlx00e032c00694 ↑0/↓0 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 3.8 s | 26.8.3 · 6.18.52-current-meson64 |

??? failure "Banana Pi M2 Ultra 01 — fail"

    `bananapim2ultra` · **inplace** · image `26.11.0-trunk.54` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 101.3 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 41.2 s | warm · up 22 s |
    | kernel-switch | ❌ | 68.4 s | branch=current · family=sunxi · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-sunxi |
    | reboot | ✅ | 43.5 s | warm · up 22 s |
    | hw-performance | ✅ | 38.0 s | AES 23 · mem 2100 · disk W 3 / R 42 MB/s · 50.6 °C · 1200 MHz |
    | dvfs | ✅ | 33.9 s | ondemand · 720–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 79.1 s | end0 ↑809/↓941 (1GE) · wlan0 ↑32/↓31 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 7.2 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi |

??? failure "Banana Pi M2Pro 01 — fail"

    `bananapim2pro` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.44 · reachable=False · port=22 |

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

    `bananapim7` · **inplace** · image `26.11.0-trunk.51` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 68.6 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 45.8 s | power-cycle · up 13 s |
    | kernel-switch | ✅ | 18.8 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 41.0 s | power-cycle · up 15 s |
    | hw-performance | ✅ | 13.8 s | AES 1260 · mem 15200 · disk W 845 / R 1401 MB/s · 58.2 °C · 1800 MHz |
    | dvfs | ✅ | 17.4 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 29.1 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 47.7 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 122.9 s | power-cycle · up 97 s |
    | hw-performance | ✅ | 13.7 s | AES 1257 · mem 7500 · disk W 888 / R 1571 MB/s · 62.8 °C · 1800 MHz |
    | dvfs | ✅ | 14.6 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 29.9 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 38.2 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 41.5 s | power-cycle · up 16 s |

    **Power** — min 1.00 W · avg 6.03 W · peak 13.20 W · 430 samples

    ```mermaid
    xychart-beta
        title "Power — Banana Pi M7 01"
        x-axis "sample" 1 --> 430
        y-axis "W" 0.5 --> 13.5
        line [4.43, 5.71, 6.85, 5.74, 6.96, 5.77, 5.04, 3.64, 5.50, 5.56, 4.76, 8.36, 5.46, 5.37, 8.67, 5.12, 5.15, 5.02, 6.16, 6.73, 6.24, 4.53, 6.50, 6.25, 5.40, 5.40, 5.40, 5.40, 5.40, 5.40, 6.66, 9.15, 5.87, 6.07, 5.91, 8.38, 7.37, 6.48, 5.75, 7.25]
    ```

??? success "Banana Pi R3 Mini 01 — pass"

    `bananapir3mini` · **inplace** · image `26.11.0-trunk` · 4 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 17.4 s | — |
    | reboot | ✅ | 60.7 s | power-cycle · up 31 s |
    | hw-performance | ✅ | 26.7 s | AES 935 · mem 3100 · disk W 78 / R 91 MB/s · 61.5 °C · None MHz |
    | dvfs | ➖ | 2.9 s | — |
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
    | dvfs | ➖ | 2.9 s | — |
    | network-iperf | ✅ | 38.5 s | lan2 ↑936/↓936 Mbps |
    | store-versions | ✅ | 6.0 s | 26.11.0-trunk.54 · 6.18.52-current-mvebu |

??? failure "Cubie A5E 01 — fail"

    `radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.52` · 10 ✅ · 3 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 108.9 s | — |
    | reboot | ✅ | 60.9 s | power-cycle · up 29 s |
    | kernel-switch | ❌ | 125.5 s | branch=current · phase=install · dpkg_state=absent |
    | reboot | ✅ | 62.0 s | power-cycle · up 30 s |
    | hw-performance | ✅ | 43.7 s | AES 358 · mem 2000 · disk W 20 / R 2 MB/s · 63.2 °C · None MHz |
    | dvfs | ➖ | 2.9 s | — |
    | network-iperf | ✅ | 105.3 s | end0 ↑838/↓939 (1GE) · end1 ↑941/↓940 (1GE) · wlan0 ↑120/↓130 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 6.0 s | 26.11.0-trunk.52 · 6.18.52-current-sunxi64 |
    | kernel-switch | ❌ | 123.5 s | branch=edge · phase=install · dpkg_state=absent |
    | reboot | ✅ | 63.6 s | power-cycle · up 33 s |
    | hw-performance | ✅ | 42.8 s | AES 357 · mem 2000 · disk W 21 / R 23 MB/s · 62.5 °C · None MHz |
    | dvfs | ➖ | 2.9 s | — |
    | network-iperf | ✅ | 91.7 s | end0 ↑817/↓941 (1GE) · end1 ↑941/↓940 (1GE) · wlan0 ↑120/↓127 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 6.0 s | 26.11.0-trunk.52 · 6.18.52-current-sunxi64 |
    | kernel-switch | ❌ | 124.0 s | branch=current · phase=install · dpkg_state=absent |
    | reboot | ✅ | 63.5 s | power-cycle · up 32 s |

    **Power** — min 1.70 W · avg 3.45 W · peak 4.20 W · 833 samples

    ```mermaid
    xychart-beta
        title "Power — Cubie A5E 01"
        x-axis "sample" 1 --> 833
        y-axis "W" 1.5 --> 4.5
        line [3.45, 3.65, 3.62, 3.45, 3.41, 2.78, 3.40, 3.68, 3.50, 3.51, 3.45, 3.47, 2.80, 3.38, 3.64, 3.40, 3.61, 3.57, 3.55, 3.54, 3.54, 3.59, 3.52, 3.52, 3.52, 3.29, 2.80, 3.57, 3.43, 3.54, 3.65, 3.63, 3.60, 3.62, 3.55, 3.53, 3.54, 3.50, 3.03, 3.17]
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
    | hw-performance | ✅ | 40.3 s | AES 371 · mem 2000 · disk W 9 / R 137 MB/s · None °C · 800 MHz |
    | dvfs | ✅ | 33.6 s | ondemand · 200–800 MHz (peak 800) |
    | network-iperf | ✅ | 38.4 s | lan0 ↑936/↓762 (1GE) Mbps |
    | store-versions | ✅ | 7.8 s | 26.8.3 · 6.18.44-current-mvebu64 |

??? failure "Helios4 01 — fail"

    `helios4` · **inplace** · image `26.11.0-trunk.54` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 52.9 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 117.2 s | warm · up 102 s |
    | kernel-switch | ❌ | 34.2 s | branch=current · family=mvebu · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-mvebu |
    | reboot | ✅ | 117.6 s | warm · up 102 s |
    | hw-performance | ✅ | 36.4 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 56.1 °C · None MHz |
    | dvfs | ➖ | 2.3 s | — |
    | network-iperf | ✅ | 34.2 s | end1 ↑568/↓477 (1GE) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.54 · 6.18.52-current-mvebu |

??? failure "Inovato Quadra 01 — fail"

    `inovato-quadra` · **inplace** · image `26.8.0-trunk.314` · 2 ✅ · 4 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 241.7 s | nightly · 26.8.0-trunk.314 → 26.8.0-trunk.314 |
    | reboot | ❌ | 213.8 s | power-cycle |
    | hw-performance | ✅ | 154.8 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 7.2 s | — |
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

??? success "Le potato 01 — pass"

    `lepotato` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 210.3 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 41.6 s | warm · up 24 s |
    | hw-performance | ✅ | 32.5 s | AES 656 · mem 3600 · disk W 17 / R 2 MB/s · 50 °C · 1512 MHz |
    | dvfs | ✅ | 23.2 s | ondemand · 500–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 50.4 s | end0 ↑94/↓94 (10/100ME) Mbps |
    | restore-stable | ✅ | 157.4 s | stable |
    | reboot | ✅ | 40.3 s | warm · up 24 s |
    | store-versions | ✅ | 5.9 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

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
    | dvfs | ➖ | 2.9 s | — |
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

    `odroidc2` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 205.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 32.5 s | warm · up 16 s |
    | kernel-switch | ✅ | 37.5 s | branch=current · family=meson64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-meson64 · kernel_before=6.18.52-current-meson64 |
    | reboot | ✅ | 30.0 s | warm · up 15 s |
    | hw-performance | ✅ | 22.9 s | AES 51 · mem 3500 · disk W 33 / R 152 MB/s · 46 °C · 1536 MHz |
    | dvfs | ✅ | 22.1 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 91.0 s | end0 ↑940/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.54 · 6.18.52-current-meson64 |

??? success "Odroid C4 01 — pass"

    `odroidc4` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 199.4 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 46.4 s | power-cycle · up 16 s |
    | kernel-switch | ✅ | 30.4 s | branch=current · family=meson64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-meson64 · kernel_before=6.18.52-current-meson64 |
    | reboot | ✅ | 46.9 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 21.6 s | AES 980 · mem 5300 · disk W 30 / R 80 MB/s · 43.7 °C · 2100 MHz |
    | dvfs | ✅ | 19.6 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 123.3 s | end0 ↑852/↓875 (1GE) · wlx24050fdd332b ↑116/↓87 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 5.0 s | 26.11.0-trunk.54 · 6.18.52-current-meson64 |

    **Power** — min 1.00 W · avg 3.44 W · peak 5.00 W · 394 samples

    ```mermaid
    xychart-beta
        title "Power — Odroid C4 01"
        x-axis "sample" 1 --> 394
        y-axis "W" 0.5 --> 5.5
        line [2.80, 3.60, 3.55, 3.65, 3.45, 3.60, 3.56, 3.50, 3.59, 3.60, 3.25, 4.02, 4.30, 3.66, 3.56, 3.59, 3.60, 3.10, 2.26, 2.83, 3.77, 3.68, 3.42, 3.24, 1.92, 2.80, 3.89, 3.53, 4.02, 3.70, 3.27, 3.34, 3.25, 2.99, 3.39, 3.28, 3.43, 4.15, 3.37, 3.92]
    ```

??? success "Odroid M1 01 — pass"

    `odroidm1` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 48.0 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 53.6 s | power-cycle · up 20 s |
    | kernel-switch | ✅ | 31.6 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 56.9 s | power-cycle · up 23 s |
    | hw-performance | ✅ | 17.1 s | AES 917 · mem 5100 · disk W 1032 / R 1018 MB/s · 33.8 °C · 1992 MHz |
    | dvfs | ✅ | 21.4 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 58.1 s | eth0 ↑639/↓941 (1GE) · wlx40a5eff39254 ↑210/↓227 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 86.1 s | branch=edge · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-7.2.6-edge-rockchip64 · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 56.0 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 17.8 s | AES 916 · mem 5100 · disk W 1034 / R 1071 MB/s · 34.4 °C · 1992 MHz |
    | dvfs | ✅ | 22.4 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 59.1 s | eth0 ↑941/↓941 (1GE) · wlx40a5eff39254 ↑211/↓228 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.54 · 7.2.6-edge-rockchip64 |
    | kernel-switch | ✅ | 86.7 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=7.2.6-edge-rockchip64 |
    | reboot | ✅ | 58.6 s | power-cycle · up 23 s |

    **Power** — min 2.00 W · avg 6.32 W · peak 10.00 W · 514 samples

    ```mermaid
    xychart-beta
        title "Power — Odroid M1 01"
        x-axis "sample" 1 --> 514
        y-axis "W" 1.5 --> 10.5
        line [6.48, 5.93, 5.77, 5.95, 7.55, 7.32, 6.81, 5.05, 5.72, 7.67, 6.52, 6.72, 6.18, 5.79, 5.88, 6.15, 5.51, 7.82, 8.52, 6.54, 6.00, 6.65, 5.44, 5.89, 6.64, 5.44, 6.15, 5.72, 5.60, 5.65, 6.00, 5.30, 7.32, 7.63, 7.20, 6.89, 5.97, 5.69, 4.69, 6.95]
    ```

??? success "Odroid N2 01 — pass"

    `odroidn2` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 172.6 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 61.6 s | power-cycle · up 24 s |
    | kernel-switch | ✅ | 24.9 s | branch=current · family=meson64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-meson64 · kernel_before=6.18.52-current-meson64 |
    | reboot | ✅ | 59.3 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 18.8 s | AES 1085 · mem 4900 · disk W 28 / R 138 MB/s · 39.4 °C · 1992 MHz |
    | dvfs | ✅ | 17.2 s | performance · 1000–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 38.8 s | end0 ↑940/↓941 (1GE) Mbps |
    | store-versions | ✅ | 3.6 s | 26.11.0-trunk.54 · 6.18.52-current-meson64 |

    **Power** — min 1.00 W · avg 3.73 W · peak 9.80 W · 313 samples

    ```mermaid
    xychart-beta
        title "Power — Odroid N2 01"
        x-axis "sample" 1 --> 313
        y-axis "W" 0.5 --> 10.0
        line [3.07, 4.52, 3.83, 3.65, 3.93, 3.66, 3.90, 4.12, 3.98, 3.56, 3.71, 4.59, 3.29, 3.23, 3.52, 4.06, 4.35, 4.56, 3.95, 3.57, 1.83, 2.12, 3.26, 3.98, 4.75, 4.27, 3.54, 3.80, 1.61, 2.27, 3.56, 4.17, 4.15, 3.50, 7.70, 4.84, 3.25, 3.32, 2.96, 3.55]
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

    `orangepioneplus` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 222.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 36.3 s | warm · up 18 s |
    | kernel-switch | ✅ | 124.3 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-sunxi64 · kernel_before=7.2.6-edge-sunxi64 |
    | reboot | ✅ | 35.2 s | warm · up 18 s |
    | hw-performance | ✅ | 29.5 s | AES 831 · mem 4600 · disk W 21 / R 23 MB/s · 61.4 °C · 1800 MHz |
    | dvfs | ✅ | 22.3 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 70.3 s | end0 ↑917/↓941 (1GE) · wlx00e04c881724 ↑142/↓174 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi64 |

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
    | dvfs | ➖ | 3.7 s | — |
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
    | hw-performance | ✅ | 21.3 s | AES 750 · mem 4100 · disk W 55 / R 127 MB/s · 66 °C · 1608 MHz |
    | dvfs | ✅ | 21.6 s | ondemand · 480–1608 MHz (peak 1608) |
    | network-iperf | ✅ | 119.1 s | end0 ↑914/↓940 (1GE) · wlan0 ↑98/↓133 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 4.8 s | 26.8.3 · 7.1.8-edge-sunxi64 |

    **Power** — min 2.60 W · avg 3.42 W · peak 4.40 W · 139 samples

    ```mermaid
    xychart-beta
        title "Power — OrangePi 3 LTS 01"
        x-axis "sample" 1 --> 139
        y-axis "W" 2.5 --> 4.5
        line [2.80, 2.80, 3.63, 3.40, 3.02, 3.40, 3.42, 3.50, 4.32, 4.40, 3.65, 3.80, 3.57, 3.07, 3.40, 3.53, 3.70, 3.27, 2.80, 2.93, 3.53, 3.10, 3.47, 3.80, 3.87, 3.75, 3.63, 3.08, 2.60, 3.58, 2.80, 3.50, 3.00, 4.40, 3.50, 3.35, 3.70, 3.40, 3.30, 2.77]
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

    `rpi4b` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 66.4 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 46.3 s | power-cycle · up 21 s |
    | kernel-switch | ✅ | 11.9 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-bcm2711 · kernel_before=6.18.52-current-bcm2711 |
    | reboot | ✅ | 45.7 s | power-cycle · up 21 s |
    | hw-performance | ✅ | 14.5 s | AES 1368 · mem 12100 · disk W 56 / R 82 MB/s · 66.7 °C · 2400 MHz |
    | dvfs | ✅ | 13.1 s | ondemand · 1500–2400 MHz (peak 2400) |
    | network-iperf | ✅ | 62.5 s | end0 ↑936/↓941 (1GE) · wlan0 ↑42/↓18 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 3.1 s | 26.11.0-trunk.54 · 6.18.52-current-bcm2711 |

    **Power** — min 3.20 W · avg 5.97 W · peak 10.20 W · 209 samples

    ```mermaid
    xychart-beta
        title "Power — Raspberry Pi 5B"
        x-axis "sample" 1 --> 209
        y-axis "W" 3.0 --> 10.5
        line [4.80, 5.56, 6.28, 5.94, 5.17, 5.82, 6.78, 5.90, 6.10, 6.90, 6.42, 6.44, 5.00, 4.37, 3.76, 4.64, 5.26, 5.97, 6.70, 6.10, 4.90, 3.88, 4.45, 7.28, 6.70, 5.30, 6.47, 6.04, 9.12, 7.62, 7.24, 5.70, 6.96, 6.56, 6.70, 6.88, 6.20, 6.28, 5.38, 5.83]
    ```

??? success "Raspberry Pi Zero 2W — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 282.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 40.9 s | warm · up 25 s |
    | kernel-switch | ✅ | 54.7 s | branch=current · family=bcm2711 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-bcm2711 · kernel_before=6.18.52-current-bcm2711 |
    | reboot | ✅ | 36.8 s | warm · up 22 s |
    | hw-performance | ✅ | 34.4 s | AES 33 · mem 2200 · disk W 20 / R 23 MB/s · 56.9 °C · 1000 MHz |
    | dvfs | ✅ | 27.9 s | ondemand · 600–1000 MHz (peak 1000) |
    | network-iperf | ✅ | 45.1 s | wlan0 ↑27/↓27 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 6.8 s | 26.11.0-trunk.54 · 6.18.52-current-bcm2711 |

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

    `rock-5t` · **inplace** · image `26.11.0-trunk.30` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 78.2 s | nightly · 26.11.0-trunk.30 → 26.11.0-trunk.30 |
    | reboot | ✅ | 54.6 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 18.0 s | AES 1251 · mem 10000 · disk W 50 / R 82 MB/s · 58.2 °C · 1800 MHz |
    | dvfs | ✅ | 16.3 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 104.4 s | enP3p49s0 ↑2353/↓2352 (2.5GE) · enP4p65s0 ↑2353/↓2354 (2.5GE) · wlP2p33s0 ↑337/↓216 (Wi-Fi 6) · wlx7cdd90ebf00a ↑96/↓121 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 67.1 s | stable |
    | reboot | ✅ | 54.5 s | power-cycle · up 22 s |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.30 · 6.18.44-current-rockchip64 |

    **Power** — min 0.90 W · avg 9.24 W · peak 16.70 W · 273 samples

??? success "Rockpi E 01 — pass"

    `rockpi-e` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 306.2 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.54 |
    | reboot | ✅ | 54.5 s | power-cycle · up 24 s |
    | kernel-switch | ✅ | 50.8 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 53.4 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 32.1 s | AES 596 · mem 3300 · disk W 21 / R 23 MB/s · 64.2 °C · 1296 MHz |
    | dvfs | ✅ | 24.9 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 95.6 s | end0 ↑941/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑159/↓211 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.5 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |

??? failure "RockPro 64 01 — fail"

    `rockpro64` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.31 · reachable=False · port=22 |

??? failure "SpacemiT K3 Pico-ITX 01 — fail"

    `k3picoitx` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.29 · reachable=False · port=22 |

??? failure "Tinker Board 01 — fail"

    `tinkerboard` · **inplace** · image `26.11.0-trunk.54` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 39.2 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 55.0 s | power-cycle · up 29 s |
    | kernel-switch | ❌ | 30.4 s | branch=current · family=rockchip · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-rockchip |
    | reboot | ✅ | 65.0 s | power-cycle · up 32 s |
    | hw-performance | ✅ | 28.6 s | AES 67 · mem 3300 · disk W 14 / R 63 MB/s · 57.7 °C · 1800 MHz |
    | dvfs | ✅ | 19.8 s | ondemand · 600–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 57.8 s | end0 ↑940/↓941 (1GE) · wlan0 ↑32/↓33 (Wi-Fi 4) Mbps |
    | store-versions | ✅ | 5.2 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip |

    **Power** — min 2.30 W · avg 3.86 W · peak 8.40 W · 241 samples

    ```mermaid
    xychart-beta
        title "Power — Tinker Board 01"
        x-axis "sample" 1 --> 241
        y-axis "W" 2.0 --> 8.5
        line [2.60, 3.60, 4.37, 4.30, 4.55, 4.35, 4.20, 2.75, 3.10, 2.50, 2.87, 3.35, 4.10, 4.40, 4.75, 4.53, 3.95, 3.00, 3.00, 3.78, 2.83, 2.57, 2.75, 4.02, 3.40, 4.00, 3.27, 3.47, 4.53, 6.45, 6.70, 3.33, 3.25, 4.00, 4.53, 3.83, 3.95, 5.80, 3.80, 3.80]
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

??? failure "UEFI arm64 01 — fail"

    `uefi-arm64` · **inplace** · image `26.11.0-trunk.30` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.45 · reachable=False · port=22 |

??? success "UEFI x86 01 — pass"

    `uefi-x86` · **inplace** · image `26.11.0-trunk.54` · 14 ✅ · 2 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 50.7 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 94.0 s | power-cycle · up 60 s |
    | kernel-switch | ✅ | 34.4 s | branch=current · family=x86 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-x86 · kernel_before=6.18.52-current-x86 |
    | reboot | ✅ | 100.4 s | power-cycle · up 58 s |
    | hw-performance | ✅ | 24.9 s | AES 237 · mem 6400 · disk W 25 / R 108 MB/s · 57 °C · 1920 MHz |
    | dvfs | ❌ | 23.3 s | schedutil · 480–1920 MHz (peak 1690) |
    | network-iperf | ✅ | 62.9 s | enp1s0 ↑919/↓941 (1GE) · wlan0 ↑25/↓22 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.2 s | 26.11.0-trunk.54 · 6.18.52-current-x86 |
    | kernel-switch | ✅ | 176.9 s | branch=edge · family=x86 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-7.2.6-edge-x86 · kernel_before=6.18.52-current-x86 |
    | reboot | ✅ | 93.6 s | power-cycle · up 60 s |
    | hw-performance | ✅ | 25.0 s | AES 237 · mem 4900 · disk W 26 / R 112 MB/s · 57 °C · 1920 MHz |
    | dvfs | ❌ | 23.9 s | schedutil · 480–1920 MHz (peak 1680) |
    | network-iperf | ✅ | 61.7 s | enp1s0 ↑920/↓941 (1GE) · wlan0 ↑26/↓30 (Wi-Fi 5) Mbps |
    | store-versions | ✅ | 5.3 s | 26.11.0-trunk.54 · 7.2.6-edge-x86 |
    | kernel-switch | ✅ | 185.4 s | branch=current · family=x86 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-x86 · kernel_before=7.2.6-edge-x86 |
    | reboot | ✅ | 98.6 s | power-cycle · up 57 s |

    **Power** — min 1.90 W · avg 3.99 W · peak 7.60 W · 839 samples

    ```mermaid
    xychart-beta
        title "Power — UEFI x86 01"
        x-axis "sample" 1 --> 839
        y-axis "W" 1.5 --> 8.0
        line [4.53, 4.00, 2.97, 4.03, 4.93, 3.80, 3.55, 3.41, 3.85, 5.21, 3.40, 4.09, 4.15, 3.80, 3.54, 4.00, 4.10, 3.80, 4.24, 4.19, 4.27, 3.88, 3.88, 4.09, 4.44, 3.06, 4.33, 4.20, 3.38, 3.85, 3.93, 4.31, 3.68, 4.15, 4.15, 3.78, 4.04, 3.56, 4.03, 5.11]
    ```

??? failure "ZeroPi 01 — fail"

    `zeropi` · **inplace** · image `26.11.0-trunk.54` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 95.1 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 56.2 s | power-cycle · up 24 s |
    | kernel-switch | ❌ | 62.8 s | branch=current · family=sunxi · installed=26.11.0-trunk.54 · boot_image=Image · kernel_before=6.18.52-current-sunxi |
    | reboot | ✅ | 55.3 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 39.6 s | AES 25 · mem 1500 · disk W 2 / R 23 MB/s · 48.4 °C · 1296 MHz |
    | dvfs | ✅ | 34.4 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 41.3 s | end0 ↑628/↓523 (1GE) Mbps |
    | store-versions | ✅ | 7.5 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi |

    **Power** — min 1.20 W · avg 2.11 W · peak 3.00 W · 319 samples

    ```mermaid
    xychart-beta
        title "Power — ZeroPi 01"
        x-axis "sample" 1 --> 319
        y-axis "W" 1.0 --> 3.5
        line [1.50, 2.05, 2.20, 2.12, 2.26, 2.10, 2.10, 2.05, 2.06, 2.25, 1.91, 1.61, 1.85, 1.82, 2.51, 2.29, 2.46, 2.26, 2.19, 2.10, 2.15, 2.20, 1.95, 1.69, 1.73, 1.98, 2.46, 2.56, 2.25, 2.02, 1.93, 2.05, 2.31, 2.44, 2.07, 2.19, 2.18, 2.34, 2.10, 2.04]
    ```


<!-- FLEET-STOP -->
