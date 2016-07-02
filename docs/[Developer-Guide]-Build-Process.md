# What is behind the build process?

Build process summary:

- creates development environment on the top of X86/AMD64 Ubuntu 14.04 LTS,
- downloads proven sources, applies patches and uses tested configurations,
- cross-compiles universal boot loader (u-boot), kernel and other tools and drivers,
- packs kernel, uboot, dtb and root customizations into debs,
- debootstraps minimalistic Debian Wheezy, Jessie and Ubuntu Trusty into SD card image,
- installs additional packets, applies customizations and shrinks image to its actual size.

Check this image [compiling example](https://youtu.be/zeShf12MNLg) with partial cache.

## Creating compile environment ##

At first run we are downloading all necessary dependencies. 

## Using board configuration ##

We need to get some predefined variables about selected board. Which kernel & uboot source to use, modules to load, which is the build number, do we need to have a single partition or dual with boot on fat, which extra drivers to compile out of the kernel tree, ...

**Board configuration example:**
    
	BOOTSIZE="16"											# FAT boot partition in MB, 0 for none
	BOOTCONFIG="udoo_neo_config"							# Which compile config to use		
	LINUXFAMILY="udoo"										# boards share kernel

Note that in this case, all main config options (kernel and uboot source) are covered within FAMILY. Check [configuration.sh](https://github.com/igorpecovnik/lib/blob/master/configuration.sh) for more config options.

This **isn't ment to be user configurable** but you can alter variables if you know what you are doing.

## Downloading sources ##

When we know where are the sources and where they need to be the download / update process starts. This might take from several minutes to several hours.

## Patching ##

In patching process we are appling patches to sources. The process is defined in:

	lib/patch/kernel/sun7i-default
	lib/patch/kernel/sunxi-dev	
	...
	lib/patch/u-boot/u-boot-default
	lib/patch/u-boot/u-boot-neo-default
	...

Patch rules for subdirectories are: **KERNEL_FAMILY-BRANCH** for kernel and **U-BOOT-SOURCE-BRANCH** for U-boot.

## Debootstrap ##

Debootstrap creates fresh Debian / Ubuntu root filesystem templates or use cached under:

	output/cache/rootfs/$DISTRIBUTION.tgz

To recreate those files you need to remove them manually. 

## Kernel install ##

When root filesystem is ready we need to install kernel image with modules, board definitions, firmwares. Along with this we set the CPU frequency min/max, hostname, modules, network interfaces templates. Here is also the place to install headers and fix + native compile them on the way.

## Distribution fixes ##

Each distributin has it's own way of doing things:

- serial console
- different packets
- configuration locations

## Board fixes ##

Each board has their own tricks: **different device names, firmware loaders, configuration (de)compilers, hardware configurators**

## Desktop installation ##

You can build a desktop withing the image. Consider this feature as experimental. Hardware acceleration on Allwinner boards is working within kernel 3.4.x only.

## External applications ##

This place is reserved for custom applications. There is one example of application - USB redirector.

## Closing image ##

There is an option to add some extra commands just before closing an image which is also automaticaly shrink to it's actual size with some small reserve.

## Directory structure ##

It will be something like this:

    compile.sh				compile execution script
	lib/bin/				blobs, firmwares, static compiled, bootsplash
    lib/config/				kernel, board, u-boot, hostapd, package list
    lib/documentation/		user and developers manual
	lib/patch/				collection of kernel and u-boot patches
	lib/scripts/			firstrun, arm hardware info, firmware loaders
	lib/LICENSE				licence description
	lib/README.md			quick manual
	lib/common.sh			creates environment, compiles, shrink image
	lib/configuration.sh	boards presets - kernel source, config, modules, ...
	lib/debootstrap.sh		basic system template creation
	lib/distributions.sh	system specific installation and fixes
	lib/main.sh				user input and script calls
	lib/makeboarddeb.sh		creates board support package .deb
	lib/repo-update.sh		creates and updates your local repository
	lib/repo-show-sh		show packets in your local repository
	lib/upgrade.sh			script to upgrade older images
	sources/				source code for kernel, uboot and other utilities
	output/repository		repository 
	output/cache			cache for root filesystem and headers compilation
	output/debs				deb packeges
	output/images			zip packed RAW image
	userpatches/kernel		put your kernel patches here
	userpatches/u-boot		put your u-boot patches here
	userpatches/			put your kernel config here


## Additional info ##

- [Allwinner SBC community](https://linux-sunxi.org/)
