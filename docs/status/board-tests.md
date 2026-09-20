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

**65** boards — **51** passed, **14** failed. Each card is the board's most recent test.

??? success "Arduino UNO Q 01 — pass"

    `arduino-uno-q` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 135.4 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 52.8 s | warm · up 35 s |
    | hw-performance | ✅ | 25.1 s | AES 940 · mem 5100 · disk W 188 / R 258 MB/s · 40.6 °C · 2016 MHz |
    | dvfs | ✅ | 31.8 s | schedutil · 300–2016 MHz (peak 2016) |
    | network-iperf | ✅ | 44.8 s | wlan0 ↑27/↓20 (Wi-Fi 5) · usb0 ↑?/↓? Mbps |
    | restore-stable | ✅ | 100.5 s | stable |
    | reboot | ✅ | 52.3 s | warm · up 35 s |
    | store-versions | ✅ | 7.5 s | 26.11.0-trunk.51 · 7.1.8-edge-qrb2210 |

??? success "Banana Pi CM4IO 01 — pass"

    `bananapicm4io` · **inplace** · image `26.8.3` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 189.4 s | nightly · 26.8.3 → 26.8.3 |
    | reboot | ✅ | 57.3 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 18.2 s | AES 852 · mem 3900 · disk W 40 / R 151 MB/s · 50.8 °C · 2016 MHz |
    | dvfs | ✅ | 18.2 s | ondemand · 1000–1512 MHz (peak 1512) |
    | network-iperf | ❌ | 577.8 s | eth0 ↑939/↓939 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) · wlx00e032c00694 ↑0/↓0 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 164.6 s | stable |
    | reboot | ✅ | 46.5 s | power-cycle · up 22 s |
    | store-versions | ✅ | 3.9 s | 26.8.3 · 6.18.44-current-meson64 |

??? failure "Banana Pi M2 Ultra 01 — fail"

    `bananapim2ultra` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.83 · reachable=False · port=22 |

??? failure "Banana Pi M2Pro 01 — fail"

    `bananapim2pro` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.44 · reachable=False · port=22 |

??? success "Banana Pi M5 01 — pass"

    `bananapim5` · **inplace** · image `26.11.0-trunk.51` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 182.1 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 169.2 s | warm · up 155 s |
    | hw-performance | ✅ | 38.3 s | AES 975 · mem 5200 · disk W 10 / R 15 MB/s · 57.2 °C · 2100 MHz |
    | dvfs | ✅ | 20.9 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ❌ | 71.2 s | end0 ↑940/↓941 (1GE) · wlx000f13960190 ↑0/↓1 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 142.1 s | stable |
    | reboot | ✅ | 166.7 s | warm · up 151 s |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.51 · 6.18.44-current-meson64 |

??? success "Banana Pi M7 01 — pass"

    `bananapim7` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 50.0 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 40.5 s | power-cycle · up 16 s |
    | hw-performance | ✅ | 13.8 s | AES 1262 · mem 15200 · disk W 963 / R 1253 MB/s · 55.5 °C · 1800 MHz |
    | dvfs | ✅ | 16.9 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 30.2 s | enP2p33s0 ↑940/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 34.8 s | stable |
    | reboot | ✅ | 48.8 s | power-cycle · up 15 s |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.51 · 6.1.115-vendor-rk35xx |

    **Power** — min 4.10 W · avg 5.84 W · peak 10.30 W · 174 samples

??? success "Banana Pi R3 Mini 01 — pass"

    `bananapir3mini` · **inplace** · image `26.11.0-trunk` · 5 ✅ · 0 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 18.1 s | — |
    | reboot | ✅ | 63.4 s | power-cycle · up 32 s |
    | hw-performance | ✅ | 26.6 s | AES 935 · mem 3200 · disk W 76 / R 91 MB/s · 61.2 °C · None MHz |
    | dvfs | ➖ | 2.1 s | — |
    | network-iperf | ✅ | 109.2 s | eth0 ↑939/↓899 (1GE) · eth1 ↑743/↓752 (1GE) · wlan0 ↑16/↓19 (Wi-Fi 6) · wlan1 ↑266/↓237 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 10.6 s | — |
    | reboot | ✅ | 61.1 s | power-cycle · up 31 s |
    | store-versions | ✅ | 4.4 s | 26.11.0-trunk · 6.18.52-current-filogic-mt7986 |

    **Power** — min 3.10 W · avg 5.96 W · peak 10.10 W · 238 samples

??? success "BananaPi BPI-F3 01 — pass"

    `bananapif3` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 134.1 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 48.7 s | power-cycle · up 19 s |
    | hw-performance | ✅ | 22.4 s | AES 30 · mem 3400 · disk W 59 / R 82 MB/s · 60 °C · 1800 MHz |
    | dvfs | ✅ | 23.0 s | performance · 614–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 148.4 s | eth0 ↑919/↓666 (1GE) · wlan0 ↑215/↓227 (Wi-Fi 6) · wlan1 ↑69/↓88 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 82.7 s | stable |
    | reboot | ✅ | 47.5 s | power-cycle · up 18 s |
    | store-versions | ✅ | 5.3 s | 26.11.0-trunk.51 · 6.18.44-current-spacemit |

