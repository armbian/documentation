# Marvel Armada Clearfog #

## Overview ##

None of kernels is fully functional so you need to try out which is best for your case.

## Legacy ##
System images with legacy kernel

- [Kernel 3.10.103](https://github.com/SolidRun/linux-armada38x) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCI are operational and [convertible to mSATA](https://github.com/igorpecovnik/lib/tree/master/patch/u-boot/u-boot-armada-default), M2 operational
- Optimized CPU frequency scaling 800-1600Mhz
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)
- [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) ready. Basic i2c tools included.
- [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) ready but untested.
- Drivers for [small TFT LCD display modules](https://github.com/notro/fbtft).
- [USB redirector](http://www.incentivespro.com/usb-server-usage.html) – for sharing USB over TCP/IP (disabled by default /etc/init.d/rc.usbsrvd)

### Bugs or limitation ###

- SFP cage is unsupported

## Vanilla ##
System images with vanilla kernel

- Kernel [4.7.3](http://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCI are operational and [convertible to mSATA](https://github.com/igorpecovnik/lib/tree/master/patch/u-boot/u-boot-armada-default), M2 operational
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)

### Bugs or limitation ###

- SFP cage is unsupported


## Development ##

- Kernel [4.4.20](https://github.com/SolidRun/linux-stable) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCI are operational and [convertible to mSATA](https://github.com/igorpecovnik/lib/tree/master/patch/u-boot/u-boot-armada-default), M2 operational
- SFP cage is supported

Accessible from repository:

    apt-get install linux-image-dev-marvell linux-dtb-dev-marvell