---
comments: true
---
# Testing the speed of wireless adapters

All wireless adapters were tested under consistent conditions - each positioned in close proximity (1-2m) and connected to the same wireless access point (AP). The adapters utilized various interface types, including USB, SDIO, and PCI, to evaluate performance across different hardware configurations.

<br>
[![Support Autotests](/images/support-autotest.png)](#contribute)

## Test Equipment

- **Access Point**: [Zyxel NWA130BE (Wi-Fi 7)](https://amzn.to/428dvnH)
- **Network Switches**: 
  - Netgear XS712T (10Gb)
  - Netgear XS508M (10Gb)
  - TP Link SG3218XP-M2 (2.5Gb PoE)
- **Power Switches**: APC AP7920  
- **Client Devices**:
  - Multiple single-board computers equipped with onboard wireless modules or PCI Wi-Fi cards

## Software and Infrastructure

- **Inventory & source of truth**: [NetBox](https://docs.armbian.com/User-Guide_Armbian-Software/Management/#netbox) holds every board in the lab, its status, and its capabilities. A scan-daemon continuously discovers boards on the lab subnets (nmap / arp / ssh) and reconciles NetBox.
- **Orchestration**: the [Armbian autotests framework](https://github.com/armbian/autotests) reads each board's capabilities from NetBox and runs a per-board pipeline — flashing a clean image where the hardware allows, otherwise testing upgrade / reboot / performance — including the WiFi throughput measurement.
- **Power control**: dispatched to the [`armbian/infra`](https://github.com/armbian/infra) backends (APC PDU, TP-Link PoE, DUT relay); no power port is ever switched by hand during a run.
- **Automation**: [GitHub Actions](https://github.com/armbian/autotests/blob/master/.github/workflows/test-fleet-iperf.yml) orchestrate the fleet runs and test execution.
- **Results**: published as a **time series** to [armbian.github.io](https://github.com/armbian/armbian.github.io) so regressions stay visible over time.

## Methodology

**Overview of the WiFi performance test process:**

1. **Power On Devices**  
   └─ Embedded WiFi-capable devices and USB wireless adapters are powered on.

2. **Configure Wireless Connection**  
   └─ Devices are configured to connect to a predefined access point (SSID).

3. **Connect to WiFi Network**  
   └─ Network connectivity is validated to ensure the device is routable.

4. **Measure Performance (iperf3)**  
   ├─ Perform reverse (`-R`) and forward iperf3 tests  
   └─ Measure throughput and link quality.

5. **Collect System & Network Info**  
   ├─ Extract link details (e.g. bitrate, signal strength)  
   └─ Record system version, kernel, architecture.

6. **Restore Wired Network**  
   └─ Reapply original routes and configuration.

7. **Upload Test Results**  
   └─ Summary, logs, and system info are uploaded as artifacts.

8. **Power Off Devices**  
   └─ All test devices are safely powered down after testing completes.

<!-- DUT-START -->

## WiFi performance

_Measured 2026-07-01 11:47 UTC_

**48** wireless link(s) · ✅ **48** pass · 📶 peak ↑ **681** / ↓ **868** Mbps

#### IEEE 802.11ac

| Board | Status | Attach | Chip | Channel | ↑ Up (Mbps) | ↓ Down (Mbps) |
|:--|:--:|:--|:--|:--|--:|--:|
| Banana Pi CM4IO | ✅ | SDIO | Realtek RTL8822CS | 2437 MHz @ 20 | 15 | 28 |
| Banana Pi CM4IO | ✅ | USB | Realtek RTL8821CU | 2437 MHz @ 20 | 45 | 36 |
| Banana Pi M2Pro | ✅ | USB | Realtek RTL8821CU | 2437 MHz @ 20 | 28 | 43 |
| BananaPi BPI-F3 | ✅ | USB | Realtek RTL8822BU | 5240 MHz @ 80 | 265 | 132 |
| Helios4 | ✅ | USB | Realtek RTL8821CU | 5240 MHz @ 80 | 259 | 241 |
| Khadas VIM1 | ✅ | SDIO | Broadcom (brcmfmac) | 5240 MHz @ 40 | 6 | 22 |
| Khadas VIM2 | ✅ | SDIO | Broadcom (brcmfmac) | 5240 MHz @ 40 | 105 | 97 |
| Khadas VIM3 | ✅ | SDIO | Broadcom (brcmfmac) | 5240 MHz @ 80 | 39 | 42 |
| NanoPi M4V2 | ✅ | SDIO | Broadcom BCM4356 | 5240 MHz @ 40 | 122 | 209 |
| NanoPi M4V2 | ✅ | USB | MediaTek MT7610 | 5240 MHz @ 80 | 131 | 245 |
| NanoPi M5 | ✅ | SDIO | Realtek RTL8822CS | 5240 MHz @ 80 | 44 | 88 |
| Orange Pi 3 | ✅ | SDIO | Broadcom (brcmfmac) | 5240 MHz @ 80 | 19 | 108 |
| Orange Pi Lite 2 | ✅ | SDIO | Broadcom (brcmfmac) | 2437 MHz @ 20 | 29 | 37 |
| Orange Pi Zero2 | ✅ | — | Unisoc UWE5622 | — | 132 | 93 |
| OrangePi 3 LTS | ✅ | — | Unisoc (unisoc_wifi) | — | 44 | 22 |
| Pine H64 | ✅ | USB | Realtek RTL8812AU | 5240 MHz @ 80 | 200 | 271 |
| Raspberry Pi | ✅ | SDIO | Broadcom (brcmfmac) | 5240 MHz @ 80 | 247 | 182 |
| Tanix TX6 | ✅ | SDIO | Realtek RTL8822CS | 5240 MHz @ 80 | 119 | 103 |
| UEFI x86 | ✅ | SDIO | Broadcom (brcmfmac) | 5240 MHz @ 40 | 25 | 22 |

#### IEEE 802.11ax

| Board | Status | Attach | Chip | Channel | ↑ Up (Mbps) | ↓ Down (Mbps) |
|:--|:--:|:--|:--|:--|--:|--:|
| BananaPi BPI-F3 | ✅ | SDIO | Realtek RTL8852BS | 5240 MHz @ 80 | 352 | 394 |
| Orange Pi 5 Plus | ✅ | USB | MediaTek MT7921 | 5240 MHz @ 80 | 646 | 350 |
| Rock 5B | ✅ | PCIe | Realtek RTL8852BE | 5240 MHz @ 80 | 199 | 609 |
| Rock 5T | ✅ | PCIe | Realtek RTL8852BE | 5240 MHz @ 80 | 348 | 450 |
| Tinker Board 2 | ✅ | PCIe | Realtek RTL8852AE | 5240 MHz @ 80 | 332 | 416 |

#### IEEE 802.11be

| Board | Status | Attach | Chip | Channel | ↑ Up (Mbps) | ↓ Down (Mbps) |
|:--|:--:|:--|:--|:--|--:|--:|
| Orange Pi 5 Plus | ✅ | PCIe | Qualcomm WCN7851 | 5240 MHz @ 160 | 232 | 784 |
| Rock 5B Plus | ✅ | PCIe | MediaTek MT7925 | 6215 MHz @ 160 | 681 | 868 |

#### IEEE 802.11n

| Board | Status | Attach | Chip | Channel | ↑ Up (Mbps) | ↓ Down (Mbps) |
|:--|:--:|:--|:--|:--|--:|--:|
| Banana Pi M2 Ultra | ✅ | SDIO | Broadcom (brcmfmac) | 2437 MHz @ 20 | 33 | 44 |
| Banana Pi M5 | ✅ | USB | Realtek RTL8192CU | 2437 MHz @ 20 | 37 | 27 |
| Banana Pi Pro | ✅ | SDIO | Broadcom (brcmfmac) | 2437 MHz @ 20 | 16 | 19 |
| Cubietruck | ✅ | SDIO | Broadcom (brcmfmac) | 2437 MHz @ 20 | 14 | 21 |
| Cubox i2eX/i4 | ✅ | SDIO | Broadcom (brcmfmac) | 2437 MHz @ 20 | 21 | 22 |
| Inovato Quadra | ✅ | SDIO | XRadio XR819 | 2437 MHz @ 20 | 12 | 23 |
| NanoPi Duo | ✅ | SDIO | XRadio XR819 | 2437 MHz @ 20 | 1 | 14 |
| NanoPi K2 | ✅ | SDIO | Broadcom (brcmfmac) | 2437 MHz @ 20 | 15 | 22 |
| NanoPi R1 | ✅ | SDIO | Broadcom (brcmfmac) | 2437 MHz @ 20 | 13 | 15 |
| NanoPi R4S | ✅ | USB | Ralink RT5370 | 2437 MHz @ 20 | 40 | 25 |
| Odroid C4 | ✅ | USB | Ralink RT5572 | 5240 MHz @ 40 | 56 | 93 |
| Orange Pi R1 | ✅ | SDIO | Realtek RTL8189ES | — | 26 | 25 |
| Orange Pi R1 | ✅ | SDIO | Realtek RTL8189ES | — | 29 | 29 |
| Orange Pi Zero | ✅ | SDIO | XRadio XR819 | 2437 MHz @ 20 | 5 | 17 |
| Orange Pi Zero | ✅ | USB | MediaTek MT7601 | 2437 MHz @ 20 | 12 | 13 |
| Orange Pi Zero Plus | ✅ | SDIO | Realtek RTL8189FS | — | 33 | 27 |
| Orange Pi Zero Plus | ✅ | SDIO | Realtek RTL8189FS | — | 35 | 26 |
| Raspberry Pi | ✅ | SDIO | Broadcom (brcmfmac) | 2437 MHz @ 20 | 17 | 24 |
| Rock 5B Plus | ✅ | USB | Realtek RTL8723BU 802.11b/g/n | 2437 MHz @ 20 | 13 | 17 |
| Rock 5T | ✅ | USB | Ralink RT5572 | 5240 MHz @ 40 | 53 | 73 |
| Tanix TX6 | ✅ | USB | Ralink RT2870/RT3070 | 2437 MHz @ 20 | 28 | 10 |
| Udoo | ✅ | USB | Ralink RT5370 | 2437 MHz @ 20 | 34 | 18 |

<!-- DUT-STOP -->

## Contribute

- Assist us in developing and maintaining our testing system: Your expertise can help us enhance and optimize [our test infrastructure](https://github.com/armbian/autotests). By contributing your skills, you can play a key role in ensuring the accuracy and reliability of our test results.

- Donate hardware: Your contribution of new hardware, whether it’s a wireless adapter or any other equipment, helps us expand our testing capabilities. We’re specifically looking for [new wireless adapters](https://www.amazon.de/hz/wishlist/ls/1GA17IGQ2MF0V?ref_=wl_share) that haven’t yet been added to our system. Your donation can directly impact the scope and depth of our tests.

- Join our team: Become part of our passionate and dedicated team. We’re looking for [individuals who share our vision and are eager to contribute to the development of innovative testing solutions](https://forum.armbian.com/staffapplications/). Whether you have technical expertise or simply a willingness to learn, there’s a place for you here!

## Other resources

- [USB WiFi Adapter Information for Linux](https://github.com/morrownr/USB-WiFi)
- [Official Linux Wireless documentation](https://wireless.docs.kernel.org/en/latest/index.html)
- [Armbian forum - Advanced users - Development](https://forum.armbian.com/forum/4-advanced-users-development/)
