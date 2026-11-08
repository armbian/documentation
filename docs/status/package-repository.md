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

_Generated 2026-11-08 12:27 UTC from [`https://apt.armbian.com`](https://apt.armbian.com) — component `main`, architecture `arm64`._

### Suites

| Suite | Codename | Updated | Packages | Latest Armbian version |
|:------|:---------|:--------|--------:|----------------------:|
| `bookworm` | bookworm | Wed, 4 Nov 2026  | 2279 | `26.8.14` |
| `trixie` | trixie | Wed, 4 Nov 2026  | 2279 | `26.8.14` |
| `sid` | sid | Wed, 4 Nov 2026  | 2279 | `26.8.14` |
| `jammy` | jammy | Wed, 4 Nov 2026  | 2279 | `26.8.14` |
| `noble` | noble | Wed, 4 Nov 2026  | 2279 | `26.8.14` |

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

Newest kernel published per family, with its Linux kernel version. The current release line is `26.8.14`; families below it were not rebuilt for it.

**85 of 86 families behind `26.8.14`.** **2 with header mismatches.**

#### Current

| Kernel package | Kernel | Armbian version | Headers |
|:---------------|:-------|----------------:|:-------:|
| `linux-image-edge-arm64` | `7.3.1` | `26.8.14` | ✅ |

#### Behind `26.8.14`

| Kernel package | Kernel | Armbian version | Headers |
|:---------------|:-------|----------------:|:-------:|
| `linux-image-cloud-arm64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-current-arm64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-legacy-arm64` | `6.12.103` | `26.8.3` | ✅ |
| `linux-image-sc8280xp-arm64` | `7.0.10` | `26.5.1` | ✅ |
| `linux-image-sm8250-arm64` | `6.7.4` | `24.2.1` | ✅ |
| `linux-image-sm8550-arm64` | `6.9.3` | `25.2.3` | ✅ |
| `linux-image-wdk2023-arm64` | `6.7.0-rc6` | `25.5.1` | ✅ |
| `linux-image-current-bcm2711` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-bcm2711` | `7.2.7` | `26.8.8` | ✅ |
| `linux-image-legacy-bcm2711` | `6.12.103` | `26.8.3` | ✅ |
| `linux-image-current-bcm2712` | `6.6.63` | `24.11.1` | ✅ |
| `linux-image-edge-bcm2712` | `6.10.14` | `24.11.1` | ✅ |
| `linux-image-current-cix-p1` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-cix-p1` | `7.1.13` | `26.8.8` | ✅ |
| `linux-image-vendor-edge-k3` | `6.18.51` | `26.8.8` | ✅ |
| `linux-image-current-filogic` | `6.12.100` | `26.8.3` | ✅ |
| `linux-image-edge-filogic` | `6.16.12` | `26.8.8` | ✅ |
| `linux-image-collabora-genio` | `6.19.0-rc5` | `26.2.1` | ✅ |
| `linux-image-edge-genio` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-vendor-genio` | `5.15.168` | `25.2.3` | ✅ |
| `linux-image-current-imx8m` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-imx8m` | `7.1.13` | `26.8.8` | ✅ |
| `linux-image-vendor-imx8ulp` | `6.1.22` | `26.8.3` | ✅ |
| `linux-image-current-imx93` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-imx93` | `7.1.13` | `26.8.8` | ✅ |
| `linux-image-current-k3-beagle` | `6.12.49` | `25.8.2` | ✅ |
| `linux-image-edge-k3-beagle` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-vendor-k3-beagle` | `6.12.49` | `26.8.3` | ✅ |
| `linux-image-current-k3` | `6.12.17` | `25.8.2` | ✅ |
| `linux-image-edge-k3` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-edge-k3-tq` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-vendor-k3` | `6.18.13` | `26.8.3` | ✅ |
| `linux-image-current-ls1046a-ask` | `6.12.49` | `26.8.3` | ✅ |
| `linux-image-current-media` | `6.1.92` | `24.5.1` | ✅ |
| `linux-image-edge-media` | `6.2.16` | `24.5.1` | ✅ |
| `linux-image-legacy-media` | `5.10.110` | `24.5.1` | ✅ |
| `linux-image-legacy-meson-s4t7` | `5.15.137` | `26.8.3` | ✅ |
| `linux-image-current-meson64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-meson64` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-current-mvebu64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-mvebu64` | `7.1.13` | `26.8.8` | ✅ |
| `linux-image-vendor-nuvoton-ma35d1` | `5.10.140` | `26.8.3` | ✅ |
| `linux-image-current-phytium-embedded` | `6.6.12` | `26.8.3` | ✅ |
| `linux-image-legacy-phytium-embedded` | `5.10.209` | `26.8.3` | ✅ |
| `linux-image-current-qcs6490` | `6.18.2` | `26.8.3` | ✅ |
| `linux-image-edge-qcs6490` | `7.2.3` | `26.8.8` | ✅ |
| `linux-image-edge-qrb2210` | `7.2.3` | `26.8.8` | ✅ |
| `linux-image-vendor-realtek-rtd1619b` | `6.6.54` | `26.8.3` | ✅ |
| `linux-image-legacy-rk35xx` | `5.10.160` | `24.5.1` | ✅ |
| `linux-image-vendor-rk35xx` | `6.1.115` | `26.8.3` | ✅ |
| `linux-image-collabora-rockchip-rk3588` | `6.9.0` | `24.5.1` | ✅ |
| `linux-image-current-rockchip-rk3588` | `6.12.0` | `24.11.2` | ✅ |
| `linux-image-edge-rockchip-rk3588` | `6.12.1` | `24.11.1` | ✅ |
| `linux-image-bleedingedge-rockchip64` | `7.3.0-rc5` | `26.8.8` | ✅ |
| `linux-image-current-rockchip64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-rockchip64` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-legacy-rockpis` | `4.4.247` | `24.2.1` | ❌ missing |
| `linux-image-current-rt-k3-beagle` | `6.12.49` | `25.8.2` | ✅ |
| `linux-image-vendor-rt-k3-beagle` | `6.12.49` | `26.8.3` | ✅ |
| `linux-image-vendor-rt-k3` | `6.18.13` | `26.8.3` | ✅ |
| `linux-image-edge-s5p6818` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-edge-sc8280xp` | `7.2.3` | `26.8.8` | ✅ |
| `linux-image-sc8280xp-sc8280xp` | `7.0.14` | `26.8.3` | ✅ |
| `linux-image-vendor-sc8280xp` | `7.0.11` | `26.8.3` | ✅ |
| `linux-image-vendor-seeed-rk3576` | `6.1.115` | `26.8.3` | ✅ |
| `linux-image-vendor-seeed-rk3588` | `6.1.115` | `26.8.3` | ✅ |
| `linux-image-current-sm8250` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-sm8250` | `6.19.14` | `26.8.8` | ✅ |
| `linux-image-current-sm8550` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-sm8550` | `7.2.3` | `26.8.8` | ✅ |
| `linux-image-bleedingedge-sm8550-sheng` | `7.2.2` | `26.8.8` | ✅ |
| `linux-image-edge-sm8550-sheng` | `7.1.8` | `26.8.8` | ✅ |
| `linux-image-edge-sm8750` | `7.1.13` | `26.8.8` | ✅ |
| `linux-image-legacy-sun50iw9-btt` | `6.1.79` | `24.5.1` | ✅ |
| `linux-image-legacy-sun50iw9` | `4.9.318` | `24.5.1` | ❌ missing |
| `linux-image-dev-sun55iw3` | `6.14.0-rc1` | `25.5.1` | ✅ |
| `linux-image-edge-sun55iw3` | `6.16.0` | `25.11.2` | ✅ |
| `linux-image-legacy-sun55iw3-syterkit` | `5.15.154` | `26.8.3` | ✅ |
| `linux-image-vendor-sun60iw2` | `6.6.98` | `26.8.3` | ✅ |
| `linux-image-current-sunxi64` | `6.18.44` | `26.8.3` | ✅ |
| `linux-image-edge-sunxi64` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-legacy-sunxi64` | `6.12.103` | `26.8.3` | ✅ |
| `linux-image-edge-uefidt` | `7.2.8` | `26.8.8` | ✅ |
| `linux-image-current-wsl2-arm64` | `6.1.158` | `25.11.2` | ✅ |
| `linux-image-edge-wsl2-arm64` | `6.6.116` | `25.11.2` | ✅ |

### External packages

Third-party and source-built packages: see [external.armbian.com](https://external.armbian.com/).

<!-- apt-status:end -->
