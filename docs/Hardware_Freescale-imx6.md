# Cubox and Hummingboard boards

## Legacy
System images with legacy kernel

- Kernel [3.14.x](https://github.com/linux4kix/linux-linaro-stable-mx6) with large hardware support, headers and some firmware included
- [Docker ready](https://forum.armbian.com/topic/490-docker-on-armbian/) – [what is Docker](https://www.docker.com/what-docker)?
- PCI-E operational (Hummingboard Pro, Gate & Edge)
- mSATA / m2 operational (Hummingboard Pro & Edge)
- Enabled audio devices: HDMI, spdif, analogue
- [Bluetooth ready](https://wiki.debian.org/BluetoothUser) (working with Cubox-i/HB PRO on-board device or external key)
- [I2C](https://en.wikipedia.org/wiki/I%C2%B2C) ready and tested with small 16×2 LCD. Basic i2c tools included.
- SPI ready and tested with ILI9341 based 2.4″ TFT LCD display.
- [Drivers for small TFT LCD](https://github.com/notro/fbtft) display modules.
- [USB redirector](https://www.incentivespro.com/usb-server-usage.html) – for sharing USB over TCP/IP (disabled by default /etc/init.d/rc.usbsrvd)

### Bugs or limitation

- Gigabit ethernet transfer rate is around 50% of its theoretical max rate (internal chip bus limitation)

## Mainline
System images with mainline kernel

- [Mainline](https://www.kernel.org/) with large hardware support, headers and some firmware included
- [Docker ready](User-Guide_Advanced-Features/#how-to-run-docker) – [what is Docker](https://www.docker.com/what-docker)?
- PCI-E operational (Hummingboard Pro, Gate & Edge)
- mSATA / m2 operational (Hummingboard Pro & Edge)
- Enabled audio devices
- Bluetooth ready (working with supported external keys)

### Bugs or limitation

- Gigabit ethernet transfer rate is around 50% of its theoretical max rate (internal chip bus limitation)

## Desktop

- Pre-installed: Firefox, LibreOffice Writer, Thunderbird
- Lightweight XFCE desktop
- Autologin, when normal user is created – no login manager (/etc/default/nodm)

## Connect your LCD display

I tried two different display connection types: I2C and SPI. Both are working perfectly with my image 2.6 or higher.

![](https://www.armbian.com/wp-content/uploads/2014/08/hummingboard-display.png)

- I am using [2.4″ 240×320 SPI TFT LCD Serial Port Module+5/3.3V Pbc Adapter Micro SD ILI9341](https://www.google.com/search?q=2.4%E2%80%B3+240%C3%97320+SPI+TFT+LCD+Serial+Port+Module%2B5%2F3.3V+Pbc+Adapter+Micro+SD+ILI9341&oq=2.4%E2%80%B3+240%C3%97320+SPI+TFT+LCD+Serial+Port+Module%2B5%2F3.3V+Pbc+Adapter+Micro+SD+ILI9341)
- Wire according to [this map](https://blog.riyas.org/2014/07/quickly-test-il9341-22-inch-22-spi-tft-raspbmc-fbtft.html).
- You have to use Armbian 1.5 or newer. Currently working only under Legacy kernel.
- Add this to your /etc/modules:
`fbtft_device name=adafruit22a rotate=90 speed=48000000 fps=50 gpios=reset:67,led:72,dc:195 busnum=1`
- Reboot
- Test – display some picture on the screen:
`fbi -d /dev/fb2 -T 1 -noverbose -a yourimage.jpg`
- [Troubleshooting and settings for other displays
LVDS](https://github.com/notro/fbtft/wiki)

## GPIO

[How to control HummingBoard GPIO from kernel space?](https://www.solid-run.com/community/topic2345.html)

## Udoo Quad

- [Kernel 3.14.x](https://github.com/UDOOboard/linux_kernel) and [4.4.x](https://github.com/patrykk/linux-udoo) with some hardware support, headers and some firmware included
- [Docker ready](https://forum.armbian.com/topic/490-docker-on-armbian/) – [what is Docker](https://www.docker.com/what-docker)?
- Wireless adapter with DHCP ready but disabled (/etc/network/interfaces, WPA2: normal connect, bonding / notebook or AP mode). It can handle between 40-70Mbit/s.
- SATA operational
- Enabled analogue (VT1613) and HDMI audio device

### Bugs

SATA & USB install not working on legacy kernel

## Udoo Neo

- [Kernel 3.14.x](https://github.com/UDOOboard/linux_kernel) with some hardware support, headers and some firmware included
- Wireless adapter with DHCP ready but disabled
