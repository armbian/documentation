## User provided patches
You can add your own patches outside build script. Place your patches inside appropriate directory, for kernel or u-boot. There are no limitations except all patches must have file name extension `.patch`. User patches directory structure mirrors directory structure of `lib/patch`. Look for the hint at the beginning of patching process to select proper directory for patches. Example:

    [ o.k. ] Started patching process for [ kernel sunxi-dev 4.4.0-rc6 ]
    [ o.k. ] Looking for user patches in [ userpatches/kernel/sunxi-dev ]

Patch with same file name in `userpatches` directory tree substitutes one in `lib/patch`. To _replace_ a patch provided by Armbian maintainers, copy it from `lib/patch` to corresponding directory in `userpatches` and edit it to your needs. To _disable_ a patch, create empty file in corresponding directory in `userpatches`.

## User provided configuration
If file `userpatches/lib.config` exists, it will be called and can override the particular kernel and u-boot versions. It can also add additional packages to be installed, by adding to `PACKAGE_LIST_ADDITIONAL`. For a comprehensive list of available variables, look through  `lib/configuration.sh`. Some examples of what you can change:

    PACKAGE_LIST_ADDITIONAL="$PACKAGE_LIST_ADDITIONAL python-serial python" # additional packages
    ARMBIAN_MAINLINE_KERNEL_VERSION='4.8' # lock in a particular kernel version
    MAINLINE_UBOOT_BRANCH='tag:v2016.11'  # or u-boot version

## User provided kernel config
If file `userpatches/linux-$KERNELFAMILY-$KERNELBRANCH.config` exists, it will be used instead of default one from `lib/config`. Look for the hint at the beginning of kernel compilation process to select proper config file name. Example:

    [ o.k. ] Compiling dev kernel [ @host ]
    [ o.k. ] Using kernel config file [ lib/config/linux-sunxi-dev.config ]

## User provided sources config	
If file `userpatches/sources/$LINUXFAMILY.conf` exists, it will be used instead of default one from `lib/config`. Look for the hint at the beginning of compilation process to select proper config file name. Example:
	
	[ o.k. ] Adding user provided sun8i overrides
	
## User provided image customization script
You can run additional commands to customize created image. Edit file:

    userpatches/customize-image.sh

and place your code here. You may test values of variables noted in the file to use different commands for different configurations. Those commands will be executed in a chroot environment just before closing image.

To add files to image easily, put them in `userpatches/overlay` and access them in `/tmp/overlay` from `customize-image.sh`

## Partitioning of the SD card

In case you define `$FIXED_IMAGE_SIZE` at build time the partition containing the rootfs will be made of this size. Default behaviour when this is not defined and `$ROOTFS_TYPE` is set to _ext4_ is to shrink the partition to minimum size at build time and expand it to the card's maximum capacity at boot time (leaving an unpartitioned spare area of ~5% when the size is 4GB or less to help the SD card's controller with wear leveling and garbage collection on old/slow cards).

You can prevent the partition expansion from within `customize-image.sh` by a `touch /root/.no_rootfs_resize` or configure the resize operation by either a percentage or a sector count using `/root/.rootfs_resize` (`50%` will use only half of the card's size if the image size doesn't exceed this or `3887103s` for example will use sector 3887103 as partition end. Values without either `%` or `s` will be ignored)
