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

**86** boards — **47** passed, **39** failed. Each card is the board's most recent test.

??? success "Arduino UNO Q 01 — pass"

    `arduino-uno-q` · **inplace** · image `26.11.0-trunk.6` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 23.8 s | — |
    | reboot | ✅ | 50.7 s | warm · up 34 s |
    | hw-performance | ✅ | 24.7 s | AES 940 · mem 5100 · disk W 169 / R 222 MB/s · 45 °C · 2016 MHz |
    | dvfs | ✅ | 32.1 s | schedutil · 300–2016 MHz (peak 2016) |
    | network-iperf | ❌ | 375.2 s | usb0 ↑0/↓0 (1GE) · wlan0 ↑22/↓19 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 27.5 s | stable |
    | reboot | ✅ | 50.8 s | warm · up 34 s |
    | store-versions | ✅ | 6.8 s | 26.11.0-trunk.6 · 7.1.8-edge-qrb2210 |

??? success "Banana Pi CM4IO 01 — pass"

    `bananapicm4io` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 15.5 s | — |
    | reboot | ✅ | 52.1 s | power-cycle · up 28 s |
    | hw-performance | ✅ | 26.8 s | AES 1364 · mem 6200 · disk W 13 / R 22 MB/s · 62.3 °C · 2016 MHz |
    | dvfs | ✅ | 15.8 s | performance · 1000–2016 MHz (peak 2400) |
    | network-iperf | ✅ | 248.0 s | end0 ↑937/↓941 (1GE) · wlan0 ↑32/↓33 (Wi-Fi 5) · wlx00e032c00694 ↑101/↓172 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 15.7 s | stable |
    | reboot | ✅ | 47.3 s | power-cycle · up 24 s |
    | store-versions | ✅ | 3.4 s | 26.8.3 · 6.18.44-current-meson64 |

??? failure "Banana Pi M2 Ultra 01 — fail"

    `bananapim2ultra` · **inplace** · image `26.11.0-trunk.19` · 0 ✅ · 1 ❌ · 7 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 17.8 s | — |
    | reboot | ❌ | 200.1 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Banana Pi M2Pro 01 — pass"

    `bananapim2pro` · **inplace** · image `26.11.0-trunk.19` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 18.2 s | — |
    | reboot | ✅ | 43.6 s | power-cycle · up 18 s |
    | hw-performance | ✅ | 20.6 s | AES 978 · mem 5300 · disk W 43 / R 158 MB/s · 53.1 °C · 2100 MHz |
    | dvfs | ✅ | 19.6 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 255.7 s | end0 ↑940/↓941 (1GE) · wlx60fb00480eb0 ↑139/↓87 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 20.5 s | stable |
    | reboot | ✅ | 47.5 s | power-cycle · up 18 s |
    | store-versions | ✅ | 5.1 s | 26.11.0-trunk.19 · 6.18.44-current-meson64 |

??? success "Banana Pi M5 01 — pass"

    `bananapim5` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 15.5 s | — |
    | reboot | ✅ | 173.0 s | warm · up 155 s |
    | hw-performance | ✅ | 38.2 s | AES 980 · mem 5300 · disk W 11 / R 15 MB/s · 56.2 °C · 2100 MHz |
    | dvfs | ✅ | 19.7 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 274.1 s | end0 ↑941/↓941 (1GE) · wlx000f13960190 ↑1/↓5 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 26.4 s | stable |
    | reboot | ✅ | 166.0 s | warm · up 149 s |
    | store-versions | ✅ | 5.3 s | 26.8.3 · 6.18.44-current-meson64 |

??? success "Banana Pi Pro 01 — pass"

    `bananapipro` · **inplace** · image `26.11.0-trunk.19` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 51.3 s | — |
    | reboot | ✅ | 64.6 s | warm · up 44 s |
    | hw-performance | ✅ | 51.7 s | AES 19 · mem 1700 · disk W 21 / R 22 MB/s · 50.9 °C · 960 MHz |
    | dvfs | ✅ | 47.1 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 304.6 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑16/↓10 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 58.9 s | stable |
    | reboot | ✅ | 62.8 s | warm · up 43 s |
    | store-versions | ✅ | 11.2 s | 26.11.0-trunk.19 · 6.18.44-current-sunxi |

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
    | upgrade | ⏭️ | 28.8 s | — |
    | reboot | ✅ | 139.8 s | power-cycle · up 113 s |
    | hw-performance | ✅ | 46.4 s | AES 358 · mem 2000 · disk W 11 / R 23 MB/s · 69.2 °C · None MHz |
    | dvfs | ➖ | 2.6 s | — |
    | network-iperf | ✅ | 205.2 s | end0 ↑910/↓941 (1GE) · end1 ↑940/↓940 (1GE) Mbps |
    | restore-stable | ✅ | 34.1 s | stable |
    | reboot | ✅ | 141.2 s | power-cycle · up 110 s |
    | store-versions | ✅ | 5.5 s | 26.11.0-trunk.19 · 6.18.44-current-sunxi64 |

    **Power** — idle 2.40 W · avg 4.18 W · peak 5.50 W · 495 samples

