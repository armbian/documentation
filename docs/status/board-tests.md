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

**82** boards — **46** passed, **36** failed. Each card is the board's most recent test.

??? success "Arduino UNO Q 01 — pass"

    `arduino-uno-q` · **inplace** · image `26.8.1` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 265.5 s | nightly · 26.8.1 → 26.11.0-trunk.6 |
    | reboot | ✅ | 48.9 s | warm · up 32 s |
    | hw-performance | ✅ | 24.6 s | AES 940 · mem 5100 · disk W 188 / R 257 MB/s · 41.5 °C · 2016 MHz |
    | dvfs | ✅ | 32.0 s | schedutil · 300–2016 MHz (peak 2016) |
    | network-iperf | ❌ | 184.1 s | usb0 ↑0/↓0 (1GE) · wlan0 ↑11/↓4 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 133.3 s | stable |
    | reboot | ✅ | 51.0 s | warm · up 34 s |
    | store-versions | ✅ | 7.0 s | 26.11.0-trunk.6 · 7.1.7-edge-qrb2210 |

??? success "Banana Pi CM4IO 01 — pass"

    `bananapicm4io` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 277.5 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 49.7 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 26.7 s | AES 1364 · mem 6200 · disk W 18 / R 22 MB/s · 67.8 °C · 2016 MHz |
    | dvfs | ✅ | 16.1 s | performance · 1000–2016 MHz (peak 2400) |
    | network-iperf | ✅ | 171.1 s | end0 ↑938/↓941 (1GE) · wlan0 ↑42/↓34 (Wi-Fi 5) · wlx00e032c00694 ↑195/↓197 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 101.5 s | stable |
    | reboot | ✅ | 47.8 s | power-cycle · up 23 s |
    | store-versions | ✅ | 3.6 s | 26.11.0-trunk.6 · 6.18.43-current-meson64 |

??? success "Banana Pi M2 Ultra 01 — pass"

    `bananapim2ultra` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 560.9 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 37.7 s | warm · up 19 s |
    | hw-performance | ✅ | 40.2 s | AES 23 · mem 2100 · disk W 13 / R 76 MB/s · 56.4 °C · 1200 MHz |
    | dvfs | ✅ | 38.4 s | ondemand · 720–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 76.8 s | end0 ↑823/↓938 (1GE) · wlan0 ↑19/↓7 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 195.2 s | stable |
    | reboot | ✅ | 37.6 s | warm · up 19 s |
    | store-versions | ✅ | 8.7 s | 26.11.0-trunk.6 · 6.12.93-legacy-sunxi |

??? success "Banana Pi M2Pro 01 — pass"

    `bananapim2pro` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 317.7 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 51.4 s | power-cycle · up 23 s |
    | hw-performance | ✅ | 20.6 s | AES 976 · mem 5200 · disk W 42 / R 156 MB/s · 56.6 °C · 2100 MHz |
    | dvfs | ✅ | 20.6 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 75.4 s | end0 ↑941/↓941 (1GE) · wlx60fb00480eb0 ↑69/↓200 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 113.9 s | stable |
    | reboot | ✅ | 51.3 s | power-cycle · up 22 s |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.6 · 6.18.43-current-meson64 |

??? success "Banana Pi M5 01 — pass"

    `bananapim5` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 277.1 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 153.2 s | warm · up 136 s |
    | hw-performance | ✅ | 21.7 s | AES 981 · mem 5000 · disk W 35 / R 152 MB/s · 56.2 °C · 2100 MHz |
    | dvfs | ✅ | 21.2 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 39.9 s | end0 ↑940/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 134.0 s | stable |
    | reboot | ✅ | 152.6 s | warm · up 134 s |
    | store-versions | ✅ | 5.0 s | 26.11.0-trunk.6 · 6.18.43-current-meson64 |

??? success "Banana Pi Pro 01 — pass"

    `bananapipro` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 694.3 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 62.0 s | warm · up 41 s |
    | hw-performance | ✅ | 60.0 s | AES 19 · mem 1600 · disk W 13 / R 21 MB/s · 50.1 °C · 960 MHz |
    | dvfs | ✅ | 55.2 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 161.4 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑18/↓20 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 266.7 s | stable |
    | reboot | ✅ | 61.9 s | warm · up 41 s |
    | store-versions | ✅ | 11.3 s | 26.11.0-trunk.6 · 6.12.93-legacy-sunxi |

??? failure "BananaPi BPI-F3 01 — fail"

    `bananapif3` · **inplace** · image `26.11.0-trunk.6` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 10.5 s | — |
    | reboot | ❌ | 218.3 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

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

??? failure "Clearfog Pro 01 — fail"

    `clearfogpro` · **inplace** · image `26.11.0-trunk.6` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.42 · reachable=False · port=22 |

??? success "Cubie A5E 01 — pass"

    `radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.19` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 30.8 s | — |
    | reboot | ✅ | 139.8 s | power-cycle · up 112 s |
    | hw-performance | ✅ | 46.3 s | AES 358 · mem 2000 · disk W 11 / R 23 MB/s · 66 °C · None MHz |
    | dvfs | ➖ | 2.7 s | — |
    | network-iperf | ✅ | 58.5 s | end0 ↑909/↓941 (1GE) · end1 ↑941/↓940 (1GE) Mbps |
    | restore-stable | ✅ | 43.7 s | stable |
    | reboot | ✅ | 142.1 s | power-cycle · up 110 s |
    | store-versions | ✅ | 12.9 s | 26.11.0-trunk.19 · 6.18.44-current-sunxi64 |

    **Power** — idle 2.30 W · avg 4.07 W · peak 4.70 W · 380 samples

??? success "Cubietruck 01 — pass"

    `cubietruck` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 662.7 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 61.4 s | warm · up 40 s |
    | hw-performance | ✅ | 56.9 s | AES 19 · mem 1700 · disk W 15 / R 22 MB/s · 48.9 °C · 960 MHz |
    | dvfs | ✅ | 55.6 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 207.5 s | end0 ↑732/↓819 (1GE) · wlan0 ↑18/↓26 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 241.6 s | stable |
    | reboot | ✅ | 59.5 s | warm · up 38 s |
    | store-versions | ✅ | 12.6 s | 26.11.0-trunk.6 · 6.18.35-current-sunxi |

