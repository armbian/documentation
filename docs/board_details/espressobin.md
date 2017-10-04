- manual flashing to latest u-boot is mandatory! [Download](https://dl.armbian.com/espressobin/u-boot/) the right boot flash for your board: 512,1G,2G and appropirate memory speeds. You can obtain numbers from current boot prompt. Copy this `flash-image-MEM-CPU_DDR_boot_sd_and_usb.bin` to your FAT formatted USB key, plug it into USB3.0 port and execute from u-boot prompt: 

		bubt flash-image-MEM-CPU_DDR_boot_sd_and_usb.bin spi usb

	After updating your SPI flash with most recent "sd\_and\_usb" u-boot, you can boot from USB or SD card the exact same way.
- If you manage to crash your SPI, proceed with [SATA boot recovery](http://wiki.espressobin.net/tiki-index.php?page=Boot+ESPRESSObin+from+SATA+drive) while you should use our [updated](https://dl.armbian.com/espressobin/u-boot/) images.