??? failure "BigTreeTech CB1 01 — fail"

    `bigtreetech-cb1` · **inplace** · image `26.8.1` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 170.5 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ✅ | 52.6 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 34.8 s | AES 705 · mem 3900 · disk W 14 / R 23 MB/s · 54.2 °C · 1512 MHz |
    | dvfs | ✅ | 23.7 s | ondemand · 480–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 32.2 s | end0 ↑94/↓94 (10/100ME) Mbps |
    | restore-stable | ✅ | 141.7 s | stable |
    | reboot | ❌ | 217.2 s | power-cycle |
    | store-versions | ⏭️ | 0.0 s | — |

    **Power** — min 0.80 W · avg 1.92 W · peak 3.60 W · 548 samples

??? success "Clearfog Pro 01 — pass"

    `clearfogpro` · **inplace** · image `26.11.0-trunk.51` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 109.7 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 35.8 s | warm · up 19 s |
    | hw-performance | ✅ | 41.5 s | AES 43 · mem 3800 · disk W 20 / R 23 MB/s · 64.2 °C · None MHz |
    | dvfs | ➖ | 2.8 s | — |
    | network-iperf | ✅ | 80.5 s | lan2 ↑936/↓936 Mbps |
    | restore-stable | ✅ | 85.6 s | stable |
    | reboot | ✅ | 37.3 s | warm · up 20 s |
    | store-versions | ✅ | 6.9 s | 26.11.0-trunk.51 · 6.6.151-current-mvebu |

??? failure "Cubie A5E 01 — fail"

    `radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.54` · 8 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 83.7 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 71.3 s | power-cycle · up 32 s |
    | kernel-switch | ✅ | 60.7 s | branch=current · family=sunxi64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-sunxi64 · kernel_before=6.18.52-current-sunxi64 |
    | reboot | ✅ | 63.5 s | power-cycle · up 32 s |
    | hw-performance | ✅ | 41.4 s | AES 358 · mem 2000 · disk W 21 / R 23 MB/s · 64.8 °C · None MHz |
    | dvfs | ➖ | 2.8 s | — |
    | network-iperf | ✅ | 89.0 s | end0 ↑820/↓941 (1GE) · end1 ↑941/↓941 (1GE) · wlan0 ↑120/↓130 (Wi-Fi 6) Mbps |
    | store-versions | ✅ | 5.7 s | 26.11.0-trunk.54 · 6.18.52-current-sunxi64 |
    | kernel-switch | ✅ | 577.5 s | branch=edge · family=sunxi64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-7.2.6-edge-sunxi64 · kernel_before=6.18.52-current-sunxi64 |
    | reboot | ❌ | 223.4 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | store-versions | ⏭️ | 0.0 s | — |
    | kernel-switch | ⏭️ | 0.0 s | skipped=board down after reboot/power-cycle |
    | reboot | ⏭️ | 0.0 s | reboot |

    **Power** — min 1.30 W · avg 3.75 W · peak 5.30 W · 996 samples

    ```mermaid
    xychart-beta
        title "Power — Cubie A5E 01"
        x-axis "sample" 1 --> 996
        y-axis "W" 1.0 --> 5.5
        line [3.53, 3.55, 3.55, 3.34, 2.66, 3.64, 3.58, 3.32, 3.04, 3.55, 3.53, 3.72, 3.67, 3.56, 3.66, 3.63, 3.60, 3.54, 3.60, 3.90, 4.31, 3.61, 4.60, 5.20, 4.69, 3.77, 4.11, 5.20, 5.19, 3.89, 3.66, 3.67, 3.69, 3.22, 3.16, 3.60, 3.60, 3.60, 3.60, 3.60]
    ```

??? success "Cubietruck 01 — pass"

    `cubietruck` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 261.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 59.5 s | warm · up 41 s |
    | hw-performance | ✅ | 60.4 s | AES 19 · mem 1700 · disk W 17 / R 22 MB/s · 48.6 °C · 960 MHz |
    | dvfs | ✅ | 55.9 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 101.6 s | end0 ↑729/↓881 (1GE) · wlan0 ↑19/↓21 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 194.7 s | stable |
    | reboot | ✅ | 62.9 s | warm · up 44 s |
    | store-versions | ✅ | 12.3 s | 26.11.0-trunk.51 · 6.18.44-current-sunxi |