??? success "Espressobin 01 — pass"

    `espressobin` · **inplace** · image `26.08.0-trunk` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 36.5 s | AES 371 · mem 2000 · disk W 66 / R 119 MB/s · None °C · 800 MHz |
    | dvfs | ✅ | 35.8 s | ondemand · 200–800 MHz (peak 800) |
    | network-iperf | ✅ | 40.1 s | lan0 ↑930/↓749 (1GE) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.9 s | 26.08.0-trunk · 6.18.42-current-mvebu64 |

??? success "Helios4 01 — pass"

    `helios4` · **inplace** · image `26.8.0-trunk.314` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 308.0 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 37.0 s | warm · up 20 s |
    | hw-performance | ✅ | 40.5 s | AES 43 · mem 3800 · disk W 14 / R 21 MB/s · 59.9 °C · None MHz |
    | dvfs | ➖ | 2.3 s | — |
    | network-iperf | ✅ | 160.6 s | end1 ↑941/↓899 (1GE) · wlx1cbfce1f85a5 ↑164/↓207 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 103.2 s | stable |
    | reboot | ✅ | 38.1 s | warm · up 19 s |
    | store-versions | ✅ | 6.0 s | 26.11.0-trunk.6 · 6.6.142-current-mvebu |

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

??? failure "Khadas VIM2 01 — fail"

    `khadas-vim2` · **inplace** · image `26.8.0-trunk.314` · 2 ✅ · 4 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 252.3 s | nightly · 26.8.0-trunk.314 → 26.8.0-trunk.314 |
    | reboot | ❌ | 203.2 s | warm |
    | hw-performance | ✅ | 155.7 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 6.0 s | — |
    | network-iperf | ⏭️ | 19.7 s | no iperf3 on board |
    | restore-stable | ❌ | 11.2 s | stable |
    | reboot | ❌ | 207.0 s | warm |
    | store-versions | ❌ | 13.4 s | — |

??? success "Khadas VIM3 01 — pass"

    `khadas-vim3` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 316.5 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 32.3 s | warm · up 16 s |
    | hw-performance | ✅ | 18.3 s | AES 851 · mem 3900 · disk W 45 / R 158 MB/s · 48.8 °C · 2016 MHz |
    | dvfs | ✅ | 17.6 s | ondemand · 1000–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 82.3 s | end0 ↑939/↓941 (1GE) · wlan0 ↑31/↓35 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 90.5 s | stable |
    | reboot | ✅ | 32.5 s | warm · up 16 s |
    | store-versions | ✅ | 4.2 s | 26.11.0-trunk.6 · 6.18.43-current-meson64 |

??? failure "Mekotronics R58S2 01 — fail"

    `mekotronics-r58s2` · **inplace** · image `26.5.2` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 251.6 s | nightly · 26.5.2 → 26.11.0-trunk.6 |
    | reboot | ❌ | 202.9 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Minisforum MS R1 — pass"

    `uefi-arm64` · **inplace** · image `26.5.1` · 3 ✅ · 1 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 18.2 s | AES 1458 · mem 13000 · disk W 1586 / R 2009 MB/s · 47 °C · 2600 MHz |
    | dvfs | ❌ | 9.6 s | ondemand · 800–2600 MHz (peak 1540) |
    | network-iperf | ✅ | 79.4 s | enp1s0 ↑7560/↓2751 (10GE) · enp49s0 ↑9250/↓8796 (10GE) · wlp97s0 ↑116/↓89 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.1 s | 26.8.0-trunk.314 · 7.0.11-edge-arm64 |

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

??? success "NanoPi Duo 01 — pass"

    `nanopiduo` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 537.0 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 50.7 s | warm · up 29 s |
    | hw-performance | ✅ | 45.0 s | AES 23 · mem 1400 · disk W 21 / R 22 MB/s · 79.9 °C · 1296 MHz |
    | dvfs | ✅ | 41.7 s | ondemand · 480–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 125.3 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑2/↓12 (Wi-Fi 4) · wlx14cf922b09d8 ↑27/↓29 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 200.7 s | stable |
    | reboot | ✅ | 49.3 s | warm · up 28 s |
    | store-versions | ✅ | 10.2 s | 26.11.0-trunk.6 · 6.12.93-legacy-sunxi |

??? success "NanoPi K2 01 — pass"

    `nanopik2-s905` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 411.5 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 36.9 s | warm · up 19 s |
    | hw-performance | ✅ | 26.6 s | AES 51 · mem 3700 · disk W 26 / R 41 MB/s · 63 °C · 2016 MHz |
    | dvfs | ✅ | 23.3 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 103.8 s | end0 ↑933/↓941 (1GE) · wlan0 ↑13/↓19 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 151.3 s | stable |
    | reboot | ✅ | 35.1 s | warm · up 18 s |
    | store-versions | ✅ | 5.3 s | 26.11.0-trunk.6 · 6.18.43-current-meson64 |

??? success "NanoPi M4V2 01 — pass"

    `nanopim4v2` · **inplace** · image `26.11.0-trunk.5` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 243.2 s | nightly · 26.11.0-trunk.5 → 26.11.0-trunk.6 |
    | reboot | ✅ | 63.2 s | power-cycle · up 36 s |
    | hw-performance | ✅ | 22.6 s | AES 1023 · mem 6600 · disk W 54 / R 61 MB/s · 51.1 °C · 1416 MHz |
    | dvfs | ✅ | 22.1 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 109.2 s | end0 ↑941/↓941 (1GE) · wlan0 ↑179/↓197 (Wi-Fi 5) · wlx803f5d16af63 ↑104/↓224 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 108.4 s | stable |
    | reboot | ✅ | 58.7 s | power-cycle · up 30 s |
    | store-versions | ✅ | 5.3 s | 26.11.0-trunk.6 · 6.18.43-current-rockchip64 |

    **Power** — idle 4.50 W · avg 7.34 W · peak 14.30 W · 515 samples