??? success "Cubietruck 01 — pass"

    `cubietruck` · **inplace** · image `26.11.0-trunk.19` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 50.8 s | — |
    | reboot | ✅ | 63.4 s | warm · up 43 s |
    | hw-performance | ✅ | 58.7 s | AES 18 · mem 1600 · disk W 19 / R 21 MB/s · 47.6 °C · 960 MHz |
    | dvfs | ✅ | 55.8 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 517.6 s | end0 ↑715/↓748 (1GE) · wlan0 ↑20/↓20 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 56.7 s | stable |
    | reboot | ✅ | 63.1 s | warm · up 43 s |
    | store-versions | ✅ | 12.3 s | 26.11.0-trunk.19 · 6.18.44-current-sunxi |

??? success "Espressobin 01 — pass"

    `espressobin` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 41.0 s | AES 371 · mem 2000 · disk W 21 / R 127 MB/s · None °C · 800 MHz |
    | dvfs | ✅ | 33.6 s | ondemand · 200–800 MHz (peak 800) |
    | network-iperf | ✅ | 70.0 s | lan0 ↑924/↓756 (1GE) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.3 s | 26.8.3 · 6.18.42-current-mvebu64 |

??? success "Helios4 01 — pass"

    `helios4` · **inplace** · image `26.8.3` · 6 ✅ · 0 ❌ · 2 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 23.4 s | — |
    | reboot | ✅ | 36.7 s | warm · up 19 s |
    | hw-performance | ✅ | 41.5 s | AES 44 · mem 3700 · disk W 20 / R 23 MB/s · 57 °C · None MHz |
    | dvfs | ➖ | 2.8 s | — |
    | network-iperf | ✅ | 179.1 s | end1 ↑941/↓941 (1GE) · wlx1cbfce1f85a5 ↑235/↓81 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 23.3 s | stable |
    | reboot | ✅ | 37.4 s | warm · up 19 s |
    | store-versions | ✅ | 5.8 s | 26.8.3 · 6.6.151-current-mvebu |

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

    `khadas-vim2` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 22.1 s | — |
    | reboot | ✅ | 36.7 s | warm · up 18 s |
    | hw-performance | ✅ | 23.9 s | AES 658 · mem 3500 · disk W 42 / R 151 MB/s · 54 °C · 1512 MHz |
    | dvfs | ✅ | 25.2 s | ondemand · 500–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 255.9 s | eth0 ↑939/↓941 (1GE) · wlan0 ↑76/↓84 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 32.6 s | stable |
    | reboot | ✅ | 35.4 s | warm · up 18 s |
    | store-versions | ✅ | 5.4 s | 26.8.3 · 6.18.44-current-meson64 |

??? failure "Khadas VIM3 01 — fail"

    `khadas-vim3` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 50.0 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 199.8 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Le potato 01 — pass"

    `lepotato` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 22.1 s | — |
    | reboot | ✅ | 42.8 s | warm · up 26 s |
    | hw-performance | ✅ | 31.9 s | AES 659 · mem 3600 · disk W 16 / R 2 MB/s · 50 °C · 1512 MHz |
    | dvfs | ✅ | 22.8 s | ondemand · 500–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 173.2 s | end0 ↑94/↓94 (10/100ME) Mbps |
    | restore-stable | ✅ | 31.6 s | stable |
    | reboot | ✅ | 38.4 s | warm · up 22 s |
    | store-versions | ✅ | 4.9 s | 26.8.3 · 6.18.44-current-meson64 |

??? failure "Mekotronics R58S2 01 — fail"

    `mekotronics-r58s2` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 130.0 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 205.0 s | power-cycle |
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

