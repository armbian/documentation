# Build commands

### kernel

Builds kernel and device tree (where applicable) and places it to the `output/debs`

Usage:
```bash
./compile.sh kernel BOARD=nanopi-r5c BRANCH=edge 
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

Sets `TARGETS_FILE` to something that doesn't exist, so the `default-targets.yaml` is used (so same list for everyone, save for userpatched-boards)

Usage:
```bash
./compile.sh inventory-boards
```
Outputs /info/boards-inventory.csv

### kernel-dtb

Builds only DTB and outputs full preprocessed dts source

Outputs preprocessed DTS source for the board in question to `output/`
also outputs the same preprocessed DTS source, ran through `dtc` with input and output DTS formats for "normalized" comparisons

Usage:
```bash
./compile.sh kernel-dtb BOARD=xxxxx BRANCH=edge
```

### rewrite-uboot-patches

Prepares git, applies patches to git, and rewrites them back from git
same as kernel, it does git archeology for mbox-less patches, etc.

- uboot-patches-to-git alias is also added, but my guess is that the rewrite is more useful.
- refactor a common config function for both kernel and uboot.

Usage:
```bash
./compile.sh rewrite-uboot-patches BOARD=xxxx BRANCH=edge 
```

### targets

Generates output/info/git_sources.json file containing URL, branch, and commit hash combo.

The easiest way to generate file for all devices is to run `./compile.sh targets`. Then, at the time of release, we will copy the output/info/git_sources.json file to config/sources/git_sources.json. Once the file is copied, the hash information from the file will be used to fetch resources for git repositories where branches are specified instead of tags or commits.

Usage:
```bash
./compile.sh targets
```

# Build options

These parameters are meant to be applied to the `./compile.sh` command. They are **all** optional.  They can also be added to your [build configuration file](Developer-Guide_Build-Preparation.md#providing-build-configuration) to save time. Default values are marked **bold** if applicable. 

## Main options

- **NETWORKING_STACK** ( string )
    - network-manager
    - systemd-networkd
    - none (to not-add any networking extensions)

Installs desired networking stack. If the parameter is undefined, it sets `systemd-networkd` for minimal images (MINIMAL=yes) and `network-manager` for the rest. Time synchronization is also changed; chrony is installed with network-manager, while systemd-timesyncd is used with systemd-networkd. In both cases, we control network settings using **Netplan**.

- **DOCKER_ARMBIAN_BASE_IMAGE** ( string )
    - **ubuntu:jammy**
    - ubuntu:noble
    - debian:bookworm

Defines the build host when using a Docker container (default). [Here](https://github.com/armbian/docker-armbian-build/pkgs/container/docker-armbian-build), you can see which other options are available.

- **CI** ( string )
  - true
  - **false**

If enabled (`true`), the Docker build container will receive Docker credentials from the host 
(`${HOME}/.docker/config.json`) and the `OCI_TARGET_BASE` environment variable.

- **OCI_TARGET_BASE** ( string )
  - url/to/container_registry/path
  - **${GHCR_SOURCE}/armbian/*** (GHCR_SOURCE is defined in `lib/functions/configuration/main-config.sh`)

Select the target for pull/push OCI cached images. If not set, default is used.

- **GHCR_MIRROR_ADDRESS** (string)

The default mirror address for ghcr.io, set by `GHCR_MIRROR=dockerproxy`, is ghcr.dockerproxy.com. When this address is unavailable, an alternative address can be set with `GHCR_MIRROR_ADDRESS`.

Example:
```
./compile.sh GHCR_MIRROR=dockerproxy GHCR_MIRROR_ADDRESS=ghcr.libcuda.so
```

- **KERNEL_COMPILER** (string)

The compiler used to compile the kernel. Usually, this option is set by the board config, but it can be set to `clang` to use LLVM to compile the kernel.

Example:
```
./compile.sh KERNEL_COMPILER=clang
```  

- **OPENSSHD_REGENERATE_HOST_KEYS** (boolean)
    - false (skip armbian-firstrun's OpenSSH host keys deletion and regeneration (eg: to let cloud-init set the SSH host keys)
    - **true** (execute armbian-firstrun's OpenSSH host keys deletion + regeneration)

Manage OpenSSH host key regeneration at armbian-firstrun service. 

Example:
```
./compile.sh OPENSSHD_REGENERATE_HOST_KEYS=false
```  

# Build options below need to be retested and added above (COULD BE DEPRECATED)

:warning: DO NOT USE! Obsolete documentation, new documentation in progress. 

- **BUILD_ONLY** (comma-separated list): defines what artifacts should be built. The default value is an empty string - it will build all artifacts. Changing this option can be useful to build partial artifacts only.
    - u-boot: build U-Boot
    - kernel: build kernel
    - armbian-config: build Armbian config
    - armbian-zsh: build Armbian zsh
    - plymouth-theme-armbian: build Armbian Plymouth theme
    - armbian-firmware: build Armbian firmware
    - armbian-bsp: build Armbian board support package
    - chroot: build additional packages
    - bootstrap: build bootstrap package
    - default: build full OS image for flashing
- **KERNEL_CONFIGURE** ( string or boolean ):
    - prebuilt: use precompiled packages (only for maintained hardware)
    - yes: automatically call kernel's `make menuconfig` (add or remove modules or features)
    - no: use provided kernel configuration provided by Armbian
    - leave empty to display the selection dialog each time
- **CLEAN_LEVEL** (comma-separated list): defines what should be cleaned. Default value is `"make,debs"` - clean sources and remove all packages. Changing this option can be useful when rebuilding images or building more than one image
    - make-atf = make clean for ATF, if it is built.
    - make-uboot = make clean for uboot, if it is built.
    - make-kernel = make clean for the kernel if it is built. very slow.<br>
      *important*: "make" by itself has been disabled since Armbian now knows how to handle Make timestamping.      
    - debs, alldebs = delete all packages in "./output/debs"
    - images = delete "./output/images"
    - cache = delete "./output/cache"
    - sources: delete `cache/sources` (all downloaded sources)
    - oldcache = remove old cached rootfs except for the newest 8 files
    - extras: delete additional packages for the current release in `output/debs/extra`
- **REPOSITORY_INSTALL** (comma-separated list): list of core packages that will be installed from the repository
    - Available options: `u-boot`, `kernel`, `bsp`, `armbian-bsp-cli`,`armbian-bsp-desktop`,`armbian-desktop`,`armbian-config`, `armbian-firmware`
    - Set to "" to use packages one from local output or build if not available
- **KERNEL\_KEEP\_CONFIG** ( yes | no ):
    - yes: use kernel config file from previous compilation for the same branch, device family, and version
    - no: use default or user-provided config file  
- **BUILD_MINIMAL** ( yes | no ):
    - yes: build a bare CLI image suitable for application deployment. This option is **not compatible** with `BUILD_DESKTOP="yes"` and `BUILD_EXTERNAL="yes"`
    - no: default CLI package selection
- **BUILD_DESKTOP** ( yes | no ):
    - yes: build an image with a minimal desktop environment
    - no: build image with console interface only  
- **EXTERNAL** ( yes | no ):
    - yes: compile and install extra applications and firmware  
- **BSPFREEZE** ( yes | no ): 
    - yes: freeze (from update) armbian packages when building images (U-Boot, kernel, DTB)  
- **INSTALL_HEADERS** ( **no** | yes ):
    - yes: install kernel headers  
- **EXTERNAL_NEW** ( no | prebuilt | compile ):
    - prebuilt: install extra applications from the repository
    - compile: compile extra applications in chroot  
- **CREATE_PATCHES** ( yes | **no** ) :warning: **Warning:** This option is deprecated and may be removed in future releases - use the new `kernel-patch` / `uboot-patch` / `atf-patch` CLI commands instead.
    - yes: prompt right before the compilation starts to make changes to the source code for both U-Boot and kernel. From these changes, patch files will be created and placed in the `output` directory. If you want these patches included in a normal run (without CREATE_PATCHES to say), these files must be copied to the appropriate directories. Also, see [user-provided patches](https://docs.armbian.com/Developer-Guide_User-Configurations/#user-provided-patches).
- **BUILD_ALL** ( yes | no | demo ): cycle through all available board and kernel configurations and make images for all combinations  
- **CARD_DEVICE** ( /dev/sdX ): set to the device of your SD card. The image will be burned and verified using Etcher for CLI.
- **EXT=rkdevflash** to flash Rockchip images to eMMC either during image build or separately with flash CLI command ([only works bare Linux, not Docker](https://github.com/armbian/build/pull/5058))
- **CRYPTROOT_ENABLE** ( yes | no ): enable LUKS encrypted rootfs
    - `CRYPTROOT_PASSPHRASE="MYSECRECTPASS"` mandatory
    - `CRYPTROOT_SSH_UNLOCK=yes` Default: `yes`
    - **Hint:** Private key can be placed in `$USERPATCHES_PATH/dropbear_authorized_keys` or they will be generated in `output/images/*.key` file
    - `CRYPTROOT_SSH_UNLOCK_PORT=2222` Default: `2022`
    - `CRYPTROOT_MAPPER=armbian-root` Default: `armbian-root`
    - **Note:** Cryptsetup root mapper name
    - **Hint:** Can be helpful for parallel image building
    - `CRYPTROOT_PARAMETERS="custom cryptsetup options"` Default: `--pbkdf pbkdf2` (May not contain `=`; separate with spaces)
    - **Note:** This function might not work well with all distributions. Debian Buster and Stretch were tested. For building under Docker, you have to use privileged mode, which can be enabled in `userpatches/config-docker`.
    - **Warning:** This feature was added as a community contribution and is mostly functional. Under some circumstances, though, the prompt will not be shown. Therefore, it should be considered experimental. Check [here](https://github.com/armbian/build/commit/681e58b6689acda6a957e325f12e7b748faa8330) and [here](https://github.com/armbian/build/issues/1183)
    - **Hint:** If you want to do the encryption part from scratch, check out [this](https://forum.armbian.com/topic/15618-full-root-filesystem%C2%A0encryption%C2%A0on-an-armbian-system-new-replaces-2017-tutorial-on-this-topic/) forum post.  
  
  
## Hidden options to minimize user input for build automation
- **BOARD** ( `string` ): set the name of the board manually to skip the dialog prompt
- **BRANCH** ( `legacy` | `current` | `edge` ): set kernel and U-Boot branch manually to skip dialog prompt; some options may not be available for all devices
- **RELEASE** ( `bullseye` | `bookworm` | `jammy` ): set OS release manually to skip dialog prompt; use this option with `KERNEL_ONLY=yes` to create board support package
- **ARMBIAN_CACHE_ROOTFS_PATH** ( `string` ): bind mount cache/rootfs to defined folder
- **ARMBIAN_CACHE_TOOLCHAIN_PATH** ( `string` ): bind mount cache/toolchain path to defined folder
  
## Hidden options for advanced users (default values are marked **bold**)
- **EXPERT** ( yes | **no** ): show development features and boards regardless of their status in interactive mode
- **USERPATCHES_PATH** ( **userpatches/** ): set alternate path for the location of the `userpatches` folder
- **USE_CCACHE** ( **yes** | no ): use a C compiler cache to speed up the build process
- **PRIVATE_CCACHE** ( yes | **no** ): use `$DEST/ccache` as ccache home directory
- **SKIP_EXTERNAL_TOOLCHAINS** ( yes | **no** ): don't download and use Linaro toolchains, by default placed in cache/toolchain (and configurable with **ARMBIAN_CACHE_TOOLCHAIN_PATH**)
- **PROGRESS_DISPLAY** ( none | **plain** | dialog ): way to display output of verbose processes - compilation, packaging, debootstrap
- **PROGRESS_LOG_TO_FILE** ( yes | **no** ): duplicate output, affected by the previous option, to log files `output/debug/*.log`
- **NO_APT_CACHER** ( **yes** | no ): disable usage of APT cache. Default `yes` in containers, but can be overridden
- **DISABLE_IPV6** ( **true** | false ): The distant future, the year Two-Thousand.  Set false to allow Aria2c to use a modern ip protocol.
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
    - 7z: compress image, hash, and signature to 7z archive
    - gz: compress image only using gz format
    - xz: compress image only using xz format
    - yes: compatibility shortcut for `sha,gpg,7z`
- **IMAGE_XZ_COMPRESSION_RATIO** ( **1** - 9 ) images compression levels when using xz compressor. Beware of memory consumption when going higher
- **SEVENZIP** ( yes | **no** ): create .7z archive with extreme compression ratio instead of .zip
- **BUILD_KSRC** ( **yes** | no ): create kernel source packages while building...
- **INSTALL_KSRC** ( yes | **no** ): ... and pre-install these kernel sources on the image 
- **ROOTFS_TYPE** ( **ext4** | f2fs | btrfs | nilfs2 | xfs | nfs ): create image with different root filesystems instead of default `ext4`. Requires setting `FIXED_IMAGE_SIZE` to something smaller than the size of your SD card for `F2FS`
- **BTRFS_COMPRESSION** ( lzo | none | **zlib** | zstd ): when choosing `ROOTFS_TYPE=btrfs`, select `btrfs` filesystem compression method and compression level. By default, the compression is `zlib`.  
When selecting `zstd` or setting zlib compression level(`zlib:[1-9]`) user must ensure kernel version is **>=4.14.x**.  
When selecting the zstd compression level (`zstd:[1-15]`), both the host and the target kernel version must be **>=5.1.x** since the kernel started supporting the zstd compression ratio only from 5.1 on.  
*Note:* The script does not check the legality of the input variable (compression ratio). Input like `zlib:1234` is legal to the script but illegal to the kernel. Beware that setting this option does affect image creation only (shrinking disk size) and will not adjust `/etc/fstab`, so it is up to the user to later edit `/etc/fstab` if compression in daily operation is also wanted (beware of severe performance penalties with random IO patterns and heavy compression algorithms!).
- **FORCE_BOOTSCRIPT_UPDATE** ( yes | no ): 
    - yes: force bootscript to get updated during bsp package upgrade
- **NAMESERVER** ( `IPv4 address` ): the DNS resolver used inside the build chroot. Does not affect the final image. Default: `1.0.0.1`
- **DOWNLOAD_MIRROR** ( `china` | `bfsu` ): select download mirror for `toolchain` and `debian/ubuntu packages`
	- `china`: use `mirrors.tuna.tsinghua.edu.cn`; it will be very fast thanks to Tsinghua University
	- `bfsu`: use `mirrors.bfsu.edu.cn`, the mirror of Beijing Foreign Studies University  
	- leave empty to use official source
- **ARMBIAN_MIRROR** (auto): override automated mirror selection, example 'ARMBIAN_MIRROR="https://yourlocalmirror.com"'
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
- **USE_TORRENT** ( yes | **no** ): use torrent to download toolchains and rootfs
- **ROOT_FS_CREATE_ONLY** ( yes | **no** ): set to yes to force local cache creation
- **EXTRAWIFI** ( **yes** | no ): include several drivers for [WiFi adapters](https://github.com/armbian/build/blob/1914066729b7d0f4ae4463bba2491e3ec37fac84/lib/compilation-prepare.sh#L179-L507)
- **WIREGUARD** ( **yes** | no ): include Wireguard for kernels before it got upstreamed to mainline. Will lose functionality soon.
- **AUFS** ( **yes** | no ): include support for [AUFS](https://en.wikipedia.org/wiki/Aufs)
- **SKIP_BOOTSPLASH** ( yes | **no** ): use kernel bootsplash. Disable in case of troubles
- **CONSOLE_AUTOLOGIN** ( **yes** | no ): automatically login as root for local consoles. Disable if your security threat model requires.
- **EXT** (`fake-vcgencmd`): execute [extension](Developer-Guide_Extensions.md) during the build
	- `fake-vcgencmd`: include [fake vcgencmd](https://github.com/clach04/fake_vcgencmd) to monitor and control boards from [Android](https://eidottermihi.github.io/rpicheck/)
- **INCLUDE_HOME_DIR** ( yes | **no** ): include directories created inside /home in final image.
