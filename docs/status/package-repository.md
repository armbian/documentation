---
title: Package repository
seo_title: "Armbian apt repository status: package & kernel versions"
description: "Live status of apt.armbian.com — package and kernel versions per suite, which kernel families lag the current release, and where linux-headers are missing or mismatched."
---
# Package repository

This page tracks what [`apt.armbian.com`](https://apt.armbian.com) is serving:
the current Armbian version per suite, the kernel version each family ships,
which families have **drifted** behind the release, and where a
`linux-image` is missing its matching `linux-headers`.

<!-- apt-status:start -->
## Armbian apt repository status

_Generated 2026-09-05 09:39 UTC from [`https://apt.armbian.com`](https://apt.armbian.com) — component `main`, architecture `arm64`._

### Suites

| Suite | Codename | Updated | Packages | Latest Armbian version |
|:------|:---------|:--------|--------:|----------------------:|
| `bookworm` | bookworm | Fri, 4 Sep 2026  | 2267 | `26.8.3` |
| `trixie` | trixie | Fri, 4 Sep 2026  | 2267 | `26.8.3` |
| `sid` | sid | Fri, 4 Sep 2026  | 2267 | `26.8.3` |
| `jammy` | jammy | Fri, 4 Sep 2026  | 2267 | `26.8.3` |
| `noble` | noble | Fri, 4 Sep 2026  | 2267 | `26.8.3` |

### Core package versions

Armbian's own base packages (component `main`) — identical across all suites.

| Package | Version |
|:--------|--------:|
| `armbian-firmware` | `26.8.3` |
| `armbian-firmware-full` | `26.8.3` |
| `armbian-zsh` | `26.8.1` |
| `armbian-plymouth-theme` | `26.8.3` |

> ⚠️ **Header mismatch:** 2 kernel families have `linux-headers` missing or at a different version than `linux-image` — see the Kernel families table below.

### Kernel families

Newest kernel published per family, with its Linux kernel version. The current release line is `26.8.3`; families below it were not rebuilt for it.

**25 of 82 families behind `26.8.3`.** **2 with header mismatches.**

#### Current

| Kernel package | Kernel | Armbian version | Headers |
|:---------------|:-------|----------------:|:-------:|
| `linux-image-cloud-arm64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-current-arm64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-arm64` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-legacy-arm64` | `6.12.103` | `26.8.3` | ✅ |
| `linux-image-current-bcm2711` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-bcm2711` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-legacy-bcm2711` | `6.12.103` | `26.8.3` | ✅ |
| `linux-image-current-cix-p1` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-cix-p1` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-vendor-edge-k3` | `6.18.38` | `26.8.3` | ✅ |
| `linux-image-current-filogic` | `6.12.100` | `26.8.3` | ✅ |
| `linux-image-edge-genio` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-current-imx8m` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-imx8m` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-vendor-imx8ulp` | `6.1.22` | `26.8.3` | ✅ |
| `linux-image-current-imx93` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-imx93` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-edge-k3-beagle` | `7.2.0-rc7` | `26.8.3` | ✅ |
| `linux-image-vendor-k3-beagle` | `6.12.49` | `26.8.3` | ✅ |
| `linux-image-edge-k3` | `7.2.0-rc7` | `26.8.3` | ✅ |
| `linux-image-vendor-k3` | `6.18.13` | `26.8.3` | ✅ |
| `linux-image-current-ls1046a-ask` | `6.12.49` | `26.8.3` | ✅ |
| `linux-image-legacy-meson-s4t7` | `5.15.137` | `26.8.3` | ✅ |
| `linux-image-current-meson64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-meson64` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-current-mvebu64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-mvebu64` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-vendor-nuvoton-ma35d1` | `5.10.140` | `26.8.3` | ✅ |
| `linux-image-current-phytium-embedded` | `6.6.12` | `26.8.3` | ✅ |
| `linux-image-legacy-phytium-embedded` | `5.10.209` | `26.8.3` | ✅ |
| `linux-image-current-qcs6490` | `6.18.2` | `26.8.3` | ✅ |
| `linux-image-edge-qcs6490` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-edge-qrb2210` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-vendor-realtek-rtd1619b` | `6.6.54` | `26.8.3` | ✅ |
| `linux-image-vendor-rk35xx` | `6.1.115` | `26.8.3` | ✅ |
| `linux-image-current-rockchip64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-rockchip64` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-vendor-rt-k3-beagle` | `6.12.49` | `26.8.3` | ✅ |
| `linux-image-vendor-rt-k3` | `6.18.13` | `26.8.3` | ✅ |
| `linux-image-edge-sc8280xp` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-sc8280xp-sc8280xp` | `7.0.14` | `26.8.3` | ✅ |
| `linux-image-vendor-sc8280xp` | `7.0.11` | `26.8.3` | ✅ |
| `linux-image-vendor-seeed-rk3576` | `6.1.115` | `26.8.3` | ✅ |
| `linux-image-vendor-seeed-rk3588` | `6.1.115` | `26.8.3` | ✅ |
| `linux-image-current-sm8250` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-sm8250` | `6.19.14` | `26.8.3` | ✅ |
| `linux-image-current-sm8550` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-sm8550` | `7.0.14` | `26.8.3` | ✅ |
| `linux-image-bleedingedge-sm8550-sheng` | `7.2.0` | `26.8.3` | ✅ |
| `linux-image-edge-sm8550-sheng` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-edge-sm8750` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-legacy-sun55iw3-syterkit` | `5.15.154` | `26.8.3` | ✅ |
| `linux-image-vendor-sun60iw2` | `6.6.98` | `26.8.3` | ✅ |
| `linux-image-current-sunxi64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-sunxi64` | `7.1.8` | `26.8.3` | ✅ |
| `linux-image-legacy-sunxi64` | `6.12.103` | `26.8.3` | ✅ |
| `linux-image-edge-uefidt` | `7.1.8` | `26.8.3` | ✅ |

#### Behind `26.8.3`

| Kernel package | Kernel | Armbian version | Headers |
|:---------------|:-------|----------------:|:-------:|
| `linux-image-sc8280xp-arm64` | `7.0.10` | `26.5.1` | ✅ |
| `linux-image-sm8250-arm64` | `6.7.4` | `24.2.1` | ✅ |
| `linux-image-sm8550-arm64` | `6.9.3` | `25.2.3` | ✅ |
| `linux-image-wdk2023-arm64` | `6.7.0-rc6` | `25.5.1` | ✅ |
| `linux-image-current-bcm2712` | `6.6.63` | `24.11.1` | ✅ |
| `linux-image-edge-bcm2712` | `6.10.14` | `24.11.1` | ✅ |
| `linux-image-collabora-genio` | `6.19.0-rc5` | `26.2.1` | ✅ |
| `linux-image-vendor-genio` | `5.15.168` | `25.2.3` | ✅ |
| `linux-image-current-k3-beagle` | `6.12.49` | `25.8.2` | ✅ |
| `linux-image-current-k3` | `6.12.17` | `25.8.2` | ✅ |
| `linux-image-current-media` | `6.1.92` | `24.5.1` | ✅ |
| `linux-image-edge-media` | `6.2.16` | `24.5.1` | ✅ |
| `linux-image-legacy-media` | `5.10.110` | `24.5.1` | ✅ |
| `linux-image-legacy-rk35xx` | `5.10.160` | `24.5.1` | ✅ |
| `linux-image-collabora-rockchip-rk3588` | `6.9.0` | `24.5.1` | ✅ |
| `linux-image-current-rockchip-rk3588` | `6.12.0` | `24.11.2` | ✅ |
| `linux-image-edge-rockchip-rk3588` | `6.12.1` | `24.11.1` | ✅ |
| `linux-image-legacy-rockpis` | `4.4.247` | `24.2.1` | ❌ missing |
| `linux-image-current-rt-k3-beagle` | `6.12.49` | `25.8.2` | ✅ |
| `linux-image-legacy-sun50iw9-btt` | `6.1.79` | `24.5.1` | ✅ |
| `linux-image-legacy-sun50iw9` | `4.9.318` | `24.5.1` | ❌ missing |
| `linux-image-dev-sun55iw3` | `6.14.0-rc1` | `25.5.1` | ✅ |
| `linux-image-edge-sun55iw3` | `6.16.0` | `25.11.2` | ✅ |
| `linux-image-current-wsl2-arm64` | `6.1.158` | `25.11.2` | ✅ |
| `linux-image-edge-wsl2-arm64` | `6.6.116` | `25.11.2` | ✅ |

### Third-party & utility packages

Upstream tools imported per suite (component `<suite>-utils`); split families (JDK, OpenZFS, ...) are folded to their newest member, and `-dbgsym` debug packages omitted.

| Package | `bookworm` | `trixie` | `sid` | `jammy` | `noble` |
|:--------|:-:|:-:|:-:|:-:|:-:|
| `anubis` | `1.25.0` | `1.25.0` | `1.24.0` | `1.25.0` | `1.25.0` |
| `aptly` | — | — | — | `1.6.2-2` | — |
| `armbian-imager` | — | `1.2.1` | — | — | — |
| `base-files` | `26.8.3-12.4+deb12u15-bookworm` | `26.8.3-13.8+deb13u6-trixie` | `26.8.3-14.2-sid` | `26.8.3-12ubuntu4.7-jammy` | `26.8.3-13ubuntu10-noble` |
| `bluez` | `5.66-1+rpt1+deb12u2` | `5.66-1+rpt1+deb12u2` | `5.66-1+rpt1+deb12u2` | — | — |
| `bluez-firmware` | `1.2-9+rpt4` | `1.2-9+rpt4` | `1.2-9+rpt4` | — | — |
| `edl-ng` | `1.5.0` | `1.5.0` | `1.5.0` | `1.5.0` | `1.5.0` |
| `fastfetch` | `2.67.1` | `2.67.1` | — | `2.67.1` | `2.67.1` |
| `firmware-brcm80211` | `1:20240709-2~bpo12+1+rpt3` | `1:20240709-2~bpo12+1+rpt3` | `1:20240709-2~bpo12+1+rpt3` | — | — |
| `gh` | `2.99.0` | `2.99.0` | `2.83.2` | `2.99.0` | `2.99.0` |
| `hello` | `1.0` | `1.0` | `1.0` | `1.0` | `1.0` |
| `homeassistant-supervised` | `3.0.0` | `3.0.0` | — | — | — |
| `libcamera` | `0.5.2+rpt20250903-1~bpo12+1` | `0.5.2+rpt20250903-1~bpo12+1` | — | `0.2.0-3fakesync1build6` | — |
| `libcec6` | — | — | — | `6.0.2-2` | — |
| `libraspberrypi` | `1:2+git20231018~131943+3c97f76-1` | `1:2+git20231018~131943+3c97f76-1` | `0~20230913+gitcc1ca18-0ubuntu2` | `0~20230913+gitcc1ca18-0ubuntu2` | `0~20230913+gitcc1ca18-0ubuntu2` |
| `linux-firmware-raspi` | — | — | — | — | `12-0ubuntu1` |
| `min` | `1.35.7` | `1.35.7` | `1.35.2` | `1.35.7` | `1.35.7` |
| `mkbootimg` | — | `1:34.0.5-12` | — | — | `1:34.0.5-12~bpo12+1` |
| `os-agent` | `1.7.2` | `1.7.2` | — | `1.7.2` | `1.7.2` |
| `pacstall` | `5.2.1-pacstall1` | `5.2.1-pacstall1` | `5.2.1-pacstall1` | — | `5.2.1-pacstall1` |
| `pi-bluetooth` | `0.1.20` | `0.1.20` | `0.1.20` | — | `0.2ubuntu1` |
| `raspberrypi-sys-mods` | `20250930~bookworm` | `20250930~bookworm` | `20250930~bookworm` | — | — |
| `raspi-config` | `20221214-0ubuntu1` | `20221214-0ubuntu1` | `20221214-0ubuntu1` | `20221214-0ubuntu1` | `20221214-0ubuntu1` |
| `raspi-firmware` | `1:1.20250915-1~bookworm` | `1:1.20250915-1~bookworm` | `1:1.20250915-1~bookworm` | — | — |
| `raspi-gpio` | `0.20231127` | `0.20231127` | `0.20231127` | — | — |
| `raspi-utils` | `20250826-1~bookworm` | `20250826-1~bookworm` | `20250826-1~bookworm` | — | — |
| `rpi-eeprom` | `20.4-1ubuntu2` | `20.4-1ubuntu2` | `20.4-1ubuntu2` | `20.4-1ubuntu2` | `20.4-1ubuntu2` |
| `spice-vdagent` | — | `0.22.1-3+b2` | — | — | — |
| `system-monitoring-center` | `2.26.0` | — | `2.26.0` | `2.26.0` | `2.26.0` |
| `unudhcpd` | `0.2.1-1+git230327.73ff39a` | `0.2.1-1+git230327.73ff39a` | `0.2.1-1+git230327.73ff39a` | `0.2.1-1+git230327.73ff39a` | `0.2.1-1+git230327.73ff39a` |
| zfs (OpenZFS) | `2.4.1-1` | `2.4.4-1` | — | `2.4.4-1arter97~ubuntu22.04.1` | `2.4.4-1arter97~ubuntu24.04.1` |
| zulu21 (JDK) | `21.0.12.1-1` | — | — | — | — |

<!-- apt-status:end -->