??? failure "NanoPi M5 01 — fail"

    `nanopi-m5` · **inplace** · image `26.8.0-trunk.314` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 221.6 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.5 |
    | reboot | ❌ | 216.4 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "NanoPi Neo 2 Black 01 — fail"

    `nanopineo2black` · **inplace** · image `26.08.0-trunk` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 387.2 s | nightly · 26.08.0-trunk → 26.11.0-trunk.6 |
    | reboot | ❌ | 201.0 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "NanoPi Neo 3 01 — pass"

    `nanopineo3` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 348.5 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 52.6 s | power-cycle · up 27 s |
    | hw-performance | ✅ | 31.5 s | AES 478 · mem 2300 · disk W 2 / R 62 MB/s · 86.2 °C · 1296 MHz |
    | dvfs | ✅ | 34.1 s | ondemand · 408–1008 MHz (peak 1200) |
    | network-iperf | ✅ | 88.0 s | end0 ↑852/↓938 (1GE) · wlx7cdd905518f9 ↑34/↓22 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 210.9 s | stable |
    | reboot | ✅ | 53.4 s | power-cycle · up 26 s |
    | store-versions | ✅ | 7.2 s | 26.11.0-trunk.6 · 6.18.43-current-rockchip64 |

??? success "NanoPi R1 01 — pass"

    `nanopi-r1` · **inplace** · image `26.08.0-trunk` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 44.7 s | AES 25 · mem 2200 · disk W 13 / R 22 MB/s · 44.4 °C · 1296 MHz |
    | dvfs | ✅ | 35.5 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 76.3 s | end0 ↑709/↓938 (1GE) · wlan0 ↑6/↓16 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.9 s | 26.08.0-trunk · 6.18.38-current-sunxi |

??? success "NanoPi R1 02 — pass"

    `nanopi-r1` · **inplace** · image `26.8.0-trunk.229` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 262.9 s | nightly · 26.8.0-trunk.229 → 26.8.0-trunk.229 |
    | reboot | ✅ | 40.4 s | warm · up 25 s |
    | hw-performance | ✅ | 44.3 s | AES 25 · mem 2000 · disk W 21 / R 22 MB/s · 41.4 °C · 1296 MHz |
    | dvfs | ✅ | 18.4 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 712.1 s | end0 ↑690/↓941 (1GE) · wlx1281394ebbec ↑4/↓10 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 215.7 s | stable |
    | reboot | ✅ | 39.6 s | warm · up 22 s |
    | store-versions | ✅ | 9.3 s | 26.8.0-trunk.229 · 6.18.35-current-sunxi |

??? failure "NanoPi R1 05 — fail"

    `nanopi-r1` · **inplace** · image `5.79` · 1 ✅ · 4 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 15.1 s | — |
    | reboot | ❌ | 203.4 s | warm |
    | hw-performance | ✅ | 38.4 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 8.0 s | — |
    | network-iperf | ⏭️ | 19.6 s | no iperf3 on board |
    | restore-stable | ❌ | 7.2 s | stable |
    | reboot | ❌ | 203.2 s | warm |
    | store-versions | ❌ | 13.4 s | — |

??? failure "NanoPi R1 06 — fail"

    `nanopi-r1` · **inplace** · image `26.5.1` · 2 ✅ · 4 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 456.9 s | nightly · 26.5.1 → 26.8.0-trunk.192 |
    | reboot | ❌ | 201.1 s | warm |
    | hw-performance | ✅ | 38.7 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 7.2 s | — |
    | network-iperf | ⏭️ | 19.8 s | no iperf3 on board |
    | restore-stable | ❌ | 7.3 s | stable |
    | reboot | ❌ | 203.2 s | warm |
    | store-versions | ❌ | 13.5 s | — |

??? success "Nanopi R2S 01 — pass"

    `nanopi-r2s` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 324.5 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 54.2 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 29.7 s | AES 495 · mem 2200 · disk W 54 / R 2 MB/s · 83.5 °C · 1296 MHz |
    | dvfs | ✅ | 32.7 s | ondemand · 408–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 45.4 s | end0 ↑885/↓936 (1GE) Mbps |
    | restore-stable | ✅ | 204.2 s | stable |
    | reboot | ✅ | 57.6 s | power-cycle · up 27 s |
    | store-versions | ✅ | 7.9 s | 26.11.0-trunk.6 · 6.18.43-current-rockchip64 |

    **Power** — idle 2.60 W · avg 3.77 W · peak 4.80 W · 613 samples

