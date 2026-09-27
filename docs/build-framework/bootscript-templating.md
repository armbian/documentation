---
seo_title: "Armbian bootscript templating: generic U-Boot boot.cmd"
description: "How Armbian renders U-Boot boot scripts from .template files with envsubst: the BOOTSCRIPT_TEMPLATE__ variables, the generic boot-generic.cmd.template, and how a board opts in."
---

# Bootscript templating

A board's U-Boot boot script (`boot.cmd`) can be a plain file that is copied as-is, or a
**template** that the build renders with the board's own values. Templating lets many boards
share one generic script and differ only in a handful of settings such as the load address or
the serial console.

The generic template is
[`config/bootscripts/boot-generic.cmd.template`](https://github.com/armbian/build/blob/main/config/bootscripts/boot-generic.cmd.template).
It is a superset of the `sunxi`, `mvebu` and `rockchip64` boot scripts. The build code lives in
[`lib/functions/rootfs/distro-agnostic.sh`](https://github.com/armbian/build/blob/main/lib/functions/rootfs/distro-agnostic.sh)
and
[`lib/functions/bsp/armbian-bsp-cli-deb.sh`](https://github.com/armbian/build/blob/main/lib/functions/bsp/armbian-bsp-cli-deb.sh).

!!! note

    The generic template is new; at the time of writing no board in `armbian/build` selects it yet.
    Existing boards keep using their own `boot-<family>.cmd` files.

## How a board opts in

The board (or family) configuration sets `BOOTSCRIPT` to `<source>:<destination>`. The source is
looked up first in `userpatches/bootscripts/`, then in `config/bootscripts/`. If the source file
name ends in `.template`, the build renders it; any other name is copied unchanged.

```bash
BOOTSCRIPT='boot-generic.cmd.template:boot.cmd'
```

The destination (`boot.cmd` above) is the name of the rendered file in `/boot` (and in the BSP
package under `/usr/share/armbian/`).

!!! warning

    `BOOTSCRIPT` set in a board file can be overridden by the family configuration
    (`config/sources/families/`). Check the effective value for every board you convert.

## Template variables

Rendering uses [`envsubst`](https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html).
Only variables whose names start with `BOOTSCRIPT_TEMPLATE__` are substituted. The generic
template uses the following ones; set them in the board configuration.

| Variable | Purpose |
|:--|:--|
| `BOOTSCRIPT_TEMPLATE__ALIGN_TO` | Alignment applied to the load addresses the script calculates, for example `0x00001000` (4 KiB). ARM64 kernels want the `Image` start on a 2 MiB (`0x00200000`) boundary. |
| `BOOTSCRIPT_TEMPLATE__BOARD_FAMILY` | Board family, for example `sun8i`. Becomes the U-Boot variable `family`. |
| `BOOTSCRIPT_TEMPLATE__BOARD_VENDOR` | Vendor name used in the device tree path (`dtb/<vendor>/`) and the overlay prefix, for example `allwinner`. Becomes `vendor`. |
| `BOOTSCRIPT_TEMPLATE__ROOTFS_TYPE` | Root filesystem type, for example `ext4`. Becomes `rootfstype`. |
| `BOOTSCRIPT_TEMPLATE__LOAD_ADDR` | Address the script loads `armbianEnv.txt` to, for example `0x45000000`. Becomes `load_addr`. |

Three more variables are filled in by the build; do not set them yourself:

| Variable | Filled from |
|:--|:--|
| `BOOTSCRIPT_TEMPLATE__DISPLAY_CONSOLE` | [`DISPLAYCON`](/build-framework/board-configuration/) and `console=` entries in `SRC_CMDLINE` |
| `BOOTSCRIPT_TEMPLATE__SERIAL_CONSOLE` | [`SERIALCON`](/build-framework/board-configuration/#serialcon) and `console=` entries in `SRC_CMDLINE` |
| `BOOTSCRIPT_TEMPLATE__CREATE_DATE` | Time of rendering (`date -Ru`) |

Console lists are comma separated and `:` becomes `,`, so `SERIALCON="ttyS0:115200,ttyGS0"`
produces `console=ttyS0,115200 console=ttyGS0`.

## Rendering and validation

1. The build collects the display and serial console values (`bootscript_export_display_console`,
   `bootscript_export_serial_console`).
2. `render_bootscript_template` substitutes every variable that is set and starts with
   `BOOTSCRIPT_TEMPLATE__`.
3. `proof_rendered_bootscript_template` searches the result for any remaining
   `$BOOTSCRIPT_TEMPLATE__...` or `${BOOTSCRIPT_TEMPLATE__...}` reference. If one is found, the
   build stops with *"Render of bootscript template was not successful"* and names the file to
   inspect.

A variable that is **unset** is left unrendered and fails the build. A variable that is set to an
empty string renders as empty and passes.

The rendering happens twice: once when the BSP package is built and once when the image rootfs
is assembled.

## Example board configuration

```bash
DISPLAYCON=''
SERIALCON="ttyS0:115200,ttyGS0"

BOOTSCRIPT='boot-generic.cmd.template:boot.cmd'
BOOTSCRIPT_TEMPLATE__ALIGN_TO='0x00001000'
BOOTSCRIPT_TEMPLATE__BOARD_FAMILY="${BOARDFAMILY:-sun8i}"
BOOTSCRIPT_TEMPLATE__BOARD_VENDOR='allwinner'
BOOTSCRIPT_TEMPLATE__LOAD_ADDR='0x45000000'
BOOTSCRIPT_TEMPLATE__ROOTFS_TYPE="${ROOTFS_TYPE:-ext4}"
```

## Your own template

Put a file ending in `.template` into `userpatches/bootscripts/` and point `BOOTSCRIPT` at it.
Reference values as `${BOOTSCRIPT_TEMPLATE__NAME}` and define `BOOTSCRIPT_TEMPLATE__NAME` in your
board or [user configuration](/build-framework/user-configurations/). Any other `$` in the
script (U-Boot's own `${variables}`) is left alone, because only the `BOOTSCRIPT_TEMPLATE__`
names are substituted.

## What the generic script does

1. Defines the U-Boot environment variables.
2. Loads `armbianEnv.txt`.
3. Builds the kernel command line from the loaded settings.
4. Loads the device tree and applies overlays.
5. Loads the kernel image and the initial ramdisk.
6. Boots the kernel with the ramdisk and device tree locations.

When U-Boot provides `setexpr`, the script calculates the load addresses of the kernel and the
ramdisk from the sizes of the device tree, kernel and ramdisk, aligned to `align_to`, so the
regions cannot overlap. Without `setexpr` it falls back to the addresses U-Boot predefines:
`fdt_addr_r`, `kernel_addr_r` and `ramdisk_addr_r`.

For the reasoning behind the address calculation and the size detection of the device tree,
kernel and ramdisk, see
[`boot-generic.cmd.template.md`](https://github.com/armbian/build/blob/main/config/bootscripts/boot-generic.cmd.template.md)
next to the template.

Reference: [board configuration](/build-framework/board-configuration/),
[user configurations](/build-framework/user-configurations/), U-Boot
[shell commands](https://docs.u-boot.org/en/latest/usage/index.html#shell-commands) and
[environment variables](https://docs.u-boot.org/en/latest/usage/environment.html).
