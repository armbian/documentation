- manual flashing to latest u-boot is mandatory! [Download](https://dl.armbian.com/espressobin/u-boot/) the right boot flash for your board: 512,1G,2G, number of RAM chips and appropirate memory speeds. You can obtain numbers from current boot prompt. Copy this `flash-image-MEM-RAM_CHIPS-CPU_DDR_boot_sd_and_usb.bin` to your FAT formatted USB key, plug it into USB3.0 port and execute from u-boot prompt: 

		bubt flash-image-MEM-RAM_CHIPS-CPU_DDR_boot_sd_and_usb.bin spi usb

	After updating your SPI flash with most recent "sd\_and\_usb" u-boot, you can boot from USB or SD card the exact same way.
	
- in case you came from stock boot loader or your boot environment was erased somehow, this is what you need to put into u-boot:

		setenv initrd_addr 0x1100000
		setenv image_name boot/Image
		setenv load_script 'if test -e mmc 0:1 boot/boot.scr; then echo \"... booting from SD\";setenv boot_interface mmc;else echo \"... booting from USB/SATA\";usb start;setenv boot_interface usb;fi;if test -e \$boot_interface 0:1 boot/boot.scr;then ext4load \$boot_interface 0:1 0x00800000 boot/boot.scr; source; fi'
		setenv bootcmd 'run get_images; run set_bootargs; run load_script;booti \$kernel_addr \$ramfs_addr \$fdt_addr'
		saveenv
- If you manage to crash your SPI, proceed with [SATA boot recovery](http://wiki.espressobin.net/tiki-index.php?page=Boot+ESPRESSObin+from+SATA+drive).
- booting directly from SATA is currently broken.
