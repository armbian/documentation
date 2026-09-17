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

**63** boards — **52** passed, **11** failed. Each card is the board's most recent test.

??? success "Arduino UNO Q 01 — pass"

    `arduino-uno-q` · **inplace** · image `26.11.0-trunk.27` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 22.6 s | — |
    | reboot | ✅ | 49.2 s | warm · up 32 s |
    | hw-performance | ✅ | 24.7 s | AES 940 · mem 5100 · disk W 168 / R 223 MB/s · 40.6 °C · 2016 MHz |
    | dvfs | ✅ | 32.5 s | schedutil · 300–2016 MHz (peak 2016) |
    | network-iperf | ❌ | 229.8 s | usb0 ↑0/↓0 (1GE) · wlan0 ↑24/↓5 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 31.4 s | stable |
    | reboot | ✅ | 51.3 s | warm · up 34 s |
    | store-versions | ✅ | 6.8 s | 26.11.0-trunk.27 · 7.1.8-edge-qrb2210 |

??? success "Banana Pi CM4IO 01 — pass"

    `bananapicm4io` · **inplace** · image `26.8.3` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 25.1 s | — |
    | reboot | ✅ | 44.3 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 18.0 s | AES 853 · mem 3900 · disk W 42 / R 152 MB/s · 51.2 °C · 2016 MHz |
    | dvfs | ✅ | 17.6 s | ondemand · 1000–1512 MHz (peak 1512) |
    | network-iperf | ❌ | 551.0 s | eth0 ↑0/↓0 (1GE) · wlan0 ↑0/↓0 (Wi-Fi 5) · wlx00e032c00694 ↑0/↓0 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 33.4 s | stable |
    | reboot | ✅ | 43.9 s | power-cycle · up 19 s |
    | store-versions | ✅ | 4.3 s | 26.8.3 · 6.18.44-current-meson64 |

??? failure "Banana Pi M2 Ultra 01 — fail"

    `bananapim2ultra` · **inplace** · image `26.11.0-trunk.49` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 25.0 s | — |
    | reboot | ❌ | 201.5 s | warm |
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

    `bananapim5` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 22.4 s | — |
    | reboot | ✅ | 170.1 s | warm · up 155 s |
    | hw-performance | ✅ | 37.9 s | AES 977 · mem 5200 · disk W 10 / R 16 MB/s · 52.9 °C · 2100 MHz |
    | dvfs | ✅ | 20.2 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 76.1 s | end0 ↑940/↓941 (1GE) · wlx000f13960190 ↑1/↓11 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 31.0 s | stable |
    | reboot | ✅ | 163.1 s | warm · up 148 s |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? success "Banana Pi M7 01 — pass"

    `bananapim7` · **inplace** · image `26.11.0-trunk.35` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 10.6 s | — |
    | reboot | ✅ | 41.6 s | power-cycle · up 15 s |
    | hw-performance | ✅ | 13.6 s | AES 1265 · mem 13600 · disk W 1067 / R 1378 MB/s · 51.8 °C · 1800 MHz |
    | dvfs | ✅ | 17.2 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 29.5 s | enP2p33s0 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 15.6 s | stable |
    | reboot | ✅ | 40.6 s | power-cycle · up 16 s |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.35 · 6.1.115-vendor-rk35xx |

    **Power** — idle 4.00 W · avg 5.84 W · peak 14.70 W · 134 samples

??? success "Banana Pi R3 Mini 01 — pass"

    `bananapir3mini` · **inplace** · image `26.11.0-trunk` · 5 ✅ · 0 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 18.6 s | — |
    | reboot | ✅ | 64.9 s | power-cycle · up 34 s |
    | hw-performance | ✅ | 26.2 s | AES 929 · mem 3200 · disk W 74 / R 91 MB/s · 60.7 °C · None MHz |
    | dvfs | ➖ | 2.0 s | — |
    | network-iperf | ✅ | 246.9 s | eth0 ↑889/↓580 (1GE) · eth1 ↑920/↓925 (1GE) · wlan0 ↑6/↓49 (Wi-Fi 6) · wlan1 ↑346/↓388 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 10.6 s | — |
    | reboot | ✅ | 72.5 s | power-cycle · up 42 s |
    | store-versions | ✅ | 4.5 s | 26.11.0-trunk · 6.18.52-current-filogic-mt7986 |

    **Power** — idle 3.20 W · avg 7.77 W · peak 13.10 W · 363 samples

