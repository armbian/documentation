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

Chooses the `make` target the framework invokes when it opens the interactive kernel configuration editor. The default `menuconfig` gives the familiar ncurses menu; set it to another kernel config front-end such as `nconfig`, `xconfig` or `gconfig` if you prefer that interface. It only has an effect when the build actually stops to configure the kernel (see `KERNEL_CONFIGURE`), so most non-interactive builds never touch it.

#### KERNEL_KEEP_CONFIG

`yes` | `no`

- `yes`: use kernel config file from previous compilation for the same branch, device family, and version
- `no`: use default or user-provided config file

Reuses the `.config` that a previous build for the same branch, device family and version exported to the output `config/` directory, instead of starting again from the shipped or user-provided defconfig. This is what lets your interactive `menuconfig` tweaks survive into the next build rather than being discarded. Leave it off for a clean, reproducible build from the tracked config; turn it on while iterating on kernel options so you don't have to re-apply your changes each time.

#### KERNEL_BUILD_DTBS

`string` · default: `yes`

Builds the kernel's device-tree blobs (`make dtbs`) and packages them alongside the kernel image so boards that boot from a DTB get the matching hardware description. It is on by default because almost every ARM and RISC-V board relies on device trees; architectures that have none, such as amd64, set it to `no` in their config. There is normally no reason to change it by hand.

#### KERNEL_INSTALL_TYPE

`string` · default: `install`

Selects the `make` target used to install the built kernel image, which differs by architecture and image format. Most arches use `install`; armhf uses `zinstall` for its compressed `zImage`, and some families (for example Amlogic Meson) use `uinstall` for a U-Boot image. The board and architecture configs set the right value, so you only override it when porting a new platform whose kernel produces a different image type.

#### KERNEL_EXTRA_CFLAGS

`string` · default: empty

Appends extra flags to the kernel's `KCFLAGS`, passed straight through to the compiler for every kernel object. It is mainly used to soften a compiler error that a newer toolchain raises on older kernel code — for example passing `-Wno-error=enum-int-mismatch` to demote a specific warning that would otherwise stop the build. Leave it empty for normal builds; some family configs set it automatically for kernels that need it, so only add flags here when you are chasing a build failure you understand.

#### DISABLE_KERNEL_PATCHES

`yes` | `no` (default)

Empties the kernel patch directory so the build applies none of Armbian's kernel patches, producing an as-close-to-vanilla upstream kernel as the source allows. Because the out-of-tree Wi-Fi drivers depend on that patched tree, this also forces `EXTRAWIFI=no`. Keep it off for normal images — the patches carry board fixes and features — and turn it on only to test whether a problem is caused by Armbian's patches or exists in mainline as well.

#### KERNEL_BTF

`string`

- `yes`
- `no`

Controls whether the kernel is built with BTF (BPF Type Format) debug information, which modern eBPF tooling relies on. By default the framework auto-detects based on the build host's available RAM, because the BTF/LD step is memory-hungry: on a low-RAM host it stops with an error rather than thrashing swap. Set `no` to accept a build without BTF, or `yes` to force BTF even on a low-RAM host (at the cost of heavy swap use); family code may set `no` to opt a platform out entirely. For more information on BTF see <https://docs.kernel.org/bpf/btf.html>

#### KERNEL_DO_STUBBLE

`string`

- `yes`
- `no` (default)

