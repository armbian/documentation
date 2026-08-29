---
title: Wi-Fi performance
seo_title: "Armbian Wi-Fi adapter performance benchmarks"
description: "Armbian WiFi performance benchmarks: throughput of USB, SDIO and PCI wireless adapters on single-board computers, tested in the Armbian autotests lab."
---
# Wi-Fi performance

All wireless adapters were tested under consistent conditions - each positioned in close proximity (1-2m) and connected to the same wireless access point (AP). The adapters utilized various interface types, including USB, SDIO, and PCI, to evaluate performance across different hardware configurations.

<!-- DUT-START -->

## Results

_Measured 2026-07-01 11:47 UTC_

**48** wireless link(s) · ✅ **48** pass · 📶 peak ↑ **681** / ↓ **868** Mbps

#### Wi-Fi 7 · 802.11be

| Chip | Attach | Channel | ↑ Up (Mbps) | ↓ Down (Mbps) |
|:--|:--|:--|--:|--:|
| <abbr title="Carrier: Rock 5B Plus">MediaTek MT7925</abbr> | PCIe | 6215 MHz @ 160 | 681 | 868 |
| <abbr title="Carrier: Orange Pi 5 Plus">Qualcomm WCN7851</abbr> | PCIe | 5240 MHz @ 160 | 232 | 784 |

#### Wi-Fi 6 · 802.11ax

| Chip | Attach | Channel | ↑ Up (Mbps) | ↓ Down (Mbps) |
|:--|:--|:--|--:|--:|
| <abbr title="Carrier: Orange Pi 5 Plus">MediaTek MT7921</abbr> | USB | 5240 MHz @ 80 | 646 | 350 |
| <abbr title="Carrier: Rock 5B">Realtek RTL8852BE</abbr> | PCIe | 5240 MHz @ 80 | 199 | 609 |
| <abbr title="Carrier: Rock 5T">Realtek RTL8852BE</abbr> | PCIe | 5240 MHz @ 80 | 348 | 450 |
| <abbr title="Carrier: Tinker Board 2">Realtek RTL8852AE</abbr> | PCIe | 5240 MHz @ 80 | 332 | 416 |
| <abbr title="Carrier: BananaPi BPI-F3">Realtek RTL8852BS</abbr> | SDIO | 5240 MHz @ 80 | 352 | 394 |

#### Wi-Fi 5 · 802.11ac

