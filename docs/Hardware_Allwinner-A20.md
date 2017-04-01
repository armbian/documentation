# Allwinner A10 & A20 boards #

## Overview ##

Both kernels are stable and production ready, but you should use them for different purpuses since their basic support differ:

- legacy: video acceleration, NAND support, connecting displays
- mainline: headless server, light desktop operations

## Legacy ##
System images with legacy kernel

- Kernel [3.4.x](https://github.com/linux-sunxi/linux-sunxi) with large hardware support, headers and some firmware included
- Enabled audio devices: analog, 8 channel HDMI, spdif and I2S (if wired and enabled in HW configuration)
- IR functional and preconfigured – tested with LG remote
- [LIRC GPIO send and receive driver](https://github.com/igorpecovnik/lib/issues/135) – tested but unconfigured
- Bluetooth ready (working with supported external keys)
- [Enabled overlayfs](User-Guide_Advanced-Features/#how-to-freeze-your-filesystem)
- [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) ready and tested with small 16×2 LCD. Basic i2c tools included.
- SPI ready and tested with ILI9341 based 2.4″ TFT LCD display.
- [Drivers for small TFT LCD](https://github.com/notro/fbtft) display modules.
- [Clustering / stacking](http://en.wikipedia.org/wiki/Cluster_(computing))
- [USB redirector](http://www.incentivespro.com/usb-server-usage.html) – for sharing USB over TCP/IP (disabled by default /etc/init.d/rc.usbsrvd)
- Onboard LED attached to SD card activity (script.bin)

### Bugs or limitation ###

- NAND install sometime fails. Dirty but working workaround: install [Lubuntu to NAND](http://dl.cubieboard.org/software/a20-cubietruck/lubuntu/) with [Phoenix tools](http://docs.cubieboard.org/downloads) and run install again.
- Shutdown results into reboot under certain conditions.

## Mainline ##
System images with mainline kernel

- [Mainline](http://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker)
- Enabled audio devices: analog & USB playback
- [USB / UAS](http://linux-sunxi.org/USB/UAS) – more efficient disk access over USB (A20 and H3)
- [CAN bus](https://en.wikipedia.org/wiki/CAN_bus) – Controller Area Network
- [USB OTG connector](http://linux-sunxi.org/USB_Gadget) – OTG or host mode
- Bluetooth ready (working with supported external keys)
- [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) ready and tested with small 16×2 LCD. Basic i2c tools included.
- Onboard LED attached to SD card activity (not enabled on all boards yet)

### Bugs or limitation ###

- No HW acceleration for desktop and video decoding
- NAND is not supported yet.
- Screen output from kernel is set to HDMI by default. Boot loader can detect and switch, kernel not.
- HDMI audio is not supported yet
- SATA port multiplier support is disabled by default, can be enabled by adding kernel parameter `ahci_sunxi.enable_pmp=1`

## Desktop ##

![YOUTUBE](hsthqj90vTU)

- HW accelerated video playback (legacy kernel only)
- MALI Open GLES (legacy kernel only)
- Pre-installed: Firefox, LibreOffice Writer, Thunderbird
- Lightweight XFCE desktop
- Autologin, when normal user is created – no login manager (/etc/default/nodm)

## Notes ##

### Setting non-standard monitor settings for A10, A20 and A31 based boards in u-boot ###

Following commands (example) needs to be executed in u-boot command prompt:
```
setenv video-mode sunxi:1024x768-24@60,monitor=dvi,hpd=0,edid=0,overscan_x=1,overscan_y=2
saveenv
```

Since environment is reset after flashing u-boot, you need to do this after every u-boot upgrade or put this to u-boot script

## Resources ##

[Armbian packages repository](http://www.armbian.com/kernel/)