Build and bundle [stubble](https://github.com/ubuntu/stubble), Canonical's EFI stub (an extension of `systemd-stub`) that loads and auto-selects a device tree at boot from a hardware-ID database. When enabled, the framework cross-compiles `stubble.efi` for the target architecture (`amd64`/`arm64`/`riscv64`) and, during kernel packaging, runs `ukify` to assemble a Unified Kernel Image (UKI) `.efi` bundling the kernel, the stubble stub, the matching device trees (selected by `finddtbs.py` against the hwids database via `--devicetree-auto`) and an SBAT section for Secure Boot revocation.

The result is a single signed UKI that EFI-boots and picks the correct device tree for the running board automatically — intended for generic UEFI-on-devicetree images. It is enabled by default for the `uefidt` family (board `uefi-arm64-dt`) and is opt-in elsewhere; boards that boot through U-Boot do not use it. Requires `ukify` (from systemd) with `--devicetree-auto` support on the build host.

#### STUBBLE_GIT_URL

`string` · default: `https://github.com/ubuntu/stubble.git`

Git repository the framework clones to obtain the stubble source when `KERNEL_DO_STUBBLE=yes`; it has no effect otherwise. It defaults to Canonical's upstream repo. Override it to build against a fork or a local mirror — for example when building behind a firewall or to pin a patched version of stubble.

#### STUBBLE_GIT_BRANCH

`string` · default: `branch:main`

Selects the git ref checked out from `STUBBLE_GIT_URL`, in the framework's usual `type:name` form (`branch:`, `tag:` or `commit:`). It defaults to `branch:main`, the tip of upstream stubble. Change it to pin a specific tag or commit for a reproducible build, or to follow a different branch on your fork.

#### ATF_LOG_LEVEL

`integer` · default: `40`

Sets the `LOG_LEVEL` passed to the ARM Trusted Firmware (TF-A) build, which controls how much the secure firmware prints on the console during early boot. TF-A uses coarse steps — higher numbers are more verbose, with `40` (info) as the default and lower values such as `20` (error/warning only) making boot quieter. Some family configs lower it for cleaner boot output; raise it when debugging a TF-A or secure-world boot problem.

#### ATF_SKIP_LDFLAGS

`string` · default: `no`

Suppresses the `--no-warn-rwx-segment` linker flag that Armbian normally adds to the TF-A build to quiet a harmless warning from newer binutils about writable-and-executable segments. Set it to `yes` for TF-A trees whose linker invocation rejects or mishandles that flag, so the build stops trying to pass it at all. Most platforms leave it at `no`; it is a per-board escape hatch, not something to change globally.

#### ATF_SKIP_LDFLAGS_WL

`string` · default: `no`

Controls how the `--no-warn-rwx-segment` LD flag is handed to the TF-A build. By default it is passed through the compiler with the `-Wl,` prefix that gcc uses to forward options to the linker; set this to `yes` for TF-A builds that give their `TF_LDFLAGS` straight to the linker (`ld`) rather than through gcc, where the `-Wl,` prefix would be wrong. Several families that link TF-A directly set it to `yes`. It is ignored when `ATF_SKIP_LDFLAGS=yes` drops the flag entirely.

#### UBOOT_LOGLEVEL

`integer`

- `0` to `9`: set U-Boot log verbosity level
- `6`: (default)

Sets how verbose the U-Boot bootloader is on the console, baked into the build via `CONFIG_LOG_MAX_LEVEL` and `CONFIG_LOG_DEFAULT_LEVEL`. The scale runs from `0` (silent) to `9` (most verbose); the default `6` corresponds to info-level messages. Lower it (some boards set `1`) for a quiet, fast-looking boot, or raise it when you need to see what U-Boot is doing while debugging a boot failure.

#### FORCE_UBOOT_UPDATE

`string` · default: `no`

Makes the board-support package's post-install script re-flash U-Boot to the boot device whenever the BSP is upgraded on a running system. This is off by default because rewriting the bootloader in place is risky — an interrupted or wrong write can leave a board unbootable — so Armbian normally ships U-Boot updates without automatically applying them. Some boards where the bootloader lives on soldered storage (SPI/eMMC) and must stay in sync with the rootfs set `yes` in their config; only enable it yourself if you understand and accept that risk.

#### UBOOT_HASH_EXTRA

`string` · default: empty

Extra text mixed into the U-Boot artifact's cache hash, so that changing it invalidates the cached package and forces U-Boot to be rebuilt and repackaged. It exists because some U-Boot builds pull in external binary blobs (DDR init, TEE, vendor firmware) whose contents the normal hash inputs don't see; board configs set this — often to a version string or a checksum of those blobs — so a blob change reliably triggers a fresh build. Leave it empty unless you are packaging such out-of-tree blobs and need cache busting.

#### SRC_EXTLINUX

`string` · default: `no`

Makes the image boot through a standard `extlinux/extlinux.conf` file rather than Armbian's own boot script and `armbianEnv.txt`. When set to `yes`, the framework writes an extlinux config for U-Boot's distro-boot to read and skips installing the traditional boot scripts. It is set per board for platforms whose U-Boot expects the extlinux/distro-boot flow; leave it at `no` on boards that use Armbian's boot scripts, since the two mechanisms are mutually exclusive.
