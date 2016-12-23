To get full functionality of this board please login as root and execute:
	
	apt-get update
	apt-get upgrade
	source /etc/armbian-release
	dpkg -r linux-u-boot-bananapi-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-bananapi
	apt-get -y install linux-u-boot-bananapipro-${BRANCH} linux-$(lsb_release -cs)-root-${BRANCH}-bananapipro
	ln -fs bin/bananapipro.bin /boot/script.bin
	echo bananapipro > /etc/hostname
	reboot