To get full functionality of this board please login as root and execute:
	
	apt-get update
	apt-get upgrade
	source /etc/armbian-release
	dpkg -r linux-u-boot-orangepipcplus-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-orangepipcplus
	apt-get -y install linux-u-boot-orangepipc-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-orangepipc
	ln -fs bin/orangepipc.bin /boot/script.bin
	echo orangepipc > /etc/hostname
	reboot