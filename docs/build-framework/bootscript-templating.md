---
seo_title: "Armbian bootscript templating"
description: "How bootscript templating works in the Armbian build framework: .template files, envsubst rendering, and the BOOTSCRIPT_TEMPLATE__ variables a board config must set."
---

# Bootscript templating

A bootscript is the small script U-Boot runs to start the board: it loads the
kernel, the device tree and the initial ramdisk, then boots the kernel. Many
boards need almost the same bootscript, with only a few values changed, such as
the load address, the serial console or the board vendor. Bootscript templating
lets those boards share one generic bootscript instead of each keeping its own
copy.

## How it works

A bootscript template is a normal bootscript file whose name ends in
`.template`, for example `boot-generic.cmd.template`. It holds placeholders
where a board-specific value belongs. Each placeholder is a variable whose name
starts with `BOOTSCRIPT_TEMPLATE__`, for example `$BOOTSCRIPT_TEMPLATE__LOAD_ADDR`.

When the build runs, it renders the template with
[`envsubst`](https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html),
a small tool that replaces each placeholder with the value of the matching
variable from the build environment. The rendered result is written out as the
plain bootscript, for example `boot.cmd`, on the boot partition and in the
board-support package. If any placeholder is left unrendered, the build stops
with an error, so a board config with a missing value fails loudly instead of
producing a broken boot script. That check only catches placeholders that were
never replaced: a variable set to an empty value, for example
`BOOTSCRIPT_TEMPLATE__ALIGN_TO=''`, is replaced with nothing, so the check
passes and the generated script has no alignment value for its address
calculation. Give each of the five board inputs a nonempty value.

Two cases change which bootscript the image actually boots. If
`SRC_EXTLINUX=yes`, the build writes an `extlinux.conf` instead and does not
deploy the bootscript to the image or the board-support package, so changing
`BOOTSCRIPT` has no effect there. If `ROOTFS_TYPE=nfs`, the build still
renders the template, but then replaces `/boot/boot.cmd` on the image with the
NFS bootscript, while the board-support package can still contain the rendered
file.

A board selects a template through the `BOOTSCRIPT` variable in its board
config, written as `source:destination`:

```bash
BOOTSCRIPT='boot-generic.cmd.template:boot.cmd'
```

