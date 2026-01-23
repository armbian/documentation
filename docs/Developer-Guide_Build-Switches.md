# Build Switches

These parameters are meant to be applied to the `./compile.sh` command. They are **all** optional. They can also be added to your [build configuration file](Developer-Guide_Build-Preparation.md#providing-build-configuration) to save time. Default values are marked **bold** if applicable.

### User space

**BOARD** ( `string` )

Set the name of the board manually to skip the dialog prompt. Name of the board is [a filename without extension](https://github.com/armbian/build/tree/main/config/boards).

**BRANCH** ( `string` )

- `vendor`
- `legacy`
- `current` (recommended)
- `edge`

Set kernel and U-Boot branch manually to skip dialog prompt

!!! tip "Note"

    Some branches may not be available for all devices.

**RELEASE** ( `string` )

- `bookworm`
- `trixie`
- `sid`
- `jammy`
- `noble`

Set packages release base manually to skip dialog prompt. Check here for [currently available releases](https://github.com/armbian/build/tree/main/config/distributions).

!!! tip "Note"

    Only stable and/or LTS upstream Debian or Ubuntu releases are officially supported. Others might work or not.

**BUILD_MINIMAL** ( `string` )

- `yes`: build a bare CLI image suitable for application deployment. This option is **not compatible** with `BUILD_DESKTOP="yes"`
- `no`: (default)

**BSPFREEZE** ( `string` )

- `yes`: freeze (from upgrade) armbian firmware packages when building images (U-Boot, kernel, DTB, BSP)
- `no`: (default)

**INSTALL_HEADERS** ( `string` )

- `yes`: pre-install kernel headers
- `no`: (default)

<hr>

### Networking

**NETWORKING_STACK** ( `string` )

- `network-manager`
- `systemd-networkd`
- `none` (to not-add any networking extensions)

Installs desired networking stack. If the parameter is undefined, it sets `systemd-networkd` for minimal images (MINIMAL=yes) and `network-manager` for the rest. Time synchronization is also changed; chrony is installed with network-manager, while systemd-timesyncd is used with systemd-networkd. In both cases, we control network settings using **Netplan**.

!!! example "Build switch example"

```sh
./compile.sh NETWORKING_STACK="network-manager"
```

<hr>

### Host environment

**EXPERT** ( `string` )

- `yes`

Show development features and boards regardless of their support status in interactive mode.

**CLEAN_LEVEL** ( `comma-separated list` )

Defines what should be cleaned. Changing this option can be useful when rebuilding images or building more than one image

- `make-atf` = make clean for ATF, if it is built.
- `make-uboot` = make clean for uboot, if it is built.
- `make-kernel` = make clean for the kernel if it is built. very slow.<br>
- `debs`, `alldebs` = delete all packages in "./output/debs"
- `images` = delete "./output/images"
- `cache` = delete "./output/cache"
- `sources` = delete `cache/sources` (all downloaded sources)
- `oldcache` = remove old cached rootfs except for the newest 8 files
- `extras` = delete additional packages for the current release in `output/debs/extra`

**CARD_DEVICE** ( `string` )

- `/dev/sdX`

After successful compilation, do a verified burn of the image to the specified storage device (flash media / SD card).

**PREFER_DOCKER** ( `string` )
- `yes` (default)
- `no`

Docker assisted compilation is on by default. Set to `no` if you prefer running compilation natively.

**DOCKER_ARMBIAN_BASE_IMAGE** ( `string` )

- `ubuntu:jammy` (default)
- `ubuntu:noble`
- `debian:bookworm`

Defines the build host when using a Docker container (default). [Here](https://github.com/armbian/docker-armbian-build/pkgs/container/docker-armbian-build), you can see which other options are available.

- **CI** ( `string` )
  - true
  - **false**

If enabled (`true`), the Docker build container will receive Docker credentials from the host
(`${HOME}/.docker/config.json`) and the `OCI_TARGET_BASE` environment variable.

- **OCI_TARGET_BASE** ( `string` )
  - url/to/container_registry/path
  - **${GHCR_SOURCE}/armbian/\*** (GHCR_SOURCE is defined in `lib/functions/configuration/main-config.sh`)

Select the target for pull/push OCI cached images. If not set, default is used.

**GHCR_MIRROR_ADDRESS** ( `string` )

The default mirror address for ghcr.io, set by `GHCR_MIRROR=dockerproxy`, is ghcr.dockerproxy.com. When this address is unavailable, an alternative address can be set with `GHCR_MIRROR_ADDRESS`.

Example:

```sh
./compile.sh GHCR_MIRROR=dockerproxy GHCR_MIRROR_ADDRESS=ghcr.libcuda.so
```

**KERNEL_COMPILER** ( `string` )

The compiler used to compile the kernel. Usually, this option is set by the board config, but it can be set to `clang` to use LLVM to compile the kernel.

Example:

```sh
./compile.sh KERNEL_COMPILER=clang
```

**OPENSSHD_REGENERATE_HOST_KEYS** ( `boolean` )

  - false (skip armbian-firstrun's OpenSSH host keys deletion and regeneration (eg: to let cloud-init set the SSH host keys)
  - **true** (execute armbian-firstrun's OpenSSH host keys deletion + regeneration)

Manage OpenSSH host key regeneration at armbian-firstrun service.

Example:

```sh
./compile.sh OPENSSHD_REGENERATE_HOST_KEYS=false
```

<hr>

### Filesystem

**ROOTFS_TYPE** ( `string` )

- `ext4` (default)
- `f2fs`
- `btrfs`
- `nilfs2`
- `xfs`
- `nfs`

Create image with different root filesystems instead of default `ext4`. Requires setting `FIXED_IMAGE_SIZE` to something smaller than the size of your SD card for `F2FS`

**BTRFS_COMPRESSION** ( `string` )

- `lzo`
- `none`
- `zlib` (default)
- `zstd`

When choosing `ROOTFS_TYPE=btrfs`, select `btrfs` filesystem compression method and compression level. By default, the compression is `zlib`.

!!! tip "Note"

    The script does not check the legality of the input variable (compression ratio). Input like `zlib:1234` is legal to the script but illegal to the kernel. Beware that setting this option does affect image creation only (shrinking disk size) and will not adjust `/etc/fstab`, so it is up to the user to later edit `/etc/fstab` if compression in daily operation is also wanted (beware of severe performance penalties with random IO patterns and heavy compression algorithms!).

**BTRFS_ROOT_SUBVOLUME** ( `string` )

When using a BTRFS image as a file system, the volume `/` is placed on
btrfs subvolume `@`. The same subvolume is set as default for mounting without
specifying the `subvol=@` option at the time the image is mounted.

Using `BTRFS_ROOT_SUBVOLUME`, you can set a different name for the
root filesystem subvolume:

```sh
./compile.sh ROOTFS_TYPE=btrfs BTRFS_ROOT_SUBVOLUME=@root
```

**CRYPTROOT_ENABLE** ( `string` )

- yes
- no

LUKS (Linux Unified Key Setup) is a specification for block device encryption. It establishes an on-disk format for the data, as well as a passphrase/key management policy. LUKS uses the kernel device mapper subsystem via the dm-crypt module.

```title="When enabled, you need to provide additional information:"
CRYPTROOT_PASSPHRASE="MYSECRECTPASS"             # Mandatory
CRYPTROOT_AUTOUNLOCK="yes"                       # Default: no. If set to yes you can omit CRYPTROOT_PASSPHRASE to do unattended unlocking
CRYPTROOT_SSH_UNLOCK="yes"                       # Default: yes
CRYPTROOT_SSH_UNLOCK_PORT="2222"                 # Default: 2022
CRYPTROOT_MAPPER=armbian-root`                   # Default: armbian-root
CRYPTROOT_PARAMETERS="custom cryptsetup options" # Default: --pbkdf pbkdf2
```

!!! tip "Tips and warnings"

    - Private key can be placed in `$USERPATCHES_PATH/dropbear_authorized_keys` or they will be generated in `output/images/*.key` file
    - If you want to do the encryption part from scratch, check out [this](https://forum.armbian.com/topic/15618-full-root-filesystem%C2%A0encryption%C2%A0on-an-armbian-system-new-replaces-2017-tutorial-on-this-topic/) forum post.
    - This function might not work well with all distributions.
    - CRYPTROOT_MAPPER name might affect parallel image building
    - CRYPTROOT_PARAMETERS may not contain `=`; separate switches with spaces
    - CRYPTROOT_AUTOUNLOCK stores encryption key in the /etc/rootfs.key

<hr>

### Advanced

**INCLUDE_HOME_DIR** ( `string` )

- `yes`
- `no` (default)

Include directories created inside /home in final image.

**ENABLE_EXTENSIONS** ( `comma-separated list` )

[Extensions](/Developer-Guide_Extensions/) allows to extend the Armbian build system without overloading the core with specific functionality. Extensions, stored in folder `extensions` are called

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

**CONSOLE_AUTOLOGIN** ( `string` )

- `yes` (default)
- `no`

Automatically login as root for local consoles at first run. Disable if your security threat model requires.

**CPUTHREADS** ( `string` )

Allows the user to override CTHREADS if CPUTHREADS is defined and a valid positive integer.

If not defined, defaults to 150% the number of CPU Threads available to maximize compilation speed.

**USE_CCACHE** ( `string` )

- `yes`
- `no` (default)

Use a C compiler cache.  Generally not needed due to git-worktree .  Can slow performance on clean builds.

**PRIVATE_CCACHE** ( `string` )

- `yes`
- `no` (default)

Use `$DEST/ccache` as ccache home directory. Setting yes to this will enable CCACHE as well.

**KERNEL_BTF**

- `yes`
- `no`

Default is to auto-detect based on build host available RAM. If not enough RAM available, use =no to accept building without BTF debug information, or use =yes to force building with BTF even if low RAM. Family code can set this to opt-out of BTF. For more information on BTF see <https://docs.kernel.org/bpf/btf.html>

**ARTIFACT_IGNORE_CACHE** ( `string` )

- `yes`
- `no`  (default)

Enforce building from source instead of using pre-built artifacts.

**SKIP_ARMBIAN_REPO** ( `string` )

- `yes`
- `no`  (default)

Enforce building without Armbian repository. Suitable for developing new releases or making custom images that don't need Armbian repository.

**SECTOR_SIZE** ( `value` )
- `512` (default, for SD/EMMC/...)
- `4096` (for UFS, requires util-linux >2.41. Tested on Debian Trixie host)

Enforce sfdisk to align partition sector sizes.

**SHARE_LOG** ( `string` )

- `yes`
- `no` (default)

Automatically upload full build logs for debugging to one of Armbian's paste servers at the end of the build process.

Example:

```sh
./compile.sh SHARE_LOG=yes
```

**UBOOT_LOGLEVEL** ( `integer` )

- `0` to `9`: set U-Boot log verbosity level
- `6`: (default)

Controls the U-Boot bootloader log level during image building. Lower values produce less verbose output. This affects `CONFIG_LOGLEVEL` and `CONFIG_LOG_MAX_LEVEL` in U-Boot configuration.

# Build options below need to be retested and added above (COULD BE DEPRECATED)

:warning: DO NOT USE! Obsolete documentation, new documentation above is in progress.

- **KERNEL_KEEP_CONFIG** ( yes | no ):
  - yes: use kernel config file from previous compilation for the same branch, device family, and version
  - no: use default or user-provided config file
- **BUILD_DESKTOP** ( yes | no ):
  - yes: build an image with a minimal desktop environment
  - no: build image with console interface only
- **CREATE_PATCHES** ( yes | **no** ) :warning: **Warning:** This option is deprecated and may be removed in future releases - use the new `kernel-patch` / `uboot-patch` / `atf-patch` CLI commands instead.
  - yes: prompt right before the compilation starts to make changes to the source code for both U-Boot and kernel. From these changes, patch files will be created and placed in the `output` directory. If you want these patches included in a normal run (without CREATE_PATCHES to say), these files must be copied to the appropriate directories. Also, see [user-provided patches](https://docs.armbian.com/Developer-Guide_User-Configurations/#user-provided-patches).
- **EXT=rkdevflash** to flash Rockchip images to eMMC either during image build or separately with flash CLI command ([only works bare Linux, not Docker](https://github.com/armbian/build/pull/5058))

## Hidden options to minimize user input for build automation

- **ARMBIAN_CACHE_ROOTFS_PATH** ( `string` ): bind mount cache/rootfs to defined folder
- **ARMBIAN_CACHE_TOOLCHAIN_PATH** ( `string` ): bind mount cache/toolchain path to defined folder

## Hidden options for advanced users (default values are marked **bold**)

- **USERPATCHES_PATH** ( **userpatches/** ): set alternate path for the location of the `userpatches` folder
- **SKIP_EXTERNAL_TOOLCHAINS** ( yes | **no** ): don't download and use Linaro toolchains, by default placed in cache/toolchain (and configurable with **ARMBIAN_CACHE_TOOLCHAIN_PATH**)
- **PROGRESS_DISPLAY** ( none | **plain** | dialog ): way to display output of verbose processes - compilation, packaging, debootstrap
- **PROGRESS_LOG_TO_FILE** ( yes | **no** ): duplicate output, affected by the previous option, to log files `output/debug/*.log`
- **NO_APT_CACHER** ( **yes** | no ): disable usage of APT cache. Default `yes` in containers, but can be overridden
- **DISABLE_IPV6** ( **true** | false ): The distant future, the year Two-Thousand. Set false to allow Aria2c to use a modern ip protocol.
- **NO_HOST_RELEASE_CHECK** ( yes | **no** ): overrides the check for a supported host system
- **USE_MAINLINE_GOOGLE_MIRROR** ( yes | **no** ): use the `googlesource.com` mirror for downloading mainline kernel sources, which may be faster than `git.kernel.org` depending on your location
- **USE_GITHUB_UBOOT_MIRROR** ( yes | **no** ): use an unofficial GitHub mirror for downloading mainline U-Boot sources, may be faster than `git.denx.de` depending on your location
- **SYNC_CLOCK** ( **yes** | no ): sync system clock on builder before start image creation process
- **OFFLINE_WORK** ( yes | **no** ): skip downloading and updating sources and time and host check. Set to "yes," and you can collect packages without accessing the internet
- **FORCE_USE_RAMDISK** ( yes | no ): overrides autodetect for using tmpfs in new debootstrap and image creation process
- **FIXED_IMAGE_SIZE** ( `integer` ): create an image file of this size (in megabytes) instead of minimal
- **BOOTSIZE** ( `integer` **96** ): set size (in megabytes) for separate /boot filesystem. Used if **ROOTFS_TYPE** set to non-ext4
- **COMPRESS_OUTPUTIMAGE** (comma-separated list): create a compressed archive with an image file and GPG signature for redistribution
  - sha: generate SHA256 hash for image
  - gpg: sign image using gpg
  - xz: compress image only using xz format
    - **IMAGE_XZ_COMPRESSION_RATIO** ( 0 - **1** - 9 ) images compression levels when using xz compressor. Beware of memory consumption when going higher
  - zstd: compress image only using zstd format
    - **ZSTD_COMPRESSION_LEVEL** ( 1 - **9** - 19 ) images compression levels when using zstd compressor. Beware of memory consumption when going higher
- **SEVENZIP** ( yes | **no** ): create .7z archive with extreme compression ratio instead of .zip
- **BUILD_KSRC** ( **yes** | no ): create kernel source packages while building...
- **INSTALL_KSRC** ( yes | **no** ): ... and pre-install these kernel sources on the image
- **FORCE_BOOTSCRIPT_UPDATE** ( yes | no ):
  - yes: force bootscript to get updated during bsp package upgrade
- **NAMESERVER** ( `IPv4 address` ): the DNS resolver used inside the build chroot. Does not affect the final image. Default: `1.0.0.1`
- **DOWNLOAD_MIRROR** ( `china` | `bfsu` ): select download mirror for `toolchain` and `debian/ubuntu packages`
  - `china`: use `mirrors.tuna.tsinghua.edu.cn`; it will be very fast thanks to Tsinghua University
  - `bfsu`: use `mirrors.bfsu.edu.cn`, the mirror of Beijing Foreign Studies University
  - leave empty to use official source
- **LOCAL_MIRROR** (auto): override automated mirror selection, example 'LOCAL_MIRROR="<https://yourlocalmirror.com>"'
- **MANAGE_ACNG** ( `yes` | **`no`** | http URL ): configures use of `apt-cacher-ng`, a cache for debian/ubuntu/etc apt repositories.
  - `yes` sets up an automatically managed `apt-cacher-ng` instance on the build host. This mode is incompatible with container builds.
  - but you can provide a URL for a self-managed `apt-cacher-ng` instance, e.g. `"http://apt-cacher.example.com:3142"`
- **MAINLINE_MIRROR** ( `google` | `tuna` | `bfsu` ): select mainline mirror of `linux-stable.git`
  - `google`: use the mirror provided by Google, the same as `USE_MAINLINE_GOOGLE_MIRROR=yes`
  - `tuna`: use the mirror provided by Tsinghua University
  - `bfsu`: use the mirror provided by Beijing Foreign Studies University, which is similar to `tuna`
  - leave empty to use the official `git.kernel.org`, which may be very slow for mainland China users
- **UBOOT_MIRROR** （ `github` | `gitee` : select mainline mirror of `u-boot.git`
  - `github`: use the mirror provided by github, the same as `USE_GITHUB_UBOOT_MIRROR=yes`
  - `gitee`: use the mirror provided by Gitee, a Chinese git services
  - leave empty to use the official `source.denx.de`, which may be very slow for mainland China users
- **GITHUB_MIRROR** ( `fastgit` | `gitclone` | `cnpmjs` ): select download mirror for GitHub hosted repository
  - `fastgit`: use the mirror provided by fastgit.org
  - `gitclone`: use the mirror provided by gitclone.com
  - `cnpmjs`: use the mirror provided by cnpmjs.org
  - leave empty to connect directly to GitHub, which may be very slow for mainland China users
- **REGIONAL_MIRROR** ( `china` ): select mirrors based on regional setting, will not overwrite explicitly specified mirror option
  - `china`: MAINLINE_MIRROR=`tuna`, UBOOT_MIRROR=`gitee`, GITHUB_MIRROR=`fastgit`, DOWNLOAD_MIRROR=`china`
  - leave empty to use default settings
- **ROOT_FS_CREATE_ONLY** ( yes | **no** ): set to yes to force local cache creation
- **EXTRAWIFI** ( **yes** | no ): include several drivers for [WiFi adapters](https://github.com/armbian/build/blob/1914066729b7d0f4ae4463bba2491e3ec37fac84/lib/compilation-prepare.sh#L179-L507)
- **DISABLE_KERNEL_PATCHES** ( yes | **no** ): Disable all Armbian-specific kernel patches and build a vanilla kernel instead. Also disables `EXTRAWIFI`
- **DOCKER_NICE** ( `integer`, -20 to 19 ): automatically propagated from the initial `compile.sh`'s `nice` value.
- **LEGACY_DEBOOTSTRAP** ( yes | **no** ): if yes, use `debootstrap`, else use `mmdebstrap`
