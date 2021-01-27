# Allwinner A10 & A20 boards

## Overview

Both *legacy* and *current* kernels are stable and production ready and mostly sharing the same features through backports.

- **Note: Kernel 3.4.x has been dropped due to lacking upstream support which has ended in 2017.**

### Features

- Enabled audio devices: analog, 8 channel HDMI, spdif and I2S (if wired and enabled in HW configuration)
- Bluetooth ready (working with supported external keys)
- [Enabled overlayfs](/User-Guide_Advanced-Features/#how-to-freeze-your-filesystem-outdated) (outdated)
- [I2C](https://en.wikipedia.org/wiki/I%C2%B2C) ready and tested with small 16×2 LCD. Basic i2c tools included.
- SPI ready and tested with ILI9341 based 2.4″ TFT LCD display.
- [Drivers for small TFT LCD](https://github.com/notro/fbtft) display modules.
- [Clustering / stacking](https://en.wikipedia.org/wiki/Cluster_(computing))
- Onboard LED attached to SD card activity (script.bin)
- [Docker ready](/User-Guide_Advanced-Features/#how-to-run-docker)
- Enabled audio devices: analog, SPDIF (if available) & USB
- [USB / UAS](https://linux-sunxi.org/USB/UAS) – more efficient disk access over USB (A20 and H3)
- [CAN bus](https://en.wikipedia.org/wiki/CAN_bus) – Controller Area Network
- [USB OTG connector](https://linux-sunxi.org/USB_Gadget) – OTG or host mode
- Bluetooth ready (working with supported external keys)
- [I2C](https://en.wikipedia.org/wiki/I%C2%B2C) ready and tested with small 16×2 LCD. Basic i2c tools included.
- Onboard LED attached to SD card activity (not enabled on all boards yet)

### Bugs or limitation

- NAND install sometime fails. Workaround: install [Lubuntu to NAND](http://dl.cubieboard.org/software/a20-cubietruck/lubuntu/) with [Phoenix tools](http://docs.cubieboard.org/downloads) and run install again. (Links no longer available - 27/01/21 Werner)
- Shutdown results into reboot under certain conditions.
- SATA port multiplier support is disabled by default, can be enabled by adding kernel parameter `ahci_sunxi.enable_pmp=1`
- Screen output from kernel is set to HDMI by default. Boot loader can detect and switch, kernel not.


## Desktop

[![IMAGE ALT TEXT](https://img.youtube.com/vi/hsthqj90vTU/0.jpg)](https://www.youtube.com/watch?v=hsthqj90vTU "Armbian Desktop")

- HW accelerated video playback (if available)
- MALI Open GLES (if available)
- Pre-installed: Firefox, LibreOffice Writer, Thunderbird
- Lightweight XFCE desktop
- Autologin, when normal user is created – no login manager (/etc/default/nodm)

## Notes

### Setting non-standard monitor settings for A10, A20 and A31 based boards in u-boot

Following commands (example) needs to be executed in u-boot command prompt:
```
setenv video-mode sunxi:1024x768-24@60,monitor=dvi,hpd=0,edid=0,overscan_x=1,overscan_y=2
saveenv
```

Since environment is reset after flashing u-boot, you need to do this after every u-boot upgrade or put this to u-boot script

## Resources

[Armbian packages repository](https://www.armbian.com/kernel/)