The part before the colon is the template file under
[`config/bootscripts/`](https://github.com/armbian/build/tree/main/config/bootscripts)
in the build repository. The part after the colon is the file name written to
the boot partition. A bootscript without the `.template` suffix is copied
unchanged, exactly as before; only `.template` files are rendered.

## Variables a board config must set

Every board that uses the generic bootscript template must set these variables
in its board config. If one is missing, the build errors out.

| Variable | What it sets |
| --- | --- |
| `BOOTSCRIPT_TEMPLATE__ALIGN_TO` | Address boundary used when the bootscript calculates load addresses, for example `0x00001000` (4 KiB). ARM64 boards usually align the kernel `Image` to a 2 MiB (`0x00200000`) boundary. |
| `BOOTSCRIPT_TEMPLATE__BOARD_FAMILY` | The CPU family of the board, for example `sun8i`. It is written into the rendered bootscript as the family name. |
| `BOOTSCRIPT_TEMPLATE__BOARD_VENDOR` | The vendor of the board, for example `allwinner`. It is used to resolve device tree and overlay file names. |
| `BOOTSCRIPT_TEMPLATE__LOAD_ADDR` | The load address used to load scripts and device tree files, for example `0x45000000`. It differs per architecture. |
| `BOOTSCRIPT_TEMPLATE__ROOTFS_TYPE` | The filesystem type of the root filesystem, for example `ext4` or `f2fs`. It can fall back to the build's `ROOTFS_TYPE`, as in `"${ROOTFS_TYPE:-ext4}"`. |

Two more variables exist, but a board config must leave them empty. The build
fills them in itself from the console settings:

| Variable | What it sets |
| --- | --- |
| `BOOTSCRIPT_TEMPLATE__DISPLAY_CONSOLE` | Leave empty. The build fills it from `DISPLAYCON` and the kernel command line. |
| `BOOTSCRIPT_TEMPLATE__SERIAL_CONSOLE` | Leave empty. The build fills it from `SERIALCON` and the kernel command line. |

Set the consoles with the normal variables instead, for example
`SERIALCON="ttyS0:115200,ttyGS0"`. Several console devices can be listed,
separated by commas. See the
[Linux kernel serial console documentation](https://www.kernel.org/doc/html/latest/admin-guide/serial-console.html)
for the allowed syntax.

One variable is set by the build itself and never by a board config:
`BOOTSCRIPT_TEMPLATE__CREATE_DATE` holds the date and time the bootscript was
rendered, and is written into the header of the generated file.

## Example board config

A board config that uses the generic bootscript template looks like this:

```bash
DISPLAYCON=''
SERIALCON="ttyS0:115200,ttyGS0"

BOOTSCRIPT='boot-generic.cmd.template:boot.cmd'
BOOTSCRIPT_TEMPLATE__ALIGN_TO='0x00001000'
BOOTSCRIPT_TEMPLATE__BOARD_FAMILY="${BOARDFAMILY:-sun8i}"
BOOTSCRIPT_TEMPLATE__BOARD_VENDOR='allwinner'
BOOTSCRIPT_TEMPLATE__DISPLAY_CONSOLE='' # leave empty here, use DISPLAYCON instead
BOOTSCRIPT_TEMPLATE__LOAD_ADDR='0x45000000'
BOOTSCRIPT_TEMPLATE__ROOTFS_TYPE="${ROOTFS_TYPE:-ext4}"
BOOTSCRIPT_TEMPLATE__SERIAL_CONSOLE='' # leave empty here, use SERIALCON instead
```

Boards move to the generic bootscript one by one, so most boards still use
their own plain bootscript today.

## Watch out for family overrides

`BOOTSCRIPT` in a board config can be overridden by a board family file under
`config/sources/families/` or `config/sources/families/includes/`. If a family file sets
`BOOTSCRIPT`, the board's value is lost. A family file that wants to keep the
board's choice should use a fallback instead of a plain assignment:

```bash
declare -g BOOTSCRIPT="${BOOTSCRIPT:-boot-sunxi.cmd}:boot.cmd"
```

Check every board of the family to make sure the bootscript selection is the
one intended.

## What the generic bootscript does

The generic bootscript, rendered from
[`boot-generic.cmd.template`](https://github.com/armbian/build/blob/main/config/bootscripts/boot-generic.cmd.template),
covers the boot steps that the `sunxi`, `mvebu` and `rockchip64` bootscripts
used to repeat separately:

1. Define U-Boot environment variables.
2. Load the U-Boot environment from `armbianEnv.txt`.
3. Build the kernel command line from the loaded environment settings.
4. Process the device tree (DT).
5. Process the kernel image.
6. Process and load the initial ramdisk.
7. Boot the kernel with the locations of the initial ramdisk and the device tree.

The device tree is loaded first, then the kernel image, with the initial
ramdisk last. When U-Boot has the `setexpr` command built in, the bootscript
calculates the load addresses of the kernel image and the initial ramdisk, so
they cannot overlap in memory. Without `setexpr`, it falls back to the
predefined load addresses from U-Boot or its default environment. The probe
for `setexpr` only runs when `load_addr_calc` is empty, which is the default.
Setting `load_addr_calc=off` in `/boot/armbianEnv.txt` forces fixed addresses
even when U-Boot supports `setexpr`.

The generated `boot.cmd` starts with a header saying it was rendered from a
template. Do not edit the generated file by hand: edit `/boot/armbianEnv.txt`
to change the supported boot parameters instead.

## References

- Generic bootscript template:
  [`config/bootscripts/boot-generic.cmd.template`](https://github.com/armbian/build/blob/main/config/bootscripts/boot-generic.cmd.template)
- Longer guide in the build repository:
  [`config/bootscripts/boot-generic.cmd.template.md`](https://github.com/armbian/build/blob/main/config/bootscripts/boot-generic.cmd.template.md)
- Rendering code:
  [`render_bootscript_template` in `lib/functions/rootfs/distro-agnostic.sh`](https://github.com/armbian/build/blob/main/lib/functions/rootfs/distro-agnostic.sh)
- Feature as merged:
  [armbian/build pull request #8935](https://github.com/armbian/build/pull/8935)
- [U-Boot shell commands](https://docs.u-boot.org/en/latest/usage/index.html#shell-commands)
- [U-Boot environment variables](https://docs.u-boot.org/en/latest/usage/environment.html)
- [Linux device tree usage](https://www.kernel.org/doc/html/latest/devicetree/usage-model.html)
- [Linux initial ramdisk](https://docs.kernel.org/admin-guide/initrd.html)
