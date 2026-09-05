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

**64** boards — **49** passed, **15** failed. Each card is the board's most recent test.

??? success "Arduino UNO Q 01 — pass"

    `arduino-uno-q` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 158.6 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 50.3 s | warm · up 33 s |
    | hw-performance | ✅ | 24.4 s | AES 934 · mem 5100 · disk W 174 / R 245 MB/s · 44.6 °C · 2016 MHz |
    | dvfs | ✅ | 32.0 s | schedutil · 300–2016 MHz (peak 2016) |
    | network-iperf | ❌ | 326.9 s | usb0 ↑0/↓0 (1GE) · wlan0 ↑17/↓20 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 102.2 s | stable |
    | reboot | ✅ | 49.8 s | warm · up 33 s |
    | store-versions | ✅ | 6.9 s | 26.11.0-trunk.27 · 7.1.8-edge-qrb2210 |

??? success "Banana Pi CM4IO 01 — pass"

    `bananapicm4io` · **inplace** · image `26.8.3` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 369.5 s | nightly · 26.8.3 → 26.8.3 |
    | reboot | ✅ | 60.4 s | power-cycle · up 23 s |
    | hw-performance | ✅ | 18.3 s | AES 851 · mem 3900 · disk W 35 / R 152 MB/s · 57.2 °C · 2016 MHz |
    | dvfs | ✅ | 18.0 s | ondemand · 1000–1512 MHz (peak 1512) |
    | network-iperf | ❌ | 408.3 s | eth0 ↑940/↓941 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) · wlx00e032c00694 ↑0/↓0 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 166.9 s | stable |
    | reboot | ✅ | 48.4 s | power-cycle · up 23 s |
    | store-versions | ✅ | 3.9 s | 26.8.3 · 6.18.44-current-meson64 |

??? failure "Banana Pi M2 Ultra 01 — fail"

    `bananapim2ultra` · **inplace** · image `26.11.0-trunk.27` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 106.1 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ❌ | 200.8 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Banana Pi M2Pro 01 — pass"

    `bananapim2pro` · **inplace** · image `26.11.0-trunk.35` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 103.5 s | nightly · 26.11.0-trunk.35 → 26.11.0-trunk.35 |
    | reboot | ✅ | 48.2 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 20.1 s | AES 980 · mem 5200 · disk W 42 / R 153 MB/s · 53.4 °C · 2100 MHz |
    | dvfs | ✅ | 19.9 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 57.5 s | end0 ↑941/↓941 (1GE) · wlx60fb00480eb0 ↑190/↓209 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 80.5 s | stable |
    | reboot | ✅ | 43.3 s | power-cycle · up 18 s |
    | store-versions | ✅ | 4.5 s | 26.11.0-trunk.35 · 6.18.44-current-meson64 |

??? success "Banana Pi M5 01 — pass"

    `bananapim5` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 186.5 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 171.7 s | warm · up 154 s |
    | hw-performance | ✅ | 38.5 s | AES 980 · mem 5200 · disk W 10 / R 15 MB/s · 53.5 °C · 2100 MHz |
    | dvfs | ✅ | 20.8 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 92.7 s | end0 ↑940/↓941 (1GE) · wlx000f13960190 ↑1/↓10 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 145.7 s | stable |
    | reboot | ✅ | 168.0 s | warm · up 150 s |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? failure "Banana Pi M7 01 — fail"

    `bananapim7` · **inplace** · image `26.8.3` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 134.7 s | nightly · 26.8.3 → 26.11.0-trunk.35 |
    | reboot | ❌ | 209.6 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

    **Power** — idle 3.50 W · avg 4.53 W · peak 9.60 W · 107 samples

??? success "Banana Pi Pro 01 — pass"

    `bananapipro` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 283.7 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 67.6 s | warm · up 47 s |
    | hw-performance | ✅ | 50.1 s | AES 19 · mem 1700 · disk W 19 / R 20 MB/s · 50 °C · 960 MHz |
    | dvfs | ✅ | 47.9 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 249.0 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑19/↓12 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 191.0 s | stable |
    | reboot | ✅ | 64.5 s | warm · up 44 s |
    | store-versions | ✅ | 11.6 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi |

??? success "BananaPi BPI-F3 01 — pass"

    `bananapif3` · **inplace** · image `26.11.0-trunk.35` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 138.4 s | nightly · 26.11.0-trunk.35 → 26.11.0-trunk.35 |
    | reboot | ✅ | 46.9 s | power-cycle · up 17 s |
    | hw-performance | ✅ | 22.3 s | AES 30 · mem 3400 · disk W 60 / R 83 MB/s · 64 °C · 1800 MHz |
    | dvfs | ✅ | 23.3 s | performance · 614–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 113.4 s | eth0 ↑941/↓941 (1GE) · eth1 ↑941/↓941 (1GE) · wlan0 ↑301/↓313 (Wi-Fi 6) · wlan1 ↑274/↓247 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 92.5 s | stable |
    | reboot | ✅ | 46.6 s | power-cycle · up 18 s |
    | store-versions | ✅ | 5.3 s | 26.11.0-trunk.35 · 6.18.44-current-spacemit |

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

    **Power** — idle 0.80 W · avg 1.92 W · peak 3.60 W · 548 samples

??? success "Clearfog Pro 01 — pass"

    `clearfogpro` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 198.8 s | nightly · 26.8.3 → 26.11.0-trunk.27 |
    | reboot | ✅ | 36.6 s | warm · up 20 s |
    | hw-performance | ✅ | 42.8 s | AES 44 · mem 3700 · disk W 21 / R 23 MB/s · 67 °C · None MHz |
    | dvfs | ➖ | 3.0 s | — |
    | network-iperf | ✅ | 55.6 s | lan2 ↑936/↓936 Mbps |
    | restore-stable | ✅ | 110.7 s | stable |
    | reboot | ✅ | 38.6 s | warm · up 22 s |
    | store-versions | ✅ | 6.4 s | 26.11.0-trunk.27 · 6.6.151-current-mvebu |

??? success "Cubie A5E 01 — pass"

    `radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.27` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 36.3 s | — |
    | reboot | ✅ | 144.3 s | power-cycle · up 110 s |
    | hw-performance | ✅ | 46.1 s | AES 358 · mem 2000 · disk W 10 / R 23 MB/s · 66.1 °C · None MHz |
    | dvfs | ➖ | 10.1 s | — |
    | network-iperf | ✅ | 58.8 s | end0 ↑910/↓941 (1GE) · end1 ↑941/↓940 (1GE) Mbps |
    | restore-stable | ✅ | 34.2 s | stable |
    | reboot | ✅ | 143.6 s | power-cycle · up 112 s |
    | store-versions | ✅ | 13.3 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi64 |

    **Power** — idle 2.70 W · avg 4.10 W · peak 4.70 W · 394 samples

??? success "Cubietruck 01 — pass"

    `cubietruck` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 285.7 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 66.4 s | warm · up 45 s |
    | hw-performance | ✅ | 61.2 s | AES 18 · mem 1600 · disk W 14 / R 21 MB/s · 46.4 °C · 960 MHz |
    | dvfs | ✅ | 55.9 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 308.7 s | end0 ↑726/↓844 (1GE) · wlan0 ↑18/↓15 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 190.2 s | stable |
    | reboot | ✅ | 65.4 s | warm · up 43 s |
    | store-versions | ✅ | 12.7 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi |

??? success "Cubox i2eX/i4 01 — pass"

    `radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 309.5 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 51.3 s | warm · up 32 s |
    | hw-performance | ✅ | 46.8 s | AES 26 · mem 756 · disk W 19 / R 20 MB/s · 52.6 °C · 996 MHz |
    | dvfs | ✅ | 40.4 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 142.9 s | end0 ↑393/↓479 (1GE) · wlan0 ↑19/↓11 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 263.8 s | stable |
    | reboot | ✅ | 49.5 s | warm · up 30 s |
    | store-versions | ✅ | 8.7 s | 26.11.0-trunk.27 · 6.18.44-current-imx6 |

??? success "Espressobin 01 — pass"

    `espressobin` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 38.5 s | AES 370 · mem 2000 · disk W 13 / R 134 MB/s · None °C · 800 MHz |
    | dvfs | ✅ | 33.6 s | ondemand · 200–800 MHz (peak 800) |
    | network-iperf | ✅ | 38.7 s | lan0 ↑936/↓749 (1GE) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 8.0 s | 26.8.3 · 6.18.44-current-mvebu64 |

??? success "Helios4 01 — pass"

    `helios4` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 124.3 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 37.0 s | warm · up 19 s |
    | hw-performance | ✅ | 41.8 s | AES 43 · mem 3700 · disk W 21 / R 23 MB/s · 56.1 °C · None MHz |
    | dvfs | ➖ | 2.8 s | — |
    | network-iperf | ✅ | 311.3 s | end1 ↑941/↓941 (1GE) · wlx1cbfce1f85a5 ↑189/↓236 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 87.0 s | stable |
    | reboot | ✅ | 39.8 s | warm · up 22 s |
    | store-versions | ✅ | 5.7 s | 26.11.0-trunk.27 · 6.6.151-current-mvebu |

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

    `mekotronics-r58hd` · **inplace** · image `26.11.0-trunk.35` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 20.7 s | nightly · 26.11.0-trunk.35 → 26.11.0-trunk.35 |
    | reboot | ✅ | 52.2 s | power-cycle · up 13 s |
    | hw-performance | ✅ | 13.9 s | AES 1303 · mem 9400 · disk W 238 / R 280 MB/s · 48.1 °C · 1800 MHz |
    | dvfs | ✅ | 16.5 s | ondemand · 1200–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 50.3 s | end0 ↑939/↓939 (1GE) · enP3p49s0 ↑939/↓939 (1GE) Mbps |
    | restore-stable | ✅ | 39.8 s | stable |
    | reboot | ✅ | 45.5 s | power-cycle · up 15 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.35 · 6.1.115-vendor-rk35xx |

    **Power** — idle 3.20 W · avg 5.68 W · peak 11.70 W · 192 samples

??? success "Mekotronics R58S2 01 — pass"

    `mekotronics-r58s2` · **inplace** · image `26.8.3` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 141.0 s | — |
    | reboot | ✅ | 44.1 s | power-cycle · up 16 s |
    | hw-performance | ✅ | 15.0 s | AES 1278 · mem 14000 · disk W 221 / R 273 MB/s · 47.2 °C · 1800 MHz |
    | dvfs | ✅ | 17.5 s | ondemand · 1800–1800 MHz (peak 2352) |
    | network-iperf | ✅ | 28.6 s | end1 ↑939/↓939 (1GE) Mbps |
    | restore-stable | ⏭️ | 139.8 s | — |
    | reboot | ✅ | 50.0 s | power-cycle · up 13 s |
    | store-versions | ✅ | 4.0 s | 26.8.3 · 6.1.115-vendor-rk35xx |

??? failure "NanoPC T6 LTS 01 — fail"

    `nanopct6-lts` · **inplace** · image `26.8.0-trunk.236` · 1 ✅ · 4 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 14.4 s | — |
    | reboot | ❌ | 226.6 s | warm |
    | hw-performance | ✅ | 120.5 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 31.0 s | — |
    | network-iperf | ⏭️ | 68.8 s | no iperf3 on board |
    | restore-stable | ❌ | 31.0 s | stable |
    | reboot | ❌ | 219.3 s | warm |
    | store-versions | ❌ | 25.3 s | — |

??? failure "NanoPi Duo 01 — fail"

    `nanopiduo` · **inplace** · image `26.11.0-trunk.27` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.84 · reachable=False · port=22 |

??? success "NanoPi K2 01 — pass"

    `nanopik2-s905` · **inplace** · image `26.11.0-trunk.35` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 140.3 s | nightly · 26.11.0-trunk.35 → 26.11.0-trunk.35 |
    | reboot | ✅ | 37.7 s | warm · up 18 s |
    | hw-performance | ✅ | 26.4 s | AES 51 · mem 3800 · disk W 24 / R 41 MB/s · 63 °C · 2016 MHz |
    | dvfs | ✅ | 22.3 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 59.4 s | end0 ↑934/↓825 (1GE) · wlan0 ↑13/↓30 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 115.0 s | stable |
    | reboot | ✅ | 45.4 s | warm · up 17 s |
    | store-versions | ✅ | 5.8 s | 26.11.0-trunk.35 · 6.18.44-current-meson64 |

??? success "NanoPi M4V2 01 — pass"

    `nanopim4v2` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 150.0 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 54.7 s | power-cycle · up 28 s |
    | hw-performance | ✅ | 21.5 s | AES 1024 · mem 6600 · disk W 52 / R 62 MB/s · 45.6 °C · 1416 MHz |
    | dvfs | ✅ | 19.7 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 122.0 s | end0 ↑939/↓939 (1GE) · wlan0 ↑169/↓202 (Wi-Fi 5) · wlx803f5d16af63 ↑123/↓185 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 93.4 s | stable |
    | reboot | ✅ | 53.4 s | power-cycle · up 27 s |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

    **Power** — idle 3.00 W · avg 7.11 W · peak 12.30 W · 425 samples

??? failure "NanoPi M5 01 — fail"

    `nanopi-m5` · **inplace** · image `26.11.0-trunk.5` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 55.9 s | nightly · 26.11.0-trunk.5 → 26.11.0-trunk.5 |
    | reboot | ❌ | 209.0 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "NanoPi Neo 2 Black 01 — fail"

    `nanopineo2black` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 105.9 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 200.8 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "NanoPi Neo 3 01 — pass"

    `nanopineo3` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 283.1 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.35 |
    | reboot | ✅ | 61.3 s | power-cycle · up 25 s |
    | hw-performance | ✅ | 28.1 s | AES 570 · mem 2400 · disk W 54 / R 63 MB/s · 80.8 °C · 1296 MHz |
    | dvfs | ✅ | 30.2 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 69.0 s | end0 ↑919/↓941 (1GE) · wlx7cdd905518f9 ↑30/↓23 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 172.7 s | stable |
    | reboot | ✅ | 59.7 s | power-cycle · up 25 s |
    | store-versions | ✅ | 7.0 s | 26.11.0-trunk.35 · 6.18.44-current-rockchip64 |

??? success "NanoPi R1 01 — pass"

    `nanopi-r1` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 41.8 s | AES 25 · mem 2200 · disk W 16 / R 22 MB/s · 43 °C · 1296 MHz |
    | dvfs | ✅ | 33.2 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 74.6 s | end0 ↑709/↓941 (1GE) · wlan0 ↑6/↓9 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.3 s | 26.8.3 · 6.18.44-current-sunxi |

??? failure "Nanopi R2S 01 — fail"

    `nanopi-r2s` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 119.6 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 209.1 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

    **Power** — idle 2.40 W · avg 3.46 W · peak 4.10 W · 268 samples

??? success "NanoPi R6S 01 — pass"

    `nanopi-r6s` · **inplace** · image `26.11.0-trunk.35` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 24.7 s | nightly · 26.11.0-trunk.35 → 26.11.0-trunk.35 |
    | reboot | ✅ | 40.5 s | power-cycle · up 14 s |
    | hw-performance | ✅ | 15.2 s | AES 1265 · mem 13600 · disk W 210 / R 262 MB/s · 47.2 °C · 1800 MHz |
    | dvfs | ✅ | 17.4 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 51.3 s | lan1 ↑2353/↓2354 (2.5GE) · lan2 ↑939/↓939 (1GE) Mbps |
    | restore-stable | ✅ | 38.7 s | stable |
    | reboot | ✅ | 42.3 s | power-cycle · up 15 s |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.35 · 6.1.115-vendor-rk35xx |

    **Power** — idle 2.60 W · avg 5.17 W · peak 11.10 W · 187 samples

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

    `odroidc2` · **inplace** · image `26.8.3` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 208.2 s | nightly · 26.8.3 → 26.11.0-trunk.27 |
    | reboot | ✅ | 28.6 s | warm · up 12 s |
    | hw-performance | ✅ | 22.7 s | AES 51 · mem 3500 · disk W 32 / R 143 MB/s · 45 °C · 1536 MHz |
    | dvfs | ✅ | 22.0 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 68.2 s | end0 ↑939/↓600 (1GE) Mbps |
    | restore-stable | ✅ | 115.9 s | stable |
    | reboot | ✅ | 28.5 s | warm · up 12 s |
    | store-versions | ✅ | 5.0 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? success "Odroid C4 01 — pass"

    `odroidc4` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 126.7 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 41.1 s | power-cycle · up 17 s |
    | hw-performance | ✅ | 21.4 s | AES 981 · mem 5300 · disk W 30 / R 76 MB/s · 44 °C · 2100 MHz |
    | dvfs | ✅ | 19.4 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 110.8 s | end0 ↑941/↓942 (1GE) · wlx24050fdd332b ↑21/↓31 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 102.8 s | stable |
    | reboot | ✅ | 41.0 s | power-cycle · up 17 s |
    | store-versions | ✅ | 4.4 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? success "Odroid M1 01 — pass"

    `odroidm1` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 18.7 s | — |
    | reboot | ✅ | 53.7 s | power-cycle · up 21 s |
    | hw-performance | ✅ | 17.8 s | AES 915 · mem 5000 · disk W 1078 / R 1066 MB/s · 37.2 °C · 1992 MHz |
    | dvfs | ✅ | 22.4 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 259.4 s | eth0 ↑533/↓941 (1GE) · wlx40a5eff39254 ↑209/↓223 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 21.4 s | stable |
    | reboot | ✅ | 53.0 s | power-cycle · up 21 s |
    | store-versions | ✅ | 5.0 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

    **Power** — idle 1.60 W · avg 4.94 W · peak 8.90 W · 359 samples

??? success "Odroid N2 01 — pass"

    `odroidn2` · **inplace** · image `26.11.0-trunk.6` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 10.7 s | — |
    | reboot | ✅ | 54.7 s | power-cycle · up 28 s |
    | hw-performance | ✅ | 19.4 s | AES 1085 · mem 4900 · disk W 27 / R 135 MB/s · 42.4 °C · 1992 MHz |
    | dvfs | ✅ | 17.3 s | performance · 1000–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 28.8 s | end0 ↑940/↓942 (1GE) Mbps |
    | restore-stable | ✅ | 14.8 s | stable |
    | reboot | ✅ | 58.7 s | power-cycle · up 29 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.6 · 6.18.44-current-meson64 |

    **Power** — idle 1.00 W · avg 3.71 W · peak 10.00 W · 165 samples

??? success "Odroid XU4 01 — pass"

    `odroidxu4` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 27.7 s | — |
    | reboot | ✅ | 59.3 s | power-cycle · up 33 s |
    | hw-performance | ✅ | 38.1 s | AES 71 · mem 4200 · disk W 1 / R 54 MB/s · 55 °C · 1400 MHz |
    | dvfs | ✅ | 30.1 s | ondemand · 600–1400 MHz (peak 2000) |
    | network-iperf | ✅ | 61.9 s | enx001e0636e380 ↑924/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 24.1 s | stable |
    | reboot | ✅ | 58.8 s | power-cycle · up 33 s |
    | store-versions | ✅ | 6.7 s | 26.11.0-trunk.27 · 6.6.151-current-odroidxu4 |

??? failure "Orange Pi 3 01 — fail"

    `orangepi3` · **inplace** · image `26.11.0-trunk.27` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 79.2 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ❌ | 207.2 s | power-cycle |
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

    **Power** — idle 1.70 W · avg 2.91 W · peak 8.90 W · 213 samples

??? success "Orange Pi 5 Plus 01 — pass"

    `orangepi5-plus` · **inplace** · image `26.11.0-trunk.35` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 92.1 s | nightly · 26.11.0-trunk.35 → 26.11.0-trunk.35 |
    | reboot | ✅ | 52.8 s | power-cycle · up 25 s |
    | hw-performance | ✅ | 17.4 s | AES 1259 · mem 14200 · disk W 55 / R 63 MB/s · 49.9 °C · 1800 MHz |
    | dvfs | ✅ | 16.0 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 76.6 s | enP3p49s0 ↑2353/↓2329 (2.5GE) · enP4p65s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑572/↓440 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 83.4 s | stable |
    | reboot | ✅ | 53.9 s | power-cycle · up 26 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.35 · 6.1.115-vendor-rk35xx |

    **Power** — idle 2.70 W · avg 6.27 W · peak 12.50 W · 317 samples

??? success "Orange Pi One+ 01 — pass"

    `orangepioneplus` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 19.2 s | — |
    | reboot | ✅ | 34.3 s | warm · up 17 s |
    | hw-performance | ✅ | 30.9 s | AES 833 · mem 4500 · disk W 21 / R 23 MB/s · 58.8 °C · 1800 MHz |
    | dvfs | ✅ | 23.7 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 158.1 s | end0 ↑913/↓941 (1GE) · wlx00e04c881724 ↑138/↓140 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 28.3 s | stable |
    | reboot | ✅ | 33.9 s | warm · up 18 s |
    | store-versions | ✅ | 5.2 s | 26.11.0-trunk.27 · 7.1.8-edge-sunxi64 |

??? failure "Orange Pi PC2 01 — fail"

    `orangepipc2` · **inplace** · image `26.11.0-trunk.27` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 43.3 s | — |
    | reboot | ✅ | 59.8 s | power-cycle · up 34 s |
    | hw-performance | ✅ | 37.5 s | AES 638 · mem 3500 · disk W 9 / R 23 MB/s · 55.5 °C · 1368 MHz |
    | dvfs | ✅ | 23.2 s | ondemand · 480–1368 MHz (peak 1368) |
    | network-iperf | ✅ | 34.4 s | end0 ↑893/↓897 (1GE) Mbps |
    | restore-stable | ❌ | 8.1 s | stable |
    | reboot | ✅ | 55.5 s | power-cycle · up 31 s |
    | store-versions | ✅ | 5.1 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi64 |

??? success "Orange Pi Prime 01 — pass"

    `orangepiprime` · **inplace** · image `26.8.3` · 3 ✅ · 0 ❌ · 5 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 45.2 s | AES 380 · mem 2100 · disk W 21 / R 23 MB/s · 39.6 °C · None MHz |
    | dvfs | ➖ | 3.0 s | — |
    | network-iperf | ✅ | 76.9 s | end0 ↑884/↓899 (1GE) · wlan0 ↑23/↓29 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 6.5 s | 26.8.3 · 6.18.44-current-sunxi64 |

??? success "Orange Pi Zero Plus 01 — pass"

    `orangepizeroplus` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 33.4 s | — |
    | reboot | ✅ | 46.3 s | warm · up 26 s |
    | hw-performance | ✅ | 34.6 s | AES 469 · mem 2600 · disk W 22 / R 23 MB/s · 60.2 °C · 1008 MHz |
    | dvfs | ✅ | 26.9 s | ondemand · 480–1008 MHz (peak 1008) |
    | network-iperf | ✅ | 104.0 s | end0 ↑892/↓936 (1GE) · wlan0 ↑33/↓31 (Wi-Fi 4) · wlan1 ↑32/↓32 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 36.9 s | stable |
    | reboot | ✅ | 45.9 s | warm · up 25 s |
    | store-versions | ✅ | 6.1 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi64 |

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
    | hw-performance | ✅ | 20.9 s | AES 750 · mem 4100 · disk W 55 / R 127 MB/s · 62.8 °C · 1608 MHz |
    | dvfs | ✅ | 21.8 s | ondemand · 480–1608 MHz (peak 1608) |
    | network-iperf | ✅ | 70.4 s | end0 ↑915/↓941 (1GE) · wlan0 ↑140/↓132 (Wi-Fi 5) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 5.4 s | 26.8.3 · 7.1.8-edge-sunxi64 |

??? failure "Pine H64 01 — fail"

    `pineh64` · **inplace** · image `26.8.0-trunk.170` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 289.9 s | nightly · 26.8.0-trunk.170 → 26.11.0-trunk.6 |
    | reboot | ❌ | 201.7 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Radxa Dragon Q6A 01 — pass"

    `radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 10.7 s | — |
    | reboot | ✅ | 135.9 s | power-cycle · up 106 s |
    | hw-performance | ✅ | 13.8 s | AES 1507 · mem 15400 · disk W 225 / R 1090 MB/s · 45.7 °C · 1958 MHz |
    | dvfs | ✅ | 14.7 s | ondemand · 300–1958 MHz (peak 2707) |
    | network-iperf | ✅ | 51.4 s | enp1s0 ↑940/↓116 (1GE) Mbps |
    | restore-stable | ✅ | 11.1 s | stable |
    | reboot | ✅ | 142.4 s | power-cycle · up 112 s |
    | store-versions | ✅ | 3.7 s | 26.11.0-trunk.27 · 6.18.2-current-qcs6490 |

    **Power** — idle 1.00 W · avg 2.05 W · peak 6.50 W · 307 samples