??? success "Nanopi R2S 03 — pass"

    `nanopi-r2s` · **inplace** · image `26.5.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 29.3 s | — |
    | reboot | ✅ | 34.2 s | warm · up 20 s |
    | hw-performance | ✅ | 22.9 s | AES 604 · mem 3300 · disk W 56 / R 65 MB/s · 56.4 °C · 1296 MHz |
    | dvfs | ✅ | 11.0 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 290.1 s | end0 ↑940/↓941 (1GE) · enx5a976e130540 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 164.6 s | stable |
    | reboot | ✅ | 34.8 s | warm · up 21 s |
    | store-versions | ✅ | 5.2 s | 26.5.1 · 6.18.35-current-rockchip64 |

??? success "Nanopi R2S 04 — pass"

    `nanopi-r2s` · **inplace** · image `26.8.0-trunk.192` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 19.7 s | — |
    | reboot | ✅ | 34.5 s | warm · up 20 s |
    | hw-performance | ✅ | 23.8 s | AES 603 · mem 3300 · disk W 55 / R 65 MB/s · 68.5 °C · 1296 MHz |
    | dvfs | ✅ | 12.3 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 113.2 s | end0 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 144.4 s | stable |
    | reboot | ✅ | 33.5 s | warm · up 19 s |
    | store-versions | ✅ | 5.2 s | 26.8.0-trunk.192 · 6.18.35-current-rockchip64 |

??? success "NanoPi R4S 01 — pass"

    `nanopi-r4s` · **inplace** · image `26.8.0-trunk.236` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 219.0 s | nightly · 26.8.0-trunk.236 → 26.8.0-trunk.314 |
    | reboot | ✅ | 45.2 s | warm · up 30 s |
    | hw-performance | ✅ | 24.5 s | AES 1015 · mem 6600 · disk W 23 / R 60 MB/s · 38.1 °C · 1416 MHz |
    | dvfs | ✅ | 18.8 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 111.9 s | end0 ↑941/↓941 (1GE) · wlx7cdd905518f9 ↑34/↓28 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 112.7 s | stable |
    | reboot | ✅ | 38.9 s | warm · up 24 s |
    | store-versions | ✅ | 5.6 s | 26.8.0-trunk.314 · 6.18.35-current-rockchip64 |

??? success "NanoPi R6S 01 — pass"

    `nanopi-r6s` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 259.8 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 58.5 s | power-cycle · up 23 s |
    | hw-performance | ✅ | 18.8 s | AES 1267 · mem 7000 · disk W 52 / R 58 MB/s · 50.8 °C · 1800 MHz |
    | dvfs | ✅ | 15.5 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 56.1 s | lan1 ↑2352/↓2286 (2.5GE) · lan2 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 74.2 s | stable |
    | reboot | ✅ | 56.1 s | power-cycle · up 22 s |
    | store-versions | ✅ | 4.0 s | 26.11.0-trunk.6 · 6.18.43-current-rockchip64 |

    **Power** — idle 3.30 W · avg 4.75 W · peak 12.40 W · 429 samples

??? failure "NanoPi R76S 01 — fail"

    `nanopi-r76s` · **inplace** · image `26.11.0-trunk.5` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 139.6 s | nightly · 26.11.0-trunk.5 → 26.11.0-trunk.6 |
    | reboot | ❌ | 200.7 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "NanoPi R76S 02 — pass"

    `nanopi-r76s` · **inplace** · image `26.8.0-trunk.192` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 128.8 s | nightly · 26.8.0-trunk.192 → 26.8.0-trunk.192 |
    | reboot | ✅ | 32.2 s | warm · up 18 s |
    | hw-performance | ✅ | 17.1 s | AES 1272 · mem 7600 · disk W 206 / R 287 MB/s · 45.3 °C · 2016 MHz |
    | dvfs | ✅ | 10.1 s | ondemand · 2016–2016 MHz (peak 2208) |
    | network-iperf | ✅ | 280.6 s | end0 ↑1852/↓2057 · end1 ↑1876/↓2289 · wlan0 ↑42/↓90 Mbps |
    | restore-stable | ✅ | 113.9 s | stable |
    | reboot | ✅ | 31.2 s | warm · up 17 s |
    | store-versions | ✅ | 4.8 s | 26.8.0-trunk.192 · 6.1.115-vendor-rk35xx |

??? failure "Odroid C1 01 — fail"

    `odroidc1` · **inplace** · image `26.8.0-trunk.314` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 207.9 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 11.1 s | — |
    | network-iperf | ⏭️ | 31.4 s | no iperf3 on board |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ❌ | 21.3 s | — |

??? success "Odroid C2 01 — pass"

    `odroidc2` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 565.6 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 45.3 s | warm · up 27 s |
    | hw-performance | ✅ | 38.5 s | AES 51 · mem 3300 · disk W 8 / R 22 MB/s · 48 °C · 1536 MHz |
    | dvfs | ✅ | 22.8 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 31.8 s | end0 ↑940/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 200.9 s | stable |
    | reboot | ✅ | 57.8 s | warm · up 33 s |
    | store-versions | ✅ | 9.8 s | 26.11.0-trunk.6 · 6.18.43-current-meson64 |

??? success "Odroid C4 01 — pass"

    `odroidc4` · **inplace** · image `26.8.1` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 205.1 s | nightly · 26.8.1 → 26.11.0-trunk.6 |
    | reboot | ✅ | 40.1 s | power-cycle · up 16 s |
    | hw-performance | ✅ | 21.5 s | AES 980 · mem 5200 · disk W 31 / R 78 MB/s · 44.4 °C · 2100 MHz |
    | dvfs | ✅ | 19.0 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 83.3 s | end0 ↑940/↓941 (1GE) · wlx24050fdd332b ↑64/↓100 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 112.8 s | stable |
    | reboot | ✅ | 42.8 s | power-cycle · up 16 s |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.6 · 6.18.43-current-meson64 |

??? success "Odroid M1 01 — pass"

    `odroidm1` · **inplace** · image `26.11.0-trunk.6` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 138.5 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ✅ | 54.3 s | power-cycle · up 23 s |
    | hw-performance | ✅ | 17.2 s | AES 914 · mem 5100 · disk W 1074 / R 1050 MB/s · 38.3 °C · 1992 MHz |
    | dvfs | ✅ | 22.7 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 62.5 s | eth0 ↑641/↓941 (1GE) · wlx40a5eff39254 ↑199/↓207 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 105.9 s | stable |
    | reboot | ✅ | 50.5 s | power-cycle · up 19 s |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.6 · 6.18.43-current-rockchip64 |

    **Power** — idle 2.00 W · avg 5.37 W · peak 9.00 W · 341 samples

??? success "Odroid N2 02 — pass"

    `odroidn2` · **inplace** · image `26.5.1` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 200.0 s | nightly · 26.5.1 → 26.8.0-trunk.314 |
    | reboot | ⏭️ | 3.2 s | power-cycle |
    | hw-performance | ✅ | 32.8 s | AES 1365 · mem 6200 · disk W 17 / R 22 MB/s · 39.6 °C · 2016 MHz |
    | dvfs | ✅ | 15.6 s | performance · 1000–2016 MHz (peak 2400) |
    | network-iperf | ✅ | 42.4 s | end0 ↑940/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 94.6 s | stable |
    | reboot | ⏭️ | 3.3 s | power-cycle |
    | store-versions | ✅ | 3.5 s | 26.8.0-trunk.314 · 6.18.34-current-meson64 |

??? success "Odroid N2 03 — pass"

    `odroidn2` · **inplace** · image `26.8.1` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 189.0 s | nightly · 26.8.1 → 26.11.0-trunk.6 |
    | reboot | ✅ | 39.4 s | warm · up 25 s |
    | hw-performance | ✅ | 19.1 s | AES 1085 · mem 4900 · disk W 26 / R 135 MB/s · 44 °C · 1992 MHz |
    | dvfs | ✅ | 17.6 s | performance · 1000–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 28.9 s | end0 ↑939/↓942 (1GE) Mbps |
    | restore-stable | ✅ | 83.9 s | stable |
    | reboot | ✅ | 38.3 s | warm · up 24 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.6 · 6.18.43-current-meson64 |

??? success "Odroid XU4 01 — pass"

    `odroidxu4` · **inplace** · image `26.11.0-trunk.5` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 350.7 s | nightly · 26.11.0-trunk.5 → 26.11.0-trunk.6 |
    | reboot | ✅ | 60.2 s | power-cycle · up 33 s |
    | hw-performance | ✅ | 38.2 s | AES 70 · mem 4500 · disk W 1 / R 50 MB/s · 63 °C · 1400 MHz |
    | dvfs | ✅ | 31.3 s | ondemand · 600–1400 MHz (peak 2000) |
    | network-iperf | ✅ | 36.5 s | enx001e0636e380 ↑923/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 142.6 s | stable |
    | reboot | ✅ | 59.5 s | power-cycle · up 33 s |
    | store-versions | ✅ | 6.6 s | 26.11.0-trunk.6 · 6.6.141-current-odroidxu4 |

??? failure "Orange Pi 3 01 — fail"

    `orangepi3` · **inplace** · image `26.8.0-trunk.314` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 335.6 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ❌ | 215.4 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Orange Pi 5 01 — pass"

    `orangepi5` · **inplace** · image `26.8.0-trunk.314` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 194.4 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 31.2 s | warm · up 16 s |
    | hw-performance | ✅ | 17.9 s | AES 1257 · mem 7700 · disk W 55 / R 63 MB/s · 49 °C · 1800 MHz |
    | dvfs | ✅ | 15.4 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 35.0 s | end0 ↑941/↓942 (1GE) Mbps |
    | restore-stable | ✅ | 75.0 s | stable |
    | reboot | ✅ | 31.4 s | warm · up 16 s |
    | store-versions | ✅ | 4.2 s | 26.11.0-trunk.6 · 6.18.43-current-rockchip64 |

??? success "Orange Pi 5 Plus 01 — pass"

    `orangepi5-plus` · **inplace** · image `26.11.0-trunk.5` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 159.7 s | nightly · 26.11.0-trunk.5 → 26.11.0-trunk.6 |
    | reboot | ✅ | 57.8 s | power-cycle · up 27 s |
    | hw-performance | ✅ | 19.0 s | AES 1256 · mem 10000 · disk W 50 / R 56 MB/s · 53.6 °C · 1800 MHz |
    | dvfs | ✅ | 45.0 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 78.6 s | enP3p49s0 ↑2353/↓2243 (2.5GE) · enP4p65s0 ↑940/↓941 (1GE) · wlxe0e1a9380c53 ↑189/↓142 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 76.4 s | stable |
    | reboot | ✅ | 54.0 s | power-cycle · up 21 s |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.6 · 6.18.43-current-rockchip64 |

    **Power** — idle 1.90 W · avg 7.13 W · peak 17.00 W · 399 samples

??? failure "Orange Pi One+ 01 — fail"

    `orangepioneplus` · **inplace** · image `26.8.0-trunk.314` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 61.2 s | — |
    | reboot | ❌ | 230.6 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Orange Pi PC + 01 — fail"

    `orangepipcplus` · **inplace** · image `26.08.0-trunk` · 1 ✅ · 4 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 13.3 s | — |
    | reboot | ❌ | 203.7 s | warm |
    | hw-performance | ✅ | 98.0 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 9.1 s | — |
    | network-iperf | ⏭️ | 34.0 s | no iperf3 on board |
    | restore-stable | ❌ | 30.3 s | stable |
    | reboot | ❌ | 202.9 s | warm |
    | store-versions | ❌ | 16.4 s | — |

??? failure "Orange Pi PC2 01 — fail"

    `orangepipc2` · **inplace** · image `26.8.0-trunk.314` · 4 ✅ · 3 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 603.3 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 59.9 s | power-cycle · up 31 s |
    | hw-performance | ✅ | 38.0 s | AES 611 · mem 3400 · disk W 9 / R 23 MB/s · 74 °C · 1368 MHz |
    | dvfs | ✅ | 24.1 s | ondemand · 480–1368 MHz (peak 1368) |
    | network-iperf | ❌ | 84.8 s | end0 ↑0/↓0 (1GE) Mbps |
    | restore-stable | ❌ | 252.0 s | stable |
    | reboot | ❌ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Orange Pi Prime 01 — pass"

    `orangepiprime` · **inplace** · image `26.08.0-trunk` · 3 ✅ · 0 ❌ · 5 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 47.1 s | AES 379 · mem 2100 · disk W 21 / R 22 MB/s · 43.8 °C · None MHz |
    | dvfs | ➖ | 3.3 s | — |
    | network-iperf | ✅ | 116.7 s | end0 ↑881/↓941 (1GE) · wlan0 ↑31/↓30 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 6.9 s | 26.08.0-trunk · 6.18.38-current-sunxi64 |

??? failure "Orange Pi R1 01 — fail"

    `orangepi-r1` · **inplace** · image `26.8.0-trunk.170` · 6 ✅ · 2 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 490.6 s | nightly · 26.8.0-trunk.170 → 26.11.0-trunk.6 |
    | reboot | ✅ | 52.7 s | warm · up 33 s |
    | hw-performance | ✅ | 39.8 s | AES 25 · mem 1400 · disk W 21 / R 23 MB/s · 67.3 °C · 1296 MHz |
    | dvfs | ✅ | 37.7 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ❌ | 412.3 s | enxc0742bfffce9 ↑93/↓94 (10/100ME) · wlan0 ↑18/↓0 (Wi-Fi 4) · wlan1 ↑16/↓3 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 335.2 s | stable |
    | reboot | ✅ | 125.5 s | warm · up 97 s |
    | store-versions | ❌ | 18.3 s | — |

??? failure "Orange Pi Win 01 — fail"

    `orangepiwin` · **inplace** · image `26.8.0-trunk.314` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 506.3 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ❌ | 213.3 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Orange Pi Zero 02 — fail"

    `orangepizero` · **inplace** · image `26.8.0-trunk.314` · 5 ✅ · 1 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 572.8 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 51.2 s | warm · up 32 s |
    | hw-performance | ✅ | 261.2 s | AES 25 · mem 1400 · disk W None / R None MB/s · 64.8 °C · 1296 MHz |
    | dvfs | ➖ | 13.2 s | — |
    | network-iperf | ⏭️ | 137.1 s | no iperf3 on board |
    | restore-stable | ❌ | 126.0 s | stable |
    | reboot | ✅ | 148.2 s | warm · up 78 s |
    | store-versions | ✅ | 17.6 s | 26.11.0-trunk.6 · 6.18.44-current-sunxi |

??? failure "Orange Pi Zero Plus 01 — fail"

    `orangepizeroplus` · **inplace** · image `26.08.0-trunk` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 562.1 s | nightly · 26.08.0-trunk → 26.11.0-trunk.6 |
    | reboot | ❌ | 200.7 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Orange Pi Zero2 01 — fail"

    `orangepizero2` · **inplace** · image `26.8.0-trunk.314` · 5 ✅ · 2 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 304.1 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 47.2 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 33.4 s | AES 705 · mem 3000 · disk W 21 / R 23 MB/s · 62.3 °C · 1512 MHz |
    | dvfs | ✅ | 26.0 s | ondemand · 480–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 131.5 s | end0 ↑872/↓941 (1GE) · wlx7c023a625db1 ↑36/↓35 (Wi-Fi 5) Mbps |
    | restore-stable | ❌ | 5.4 s | stable |
    | reboot | ❌ | 499.1 s | power-cycle |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "OrangePi 3 LTS 01 — pass"

    `orangepi3-lts` · **inplace** · image `26.08.0-trunk` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 22.0 s | AES 750 · mem 4100 · disk W 54 / R 127 MB/s · 64.2 °C · 1608 MHz |
    | dvfs | ✅ | 22.6 s | ondemand · 480–1608 MHz (peak 1608) |
    | network-iperf | ✅ | 65.6 s | end0 ↑918/↓941 (1GE) · wlan0 ↑142/↓132 (Wi-Fi 5) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 5.1 s | 26.08.0-trunk · 7.0.14-edge-sunxi64 |

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

    `radxa-dragon-q6a` · **inplace** · image `26.2.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 21.9 s | — |
    | reboot | ✅ | 107.8 s | warm · up 93 s |
    | hw-performance | ✅ | 17.1 s | AES 1524 · mem 15000 · disk W 51 / R 74 MB/s · 43.6 °C · 1958 MHz |
    | dvfs | ✅ | 8.1 s | ondemand · 300–1958 MHz (peak 1958) |
    | network-iperf | ✅ | 64.5 s | enp1s0 ↑941/↓927 Mbps |
    | restore-stable | ✅ | 154.3 s | stable |
    | reboot | ✅ | 111.6 s | warm · up 97 s |
    | store-versions | ✅ | 4.0 s | 26.2.1 · 6.18.10-edge-qcs6490 |

