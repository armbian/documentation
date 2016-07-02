# What do I need?

- x86/x64 machine running any OS; 4G ram, SSD, quad core (recommended),
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or similar virtualization software **(highly recommended)**,
- alternatively - [Docker](https://github.com/igorpecovnik/lib/pull/255#issuecomment-205045273), [systemd-nspawn](https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html) or other containerization software,
- compilation environment is **highly recommended** to be [Ubuntu Trusty 14.04](http://archive.ubuntu.com/ubuntu/dists/trusty-updates/main/installer-amd64/current/images/netboot/mini.iso) or Ubuntu Xenial 16.04 (other releases are **not officially supported**),
- installed basic system, OpenSSH and Samba (optional),
- superuser rights (configured `sudo` or root shell),
- cca. 20G of free space.

# How to start?

Login as root and run:

	apt-get -y -qq install git
    git clone --depth 1 https://github.com/igorpecovnik/lib
	cp lib/compile.sh .
	nano compile.sh # alter if necessary

Run the script

	./compile.sh

![](http://www.armbian.com/wp-content/uploads/2016/01/21.png)

### Supplying options via command line parameters
Instead of editing compile.sh to set options, you can set them by supplying command line parameters to compile.sh
Example:

    ./compile.sh BRANCH=next BOARD=cubietruck KERNEL_ONLY=yes PROGRESS_DISPLAY=plain RELEASE=jessie

Note: Option `BUILD_ALL` cannot be set to "yes" via command line parameter.
