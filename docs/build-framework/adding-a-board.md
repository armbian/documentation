---
seo_title: "Armbian: add a new board or board family"
description: "How to add a new board or board family to the Armbian build framework: board config fields, status suffixes, family configs, and a worked example for ARM SBCs."
---

# Adding a new board or board family

Armbian describes hardware with two kinds of configuration file:

- a **board config** — one file per board, under [`config/boards/`](https://github.com/armbian/build/tree/main/config/boards), naming the board and pointing it at a family, a U-Boot config and a device tree;
- a **board family config** — one file per SoC family, under [`config/sources/families/`](https://github.com/armbian/build/tree/main/config/sources/families), holding everything shared by the boards of that family (kernel source, U-Boot branch, CPU limits, family tweaks).

A board config selects its family with `BOARDFAMILY`, and the build merges the two at run time. If your board belongs to an SoC family Armbian already supports, you usually only need a **new board config**. A genuinely new SoC needs a **new family** as well.

## Board config

Create `config/boards/<board>.<status>`. The file name without its extension is the `BOARD` identifier you pass to the build, e.g. `config/boards/bananapim5.conf` → `./compile.sh build BOARD=bananapim5`.

### Status suffix

The extension records the board's support status (shown at the login prompt and used by the board selector):

| Extension | Meaning |
|---|---|
| `.conf` | Standard support — an active maintainer ships stable images |
| `.csc` | Community-supported config — community creations or no active maintainer |
| `.tvb` | TV box — community-maintained, same tier as `.csc` |
| `.wip` | Work in progress — a maintainer has committed but images are not yet stable |
| `.eos` | End of service — no longer maintained |

New boards without a committed maintainer typically start as `.csc` (or `.wip` while bring-up is ongoing). See the [Board Support Rules](../User-Guide_Board-Support-Rules.md) for what each tier requires.

### Key fields

A minimal board config sets the identity, the family, and the boot/kernel pointers:

```bash
# Amlogic S905X3 quad core 2-4GB RAM SoC eMMC GBE USB3 SPI
BOARD_NAME="Banana Pi M5"          # "COMPANY PRODUCT VERSION"; used for hostname/welcome text
BOARD_VENDOR="sinovoip"
BOARDFAMILY="meson-sm1"            # the family file in config/sources/families/
BOARD_MAINTAINER="igorpecovnik"    # space-separated GitHub logins (empty for unmaintained)
INTRODUCED="2021"                  # year the board reached the market
BOOTCONFIG="bananapi-m5_defconfig" # U-Boot defconfig name (see the u-boot configs/ tree)
BOOT_FDT_FILE="amlogic/meson-sm1-bananapi-m5.dtb"  # device tree, relative to the dtb dir
KERNEL_TARGET="current,edge"       # which kernel branches to build (legacy/current/edge)
KERNEL_TEST_TARGET="current"       # subset built by CI / release automation
SERIALCON="ttyAML0"                # serial console device (optionally :baud)
```

Commonly-used extras include `HAS_VIDEO_OUTPUT`, `BOOT_LOGO`, `MODULES_BLACKLIST`, `DEFAULT_OVERLAYS`, `OVERLAY_PREFIX`, `IMAGE_PARTITION_TABLE`, `BOOTFS_TYPE`, `CPUMIN`/`CPUMAX`, and `PACKAGE_LIST_BOARD`. The board file can also define **hook functions** for board-specific steps — the Banana Pi M5 config, for example, fetches Amlogic FIP blobs and post-processes U-Boot via `fetch_sources_tools__…` and `post_uboot_custom_postprocess__…` hooks.

!!! tip "Full field reference"
    Every board option is documented in [Board configuration](board-configuration.md). If a field is unclear, grep the framework for it:
    ```bash
    grep -r -A5 -B5 "BOOT_FDT_FILE" lib/ config/
    ```

## Board family config

If the SoC family is new, add `config/sources/families/<family>.conf` (its name is what boards set as `BOARDFAMILY`). The family config carries what all its boards share:

- **Kernel source and branch** per `BRANCH` — `KERNELSOURCE`, `KERNELBRANCH`, `KERNEL_MAJOR_MINOR`, `KERNELPATCHDIR`, `LINUXCONFIG`.
- **U-Boot source and patch dir** — `BOOTBRANCH`, `BOOTPATCHDIR` (a board can override with `BOOTBRANCH_BOARD` / `BOOTPATCHDIR`).
- **Architecture and platform** — `ARCH`, and often a shared include via `source "${BASH_SOURCE%/*}/include/<soc>_common.inc"`.
- **CPU limits and governor** — `CPUMIN`, `CPUMAX`, `GOVERNOR`.
- **Hook functions** — e.g. `family_tweaks()`, `uboot_custom_postprocess()`, `write_uboot_platform()`.

The `BOARDFAMILY` → build-time family mapping is listed in [`config/sources/README.md`](https://github.com/armbian/build/blob/main/config/sources/README.md).

## Kernel and U-Boot patches

Board- and family-specific patches live under [`patch/kernel/`](https://github.com/armbian/build/tree/main/patch/kernel) and [`patch/u-boot/`](https://github.com/armbian/build/tree/main/patch/u-boot), in the directory named by the family's `KERNELPATCHDIR` / `BOOTPATCHDIR`. Kernel config fragments live in `config/kernel/linux-<family>-<branch>.config` (regenerate with `./compile.sh rewrite-kernel-config`).

## Test before you submit

Build and boot-test each kernel target you declared:

```bash
./compile.sh build BOARD=<board> BRANCH=current
```

Write the image to media, confirm it boots to a login prompt over serial and/or network, and check the peripherals the board is expected to support. Bring-up that isn't ready for stable images belongs in `.wip`.

## Submit

Open a pull request against [armbian/build](https://github.com/armbian/build) with the new config (and any patches). Set `BOARD_MAINTAINER` to your GitHub login if you intend to maintain it, and pick the [status suffix](#status-suffix) that matches your commitment. The [Board Support Rules](../User-Guide_Board-Support-Rules.md) describe the obligations of each tier.

## Further reading

Real pull requests that add boards/families are a good template for the exact set of files to touch:

- [https://github.com/armbian/build/pull/3176/files](https://github.com/armbian/build/pull/3176/files)
- [https://github.com/armbian/build/pull/3138/files](https://github.com/armbian/build/pull/3138/files)
- [https://github.com/armbian/build/pull/7902/files](https://github.com/armbian/build/pull/7902/files)
- [https://github.com/armbian/build/pull/8208/files](https://github.com/armbian/build/pull/8208/files)
