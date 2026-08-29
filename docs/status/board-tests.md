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

**87** boards — **48** passed, **39** failed. Each card is the board's most recent test.

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

??? failure "Banana Pi CM4IO 01 — fail"

    `bananapicm4io` · **inplace** · image `26.11.0-trunk.27` · 1 ✅ · 1 ❌ · 6 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 111.4 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ❌ | 205.2 s | power-cycle |
    | hw-perf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | dvfs | ⏭️ | 0.0 s | — |
    | net-iperf | ⏭️ | 0.0 s | board down after reboot/power-cycle |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ⏭️ | 0.0 s | — |

??? failure "Banana Pi M2 Ultra 01 — fail"

    `bananapim2ultra` · **inplace** · image `26.11.0-trunk.19` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.83 · reachable=False · port=22 |

??? success "Banana Pi M2Pro 01 — pass"

    `bananapim2pro` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 118.2 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 46.1 s | power-cycle · up 22 s |
    | hw-performance | ✅ | 20.0 s | AES 980 · mem 5300 · disk W 42 / R 152 MB/s · 53.1 °C · 2100 MHz |
    | dvfs | ✅ | 20.0 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 257.3 s | end0 ↑940/↓941 (1GE) · wlx60fb00480eb0 ↑192/↓211 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 80.5 s | stable |
    | reboot | ✅ | 43.0 s | power-cycle · up 18 s |
    | store-versions | ✅ | 4.5 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? success "Banana Pi M5 01 — pass"

    `bananapim5` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 185.6 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 171.8 s | warm · up 155 s |
    | hw-performance | ✅ | 37.6 s | AES 979 · mem 5300 · disk W 10 / R 15 MB/s · 54.7 °C · 2100 MHz |
    | dvfs | ✅ | 20.2 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 108.2 s | end0 ↑940/↓941 (1GE) · wlx000f13960190 ↑1/↓11 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 144.8 s | stable |
    | reboot | ✅ | 167.1 s | warm · up 150 s |
    | store-versions | ✅ | 4.8 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? success "Banana Pi Pro 01 — pass"

    `bananapipro` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 278.8 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 65.1 s | warm · up 44 s |
    | hw-performance | ✅ | 49.6 s | AES 19 · mem 1700 · disk W 19 / R 22 MB/s · 50.7 °C · 960 MHz |
    | dvfs | ✅ | 46.3 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 206.4 s | end0 ↑94/↓94 (10/100ME) · wlan0 ↑8/↓17 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 191.7 s | stable |
    | reboot | ✅ | 64.2 s | warm · up 43 s |
    | store-versions | ✅ | 11.0 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi |

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

    `radxa-cubie-a5e` · **inplace** · image `26.11.0-trunk.27` · 7 ✅ · 0 ❌ · 1 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 189.9 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 141.2 s | power-cycle · up 112 s |
    | hw-performance | ✅ | 46.8 s | AES 358 · mem 2000 · disk W 10 / R 23 MB/s · 67.1 °C · None MHz |
    | dvfs | ➖ | 2.6 s | — |
    | network-iperf | ✅ | 172.9 s | end0 ↑916/↓938 (1GE) · end1 ↑941/↓940 (1GE) Mbps |
    | restore-stable | ✅ | 130.6 s | stable |
    | reboot | ✅ | 139.9 s | power-cycle · up 112 s |
    | store-versions | ✅ | 5.5 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi64 |

    **Power** — idle 1.00 W · avg 4.17 W · peak 5.20 W · 688 samples

??? success "Cubietruck 01 — pass"

    `cubietruck` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 285.2 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 65.4 s | warm · up 44 s |
    | hw-performance | ✅ | 59.5 s | AES 19 · mem 1600 · disk W 15 / R 22 MB/s · 46.4 °C · 960 MHz |
    | dvfs | ✅ | 55.7 s | ondemand · 528–960 MHz (peak 960) |
    | network-iperf | ✅ | 264.9 s | end0 ↑722/↓732 (1GE) · wlan0 ↑12/↓26 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 190.8 s | stable |
    | reboot | ✅ | 65.7 s | warm · up 45 s |
    | store-versions | ✅ | 12.2 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi |

??? success "Cubox i2eX/i4 01 — pass"

    `radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 308.5 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 49.8 s | warm · up 30 s |
    | hw-performance | ✅ | 46.7 s | AES 26 · mem 709 · disk W 19 / R 20 MB/s · 54.3 °C · 996 MHz |
    | dvfs | ✅ | 39.6 s | ondemand · 396–996 MHz (peak 996) |
    | network-iperf | ✅ | 231.7 s | end0 ↑392/↓586 (1GE) · wlan0 ↑19/↓20 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 233.4 s | stable |
    | reboot | ✅ | 50.7 s | warm · up 30 s |
    | store-versions | ✅ | 8.6 s | 26.11.0-trunk.27 · 6.18.44-current-imx6 |

??? success "Espressobin 01 — pass"

    `espressobin` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 46.7 s | AES 371 · mem 2000 · disk W 22 / R 83 MB/s · None °C · 800 MHz |
    | dvfs | ✅ | 33.8 s | ondemand · 200–800 MHz (peak 800) |
    | network-iperf | ✅ | 44.1 s | lan0 ↑932/↓746 (1GE) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 7.9 s | 26.8.3 · 6.18.42-current-mvebu64 |

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
    | upgrade | ✅ | 189.8 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 36.5 s | warm · up 17 s |
    | hw-performance | ✅ | 23.7 s | AES 655 · mem 3500 · disk W 42 / R 145 MB/s · 56 °C · 1512 MHz |
    | dvfs | ✅ | 25.2 s | ondemand · 500–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 98.8 s | eth0 ↑940/↓941 (1GE) · wlan0 ↑73/↓92 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 127.9 s | stable |
    | reboot | ✅ | 35.3 s | warm · up 17 s |
    | store-versions | ✅ | 5.4 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

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

    `lepotato` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 205.4 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 43.4 s | warm · up 27 s |
    | hw-performance | ✅ | 32.0 s | AES 656 · mem 3500 · disk W 16 / R 2 MB/s · 50 °C · 1512 MHz |
    | dvfs | ✅ | 22.9 s | ondemand · 500–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 111.5 s | end0 ↑94/↓94 (10/100ME) Mbps |
    | restore-stable | ✅ | 150.2 s | stable |
    | reboot | ✅ | 41.0 s | warm · up 24 s |
    | store-versions | ✅ | 5.6 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

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

    `nanopim4v2` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 105.9 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 53.1 s | power-cycle · up 25 s |
    | hw-performance | ✅ | 20.9 s | AES 1019 · mem 6600 · disk W 54 / R 60 MB/s · 46.2 °C · 1416 MHz |
    | dvfs | ✅ | 19.8 s | ondemand · 408–1416 MHz (peak 1800) |
    | network-iperf | ✅ | 163.6 s | end0 ↑939/↓939 (1GE) · wlan0 ↑131/↓138 (Wi-Fi 5) · wlx803f5d16af63 ↑128/↓153 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 79.1 s | stable |
    | reboot | ✅ | 55.5 s | power-cycle · up 27 s |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

    **Power** — idle 3.00 W · avg 7.06 W · peak 12.50 W · 411 samples

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
    | hw-performance | ✅ | 39.8 s | AES 25 · mem 2200 · disk W 19 / R 22 MB/s · 44.9 °C · 1296 MHz |
    | dvfs | ✅ | 32.9 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 70.8 s | end0 ↑707/↓941 (1GE) · wlan0 ↑20/↓23 (Wi-Fi 4) Mbps |
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

    `nanopi-r76s` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 91.1 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 40.2 s | warm · up 23 s |
    | hw-performance | ✅ | 17.6 s | AES 1310 · mem 8800 · disk W 62 / R 70 MB/s · 46.2 °C · 2016 MHz |
    | dvfs | ✅ | 17.1 s | ondemand · 408–2016 MHz (peak 2208) |
    | network-iperf | ✅ | 120.8 s | end0 ↑2353/↓2354 (2.5GE) · end1 ↑2353/↓2254 (2.5GE) · wlan0 ↑98/↓180 (Wi-Fi 5) · wlxe0e1a933de37 ↑69/↓142 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 64.3 s | stable |
    | reboot | ✅ | 36.6 s | warm · up 18 s |
    | store-versions | ✅ | 3.8 s | 26.11.0-trunk.27 · 7.1.8-edge-rockchip64 |

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

    `odroidc4` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 131.8 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 41.0 s | power-cycle · up 16 s |
    | hw-performance | ✅ | 21.7 s | AES 980 · mem 5200 · disk W 30 / R 78 MB/s · 44.1 °C · 2100 MHz |
    | dvfs | ✅ | 19.3 s | ondemand · 1000–2100 MHz (peak 2100) |
    | network-iperf | ✅ | 132.6 s | end0 ↑941/↓941 (1GE) · wlx24050fdd332b ↑77/↓128 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 96.6 s | stable |
    | reboot | ✅ | 41.9 s | power-cycle · up 16 s |
    | store-versions | ✅ | 4.4 s | 26.11.0-trunk.27 · 6.18.44-current-meson64 |

??? success "Odroid M1 01 — pass"

    `odroidm1` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 108.6 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 52.5 s | power-cycle · up 21 s |
    | hw-performance | ✅ | 16.8 s | AES 914 · mem 5000 · disk W 1038 / R 1020 MB/s · 37.2 °C · 1992 MHz |
    | dvfs | ✅ | 21.5 s | ondemand · 408–1992 MHz (peak 1992) |
    | network-iperf | ✅ | 86.8 s | eth0 ↑551/↓941 (1GE) · wlx40a5eff39254 ↑153/↓136 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 73.9 s | stable |
    | reboot | ✅ | 53.3 s | power-cycle · up 20 s |
    | store-versions | ✅ | 4.7 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

    **Power** — idle 1.60 W · avg 5.22 W · peak 10.90 W · 341 samples

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

??? success "Odroid XU4 01 — pass"

    `odroidxu4` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 173.0 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 61.2 s | power-cycle · up 31 s |
    | hw-performance | ✅ | 37.9 s | AES 71 · mem 5500 · disk W 1 / R 54 MB/s · 57 °C · 1400 MHz |
    | dvfs | ✅ | 29.1 s | ondemand · 600–1400 MHz (peak 2000) |
    | network-iperf | ✅ | 278.2 s | enx001e0636e380 ↑924/↓941 (1GE) Mbps |
    | restore-stable | ✅ | 118.2 s | stable |
    | reboot | ✅ | 57.2 s | power-cycle · up 31 s |
    | store-versions | ✅ | 7.0 s | 26.11.0-trunk.27 · 6.6.151-current-odroidxu4 |

??? failure "Orange Pi 3 01 — fail"

    `orangepi3` · **inplace** · image `26.11.0-trunk.19` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.41 · reachable=False · port=22 |

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

    `orangepi5-plus` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 107.2 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 52.2 s | power-cycle · up 27 s |
    | hw-performance | ✅ | 17.5 s | AES 1263 · mem 14000 · disk W 55 / R 63 MB/s · 45.3 °C · 1800 MHz |
    | dvfs | ✅ | 16.2 s | ondemand · 1800–1800 MHz (peak 2256) |
    | network-iperf | ✅ | 232.1 s | enP3p49s0 ↑2351/↓2223 (2.5GE) · enP4p65s0 ↑941/↓941 (1GE) · wlxe0e1a9380c53 ↑636/↓427 (Wi-Fi 6) Mbps |
    | restore-stable | ✅ | 89.1 s | stable |
    | reboot | ✅ | 51.0 s | power-cycle · up 26 s |
    | store-versions | ✅ | 3.4 s | 26.11.0-trunk.27 · 6.1.115-vendor-rk35xx |

    **Power** — idle 2.70 W · avg 6.07 W · peak 13.50 W · 458 samples

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

    `orangepioneplus` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 146.6 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 33.5 s | warm · up 17 s |
    | hw-performance | ✅ | 30.0 s | AES 835 · mem 4600 · disk W 21 / R 23 MB/s · 61.6 °C · 1800 MHz |
    | dvfs | ✅ | 22.6 s | ondemand · 480–1800 MHz (peak 1800) |
    | network-iperf | ✅ | 227.7 s | end0 ↑916/↓942 (1GE) · wlx00e04c881724 ↑121/↓101 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 97.8 s | stable |
    | reboot | ✅ | 35.5 s | warm · up 19 s |
    | store-versions | ✅ | 5.1 s | 26.11.0-trunk.27 · 7.1.8-edge-sunxi64 |

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

    `orangepipc2` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 244.0 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 60.0 s | power-cycle · up 34 s |
    | hw-performance | ✅ | 38.2 s | AES 638 · mem 3500 · disk W 9 / R 22 MB/s · 62.7 °C · 1368 MHz |
    | dvfs | ✅ | 24.1 s | ondemand · 480–1368 MHz (peak 1368) |
    | network-iperf | ✅ | 39.4 s | end0 ↑847/↓872 (1GE) Mbps |
    | restore-stable | ✅ | 182.9 s | stable |
    | reboot | ✅ | 59.0 s | power-cycle · up 34 s |
    | store-versions | ✅ | 5.2 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi64 |

??? success "Orange Pi Prime 01 — pass"

    `orangepiprime` · **inplace** · image `26.8.3` · 3 ✅ · 0 ❌ · 5 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 45.0 s | AES 379 · mem 2100 · disk W 21 / R 23 MB/s · 38.2 °C · None MHz |
    | dvfs | ➖ | 3.1 s | — |
    | network-iperf | ✅ | 166.3 s | end0 ↑883/↓787 (1GE) · wlan0 ↑25/↓34 (Wi-Fi 4) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 6.5 s | 26.8.3 · 6.18.38-current-sunxi64 |

??? success "Orange Pi R1 01 — pass"

    `orangepi-r1` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 245.8 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 52.9 s | warm · up 35 s |
    | hw-performance | ✅ | 39.7 s | AES 25 · mem 1400 · disk W 21 / R 23 MB/s · 63.2 °C · 1296 MHz |
    | dvfs | ✅ | 34.0 s | ondemand · 480–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 124.6 s | enxc0742bfffce9 ↑94/↓94 (10/100ME) · wlan0 ↑21/↓28 (Wi-Fi 4) · wlan1 ↑12/↓31 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 158.3 s | stable |
    | reboot | ✅ | 53.6 s | warm · up 34 s |
    | store-versions | ✅ | 9.1 s | 26.11.0-trunk.27 · 6.18.44-current-sunxi |

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

    `orangepizero2` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 160.3 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 44.2 s | power-cycle · up 19 s |
    | hw-performance | ✅ | 32.8 s | AES 705 · mem 3000 · disk W 21 / R 23 MB/s · 60.9 °C · 1512 MHz |
    | dvfs | ✅ | 26.3 s | ondemand · 480–1512 MHz (peak 1512) |
    | network-iperf | ✅ | 123.7 s | end0 ↑877/↓941 (1GE) · wlx7c023a625db1 ↑35/↓34 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 136.2 s | stable |
    | reboot | ✅ | 44.2 s | power-cycle · up 19 s |
    | store-versions | ✅ | 6.0 s | 26.11.0-trunk.27 · 7.1.8-edge-sunxi64 |

??? success "OrangePi 3 LTS 01 — pass"

    `orangepi3-lts` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 20.8 s | AES 750 · mem 4100 · disk W 55 / R 127 MB/s · 63.9 °C · 1608 MHz |
    | dvfs | ✅ | 21.4 s | ondemand · 480–1608 MHz (peak 1608) |
    | network-iperf | ✅ | 155.0 s | end0 ↑921/↓941 (1GE) · wlan0 ↑42/↓9 (Wi-Fi 5) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.8 s | 26.8.3 · 7.0.14-edge-sunxi64 |

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

    `radxa-dragon-q6a` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 77.4 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 136.2 s | power-cycle · up 106 s |
    | hw-performance | ✅ | 13.2 s | AES 1511 · mem 18600 · disk W 252 / R 1164 MB/s · 48.4 °C · 1958 MHz |
    | dvfs | ✅ | 14.0 s | ondemand · 300–1958 MHz (peak 2707) |
    | network-iperf | ✅ | 28.2 s | enp1s0 ↑941/↓940 (1GE) Mbps |
    | restore-stable | ✅ | 64.8 s | stable |
    | reboot | ✅ | 135.8 s | power-cycle · up 106 s |
    | store-versions | ✅ | 3.6 s | 26.11.0-trunk.27 · 6.18.2-current-qcs6490 |

    **Power** — idle 1.00 W · avg 2.59 W · peak 8.30 W · 385 samples

??? success "Radxa ZERO 3 01 — pass"

    `radxa-zero3` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 32.7 s | AES 720 · mem 3900 · disk W 21 / R 22 MB/s · 50.6 °C · 1416 MHz |
    | dvfs | ✅ | 25.4 s | ondemand · 408–1416 MHz (peak 1416) |
    | network-iperf | ✅ | 50.5 s | wlan0 ↑11/↓10 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 9.5 s | 26.5.1 · 6.18.24-current-rockchip64 |

??? success "Raspberry Pi 01 — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 50.2 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 42.7 s | power-cycle · up 19 s |
    | hw-performance | ✅ | 14.3 s | AES 1368 · mem 12100 · disk W 56 / R 90 MB/s · 70.5 °C · 2400 MHz |
    | dvfs | ✅ | 13.3 s | ondemand · 1500–2400 MHz (peak 2400) |
    | network-iperf | ✅ | 50.9 s | end0 ↑936/↓941 (1GE) · wlan0 ↑28/↓38 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 37.6 s | stable |
    | reboot | ✅ | 44.2 s | power-cycle · up 21 s |
    | store-versions | ✅ | 3.0 s | 26.11.0-trunk.27 · 6.18.44-current-bcm2711 |

    **Power** — idle 2.20 W · avg 5.30 W · peak 8.30 W · 205 samples

??? success "Raspberry Pi 02 — pass"

    `rpi4b` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 170.5 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 37.5 s | warm · up 19 s |
    | hw-performance | ✅ | 33.6 s | AES 40 · mem 2500 · disk W 20 / R 22 MB/s · 61.8 °C · 1200 MHz |
    | dvfs | ✅ | 26.5 s | ondemand · 600–1200 MHz (peak 1200) |
    | network-iperf | ✅ | 88.5 s | enxb827eb253a53 ↑94/↓94 (10/100ME) · wlan0 ↑22/↓36 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 122.5 s | stable |
    | reboot | ✅ | 38.1 s | warm · up 19 s |
    | store-versions | ✅ | 6.0 s | 26.11.0-trunk.27 · 6.18.44-current-bcm2711 |

??? success "ROCK 2F 01 — pass"

    `rock-2f` · **inplace** · image `26.5.1` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 27.5 s | AES 822 · mem 5900 · disk W 32 / R 65 MB/s · 49 °C · 2016 MHz |
    | dvfs | ✅ | 25.1 s | ondemand · 408–2016 MHz (peak 2016) |
    | network-iperf | ✅ | 100.7 s | wlan0 ↑78/↓56 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 5.4 s | 26.5.1 · 6.1.115-vendor-rk35xx |

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

    `rock-5b` · **inplace** · image `26.8.3` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.32 · reachable=False · port=22 |

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

    `rock-5b-plus` · **inplace** · image `26.8.3` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.47 · reachable=False · port=22 |

??? success "Rock 5T 01 — pass"

    `rock-5t` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 84.4 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 44.2 s | power-cycle · up 16 s |
    | hw-performance | ✅ | 18.1 s | AES 1250 · mem 10000 · disk W 51 / R 83 MB/s · 59.2 °C · 1800 MHz |
    | dvfs | ✅ | 16.4 s | ondemand · 408–1800 MHz (peak 2400) |
    | network-iperf | ✅ | 117.5 s | enP3p49s0 ↑2353/↓2354 (2.5GE) · enP4p65s0 ↑2353/↓2354 (2.5GE) · wlP2p33s0 ↑323/↓258 (Wi-Fi 6) · wlx7cdd90ebf00a ↑94/↓119 (Wi-Fi 4) Mbps |
    | restore-stable | ✅ | 66.5 s | stable |
    | reboot | ✅ | 45.2 s | power-cycle · up 17 s |
    | store-versions | ✅ | 3.9 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

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

    `rockpi-e` · **inplace** · image `26.11.0-trunk.27` · 8 ✅ · 0 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ✅ | 200.2 s | nightly · 26.11.0-trunk.27 → 26.11.0-trunk.27 |
    | reboot | ✅ | 53.3 s | power-cycle · up 24 s |
    | hw-performance | ✅ | 31.7 s | AES 598 · mem 3300 · disk W 21 / R 23 MB/s · 62.9 °C · 1296 MHz |
    | dvfs | ✅ | 25.2 s | ondemand · 408–1296 MHz (peak 1296) |
    | network-iperf | ✅ | 61.7 s | end0 ↑941/↓941 (1GE) · wlx7ca7b020e87c ↑160/↓205 (Wi-Fi 5) Mbps |
    | restore-stable | ✅ | 147.9 s | stable |
    | reboot | ✅ | 49.6 s | power-cycle · up 25 s |
    | store-versions | ✅ | 13.0 s | 26.11.0-trunk.27 · 6.18.44-current-rockchip64 |

??? success "SpacemiT K3 Pico-ITX 01 — pass"

    `k3picoitx` · **inplace** · image `26.8.3` · 4 ✅ · 0 ❌ · 4 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | upgrade | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | hw-performance | ✅ | 22.2 s | AES 797 · mem 12000 · disk W 25 / R 40 MB/s · 62 °C · 2200 MHz |
    | dvfs | ✅ | 15.5 s | performance · 614–2200 MHz (peak 2200) |
    | network-iperf | ✅ | 60.2 s | eth0 ↑941/↓941 (1GE) · wlan0 ↑56/↓170 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 3.7 s | 26.8.3 · 6.18.3-legacy-spacemit-k3 |

    **Power** — idle 13.50 W · avg 14.87 W · peak 22.70 W · 88 samples

??? failure "Tanix TX6 01 — fail"

    `tanix-tx6` · **inplace** · image `26.11.0-trunk.6` · 0 ✅ · 1 ❌ · 0 ⏭️

    | Module | Status | Time | Detail |
    |:--|:--:|--:|:--|
    | reachable | ❌ | 0.0 s | ip=10.0.50.21 · reachable=False · port=22 |

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
    | hw-performance | ✅ | 15.7 s | AES 1402 · mem 13000 · disk W 1578 / R 2263 MB/s · 45 °C · 2600 MHz |
    | dvfs | ✅ | 18.6 s | ondemand · 800–2600 MHz (peak 2600) |
    | network-iperf | ✅ | 123.5 s | enp1s0 ↑8788/↓9372 (10GE) · enp49s0 ↑7633/↓9377 (10GE) · wlp97s0 ↑111/↓86 (Wi-Fi 6) Mbps |
    | restore-stable | ⏭️ | 0.0 s | — |
    | reboot | ⏭️ | 0.0 s | reboot |
    | store-versions | ✅ | 4.4 s | 26.8.0-trunk.314 · 7.1.2-edge-arm64 |

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