??? success "Radxa ZERO 3 01 — pass"

    `radxa-zero3` · **inplace** · image `26.2.5` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 41.6 s | AES 719 · mem 3900 · disk W 20 / R 23 MB/s · 52.5 °C · 1416 MHz |
    | dvfs | ✅ | 27.4 s | ondemand · 408–1416 MHz (peak 1416) |
    | network-iperf | ✅ | 46.6 s | wlan0 ↑4/↓15 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 6.1 s | 26.2.5 · 6.18.24-current-rockchip64 |

??? failure "Raspberry Pi 01 — fail"

    `rpi4b` · **inplace** · image `26.8.0-trunk.314` · 0 ✅ · 2 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ❌ | 133.5 s | — |
    | reboot | ❌ | 206.3 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Raspberry Pi 02 — pass"

    `rpi4b` · **inplace** · image `26.8.0-trunk.236` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 448.8 s | nightly · 26.8.0-trunk.236 → 26.8.0-trunk.314 |
    | reboot | ✅ | 50.4 s | warm · up 34 s |
    | hw-performance | ✅ | 45.3 s | AES 19 · mem 1400 · disk W 20 / R 22 MB/s · 54.8 °C · 1200 MHz |
    | dvfs | ✅ | 26.5 s | ondemand · 600–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 86.4 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑24/↓30 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 247.3 s | stable |
    | reboot | ✅ | 51.6 s | warm · up 34 s |
    | store-versions | ✅ | 8.9 s | 26.8.0-trunk.314 · 6.18.35-current-bcm2711 |

