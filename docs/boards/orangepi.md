To get full functionality of orangepi, you need to execute those commands:
	
	apt-get update
	apt-get upgrade
	source /etc/armbian-release
	dpkg -r linux-u-boot-bananapi-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-bananapi
	apt-get -y install linux-u-boot-orangepi-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-orangepi
	ln -fs bin/orangepi.bin /boot/script.bin
	echo orangepi > /etc/hostname
	reboot