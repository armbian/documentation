This is a universal image shared with the Banana Pi board.

To get full functionality of this board please login as root and execute:
	
	echo 'fdtfile=sun7i-a20-bananapi-m1-plus.dtb' >> /boot/armbianEnv.txt
	ln -fs bin/bananapim1plus.bin /boot/script.bin
	reboot
	
WiFi does not want to connect in legacy kernel, while it works fine in mainline.