??? success "Radxa ZERO 3 01 — pass"

    `radxa-zero3` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 28.0 s | AES 720 · mem 4000 · disk W None / R None MB/s · 50 °C · 1416 MHz |
    | dvfs | ✅ | 28.7 s | ondemand · 408–1416 MHz (peak 1416) |
    | network-iperf | ✅ | 50.0 s | wlan0 ↑1/↓5 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 8.2 s | 26.5.1 · 6.18.44-current-rockchip64 |

??? success "Raspberry Pi 01 — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 15.5 s | — |
    | reboot | ✅ | 45.7 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 14.9 s | AES 1368 · mem 12100 · disk W 51 / R 88 MB/s · 54 °C · 2400 MHz |
    | dvfs | ✅ | 12.9 s | ondemand · 1500–2400 MHz (peak 2400) |
    | network-iperf | ✅ | 50.5 s | end0 ↑936/↓941 (1GE) · wlan0 ↑45/↓41 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 7.9 s | stable |
    | reboot | ✅ | 40.5 s | power-cycle · up 17 s |
    | store-versions | ✅ | 3.7 s | 26.11.0-trunk.27 · 6.18.44-current-bcm2711 |

    **Power** — idle 2.40 W · avg 4.70 W · peak 8.20 W · 157 samples