??? success "Cubox i2eX/i4 01 — pass"

    `radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 417.1 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 66.4 s | power-cycle · up 29 s |
    | hw-performance | ✅ | 46.7 s | AES 26 · mem 778 · disk W 19 / R 20 MB/s · 52 °C · 996 MHz |
    | dvfs | ✅ | 40.8 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 78.8 s | end0 ↑392/↓211 (1GE) · wlan0 ↑18/↓14 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 360.4 s | stable |
    | reboot | ✅ | 66.3 s | power-cycle · up 30 s |
    | store-versions | ✅ | 8.7 s | 26.11.0-trunk.51 · 6.18.44-current-imx6 |

??? success "Espressobin 01 — pass"

    `espressobin` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 35.7 s | AES 371 · mem 2000 · disk W 14 / R 142 MB/s · None °C · 800 MHz |
    | dvfs | ✅ | 33.5 s | ondemand · 200–800 MHz (peak 800) |
    | network-iperf | ✅ | 38.1 s | lan0 ↑936/↓745 (1GE) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.2 s | 26.8.3 · 6.18.44-current-mvebu64 |

??? success "Helios4 01 — pass"

    `helios4` · **inplace** · image `26.11.0-trunk.51` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 108.2 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 117.7 s | warm · up 103 s |
    | hw-performance | ✅ | 36.5 s | AES 43 · mem 3800 · disk W 20 / R 23 MB/s · 52.7 °C · None MHz |
    | dvfs | ➖ | 2.3 s | — |
    | network-iperf | ✅ | 31.2 s | end1 ↑939/↓939 (1GE) Mbps |
    | restore-stable | ✅ | 80.6 s | stable |
    | reboot | ✅ | 33.0 s | warm · up 18 s |
    | store-versions | ✅ | 5.4 s | 26.11.0-trunk.51 · 6.6.151-current-mvebu |

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
    | upgrade | ✅ | 84.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 54.6 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 19.5 s | AES 1253 · mem 6900 · disk W 99 / R 155 MB/s · 47.6 °C · 2208 MHz |
    | dvfs | ✅ | 22.3 s | ondemand · 500–2208 MHz (peak 2208) |
    | network-iperf | ✅ | 176.7 s | eth0 ↑845/↓751 (1GE) · wlan0 ↑144/↓63 (Wi-Fi 6) · wlan1 ↑120/↓55 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 59.5 s | stable |
    | reboot | ✅ | 55.0 s | power-cycle · up 22 s |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.51 · 5.15.137-legacy-meson-s4t7 |

    **Power** — min 1.70 W · avg 3.87 W · peak 8.30 W · 381 samples

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

    `mekotronics-r58hd` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 54.3 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 45.6 s | power-cycle · up 15 s |
    | hw-performance | ✅ | 13.5 s | AES 1292 · mem 14000 · disk W 250 / R 290 MB/s · 50.8 °C · 1800 MHz |
    | dvfs | ✅ | 16.3 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 56.3 s | end0 ↑826/↓522 (1GE) · enP3p49s0 ↑933/↓933 (1GE) Mbps |
    | restore-stable | ✅ | 40.6 s | stable |
    | reboot | ✅ | 45.7 s | power-cycle · up 14 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.51 · 6.1.115-vendor-rk35xx |

    **Power** — min 3.50 W · avg 6.00 W · peak 12.20 W · 223 samples

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

    `nanopifire3` · **inplace** · image `26.11.0-trunk.51` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 104.0 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 56.2 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 43.3 s | AES 370 · mem 2000 · disk W 20 / R 22 MB/s · 65 °C · None MHz |
    | dvfs | ➖ | 2.8 s | — |
    | network-iperf | ✅ | 48.0 s | eth0 ↑431/↓822 (1GE) Mbps |
    | restore-stable | ⏭️ | 30.0 s | — |
    | reboot | ✅ | 49.7 s | power-cycle · up 15 s |
    | store-versions | ✅ | 6.3 s | 26.11.0-trunk.51 · 7.2.6-edge-s5p6818 |

??? success "NanoPi K2 01 — pass"

    `nanopik2-s905` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 169.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 39.8 s | warm · up 25 s |
    | hw-performance | ✅ | 32.2 s | AES 51 · mem 3700 · disk W 10 / R 40 MB/s · 61 °C · 2016 MHz |
    | dvfs | ✅ | 21.0 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 72.9 s | end0 ↑934/↓941 (1GE) · wlan0 ↑13/↓24 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 144.0 s | stable |
    | reboot | ✅ | 38.9 s | warm · up 24 s |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.51 · 6.18.44-current-meson64 |

??? success "NanoPi M4V2 01 — pass"

    `nanopim4v2` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 97.3 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 54.5 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 22.6 s | AES 1020 · mem 6600 · disk W 52 / R 60 MB/s · 46.9 °C · 1416 MHz |
    | dvfs | ✅ | 20.1 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 139.7 s | end0 ↑305/↓729 (1GE) · wlan0 ↑153/↓163 (Wi-Fi 5) · wlx803f5d16af63 ↑73/↓116 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 77.3 s | stable |
    | reboot | ✅ | 54.2 s | power-cycle · up 26 s |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.51 · 6.18.44-current-rockchip64 |

    **Power** — min 3.00 W · avg 7.10 W · peak 12.30 W · 376 samples

??? success "NanoPi M5 01 — pass"

    `nanopi-m5` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 117.8 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 52.9 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 18.0 s | AES 1269 · mem 8000 · disk W 64 / R 77 MB/s · 44.4 °C · 2016 MHz |
    | dvfs | ✅ | 18.3 s | ondemand · 2016–2016 MHz (peak 2208) |
    | network-iperf | ✅ | 112.4 s | end0 ↑554/↓423 (1GE) · end1 ↑845/↓764 (1GE) · wlan0 ↑31/↓80 (Wi-Fi 5) · wlx44334c47dec3 ↑34/↓12 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 83.6 s | stable |
    | reboot | ✅ | 45.6 s | power-cycle · up 22 s |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.51 · 6.1.115-vendor-rk35xx |

    **Power** — min 0.60 W · avg 4.71 W · peak 8.20 W · 369 samples

??? failure "NanoPi M6 01 — fail"

    `nanopi-m6` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.64 · reachable=False · port=22 |

    **Power** — min 1.50 W · avg 2.16 W · peak 2.50 W · 42 samples

??? success "NanoPi Neo 2 Black 01 — pass"

    `nanopineo2black` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 128.8 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 51.5 s | power-cycle · up 21 s |
    | hw-performance | ✅ | 30.8 s | AES 636 · mem 3500 · disk W 18 / R 2 MB/s · 62.7 °C · 1368 MHz |
    | dvfs | ✅ | 23.5 s | ondemand · 480–1368 MHz (peak 1368) |
    | network-iperf | ✅ | 34.5 s | end0 ↑665/↓448 (1GE) Mbps |
    | restore-stable | ✅ | 99.1 s | stable |
    | reboot | ✅ | 45.5 s | power-cycle · up 20 s |
    | store-versions | ✅ | 5.2 s | 26.11.0-trunk.51 · 6.18.44-current-sunxi64 |

??? success "NanoPi Neo 3 01 — pass"

    `nanopineo3` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 188.9 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 50.9 s | power-cycle · up 25 s |
    | hw-performance | ✅ | 28.4 s | AES 592 · mem 2400 · disk W 53 / R 2 MB/s · 77.3 °C · 1296 MHz |
    | dvfs | ✅ | 30.4 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 67.8 s | end0 ↑900/↓941 (1GE) · wlx7cdd905518f9 ↑29/↓26 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 149.2 s | stable |
    | reboot | ✅ | 51.9 s | power-cycle · up 26 s |
    | store-versions | ✅ | 6.8 s | 26.11.0-trunk.51 · 6.18.44-current-rockchip64 |

??? success "NanoPi R6S 01 — pass"

    `nanopi-r6s` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 49.8 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 34.5 s | power-cycle · up 12 s |
    | hw-performance | ✅ | 14.3 s | AES 1281 · mem 15400 · disk W 207 / R 274 MB/s · 34.2 °C · 1800 MHz |
    | dvfs | ✅ | 17.1 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 28.5 s | lan2 ↑937/↓918 (1GE) Mbps |
    | restore-stable | ✅ | 35.4 s | stable |
    | reboot | ✅ | 41.2 s | power-cycle · up 11 s |
    | store-versions | ✅ | 4.3 s | 26.11.0-trunk.51 · 6.1.115-vendor-rk35xx |

    **Power** — min 0.70 W · avg 4.01 W · peak 9.30 W · 178 samples

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
    | upgrade | ✅ | 125.4 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 31.7 s | warm · up 17 s |
    | hw-performance | ✅ | 22.6 s | AES 51 · mem 3500 · disk W 34 / R 153 MB/s · 45 °C · 1536 MHz |
    | dvfs | ✅ | 21.9 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 31.0 s | end0 ↑940/↓940 (1GE) Mbps |
    | restore-stable | ✅ | 102.4 s | stable |
    | reboot | ✅ | 31.7 s | warm · up 17 s |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.51 · 6.18.44-current-meson64 |

??? success "Odroid C4 01 — pass"

    `odroidc4` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 115.9 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 46.9 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 21.6 s | AES 980 · mem 5200 · disk W 31 / R 77 MB/s · 40.7 °C · 2100 MHz |
    | dvfs | ✅ | 19.1 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 60.0 s | end0 ↑834/↓938 (1GE) · wlx24050fdd332b ↑75/↓43 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 97.2 s | stable |
    | reboot | ✅ | 46.1 s | power-cycle · up 17 s |
    | store-versions | ✅ | 4.3 s | 26.11.0-trunk.51 · 6.18.44-current-meson64 |

    **Power** — min 1.00 W · avg 3.40 W · peak 5.00 W · 330 samples

??? success "Odroid M1 01 — pass"

    `odroidm1` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 94.0 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 56.8 s | power-cycle · up 23 s |
    | hw-performance | ✅ | 16.7 s | AES 918 · mem 5100 · disk W 1032 / R 1038 MB/s · 34.4 °C · 1992 MHz |
    | dvfs | ✅ | 21.3 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 67.7 s | eth0 ↑516/↓941 (1GE) · wlx40a5eff39254 ↑212/↓215 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 72.3 s | stable |
    | reboot | ✅ | 54.7 s | power-cycle · up 22 s |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.51 · 6.18.44-current-rockchip64 |

    **Power** — min 1.90 W · avg 6.26 W · peak 10.70 W · 300 samples

??? success "Odroid N2 01 — pass"

    `odroidn2` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 107.1 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 63.5 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 19.5 s | AES 1085 · mem 4900 · disk W 24 / R 136 MB/s · 37.5 °C · 1992 MHz |
    | dvfs | ✅ | 16.9 s | performance · 1000–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 31.2 s | end0 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 73.6 s | stable |
    | reboot | ✅ | 56.4 s | power-cycle · up 28 s |
    | store-versions | ✅ | 3.6 s | 26.11.0-trunk.51 · 6.18.44-current-meson64 |

    **Power** — min 1.00 W · avg 3.61 W · peak 9.60 W · 299 samples

??? success "Odroid XU4 01 — pass"

    `odroidxu4` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 291.4 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.51 |
    | reboot | ✅ | 62.5 s | power-cycle · up 36 s |
    | hw-performance | ✅ | 37.9 s | AES 68 · mem 5800 · disk W 1 / R 54 MB/s · 61 °C · 1400 MHz |
    | dvfs | ✅ | 30.6 s | ondemand · 600–1400 MHz (peak 2000) |
    | network-iperf | ✅ | 40.8 s | enx001e0636e380 ↑923/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 132.0 s | stable |
    | reboot | ✅ | 56.9 s | power-cycle · up 32 s |
    | store-versions | ✅ | 7.1 s | 26.11.0-trunk.51 · 6.6.151-current-odroidxu4 |

??? failure "Orange Pi 3 01 — fail"

    `orangepi3` · **inplace** · image `26.11.0-trunk.49` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 55.0 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ❌ | 196.3 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

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

    `orangepi5-plus` · **inplace** · image `26.11.0-trunk.51` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 5.6 s | — |
    | reboot | ✅ | 62.2 s | power-cycle · up 37 s |
    | hw-performance | ✅ | 24.9 s | AES 1267 · mem 13600 · disk W 20 / R 22 MB/s · 54.5 °C · 1800 MHz |
    | dvfs | ✅ | 16.3 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 59.6 s | enP3p49s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑405/↓399 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 4.7 s | — |
    | reboot | ✅ | 51.8 s | power-cycle · up 27 s |
    | store-versions | ✅ | 4.3 s | 26.11.0-trunk.51 · 6.1.172-vendor-rk35xx |

    **Power** — min 0.60 W · avg 5.52 W · peak 10.80 W · 182 samples

??? success "Orange Pi Lite 2 01 — pass"

    `orangepilite2` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 212.6 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 55.8 s | warm · up 39 s |
    | hw-performance | ✅ | 30.0 s | AES 798 · mem 6300 · disk W 21 / R 23 MB/s · 75.3 °C · 1800 MHz |
    | dvfs | ✅ | 24.7 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 38.9 s | wlan0 ↑24/↓22 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 168.2 s | stable |
    | reboot | ✅ | 52.0 s | warm · up 34 s |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.51 · 6.12.103-legacy-sunxi64 |

??? success "Orange Pi One+ 01 — pass"

    `orangepioneplus` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 130.3 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 36.7 s | warm · up 18 s |
    | hw-performance | ✅ | 29.6 s | AES 834 · mem 4600 · disk W 21 / R 23 MB/s · 59.2 °C · 1800 MHz |
    | dvfs | ✅ | 22.7 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 62.9 s | end0 ↑912/↓941 (1GE) · wlx00e04c881724 ↑131/↓169 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 95.9 s | stable |
    | reboot | ✅ | 37.4 s | warm · up 18 s |
    | store-versions | ✅ | 5.1 s | 26.11.0-trunk.51 · 7.1.8-edge-sunxi64 |

??? failure "Orange Pi PC2 01 — fail"

    `orangepipc2` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.58 · reachable=False · port=22 |

??? success "Orange Pi Prime 01 — pass"

    `orangepiprime` · **inplace** · image `26.11.0-trunk.51` · 3 ✅ · 0 ❌ · 5 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 44.3 s | AES 379 · mem 2100 · disk W 21 / R 23 MB/s · 42 °C · None MHz |
    | dvfs | ➖ | 2.9 s | — |
    | network-iperf | ✅ | 124.7 s | end0 ↑885/↓713 (1GE) · wlan0 ↑31/↓26 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 6.7 s | 26.11.0-trunk.51 · 6.18.51-current-sunxi64 |

??? success "Orange Pi Zero2 01 — pass"

    `orangepizero2` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 87.3 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 45.5 s | power-cycle · up 19 s |
    | hw-performance | ✅ | 32.6 s | AES 700 · mem 3000 · disk W 21 / R 23 MB/s · 59.8 °C · 1512 MHz |
    | dvfs | ✅ | 26.4 s | ondemand · 480–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 250.5 s | end0 ↑876/↓941 (1GE) · wlx7c023a625db1 ↑37/↓20 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 63.8 s | stable |
    | reboot | ✅ | 44.3 s | power-cycle · up 19 s |
    | store-versions | ✅ | 5.9 s | 26.11.0-trunk.27 · 7.1.8-edge-sunxi64 |

??? success "OrangePi 3 LTS 01 — pass"

    `orangepi3-lts` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 20.8 s | AES 750 · mem 4100 · disk W 54 / R 127 MB/s · 62.6 °C · 1608 MHz |
    | dvfs | ✅ | 21.6 s | ondemand · 480–1608 MHz (peak 1608) |
    | network-iperf | ✅ | 66.3 s | end0 ↑916/↓940 (1GE) · wlan0 ↑127/↓114 (Wi-Fi 5) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.8 s | 26.8.3 · 7.1.8-edge-sunxi64 |

    **Power** — min 2.50 W · avg 3.41 W · peak 4.50 W · 96 samples

??? success "Radxa Dragon Q6A 01 — pass"

    `radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 199.9 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 138.0 s | power-cycle · up 106 s |
    | hw-performance | ✅ | 13.0 s | AES 1514 · mem 18500 · disk W 234 / R 1135 MB/s · 49.2 °C · 1958 MHz |
    | dvfs | ✅ | 13.4 s | ondemand · 300–1958 MHz (peak 2707) |
    | network-iperf | ✅ | 28.0 s | enp1s0 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 66.6 s | stable |
    | reboot | ✅ | 138.9 s | power-cycle · up 106 s |
    | store-versions | ✅ | 4.2 s | 26.11.0-trunk.51 · 6.18.2-current-qcs6490 |

    **Power** — min 1.10 W · avg 2.40 W · peak 7.60 W · 487 samples

