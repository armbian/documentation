---
seo_title: "Armbian kernel & U-Boot build switches"
description: "Kernel and bootloader switches for the Armbian build: kernel source fetch, config, compiler, BTF, stubble UKI, ATF/TF-A and U-Boot options."
---

# Kernel & U-Boot

Switches that control how the kernel and bootloader are fetched, configured and built: kernel source and config, compiler, kernel features (BTF, stubble UKI), ATF/TF-A and U-Boot.

#### KERNEL_GIT

`string`

- `shallow`
- `full`
- unset (default): let the system decide

Selects how the Linux kernel git tree is fetched when a kernel has to be built from scratch. The kernel repo is huge; to avoid hammering upstream git servers, Armbian caches daily git-tree exports on ghcr.io and only `git fetch`es the small delta.

- `shallow` — a shallow tree for a single `stable` branch. Small download, less disk; ideal for restricted devices (SBCs) building a single kernel.
- `full` — the complete tree (Torvalds' `master` plus all supported `stable` branches). Large download and disk footprint, but more efficient over time when building several kernels on one machine (CI servers, developer workstations).

#### KERNEL_COMPILER

`string`

The compiler used to compile the kernel. Usually, this option is set by the board config, but it can be set to `clang` to use LLVM to compile the kernel.

Example:

```sh
./compile.sh KERNEL_COMPILER=clang
```

#### KERNEL_MENUCONFIG

`string` · default: `menuconfig`

The `make` target used for interactive kernel configuration (e.g. `nconfig`, `xconfig`).

#### KERNEL_KEEP_CONFIG

`yes` | `no`

- `yes`: use kernel config file from previous compilation for the same branch, device family, and version
- `no`: use default or user-provided config file

#### KERNEL_BUILD_DTBS

`string` · default: `yes`

Build and package the kernel device-tree blobs (dtbs).

#### KERNEL_INSTALL_TYPE

`string` · default: `install`

Kernel image `make`-install target (`install`/`zinstall`/`uinstall`, per architecture).

#### KERNEL_EXTRA_CFLAGS

`string` · default: empty

Extra `KCFLAGS` appended to the kernel compile (e.g. to downgrade a specific error).

#### DISABLE_KERNEL_PATCHES

`yes` | `no` (default)

Disable all Armbian-specific kernel patches and build a vanilla kernel; also disables `EXTRAWIFI`.

#### KERNEL_BTF

`string`

- `yes`
- `no`

Default is to auto-detect based on build host available RAM. If not enough RAM available, use =no to accept building without BTF debug information, or use =yes to force building with BTF even if low RAM. Family code can set this to opt-out of BTF. For more information on BTF see <https://docs.kernel.org/bpf/btf.html>

#### KERNEL_DO_STUBBLE

`string`

- `yes`
- `no` (default)

Build and bundle [stubble](https://github.com/ubuntu/stubble), Canonical's EFI stub (an extension of `systemd-stub`) that loads and auto-selects a device tree at boot from a hardware-ID database. When enabled, the framework cross-compiles `stubble.efi` for the target architecture (`amd64`/`arm64`/`riscv64`) and, during kernel packaging, runs `ukify` to assemble a Unified Kernel Image (UKI) `.efi` bundling the kernel, the stubble stub, the matching device trees (selected by `finddtbs.py` against the hwids database via `--devicetree-auto`) and an SBAT section for Secure Boot revocation.

The result is a single signed UKI that EFI-boots and picks the correct device tree for the running board automatically — intended for generic UEFI-on-devicetree images. It is enabled by default for the `uefidt` family (board `uefi-arm64-dt`) and is opt-in elsewhere; boards that boot through U-Boot do not use it. Requires `ukify` (from systemd) with `--devicetree-auto` support on the build host.

#### STUBBLE_GIT_URL

`string` · default: `https://github.com/ubuntu/stubble.git`

Git source repo for the stubble UKI/boot tooling (used when `KERNEL_DO_STUBBLE=yes`).

#### STUBBLE_GIT_BRANCH

`string` · default: `branch:main`

Git ref of the stubble repo to fetch.

#### ATF_LOG_LEVEL

`integer` · default: `40`

TF-A `LOG_LEVEL` passed to the ARM Trusted Firmware build.

#### ATF_SKIP_LDFLAGS

`string` · default: `no`

Skip adding the `--no-warn-rwx-segment` LD flag to the TF-A build.

#### ATF_SKIP_LDFLAGS_WL

`string` · default: `no`

Pass the TF-A LD flag directly (omit the `-Wl,` gcc prefix).

#### UBOOT_LOGLEVEL

`integer`

- `0` to `9`: set U-Boot log verbosity level
- `6`: (default)

Controls the U-Boot bootloader log level during image building. Lower values produce less verbose output. This affects `CONFIG_LOGLEVEL` and `CONFIG_LOG_MAX_LEVEL` in U-Boot configuration.

#### FORCE_UBOOT_UPDATE

`string` · default: `no`

Force flashing/updating U-Boot on running systems via the bsp postinst.

#### UBOOT_HASH_EXTRA

`string` · default: empty

Extra string folded into the U-Boot artifact hash to force a repackage when a blob changes.

#### SRC_EXTLINUX

`string` · default: `no`

Boot via `extlinux.conf` instead of Armbian boot scripts.