??? success "Raspberry Pi 02 — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 33.8 s | — |
    | reboot | ✅ | 48.9 s | warm · up 30 s |
    | hw-performance | ✅ | 40.8 s | AES 20 · mem 1400 · disk W 20 / R 22 MB/s · 54.2 °C · 1200 MHz |
    | dvfs | ✅ | 36.3 s | ondemand · 600–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 203.1 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑24/↓20 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 41.5 s | stable |
    | reboot | ✅ | 50.9 s | warm · up 32 s |
    | store-versions | ✅ | 9.3 s | 26.11.0-trunk.27 · 6.18.44-current-bcm2711 |

??? success "ROCK 2F 01 — pass"

    `rock-2f` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 30.1 s | AES 822 · mem 5900 · disk W 16 / R 65 MB/s · 48.4 °C · 2016 MHz |
    | dvfs | ✅ | 25.7 s | ondemand · 408–2016 MHz (peak 2016) |
    | network-iperf | ✅ | 51.8 s | wlan0 ↑69/↓54 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 5.8 s | 26.5.1 · 6.1.115-vendor-rk35xx |

??? success "Rock 5B 01 — pass"

    `rock-5b` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 10.5 s | — |
    | reboot | ✅ | 47.5 s | power-cycle · up 16 s |
    | hw-performance | ✅ | 20.8 s | AES 1292 · mem 11000 · disk W 23 / R 83 MB/s · 54.5 °C · 1800 MHz |
    | dvfs | ✅ | 15.4 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 55.2 s | enP4p65s0 ↑2352/↓2299 (2.5GE) Mbps |
    | restore-stable | ✅ | 12.8 s | stable |
    | reboot | ✅ | 44.8 s | power-cycle · up 16 s |
    | store-versions | ✅ | 4.1 s | 26.8.3 · 6.18.44-current-rockchip64 |

