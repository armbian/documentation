---
title: Package repository
seo_title: "Armbian apt repository status: package & kernel versions"
description: "Live status of apt.armbian.com — package and kernel versions per suite, which kernel families lag the current release, and where linux-headers are missing or mismatched."
---
# Package repository status

This page tracks what [`apt.armbian.com`](https://apt.armbian.com) is serving:
the current Armbian version per suite, the kernel version each family ships,
which families have **drifted** behind the release, and where a
`linux-image` is missing its matching `linux-headers`.

!!! info "Auto-generated"

    The table below is regenerated daily by
    [`apt-repo-status.py`](https://github.com/armbian/documentation/blob/main/tools/apt-repo-status.py)
    from the repository indices. Run it locally with
    `tools/apt-repo-status.py --kernels` to reproduce.

<!-- apt-status:start -->
## Armbian apt repository status

_Generated 2026-08-27 19:34 UTC from [`https://apt.armbian.com`](https://apt.armbian.com) — component `main`, architecture `arm64`._

### Suites

| Suite | Codename | Updated | Packages | Latest Armbian version |
|:------|:---------|:--------|--------:|----------------------:|
| `bookworm` | bookworm | Thu, 27 Aug 2026 | 2267 | `26.8.3` |
| `trixie` | trixie | Thu, 27 Aug 2026 | 2267 | `26.8.3` |
| `sid` | sid | Thu, 27 Aug 2026 | 2267 | `26.8.3` |
| `jammy` | jammy | Thu, 27 Aug 2026 | 2267 | `26.8.3` |
| `noble` | noble | Thu, 27 Aug 2026 | 2267 | `26.8.3` |

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

| Family and branch | Kernel | Armbian version | Headers |
|:------------------|:-------|----------------:|:--------|
| `arm64-cloud` | `6.18.44` | `26.8.3` | ✅ |
| `arm64-current` | `6.18.44` | `26.8.3` | ✅ |
| `arm64-edge` | `7.1.8` | `26.8.3` | ✅ |
| `arm64-legacy` | `6.12.103` | `26.8.3` | ✅ |
| `bcm2711-current` | `6.18.44` | `26.8.3` | ✅ |
| `bcm2711-edge` | `7.1.8` | `26.8.3` | ✅ |
| `bcm2711-legacy` | `6.12.103` | `26.8.3` | ✅ |
| `cix-p1-current` | `6.18.44` | `26.8.3` | ✅ |
| `cix-p1-edge` | `7.1.8` | `26.8.3` | ✅ |
| `edge-k3-vendor` | `6.18.38` | `26.8.3` | ✅ |
| `filogic-current` | `6.12.100` | `26.8.3` | ✅ |
| `genio-edge` | `7.1.8` | `26.8.3` | ✅ |
| `imx8m-current` | `6.18.44` | `26.8.3` | ✅ |
| `imx8m-edge` | `7.1.8` | `26.8.3` | ✅ |
| `imx8ulp-vendor` | `6.1.22` | `26.8.3` | ✅ |
| `imx93-current` | `6.18.44` | `26.8.3` | ✅ |
| `imx93-edge` | `7.1.8` | `26.8.3` | ✅ |
| `k3-beagle-edge` | `7.2.0-rc7` | `26.8.3` | ✅ |
| `k3-beagle-vendor` | `6.12.49` | `26.8.3` | ✅ |
| `k3-edge` | `7.2.0-rc7` | `26.8.3` | ✅ |
| `k3-vendor` | `6.18.13` | `26.8.3` | ✅ |
| `ls1046a-ask-current` | `6.12.49` | `26.8.3` | ✅ |
| `meson-s4t7-legacy` | `5.15.137` | `26.8.3` | ✅ |
| `meson64-current` | `6.18.44` | `26.8.3` | ✅ |
| `meson64-edge` | `7.1.8` | `26.8.3` | ✅ |
| `mvebu64-current` | `6.18.44` | `26.8.3` | ✅ |
| `mvebu64-edge` | `7.1.8` | `26.8.3` | ✅ |
| `nuvoton-ma35d1-vendor` | `5.10.140` | `26.8.3` | ✅ |
| `phytium-embedded-current` | `6.6.12` | `26.8.3` | ✅ |
| `phytium-embedded-legacy` | `5.10.209` | `26.8.3` | ✅ |
| `qcs6490-current` | `6.18.2` | `26.8.3` | ✅ |
| `qcs6490-edge` | `7.1.8` | `26.8.3` | ✅ |
| `qrb2210-edge` | `7.1.8` | `26.8.3` | ✅ |
| `realtek-rtd1619b-vendor` | `6.6.54` | `26.8.3` | ✅ |
| `rk35xx-vendor` | `6.1.115` | `26.8.3` | ✅ |
| `rockchip64-current` | `6.18.44` | `26.8.3` | ✅ |
| `rockchip64-edge` | `7.1.8` | `26.8.3` | ✅ |
| `rt-k3-beagle-vendor` | `6.12.49` | `26.8.3` | ✅ |
| `rt-k3-vendor` | `6.18.13` | `26.8.3` | ✅ |
| `sc8280xp-edge` | `7.1.8` | `26.8.3` | ✅ |
| `sc8280xp-sc8280xp` | `7.0.14` | `26.8.3` | ✅ |
| `sc8280xp-vendor` | `7.0.11` | `26.8.3` | ✅ |
| `seeed-rk3576-vendor` | `6.1.115` | `26.8.3` | ✅ |
| `seeed-rk3588-vendor` | `6.1.115` | `26.8.3` | ✅ |
| `sm8250-current` | `6.18.44` | `26.8.3` | ✅ |
| `sm8250-edge` | `6.19.14` | `26.8.3` | ✅ |
| `sm8550-current` | `6.18.44` | `26.8.3` | ✅ |
| `sm8550-edge` | `7.0.14` | `26.8.3` | ✅ |
| `sm8550-sheng-bleedingedge` | `7.2.0` | `26.8.3` | ✅ |
| `sm8550-sheng-edge` | `7.1.8` | `26.8.3` | ✅ |
| `sm8750-edge` | `7.1.8` | `26.8.3` | ✅ |
| `sun55iw3-syterkit-legacy` | `5.15.154` | `26.8.3` | ✅ |
| `sun60iw2-vendor` | `6.6.98` | `26.8.3` | ✅ |
| `sunxi64-current` | `6.18.44` | `26.8.3` | ✅ |
| `sunxi64-edge` | `7.1.8` | `26.8.3` | ✅ |
| `sunxi64-legacy` | `6.12.103` | `26.8.3` | ✅ |
| `uefidt-edge` | `7.1.8` | `26.8.3` | ✅ |

#### Behind `26.8.3`

| Family and branch | Kernel | Armbian version | Headers |
|:------------------|:-------|----------------:|:--------|
| `arm64-sc8280xp` | `7.0.10` | `26.5.1` | ✅ |
| `arm64-sm8250` | `6.7.4` | `24.2.1` | ✅ |
| `arm64-sm8550` | `6.9.3` | `25.2.3` | ✅ |
| `arm64-wdk2023` | `6.7.0-rc6` | `25.5.1` | ✅ |
| `bcm2712-current` | `6.6.63` | `24.11.1` | ✅ |
| `bcm2712-edge` | `6.10.14` | `24.11.1` | ✅ |
| `genio-collabora` | `6.19.0-rc5` | `26.2.1` | ✅ |
| `genio-vendor` | `5.15.168` | `25.2.3` | ✅ |
| `k3-beagle-current` | `6.12.49` | `25.8.2` | ✅ |
| `k3-current` | `6.12.17` | `25.8.2` | ✅ |
| `media-current` | `6.1.92` | `24.5.1` | ✅ |
| `media-edge` | `6.2.16` | `24.5.1` | ✅ |
| `media-legacy` | `5.10.110` | `24.5.1` | ✅ |
| `rk35xx-legacy` | `5.10.160` | `24.5.1` | ✅ |
| `rockchip-rk3588-collabora` | `6.9.0` | `24.5.1` | ✅ |
| `rockchip-rk3588-current` | `6.12.0` | `24.11.2` | ✅ |
| `rockchip-rk3588-edge` | `6.12.1` | `24.11.1` | ✅ |
| `rockpis-legacy` | `4.4.247` | `24.2.1` | ❌ missing |
| `rt-k3-beagle-current` | `6.12.49` | `25.8.2` | ✅ |
| `sun50iw9-btt-legacy` | `6.1.79` | `24.5.1` | ✅ |
| `sun50iw9-legacy` | `4.9.318` | `24.5.1` | ❌ missing |
| `sun55iw3-dev` | `6.14.0-rc1` | `25.5.1` | ✅ |
| `sun55iw3-edge` | `6.16.0` | `25.11.2` | ✅ |
| `wsl2-arm64-current` | `6.1.158` | `25.11.2` | ✅ |
| `wsl2-arm64-edge` | `6.6.116` | `25.11.2` | ✅ |

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
| `gh` | `2.98.0` | `2.98.0` | `2.83.2` | `2.98.0` | `2.98.0` |
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
| zfs (OpenZFS) | `2.4.1-1` | `2.4.3-3` | — | `2.4.4-1arter97~ubuntu22.04.1` | `2.4.4-1arter97~ubuntu24.04.1` |
| zulu21 (JDK) | `21.0.12.1-1` | — | — | — | — |

<!-- apt-status:end -->