??? success "Radxa ZERO 3 01 — pass"

    `radxa-zero3` · **inplace** · image `26.5.1` · 3 ✅ · 1 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 37.4 s | AES 720 · mem 3900 · disk W 21 / R 22 MB/s · 51.2 °C · 1416 MHz |
    | dvfs | ✅ | 77.6 s | ondemand · 408–1416 MHz (peak 1416) |
    | network-iperf | ❌ | 50.7 s | wlan0 ↑0/↓1 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 8.7 s | 26.5.1 · 6.18.44-current-rockchip64 |

??? success "Raspberry Pi 3B — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 251.7 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 50.7 s | warm · up 34 s |
    | hw-performance | ✅ | 45.9 s | AES 20 · mem 1400 · disk W 20 / R 22 MB/s · 54.8 °C · 1200 MHz |
    | dvfs | ✅ | 38.4 s | ondemand · 600–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 98.7 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑24/↓24 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 202.2 s | stable |
    | reboot | ✅ | 48.1 s | warm · up 30 s |
    | store-versions | ✅ | 9.1 s | 26.11.0-trunk.51 · 6.18.44-current-bcm2711 |

??? success "Raspberry Pi 5B — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 46.4 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 54.1 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 14.6 s | AES 1368 · mem 12100 · disk W 54 / R 87 MB/s · 68.8 °C · 2400 MHz |
    | dvfs | ✅ | 13.4 s | ondemand · 1500–2400 MHz (peak 2400) |
    | network-iperf | ✅ | 52.1 s | end0 ↑935/↓941 (1GE) · wlan0 ↑47/↓37 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 42.2 s | stable |
    | reboot | ✅ | 45.8 s | power-cycle · up 22 s |
    | store-versions | ✅ | 3.3 s | 26.11.0-trunk.51 · 6.18.44-current-bcm2711 |

    **Power** — min 2.60 W · avg 5.94 W · peak 10.20 W · 217 samples

