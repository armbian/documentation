This is a universal image shared with the Banana Pi board.

To get full functionality of this board please login as root and execute:
	
	apt-get update
	apt-get upgrade
	source /etc/armbian-release
	dpkg -r linux-u-boot-bananapi-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-bananapi
	apt-get -y install linux-u-boot-orangepi-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-orangepi
	ln -fs bin/orangepi.bin /boot/script.bin
	echo orangepi > /etc/hostname
	reboot