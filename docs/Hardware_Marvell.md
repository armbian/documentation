# Marvell Armada Clearfog #

## Overview ##

None of kernels are fully functional so you need to try out which is best for your case.

## Default ##
System images with mainline 4.14.x kernel and u-boot 2018.1

- [Mainline kernel](http://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCIe are operational and [convertible to mSATA](https://github.com/armbian/build/tree/master/patch/u-boot/u-boot-mvebu), M2 operational
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)
- [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) ready. Basic i2c tools included.
- [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) ready but untested.

### Bugs or limitation ###

- SFP is not supported, might work when compiling your own image with the sfp modules.

## Next ##
System images with mainline 4.19.x kernel and u-boot 2018.1

- [Mainline kernel](http://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCIe are operational and [convertible to mSATA](https://github.com/armbian/build/tree/master/patch/u-boot/u-boot-mvebu), M2 operational
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)
- [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) ready. Basic i2c tools included.
- [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) ready but untested.
- SFP ready and tested with a copper 1G module
- SFP DDMI is operational (`sudo ethtool -m eth2`)

### Bugs or limitation ###

- some combination of mPCIe devices leads to incorrect/no detection, this has been observed with multiple SATA and WiFi Cards, [see here for a test matrix](https://docs.google.com/spreadsheets/d/1VggzrfFibH0cmpSGW2FyoJW-d936Y2amwwKutUwX4-8). 

## Notes

- In case you ever run into troubles and ask for help in the forums please ensure to provide a serial console log (UART adapter on board accessible through Micro USB with 115200/8/N/1 settings)
- The boards can boot from various sources that are adjustable with a DIP switch. Comprehensive information about the necessary preparations [available here](https://github.com/nightseas/arm_applications/blob/master/doc/getting_started_with_clearfog_base.md).
