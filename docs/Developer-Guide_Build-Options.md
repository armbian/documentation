- **KERNEL_ONLY** (yes&#124;no):
    - leave empty to display selection dialog each time
    - set to "yes" to compile only kernel, u-boot and other packages for installing on existing Armbian system
    - set to "no" to build complete OS image for writing to SD card
- **KERNEL_CONFIGURE** (yes&#124;no):
    - leave empty to display selection dialog each time
    - set to "yes" to configure kernel (add or remove modules or features). Kernel configuration menu will be brought up before compilation
    - set to "no" to compile kernel without changing default or custom provided configuration
- **CLEAN_LEVEL** (comma-separated list): defines what should be cleaned. Default value is `"make,debs"` - clean sources and remove all packages. Changing this option can be useful when rebuilding images or building more than one image
    - "make" = execute `make clean` for selected kernel and u-boot sources,
	- "images" = delete `output/images` (complete OS images),
	- "debs" = delete packages in `output/debs` for current branch and device family,
	- "alldebs" = delete all packages in `output/debs`,
	- "cache" = delete `cache/rootfs` (rootfs cache),
	- "oldcache" = remove old `cache/rootfs` except for the newest 8 files,
	- "sources" = delete `cache/sources` (all downloaded sources),
	- "extras" = delete additional packages for current release in `output/debs/extra`
- **KERNEL\_KEEP\_CONFIG** (yes&#124;no):
    - set to "yes" to use kernel config file from previous compilation for the same branch, device family and version
    - set to "no" to use default or user-provided config file
- **BUILD_MINIMAL** (yes&#124;no):
    - set to "yes" to build bare CLI image suitable for application deployment.	This option is not compatible with BUILD_DESKTOP="yes" and BUILD_EXTERNAL="yes"
- **BUILD_DESKTOP** (yes&#124;no):
    - set to "yes" to build image with minimal desktop environment
    - set to "no" to build image with console interface only
- **EXTERNAL** (yes&#124;no):
    - set to "yes" to compile and install extra applications and firmware
- **BSPFREEZE** (no&#124;yes): freeze (from update) armbian packages when building images (u-boot, kernel, dtb)
- **INSTALL_HEADERS** (no&#124;yes): install kernel headers package
- **EXTERNAL_NEW** (no&#124;prebuilt&#124;compile):
	- set to "prebuilt" to install extra applications from repository
	- set to "compile" to compile extra applications in chroot
- **CREATE_PATCHES** (yes&#124;no):
	- set to "yes" will prompt you right before the compilation starts to make changes to the source code. Separate for u-boot and kernel. It will also create a patch out of this. If you want that this patch is included in the normal run, you need to copy it to appropriate directory
	- set to "no" compilation will run uninterrupted
- **BUILD_ALL** (yes&#124;no&#124;demo): cycle through all available board and kernel configurations and make images for all combinations
- **LIB_TAG** (master&#124;"branchname"):
	- set to "master" to compile from the master branch (default)
	- set to "branchname" to compile from any other branch available ("next" & "second" are deprecated and **not** recommended to use).
- **CARD_DEVICE** (/dev/sdx) set to the device of your SD card. The image will be burned and verified using Etcher for CLI.
- **CRYPTROOT_ENABLE** (yes&#124;no): set to enable LUKS encrypted rootfs. You must also provide unlock password CRYPTROOT_PASSPHRASE="MYSECRECTPASS" and optional CRYPTROOT_SSH_UNLOCK=yes CRYPTROOT_SSH_UNLOCK_PORT=2222 CRYPTROOT_PARAMETERS="custom cryptsetup options" Function might not work well with all distributions. Debian Buster and Stretch were tested. For building under the Docker you have to use privilege mode which can be enable in userpatches/config-docker.	

More info:

[1] https://github.com/armbian/build/commit/681e58b6689acda6a957e325f12e7b748faa8330

[2] https://github.com/armbian/build/issues/1183

### Hidden options to minimize user input for build automation:
- **BOARD** (string): you can set name of board manually to skip dialog prompt
- **BRANCH** (legacy&#124;current&#124;dev): you can set kernel and u-boot branch manually to skip dialog prompt; some options may not be available for all devices
- **RELEASE** (stretch&#124;jessie&#124;bionic&#124;xenial): you can set OS release manually to skip dialog prompt; use this option with `KERNEL_ONLY=yes` to create board support package

### Hidden options for advanced users (default values are marked **bold**):
- **USERPATCHES_PATH** (**userpatches/**): set alternate path for location of `userpatches` folder
- **USE_CCACHE** (**yes**&#124;no): use a C compiler cache to speed up the build process
- **PRIVATE_CCACHE** (yes&#124;**no**) use `$DEST/ccache` as ccache home directory
- **PROGRESS_DISPLAY** (none&#124;**plain**&#124;dialog): way to display output of verbose processes - compilation, packaging, debootstrap
- **PROGRESS_LOG_TO_FILE** (yes&#124;**no**): duplicate output, affected by previous option, to log files `output/debug/*.log`
- **USE_MAINLINE_GOOGLE_MIRROR** (yes&#124;**no**): use `googlesource.com` mirror for downloading mainline kernel sources, may be faster than `git.kernel.org` depending on your location
- **USE_GITHUB_UBOOT_MIRROR** (yes&#124;**no**): use unofficial Github mirror for downloading mainline u-boot sources, may be faster than `git.denx.de` depending on your location
- **IGNORE_UPDATES** (yes&#124;**no**): skip downloading and updating sources
- **FORCE_USE_RAMDISK** (yes&#124;no): overrides autodetect for using tmpfs in new debootstrap and image creation process
- **FIXED_IMAGE_SIZE** (integer): create image file of this size (in megabytes) instead of minimal
- **COMPRESS_OUTPUTIMAGE** (comma-separated list): create compressed archive with image file and GPG signature for redistribution
	- *sha* - generate SHA256 hash for image,
	- *gpg* - sign image using gpg,
	- *7z* - compress image, hash and signature to 7z archive,
	- *gz* - compress image only using gz format,
	- *yes* - compatibility shorcut for sha,gpg,7z.
- **SEVENZIP** (yes&#124;**no**): create .7z archive with extreme compression ratio instead of .zip
- **BUILD_KSRC** (**yes**&#124;no): create kernel source packages 
- **ROOTFS_TYPE** (**ext4**&#124;f2fs&#124;btrfs&#124;nfs&#124;fel): create image with different root filesystems instead of default ext4. Requires setting `FIXED_IMAGE_SIZE` to something smaller than the size of your SD card for F2FS
- **BTRFS_COMPRESSION** (**lzo**|zlib:3|zstd) select btrfs filesystem compression method and compression level. By default the compression is `lzo`, user must ensure kernel version is above `4.14` when selecting `zstd` or setting zlib compression level(`zlib:[1-9]`). Both the host and the target kernel version must above `5.1` when selecting zstd compression level (`zstd:[1-15]`), since kernel start supporting zstd compression ratio from `5.1`. The script does not check the legality of input variable(compression ratio), input like `zlib:1234` is legal to script, but illegal to kernel. When using microsd card, `zstd` is preferred because of the poor 4k I/O performance of microsd card.
- **FORCE_CHECKOUT** (yes&#124;no): set to "no" to skip forced sources checkout and patching
- **FORCE_BOOTSCRIPT_UPDATE** (yes&#124;no): set to "yes" to force bootscript to get updated during bsp package upgrade
- **NAMESERVER** (ipv4 address): the DNS resolver used inside the build chroot. Does not affect the final image. Default: 1.0.0.1
- **DOWNLOAD_MIRROR** select download mirror for `toolchain` and `debian/ubuntu packages`.
	- set to `china` to use `mirrors.tuna.tsinghua.edu.cn`, it will be very fast thanks to tsinghua university.
	- leave it empty to use official source.
- **MAINLINE_MIRROR** select mainline mirror of `linux-stable.git`
	- set to `google` to use mirror provided by Google, the same as `USE_MAINLINE_GOOGLE_MIRROR=yes`.
	- set to `tuna` to use mirror provided by tsinghua university.
	- leave it empty to use offical `git.kernel.org`, it may be very slow for mainland china users.
- **USE_TORRENT** (**yes**&#124;no): use torrent to download toolchains and rootfs
- **ROOT_FS_CREATE_ONLY** set to `FORCE` to skip rootfs download and create locally
