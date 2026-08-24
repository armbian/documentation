---
seo_title: "Armbian basic build commands: build, flash, kernel"
description: "Everyday Armbian build commands: build a full image or just the kernel with compile.sh, and flash it to an SD card, USB or eMMC."
---

# Basic commands

Everyday commands for building a full image or just the kernel, and writing it to media.

## build

The default command. Builds a full OS image (or only the requested artifacts, depending on the switches) for the selected board and release. This is what runs when you invoke `./compile.sh` with no command, or explicitly:

Usage:
```bash
./compile.sh build BOARD=uefi-x86 BRANCH=current RELEASE=trixie
```

## flash

Writes an already-built image to a block device (SD card, USB, eMMC). Name the
target device; the newest image in `output/images` is used unless you name one
too.

Usage:
```bash
./compile.sh flash CARD_DEVICE=/dev/sdX
```

`CARD_DEVICE` is mandatory &mdash; run `lsblk` to find the device name. Docker is
not an obstacle: the launcher passes the device into the container when it is
set (`DOCKER_SKIP_CARD_DEVICE=yes` opts out).

!!! danger "Check the device name first"

    Everything on `CARD_DEVICE` is overwritten. Naming the wrong disk destroys
    it.

Pass `BOARD`, `RELEASE` or `BRANCH` to narrow which image is picked, or `IMAGE`
to name a file outright:

```bash
./compile.sh flash CARD_DEVICE=/dev/sdX BOARD=rockpi-4a BRANCH=current
./compile.sh flash CARD_DEVICE=/dev/sdX IMAGE=output/images/Armbian_26.8.3_Rockpi-4a_trixie_current_6.12.13.img
```

When the image is picked for you, the choice is reported before anything is
written, so you can check it is the one you meant:

```text
[🌱] cli_flash [ No image file specified. Using latest built image file found: Armbian-unofficial_26.08.0-trunk_Bananapim2_resolute_current_6.18.46_minimal.img ]
[🌱] cli_flash [ Flashing image file: Armbian-unofficial_26.08.0-trunk_Bananapim2_resolute_current_6.18.46_minimal.img ]
```

The image is read back and verified against its checksum after writing. Set
`SKIP_VERIFY=yes` to skip that.

## kernel

Builds only the kernel and device tree (where applicable) and places the packages in `output/debs`.

Usage:
```bash
./compile.sh kernel BOARD=nanopi-r5c BRANCH=edge
```

## uboot

Builds only the U-Boot bootloader and places the package in `output/debs`.

Usage:
```bash
./compile.sh uboot BOARD=nanopi-r5c BRANCH=edge
```
