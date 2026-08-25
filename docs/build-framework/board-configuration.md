---
seo_title: "Armbian board configuration variables"
description: "Reference of every variable in an Armbian board .conf file: BOARD_NAME, BOARD_VENDOR, BOARDFAMILY, BOOTCONFIG, KERNEL_TARGET, kernel modules, partitions, console and more."
---

# Board configuration

Every board Armbian supports is described by a configuration file in
[`config/boards/<board>.conf`](https://github.com/armbian/build/tree/main/config/boards)
(or `.csc` / `.tvb` / `.wip` / `.eos` depending on [support status](#support-status)).
Its variables declare the board's name, family, bootloader, kernel targets and the
other build-time settings the framework applies when building that board. This page
is the reference for all of them; to add a whole new board from scratch, start with
[Adding a Board](/build-framework/adding-a-board/).

!!! tip

    If a variable is unclear, grep the source for context:
    `grep -r -A5 -B5 "VARIABLE_HERE" /path/to/armbian/build`

## Identity

#### BOARD_NAME

`string` · required

Human-readable board name used in the welcome text, hostname and other places. The
convention is `COMPANY PRODUCT VERSION`. It is frequently referenced by scripting
logic (and hacks), so keep it consistent with the name declared in the board
configuration.

- Example: `OLIMEX Teres A64`

#### BOARD_VENDOR

`string` · required

Vendor / manufacturer slug for the board, written in lowercase (for example `radxa`,
`xunlong`, `sinovoip`, `amlogic`). It groups boards by their maker and is validated in
CI, which rejects a board config that leaves it empty.

- Example: `radxa`

#### BOARDFAMILY

`string` · required

Family the board belongs to. It selects the family-specific configuration applied at
build time — temperature limits, LED behaviour, default CPU frequencies and similar.
The value must match a family defined under
[`config/sources/families/`](https://github.com/armbian/build/blob/main/config/sources/README.md).

- Example: `sun50iw1`

#### BOARD_MAINTAINER

`space-separated list of GitHub logins` · recommended

The board's maintainer(s), by GitHub username. Boards left without a maintainer tend
to rot, so CI warns when this is empty; it is left blank on unmaintained (`.csc`)
boards.

#### INTRODUCED

`year` · recommended

The year the board first came to market. Used for inventory and ordering.

- Example: `2022`

## Bootloader & U-Boot

#### BOOTCONFIG

`u-boot identifier`

Name of the U-Boot defconfig for the build, without the `_defconfig` suffix. Look up
the matching configuration in the
[U-Boot source tree](https://github.com/u-boot/u-boot/tree/master/configs).

- Example: `teres-i`

#### CRUSTCONFIG

`crust identifier`

Name of the [crust](https://github.com/crust-firmware/crust) defconfig for the build.
Set this only when the board has an Allwinner CPU with an AR100 coprocessor whose SoC
is supported by crust firmware; look up the value in the
[crust source tree](https://github.com/crust-firmware/crust/tree/master/configs).

- Example: `nanopi_m1_defconfig`

#### BOOT_LOGO

`string` · default: not set

Whether to show the Armbian splash during the bootloader phase.

- `yes`: always show the Armbian boot logo
- `desktop`: show it only when `BUILD_DESKTOP=yes`
- unset (default): no boot logo

#### BOOT_FDT_FILE

`string`

Force a specific device tree when it differs from the one U-Boot would pick itself.

- `[family]/[file.dtb]`: use this device tree instead
- `none`: do not use a device tree configuration
- Example: `rockchip/rk3568-rock-3-a.dtb`

#### OVERLAY_PREFIX

`string`

Prefix for device-tree and overlay file paths. It is used to build the overlay path
for [`DEFAULT_OVERLAYS`](#default_overlays) and is written to `armbianEnv.txt` as
`overlay_prefix=` so the running system loads overlays from the right directory.

- Example: `sun8i-h3`

#### DEFAULT_OVERLAYS

`space-separated list of dtb overlays`

Device-tree overlays enabled by default. Each family ships a basic dtb, but boards
expose different SoC features (one board might wire up four USB ports where another
does not), so the relevant overlays are switched on per board. Combined with
[`OVERLAY_PREFIX`](#overlay_prefix) to locate the overlay files.

- Examples: `usbhost0`, `usbhost2`, `usbhost3`, `cir`, `analog-codec`, `gpio-regulator-1.3v`, `uart1`

#### FORCE_BOOTSCRIPT_UPDATE

`boolean`

- `yes`: force the boot script to be overwritten on every BSP package upgrade
- `no` (default): treat the boot script as user-editable and leave it alone

Normally the boot script (`boot.cmd` / `boot.scr`) is left untouched once installed so
that a board-support-package upgrade does not clobber local edits. Set `yes` on boards
whose boot script must always track the packaged version; roughly two dozen board
configs do. Leave it unset unless you specifically need that behaviour.

## Kernel

#### KERNEL_TARGET

`comma-separated list of kernel branches` · required

Which kernel branches are built for the board. Standard values are `legacy`,
`current` and `edge`; many boards also build a SoC-vendor kernel via `vendor` (and
variants such as `vendor-edge`). Any valid branch name may be listed. A board with no
`KERNEL_TARGET` fails the build.

- Example: `current,edge` or `vendor,current,edge`

#### KERNEL_TEST_TARGET

`comma-separated list of kernel branches` · recommended

Kernel branches to test when they differ from the build targets; it also drives
build-list generation and is recorded in `/etc/armbian-release`. (Internal switch.)

- Example: `current,edge`

#### MODULES

`space-separated list of kernel modules`

Kernel modules to load at boot for **all** kernel branches. The build writes each
name into `/etc/modules` on the image, so the modules are auto-loaded early on the
running board.

#### MODULES_CURRENT / MODULES_LEGACY / MODULES_EDGE

`space-separated list of kernel modules`

Same as [`MODULES`](#modules), but scoped to a single kernel branch (the suffix names
the branch — any branch works, e.g. `MODULES_VENDOR`). When a branch-specific list is
set it is used **instead of** the generic `MODULES` for that branch, not in addition
to it.

#### MODULES_BLACKLIST

`space-separated list of kernel modules`

Kernel modules to blacklist / deny for **all** kernel branches. Each name is written
to `/etc/modprobe.d/blacklist-<board>.conf` on the image so it is not auto-loaded.

#### MODULES_BLACKLIST_CURRENT / MODULES_BLACKLIST_LEGACY / MODULES_BLACKLIST_EDGE

`space-separated list of kernel modules`

Same as [`MODULES_BLACKLIST`](#modules_blacklist), but scoped to a single kernel
branch (the suffix names the branch). A branch-specific blacklist replaces the generic
`MODULES_BLACKLIST` for that branch rather than adding to it.

## Partitions & filesystem

#### IMAGE_PARTITION_TABLE

`string` · default: `msdos`

Disklabel type for the image.

- `msdos` (default): DOS/MBR disklabel
- `gpt`: GPT disklabel

#### BOOTFS_TYPE

`string` · default: `ext4`

Filesystem for the boot partition.

- `none`: keep `/boot` on the root filesystem (no separate boot partition)
- `ext4` (default): [Fourth Extended Filesystem](https://en.wikipedia.org/wiki/Ext4)
- `ext2`: [Second Extended Filesystem](https://en.wikipedia.org/wiki/Ext2)
- `fat`: [FAT32](https://en.wikipedia.org/wiki/File_Allocation_Table#FAT32)

#### BOOTSIZE

`integer` (MiB) · default: `256` (when a separate `/boot` is required)

Size of a separate `/boot` partition, in MiB, created when one is required. Override
it where a board's bootloader needs more room; the partitioning step falls back to
256 MiB when a boot partition is required but the value is left empty or unusably
small.

## Console & hardware

#### SERIALCON

`comma-separated list of terminal interfaces [:bandwidth]` · default: `ttyS0`

Which serial console(s) the system enables (a getty is started on each, and the value
also feeds the boot script and U-Boot). Append `:bandwidth` to run a console at a
non-default speed. Defaults to `ttyS0` when unset.

- Example: `ttyS0:15000000,ttyGS1`

#### DEFAULT_CONSOLE

`string` · default: not set

Default console for boot output, written as `console=` into `armbianEnv.txt` — useful
for headless devices.

- `serial`: send boot messages to the serial console
- `both`: serial and display
- unset (default): leave the family default

#### HAS_VIDEO_OUTPUT

`boolean`

- `yes` (default): the board has video output; video-related configuration is enabled
- `no`: no video output; desktop builds are refused (`BUILD_DESKTOP` is forced off)

Declares whether the board can drive a display (for splash, desktop and other
eye candy). Setting `no` on a headless board disables the video stack and prevents a
desktop image from being built for it.

#### POWER_MANAGEMENT_FEATURES

`boolean`

- `yes`: enable systemd sleep modes (suspend, hibernate, hybrid sleep)
- `no` (default): disable all sleep modes

Controls whether system sleep is allowed on the built image. Off by default because
suspend/hibernate are unstable on most single-board computers; enable it only on
hardware where sleep is known to work.

#### CPUMIN

`integer` (Hz)

Minimum CPU frequency the system scales down to. The default differs per family (for
example `480000` on sunxi8 boards); set it only to override the family default.

#### CPUMAX

`integer` (Hz)

Maximum CPU frequency the system scales up to. The default differs per family (for
example `1400000` on sunxi8 boards); set it only to override the family default.

## Software

#### SKIP_ARMBIAN_REPO

`boolean` · default: `no`

- `yes`: exclude the Armbian apt repository from the image (`armbian.sources` stays `.disabled`)
- `no` (default): include the Armbian repo

Builds the image without Armbian's apt repository, so the system sees only the base
Debian/Ubuntu repositories. Useful when developing a new release before its repository
exists, or for custom images that must not pull packages from Armbian.

#### PACKAGE_LIST_BOARD

`space-separated list of packages`

Extra packages to install on images for this board, on top of the family and
distribution defaults.

#### PACKAGE_LIST_BOARD_REMOVE

`space-separated list of packages`

Packages to remove from images for this board.

#### FULL_DESKTOP

`boolean`

- `yes`: install the full desktop application stack (office, Thunderbird, etc.)
- `no`: install only the minimal desktop

Whether desktop images for this board carry the full application stack or a leaner
selection.

#### DESKTOP_AUTOLOGIN

`boolean` · default: `no`

- `yes`: automatically log in to the desktop
- `no` (default): show the desktop login prompt

## Deprecated

#### BOOTCONFIG_LEGACY / BOOTCONFIG_CURRENT / BOOTCONFIG_EDGE

`u-boot identifier`

Per-branch U-Boot defconfig overrides. Deprecated — use [`BOOTCONFIG`](#bootconfig)
instead.

#### PACKAGE_LIST_BOARD_DESKTOP / PACKAGE_LIST_BOARD_DESKTOP_REMOVE

`space-separated list of packages`

Desktop-only package add/remove lists. Deprecated — use
[`PACKAGE_LIST_BOARD`](#package_list_board) /
[`PACKAGE_LIST_BOARD_REMOVE`](#package_list_board_remove) instead.

## Support status

A board's support status is encoded in the extension of its configuration file, and is
shown at the login prompt:

| File extension | Description |
|:--|:--|
| `.conf` | Standard, supported board |
| `.csc` or `.tvb` | Community creation or no active maintainer |
| `.wip` | Work in progress |
| `.eos` | End of life |
