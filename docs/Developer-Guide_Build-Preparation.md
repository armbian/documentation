# What do I need?

- x86/x64 machine running any OS; 4G ram, SSD, quad core (recommended),
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or similar virtualization software **(highly recommended with a minimum of 20GB hard disk space for the virtual disk image)**,
- Setting up VirtualBox and compile environment is easy following our [Vagrant tutorial](https://docs.armbian.com/Developer-Guide_Using-Vagrant/),
- when you don't want to build whole OS images (`KERNEL_ONLY=yes`) then [Docker](https://github.com/igorpecovnik/lib/pull/255#issuecomment-205045273), [systemd-nspawn](https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html) or other containerization software can be used,
- **Only supported** compilation environment is [Ubuntu Xenial 16.04 x64](http://archive.ubuntu.com/ubuntu/dists/xenial-updates/main/installer-amd64/current/images/netboot/mini.iso) (**no other releases are supported**! It has to be exactly 16.04 otherwise default compiler versions might not match so if you're on an older Ubuntu release upgrade to 16.04 now, if you use a newer Ubuntu version start with 16.04 from scratch),
- installed basic system, OpenSSH and Samba (optional),
- no spaces in full path to the build script location allowed,
- superuser rights (configured `sudo` or root shell).

Please note that system requirements (both hardware and OS/software) may differ depending on the build environment (Vagrant, Docker, Virtualbox, native).

# How to start?

Login as root and run:

	apt-get -y -qq install git
	git clone --depth 1 https://github.com/armbian/build
	cd build

Run the script

	sudo ./compile.sh

![](http://www.armbian.com/wp-content/uploads/2016/01/21.png)

# Providing build configuration

After the first run of `compile.sh` a new configuration file `config-default.conf` will be created.
You may edit it to your needs or create different configuration files using it as a template.

Alternatively you can supply options as command line parameters to compile.sh
Example:

    ./compile.sh BOARD=cubietruck BRANCH=next KERNEL_ONLY=yes RELEASE=xenial

Note: Option `BUILD_ALL` cannot be set to "yes" via command line parameter.
