# Marvel Armada Clearfog #

## Overview ##

None of kernels are fully functional so you need to try out which is best for your case.

## LTS ##
System images with patched mainline 4.4.x kernel

- [Kernel 4.4.x](https://github.com/moonman/linux-stable)
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCIe are operational and [convertible to mSATA](https://github.com/igorpecovnik/lib/tree/master/patch/u-boot/u-boot-armada-default), M2 operational
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)
- [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) ready. Basic i2c tools included.
- [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) ready but untested.
- [USB redirector](http://www.incentivespro.com/usb-server-usage.html) – for sharing USB over TCP/IP (disabled by default /etc/init.d/rc.usbsrvd)

### Bugs or limitation ###

- DFS (Cpufreq) is not supported

## Mainline ##
System images with vanilla kernel

- [Mainline kernel](http://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCIe are operational and [convertible to mSATA](https://github.com/igorpecovnik/lib/tree/master/patch/u-boot/u-boot-armada-default), M2 operational
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)

### Bugs or limitation ###

- DFS (Cpufreq) is not supported
- SFP cage support ported from 4.4.x and may be removed in the future