??? success "BananaPi BPI-F3 01 — pass"

    `bananapif3` · **inplace** · image `26.11.0-trunk.35` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 24.4 s | — |
    | reboot | ✅ | 46.8 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 22.2 s | AES 30 · mem 3600 · disk W 58 / R 83 MB/s · 62 °C · 1800 MHz |
    | dvfs | ✅ | 23.2 s | performance · 614–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 270.1 s | eth0 ↑933/↓830 (1GE) · wlan0 ↑318/↓294 (Wi-Fi 6) · wlan1 ↑197/↓218 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 36.0 s | stable |
    | reboot | ✅ | 47.4 s | power-cycle · up 17 s |
    | store-versions | ✅ | 5.2 s | 26.11.0-trunk.35 · 6.18.44-current-spacemit |

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

    `clearfogpro` · **inplace** · image `26.8.3` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 27.4 s | — |
    | reboot | ✅ | 36.8 s | warm · up 19 s |
    | hw-performance | ✅ | 42.1 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 64.6 °C · None MHz |
    | dvfs | ➖ | 2.9 s | — |
    | network-iperf | ✅ | 70.4 s | lan2 ↑936/↓936 Mbps |
    | restore-stable | ✅ | 31.7 s | stable |
    | reboot | ✅ | 36.0 s | warm · up 19 s |
    | store-versions | ✅ | 6.1 s | 26.8.3 · 6.6.151-current-mvebu |

??? failure "Cubie A5E 01 — fail"

    `radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.49` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.24 · reachable=False · port=22 |

    **Power** — idle 2.00 W · avg 2.00 W · peak 2.00 W · 47 samples

??? success "Cubietruck 01 — pass"

    `cubietruck` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 51.5 s | — |
    | reboot | ✅ | 61.8 s | warm · up 43 s |
    | hw-performance | ✅ | 59.6 s | AES 19 · mem 1700 · disk W 14 / R 22 MB/s · 48.6 °C · 960 MHz |
    | dvfs | ✅ | 56.5 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 224.5 s | end0 ↑721/↓848 (1GE) · wlan0 ↑11/↓25 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 67.9 s | stable |
    | reboot | ✅ | 60.1 s | warm · up 42 s |
    | store-versions | ✅ | 12.5 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi |

??? success "Cubox i2eX/i4 01 — pass"

    `radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 46.0 s | — |
    | reboot | ✅ | 57.4 s | power-cycle · up 31 s |
    | hw-performance | ✅ | 46.7 s | AES 26 · mem 743 · disk W 19 / R 20 MB/s · 50.9 °C · 996 MHz |
    | dvfs | ✅ | 40.2 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 206.3 s | end0 ↑394/↓215 (1GE) · wlan0 ↑6/↓9 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 57.4 s | stable |
    | reboot | ✅ | 56.4 s | power-cycle · up 29 s |
    | store-versions | ✅ | 8.9 s | 26.11.0-trunk.27 · 6.18.44-current-imx6 |

??? success "Espressobin 01 — pass"

    `espressobin` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 35.7 s | AES 371 · mem 2000 · disk W 64 / R 131 MB/s · None °C · 800 MHz |
    | dvfs | ✅ | 33.5 s | ondemand · 200–800 MHz (peak 800) |
    | network-iperf | ✅ | 48.5 s | lan0 ↑936/↓756 (1GE) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.3 s | 26.8.3 · 6.18.44-current-mvebu64 |

??? success "Helios4 01 — pass"

    `helios4` · **inplace** · image `26.8.3` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 22.2 s | — |
    | reboot | ✅ | 33.7 s | warm · up 19 s |
    | hw-performance | ✅ | 36.8 s | AES 43 · mem 3800 · disk W 21 / R 23 MB/s · 57.5 °C · None MHz |
    | dvfs | ➖ | 2.3 s | — |
    | network-iperf | ✅ | 92.8 s | end1 ↑680/↓794 (1GE) · wlx1cbfce1f85a5 ↑213/↓132 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 28.1 s | stable |
    | reboot | ✅ | 33.8 s | warm · up 18 s |
    | store-versions | ✅ | 5.2 s | 26.8.3 · 6.6.151-current-mvebu |

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

    `mekotronics-r58hd` · **inplace** · image `26.11.0-trunk.35` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 11.3 s | — |
    | reboot | ✅ | 45.5 s | power-cycle · up 15 s |
    | hw-performance | ✅ | 13.8 s | AES 1302 · mem 14000 · disk W 241 / R 280 MB/s · 49 °C · 1800 MHz |
    | dvfs | ✅ | 16.7 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ❌ | 851.7 s | end0 ↑791/↓223 (1GE) · enP3p49s0 ↑0/↓939 (1GE) Mbps |
    | restore-stable | ✅ | 97.3 s | stable |
    | reboot | ✅ | 42.1 s | power-cycle · up 16 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.35 · 6.1.115-vendor-rk35xx |

    **Power** — idle 3.40 W · avg 5.25 W · peak 12.00 W · 885 samples

??? success "Mekotronics R58S2 01 — pass"

    `mekotronics-r58s2` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 13.2 s | — |
    | reboot | ✅ | 45.0 s | power-cycle · up 15 s |
    | hw-performance | ✅ | 14.4 s | AES 1282 · mem 14000 · disk W 224 / R 273 MB/s · 42.5 °C · 1800 MHz |
    | dvfs | ✅ | 18.1 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 66.1 s | end1 ↑619/↓870 (1GE) · wlan0 ↑59/↓156 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 14.5 s | stable |
    | reboot | ✅ | 44.2 s | power-cycle · up 15 s |
    | store-versions | ✅ | 3.9 s | 26.8.3 · 6.1.115-vendor-rk35xx |

??? success "NanoPi Fire3 01 — pass"

    `nanopifire3` · **inplace** · image `26.8.6` · 5 ✅ · 0 ❌ · 3 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 37.5 s | — |
    | reboot | ✅ | 51.0 s | power-cycle · up 17 s |
    | hw-performance | ✅ | 43.6 s | AES 374 · mem 2000 · disk W 20 / R 22 MB/s · 65 °C · None MHz |
    | dvfs | ➖ | 3.1 s | — |
    | network-iperf | ✅ | 35.6 s | eth0 ↑890/↓939 (1GE) Mbps |
    | restore-stable | ⏭️ | 22.3 s | — |
    | reboot | ✅ | 49.9 s | power-cycle · up 14 s |
    | store-versions | ✅ | 6.7 s | 26.8.6 · 7.2.5-edge-s5p6818 |

??? success "NanoPi K2 01 — pass"

    `nanopik2-s905` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 22.7 s | — |
    | reboot | ✅ | 40.4 s | warm · up 25 s |
    | hw-performance | ✅ | 31.9 s | AES 51 · mem 3700 · disk W 10 / R 41 MB/s · 56 °C · 2016 MHz |
    | dvfs | ✅ | 20.7 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 127.1 s | end0 ↑934/↓941 (1GE) · wlan0 ↑15/↓28 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 29.2 s | stable |
    | reboot | ✅ | 35.9 s | warm · up 21 s |
    | store-versions | ✅ | 4.7 s | 26.8.3 · 6.18.44-current-meson64 |

??? success "NanoPi M4V2 01 — pass"

    `nanopim4v2` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 16.5 s | — |
    | reboot | ✅ | 61.9 s | power-cycle · up 31 s |
    | hw-performance | ✅ | 21.5 s | AES 1021 · mem 6600 · disk W 54 / R 62 MB/s · 46.9 °C · 1416 MHz |
    | dvfs | ✅ | 20.9 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 166.0 s | end0 ↑656/↓845 (1GE) · wlan0 ↑146/↓184 (Wi-Fi 5) · wlx803f5d16af63 ↑62/↓137 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 20.9 s | stable |
    | reboot | ✅ | 57.8 s | power-cycle · up 29 s |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

    **Power** — idle 2.20 W · avg 7.06 W · peak 12.00 W · 295 samples

??? success "NanoPi M5 01 — pass"

    `nanopi-m5` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 16.7 s | — |
    | reboot | ✅ | 50.5 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 20.6 s | AES 1273 · mem 7800 · disk W 62 / R 67 MB/s · 42.5 °C · 2016 MHz |
    | dvfs | ✅ | 21.7 s | ondemand · 2016–2016 MHz (peak 2208) |
    | network-iperf | ✅ | 239.2 s | end0 ↑631/↓859 (1GE) · end1 ↑690/↓656 (1GE) · wlan0 ↑38/↓48 (Wi-Fi 5) · wlx44334c47dec3 ↑17/↓32 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 21.2 s | stable |
    | reboot | ✅ | 54.5 s | power-cycle · up 24 s |
    | store-versions | ✅ | 4.4 s | 26.8.3 · 6.1.115-vendor-rk35xx |

    **Power** — idle 0.60 W · avg 4.65 W · peak 7.80 W · 348 samples

??? success "NanoPi M6 01 — pass"

    `nanopi-m6` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 18.5 s | — |
    | reboot | ✅ | 51.4 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 27.2 s | AES 1212 · mem 10200 · disk W 15 / R 30 MB/s · 49.9 °C · 1800 MHz |
    | dvfs | ✅ | 16.9 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 153.1 s | lan ↑936/↓573 (1GE) · wlP3p49s0 ↑74/↓163 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 21.7 s | stable |
    | reboot | ✅ | 50.6 s | power-cycle · up 19 s |
    | store-versions | ✅ | 3.7 s | 26.8.3 · 6.18.44-current-rockchip64 |

    **Power** — idle 1.20 W · avg 4.28 W · peak 11.30 W · 276 samples

??? failure "NanoPi Neo 2 Black 01 — fail"

    `nanopineo2black` · **inplace** · image `26.11.0-trunk.27` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 25.2 s | — |
    | reboot | ❌ | 217.6 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "NanoPi Neo 3 01 — pass"

    `nanopineo3` · **inplace** · image `26.11.0-trunk.44` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 27.9 s | — |
    | reboot | ✅ | 50.6 s | power-cycle · up 25 s |
    | hw-performance | ✅ | 28.1 s | AES 596 · mem 2300 · disk W 51 / R 63 MB/s · 76.5 °C · 1296 MHz |
    | dvfs | ✅ | 29.4 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 160.9 s | end0 ↑920/↓941 (1GE) · wlx7cdd905518f9 ↑32/↓4 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 44.5 s | stable |
    | reboot | ✅ | 50.9 s | power-cycle · up 25 s |
    | store-versions | ✅ | 7.6 s | 26.11.0-trunk.44 · 6.18.44-current-rockchip64 |

??? success "NanoPi R6S 01 — pass"

    `nanopi-r6s` · **inplace** · image `26.11.0-trunk.35` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 11.0 s | — |
    | reboot | ✅ | 34.9 s | power-cycle · up 12 s |
    | hw-performance | ✅ | 14.5 s | AES 1280 · mem 13600 · disk W 209 / R 263 MB/s · 36.1 °C · 1800 MHz |
    | dvfs | ✅ | 18.6 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 29.5 s | lan2 ↑863/↓863 (1GE) Mbps |
    | restore-stable | ✅ | 14.5 s | stable |
    | reboot | ✅ | 37.1 s | power-cycle · up 14 s |
    | store-versions | ✅ | 4.5 s | 26.11.0-trunk.35 · 6.1.115-vendor-rk35xx |

    **Power** — idle 1.30 W · avg 3.75 W · peak 9.30 W · 126 samples

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

    `odroidc2` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 18.7 s | — |
    | reboot | ✅ | 31.8 s | warm · up 17 s |
    | hw-performance | ✅ | 22.1 s | AES 51 · mem 3500 · disk W 34 / R 152 MB/s · 42 °C · 1536 MHz |
    | dvfs | ✅ | 21.6 s | ondemand · 500–1536 MHz (peak 1536) |
    | network-iperf | ✅ | 62.2 s | end0 ↑940/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 28.9 s | stable |
    | reboot | ✅ | 32.3 s | warm · up 17 s |
    | store-versions | ✅ | 4.9 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? success "Odroid C4 01 — pass"

    `odroidc4` · **inplace** · image `26.11.0-trunk.49` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 17.5 s | — |
    | reboot | ✅ | 45.8 s | power-cycle · up 17 s |
    | hw-performance | ✅ | 24.7 s | AES 980 · mem 5300 · disk W 30 / R 74 MB/s · 41.4 °C · 2100 MHz |
    | dvfs | ✅ | 18.6 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 74.9 s | end0 ↑937/↓939 (1GE) · wlx24050fdd332b ↑112/↓60 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 22.8 s | stable |
    | reboot | ✅ | 45.4 s | power-cycle · up 16 s |
    | store-versions | ✅ | 5.4 s | 26.11.0-trunk.49 · 6.18.44-current-meson64 |

    **Power** — idle 1.20 W · avg 3.31 W · peak 5.00 W · 202 samples

??? success "Odroid M1 01 — pass"

    `odroidm1` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 18.5 s | — |
    | reboot | ✅ | 56.2 s | power-cycle · up 21 s |
    | hw-performance | ✅ | 16.8 s | AES 917 · mem 5100 · disk W 1037 / R 1028 MB/s · 34.4 °C · 1992 MHz |
    | dvfs | ✅ | 21.3 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 63.0 s | eth0 ↑576/↓941 (1GE) · wlx40a5eff39254 ↑130/↓177 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 25.1 s | stable |
    | reboot | ✅ | 55.7 s | power-cycle · up 21 s |
    | store-versions | ✅ | 4.5 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

    **Power** — idle 1.90 W · avg 6.35 W · peak 10.70 W · 190 samples

??? success "Odroid N2 01 — pass"

    `odroidn2` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 12.9 s | — |
    | reboot | ✅ | 60.6 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 19.1 s | AES 1085 · mem 4900 · disk W 28 / R 135 MB/s · 37.2 °C · 1992 MHz |
    | dvfs | ✅ | 17.7 s | performance · 1000–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 27.7 s | end0 ↑940/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 19.8 s | stable |
    | reboot | ✅ | 63.9 s | power-cycle · up 27 s |
    | store-versions | ✅ | 3.8 s | 26.8.3 · 6.18.44-current-meson64 |

    **Power** — idle 1.00 W · avg 3.59 W · peak 9.70 W · 177 samples

??? success "Odroid XU4 01 — pass"

    `odroidxu4` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 22.9 s | — |
    | reboot | ✅ | 62.1 s | power-cycle · up 36 s |
    | hw-performance | ✅ | 37.8 s | AES 71 · mem 4400 · disk W 1 / R 54 MB/s · 58 °C · 1400 MHz |
    | dvfs | ✅ | 32.1 s | ondemand · 600–1400 MHz (peak 2000) |
    | network-iperf | ✅ | 42.5 s | enx001e0636e380 ↑923/↓940 (1GE) Mbps |
    | restore-stable | ✅ | 29.6 s | stable |
    | reboot | ✅ | 59.1 s | power-cycle · up 32 s |
    | store-versions | ✅ | 6.5 s | 26.11.0-trunk.27 · 6.6.151-current-odroidxu4 |

??? failure "Orange Pi 3 01 — fail"

    `orangepi3` · **inplace** · image `26.11.0-trunk.49` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 15.8 s | — |
    | reboot | ❌ | 196.5 s | warm |
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

    `orangepi5-plus` · **inplace** · image `26.11.0-trunk.35` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 12.5 s | — |
    | reboot | ✅ | 52.9 s | power-cycle · up 28 s |
    | hw-performance | ✅ | 17.4 s | AES 1255 · mem 15300 · disk W 53 / R 62 MB/s · 55.5 °C · 1800 MHz |
    | dvfs | ✅ | 16.3 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 56.0 s | enP3p49s0 ↑941/↓940 (1GE) · wlxe0e1a9380c53 ↑553/↓358 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 14.0 s | stable |
    | reboot | ✅ | 53.0 s | power-cycle · up 28 s |
    | store-versions | ✅ | 3.5 s | 26.11.0-trunk.35 · 6.1.115-vendor-rk35xx |

    **Power** — idle 2.50 W · avg 5.95 W · peak 11.20 W · 176 samples

??? success "Orange Pi One+ 01 — pass"

    `orangepioneplus` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 26.9 s | — |
    | reboot | ✅ | 35.5 s | warm · up 17 s |
    | hw-performance | ✅ | 30.3 s | AES 833 · mem 4500 · disk W 21 / R 23 MB/s · 57.5 °C · 1800 MHz |
    | dvfs | ✅ | 23.6 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 67.8 s | end0 ↑918/↓941 (1GE) · wlx00e04c881724 ↑27/↓27 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 34.7 s | stable |
    | reboot | ✅ | 35.6 s | warm · up 18 s |
    | store-versions | ✅ | 6.2 s | 26.11.0-trunk.27 · 7.1.8-edge-sunxi64 |

??? failure "Orange Pi PC2 01 — fail"

    `orangepipc2` · **inplace** · image `26.11.0-trunk.27` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 29.7 s | — |
    | reboot | ❌ | 213.7 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Orange Pi Prime 01 — pass"

    `orangepiprime` · **inplace** · image `26.11.0-trunk.49` · 3 ✅ · 0 ❌ · 5 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 45.7 s | AES 380 · mem 2100 · disk W 21 / R 23 MB/s · 40.9 °C · None MHz |
    | dvfs | ➖ | 2.9 s | — |
    | network-iperf | ✅ | 65.8 s | end0 ↑875/↓934 (1GE) · wlan0 ↑27/↓37 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 6.5 s | 26.11.0-trunk.49 · 6.18.51-current-sunxi64 |

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
    | hw-performance | ✅ | 20.9 s | AES 750 · mem 4100 · disk W 54 / R 127 MB/s · 63.7 °C · 1608 MHz |
    | dvfs | ✅ | 21.7 s | ondemand · 480–1608 MHz (peak 1608) |
    | network-iperf | ✅ | 62.0 s | end0 ↑918/↓940 (1GE) · wlan0 ↑33/↓20 (Wi-Fi 5) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.8 s | 26.8.3 · 7.1.8-edge-sunxi64 |

    **Power** — idle 2.50 W · avg 3.37 W · peak 4.80 W · 92 samples

??? success "Radxa Dragon Q6A 01 — pass"

    `radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 10.5 s | — |
    | reboot | ✅ | 138.1 s | power-cycle · up 106 s |
    | hw-performance | ✅ | 13.0 s | AES 1513 · mem 15400 · disk W 247 / R 1183 MB/s · 45.3 °C · 1958 MHz |
    | dvfs | ✅ | 13.4 s | ondemand · 300–1958 MHz (peak 2707) |
    | network-iperf | ✅ | 27.5 s | enp1s0 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 13.6 s | stable |
    | reboot | ✅ | 138.5 s | power-cycle · up 105 s |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.27 · 6.18.2-current-qcs6490 |

    **Power** — idle 1.00 W · avg 2.21 W · peak 7.00 W · 283 samples

