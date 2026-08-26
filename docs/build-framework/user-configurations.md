---
seo_title: "Armbian userpatches: custom patches & config files"
description: "Customize Armbian builds with userpatches: add kernel, U-Boot and ATF patches, config files, a custom kernel config, extensions, first-boot presets and image scripts without editing the core."
---

# User configurations

Everything that customises a build lives in the `userpatches/` directory, so you never have to edit the build framework itself and your changes survive a `git pull`. The directory is created on first run; its location can be moved with the [`USERPATCHES_PATH`](/build-framework/switches/host-docker/#userpatches_path) switch.

## Configuration files

A configuration file named `userpatches/config-<name>.conf` (`.conf.sh` also works) is a bash script sourced during the build when you run `./compile.sh <name>`. It is the tidy alternative to a long command line: put one `PARAM=value` per line — any [build switch](/build-framework/switches/) works — and reuse it with a short command.

```bash
# userpatches/config-myboard.conf
BOARD="bananapim5"
BRANCH="current"
RELEASE="trixie"
BUILD_MINIMAL="no"
BUILD_DESKTOP="no"
```

```bash
./compile.sh myboard        # sources userpatches/config-myboard.conf
```

Command-line parameters still override what the config sets. More advanced files can use conditionals, define [hook functions](/build-framework/extensions/hooks/), and source other config files.

## Patches

The build applies patches from the framework's `patch/` tree and, on top of it, from the matching `userpatches/` directory — so you can add, override or disable patches without touching the shipped ones:

| Component | Framework | Your patches |
|---|---|---|
| Kernel | `patch/kernel/<KERNELPATCHDIR>/` | `userpatches/kernel/<KERNELPATCHDIR>/` |
| U-Boot | `patch/u-boot/<BOOTPATCHDIR>/` | `userpatches/u-boot/<BOOTPATCHDIR>/` |
| ATF (TF-A) | `patch/atf/<ATFPATCHDIR>/` | `userpatches/atf/<ATFPATCHDIR>/` |

The build prints the exact directory it is reading, so you always know where a patch belongs:

```text
[🌱] Started patching process for [ kernel rockchip64 current ]
[🌱] Looking for user patches in [ userpatches/kernel/archive/rockchip64-6.12 ]
```

All patch files must end in `.patch`. A file with the **same name** in `userpatches/` overrides the framework's copy — to *replace* an Armbian patch, copy it into the matching `userpatches/` directory and edit it; to *disable* one, create an empty file with the same name there.

!!! tip "Creating and refreshing patches"
    Rather than hand-editing `.patch` files, use the interactive [patch commands](/build-framework/commands/advanced/) — `kernel-patch`, `uboot-patch`, `atf-patch`, `crust-patch` — which pause the build so you can edit the source and then write the diff out for you, and `rewrite-kernel-patches` / `rewrite-uboot-patches` to refresh an existing set against newer sources.

## Custom kernel configuration

To build with your own kernel `.config`, drop it in `userpatches/` (or `userpatches/config/kernel/`) named after the config the board uses — the build reports the name it expects:

```text
[🌱] Using kernel config provided by user [ userpatches/linux-rockchip64-current.config ]
```

So for the example above you would provide `userpatches/linux-rockchip64-current.config`. Edit it interactively instead with the [`kernel-config`](/build-framework/commands/basic/) command.

## Family (source) overrides

If `userpatches/config/sources/families/<LINUXFAMILY>.conf` exists, it is sourced **in addition to** the framework's family file, letting you override kernel/U-Boot sources, branches and family tweaks for a whole SoC family. The build confirms the file it picked up:

```text
[🌱] Sourcing family configuration userpatches/config/sources/families/sunxi64.conf
```

## Extensions

Custom [build extensions](/build-framework/extensions/) go in `userpatches/extensions/`; the framework searches there before its own `extensions/` directory, so a user extension with the same name takes precedence. Enable them per build with the [`ENABLE_EXTENSIONS`](/build-framework/switches/image-contents/#enable_extensions) switch.

## First-boot presets

Every fresh image ships a `/root/.not_logged_in_yet` marker that triggers the interactive first-run setup (root password, user account, locale, network). Provide `userpatches/firstboot.conf` to preseed those answers for an unattended first boot — see [First-boot configuration](/User-Guide_Autoconfig/) for the available keys.

## Image customization script

`userpatches/customize-image.sh` (created from a template on first run) runs **inside the target rootfs in a chroot**, right before the image is finalised — the place to install extra packages, drop in files or tweak configuration. To add files, put them under `userpatches/overlay/`; they are reachable as `/tmp/overlay` from the script.

The chroot executes target-architecture code even when the build host is a different architecture (via `qemu-user-static`, or natively where the host matches — see [`PREFER_NATIVE_ARMHF`](/build-framework/switches/performance/#prefer_native_armhf)), so packages you install and commands you run apply to the SBC's architecture, not the host's.

## Partitioning and rootfs resize

By default the rootfs partition is shrunk to the minimum at build time and expanded to fill the media on first boot (leaving ~5% unpartitioned on cards of 4 GB or less to help the flash controller with wear levelling). Set [`FIXED_IMAGE_SIZE`](/build-framework/switches/filesystem/#fixed_image_size) (in MiB) to force a specific size instead.

The first-boot expansion is controlled by two markers you can create from `customize-image.sh`:

- `touch /root/.no_rootfs_resize` — skip the automatic expansion entirely.
- write a value to `/root/.rootfs_resize` — `50%` uses only half the media (unless the image already exceeds that), or an absolute sector count like `3887103s` sets the partition end. Values without `%` or `s` are ignored.
