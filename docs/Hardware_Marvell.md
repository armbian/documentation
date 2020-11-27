# Marvell Armada

## Helios4

### Overview

All builds provide 100% hardware support for Helios4.

### Build Version Status

#### Legacy

- U-Boot : Mainline 2019.04
- Linux Kernel : Mainline 4.19.y

#### Current

- U-Boot : Mainline 2019.04
- Linux Kernel : Mainline 5.4.y

### Known Limitations

* SDcard High Speed timing have compatibility issue with some brands.</br>
Temporary workaround : Disable UHS option/support.</br>
Can be manually enable, refer to the following [page](https://wiki.kobol.io/sdcard) (2020-11-25 link broken [archive](https://web.archive.org/web/20191113071529/https://wiki.kobol.io/sdcard/)).

* During SATA heavy load, accessing SPI NOR Flash will generate ATA errors.</br>
Temporary workaround : Disable SPI NOR flash.</br>
Can be manually enable, refer to the following [page](https://wiki.kobol.io/spi) (2020-11-25 link broken [archive](https://web.archive.org/web/20191113071543/https://wiki.kobol.io/spi/)).

### Notes

Find more details about hardware support and configuration on [Helios4 Wiki](https://wiki.kobol.io).

## Clearfog Pro/Base

### Overview

Both builds provide close to 100% hardware support, some slight differences are listed below.

### Build Version Status

#### Legacy/Current

- [Mainline kernel](https://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](/User-Guide_Advanced-Features/#how-to-run-docker)
- Both mPCIe are operational and [convertible to mSATA](#converting-mpcie-to-msata), M2 operational
- Added patch to unlock Atheros regulatory restrictions which unlock 5Ghz AP mode in cheap Atheros cards (ath9 driver)
- Bluetooth ready (working with supported external keys)
- [I2C](https://en.wikipedia.org/wiki/I%C2%B2C) ready. Basic i2c tools included.
- [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) ready but untested.
- SFP is working at up to 1GB/s even with faster fiber modules
- SFP DDMI is operational (`sudo ethtool -m eth2`)

### Bugs or limitation

- all builds suffer from minor problems with specific mPCIe combinations. If you run into problems check [this test matrix](https://docs.google.com/spreadsheets/d/1izPD5XUzQC0ZZWb8FMBMkofN73w-m_6bjrtZK-zr_b4) for some known working/not working combinations.

### Converting mPCIe to mSATA

- To convert mPCIe to mSATA you have to enable the corresponding patches in [u-boot-mvebu](https://github.com/armbian/build/tree/master/patch/u-boot/u-boot-mvebu-dev). Afterwards rebuild u-boot with our build system and write the new u-boot to your boot medium. If you need assistance ask in the forum.

### Notes

- In case you ever run into troubles and ask for help in the forums please ensure to provide a serial console log (UART adapter on board accessible through Micro USB with 115200/8/N/1 settings)
- The boards can boot from various sources that are adjustable with a DIP switch. Comprehensive information about the necessary preparations [available here](https://github.com/nightseas/arm_applications/blob/master/doc/getting_started_with_clearfog_base.md).