??? failure "ROCK 2F 01 — fail"

    `rock-2f` · **inplace** · image `26.2.5` · 1 ✅ · 4 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 25.1 s | — |
    | reboot | ❌ | 201.8 s | warm |
    | hw-performance | ✅ | 61.9 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 16.4 s | — |
    | network-iperf | ⏭️ | 21.6 s | no iperf3 on board |
    | restore-stable | ❌ | 7.1 s | stable |
    | reboot | ❌ | 228.1 s | warm |
    | store-versions | ❌ | 32.6 s | — |

??? failure "Rock 5B 01 — fail"

    `rock-5b` · **inplace** · image `26.8.0-trunk.314` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 188.1 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ✅ | 44.8 s | power-cycle · up 15 s |
    | hw-performance | ✅ | 17.2 s | AES 1289 · mem 11000 · disk W 66 / R 82 MB/s · 59.2 °C · 1800 MHz |
    | dvfs | ✅ | 15.8 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 28.6 s | enP4p65s0 ↑2353/↓2314 (2.5GE) Mbps |
    | restore-stable | ✅ | 72.6 s | stable |
    | reboot | ❌ | 381.3 s | power-cycle |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Rock 5B 02 — fail"

    `rock-5b` · **inplace** · image `26.8.0-trunk.314` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 189.0 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.6 |
    | reboot | ❌ | 211.5 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Rock 5B 05 — fail"

    `rock-5b` · **inplace** · image `26.8.0-trunk.192` · 2 ✅ · 4 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 77.5 s | nightly · 26.8.0-trunk.192 → 26.8.0-trunk.192 |
    | reboot | ❌ | 213.0 s | power-cycle |
    | hw-performance | ✅ | 38.6 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 7.2 s | — |
    | network-iperf | ⏭️ | 19.8 s | no iperf3 on board |
    | restore-stable | ❌ | 7.3 s | stable |
    | reboot | ❌ | 231.4 s | power-cycle |
    | store-versions | ❌ | 13.8 s | — |