??? success "Radxa ZERO 3 01 — pass"

    `radxa-zero3` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 49.6 s | AES 720 · mem 4000 · disk W 21 / R 22 MB/s · 47.8 °C · 1416 MHz |
    | dvfs | ✅ | 40.3 s | ondemand · 408–1416 MHz (peak 1416) |
    | network-iperf | ✅ | 41.5 s | wlan0 ↑8/↓17 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 14.1 s | 26.5.1 · 6.18.44-current-rockchip64 |

??? success "Raspberry Pi 3B — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 42.8 s | — |
    | reboot | ✅ | 50.6 s | warm · up 35 s |
    | hw-performance | ✅ | 42.2 s | AES 20 · mem 1400 · disk W 20 / R 22 MB/s · 51.5 °C · 1200 MHz |
    | dvfs | ✅ | 38.8 s | ondemand · 600–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 146.7 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑25/↓18 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 60.5 s | stable |
    | reboot | ✅ | 46.9 s | warm · up 30 s |
    | store-versions | ✅ | 9.8 s | 26.11.0-trunk.27 · 6.18.44-current-bcm2711 |

??? success "Raspberry Pi 5B — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 7.0 s | — |
    | reboot | ✅ | 43.6 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 14.5 s | AES 1368 · mem 12100 · disk W 54 / R 84 MB/s · 64.5 °C · 2400 MHz |
    | dvfs | ✅ | 13.1 s | ondemand · 1500–2400 MHz (peak 2400) |
    | network-iperf | ✅ | 52.4 s | end0 ↑935/↓941 (1GE) · wlan0 ↑32/↓17 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 9.9 s | stable |
    | reboot | ✅ | 45.8 s | power-cycle · up 21 s |
    | store-versions | ✅ | 3.2 s | 26.11.0-trunk.27 · 6.18.44-current-bcm2711 |

    **Power** — idle 3.80 W · avg 5.97 W · peak 9.80 W · 145 samples

