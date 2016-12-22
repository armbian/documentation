To get full functionality of lime2-emmc, you need to execute those commands:
	
	apt-get update
	apt-get upgrade
	source /etc/armbian-release
	dpkg -r linux-u-boot-lime2-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-lime2
	apt-get -y install linux-u-boot-lime2-emmc-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-lime2-emmc
	ln -fs bin/lime2-emmc.bin /boot/script.bin
	echo lime2-emmc > /etc/hostname
	reboot