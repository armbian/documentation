# What do I need?

- x86/x64 machine running any OS; 4G ram, SSD, quad core (recommended),
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or similar virtualization software **(highly recommended with a minimum of 20GB hard disk space for the virtual disk image)**,
- Setting up VirtualBox and compile environment is easy following our [Vagrant tutorial](https://docs.armbian.com/Developer-Guide_Using-Vagrant/),
- [Docker](Developer-Guide_Building-with-Docker.md) environment is also supported for building kernels and full OS images,
- **The only supported** compilation environment is [Ubuntu Xenial 16.04 x64](http://archive.ubuntu.com/ubuntu/dists/xenial-updates/main/installer-amd64/current/images/netboot/mini.iso) (**no other releases are supported**! It has to be exactly 16.04 otherwise default compiler versions might not match so if you're on an older Ubuntu release upgrade to 16.04 now, if you use a newer Ubuntu version start with 16.04 from scratch),
- installed basic system, OpenSSH and Samba (optional),
- no spaces in full path to the build script location allowed,
- superuser rights (configured `sudo` or root shell).

Please note that system requirements (both hardware and OS/software) may differ depending on the build environment (Vagrant, Docker, Virtualbox, native).

# How to start?

#### Native and Virtualbox environments:

Login as root and run:

	apt-get -y -qq install git
	git clone --depth 1 https://github.com/armbian/build
	cd build

Run the script

	./compile.sh

Make sure that full path to the build script does not contain spaces.

![](http://www.armbian.com/wp-content/uploads/2016/01/21.png)

# Providing build configuration

After the first run of `compile.sh` a new configuration file `config-default.conf` will be created.
You may edit it to your needs or create different configuration files using it as a template.

Alternatively you can supply options as command line parameters to compile.sh.
Example:

    ./compile.sh BOARD=cubietruck BRANCH=next KERNEL_ONLY=yes RELEASE=xenial

Note: Option `BUILD_ALL` cannot be set to "yes" via command line parameter.

# Using our automated build system

If you don't own the proper equipment to build images on your own, you can make use of the automated build system.
Packages are recompiled every night (starting at 00:01 CEST) and a few testing images are produced.
These images are accessible on the [download server](https://dl.armbian.com/) under board folder, subfolder "Nightly".
Packages, when successfully built, are published in the beta repository.
You can switch to beta repository in [armbian-config](User-Guide_Armbian-Config.md) or by changing apt.armbian.com to beta.armbian.com in /etc/apt/sources.list.d/armbian.list.

Board beta images are defined in board configuration files which are located [here](https://github.com/armbian/build/tree/master/config/boards).
This is a typical board configuration:

	# A20 dual core 1Gb SoC
	BOARD_NAME="Banana Pi"
	LINUXFAMILY="sun7i"
	BOOTCONFIG="Bananapi_defconfig"
	MODULES="hci_uart gpio_sunxi rfcomm hidp sunxi-ir bonding spi_sun7i 8021q a20_tp #ap6211"
	MODULES_NEXT="brcmfmac bonding"
	#
	KERNEL_TARGET="default,next,dev"
	CLI_TARGET="jessie,xenial:next"
	DESKTOP_TARGET="xenial:default,next"
	
	CLI_BETA_TARGET=""
	DESKTOP_BETA_TARGET=""
	#
	RECOMMENDED="Ubuntu_xenial_default_desktop:90,Debian_jessie_next:100"
	#
	BOARDRATING=""
	CHIP="http://docs.armbian.com/Hardware_Allwinner-A20/"
	HARDWARE="https://linux-sunxi.org/Banana_Pi"
	FORUMS="http://forum.armbian.com/index.php/forum/7-allwinner-a10a20/"
	BUY="http://amzn.to/2fToHjR"

If you want that our automated system start making images for this particular board, you need to alter parameters CLI_BETA_TARGET and DESKTOP_BETA_TARGET.
Variants are depenendend from KERNEL_TARGET definitions and supported userlands: jessie, xenial, stretch.
To edit those parameters you need to push changes to the build script.
You need to [fork a project and create a pull request](Process_Contribute.md) and after it's imported by one of the administrators, images will start to show up in appropriate folder.

If you want to enable Debian stretch desktop image with mainline kernel choose the following:

	DESKTOP_BETA_TARGET="stretch:next"

or 

	CLI_BETA_TARGET="xenial:default"

for command line interfaces Ubuntu Xenial based images with legacy kernel 3.4.113 or

	DESKTOP_BETA_TARGET="jessie:dev"

for image with latest upstream development kernel.