| Chip | Attach | Channel | ↑ Up (Mbps) | ↓ Down (Mbps) |
|:--|:--|:--|--:|--:|
| <abbr title="Carrier: Pine H64">Realtek RTL8812AU</abbr> | USB | 5240 MHz @ 80 | 200 | 271 |
| <abbr title="Carrier: BananaPi BPI-F3">Realtek RTL8822BU</abbr> | USB | 5240 MHz @ 80 | 265 | 132 |
| <abbr title="Carrier: Helios4">Realtek RTL8821CU</abbr> | USB | 5240 MHz @ 80 | 259 | 241 |
| <abbr title="Carrier: Raspberry Pi">Broadcom (brcmfmac)</abbr> | SDIO | 5240 MHz @ 80 | 247 | 182 |
| <abbr title="Carrier: NanoPi M4V2">MediaTek MT7610</abbr> | USB | 5240 MHz @ 80 | 131 | 245 |
| <abbr title="Carrier: NanoPi M4V2">Broadcom BCM4356</abbr> | SDIO | 5240 MHz @ 40 | 122 | 209 |
| <abbr title="Carrier: Orange Pi Zero2">Unisoc UWE5622</abbr> | — | — | 132 | 93 |
| <abbr title="Carrier: Tanix TX6">Realtek RTL8822CS</abbr> | SDIO | 5240 MHz @ 80 | 119 | 103 |
| <abbr title="Carrier: Orange Pi 3">Broadcom (brcmfmac)</abbr> | SDIO | 5240 MHz @ 80 | 19 | 108 |
| <abbr title="Carrier: Khadas VIM2">Broadcom (brcmfmac)</abbr> | SDIO | 5240 MHz @ 40 | 105 | 97 |
| <abbr title="Carrier: NanoPi M5">Realtek RTL8822CS</abbr> | SDIO | 5240 MHz @ 80 | 44 | 88 |
| <abbr title="Carrier: Banana Pi CM4IO">Realtek RTL8821CU</abbr> | USB | 2437 MHz @ 20 | 45 | 36 |
| <abbr title="Carrier: OrangePi 3 LTS">Unisoc (unisoc_wifi)</abbr> | — | — | 44 | 22 |
| <abbr title="Carrier: Banana Pi M2Pro">Realtek RTL8821CU</abbr> | USB | 2437 MHz @ 20 | 28 | 43 |
| <abbr title="Carrier: Khadas VIM3">Broadcom (brcmfmac)</abbr> | SDIO | 5240 MHz @ 80 | 39 | 42 |
| <abbr title="Carrier: Orange Pi Lite 2">Broadcom (brcmfmac)</abbr> | SDIO | 2437 MHz @ 20 | 29 | 37 |
| <abbr title="Carrier: Banana Pi CM4IO">Realtek RTL8822CS</abbr> | SDIO | 2437 MHz @ 20 | 15 | 28 |
| <abbr title="Carrier: UEFI x86">Broadcom (brcmfmac)</abbr> | SDIO | 5240 MHz @ 40 | 25 | 22 |
| <abbr title="Carrier: Khadas VIM1">Broadcom (brcmfmac)</abbr> | SDIO | 5240 MHz @ 40 | 6 | 22 |

#### Wi-Fi 4 · 802.11n

| Chip | Attach | Channel | ↑ Up (Mbps) | ↓ Down (Mbps) |
|:--|:--|:--|--:|--:|
| <abbr title="Carrier: Odroid C4">Ralink RT5572</abbr> | USB | 5240 MHz @ 40 | 56 | 93 |
| <abbr title="Carrier: Rock 5T">Ralink RT5572</abbr> | USB | 5240 MHz @ 40 | 53 | 73 |
| <abbr title="Carrier: Banana Pi M2 Ultra">Broadcom (brcmfmac)</abbr> | SDIO | 2437 MHz @ 20 | 33 | 44 |
| <abbr title="Carrier: NanoPi R4S">Ralink RT5370</abbr> | USB | 2437 MHz @ 20 | 40 | 25 |
| <abbr title="Carrier: Banana Pi M5">Realtek RTL8192CU</abbr> | USB | 2437 MHz @ 20 | 37 | 27 |
| <abbr title="Carrier: Orange Pi Zero Plus">Realtek RTL8189FS</abbr> | SDIO | — | 35 | 26 |
| <abbr title="Carrier: Udoo">Ralink RT5370</abbr> | USB | 2437 MHz @ 20 | 34 | 18 |
| <abbr title="Carrier: Orange Pi Zero Plus">Realtek RTL8189FS</abbr> | SDIO | — | 33 | 27 |
| <abbr title="Carrier: Orange Pi R1">Realtek RTL8189ES</abbr> | SDIO | — | 29 | 29 |
| <abbr title="Carrier: Tanix TX6">Ralink RT2870/RT3070</abbr> | USB | 2437 MHz @ 20 | 28 | 10 |
| <abbr title="Carrier: Orange Pi R1">Realtek RTL8189ES</abbr> | SDIO | — | 26 | 25 |
| <abbr title="Carrier: Raspberry Pi">Broadcom (brcmfmac)</abbr> | SDIO | 2437 MHz @ 20 | 17 | 24 |
| <abbr title="Carrier: Inovato Quadra">XRadio XR819</abbr> | SDIO | 2437 MHz @ 20 | 12 | 23 |
| <abbr title="Carrier: Cubox i2eX/i4">Broadcom (brcmfmac)</abbr> | SDIO | 2437 MHz @ 20 | 21 | 22 |
| <abbr title="Carrier: NanoPi K2">Broadcom (brcmfmac)</abbr> | SDIO | 2437 MHz @ 20 | 15 | 22 |
| <abbr title="Carrier: Cubietruck">Broadcom (brcmfmac)</abbr> | SDIO | 2437 MHz @ 20 | 14 | 21 |
| <abbr title="Carrier: Banana Pi Pro">Broadcom (brcmfmac)</abbr> | SDIO | 2437 MHz @ 20 | 16 | 19 |
| <abbr title="Carrier: Orange Pi Zero">XRadio XR819</abbr> | SDIO | 2437 MHz @ 20 | 5 | 17 |
| <abbr title="Carrier: Rock 5B Plus">Realtek RTL8723BU 802.11b/g/n</abbr> | USB | 2437 MHz @ 20 | 13 | 17 |
| <abbr title="Carrier: NanoPi R1">Broadcom (brcmfmac)</abbr> | SDIO | 2437 MHz @ 20 | 13 | 15 |
| <abbr title="Carrier: NanoPi Duo">XRadio XR819</abbr> | SDIO | 2437 MHz @ 20 | 1 | 14 |
| <abbr title="Carrier: Orange Pi Zero">MediaTek MT7601</abbr> | USB | 2437 MHz @ 20 | 12 | 13 |