??? failure "Rock 5B 06 — fail"

    `rock-5b` · **inplace** · image `26.8.0-trunk.192` · 2 ✅ · 4 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 76.5 s | nightly · 26.8.0-trunk.192 → 26.8.0-trunk.192 |
    | reboot | ❌ | 220.1 s | power-cycle |
    | hw-performance | ✅ | 38.7 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 7.2 s | — |
    | network-iperf | ⏭️ | 19.8 s | no iperf3 on board |
    | restore-stable | ❌ | 7.4 s | stable |
    | reboot | ❌ | 231.8 s | power-cycle |
    | store-versions | ❌ | 13.4 s | — |

??? success "Rock 5B 07 — pass"

    `rock-5b` · **inplace** · image `26.8.0-trunk.192` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 13.8 s | — |
    | reboot | ✅ | 22.0 s | warm · up 8 s |
    | hw-performance | ✅ | 16.1 s | AES 1290 · mem 10600 · disk W 89 / R 214 MB/s · 57 °C · 1800 MHz |
    | dvfs | ✅ | 17.0 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 162.2 s | eth0 ↑2353/↓2283 (2.5GE) · wlx24418c14ae10 ↑652/↓858 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 60.4 s | stable |
    | reboot | ✅ | 22.1 s | warm · up 8 s |
    | store-versions | ✅ | 4.8 s | 26.8.0-trunk.192 · 6.18.35-current-rockchip64 |

??? success "Rock 5B 08 — pass"

    `rock-5b` · **inplace** · image `26.8.0-trunk.192` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 15.1 s | — |
    | reboot | ✅ | 18.4 s | warm · up 5 s |
    | hw-performance | ✅ | 16.2 s | AES 1289 · mem 10000 · disk W 81 / R 189 MB/s · 59.2 °C · 1800 MHz |
    | dvfs | ✅ | 9.0 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 309.4 s | enP4p65s0 ↑2353/↓2290 (2.5GE) · wlx7419f81555cb ↑570/↓384 (Wi-Fi 7) Mbps |
    | restore-stable | ✅ | 67.1 s | stable |
    | reboot | ✅ | 20.9 s | warm · up 7 s |
    | store-versions | ✅ | 5.0 s | 26.8.0-trunk.192 · 6.18.35-current-rockchip64 |

??? failure "Rock 5B Plus 01 — fail"

    `rock-5b-plus` · **inplace** · image `26.8.0-trunk.236` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 11.7 s | — |
    | reboot | ❌ | 204.9 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Rock 5T 01 — fail"

    `rock-5t` · **inplace** · image `26.8.0-trunk.236` · 5 ✅ · 2 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 220.8 s | nightly · 26.8.0-trunk.236 → 26.11.0-trunk.6 |
    | reboot | ✅ | 48.4 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 21.5 s | AES 1248 · mem 11000 · disk W 21 / R 86 MB/s · 64.7 °C · 1800 MHz |
    | dvfs | ✅ | 45.6 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ❌ | 238.0 s | enP3p49s0 ↑2313/↓1133 (2.5GE) · enP4p65s0 ↑2353/↓1762 (2.5GE) · wlP2p33s0 ↑22/↓26 (Wi-Fi 6) · wlx7cdd90ebf00a ↑24/↓0 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 151.2 s | stable |
    | reboot | ❌ | 400.9 s | power-cycle |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Rock 5T 02 — pass"

    `rock-5t` · **inplace** · image `26.8.0-trunk.192` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 101.6 s | nightly · 26.8.0-trunk.192 → 26.8.0-trunk.192 |
    | reboot | ✅ | 37.3 s | warm · up 23 s |
    | hw-performance | ✅ | 19.8 s | AES 1258 · mem 8000 · disk W 21 / R 82 MB/s · 56.4 °C · 1800 MHz |
    | dvfs | ✅ | 17.0 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 527.1 s | enP3p49s0 ↑2353/↓2354 · enP4p65s0 ↑2353/↓2353 · wlP2p33s0 ↑320/↓468 Mbps |
    | restore-stable | ✅ | 98.7 s | stable |
    | reboot | ✅ | 30.9 s | warm · up 17 s |
    | store-versions | ✅ | 4.5 s | 26.8.0-trunk.192 · 6.18.35-current-rockchip64 |

??? failure "Rockpi 4B+ 01 — fail"

    `rockpi-4b` · **inplace** · image `26.11.0-trunk.1` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 87.3 s | nightly · 26.11.0-trunk.1 → 26.11.0-trunk.1 |
    | reboot | ❌ | 195.7 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Rockpi E 01 — pass"

    `rockpi-e` · **inplace** · image `26.5.1` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 430.0 s | nightly · 26.5.1 → 26.8.0-trunk.314 |
    | reboot | ⏭️ | 3.9 s | power-cycle |
    | hw-performance | ✅ | 33.3 s | AES 603 · mem 3300 · disk W 20 / R 23 MB/s · 64.6 °C · 1296 MHz |
    | dvfs | ✅ | 19.6 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 63.5 s | end0 ↑941/↓939 (1GE) · wlx7ca7b020e87c ↑177/↓204 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 170.8 s | stable |
    | reboot | ⏭️ | 3.9 s | power-cycle |
    | store-versions | ✅ | 5.5 s | 26.8.0-trunk.314 · 6.18.33-current-rockchip64 |