??? success "Raspberry Pi Zero 2W — pass"

    `rpi4b` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 36.3 s | — |
    | reboot | ✅ | 39.8 s | warm · up 22 s |
    | hw-performance | ✅ | 34.2 s | AES 33 · mem 2200 · disk W 20 / R 23 MB/s · 51.5 °C · 1000 MHz |
    | dvfs | ✅ | 27.4 s | ondemand · 600–1000 MHz (peak 1000) |
    | network-iperf | ✅ | 65.0 s | wlan0 ↑32/↓32 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 46.4 s | stable |
    | reboot | ✅ | 37.4 s | warm · up 22 s |
    | store-versions | ✅ | 6.3 s | 26.8.1 · 6.18.44-current-bcm2711 |

??? success "ROCK 2F 01 — pass"

    `rock-2f` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 31.5 s | AES 825 · mem 5900 · disk W 38 / R 65 MB/s · 46.6 °C · 2016 MHz |
    | dvfs | ✅ | 25.5 s | ondemand · 408–2016 MHz (peak 2016) |
    | network-iperf | ✅ | 46.4 s | wlan0 ↑31/↓28 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 5.5 s | 26.5.1 · 6.1.115-vendor-rk35xx |

??? success "Rock 5B 01 — pass"

    `rock-5b` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 12.4 s | — |
    | reboot | ✅ | 46.2 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 20.5 s | AES 1285 · mem 10000 · disk W 24 / R 83 MB/s · 62.8 °C · 1800 MHz |
    | dvfs | ✅ | 15.6 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 42.2 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 14.7 s | stable |
    | reboot | ✅ | 54.6 s | power-cycle · up 21 s |
    | store-versions | ✅ | 3.9 s | 26.8.3 · 6.18.44-current-rockchip64 |

    **Power** — idle 0.70 W · avg 5.73 W · peak 13.30 W · 162 samples

