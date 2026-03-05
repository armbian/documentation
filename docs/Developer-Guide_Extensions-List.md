# Extensions Reference

Alphabetical reference of all official Armbian build framework extensions.
Extensions live in the `extensions/` directory of the build repository.

To enable one or more extensions:

```bash
./compile.sh BOARD=... BRANCH=... ENABLE_EXTENSIONS="ext-name,another-ext"
```

Extensions with dedicated documentation pages are linked below.
All others are documented by a short description and key parameters.

---

## allwinner-kernel-bump

Bumps the kernel version for Allwinner-based boards.

---

## amlogic-fip-blobs

Fetches Amlogic FIP (Firmware Image Package) blobs needed for bootloader assembly on Amlogic SoCs.

---

## apa

Enables Armbian Package Archive (APA) in the target image by default.

---

## arm64-compat-vdso

Enables 32-bit compat vDSO for arm64 kernels. Requires a 32-bit ARM cross-compiler for GCC builds (`gcc-arm-linux-gnueabi` or custom `CROSS_COMPILE_COMPAT`). For clang builds uses the built-in LLVM backend.

---

## armbian-config

Installs `armbian-config` from the Armbian GitHub repository into the image.

---

## armbian-live-patch

Installs the Armbian Live Patch systemd service into the BSP package.

---

## bcmdhd

Builds the Broadcom BCM WiFi (`bcmdhd`) driver as a DKMS kernel module. Requires working kernel headers.

---

## bcmdhd-spacemit

Builds the Broadcom BCM WiFi driver for SpacemiT platforms as a DKMS kernel module.

---

## bluetooth-hciattach

Sets up Bluetooth via `hciattach` for boards that require serial attachment.

---

## c-plus-plus-compiler

Adds a C++ compiler to host build dependencies. The C++ compiler is no longer included by default; enable this extension when the build requires it.

---

## ccache-remote

Enables ccache with a remote storage backend (Redis or HTTP/WebDAV) for sharing the compilation cache across multiple build hosts. Requires ccache 4.4+.

---

## cleanup-space-final-image

Runs `zerofree` and cleans APT caches in the final image to reduce disk footprint.

---

## cloud-init

Installs and configures cloud-init in the target image.

---

## detect-unused-extensions

Developer/testing extension: a hook honeypot used to verify the extension framework works correctly.

---

## fake-vcgencmd

Installs a fake `vcgencmd` stub for Raspberry Pi software compatibility on non-Pi boards.

---

## fs-btrfs-support

Adds Btrfs filesystem support: host build tools and image packages. Auto-enabled when `ROOTFS_TYPE=btrfs`.

---

## fs-cryptroot-support

Adds LUKS/cryptroot support. Auto-enabled when `CRYPTROOT_ENABLE=yes`.

---

## fs-f2fs-support

Adds F2FS filesystem support. Auto-enabled when `ROOTFS_TYPE=f2fs`.

---

## fs-nilfs2-support

Adds NILFS2 filesystem support. Auto-enabled when `ROOTFS_TYPE=nilfs2`.

---

## fs-xfs-support

Adds XFS filesystem support. Auto-enabled when `ROOTFS_TYPE=xfs`.

---

## gen-sample-extension-docs

Generates extension hook documentation and a sample extension file. Useful for extension developers.

---

## grub

Standard GRUB bootloader setup for UEFI-capable boards. Supports `DISTRO_GENERIC_KERNEL` mode.

---

## grub-riscv64

GRUB bootloader setup for RISC-V 64-bit boards.

---

## grub-with-dtb

GRUB with device tree blob (DTB) embedding support.

---

## gxlimg

Builds the `gxlimg` tool used for creating Amlogic bootable images.

---

## image-output-abl

Converts the output image to ABL (Android Boot Loader) format using `mkbootimg`.

---

## image-output-oowow

Creates an image compatible with the OOWOW recovery system for Khadas boards.

---

## image-output-ovf

Produces an OVF (Open Virtualization Format) archive for use in VMware and other hypervisors. Depends on `image-output-qcow2`.

---

## image-output-qcow2

Produces a qcow2 image suitable for QEMU/KVM virtualization.

---

## image-output-utm

Produces a UTM-compatible image for macOS virtualization. Depends on `image-output-qcow2`.

---

## image-output-vhd-azure

Produces a VHD image for use with Microsoft Azure.

---

## image-output-vhdx

Produces a VHDX image. Depends on `image-output-qcow2`.

---

## initramfs-usb-gadget-ums

Adds USB Mass Storage (UMS) gadget support to the initramfs, allowing the board to expose its storage over USB.

---

## jethub-burn

