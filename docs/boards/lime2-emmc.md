To get full support with access to eMMC and stable settings, you need to execute those commands:
	
	source /etc/armbian-release
	dpkg -r linux-u-boot-lime2-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-lime2
	apt-get -y install linux-u-boot-lime2-emmc-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-lime2-emmc
	ln -fs bin/lime2-emmc.bin /boot/script.bin
	echo lime2-emmc > /etc/hostname
	reboot

After this, your lime2 image becomes full featured lime2-emmc image.