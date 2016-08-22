# Cubox and Hummingboard boards #

## Overview ##

Both kernels are stable and production ready, but you should use them for different purpuses since their basic support differ:

- legacy: video acceleration, NAND support, connecting displays
- vanilla: headless server, **no HDMI output - serial console or remote access only**

## Legacy ##
System images with legacy kernel

- Kernel [3.14.x](https://github.com/linux4kix/linux-linaro-stable-mx6) with large hardware support, headers and some firmware included
- [Docker ready](http://forum.armbian.com/index.php/topic/490-docker-on-armbian/) – [what is Docker](https://www.docker.com/what-docker)?
- PCI-E operational (Hummingboard Pro, Gate & Edge)
- mSATA / m2 operational (Hummingboard Pro & Edge)
- Enabled audio devices: HDMI, spdif, analogue
- [Bluetooth ready](https://wiki.debian.org/BluetoothUser) (working with Cubox-i/HB PRO on-board device or external key)
- [I2C](http://en.wikipedia.org/wiki/I%C2%B2C) ready and tested with small 16×2 LCD. Basic i2c tools included.
- SPI ready and tested with ILI9341 based 2.4″ TFT LCD display.
- [Drivers for small TFT LCD](https://github.com/notro/fbtft) display modules.
- [USB redirector](http://www.incentivespro.com/usb-server-usage.html) – for sharing USB over TCP/IP (disabled by default /etc/init.d/rc.usbsrvd)

### Bugs or limitation ###

- Gigabit ethernet transfer rate is around 50% of its theoretical max rate (internal chip bus limitation)

## Vanilla ##
System images with vanilla kernel

- Kernel [4.7.x](http://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker) – [what is Docker](https://www.docker.com/what-docker)?
- PCI-E operational (Hummingboard Pro, Gate & Edge)
- mSATA / m2 operational (Hummingboard Pro & Edge)
- Enabled audio devices
- Bluetooth ready (working with supported external keys)

### Bugs or limitation ###

- Serial console only
- Gigabit ethernet transfer rate is around 50% of its theoretical max rate (internal chip bus limitation)

## Desktop ##

- Pre-installed: Firefox, LibreOffice Writer, Thunderbird
- Lightweight XFCE desktop
- Autologin, when normal user is created – no login manager (/etc/default/nodm)


# Udoo Quad #

# Udoo Neo #