??? failure "NanoPi Duo 01 — fail"

    `nanopiduo` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 156.0 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 204.0 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "NanoPi K2 01 — fail"

    `nanopik2-s905` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 80.4 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 197.8 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "NanoPi M4V2 01 — pass"

    `nanopim4v2` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 16.4 s | — |
    | reboot | ✅ | 53.0 s | power-cycle · up 26 s |
    | hw-performance | ✅ | 21.2 s | AES 1022 · mem 6300 · disk W 54 / R 60 MB/s · 47.5 °C · 1416 MHz |
    | dvfs | ✅ | 19.6 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 452.3 s | end0 ↑938/↓939 (1GE) · wlan0 ↑157/↓193 (Wi-Fi 5) · wlx803f5d16af63 ↑120/↓199 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 19.5 s | stable |
    | reboot | ✅ | 53.5 s | power-cycle · up 27 s |
    | store-versions | ✅ | 4.8 s | 26.8.3 · 6.18.44-current-rockchip64 |

    **Power** — idle 2.50 W · avg 6.65 W · peak 12.60 W · 524 samples

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

??? failure "NanoPi Neo 3 01 — fail"

    `nanopineo3` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 121.0 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 209.7 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "NanoPi R1 01 — pass"

    `nanopi-r1` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 39.9 s | AES 25 · mem 2200 · disk W 19 / R 22 MB/s · 46.7 °C · 1296 MHz |
    | dvfs | ✅ | 33.2 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 249.1 s | end0 ↑707/↓916 (1GE) · wlan0 ↑2/↓4 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.2 s | 26.8.3 · 6.18.38-current-sunxi |

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

??? failure "NanoPi R6S 01 — fail"

    `nanopi-r6s` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 32.3 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 215.3 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

    **Power** — idle 3.30 W · avg 4.23 W · peak 5.90 W · 190 samples

??? success "NanoPi R76S 01 — pass"

    `nanopi-r76s` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 11.3 s | — |
    | reboot | ✅ | 35.2 s | warm · up 17 s |
    | hw-performance | ✅ | 17.8 s | AES 1299 · mem 8800 · disk W 62 / R 70 MB/s · 49.9 °C · 2016 MHz |
    | dvfs | ✅ | 17.0 s | ondemand · 408–2016 MHz (peak 2208) |
    | network-iperf | ✅ | 362.2 s | end0 ↑2353/↓2354 (2.5GE) · end1 ↑2351/↓2237 (2.5GE) · wlan0 ↑85/↓135 (Wi-Fi 5) · wlxe0e1a933de37 ↑125/↓213 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 14.0 s | stable |
    | reboot | ✅ | 36.6 s | warm · up 18 s |
    | store-versions | ✅ | 4.0 s | 26.8.3 · 7.1.8-edge-rockchip64 |

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

??? success "Odroid C1 01 — pass"

    `odroidc1` · **inplace** · image `26.8.0-trunk.314` · 3 ✅ · 0 ❌ · 5 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 80.8 s | AES 29 · mem 1900 · disk W 3 / R 10 MB/s · 55.6 °C · 1536 MHz |
    | dvfs | ➖ | 6.0 s | ondemand · 504–1536 MHz |
    | network-iperf | ✅ | 121.9 s | eth0 ↑934/↓941 (1GE) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.2 s | 26.8.0-trunk.314 · 6.12.28-current-meson |

??? failure "Odroid C2 01 — fail"

    `odroidc2` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 86.4 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 200.1 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Odroid C4 01 — pass"

    `odroidc4` · **inplace** · image `26.11.0-trunk.6` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 17.4 s | — |
    | reboot | ✅ | 41.2 s | power-cycle · up 16 s |
    | hw-performance | ✅ | 21.7 s | AES 979 · mem 5300 · disk W 30 / R 77 MB/s · 44.7 °C · 2100 MHz |
    | dvfs | ✅ | 18.9 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 235.4 s | end0 ↑940/↓942 (1GE) · wlx24050fdd332b ↑113/↓98 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 19.6 s | stable |
    | reboot | ✅ | 40.8 s | power-cycle · up 16 s |
    | store-versions | ✅ | 4.3 s | 26.11.0-trunk.6 · 6.18.44-current-meson64 |

