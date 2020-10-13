# What do I need?

- x86/x64 machine running any OS; at least 4G RAM, SSD, quad core (recommended),
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or similar virtualization software **(highly recommended with a minimum of 25GB hard disk space for the virtual disk image)**,
- **The officially supported** compilation environment is [Ubuntu Focal 20.04 x64](http://archive.ubuntu.com/ubuntu/dists/focal/main/installer-amd64/current/legacy-images/netboot/mini.iso) **only!** (Support for Ubuntu 18.04 will be there until either we run into issues we do not want to waste time on or upstream support ends),
- `binfmt_misc` kernel module.  Some *ubuntu-cloud* images do not have this module.  Switch to a generic kernel if that is the case.
- installed basic system, OpenSSH and Samba (optional),
- no spaces in full path to the build script location allowed,
- superuser rights (configured `sudo` or root shell).

Not officially supported build environments from community contributions:

- Setting up VirtualBox and compile environment is easy following our [Vagrant tutorial](https://docs.armbian.com/Developer-Guide_Using-Vagrant/),
- [Docker](Developer-Guide_Building-with-Docker.md) environment is also supported for building kernels and full OS images,
- [Multipass](https://gist.github.com/atomic77/7633fcdbf99dca80f31fd6d64bfd0565)

Please note that system requirements (both hardware and OS/software) may differ depending on the build environment (Vagrant, Docker, Virtualbox, native).

# How to start?

### Native and VirtualBox environments:

Login as root and run:

```bash
apt-get -y -qq install git  
git clone --depth 1 https://github.com/armbian/build  
cd build  
```

Run the script

	./compile.sh

Make sure that full path to the build script **does not contain spaces**.

![](http://www.armbian.com/wp-content/uploads/2016/01/21.png)

### Providing build configuration

After the first run of `compile.sh` a new configuration file `config-example.conf` and symlink `config-default.conf` will be created.
You may edit it to your needs or create different configuration files using it as a template.

Alternatively you can supply options as command line parameters to compile.sh.
Example:

    ./compile.sh BOARD=cubietruck BRANCH=current KERNEL_ONLY=yes RELEASE=bionic

Note: Option `BUILD_ALL` cannot be set to "yes" via command line parameter.

## Base and descendant configuration

You can create one base configuration (`config-base.conf`) and use this in descendant config (`config-dev.conf`). Three parameters (*BRANCH*, *RELEASE*, *COMPRESS_OUTPUTIMAGE*) will be overwritten.

```
. ./config-base.conf  
  
BRANCH="dev"  
RELEASE="buster"  
COMPRESS_OUTPUTIMAGE="sha,gz"  
```

### Using our automated build system

If you do not own the proper equipment to build images on your own, you can make use of the automated build system.
Packages are recompiled every night (starting at 00:01 CEST) and a few testing images are produced.
These images are accessible on the [download server](https://dl.armbian.com/) under board folder, subfolder "*Nightly*".
Packages, when successfully built, are published in the *beta* repository.
You can switch to *beta* repository in [armbian-config](User-Guide_Armbian-Config.md) or by changing *apt.armbian.com* to *beta.armbian.com* in /etc/apt/sources.list.d/armbian.list.

Board beta images are defined in board configuration files which are located [here](https://github.com/armbian/build/tree/master/config/boards).
This is a typical board configuration:

```
	# A20 dual core 1Gb SoC  
	BOARD_NAME="Banana Pi"  
	LINUXFAMILY="sun7i"  
	BOOTCONFIG="Bananapi_defconfig"  
	MODULES="hci_uart gpio_sunxi rfcomm hidp sunxi-ir bonding spi_sun7i 8021q a20_tp #ap6211"  
	MODULES_NEXT="brcmfmac bonding"  
	#  
	KERNEL_TARGET="legacy,current,dev"  
	CLI_TARGET="buster,bionic,focal:current"  
	DESKTOP_TARGET="stretch:legacy,current"  
	  
	CLI_BETA_TARGET=""  
	DESKTOP_BETA_TARGET=""  
	#  
	BOARDRATING=""  
	CHIP="http://docs.armbian.com/Hardware_Allwinner-A20/"  
	HARDWARE="https://linux-sunxi.org/Banana_Pi"  
	FORUMS="https://forum.armbian.com/forum/7-allwinner-a10a20/"  
	BUY="http://amzn.to/2fToHjR"  
```

You can find more information about those variables [here](https://github.com/armbian/build/blob/master/config/boards/README.md).

If you want that our automated system start making images for this particular board, you need to alter parameters `CLI_BETA_TARGET` and `DESKTOP_BETA_TARGET`.
Variants are depenendend from `KERNEL_TARGET` definitions and supported userlands: `focal`, `buster`, `bionic`, `stretch`.
To edit those parameters you need to push changes to the build script.
You need to [fork a project and create a pull request](Process_Contribute.md) and after it is imported by one of the administrators, images will start to show up in appropriate folder.

If you want to enable Debian buster desktop image with _current_ kernel choose the following:

	DESKTOP_BETA_TARGET="buster:current"

or for command line interfaces Ubuntu Bionic based images with legacy kernel 4.19.x

	CLI_BETA_TARGET="bionic:legacy"

or for image with latest upstream development kernel.

	DESKTOP_BETA_TARGET="buster:dev"


### Using alternate armbian builder repos and branches

By default, armbian-builder assumes working from `master` of `https://github.com/armbian/build.git`.  If you are working from your own repo / branch, `touch .ignore_changes` will cause armbian-builder to not attempt a repo checkout.

### Executing any bash statement

Currently, invoking compile.sh will run a monotonous task of building all the components into a final image.

In some situation, especially when developing with Kernel or U-Boot, it is handy to run a portion of that great task like:

```
        # using default profile  
        ./compile.sh 'fetch_from_repo "$BOOTSOURCE" "$BOOTDIR" "$BOOTBRANCH" "yes"'  
        ./compile.sh 'compile_uboot'  
```

You can also dump the variable:

```
        # using profile of `userpatches/config-my.conf`  
        ./compile.sh my 'echo $SRC/cache/sources/$BOOTSOURCEDIR'  
```

NOTE: please use single quotes to keep the `$VAR` from early expansion in the command line shell.
