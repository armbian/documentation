# User Configuration

## User provided patches

You can add your own patches outside the build script. Place your patches inside the appropriate directory, for kernel or u-boot. There are no limitations except that all patches must have the file name extension `.patch`. `userpatches` directory structure mirrors directory structure of `patch`. Look for the hint at the beginning of patching process to select the proper directory for patches. Example:

    [ o.k. ] Started patching process for [ kernel sunxi-edge 4.4.0-rc6 ]
    [ o.k. ] Looking for user patches in [ userpatches/kernel/sunxi-edge ]

Patches with the same file name and path in the `userpatches` directory tree override those in the `patch` directory. To _replace_ a patch provided by Armbian maintainers, copy it from `patch` to the corresponding directory in `userpatches` and edit it to your needs. To _disable_ a patch, create an empty file in the corresponding directory in `userpatches`.

## User provided configuration

A configuration file named `userpatches/config-<something>.conf.sh` (`.conf` also allowed) is a bash script that is sourced during the build if `./compile.sh something` is issued. All parameters which normally are passed via command line can be used (`PARAM1=value1` `PARAM2=value`) by using the same syntax, one separate line per `PARAM`. Command-line parameters still can override what is in the config file. More advanced use cases can use conditionals, define functions to implement hooks, source other/common config files, etc. A few, quite complex, examples can be found [here](https://github.com/lanefu/armbian-userpatches-example-indiedroid-nova).

## Legacy user provided configuration (deprecated, support for this will be removed at some point)

If the file `userpatches/lib.config` exists, it will be called and can override the particular kernel and u-boot versions. For a comprehensive list of available variables, look through  `lib/functions/configuration/main-config.sh`. Some examples of what you can change:

    [[ $LINUXFAMILY == sunxi64 && $BRANCH == edge ]] && BOOTBRANCH='tag:v2017.09' # conditionally change u-boot git branch/tag
    KERNELBRANCH="tag:v5.4.28" #always change to this kernel tag

## User provided kernel config

If the file `userpatches/linux-$LINUXFAMILY-$BRANCH.config` exists, it will be used instead of the default one from `config`. Look for the hint at the beginning of the kernel compilation process to select the proper config file name. Example:

    [ o.k. ] Compiling current kernel [ 5.10.47 ]
    [ o.k. ] Using kernel config provided by user [ userpatches/linux-rockchip64-current.config ]

## User provided sources config overrides

If file `userpatches/sources/$LINUXFAMILY.conf` exists, it will be used in addition to the default one from `config/sources`. Look for the hint at the beginning of the compilation process to select the proper config file name.
Please note that there are some exceptions for LINUXFAMILY like `sunxi` (32-bit mainline sunxi) and `sunxi64` (64-bit mainline sunxi)

Example:
	
	[ o.k. ] Adding user provided sunxi64 overrides
	
## User provided image customization script

You can run additional commands to customize the created image. Edit this file:

    userpatches/customize-image.sh

and place your code here. You may test the values of variables noted in the file to use different commands for different configurations. Those commands will be executed in a chroot environment just before finalizing the image.

To add files to the image easily, put them in `userpatches/overlay` and access them in `/tmp/overlay` from `customize-image.sh`

Be advised that even though you are compiling an image on an amd64 machine, any additional apt packages you configure or commands you run in customize-image.sh will be automatically installed/executed/virtualized for the architecture of the build target SBC.

## Partitioning of the SD card

In case you define `$FIXED_IMAGE_SIZE` at build time the partition containing the rootfs will be made of this size. Default behaviour when this is not defined is to shrink the partition to minimum size at build time and expand it to the card's maximum capacity at boot time (leaving an unpartitioned spare area of ~5% when the size is 4GB or less to help the SD card's controller with wear leveling and garbage collection on old/slow cards).

You can prevent the partition expansion from within `customize-image.sh` by a `touch /root/.no_rootfs_resize` or configure the resize operation by either a percentage or a sector count using `/root/.rootfs_resize` (`50%` will use only half of the card's size if the image size doesn't exceed this or `3887103s` for example will use sector 3887103 as partition end. Values without either `%` or `s` will be ignored).