??? success "Odroid M1 01 — pass"

    `odroidm1` · **inplace** · image `26.11.0-trunk.6` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 17.7 s | — |
    | reboot | ✅ | 52.7 s | power-cycle · up 21 s |
    | hw-performance | ✅ | 16.8 s | AES 914 · mem 5000 · disk W 1037 / R 1040 MB/s · 39.4 °C · 1992 MHz |
    | dvfs | ✅ | 21.6 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 285.4 s | eth0 ↑604/↓941 (1GE) · wlx40a5eff39254 ↑192/↓183 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 21.3 s | stable |
    | reboot | ✅ | 54.9 s | power-cycle · up 23 s |
    | store-versions | ✅ | 4.6 s | 26.11.0-trunk.6 · 6.18.44-current-rockchip64 |

    **Power** — idle 1.60 W · avg 4.86 W · peak 8.30 W · 383 samples

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

??? failure "Odroid XU4 01 — fail"

    `odroidxu4` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 82.9 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 210.0 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Orange Pi 3 01 — fail"

    `orangepi3` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 130.6 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 213.7 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Orange Pi 5 01 — fail"

    `orangepi5` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 33.9 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 196.0 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

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

??? failure "Orange Pi 5 Plus 02 — fail"

    `orangepi5-plus` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 37.4 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 198.1 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Orange Pi One+ 01 — pass"

    `orangepioneplus` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 23.5 s | — |
    | reboot | ✅ | 35.7 s | warm · up 17 s |
    | hw-performance | ✅ | 29.6 s | AES 839 · mem 4600 · disk W 21 / R 23 MB/s · 61.5 °C · 1800 MHz |
    | dvfs | ✅ | 22.6 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 201.6 s | end0 ↑912/↓941 (1GE) · wlx00e04c881724 ↑92/↓67 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 28.6 s | stable |
    | reboot | ✅ | 33.8 s | warm · up 17 s |
    | store-versions | ✅ | 5.8 s | 26.8.3 · 7.1.8-edge-sunxi64 |

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

??? success "Orange Pi PC2 01 — pass"

    `orangepipc2` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 29.0 s | — |
    | reboot | ✅ | 59.4 s | power-cycle · up 34 s |
    | hw-performance | ✅ | 38.8 s | AES 637 · mem 3500 · disk W 9 / R 23 MB/s · 58.4 °C · 1368 MHz |
    | dvfs | ✅ | 22.8 s | ondemand · 480–1368 MHz (peak 1368) |
    | network-iperf | ✅ | 49.2 s | end0 ↑894/↓882 (1GE) Mbps |
    | restore-stable | ✅ | 29.5 s | stable |
    | reboot | ✅ | 54.7 s | power-cycle · up 29 s |
    | store-versions | ✅ | 5.7 s | 26.8.3 · 6.18.44-current-sunxi64 |

??? success "Orange Pi Prime 01 — pass"

    `orangepiprime` · **inplace** · image `26.8.3` · 3 ✅ · 0 ❌ · 5 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 45.1 s | AES 379 · mem 2100 · disk W 21 / R 23 MB/s · 42.7 °C · None MHz |
    | dvfs | ➖ | 3.8 s | — |
    | network-iperf | ✅ | 299.6 s | end0 ↑873/↓941 (1GE) · wlan0 ↑21/↓20 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 6.6 s | 26.8.3 · 6.18.38-current-sunxi64 |

??? success "Orange Pi R1 01 — pass"

    `orangepi-r1` · **inplace** · image `26.11.0-trunk.6` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 40.3 s | — |
    | reboot | ✅ | 52.2 s | warm · up 34 s |
    | hw-performance | ✅ | 39.8 s | AES 25 · mem 1400 · disk W 21 / R 23 MB/s · 62.4 °C · 1296 MHz |
    | dvfs | ✅ | 35.0 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 383.2 s | enxc0742bfffce9 ↑94/↓94 (10/100ME) · wlan0 ↑12/↓31 (Wi-Fi 4) · wlan1 ↑28/↓9 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 46.4 s | stable |
    | reboot | ✅ | 50.4 s | warm · up 32 s |
    | store-versions | ✅ | 8.3 s | 26.11.0-trunk.6 · 6.18.44-current-sunxi |

??? failure "Orange Pi Win 01 — fail"

    `orangepiwin` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 125.1 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 215.8 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Orange Pi Zero 02 — fail"

    `orangepizero` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 178.0 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 202.4 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

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

??? success "Orange Pi Zero2 01 — pass"

    `orangepizero2` · **inplace** · image `26.11.0-trunk.6` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 87.6 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ✅ | 45.5 s | power-cycle · up 19 s |
    | hw-performance | ✅ | 33.3 s | AES 705 · mem 3000 · disk W 21 / R 22 MB/s · 60.6 °C · 1512 MHz |
    | dvfs | ✅ | 26.3 s | ondemand · 480–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 272.1 s | end0 ↑875/↓941 (1GE) · wlx7c023a625db1 ↑38/↓31 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 63.6 s | stable |
    | reboot | ✅ | 45.4 s | power-cycle · up 20 s |
    | store-versions | ✅ | 5.9 s | 26.11.0-trunk.6 · 7.1.8-edge-sunxi64 |