??? success "Raspberry Pi Zero 2W — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 202.9 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 40.1 s | warm · up 24 s |
    | hw-performance | ✅ | 33.6 s | AES 33 · mem 2200 · disk W 3 / R 23 MB/s · 54.8 °C · 1000 MHz |
    | dvfs | ✅ | 26.9 s | ondemand · 600–1000 MHz (peak 1000) |
    | network-iperf | ✅ | 41.9 s | wlan0 ↑37/↓24 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 162.3 s | stable |
    | reboot | ✅ | 38.8 s | warm · up 23 s |
    | store-versions | ✅ | 6.3 s | 26.11.0-trunk.51 · 6.18.44-current-bcm2711 |

??? success "ROCK 2F 01 — pass"

    `rock-2f` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 30.4 s | AES 824 · mem 5900 · disk W 15 / R 65 MB/s · 47.8 °C · 2016 MHz |
    | dvfs | ✅ | 23.4 s | ondemand · 408–2016 MHz (peak 2016) |
    | network-iperf | ✅ | 40.4 s | wlan0 ↑211/↓218 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 5.1 s | 26.5.1 · 6.1.115-vendor-rk35xx |

??? success "Rock 5B 01 — pass"

    `rock-5b` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 79.4 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 52.6 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 20.5 s | AES 1286 · mem 11000 · disk W 24 / R 80 MB/s · 64.7 °C · 1800 MHz |
    | dvfs | ✅ | 14.9 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 29.3 s | enP4p65s0 ↑941/↓942 (1GE) Mbps |
    | restore-stable | ✅ | 68.6 s | stable |
    | reboot | ✅ | 52.0 s | power-cycle · up 20 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.51 · 6.18.44-current-rockchip64 |

    **Power** — min 0.70 W · avg 5.78 W · peak 13.50 W · 255 samples