??? success "Rock 5B 02 — pass"

    `rock-5b` · **inplace** · image `26.11.0-trunk.31` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 7.3 s | — |
    | reboot | ✅ | 31.7 s | warm · up 14 s |
    | hw-performance | ✅ | 17.7 s | AES 1294 · mem 5800 · disk W 65 / R 74 MB/s · 53.6 °C · 1800 MHz |
    | dvfs | ✅ | 16.0 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 55.2 s | enP4p65s0 ↑2353/↓2309 (2.5GE) · wlP2p33s0 ↑752/↓318 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 63.4 s | stable |
    | reboot | ✅ | 29.4 s | warm · up 12 s |
    | store-versions | ✅ | 4.1 s | 26.11.0-trunk.31 · 6.18.44-current-rockchip64 |

??? success "Rock 5B Plus 01 — pass"

    `rock-5b-plus` · **inplace** · image `26.11.0-trunk.31` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 5.8 s | — |
    | reboot | ✅ | 36.7 s | warm · up 15 s |
    | hw-performance | ✅ | 18.4 s | AES 1300 · mem 14200 · disk W 43 / R 82 MB/s · 48.1 °C · 1800 MHz |
    | dvfs | ✅ | 16.1 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 27.9 s | enP4p65s0 ↑2352/↓2352 (2.5GE) Mbps |
    | restore-stable | ✅ | 105.9 s | stable |
    | reboot | ✅ | 34.8 s | warm · up 15 s |
    | store-versions | ✅ | 3.5 s | 26.11.0-trunk.31 · 6.1.115-vendor-rk35xx |

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

    **Power** — idle 0.90 W · avg 9.24 W · peak 16.70 W · 273 samples