??? success "OrangePi 3 LTS 01 — pass"

    `orangepi3-lts` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 20.6 s | AES 750 · mem 4100 · disk W 55 / R 127 MB/s · 63.9 °C · 1608 MHz |
    | dvfs | ✅ | 21.8 s | ondemand · 480–1608 MHz (peak 1608) |
    | network-iperf | ✅ | 163.3 s | end0 ↑918/↓941 (1GE) · wlan0 ↑30/↓24 (Wi-Fi 5) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.9 s | 26.8.3 · 7.0.14-edge-sunxi64 |

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

    `radxa-dragon-q6a` · **inplace** · image `26.5.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 10.0 s | — |
    | reboot | ✅ | 135.2 s | power-cycle · up 106 s |
    | hw-performance | ✅ | 13.3 s | AES 1510 · mem 15500 · disk W 240 / R 1146 MB/s · 47.3 °C · 1958 MHz |
    | dvfs | ✅ | 14.0 s | ondemand · 300–1958 MHz (peak 2707) |
    | network-iperf | ✅ | 76.5 s | enp1s0 ↑941/↓940 (1GE) Mbps |
    | restore-stable | ✅ | 10.7 s | stable |
    | reboot | ✅ | 136.4 s | power-cycle · up 106 s |
    | store-versions | ✅ | 3.6 s | 26.5.1 · 6.18.2-current-qcs6490 |

    **Power** — idle 1.00 W · avg 2.08 W · peak 6.80 W · 325 samples

??? success "Radxa ZERO 3 01 — pass"

    `radxa-zero3` · **inplace** · image `26.5.1` · 3 ✅ · 1 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 36.6 s | AES 719 · mem 3900 · disk W 21 / R 22 MB/s · 51.9 °C · 1416 MHz |
    | dvfs | ✅ | 31.1 s | ondemand · 408–1416 MHz (peak 1416) |
    | network-iperf | ❌ | 87.3 s | wlan0 ↑0/↓3 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 9.1 s | 26.5.1 · 6.18.24-current-rockchip64 |

??? success "Raspberry Pi 01 — pass"

    `rpi4b` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 6.6 s | — |
    | reboot | ✅ | 39.8 s | power-cycle · up 17 s |
    | hw-performance | ✅ | 14.2 s | AES 1368 · mem 12100 · disk W 53 / R 89 MB/s · 70.5 °C · 2400 MHz |
    | dvfs | ✅ | 13.1 s | ondemand · 1500–2400 MHz (peak 2400) |
    | network-iperf | ✅ | 233.0 s | end0 ↑936/↓941 (1GE) · wlan0 ↑48/↓29 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 8.1 s | stable |
    | reboot | ✅ | 39.9 s | power-cycle · up 17 s |
    | store-versions | ✅ | 3.8 s | 26.8.1 · 6.18.44-current-bcm2711 |

    **Power** — idle 2.10 W · avg 4.93 W · peak 8.90 W · 289 samples

??? failure "Raspberry Pi 02 — fail"

    `rpi4b` · **inplace** · image `26.8.0-trunk.314` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 158.6 s | nightly · 26.8.0-trunk.314 → 26.8.0-trunk.314 |
    | reboot | ❌ | 199.5 s | warm |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "ROCK 2F 01 — pass"

    `rock-2f` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 29.8 s | AES 818 · mem 5900 · disk W 23 / R 65 MB/s · 50.9 °C · 2016 MHz |
    | dvfs | ✅ | 24.9 s | ondemand · 408–2016 MHz (peak 2016) |
    | network-iperf | ✅ | 125.0 s | wlan0 ↑33/↓57 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 5.3 s | 26.5.1 · 6.1.115-vendor-rk35xx |

??? failure "Rock 5B 01 — fail"

    `rock-5b` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 31.8 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 210.8 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Rock 5B 02 — fail"

    `rock-5b` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 33.5 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 214.8 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Rock 5B 03 — fail"

    `rock-5b` · **inplace** · image `26.8.3` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 55.0 s | nightly · 26.8.3 → 26.8.3 |
    | reboot | ❌ | 197.1 s | warm |
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
    | upgrade | ⏭️ | 8.2 s | — |
    | reboot | ❌ | 208.5 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? success "Rock 5T 01 — pass"

    `rock-5t` · **inplace** · image `26.8.3` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 11.5 s | — |
    | reboot | ✅ | 45.0 s | power-cycle · up 16 s |
    | hw-performance | ✅ | 17.9 s | AES 1249 · mem 7600 · disk W 52 / R 82 MB/s · 60.1 °C · 1800 MHz |
    | dvfs | ✅ | 15.6 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 198.8 s | enP3p49s0 ↑2350/↓2354 (2.5GE) · enP4p65s0 ↑2353/↓2354 (2.5GE) · wlP2p33s0 ↑341/↓350 (Wi-Fi 6) · wlx7cdd90ebf00a ↑93/↓124 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 14.0 s | stable |
    | reboot | ✅ | 44.9 s | power-cycle · up 15 s |
    | store-versions | ✅ | 4.0 s | 26.8.3 · 6.18.44-current-rockchip64 |

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

    `rockpi-e` · **inplace** · image `26.8.1` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 23.0 s | — |
    | reboot | ✅ | 53.8 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 31.3 s | AES 603 · mem 3300 · disk W 21 / R 23 MB/s · 64.6 °C · 1296 MHz |
    | dvfs | ✅ | 24.1 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 212.1 s | end0 ↑940/↓941 (1GE) · wlx7ca7b020e87c ↑177/↓204 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 30.9 s | stable |
    | reboot | ✅ | 52.9 s | power-cycle · up 24 s |
    | store-versions | ✅ | 5.5 s | 26.8.1 · 6.18.44-current-rockchip64 |

??? success "SpacemiT K3 Pico-ITX 01 — pass"

    `k3picoitx` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 22.3 s | AES 796 · mem 12000 · disk W 24 / R 40 MB/s · 63 °C · 2200 MHz |
    | dvfs | ✅ | 15.4 s | performance · 614–2200 MHz (peak 2200) |
    | network-iperf | ✅ | 166.7 s | eth0 ↑941/↓941 (1GE) · wlan0 ↑68/↓174 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 3.7 s | 26.8.3 · 6.18.3-legacy-spacemit-k3 |

    **Power** — idle 13.60 W · avg 14.45 W · peak 22.70 W · 175 samples

??? success "Tanix TX6 01 — pass"

    `tanix-tx6` · **inplace** · image `26.11.0-trunk.6` · 6 ✅ · 1 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 23.1 s | — |
    | reboot | ✅ | 32.1 s | warm · up 13 s |
    | hw-performance | ✅ | 20.2 s | AES 793 · mem 4400 · disk W 54 / R 128 MB/s · 71.6 °C · 1704 MHz |
    | dvfs | ✅ | 21.6 s | ondemand · 480–1704 MHz (peak 1704) |
    | network-iperf | ❌ | 224.3 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑0/↓0 (Wi-Fi 5) · wlx44334c47dec3 ↑42/↓29 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 23.5 s | stable |
    | reboot | ✅ | 30.9 s | warm · up 12 s |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.6 · 6.18.44-current-sunxi64 |

??? failure "Tinker Board 01 — fail"

    `tinkerboard` · **inplace** · image `26.11.0-trunk.5` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 58.7 s | nightly · 26.11.0-trunk.5 → 26.11.0-trunk.5 |
    | reboot | ❌ | 212.5 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

    **Power** — idle 1.20 W · avg 3.18 W · peak 5.60 W · 223 samples

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
    | hw-performance | ✅ | 15.9 s | AES 1458 · mem 13000 · disk W 1547 / R 2303 MB/s · 47 °C · 2600 MHz |
    | dvfs | ✅ | 15.4 s | ondemand · 800–2600 MHz (peak 2600) |
    | network-iperf | ✅ | 193.4 s | enp1s0 ↑8260/↓9385 (10GE) · enp49s0 ↑8734/↓9385 (10GE) · wlp97s0 ↑96/↓72 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.3 s | 26.8.0-trunk.314 · 7.1.2-edge-arm64 |

??? failure "UEFI x86 01 — fail"

    `uefi-x86` · **inplace** · image `26.11.0-trunk.6` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 72.5 s | nightly · 26.11.0-trunk.6 → 26.11.0-trunk.6 |
    | reboot | ❌ | 213.4 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

    **Power** — idle 0.90 W · avg 4.47 W · peak 5.60 W · 233 samples

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