<!-- DUT-STOP -->

## Test Equipment

All adapters connect to a single common **access point** — a [Zyxel NWA130BE (Wi-Fi 7)](https://amzn.to/428dvnH) — so throughput is comparable across every board. The boards under test and their radios are listed in the [results](#results) above.

## Software and Infrastructure

[NetBox](https://docs.armbian.com/software/netbox/) is the lab's source of truth — every board, its capabilities and its wiring. The Armbian autotests framework reads that inventory and drives each board over self-hosted GitHub Actions, power included via `armbian/infra`.

## Methodology

Wireless throughput is one step of the per-board Armbian autotests pipeline. For each board:

1. **Power on & flash** — the board is powered up and, where the hardware allows, flashed with a clean Armbian image; boards that can't take a clean flash are tested in place.
2. **Provision & connect** — first login, a stable lab IP, and the Wi-Fi association to the common access point (SSID) are configured, then connectivity is verified.
3. **Measure with iperf3** — the board runs `iperf3` as the client, source-bound to each interface, against the lab's central server in both directions: upload (board → server) and download (`-R`, server → board). Goodput is recorded in Mbit/s.
4. **Enrich from NetBox** — each result is annotated with the interface type, Wi-Fi chip, and channel frequency/width, so every number carries the hardware that produced it.
5. **Restore & power down** — the original wired configuration is restored, results are uploaded, and the board is powered off.

Results are published as a time series, so a regression shows up the moment throughput drops on a given board.

## Contribute

- Assist us in developing and maintaining our testing system: Your expertise can help us enhance and optimize our test infrastructure. By contributing your skills, you can play a key role in ensuring the accuracy and reliability of our test results.

- Donate hardware: Your contribution of new hardware, whether it’s a wireless adapter or any other equipment, helps us expand our testing capabilities. We’re specifically looking for [new wireless adapters](https://www.amazon.de/hz/wishlist/ls/1GA17IGQ2MF0V?ref_=wl_share) that haven’t yet been added to our system. Your donation can directly impact the scope and depth of our tests.

- Join our team: Become part of our passionate and dedicated team. We’re looking for [individuals who share our vision and are eager to contribute to the development of innovative testing solutions](https://forum.armbian.com/staffapplications/). Whether you have technical expertise or simply a willingness to learn, there’s a place for you here!

## Other resources

- [USB WiFi Adapter Information for Linux](https://github.com/morrownr/USB-WiFi)
- [Official Linux Wireless documentation](https://wireless.docs.kernel.org/en/latest/index.html)
- [Armbian forum - Advanced users - Development](https://forum.armbian.com/forum/4-advanced-users-development/)
