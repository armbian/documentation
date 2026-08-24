---
seo_title: "Armbian basic build commands: build, kernel, uboot"
description: "Everyday Armbian build commands: build a full image, or just the kernel or U-Boot bootloader, with compile.sh."
---

# Basic commands

Everyday commands for building a full image, or just the kernel or U-Boot bootloader.

## build

The default command. Builds a full OS image (or only the requested artifacts, depending on the switches) for the selected board and release. This is what runs when you invoke `./compile.sh` with no command, or explicitly:

Usage:
```bash
./compile.sh build BOARD=uefi-x86 BRANCH=current RELEASE=trixie
```

## kernel

Builds only the kernel and device tree (where applicable) and places the packages in `output/debs`.

Usage:
```bash
./compile.sh kernel BOARD=nanopi-r5c BRANCH=edge
```

## kernel-config

Automatically call kernel's `make menuconfig` (add or remove modules or features)

Usage:
```bash
./compile.sh kernel-config BOARD=nanopi-r5c BRANCH=edge
```

## uboot

Builds only the U-Boot bootloader and places the package in `output/debs`.

Usage:
```bash
./compile.sh uboot BOARD=nanopi-r5c BRANCH=edge
```