??? success "Rockpi E 01 — pass"

    `rockpi-e` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 23.3 s | — |
    | reboot | ✅ | 53.4 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 32.6 s | AES 595 · mem 3200 · disk W 21 / R 23 MB/s · 62.5 °C · 1296 MHz |
    | dvfs | ✅ | 25.6 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 96.5 s | end0 ↑941/↓941 (1GE) · wlx7ca7b020e87c ↑179/↓138 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 30.8 s | stable |
    | reboot | ✅ | 53.3 s | power-cycle · up 24 s |
    | store-versions | ✅ | 5.9 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

??? success "SpacemiT K3 Pico-ITX 01 — pass"

    `k3picoitx` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 22.3 s | AES 796 · mem 12000 · disk W 24 / R 40 MB/s · 61 °C · 2200 MHz |
    | dvfs | ✅ | 15.5 s | performance · 614–2200 MHz (peak 2200) |
    | network-iperf | ✅ | 132.7 s | eth0 ↑941/↓941 (1GE) · wlan0 ↑78/↓154 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 3.7 s | 26.8.3 · 6.18.3-legacy-spacemit-k3 |

    **Power** — idle 13.40 W · avg 14.40 W · peak 22.40 W · 148 samples

??? success "Tinker Board 01 — pass"

    `tinkerboard` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 14.9 s | — |
    | reboot | ✅ | 67.1 s | power-cycle · up 35 s |
    | hw-performance | ✅ | 29.6 s | AES 67 · mem 3300 · disk W 14 / R 63 MB/s · 56.8 °C · 1800 MHz |
    | dvfs | ✅ | 21.2 s | ondemand · 600–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 101.1 s | end0 ↑941/↓941 (1GE) · wlan0 ↑25/↓28 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 18.1 s | stable |
    | reboot | ✅ | 55.2 s | power-cycle · up 30 s |
    | store-versions | ✅ | 4.9 s | 26.8.1 · 6.18.44-current-rockchip |

    **Power** — idle 2.10 W · avg 3.84 W · peak 8.70 W · 243 samples

