# What happens behind the build process?

### Build process summary:

- creates development environment on top of amd64 Ubuntu 20.04 LTS,
- downloads proven sources, applies patches on top and uses tested configurations,
- cross-compiles universal boot loader (***U-Boot***), kernel and other tools and drivers,
- packs kernel, U-Boot, dtb and root customizations into Debian packages,
- debootstraps minimalistic Debian Buster and Ubuntu Focal into SD card images,
- installs additional packets, applies customizations and shrinks image to its actual size.

Check this image [compiling example](https://youtu.be/zeShf12MNLg) with partial cache.


### Build process details:

## Creating compile environment ##
First things first. All necessary dependencies are downloaded and installed. This happens though both http and torrent network. Btw. having too much unused traffic? Help us to reduce ours :) https://forum.armbian.com/topic/4198-seed-our-torrents/

## Using board configuration ##
We need to get some predefined variables about selected the board. Which kernel & uboot source to use, modules to load, which is the build number, do we need to have a single partition or dual with boot on fat, which extra drivers to compile out of the kernel tree ...
All this stuff is predefined for each and every single supported board.

## Downloading sources ##
When we know which sources to use and where they need to be the download or updated this process starts. This might take from several minutes to several hours.

## Patching ##
In the patching process we are applying patches to the used sources. The process is - depending on selected board - defined in:

	lib/patch/kernel/sun7i-default
	lib/patch/kernel/sunxi-dev
	...
	lib/patch/u-boot/u-boot-default
	lib/patch/u-boot/u-boot-neo-default
	...

Patch rules for subdirectories are: **KERNEL_FAMILY-BRANCH** for kernel and **U-BOOT-SOURCE-BRANCH** for U-Boot.

## Debootstrap ##
Debootstrap creates fresh Debian / Ubuntu root filesystem templates or use cached under:

	output/cache/rootfs/

To recreate those files you need to remove them manually. 
From time to time they will be recreated anyway if Armbian updates their rootfs cache.

## Kernel install ##
When the root filesystem is ready we need to install the kernel image with modules, board definitions and firmwares. Along with this we set the CPU frequency min/max, hostname, modules, network interfaces templates. Here is also the place to install headers and fix + native compile them on the way.

## Distribution fixes ##
Each distribution has it's own way of doing things:

- serial console
- different packets
- configuration locations

## Board fixes ##
Each board has their own tricks: **different device names, firmware loaders, configuration (de)compilers, hardware configurators**

## Desktop installation ##
You can build a desktop environment withing the image. Consider this feature as experimental. Do not expect to have working hardware acceleration since this is a very complicated task and needs individial care for different boards.

## External applications ##
This place is reserved for custom applications. There is one example of application: USB redirector.

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
