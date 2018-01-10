# Marvel Armada Clearfog #

## Overview ##

None of kernels are fully functional so you need to try out which is best for your case.

## LTS ##
System images with patched mainline 4.4.x kernel

- [Kernel 4.4.x](https://github.com/moonman/linux-stable)
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCIe are operational and [convertible to mSATA](https://github.com/igorpecovnik/lib/tree/master/patch/u-boot/u-boot-armada), M2 operational
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)
- [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) ready. Basic i2c tools included.
- [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) ready but untested.
- SFP ready and tested with a fibre 1G/1.25G module, requires configuring eth2 - static, DHCP or bridged (not configured by default)
- SFP DDMI is operational (`sudo ethtool -m eth2`)

### Bugs or limitation ###

- DFS (Cpufreq) is not supported

## Mainline ##
System images with mainline kernel

- [Mainline kernel](http://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCIe are operational and [convertible to mSATA](https://github.com/igorpecovnik/lib/tree/master/patch/u-boot/u-boot-armada), M2 operational
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)

### Bugs or limitation ###

- SFP is not supported yet

## Notes

- In case you ever run into troubles and ask for help in the forums please ensure to provide a serial console log (UART adapter on board accessible through Micro USB with 115200/8/N/1 settings)
- The boards can boot from various sources that are adjustable with a DIP switch. Comprehensive information about the necessary preparations [available here](https://github.com/nightseas/arm_applications/blob/master/doc/getting_started_with_clearfog_base.md).
