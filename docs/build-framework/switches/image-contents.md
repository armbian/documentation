---
seo_title: "Armbian image contents build switches"
description: "Control what goes inside an Armbian image: networking stack, kernel headers, firmware, WiFi drivers, extensions and first-run behaviour."
---

# Contents

Control what lands inside the rootfs — firmware and kernel packages, the networking stack, extra drivers, extensions and first-run behaviour.

#### INSTALL_ARMBIAN_FIRMWARE

`string` · default: `yes`

Installs the `armbian-firmware` package, a curated collection of binary firmware blobs (Wi-Fi, Bluetooth, GPU and other peripherals) that many boards need to bring their hardware up. Left on by default; set `no` only for images where you supply firmware yourself or want the smallest possible rootfs.

#### BOARD_FIRMWARE_INSTALL

`string` · default: empty

Selects which firmware variant is installed. Empty installs the standard `armbian-firmware`; set to `-full` to install `armbian-firmware-full`, the much larger package covering a far wider range of devices — useful when one image has to support many different peripherals, at the cost of extra size.

#### INSTALL_HEADERS

`string`

- `yes`: pre-install kernel headers
- `no` (default)

Pre-installs the matching kernel headers into the image so that DKMS and other out-of-tree kernel modules can be compiled directly on the running board. Off by default because the headers add noticeable size; enable it when the board's users will build kernel modules themselves.

#### EXTRAWIFI

`yes` (default) | `no`

Builds and includes a set of out-of-tree Wi-Fi and Bluetooth adapter drivers that are not in the mainline kernel, covering many popular USB and SDIO chipsets. On by default; set `no` to build with in-kernel drivers only — for a leaner image, or when a mainline driver already covers your adapter. See the [driver list](https://github.com/armbian/build/blob/main/lib/functions/compilation/patch/drivers_network.sh).

#### BSPFREEZE

`string`

- `yes`: hold the Armbian board-support packages so they are not upgraded
- `no` (default)

Marks the Armbian board-support packages (U-Boot, kernel, DTB and the BSP metapackage) as held, so `apt upgrade` on the running system will not replace them. Use it to pin a known-good board-support stack — handy for reproducible or long-lived deployments where an unattended kernel or U-Boot bump would be disruptive.

#### SKIP_ARMBIAN_REPO

`string`

- `yes`
- `no` (default)

Builds the image without adding Armbian's apt repository, so the system sees only the base Debian/Ubuntu repositories. Suitable when developing a new release before its repository exists, or for custom images that must not pull packages from Armbian.

#### ARMBIAN_ZSH_SOURCE

`string` · default: `https://github.com/ohmyzsh/ohmyzsh`

Git repository that the `armbian-zsh` package fetches oh-my-zsh from. Override it to build against a fork or a local mirror — for example when building behind a firewall, or to pin a specific oh-my-zsh revision.

#### EXTRA_ROOTFS_NAME

`string` · default: empty

Appends a suffix to the cached root filesystem's name so a customised build gets its own cache entry instead of reusing — or overwriting — the standard one. Set it when your userpatches change the rootfs in a way the cache key would not otherwise capture, to avoid stale-cache surprises.

#### INCLUDE_HOME_DIR

`string`

- `yes`
- `no` (default)

Includes files placed under `/home` in the build tree in the final image, letting you bake user data or dotfiles into the rootfs. Off by default so that `/home` starts empty on a fresh image.

#### NETWORKING_STACK

`string`

- `network-manager`
- `systemd-networkd`
- `none` (to not-add any networking extensions)

Installs the desired networking stack. If the parameter is undefined, it sets `systemd-networkd` for minimal images (`BUILD_MINIMAL=yes`) and `network-manager` for the rest. Time synchronization is also changed accordingly: chrony is installed with network-manager, while systemd-timesyncd is used with systemd-networkd. In both cases, network settings are controlled through **Netplan**.

```sh
./compile.sh NETWORKING_STACK="network-manager"
```

#### NTP_SERVER

`string` · default: `pool.ntp.org`

NTP server used to synchronise the clock on the **build host** during preparation (via `ntpdate`); it does not change the time source in the finished image. Point it at an internal server when the default `pool.ntp.org` is unreachable on your network.

#### CONSOLE_AUTOLOGIN

`string`

- `yes` (default)
- `no`

Automatically logs in as root on the local serial/HDMI console at first boot, so a freshly flashed board is immediately usable without a keyboard-and-password step. Set `no` if your security threat model requires a login prompt on the physical console.

#### OPENSSHD_REGENERATE_HOST_KEYS

`boolean`

- `true` (default): armbian-firstrun deletes the shipped OpenSSH host keys and regenerates them
- `false`: keep the shipped keys untouched

Controls whether `armbian-firstrun` deletes the image's shipped OpenSSH host keys and regenerates fresh ones on first boot, so every device ends up with unique keys. Set `false` to keep the keys as-is — for example when cloud-init or another provisioning tool is responsible for setting them.

```sh
./compile.sh OPENSSHD_REGENERATE_HOST_KEYS=false
```

#### KEEP_ORIGINAL_OS_RELEASE

`string` · default: `no`

Keeps the base distribution's `/etc/os-release` instead of replacing it with Armbian's. By default Armbian overwrites the file so the system identifies itself as Armbian; set `yes` when software or tooling keys off the upstream Debian/Ubuntu identity.

#### ENABLE_EXTENSIONS

`comma-separated list`

[Extensions](/build-framework/extensions/) add optional functionality to a build without bloating the core — extra image formats, drivers, tooling and more. Pass a comma-separated list of extension names (the filenames under `extensions/`) to enable them for this build.

```sh
./compile.sh \
build \
BOARD=uefi-x86 \
BRANCH=current \
BUILD_DESKTOP=no \
BUILD_MINIMAL=no \
KERNEL_CONFIGURE=no \
RELEASE=noble \
ENABLE_EXTENSIONS=mesa-vpu,nvidia \
```
