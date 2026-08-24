---
seo_title: "Armbian board configuration variables"
description: "Reference of every variable in an Armbian board .conf file: BOARD_NAME, BOARDFAMILY, BOOTCONFIG, KERNEL_TARGET, kernel modules, filesystems and more."
---

# Board configuration

Every board Armbian supports is described by a configuration file in
[`config/boards/<board>.conf`](https://github.com/armbian/build/tree/main/config/boards)
(or `.csc` / `.wip` / `.eos` depending on [support status](#support-status)). These
variables declare the board name, family, bootloader, kernel targets and other
build-time settings the framework applies when building that board. This page is
the reference for all of them; to add a whole new board, start with
[Adding a Board](/build-framework/adding-a-board/).

!!! tip

    If a variable is unclear, grep the source for context:
    `grep -r -A5 -B5 "BUILD_OPTION_HERE" /path/to/armbian/build`

## Build options

- **BOARD_NAME** ( `company product version` ): board name used in the welcome text, hostname and other places. The convention is `COMPANY PRODUCT VERSION`; it is often used in scripting logic, so follow the name declared in the board configuration.
    - Example: `OLIMEX Teres A64`
- **BOARDFAMILY** ( `board-family` ): family of the board, used to apply family-specific configuration at build time (temperature, LED behaviour, etc.).
    - Refer to the [sources table](https://github.com/armbian/build/blob/main/config/sources/README.md).
    - Example: `sun50iw1`
- **BOARD_MAINTAINER** ( space-separated list of GitHub logins ): the board's maintainer(s).
- **INTRODUCED** ( `year` ): when the board first came to market.
    - Example: `2022`
- **BOOTCONFIG** ( u-boot identifier ): name of the u-boot configuration for the build, without the `_defconfig` suffix.
    - Refer to the [u-boot source tree](https://github.com/u-boot/u-boot/tree/master/configs) to find the configuration for the board.
    - Example: `teres-i`
- **BOOTSIZE** ( int ): size of the boot partition in MiB.
    - Default: `256`
- **BOOT_LOGO** ( `string` ): whether to show an eyecandy splash during the bootloader phase.
    - `yes`: show the Armbian boot logo
    - `desktop`: show the Armbian boot logo when `BUILD_DESKTOP=yes`
    - Default: not set
- **CRUSTCONFIG** ( crust identifier ): name of the crust defconfig for the build. Specify only if the board has an Allwinner CPU with an AR100 coprocessor and the SoC is supported by [crust firmware](https://github.com/crust-firmware/crust).
    - Refer to the [crust source tree](https://github.com/crust-firmware/crust/tree/master/configs).
    - Example: `nanopi_m1_defconfig`
- **IMAGE_PARTITION_TABLE** ( `string` ): disklabel type.
    - `msdos`: use a dos/msdos disklabel
    - `gpt`: use a GPT disklabel
    - Default: `msdos`
- **BOOTFS_TYPE** ( filesystem ): filesystem for the boot partition.
    - `none`: keep `/boot` on the root filesystem
    - `ext4`: [Fourth Extended Filesystem](https://en.wikipedia.org/wiki/Ext4)
    - `ext2`: [Second Extended Filesystem](https://en.wikipedia.org/wiki/Ext2)
    - `fat`: [FAT32](https://en.wikipedia.org/wiki/File_Allocation_Table#FAT32)
    - Default: `ext4`
- **DEFAULT_OVERLAYS** ( space-separated list of dtb overlays ): device-tree overlays enabled by default. Each family has a basic dtb, but boards use different SoC features (e.g. one board exposes four USB ports, another does not), so overlays are enabled per board.
    - Examples: `usbhost0`, `usbhost2`, `usbhost3`, `cir`, `analog-codec`, `gpio-regulator-1.3v`, `uart1`
- **DEFAULT_CONSOLE** ( `string` ): default console for boot output.
    - `serial`: output boot messages to the serial console
    - Default: not set
- **MODULES** ( space-separated list of kernel modules ): modules appended to the kernel command line for **all** kernel branches.
- **MODULES_LEGACY** / **MODULES_CURRENT** / **MODULES_EDGE**: as above, for the **legacy** / **current** / **edge** kernel respectively.
- **MODULES_BLACKLIST** ( space-separated list of kernel modules ): modules added to the kernel's blacklist/deny list for **all** kernel branches.
- **MODULES_BLACKLIST_LEGACY** / **MODULES_BLACKLIST_CURRENT** / **MODULES_BLACKLIST_EDGE**: as above, for the **legacy** / **current** / **edge** kernel respectively.
- **SERIALCON** ( comma-separated list of terminal interfaces `[:bandwidth]` ): which serial console(s) the system should use.
    - Example: `ttyS0:15000000,ttyGS1`
- **SKIP_ARMBIAN_REPO** ( boolean ): whether to exclude the Armbian repository from the built image.
    - `yes`: exclude the Armbian repo (`armbian.sources` stays `.disabled`)
    - `no`: include the Armbian repo (default)
- **POWER_MANAGEMENT_FEATURES** ( boolean ): whether system sleep (suspend, hibernate, hybrid sleep) is allowed on the built image.
    - `yes`: enable systemd sleep modes
    - `no` (default): disable all sleep modes — suspend/hibernate are unstable on most single-board computers
- **HAS_VIDEO_OUTPUT** ( boolean ): whether the board has video output (splash, eyecandy, etc.).
    - `yes`: enable video-related configuration
    - `no`: disable video-related configuration
- **KERNEL_TARGET** ( comma-separated list of kernel releases or branches ): which kernels are built for the board.
    - `legacy` / `current` / `edge`: use that kernel
    - `[branch]`: use the specified branch kernel
    - none: exits with an error
- **KERNEL_TEST_TARGET** ( comma-separated list of kernel releases or branches ): test targets when they differ from the build targets; also applies to build-list generation. (internal switch)
- **FULL_DESKTOP** ( boolean ): whether to install the full desktop application stack (office, Thunderbird, etc.).
    - `yes`: install the desktop stack
    - `no`: do not
- **DESKTOP_AUTOLOGIN** ( boolean ): toggle desktop autologin.
    - `yes`: automatically log in to the desktop
    - `no` (default): disable desktop autologin
- **PACKAGE_LIST_BOARD** ( space-separated list of packages ): extra packages to install on the system.
- **PACKAGE_LIST_BOARD_REMOVE** ( space-separated list of packages ): packages to remove from the system.
- **BOOT_FDT_FILE** ( device tree configuration ): force a specific device tree if it differs from the one u-boot selects.
    - `[family]/[file.dtb]`: replace the device tree with the one specified
    - `none`: do not use a device tree configuration
    - Example: `rockchip/rk3568-rock-3-a.dtb`
- **CPUMIN** ( minimum CPU frequency in Hz ): minimum CPU frequency the system scales to.
    - Default: differs per family (e.g. `480000` for sunxi8 boards)
- **CPUMAX** ( maximum CPU frequency in Hz ): maximum CPU frequency the system scales to.
    - Default: differs per family (e.g. `1400000` for sunxi8 boards)
- **FORCE_BOOTSCRIPT_UPDATE** ( boolean ): force bootscript installation if not present.
    - `yes`: enable
    - `no`: disable
- **OVERLAY_PREFIX** ( prefix ): prefix for device-tree and overlay file paths, set while creating an image.
    - Example: `sun8i-h3`

## Deprecated

- **BOOTCONFIG_LEGACY** / **BOOTCONFIG_CURRENT** / **BOOTCONFIG_EDGE** ( u-boot identifier ): use **BOOTCONFIG** instead.
- **PACKAGE_LIST_BOARD_DESKTOP** / **PACKAGE_LIST_BOARD_DESKTOP_REMOVE** ( space-separated list of packages ): use **PACKAGE_LIST_BOARD** / **PACKAGE_LIST_BOARD_REMOVE** instead.

## Support status

A board's support status is encoded in its configuration file's extension, and is shown at the login prompt:

| File extension | Description |
|:--|:--|
| `.conf` | Standard, supported board |
| `.csc` or `.tvb` | Community creation or no active maintainer |
| `.wip` | Work in progress |
| `.eos` | End of life |