??? success "Rock 5B 02 — pass"

    `rock-5b` · **inplace** · image `26.11.0-trunk.31` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 12.7 s | — |
    | reboot | ✅ | 50.5 s | power-cycle · up 17 s |
    | hw-performance | ✅ | 17.4 s | AES 1286 · mem 11000 · disk W 64 / R 74 MB/s · 62.8 °C · 1800 MHz |
    | dvfs | ✅ | 15.4 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 58.2 s | enP4p65s0 ↑941/↓941 (1GE) · wlP2p33s0 ↑659/↓215 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 14.7 s | stable |
    | reboot | ✅ | 50.5 s | power-cycle · up 18 s |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.31 · 6.18.44-current-rockchip64 |

    **Power** — idle 2.60 W · avg 6.05 W · peak 13.90 W · 164 samples

??? success "Rock 5B Plus 01 — pass"

    `rock-5b-plus` · **inplace** · image `26.11.0-trunk.31` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 6.6 s | — |
    | reboot | ✅ | 51.7 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 18.1 s | AES 1287 · mem 15800 · disk W 25 / R 82 MB/s · 48.1 °C · 1800 MHz |
    | dvfs | ✅ | 15.9 s | ondemand · 1800–1800 MHz (peak 2304) |
    | network-iperf | ✅ | 29.2 s | enP4p65s0 ↑941/↓941 (1GE) Mbps |
    | restore-stable | ⏭️ | 4.2 s | — |
    | reboot | ✅ | 50.5 s | power-cycle · up 26 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.31 · 6.1.115-vendor-rk35xx |

    **Power** — idle 2.50 W · avg 3.68 W · peak 8.80 W · 136 samples

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
    | upgrade | ⏭️ | 25.8 s | — |
    | reboot | ✅ | 54.4 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 32.5 s | AES 600 · mem 3300 · disk W 21 / R 23 MB/s · 62.1 °C · 1296 MHz |
    | dvfs | ✅ | 25.9 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 118.3 s | end0 ↑941/↓941 (1GE) · end1 ↑94/↓94 (10/100ME) · wlx7ca7b020e87c ↑159/↓171 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 36.7 s | stable |
    | reboot | ✅ | 53.6 s | power-cycle · up 24 s |
    | store-versions | ✅ | 6.6 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