Adds JetHub device flashing support to the build.

---

## kernel-rust

Enables Rust language support in the Linux kernel (`CONFIG_RUST`). Installs a rustup-managed toolchain into `${SRC}/cache/tools/rustup/` and configures all required make parameters.

See: [kernel-rust extension](Developer-Guide_Extension-kernel-rust.md)

---

## kernel-version-toolchain

Adds the compiler name and version (e.g. `gcc13.3`, `clang20.1`) to the kernel artifact version string, ensuring cache invalidation when the toolchain changes.

**Variables:** none (auto-detects from `KERNEL_COMPILER`).

---

## lowmem

Applies Armbian optimizations for low-memory boards (reduced parallelism, swap configuration, etc.).

---

## lsmod

Applies `localmodconfig` based on an lsmod output file to build a minimal kernel. Place the lsmod file in `userpatches/lsmod/<board>.lsmod`. **Variable:** `LSMOD` (defaults to `$BOARD`).

---

## lvm

Adds LVM (Logical Volume Manager) support to the image.

---

## marvell-tools

Fetches Marvell Armada A3700 build tools, DDR library, and binary blobs needed for bootloader assembly.

---

## mesa-vpu

Installs Mesa 3D and VPU/Chromium acceleration packages. On Ubuntu: full 3D + 4K VPU. On Debian: 3D only.

---

## mtkflash

Adds MediaTek device flashing tool support to the build.

---

## net-chrony

Installs the `chrony` NTP daemon for network time synchronization.

---

## net-network-manager

Installs NetworkManager and Netplan for network interface management.

---

## net-systemd-networkd

Installs systemd-networkd and Netplan for network interface management.

---

## net-systemd-timesyncd

Installs `systemd-timesyncd` for network time synchronization.

---

## nicod-armbian-gaming

Gaming-oriented Armbian image configuration.

---

## nomod

Builds the kernel with all modules disabled (`localmodconfig` with empty lsmod). Produces a non-working kernel — intended for rapid kernel build/packaging tests only.

---

## nvidia

Builds the Nvidia proprietary kernel module via DKMS. Not available in minimal images.

---

## odin2-preset-firstrun

Applies preset first-run configuration specific to the Odin2 gaming device.

---

## preset-firstrun

Applies preset network and first-run configuration to the image (writes `.not_logged_in_yet`).

---

## radxa-aic8800

Builds the Radxa AIC8800 WiFi driver as a DKMS kernel module. Requires working kernel headers.

---

## rkbin-tools

Fetches Rockchip binary tools (`rkbin`) from the configured git repository. **Variables:** `RKBIN_GIT_URL`, `RKBIN_GIT_BRANCH`.

---

## rkdevflash

Adds Rockchip device flashing tool support to the build.

---

## sunxi-tools

Adds a 32-bit ARM cross-compiler to host dependencies for Allwinner (sunxi) builds. Only required outside Docker.

---

## syterkit-allwinner

Writes the SyterKit bootloader image to the appropriate offset in the Allwinner output image.

---

## ti-debpkgs

Installs Texas Instruments packages from the official TI Debian package repository.

---

## u-boot-menu

Configures the U-Boot boot menu for boards that support it.

---

## uboot-btrfs

Enables Btrfs filesystem support in U-Boot (`CONFIG_CMD_BTRFS`).

---

## uefi-edk2-rk3588

Integrates UEFI EDK2 firmware for Rockchip RK3588 boards.

---

## ufs

Creates a UFS-sector-aligned image. Requires Debian Trixie (13) or newer as the build host. Set `DOCKER_ARMBIAN_BASE_IMAGE=debian:trixie` when building in Docker.

---

## uwe5622-allwinner

Builds the UWE5622 WiFi driver for Allwinner-based boards.

---

## v4l2loopback-dkms

Builds the `v4l2loopback` virtual camera kernel module via DKMS. Not available in minimal images.

---

## vmware-vm

Creates a VMware-compatible image (VMDK + OVF) with VMware tools installed. Depends on `image-output-ovf`.

---

## wayland-sessions-mask

Masks Wayland desktop session entries for boards with limited or unstable Wayland support.

---

## watchdog

Installs the `watchdog` daemon and enables `CONFIG_WATCHDOG` / hardware watchdog device support in the kernel.

---

## xorg-lima-serverflags

Configures X.Org server flags for the Lima open-source GPU driver.

---

## yt6801

Builds the Motorcomm YT6801 Ethernet controller driver as a DKMS kernel module. Requires working kernel headers.

---

## zfs

Builds ZFS kernel module and userspace tools via DKMS. Requires working kernel headers.
