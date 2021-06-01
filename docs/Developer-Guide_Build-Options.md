# Build options

These parameters are meant to be applied to the `./compile.sh` command. They are **all** optional.  They can also be added to your [build configuration file](/Developer-Guide_Build-Preparation/#providing-build-configuration) to save time.

## Main options

- **KERNEL_ONLY** ( yes | no ):
    - yes: compiles only kernel, U-Boot and other packages for installation on existing Armbian system
    - no: build complete OS image for writing to SD card
    - leave empty to display selection dialog each time
- **KERNEL_CONFIGURE** ( yes | no ):
    - yes: Automatically call kernel's `make menuconfig` (add or remove modules or features)
    - no: Use provided kernel configuration provided by Armbian
    - leave empty to display selection dialog each time
- **CLEAN_LEVEL** (comma-separated list): defines what should be cleaned. Default value is `"make,debs"` - clean sources and remove all packages. Changing this option can be useful when rebuilding images or building more than one image
    - make: execute `make clean` for selected kernel and U-Boot sources
    - images: delete `output/images` (complete OS images)
    - debs: delete packages in `output/debs` for current branch and device family
    - alldebs: delete all packages in `output/debs`
    - cache: delete `cache/rootfs` (rootfs cache)
    - oldcache: remove old `cache/rootfs` except for the newest eight files
    - sources: delete `cache/sources` (all downloaded sources)
    - extras: delete additional packages for current release in `output/debs/extra`
- **REPOSITORY_INSTALL** (comma-separated list): list of core packages which will be installed from repository
    - Available options: `u-boot`, `kernel`, `bsp`, `armbian-config`, `armbian-firmware`
    - Set to "" to use packages one from local output or build if not available
- **KERNEL\_KEEP\_CONFIG** ( yes | no ):
    - yes: use kernel config file from previous compilation for the same branch, device family and version
    - no: use default or user-provided config file  
- **BUILD_MINIMAL** ( yes | no ):
    - yes: build bare CLI image suitable for application deployment. This option is **not compatible** with `BUILD_DESKTOP="yes"` and `BUILD_EXTERNAL="yes"`
    - no: default CLI package selection
- **BUILD_DESKTOP** ( yes | no ):
    - yes: build image with minimal desktop environment
    - no: build image with console interface only  
- **EXTERNAL** ( yes | no ):
    - yes: compile and install extra applications and firmware  
- **BSPFREEZE** ( yes | no ): 
    - yes: freeze (from update) armbian packages when building images (U-Boot, kernel, DTB)  
- **INSTALL_HEADERS** ( no | yes ):
    - yes: install kernel headers  
- **EXTERNAL_NEW** ( no | prebuilt | compile ):
    - prebuilt: install extra applications from repository
    - compile: compile extra applications in chroot  
- **CREATE_PATCHES** ( yes | no ):
    - yes: prompt right before the compilation starts to make changes to the source code, separate for U-Boot and kernel, and will create patch files out of this. If you want these patches are included in the normal run, you need to copy them to their appropriate directories.
    - no: will not do what is described above and simply builds without interruption   
- **BUILD_ALL** ( yes | no | demo ): cycle through all available board and kernel configurations and make images for all combinations  
- **LIB_TAG** ( master | "branchname" ):
    - set to `master` to compile from the master branch (default)
    - set to another "branchname" to compile from any other branch available. Check [here](https://github.com/armbian/build/branches) for available branches  
- **CARD_DEVICE** ( /dev/sdX ): set to the device of your SD card. The image will be burned and verified using Etcher for CLI.
- **CRYPTROOT_ENABLE** ( yes | no ): enable LUKS encrypted rootfs
    - `CRYPTROOT_PASSPHRASE="MYSECRECTPASS"` mandatory
    - `CRYPTROOT_SSH_UNLOCK=yes` Default: `yes`
    - `CRYPTROOT_SSH_UNLOCK_PORT=2222` Default: `2022`
    - `CRYPTROOT_PARAMETERS="custom cryptsetup options"` Default: `--pbkdf pbkdf2` (May not contain `=`; separate with spaces)
    - **Note:** This function might not work well with all distributions. Debian Buster and Stretch were tested. For building under Docker you have to use privileged mode which can be enable in `userpatches/config-docker`.
    - **Warning:** This feature was added as community contribution and mostly functional. Under some circumstances though the prompt will not be shown. Therefore it should be considered experimental. Check [here](https://github.com/armbian/build/commit/681e58b6689acda6a957e325f12e7b748faa8330) and [here](https://github.com/armbian/build/issues/1183)
    - **Hint:** If you want to do the encryption part from scratch check out [this](https://forum.armbian.com/topic/15618-full-root-filesystem%C2%A0encryption%C2%A0on-an-armbian-system-new-replaces-2017-tutorial-on-this-topic/) forum post.  
  
  
## Hidden options to minimize user input for build automation
- **BOARD** ( `string` ): set name of board manually to skip dialog prompt
- **BRANCH** ( `legacy` | `current` | `dev` ): set kernel and U-Boot branch manually to skip dialog prompt; some options may not be available for all devices
- **RELEASE** ( `stretch` | `buster` | `bullseye` | `bionic` | `focal` | `groovy` ): set OS release manually to skip dialog prompt; use this option with `KERNEL_ONLY=yes` to create board support package  
  
## Hidden options for advanced users (default values are marked **bold**)
- **EXPERT** ( yes | **no** ): Show development features in interactive mode
- **USERPATCHES_PATH** ( **userpatches/** ): set alternate path for location of `userpatches` folder
- **USE_CCACHE** ( **yes** | no ): use a C compiler cache to speed up the build process
- **PRIVATE_CCACHE** ( yes | **no** ) use `$DEST/ccache` as ccache home directory
- **PROGRESS_DISPLAY** ( none | **plain** | dialog ): way to display output of verbose processes - compilation, packaging, debootstrap
- **PROGRESS_LOG_TO_FILE** ( yes | **no** ): duplicate output, affected by previous option, to log files `output/debug/*.log`
- **USE_MAINLINE_GOOGLE_MIRROR** ( yes | **no** ): use `googlesource.com` mirror for downloading mainline kernel sources, may be faster than `git.kernel.org` depending on your location
- **USE_GITHUB_UBOOT_MIRROR** ( yes | **no** ): use unofficial Github mirror for downloading mainline U-Boot sources, may be faster than `git.denx.de` depending on your location
- **SYNC_CLOCK** ( **yes** | no ): sync system clock on builder before start image creation process
- **OFFLINE_WORK** ( yes | **no** ): skip downloading and updating sources as well as time and host check. Set to "yes" and you can collect packages without accessing the internet
- **FORCE_USE_RAMDISK** ( yes | no ): overrides autodetect for using tmpfs in new debootstrap and image creation process
- **FIXED_IMAGE_SIZE** ( `integer` ): create image file of this size (in megabytes) instead of minimal
- **BOOTSIZE** ( `integer` **96** ): set size (in megabytes) for separate /boot filesystem. Used if **ROOTFS_TYPE** set to non-ext4
- **COMPRESS_OUTPUTIMAGE** (comma-separated list): create compressed archive with image file and GPG signature for redistribution
    - sha: generate SHA256 hash for image
    - gpg: sign image using gpg
    - 7z: compress image, hash and signature to 7z archive
    - gz: compress image only using gz format
    - yes: compatibility shorcut for `sha,gpg,7z`
- **SEVENZIP** ( yes | **no** ): create .7z archive with extreme compression ratio instead of .zip
- **BUILD_KSRC** ( **yes** | no ): create kernel source packages while building...
- **INSTALL_KSRC** ( yes | **no** ): ... and pre-install these kernel sources on the image 
- **ROOTFS_TYPE** ( **ext4** | f2fs | btrfs | xfs | nfs | fel ): create image with different root filesystems instead of default `ext4`. Requires setting `FIXED_IMAGE_SIZE` to something smaller than the size of your SD card for `F2FS`
- **BTRFS_COMPRESSION** ( lzo | none | **zlib** | zstd ): when choosing `ROOTFS_TYPE=btrfs` select `btrfs` filesystem compression method and compression level. By default the compression is `zlib`.  
When selecting `zstd` or setting zlib compression level(`zlib:[1-9]`) user must ensure kernel version is **>=4.14.x**.  
When selecting zstd compression level (`zstd:[1-15]`) both the host and the target kernel version must be **>=5.1.x** since kernel started supporting zstd compression ratio only from 5.1 on.  
*Note:* The script does not check the legality of input variable (compression ratio). Input like `zlib:1234` is legal to the script but illegal to the kernel. Beware that setting this option does affect image creation only (shrinking disk size) and will not adjust `/etc/fstab` so it is up to the user to later edit `/etc/fstab` if compression in daily operation is also wanted (beware of serious performance penalties with random IO patterns and heavy compression algorithms!).
- **FORCE_BOOTSCRIPT_UPDATE** ( yes | no ): 
    - yes: force bootscript to get updated during bsp package upgrade
- **NAMESERVER** ( `IPv4 address` ): the DNS resolver used inside the build chroot. Does not affect the final image. Default: `1.0.0.1`
- **DOWNLOAD_MIRROR** ( `china` | `bfsu` ): select download mirror for `toolchain` and `debian/ubuntu packages`
	- `china`: use `mirrors.tuna.tsinghua.edu.cn`, it will be very fast thanks to Tsinghua University
	- `bfsu`: use `mirrors.bfsu.edu.cn`, mirror of Beijing Foreign Studies University  
	- leave empty to use official source
- **ARMBIAN_MIRROR** (auto): override automated mirror selection, example 'ARMBIAN_MIRROR="https://yourlocalmirror.com"'
- **MAINLINE_MIRROR** ( `google` | `tuna` | `bfsu` ): select mainline mirror of `linux-stable.git`
	- `google`: use mirror provided by Google, the same as `USE_MAINLINE_GOOGLE_MIRROR=yes`
	- `tuna`: use mirror provided by Tsinghua University
	- `bfsu`: use mirror provided by Beijing Foreign Studies University which is similar to `tuna`
	- leave empty to use offical `git.kernel.org`, may be very slow for mainland china users
- **USE_TORRENT** ( **yes** | no ): use torrent to download toolchains and rootfs
- **ROOT_FS_CREATE_ONLY** ( `FORCE` ): set to skip rootfs download and create locally
- **EXTRAWIFI** ( **yes** | no ): include several drivers for [WiFi adapters](https://github.com/armbian/build/blob/1914066729b7d0f4ae4463bba2491e3ec37fac84/lib/compilation-prepare.sh#L179-L507)
- **WIREGUARD** ( **yes** | no ): include Wireguard for kernels before it got upstreamed to mainline. Will lose functionality soon.
- **AUFS** ( **yes** | no ): Include support for [AUFS](https://en.wikipedia.org/wiki/Aufs)