??? success "RockPro 64 01 — pass"

    `rockpro64` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 15.7 s | — |
    | reboot | ✅ | 65.4 s | power-cycle · up 37 s |
    | hw-performance | ✅ | 20.3 s | AES 1020 · mem 6500 · disk W 66 / R 119 MB/s · 42.8 °C · 1416 MHz |
    | dvfs | ✅ | 21.0 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 62.4 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑97/↓82 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 21.1 s | stable |
    | reboot | ✅ | 58.6 s | power-cycle · up 36 s |
    | store-versions | ✅ | 5.0 s | 26.8.1 · 6.18.44-current-rockchip64 |

??? success "SpacemiT K3 Pico-ITX 01 — pass"

    `k3picoitx` · **inplace** · image `26.11.0-trunk.49` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 52.8 s | — |
    | reboot | ✅ | 52.4 s | power-cycle · up 30 s |
    | hw-performance | ✅ | 13.0 s | AES 796 · mem 12600 · disk W 1455 / R 1516 MB/s · 59 °C · 2200 MHz |
    | dvfs | ✅ | 14.3 s | performance · 614–2200 MHz (peak 2200) |
    | network-iperf | ✅ | 57.1 s | eth0 ↑921/↓928 (1GE) · wlan0 ↑104/↓127 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 41.8 s | — |
    | reboot | ✅ | 52.5 s | power-cycle · up 30 s |
    | store-versions | ✅ | 3.6 s | 26.11.0-trunk.49 · 6.18.3-legacy-spacemit-k3 |