??? success "Rock 5B 02 — pass"

    `rock-5b` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 75.8 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 54.6 s | power-cycle · up 20 s |
    | hw-performance | ✅ | 17.9 s | AES 1284 · mem 11000 · disk W 62 / R 73 MB/s · 64.7 °C · 1800 MHz |
    | dvfs | ✅ | 15.1 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 55.7 s | enP4p65s0 ↑941/↓942 (1GE) · wlP2p33s0 ↑637/↓263 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 63.1 s | stable |
    | reboot | ✅ | 52.3 s | power-cycle · up 20 s |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.51 · 6.18.44-current-rockchip64 |

    **Power** — min 4.00 W · avg 6.04 W · peak 13.70 W · 254 samples

??? success "Rock 5B Plus 01 — pass"

    `rock-5b-plus` · **inplace** · image `26.11.0-trunk.54` · 16 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 22.8 s | nightly · 26.11.0-trunk.54 → 26.11.0-trunk.54 |
    | reboot | ✅ | 53.5 s | power-cycle · up 27 s |
    | kernel-switch | ✅ | 16.3 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 47.9 s | power-cycle · up 23 s |
    | hw-performance | ✅ | 16.0 s | AES 1295 · mem 14200 · disk W 66 / R 81 MB/s · 54.5 °C · 1800 MHz |
    | dvfs | ✅ | 16.3 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 28.0 s | enP4p65s0 ↑941/↓940 (1GE) Mbps |
    | store-versions | ✅ | 3.6 s | 26.11.0-trunk.54 · 6.1.172-vendor-rk35xx |
    | kernel-switch | ✅ | 88.1 s | branch=current · family=rockchip64 · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.18.52-current-rockchip64 · kernel_before=6.1.172-vendor-rk35xx |
    | reboot | ✅ | 48.8 s | power-cycle · up 23 s |
    | hw-performance | ✅ | 18.2 s | AES 1280 · mem 7700 · disk W 66 / R 72 MB/s · 55.5 °C · 1800 MHz |
    | dvfs | ✅ | 15.1 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 28.3 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
    | store-versions | ✅ | 4.1 s | 26.11.0-trunk.54 · 6.18.52-current-rockchip64 |
    | kernel-switch | ✅ | 57.0 s | branch=vendor · family=rk35xx · installed=26.11.0-trunk.54 · boot_image=vmlinuz-6.1.172-vendor-rk35xx · kernel_before=6.18.52-current-rockchip64 |
    | reboot | ✅ | 47.9 s | power-cycle · up 23 s |

    **Power** — min 0.90 W · avg 4.45 W · peak 11.20 W · 410 samples

    ```mermaid
    xychart-beta
        title "Power — Rock 5B Plus 01"
        x-axis "sample" 1 --> 410
        y-axis "W" 0.5 --> 11.5
        line [3.00, 3.00, 4.25, 3.98, 3.15, 3.47, 4.24, 4.16, 3.33, 3.01, 3.51, 4.00, 3.48, 6.56, 3.43, 3.87, 3.98, 3.51, 3.78, 4.01, 3.67, 3.45, 3.40, 3.75, 2.61, 2.64, 5.01, 5.91, 6.76, 8.28, 6.08, 5.84, 5.83, 6.47, 6.06, 6.49, 6.17, 5.60, 3.46, 4.65]
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
    | upgrade | ✅ | 189.2 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 54.3 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 32.0 s | AES 599 · mem 3300 · disk W 21 / R 23 MB/s · 60.4 °C · 1296 MHz |
    | dvfs | ✅ | 24.9 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 87.7 s | end0 ↑941/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑91/↓200 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 146.7 s | stable |
    | reboot | ✅ | 49.7 s | power-cycle · up 24 s |
    | store-versions | ✅ | 6.3 s | 26.11.0-trunk.51 · 6.18.44-current-rockchip64 |

??? failure "RockPro 64 01 — fail"

    `rockpro64` · **inplace** · image `26.11.0-trunk.51` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.31 · reachable=False · port=22 |

??? success "SpacemiT K3 Pico-ITX 01 — pass"

    `k3picoitx` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 68.4 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 62.5 s | power-cycle · up 41 s |
    | hw-performance | ✅ | 12.3 s | AES 778 · mem 12800 · disk W 1328 / R 1454 MB/s · 43 °C · 2150 MHz |
    | dvfs | ✅ | 14.3 s | performance · 614–2150 MHz (peak 2150) |
    | network-iperf | ✅ | 93.8 s | eth0 ↑937/↓942 (1GE) · wlan0 ↑27/↓149 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 33.9 s | stable |
    | reboot | ✅ | 51.0 s | power-cycle · up 29 s |
    | store-versions | ✅ | 3.4 s | 26.11.0-trunk.51 · 6.18.3-legacy-spacemit-k3 |

??? success "Tinker Board 01 — pass"

    `tinkerboard` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 84.5 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 58.7 s | power-cycle · up 32 s |
    | hw-performance | ✅ | 27.9 s | AES 67 · mem 3300 · disk W 14 / R 63 MB/s · 59.5 °C · 1800 MHz |
    | dvfs | ✅ | 20.2 s | ondemand · 600–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 63.7 s | end0 ↑941/↓941 (1GE) · wlan0 ↑18/↓27 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 65.1 s | stable |
    | reboot | ✅ | 62.2 s | power-cycle · up 29 s |
    | store-versions | ✅ | 4.5 s | 26.11.0-trunk.51 · 6.18.44-current-rockchip |

    **Power** — min 1.30 W · avg 3.91 W · peak 8.40 W · 310 samples

??? success "Udoo 01 — pass"

    `udoo` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 461.4 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 65.6 s | power-cycle · up 32 s |
    | hw-performance | ✅ | 50.9 s | AES 26 · mem 718 · disk W 19 / R 20 MB/s · 49.2 °C · 996 MHz |
    | dvfs | ✅ | 43.5 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 81.6 s | end0 ↑400/↓232 (1GE) · wlx7cdd903aa418 ↑34/↓34 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 444.8 s | stable |
    | reboot | ✅ | 73.3 s | power-cycle · up 33 s |
    | store-versions | ✅ | 9.5 s | 26.11.0-trunk.51 · 6.18.44-current-imx6 |

    **Power** — min 1.30 W · avg 5.74 W · peak 8.40 W · 1004 samples

??? failure "UEFI arm64 01 — fail"

    `uefi-arm64` · **inplace** · image `26.11.0-trunk.30` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.45 · reachable=False · port=22 |

??? success "UEFI x86 01 — pass"

    `uefi-x86` · **inplace** · image `26.11.0-trunk.51` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 183.0 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 92.6 s | power-cycle · up 58 s |
    | hw-performance | ✅ | 25.6 s | AES 237 · mem 5800 · disk W 24 / R 104 MB/s · 61 °C · 1920 MHz |
    | dvfs | ❌ | 23.3 s | schedutil · 480–1920 MHz (peak 1680) |
    | network-iperf | ✅ | 66.9 s | enp1s0 ↑911/↓941 (1GE) · wlan0 ↑35/↓32 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 161.5 s | stable |
    | reboot | ✅ | 87.0 s | power-cycle · up 56 s |
    | store-versions | ✅ | 5.2 s | 26.11.0-trunk.51 · 6.18.44-current-x86 |

    **Power** — min 2.00 W · avg 4.10 W · peak 6.90 W · 520 samples

??? success "ZeroPi 01 — pass"

    `zeropi` · **inplace** · image `26.11.0-trunk.51` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 189.6 s | nightly · 26.11.0-trunk.51 → 26.11.0-trunk.51 |
    | reboot | ✅ | 54.9 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 39.5 s | AES 25 · mem 1500 · disk W 2 / R 23 MB/s · 47.3 °C · 1296 MHz |
    | dvfs | ✅ | 33.8 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 38.6 s | end0 ↑638/↓934 (1GE) Mbps |
    | restore-stable | ✅ | 148.3 s | stable |
    | reboot | ✅ | 54.9 s | power-cycle · up 25 s |
    | store-versions | ✅ | 7.9 s | 26.11.0-trunk.51 · 6.18.44-current-sunxi |

    **Power** — min 1.20 W · avg 2.12 W · peak 3.40 W · 460 samples


<!-- FLEET-STOP -->