??? success "Udoo 01 — pass"

    `udoo` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 42.7 s | — |
    | reboot | ✅ | 61.5 s | power-cycle · up 31 s |
    | hw-performance | ✅ | 50.7 s | AES 26 · mem 711 · disk W 13 / R 20 MB/s · 45.8 °C · 996 MHz |
    | dvfs | ✅ | 43.1 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 80.7 s | end0 ↑398/↓222 (1GE) · wlx7cdd903aa418 ↑38/↓30 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 50.5 s | stable |
    | reboot | ✅ | 64.3 s | power-cycle · up 33 s |
    | store-versions | ✅ | 9.1 s | 26.8.1 · 6.18.44-current-imx6 |

    **Power** — idle 1.20 W · avg 5.89 W · peak 8.00 W · 329 samples

??? success "UEFI arm64 01 — pass"

    `uefi-arm64` · **inplace** · image `26.8.0-trunk.314` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 15.7 s | AES 1402 · mem 13000 · disk W 1578 / R 2263 MB/s · 45 °C · 2600 MHz |
    | dvfs | ✅ | 18.6 s | ondemand · 800–2600 MHz (peak 2600) |
    | network-iperf | ✅ | 123.5 s | enp1s0 ↑8788/↓9372 (10GE) · enp49s0 ↑7633/↓9377 (10GE) · wlp97s0 ↑111/↓86 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.4 s | 26.8.0-trunk.314 · 7.1.2-edge-arm64 |

??? success "UEFI x86 01 — pass"

    `uefi-x86` · **inplace** · image `26.11.0-trunk.35` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 181.3 s | nightly · 26.11.0-trunk.35 → 26.11.0-trunk.35 |
    | reboot | ✅ | 92.2 s | power-cycle · up 58 s |
    | hw-performance | ✅ | 26.0 s | AES 237 · mem 4900 · disk W 26 / R 112 MB/s · 63 °C · 1920 MHz |
    | dvfs | ❌ | 23.5 s | schedutil · 480–1920 MHz (peak 1680) |
    | network-iperf | ✅ | 61.3 s | enp1s0 ↑917/↓941 (1GE) · wlan0 ↑34/↓39 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 198.3 s | stable |
    | reboot | ✅ | 98.5 s | power-cycle · up 56 s |
    | store-versions | ✅ | 5.7 s | 26.11.0-trunk.35 · 6.18.44-current-x86 |

    **Power** — idle 0.70 W · avg 4.19 W · peak 6.90 W · 568 samples


<!-- FLEET-STOP -->