??? success "Tinker Board 01 — pass"

    `tinkerboard` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 23.6 s | — |
    | reboot | ✅ | 55.9 s | power-cycle · up 30 s |
    | hw-performance | ✅ | 27.4 s | AES 67 · mem 3300 · disk W 14 / R 64 MB/s · 55.9 °C · 1800 MHz |
    | dvfs | ✅ | 20.3 s | ondemand · 600–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 67.2 s | end0 ↑940/↓941 (1GE) · wlan0 ↑6/↓12 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 21.4 s | stable |
    | reboot | ✅ | 61.6 s | power-cycle · up 28 s |
    | store-versions | ✅ | 5.3 s | 26.8.1 · 6.18.44-current-rockchip |

    **Power** — idle 1.30 W · avg 3.79 W · peak 8.30 W · 228 samples

??? success "Udoo 01 — pass"

    `udoo` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 49.8 s | — |
    | reboot | ✅ | 71.3 s | power-cycle · up 30 s |
    | hw-performance | ✅ | 51.2 s | AES 26 · mem 726 · disk W 19 / R 20 MB/s · 47.5 °C · 996 MHz |
    | dvfs | ✅ | 43.4 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 83.3 s | end0 ↑398/↓224 (1GE) · wlx7cdd903aa418 ↑28/↓18 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 62.5 s | stable |
    | reboot | ✅ | 74.4 s | power-cycle · up 33 s |
    | store-versions | ✅ | 9.5 s | 26.8.1 · 6.18.44-current-imx6 |

    **Power** — idle 3.60 W · avg 6.03 W · peak 8.00 W · 364 samples

??? failure "UEFI arm64 01 — fail"

    `uefi-arm64` · **inplace** · image `26.11.0-trunk.30` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.45 · reachable=False · port=22 |

??? success "UEFI x86 01 — pass"

    `uefi-x86` · **inplace** · image `26.11.0-trunk.35` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 21.8 s | — |
    | reboot | ✅ | 91.7 s | power-cycle · up 61 s |
    | hw-performance | ✅ | 25.3 s | AES 237 · mem 6300 · disk W 26 / R 109 MB/s · 57 °C · 1920 MHz |
    | dvfs | ❌ | 23.9 s | schedutil · 480–1920 MHz (peak 1680) |
    | network-iperf | ✅ | 61.9 s | enp1s0 ↑888/↓941 (1GE) · wlan0 ↑27/↓22 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 26.2 s | stable |
    | reboot | ✅ | 92.0 s | power-cycle · up 59 s |
    | store-versions | ✅ | 5.3 s | 26.11.0-trunk.35 · 6.18.44-current-x86 |

    **Power** — idle 2.50 W · avg 3.90 W · peak 7.80 W · 273 samples

??? success "ZeroPi 01 — pass"

    `zeropi` · **inplace** · image `26.11.0-trunk.49` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 35.9 s | — |
    | reboot | ✅ | 55.2 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 39.5 s | AES 25 · mem 1500 · disk W 2 / R 23 MB/s · 45.8 °C · 1296 MHz |
    | dvfs | ✅ | 34.1 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 44.5 s | end0 ↑628/↓920 (1GE) Mbps |
    | restore-stable | ✅ | 53.9 s | stable |
    | reboot | ✅ | 56.3 s | power-cycle · up 25 s |
    | store-versions | ✅ | 8.1 s | 26.11.0-trunk.49 · 6.18.44-current-sunxi |

    **Power** — idle 1.10 W · avg 2.08 W · peak 3.00 W · 261 samples


<!-- FLEET-STOP -->
