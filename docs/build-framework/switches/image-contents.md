---
seo_title: "Armbian image contents build switches"
description: "Control what goes inside an Armbian image: networking stack, kernel headers, firmware, WiFi drivers, extensions and first-run behaviour."
---

# Image contents

Control what lands inside the rootfs — firmware and kernel packages, the networking stack, extra drivers, extensions and first-run behaviour.

#### INSTALL_ARMBIAN_FIRMWARE

`string` · default: `yes`

Install the armbian-firmware package into the rootfs.

#### BOARD_FIRMWARE_INSTALL

`string` · default: empty

Set to `-full` to install the full firmware variant instead of the base one.

#### INSTALL_HEADERS

`string`

- `yes`: pre-install kernel headers
- `no`: (default)

#### EXTRAWIFI

`yes` (default) | `no`

Include several out-of-tree WiFi/BT adapter drivers. See the [driver list](https://github.com/armbian/build/blob/1914066729b7d0f4ae4463bba2491e3ec37fac84/lib/compilation-prepare.sh#L179-L507).

#### BSPFREEZE

`string`

- `yes`: freeze (from upgrade) armbian firmware packages when building images (U-Boot, kernel, DTB, BSP)
- `no`: (default)

#### SKIP_ARMBIAN_REPO

`string`

- `yes`
- `no`  (default)

Enforce building without Armbian repository. Suitable for developing new releases or making custom images that don't need Armbian repository.

#### ARMBIAN_ZSH_SOURCE

`string` · default: `https://github.com/ohmyzsh/ohmyzsh`

Git source repo for oh-my-zsh in the armbian-zsh package.

#### EXTRA_ROOTFS_NAME

`string` · default: empty

Suffix appended to the rootfs cache name to force a distinct cache variant.

#### INCLUDE_HOME_DIR

`string`

- `yes`
- `no` (default)

Include directories created inside /home in final image.

#### NETWORKING_STACK

`string`

- `network-manager`
- `systemd-networkd`
- `none` (to not-add any networking extensions)

Installs desired networking stack. If the parameter is undefined, it sets `systemd-networkd` for minimal images (BUILD_MINIMAL=yes) and `network-manager` for the rest. Time synchronization is also changed; chrony is installed with network-manager, while systemd-timesyncd is used with systemd-networkd. In both cases, we control network settings using **Netplan**.

!!! example "Build switch example"

```sh
./compile.sh NETWORKING_STACK="network-manager"
```

#### NTP_SERVER

`string` · default: `pool.ntp.org`

NTP server used by ntpdate during host prep.

#### CONSOLE_AUTOLOGIN

`string`

- `yes` (default)
- `no`

Automatically login as root for local consoles at first run. Disable if your security threat model requires.

#### OPENSSHD_REGENERATE_HOST_KEYS

`boolean`

  - false (skip armbian-firstrun's OpenSSH host keys deletion and regeneration (eg: to let cloud-init set the SSH host keys)
  - **true** (execute armbian-firstrun's OpenSSH host keys deletion + regeneration)

Manage OpenSSH host key regeneration at armbian-firstrun service.

Example:

```sh
./compile.sh OPENSSHD_REGENERATE_HOST_KEYS=false
```

#### KEEP_ORIGINAL_OS_RELEASE

`string` · default: `no`

Keep the distro's original `/etc/os-release` instead of overwriting it with Armbian's.

#### ENABLE_EXTENSIONS

`comma-separated list`

[Extensions](/build-framework/extensions/) allows to extend the Armbian build system without overloading the core with specific functionality. Extensions, stored in folder `extensions` are called

!!! example "Build switch example"

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
