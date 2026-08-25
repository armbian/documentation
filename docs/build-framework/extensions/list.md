---
seo_title: "Armbian build extensions list & ENABLE_EXTENSIONS"
description: "Alphabetical reference of official Armbian build framework extensions, how to enable them with ENABLE_EXTENSIONS, and what each one does."
---


# Extensions Reference

Alphabetical reference of all official Armbian build framework extensions.
Extensions live in the [`extensions/`](https://github.com/armbian/build/tree/main/extensions)
directory of the build repository.

To enable one or more extensions:

```bash
./compile.sh BOARD=... BRANCH=... ENABLE_EXTENSIONS="ext-name,another-ext"
```

!!! info "This page is generated"
    Each entry comes from the `# @description` header of the extension's source
    file in `armbian/build`. To change a description, edit that header — not this
    page. Extensions with a dedicated page are linked from their entry.


## allwinner-kernel-bump

Automates bumping the `edge` kernel for Allwinner (`sunxi*`) boards to the latest mainline version. On relaunch it reads the new `KERNEL_MAJOR_MINOR` from `master`, points `KERNELPATCHDIR` at `archive/sunxi-<ver>`, fetches Megous's git bundle from `xff.cz`, and regenerates the `patches.megous` set plus `series.conf`. Only usable with sunxi edge builds.

## amlogic-fip-blobs

Fetches the Amlogic FIP (Firmware Image Package) blobs required for bootloader assembly on Amlogic SoCs. Clones `retro98boy/amlogic-fip-blobs` at a pinned commit into the sources tools cache via `fetch_from_repo`. Enabled for Amlogic boards whose u-boot build needs these proprietary firmware blobs to produce a bootable image.

## apa

Enables the Armbian Package Archive (APA) in the target image by setting `APA_IS_ACTIVE` and adding the `github.armbian.com/apa` apt repository. Installs `armbian-common` and `armbian-bsp` from it, plus the matching `armbian-desktop-*` metapackage when a `DESKTOP_ENVIRONMENT` (XFCE/KDE/GNOME) is selected. Enable it to source Armbian's core packages from APA by default.

## applications-ha

Builds a Home Assistant Supervised image: enables `docker-ce`, installs `os-agent` and the Armbian-patched `homeassistant-supervised` deb, adds AppArmor to the kernel cmdline, and pulls in NetworkManager, AppArmor and CIFS/NFS support. Requires a full (non-`MINIMAL`) Debian image and appends a `-homeassistant` suffix to the output.

## applications-kali

Preinstalls the Kali `kali-rolling` APT repository into the image and tags it `-kali`. Adds Kali's signing key, writes the sources list, and pins all Kali packages to priority 50 so nothing is pulled unless explicitly requested. Adds a login MOTD listing installable `kali-tools-*` packages; Debian only.

## applications-omv

Preinstalls OpenMediaVault (OMV), the NAS web management platform, into the image. Runs `armbian-config --api module_omv install` in the chroot after repo customization and appends an `-omv` image suffix. Only supported on Debian `bookworm` and `trixie`; the build errors out on any other release.

## arm64-compat-vdso

Builds the arm64 kernel with `CONFIG_COMPAT`, `CONFIG_COMPAT_VDSO` and `CONFIG_ARM64_32BIT_EL0`, letting a host on this kernel run armhf userspace natively at full speed. This lets armhf rootfs/chroot steps build native instead of through `qemu-user-static` (~10× faster); the framework auto-detects it via `PREFER_NATIVE_ARMHF`. Needs a 32-bit ARM cross-compiler for GCC builds.

## armbian-config

Installs the `armbian-config` management tool into the image from Armbian's own APT repository. Adds `http://github.armbian.com/configng` (stable/main, signed by `APT_SIGNING_KEY_FILE`) as an APT source, then installs the package in the chroot. Packages are built from `armbian/configng` and merged into the main repo periodically.

## armbian-live-patch

Installs the Armbian Live Patch systemd service and its `/usr/lib/armbian/armbian-live-patch` helper into the BSP package. On boot and before apt upgrades it downloads a patch script from `dl.armbian.com/_patch`, verifies its GPG signature against the Armbian keyring, then runs it — letting Armbian push small live fixes to deployed systems.

## bcmdhd

Installs the Broadcom `bcmdhd` WiFi driver as a DKMS module. Downloads the latest `pcie`, `sdio`, or `usb` variant `.deb` (selected by `BCMDHD_TYPE`) from the `armbian/bcmdhd-dkms` GitHub releases and builds it in the chroot. Forces `INSTALL_HEADERS=yes`; skips when `BCMDHD_TYPE` is unset or the kernel lacks working headers.

## bcmdhd-spacemit

Installs the Broadcom `bcmdhd` WiFi driver for SpacemiT boards as a prebuilt DKMS `.deb`, downloaded from the `sven-ola/bcmdhd-spacemit-dkms` Codeberg releases and built in the chroot. Fetches the `pcie`, `sdio` or `usb` variant per `BCMDHD_SPACEMIT_TYPE`/`BCMDHD_SPACEMIT_TAG`. Forces `INSTALL_HEADERS=yes`, requiring a kernel with working headers.

## bluetooth-hciattach

Configures Bluetooth on boards that need manual `hciattach` serial attachment. Adds the `bluetooth`/`bluez` packages and installs a systemd service running `rfkill unblock` plus `hciattach` with `BLUETOOTH_HCIATTACH_PARAMS`/`BLUETOOTH_HCIATTACH_RKFILL_NUM`. Only deployed on `vendor*`/`legacy*` BSP branches, since mainline kernels bind Bluetooth via serdev.

## brostrend-aic8800-dkms

Installs the AIC8800 WiFi/BT DKMS driver for BroStrend USB adapters. Fetches the latest `aic8800-dkms` release from `Shadowrom2020/aic8800-dkms` GitHub and builds the kernel module in the chroot. Forces `INSTALL_HEADERS=yes` — requires a kernel with working headers package.

## c-plus-plus-compiler

Adds a C++ compiler to the host build dependencies, no longer included by default in `prepare-host.sh`. Appends the native `g++` plus the `g++-aarch64-linux-gnu` arm64 cross-compiler (skipped on non-standard hosts like riscv64) to `EXTRA_BUILD_DEPS`. Enable it when the build requires a C++ compiler.

## ccache-remote

Enables ccache with a remote Redis or HTTP/WebDAV backend so the compilation cache is shared across build hosts, and forces `USE_CCACHE=yes`. Set `CCACHE_REMOTE_STORAGE` explicitly, or let it auto-discover a server via DNS-SD/Avahi, DNS SRV (`CCACHE_REMOTE_DOMAIN`) or legacy `ccache.local`. Requires ccache 4.4+ and identical project paths on every host.

See: [ccache-remote extension](/build-framework/extensions/ccache-remote/)

## cleanup-space-final-image

Shrinks the final image's compressed footprint. Removes bulky rarely-needed firmware trees (`netronome`, `mrv`, `mellanox`), runs `zerofree` on every ext4 partition after unmount so unused blocks compress away, and logs the largest directories via `du`. Pulls in `fs-tools::zerofree`; enable it to produce smaller downloadable images.

## cloud-init

Installs and configures `cloud-init` in the image using the NoCloud data source, which reads its configuration from the FAT `armbi_boot` partition. Adds the `cloud-init` and `cloud-initramfs-dyn-netconf` packages, forces `BOOTFS_TYPE=fat`, ships empty default configs (hostname + DHCP), and disables `armbian-first-run`. Tags the image `-ci`.

## detect-unused-extensions

Developer/testing extension that detects "wishful hooking" — extension functions whose hook-point names are never actually called by the build. Runs late via `extension_metadata_ready` to scan `defined_hook_point_functions`, warning about any uncalled hook. Includes a deliberate honeypot function to verify the detector itself still works.

## docker-ce

Preinstalls Docker CE from Docker's official apt repository into the target image. Fetches the Docker GPG key, wires up a `download.docker.com` sources list for the matching Debian/Ubuntu release, then installs `docker-ce`, `docker-ce-cli`, `containerd.io` and `docker-compose-plugin` in the chroot. Enable it to ship container support out of the box.

## fake-vcgencmd

Installs a stub `vcgencmd` so Raspberry Pi software that probes it runs on non-Pi boards. Downloads the script (plus LICENSE/README) from `clach04/fake_vcgencmd` v0.0.2 into `/usr/bin/vcgencmd` and makes it executable. Skipped on `rpi4b`, which ships the genuine `vcgencmd`.

## fs-btrfs-support

Adds Btrfs filesystem support, no longer bundled by default in `prepare-host.sh`. Appends `btrfs-progs` to both host build deps and the image packages, and injects the matching checksum module (`xxhash_generic` or `blake2b_generic`) into initramfs based on `BTRFS_CHECKSUM`. Auto-enabled when `ROOTFS_TYPE=btrfs` in `main-config.sh`.

## fs-cryptroot-support

Encrypts the root partition with LUKS via `cryptsetup luksFormat`, adds `cryptsetup-initramfs` to the image and requires a separate boot partition. Supports a passphrase, an auto-generated autounlock keyfile, or `dropbear-initramfs` remote SSH unlock (`CRYPTROOT_SSH_UNLOCK`). Auto-enabled when `CRYPTROOT_ENABLE=yes`.

## fs-f2fs-support

Adds F2FS filesystem support to the build host. Appends `f2fs-tools` to `EXTRA_BUILD_DEPS` so the required tooling is present when building an f2fs root, which is no longer bundled by `prepare-host.sh`. Auto-enabled when `ROOTFS_TYPE=f2fs` in `main-config.sh`.

## fs-nilfs2-support

Adds NILFS2 root-filesystem support. Installs `nilfs-tools` into both the image and the host build dependencies, and appends the `nilfs2` module to `/etc/initramfs-tools/modules` so the log-structured filesystem can be mounted at boot. Auto-enabled when `ROOTFS_TYPE=nilfs2` in `main-config.sh`.

## fs-xfs-support

Adds XFS root filesystem support, no longer bundled by default in `prepare-host.sh`. Installs `xfsprogs` into the image and adds it to the host build dependencies (`fs-tools::xfsprogs`) so the rootfs can be created. Auto-enabled when `ROOTFS_TYPE=xfs` is set in `main-config.sh`.

## gateway-dk-ask

Integrates NXP's ASK data-plane acceleration for the Mono Gateway DK (LS1046A). Builds the ASK kernel modules (CDX, FCI, auto-bridge, sfp-led, lp5812) in-tree, then compiles userspace tools (`fmlib`, `fmc`, `libfci`, `libcli`, `dpa-app`, `cmm`) and patched libraries in the chroot. Everything ships as one `gateway-dk-ask` `.deb`.

## gen-sample-extension-docs

Generates reference documentation for the build framework's extension system. Writes auto-generated Markdown of every hook point to `userpatches/extensions/hooks.auto.docs.md` and a fully commented `sample-extension.sh` stub, both derived from the live hook registry. Enable it as an extension developer to discover all available hooks.

## grub

Standard GRUB bootloader setup for UEFI-capable boards (amd64, arm64, loong64), with optional amd64 BIOS support and a `DISTRO_GENERIC_KERNEL` mode that boots the distro kernel instead of Armbian's. Installs `grub-efi`, generates `grub.cfg`, and sets `GRUB_GFXPAYLOAD_LINUX=text` with `splash plymouth.ignore-serial-consoles` to keep the framebuffer console on `fbcon` and kernel boot messages visible.

## grub-riscv64

Sets up the GRUB bootloader for UEFI-capable RISC-V 64-bit boards, using target `riscv64-efi` and a GPT/ESP layout instead of u-boot. Adds `grub-efi` and `efibootmgr` packages and copies the DTBs into the ESP. Mirrors the console/splash cmdline conventions of the standard `grub` extension.

## grub-with-dtb

A superset of the `grub` extension that boots via DeviceTree instead of ACPI, for EFI-only ARM64 machines like the ThinkPad X13s or Phytium D2000. Requires `BOOT_FDT_FILE`/`GRUB_FDT_FILE`, and installs a kernel hook plus a custom `09_linux_with_dtb.sh` GRUB script that deploys the DTB to the boot partition.

## gxlimg

Builds the `gxlimg` host tool for packaging Amlogic bootable images. Fetches `repk/gxlimg` at a pinned commit, compiles it and installs to `/usr/local/bin/gxlimg` (only when the commit changed). Provides `gxlimg_repack_fip_with_new_uboot`, which extracts BL2/BL3x from an existing FIP and repacks them with a fresh `u-boot.bin` for `gxl`/`g12a`/`g12b` SoCs.

## image-output-abl

Repackages the finished image into Android Boot Loader (ABL) format for Qualcomm/Snapdragon boards. Adds `mkbootimg` as a host dep, splits the rootfs into a separate `.rootfs.img`, then builds gzipped-kernel boot and recovery images for each DTB in `ABL_DTB_LIST`. Skips when `UEFI_GRUB_TARGET` or `BOOTFS_TYPE` is set.

## image-output-arduino

Converts the Armbian image into a QDL-flashable `.tar` archive for the Arduino UNO Q (Qualcomm QRB2210). Splits the boot and root partitions with `dd` and extracts the U-Boot `boot.img` from the rootfs. Bundles Qualcomm firehose flash binaries fetched from the `armbian/qcombin` repo during image creation.

## image-output-iso

Builds a bootable live `.iso` from a UEFI image so it boots from a BMC/IPMI virtual CD-ROM. Packs the kernel, `live-boot` initrd and a squashfs rootfs into a hybrid ISO9660 with self-contained GRUB (`xorriso`/`mksquashfs`/`grub-mkstandalone`), dropping the `.img` by default. UEFI-only with Secure Boot off, restricted to `uefi-*` boards using the `grub` extension.

## image-output-oowow

Converts the output image to Khadas OOWOW recovery format using Khadas' `xze` tool, downloaded and cached from the krescue repo, and embeds board metadata matched by `KHADAS_OOWOW_BOARD_ID`. Forces `COMPRESS_OUTPUTIMAGE` to none/sha because xze already applies its own xz compression. Requires `KHADAS_OOWOW_BOARD_ID` to be set.

## image-output-ovf

Converts the qcow2 from `image-output-qcow2` into a VMware VMDK using `qemu-img` (resized +47G), generates a matching `.vmx` and bundles them into a `.vmware.zip` for import into VMware and other hypervisors. Tune the guest with `OVF_VM_CPUS` and `OVF_VM_RAM_GB`; `OVF_KEEP_QCOW2`/`OVF_KEEP_IMG` retain intermediates.

## image-output-qcow2

Converts the finished raw image to qcow2 for QEMU/KVM using `qemu-img convert`, adding `qemu-utils` to the host build dependencies. Optionally grows the disk by `QCOW2_RESIZE_AMOUNT` and deletes the original `.img` unless `QCOW2_KEEP_IMG=yes`. Skipped entirely when `SKIP_QCOW2=yes` (set by the Azure VHD extension).

## image-output-sophgo-emmc-installer

Rewrites the finished `.img` into an eMMC installer card for Sophgo SG200x (Milk-V Duo S): extracts `fip-emmc.bin`, wraps the whole image as an `armbian.emmc` CIMG payload, and builds a bootable FAT card whose U-Boot `cvi_update` flashes the eMMC. Opt-in; use it when no running system is available to install from.

## image-output-utm

Produces a UTM-compatible virtual machine bundle for macOS from the qcow2 output; depends on `image-output-qcow2`. Wraps a resized qcow2 disk and a generated `config.plist` into a `.utm.zip`, setting CPUs and RAM via `UTM_VM_CPUS`/`UTM_VM_RAM_GB`. Enable it to run Armbian images under UTM on Apple Silicon or Intel Macs.

## image-output-vhd-azure

Produces a fixed-format VHD for Microsoft Azure via `qemu-img convert -O vpc`, first rounding the raw disk up to a whole megabyte plus 512 bytes as Azure requires. Forces `SKIP_QCOW2=yes`, making it incompatible with `image-output-qcow2`. Deletes the original `.img` unless `VHD_KEEP_IMG=yes`.

## image-output-vhdx

Converts the qcow2 from `image-output-qcow2` into a dynamic Microsoft Hyper-V VHDX using `qemu-img` (resized +47G), then bundles it with a PowerShell VM-creation script into a `.hyperv.zip`. Enable it to get a Hyper-V-importable image; set `VHDX_KEEP_QCOW2` or `VHDX_KEEP_IMG` to retain the intermediates.

## initramfs-usb-gadget-ums

An early initramfs `init-premount` script turns the board into a USB Mass Storage gadget. When `ums=yes` is on the kernel command line it exposes all block devices over USB and loops forever instead of booting. A host can then flash the eMMC/SD/NVMe with BalenaEtcher or similar.

## jethub-burn

Converts the finished `.img` into an Amlogic USB burn image for JetHub J80/J100/J200 boards. Fetches `jethome-iot/jethome-tools`, compiles the board DTB partition, extracts the rootfs and packs everything with `aml_image_v2_packer_new` using `u-boot.nosd.bin` from the U-Boot deb. Outputs `${version}.burn.img` alongside the normal image.

## kernel-debug-tiers

Bakes cumulative kernel debug information into headless boards so serial-console facilities (Magic SysRq, KGDB, pstore) print meaningful symbols instead of raw hex. `KERNEL_DEBUG_TIER` (0-3, default 1) layers printk/lockup detection, then pstore/ramoops and full kallsyms, then KGDB/KDB over serial. Requires `DEBUG_INFO_BTF`, so `KERNEL_BTF=no` is a hard error.

## kernel-rust

Enables Rust language support in the Linux kernel (`CONFIG_RUST`). Installs a rustup-managed toolchain (`RUST_VERSION`, `bindgen-cli`, `rust-src`) into `${SRC}/cache/tools/rustup/`, keyed by a content hash, and passes `RUSTC`/`RUSTFMT`/`BINDGEN` make params. Ships prebuilt Rust crate artifacts in `linux-headers` so out-of-tree DKMS Rust modules can build.

See: [kernel-rust extension](/build-framework/extensions/kernel-rust/)

## kernel-version-toolchain

Appends the kernel compiler name and major.minor version (e.g. `gcc13.3`, `clang20.1`) to the kernel artifact version string. Auto-detects the binary from `KERNEL_COMPILER` and reads it via `-dumpfullversion`, adding a `_T` part to the artifact hash. Enable it so cached kernels rebuild when the host toolchain changes.

## lowmem

Applies userland tweaks for boards with under 256MB RAM: writes an initramfs config (`MODULES=dep`, fixed `RUNSIZE`), installs the `lowmem-mkswap` swapfile service and `armbian-lowmem` defaults, and disables `armbian-ramlog` and zram swap. Enable it on very-low-memory boards so apt, locale-gen and boot run smoothly.

## lsmod

Runs `make localmodconfig` against a captured `lsmod` file to strip the kernel down to only the modules your hardware actually loads, compiling several times faster. Reads the file from `userpatches/lsmod/${LSMOD}.lsmod`, where the `LSMOD` variable defaults to `$BOARD`. Errors out if that file is missing.

## lvm

Places the root filesystem on an LVM logical volume. Creates a PV/VG/LV on the root partition (`lvm2`), sizing the volume to ~130% of the rootfs, and forces a separate boot partition (`BOOTPART_REQUIRED=yes`) since many bootloaders cannot read LVM. Customise the group name via `${LVM_VG_NAME:-armbivg}`; a `-lvm` suffixed image is produced.

## marvell-tools

Fetches the host sources needed to assemble Marvell Armada A3720/A8040 bootloaders. Clones pinned `A3700-utils` (bschnei's fork, fixes modern-toolchain build errors), `mv-ddr-marvell`, `binaries-marvell`, `cryptopp`, and CZ.NIC `mox-boot-builder` for the WTMI secure firmware. Used by EspressoBin/MacchiatoBin bootloader builds; pins guarantee reproducible firmware.

## mtkflash

Clones and builds the Rust `mtk-flash` tool from `grinn-global/mtk-flash`, then flashes a MediaTek board over `/dev/ttyACMx` with the produced `lk.bin`, `fip.img` and disk image after the build. Needs the Rust toolchain and direct host USB access (no Docker); set `MTKFLASH_TTYACM_DEVICE` to pick the port.

## net-chrony

Adds the `chrony` package to the image for network time synchronization. Chrony is a full-featured NTP client/server that syncs faster and copes with intermittent connections and jitter better than `systemd-timesyncd`. Enable it as the alternative time-sync extension when accurate or robust NTP is required.

## net-network-manager

Manages network interfaces with NetworkManager backed by Netplan. Installs `network-manager`, `network-manager-openvpn` and `netplan.io` (plus desktop, Ubuntu and VPN extras), enables `systemd-resolved`, disables `NetworkManager-wait-online`, and deploys the extension's Netplan/NM config files. Requires `NETWORKING_STACK=network-manager`, which selects this stack.

## net-systemd-networkd

Manages network interfaces with `systemd-networkd` plus Netplan: adds `netplan.io`, enables `systemd-networkd` and `systemd-resolved`, and installs Netplan/networkd config plus drop-in overrides for `systemd-networkd-wait-online` and `apt-daily-upgrade`. Requires `NETWORKING_STACK=systemd-networkd`, and chmods the Netplan configs to `600`.

## net-systemd-timesyncd

Adds the `systemd-timesyncd` package to the image and enables `systemd-timesyncd.service` in the chroot for network time synchronization. This is systemd's lightweight built-in SNTP client, sufficient when full NTP features aren't needed. Enable it as a minimal alternative to the `chrony` extension.

## nicod-armbian-gaming

Adds a launcher for NicoD's `armbian-gaming` project to the image. Drops `/usr/local/bin/nicod-armbian-gaming`, a script that clones (or `git pull`s) `NicoD-SBC/armbian-gaming` on first run and executes its `armbian-gaming.sh`. Appends a `-gaming` suffix to the image name; enable it to ship a gaming-oriented image.

## nomod

Builds the kernel with almost all modules disabled by running `make mod2noconfig`, stripping the config down to built-ins only. The result is a deliberately non-working kernel. Use it only to speed up testing of the kernel image build and packaging pipeline, never for a usable image.

## nvidia

Installs the NVIDIA proprietary driver and builds its kernel module via DKMS, blacklisting `nouveau`. Auto-detects the highest `nvidia-dkms-<N>` in the chroot's apt index (or uses `NVIDIA_DRIVER_VERSION`/the Debian `nvidia-dkms` metapackage), forces `INSTALL_HEADERS=yes`, and ships an `armbian-nvidia-autodetect` service that disables the driver on GPU-less hosts. Skipped on minimal images.

## odin2-preset-firstrun

Bakes first-boot presets for the Odin2 handheld gaming device into `/root/.not_logged_in_yet`, setting the `odin2` user, default locale/timezone, shell, and Ethernet/WiFi network toggles. Also clones `Squishy123/odin2-scripts` into the rootfs and installs an `install-odin2-scripts` launcher. Enable it when building images specifically for the Odin2.

## photonicat-pm

Installs the `photonicat-pm` DKMS power-management driver for the Ariaboard Photonicat router. Fetches the latest `HackingGate/photonicat-pm` release deb and builds the kernel module in the chroot, forcing `INSTALL_HEADERS=yes`. Requires a kernel with a working headers package and is skipped on kernels ≥ 6.20.

## preset-firstrun

Writes a `/root/.not_logged_in_yet` file that preseeds the first-boot wizard so the image configures itself unattended. Sets network mode (Ethernet/WiFi with SSID, key, country and optional static IP), locale, timezone, shell, and default root/user names and passwords. Edit its placeholder values before enabling for hands-off deployments.

## r8125-dkms

Installs Realtek's official `r8125` (v9.016.01) 2.5GbE DKMS driver and blacklists the buggy in-kernel `r8169`. Host-side downloads `awesometic/realtek-r8125-dkms`, then adds/builds/installs the module in the chroot against the target kernel. Forces `INSTALL_HEADERS=yes`; needed on the EasePi-A2 rk35xx vendor kernel where `r8169` breaks RTL8125B TX.

## radxa-aic8800

Installs the AIC8800 WiFi DKMS driver and firmware for Radxa boards. Downloads the `aic8800-<type>-dkms` and firmware debs (`pcie`/`sdio`/`usb` per `AIC8800_TYPE`) from the latest `radxa-pkg/aic8800` release and builds the module in the chroot. Forces `INSTALL_HEADERS=yes`, needs working kernel headers, and skips kernels ≥ 7.3.

## rkbin-tools

Fetches the Rockchip `rkbin` repository (default `armbian/rkbin`) and installs the `loaderimage` and `trust_merger` host tools into `/usr/local/bin`, reinstalling only when the git commit changes. Needed to package Rockchip U-Boot/TPL/SPL images. Override the source with `RKBIN_GIT_URL` and `RKBIN_GIT_BRANCH`.

## rkdevflash

Builds Radxa's `rkdeveloptool` and flashes the freshly built image to a connected Rockchip device over USB. Enables `rkbin-tools` for the `ROCKUSB_BLOB` SPL loader, waits for the board, switches Maskrom to Loader mode, writes the image (`wl`), then resets it. Cannot run under Docker.

## rkusbboot

Clones and builds Rockchip `rkusbboot` from `RadxaNaoki/rkusbboot`, adding host deps like `libusb`/`libudev` and enabling `rkbin-tools` for the loader blobs. After the build it RAMBoots the fresh image over USB into a Maskrom-mode device, enabling `CONFIG_ROCKCHIP_MASKROM_IMAGE` in mainline u-boot. Cannot run under Docker.

## sophgo-sg200x-aic8800

Adds AIC8800D80 Wi-Fi 6 + Bluetooth 5 (SDIO) support for Sophgo SG200x / Milk-V Duo S boards, which lack a mainline driver. Copies the pinned `queenkjuul/aic8800-milkv-duos` vendor driver into the kernel tree and builds it as in-tree modules with a compiled-in firmware path. Also configures modprobe ordering and a Bluetooth attach service.

## sunxi-tools

Builds and installs `sunxi-tools` (e.g. `sunxi-fexc`) on the host from the `linux-sunxi/sunxi-tools` Git repo, recompiling only when the commit hash changes. Also adds 32-bit armhf (`gcc-arm-linux-gnueabi`) and OpenRISC (`gcc-or1k-elf`) cross-compilers for Allwinner bootloader and crust builds; those compilers are only needed outside Docker.

## sysrq-serial-trigger

Enables Magic SysRq over the serial console so an operator can sync, remount read-only and reboot a hung headless board. Sets the `MAGIC_SYSRQ`/`MAGIC_SYSRQ_SERIAL` kernel options with a non-empty `SYSRQ_SERIAL_SEQUENCE` (default `sysrq`), raises U-Boot `BOOTDELAY` to 5, and writes `kernel.sysrq=1` for the full command set.

## syterkit-allwinner

Writes the SyterKit bootloader to the correct offset of a finished Allwinner image. Downloads the latest `YuzukiHD/SyterKit` release for `SYTERKIT_BOARD_ID`, extracts it, and `dd`s `extlinux_boot_bin_card.bin` to the loop device at an 8KB seek. Auto-used by Allwinner boards that boot via SyterKit instead of U-Boot.

## ti-debpkgs

Adds the official Texas Instruments Debian package repository (`TexasInstruments/ti-debpkgs`) and installs the packages listed in `TI_PACKAGES`. Validates the APT suite against the repo's `dists` (via GitHub API), using `RELEASE` or the `TI_DEBPKGS_SUITE`/`TI_DEBPKGS_FALLBACK_SUITES` overrides, and installs an apt-preferences pin. Skips gracefully when no matching suite exists.

## u-boot-menu

Sets up a U-Boot extlinux boot menu on boards that support it. Installs the Debian/Ubuntu `u-boot-menu` package, writes `/etc/default/u-boot` (label, 10s timeout, FDT dir, cmdline from `${SRC_CMDLINE}`), then runs `u-boot-update` in the chroot to generate `extlinux.conf`. Honours `EXTLINUX_SPECIFIC_FDT` and `EXTLINUX_UINITRD`.

## uboot-binman-fix-pkg-resources

Patches U-Boot's `binman` tool (`tools/binman/control.py`) to use `importlib.resources` instead of `pkg_resources`, restoring build compatibility on hosts with `setuptools >= 82`, which removed `pkg_resources`. Runs only when `control.py` still imports `pkg_resources`, so it is a safe no-op on newer U-Boot. Covers v2024.x–v2025.04.

## uboot-btrfs

Enables Btrfs filesystem support in U-Boot by running `scripts/config --enable CONFIG_CMD_BTRFS` on the bootloader config during the `post_config_uboot_target` hook. This lets U-Boot read kernels and boot scripts from a Btrfs `/boot`. Enable it for boards using a Btrfs boot filesystem.

## uboot-fix-pylibfdt-swig

Fixes old U-Boot's `pylibfdt` failing to build against SWIG >= 4.3 (Debian trixie), which gave `SWIG_Python_AppendOutput()` a third argument. Rewrites the 2-arg calls to the version-agnostic `SWIG_AppendOutput()` macro in `libfdt.i`/`libfdt_wrap.c` under both pylibfdt paths. A safe no-op when the old call is absent; companion to `uboot-binman-fix-pkg-resources`.

## uefi-edk2-rk3588

Integrates edk2-porting UEFI/EDK2 firmware for Rockchip RK3588 boards, enabling `grub-with-dtb` and `initramfs-usb-gadget-ums`, forcing a GPT layout and `acpi=off`. Downloads the latest `edk2-porting/edk2-rk3588` release image and `dd`s it onto the loop device, then creates a `uboot` partition for SPL. Requires `UEFI_EDK2_BOARD_ID` to be set.

## ufs

Produces a UFS-sector-aligned image by setting `SECTOR_SIZE=4096` and appending a `-ufs` image suffix. Requires `sfdisk` >= 2.41 (util-linux), so the build host must be Debian Trixie (13) or newer; set `DOCKER_ARMBIAN_BASE_IMAGE=debian:trixie` when building in Docker. The version check is skipped unless actually building an image.

## uwe5622-allwinner

Enables the Spreadtrum UWE5622 (AW859A) WiFi/Bluetooth combo on Allwinner boards. Adds the `sprdbt_tty` module and `bluez`/`rfkill` packages, installs the `aw859a-wifi` and `aw859a-bluetooth` systemd services, and deploys the `hciattach_opi` blob for BT attach. Enable on sunxi boards carrying this chip.

## v4l2loopback-dkms

Builds the `v4l2loopback` virtual-camera kernel module via DKMS in the chroot, installing `v4l2loopback-dkms`, `v4l2loopback-utils`, and `v4l-utils`. Forces `INSTALL_HEADERS=yes` and requires a kernel with a working headers package. Skipped on minimal CLI images and on kernels 7.2 or newer, where the module no longer builds.

## vmware-vm

Builds a VMware-ready image by enabling the `image-output-ovf` extension (VMDK + OVF output) and installing `open-vm-tools` in the guest. On desktop builds it also adds `open-vm-tools-desktop` and the `xserver-xorg-video-vmware` driver for display integration. Enable it to run Armbian under VMware.

## watchdog

Installs the `watchdog` daemon package and configures it for hardware watchdog support. Uncomments `watchdog-device` in `/etc/watchdog.conf` so the daemon uses `/dev/watchdog` to reset a hung system. Enable it for boards with a hardware watchdog that should trigger automatic recovery on lockups.

## wayland-sessions-mask

Masks Wayland desktop session entries on boards with limited or unstable Wayland support due to GPU or driver constraints. Places empty marker files in `/usr/local/share/wayland-sessions/`, which overrides `/usr/share/wayland-sessions/`, in a desktop-agnostic, upgrade-safe way. Enable it via `enable_extension` in a board config; sessions stay enabled otherwise.

## xorg-lima-serverflags

Installs `40-serverflags.conf` into `/etc/X11/xorg.conf.d` to work around faulty GPU autodetection with the open-source Lima driver. Disables `AutoAddGPU`, enables the `dmabuf_capable` debug flag, and adds an `OutputClass` binding Rockchip to the `modesetting` driver with `glamor` acceleration as the primary GPU.

## yt6801

Installs the Motorcomm YT6801 Ethernet controller driver as a DKMS kernel module. Queries the GitHub API for the latest `amazingfate/yt6801-dkms` release, downloads its `.deb` into the chroot (via `ghproxy` when `GITHUB_MIRROR=ghproxy`) and installs it to build against the target kernel. Forces `INSTALL_HEADERS=yes`; needs a working headers package.

## zfs

Installs OpenZFS on the image by building the `zfs` kernel module through DKMS. Installs the `zfs-dkms` and `zfsutils-linux` packages in the chroot, forcing `INSTALL_HEADERS=yes` so the module can compile against the kernel headers. Skips itself when `KERNEL_HAS_WORKING_HEADERS` is not `yes`.