??? success "SpacemiT K3 Pico-ITX 01 — pass"

    `k3picoitx` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 22.9 s | AES 796 · mem 12000 · disk W 23 / R 40 MB/s · 61 °C · 2200 MHz |
    | dvfs | ✅ | 15.6 s | performance · 614–2200 MHz (peak 2200) |
    | network-iperf | ✅ | 53.2 s | eth0 ↑941/↓942 (1GE) · wlan0 ↑111/↓190 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 3.6 s | 26.8.3 · 6.18.3-legacy-spacemit-k3 |

    **Power** — idle 13.60 W · avg 15.10 W · peak 22.70 W · 81 samples

??? failure "Tanix TX6 01 — fail"

    `tanix-tx6` · **inplace** · image `26.8.0-trunk.170` · 3 ✅ · 4 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ❌ | 353.2 s | nightly · 26.8.0-trunk.170 → ? |
    | reboot | ✅ | 80.1 s | warm · up 34 s |
    | hw-perf | ❌ | 0.0 s | — |
    | dvfs | ❌ | 56.9 s | ondemand · 480–1704 MHz (peak 1608) |
    | network-iperf | ⏭️ | 32.1 s | no interfaces with an IP |
    | restore-stable | ❌ | 7.7 s | stable |
    | reboot | ✅ | 46.6 s | warm · up 26 s |
    | store-versions | ✅ | 29.2 s | 26.11.0-trunk.6 · 6.18.44-current-sunxi64 |

??? failure "Tinker Board 01 — fail"

    `tinkerboard` · **inplace** · image `26.11.0-trunk.5` · 0 ✅ · 2 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ❌ | 182.7 s | — |
    | reboot | ❌ | 237.4 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

    **Power** — idle 2.50 W · avg 4.17 W · peak 5.60 W · 96 samples

??? failure "Tinker Board 2 01 — fail"

    `tinkerboard-2` · **inplace** · image `26.8.0-trunk.236` · 1 ✅ · 2 ❌ · 5 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 55.0 s | — |
    | reboot | ⏭️ | 3.3 s | power-cycle |
    | hw-performance | ✅ | 99.9 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 7.1 s | — |
    | network-iperf | ⏭️ | 37.7 s | no iperf3 on board |
    | restore-stable | ❌ | 19.0 s | stable |
    | reboot | ⏭️ | 3.3 s | power-cycle |
    | store-versions | ❌ | 37.2 s | — |

??? failure "Udoo 01 — fail"

    `udoo` · **inplace** · image `26.8.0-trunk.314` · 2 ✅ · 4 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 1338.3 s | nightly · 26.8.0-trunk.314 → 26.11.0-trunk.3 |
    | reboot | ❌ | 215.8 s | power-cycle |
    | hw-performance | ✅ | 138.1 s | AES None · mem None · disk W None / R None MB/s · None °C · None MHz |
    | dvfs | ➖ | 7.2 s | — |
    | network-iperf | ⏭️ | 20.3 s | no iperf3 on board |
    | restore-stable | ❌ | 294.3 s | stable |
    | reboot | ❌ | 222.1 s | power-cycle |
    | store-versions | ❌ | 12.3 s | — |

??? success "UEFI arm64 01 — pass"

    `uefi-arm64` · **inplace** · image `26.8.0-trunk.314` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 16.5 s | AES 1458 · mem 14000 · disk W 1554 / R 2197 MB/s · 46 °C · 2600 MHz |
    | dvfs | ✅ | 18.6 s | ondemand · 800–2600 MHz (peak 2600) |
    | network-iperf | ✅ | 82.0 s | enp1s0 ↑4527/↓2468 (10GE) · enp49s0 ↑8726/↓9301 (10GE) · wlp97s0 ↑100/↓97 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.5 s | 26.8.0-trunk.314 · 7.1.2-edge-arm64 |

??? success "UEFI x86 01 — pass"

    `uefi-x86` · **inplace** · image `26.8.0-trunk.236` · 7 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 478.4 s | nightly · 26.8.0-trunk.236 → 26.8.0-trunk.314 |
    | reboot | ✅ | 47.7 s | warm · up 33 s |
    | hw-performance | ✅ | 24.9 s | AES 237 · mem 4800 · disk W 21 / R 106 MB/s · 57 °C · 1920 MHz |
    | dvfs | ❌ | 10.9 s | schedutil · 480–1920 MHz (peak 1565) |
    | network-iperf | ✅ | 61.1 s | enp1s0 ↑920/↓941 (1GE) · wlan0 ↑25/↓23 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 141.9 s | stable |
    | reboot | ✅ | 45.6 s | warm · up 30 s |
    | store-versions | ✅ | 4.8 s | 26.8.0-trunk.314 · 6.18.32-current-x86 |

??? success "Z28 PRO 01 — pass"

    `z28pro` · **inplace** · image `26.8.0-trunk.15` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 378.4 s | nightly · 26.8.0-trunk.15 → 26.11.0-trunk.3 |
    | reboot | ✅ | 65.0 s | power-cycle · up 25 s |
    | hw-performance | ✅ | 51.4 s | AES 603 · mem 2400 · disk W 51 / R 110 MB/s · 60 °C · 1296 MHz |
    | dvfs | ➖ | 5.2 s | ondemand · 408–1296 MHz |
    | network-iperf | ✅ | 71.2 s | end0 ↑927/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 183.8 s | stable |
    | reboot | ✅ | 65.0 s | power-cycle · up 24 s |
    | store-versions | ✅ | 6.7 s | 26.11.0-trunk.3 · 6.18.43-current-rockchip64 |

    **Power** — idle 1.20 W · avg 4.28 W · peak 6.20 W · 684 samples


<!-- FLEET-STOP -->
