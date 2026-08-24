---
seo_title: "Armbian build commands for compile.sh"
description: "Armbian build framework commands for compile.sh: build the kernel, run kernel-config menuconfig, rewrite the kernel config, check device trees and more."
---

# Build commands

### build

The default command. Builds a full OS image (or only the requested artifacts, depending on the switches) for the selected board and release. This is what runs when you invoke `./compile.sh` with no command, or explicitly:

Usage:
```bash
./compile.sh build BOARD=uefi-x86 BRANCH=current RELEASE=trixie
```

### flash

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
    it, and the command does not ask for confirmation beyond a short countdown.

Pass `BOARD`, `RELEASE` or `BRANCH` to narrow which image is picked, or `IMAGE`
to name a file outright:

```bash
./compile.sh flash CARD_DEVICE=/dev/sdX BOARD=rockpi-4a BRANCH=current
./compile.sh flash CARD_DEVICE=/dev/sdX IMAGE=output/images/Armbian_26.8.3_Rockpi-4a_trixie_current_6.12.13.img
```

When the image is picked for you, the choice is announced before the countdown,
so you can check it is the one you meant before anything is written:

```text
[🌱] cli_flash [ No image file specified. Using latest built image file found: Armbian-unofficial_26.08.0-trunk_Bananapim2_resolute_current_6.18.46_minimal.img ]
[🌱] cli_flash [ Flashing image file: Armbian-unofficial_26.08.0-trunk_Bananapim2_resolute_current_6.18.46_minimal.img ]
Counting down: 2... 1... 0...
```

If that is not the image you wanted, press ++ctrl+c++ during the countdown and
rerun with `BOARD`, `RELEASE`, `BRANCH` or `IMAGE` to pin it down. Pressing any
other key makes the countdown finish *sooner*, it does not cancel it, and a run
with no terminal attached (CI, or piped input) skips the countdown altogether.

The image is read back and verified against its checksum after writing. Set
`SKIP_VERIFY=yes` to skip that.

### docker / docker-shell / docker-purge

`docker` runs the build inside Armbian's build container — the default path, since `./compile.sh` relaunches itself in Docker when it is available. `docker-shell` drops you into an interactive shell inside that container (useful for editing sources, inspecting build errors, or running individual build steps), and `docker-purge` removes the container together with its named volumes and cached build image.

Usage:
```bash
./compile.sh docker-shell BOARD=rockpi-4a BRANCH=edge RELEASE=trixie
```

### kernel

Builds kernel and device tree (where applicable) and places it to the `output/debs`

Usage:
```bash
./compile.sh kernel BOARD=nanopi-r5c BRANCH=edge
```

### kernel-config

Automatically call kernel's `make menuconfig` (add or remove modules or features)

Usage:
```bash
./compile.sh kernel-config BOARD=nanopi-r5c BRANCH=edge
```

### rewrite-kernel-config

Automatically validates kernel config changes and dependency chains. After manually editing the config for a given family and branch this is needed to ensure the config change will persist our CI.

Usage:
```bash
./compile.sh rewrite-kernel-config BOARD=xxxxx BRANCH=current
```

### dts-check

Validate dts files and improve board & patch development overall.

This option validates the dts/dtb file for the selected board against the device tree bindings and outputs the validation logs to the user. It can be used when adding a new board, developing or improving a dts file.

Usage:
```bash
./compile.sh dts-check BOARD=nanopi-r5c BRANCH=edge 
```
### inventory-boards

Outputs a one-board-per-line CSV inventory of boards.

Sets `TARGETS_FILE` to something that doesn't exist, so the `targets-default.yaml` is used (so same list for everyone, save for userpatched-boards)

Usage:
```bash
./compile.sh inventory-boards
```
Outputs output/info/boards-inventory.csv

### kernel-dtb

Builds only DTB and outputs full preprocessed dts source

Outputs preprocessed DTS source for the board in question to `output/`
also outputs the same preprocessed DTS source, ran through `dtc` with input and output DTS formats for "normalized" comparisons

Usage:
```bash
./compile.sh kernel-dtb BOARD=xxxxx BRANCH=edge
```

### uboot-patch

Create patch files for u-boot.

The output patch files are written to
**output/patch/u-boot-${LINUXFAMILY}-${[BRANCH](https://docs.armbian.com/build-framework/switches/#user-space)}.patch**.
To use them in subsequent builds they
must be copied to the appropriate directories in the patch/u-boot directory.
See: [user-provided patches](https://docs.armbian.com/build-framework/user-configurations/#user-provided-patches)

Any uncommitted changes in the work tree and index are committed
to establish a clean work tree.
It would be best if there are no uncommitted changes when running
`uboot-patch`.

If there is an existing patch file at the output path specified above, it
may be applied before continuing work.

When the prompt `Press <ENTER\> after you are done editing in ${pwd}` appears,
in a separate window, navigate to the specified directory
and make any required changes.
When changes are complete,
return to the window running the `uboot-patch` command
and press `<ENTER>`. 

A patch to recreate the changes introduced to the u-boot tree is presented
and the prompt "Are you happy with this patch?".
You can respond
`yes` to accept the patch as-is and generate the output patch file,
`stop` to abort the command without producing the output patch file,
or anything else to loop back, to make further changes.

Instead of creating them while running `uboot-patch`,
new device tree files should be created in the relevant `dt` directory under
`patch/u-boot`
and new _defconfig files should be created in the relevant `configs` directory
under `patch/u-boot`.
While the `uboot-patch` command will add these new files to the patch
if they are created while running `uboot-patch`,
this is not the preferred way of adding these files.

### rewrite-uboot-patches

Prepares git, applies patches to git, and rewrites them back from git
same as kernel, it does git archeology for mbox-less patches, etc.

Note: MAINTAINER and MAINTAINEREMAIL should be set.

- uboot-patches-to-git alias is also added, but my guess is that the rewrite is more useful.
- refactor a common config function for both kernel and uboot.

Usage:
```bash
./compile.sh rewrite-uboot-patches BOARD=xxxx BRANCH=edge 
```

### rewrite-kernel-patches

Prepares git, applies patches to git, and rewrites them back from git
same as kernel, it does git archeology for mbox-less patches, etc.

Usage:
```bash
./compile.sh rewrite-kernel-patches BOARD=xxxx BRANCH=edge 
```

### targets

Generates output/info/git_sources.json file containing URL, branch, and commit hash combo.

The easiest way to generate file for all devices is to run `./compile.sh targets`. Then, at the time of release, we will copy the output/info/git_sources.json file to config/sources/git_sources.json. Once the file is copied, the hash information from the file will be used to fetch resources for git repositories where branches are specified instead of tags or commits.

Usage:
```bash
./compile.sh targets
```

### show-extensions

Lists the [extension hook points](/build-framework/extensions/hooks/) that exist in the build sources, optionally with their inline documentation.

The list is produced by statically scanning `lib/`, `extensions/` and `config/` for `call_extension_method` call sites, so it always describes the checked-out tree — including hooks added by userpatches — without running a build.

No board configuration is needed, the command does not relaunch into Docker and does not install host dependencies.

Usage:

```bash
./compile.sh show-extensions
```

Outputs one hook name per line, sorted alphabetically.

```bash
./compile.sh show-extensions SHOW_EXTENSIONS=docs
```

Outputs a Markdown document with the documentation of every hook; this is what [Extension Hooks](/build-framework/extensions/hooks/) is generated from.
