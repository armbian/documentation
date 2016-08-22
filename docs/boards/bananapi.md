- total memory is 1000Mb (disabled all memory reservations for GPU on CLI images)
- EDID detect video mode will fail on 4k monitor - you need to [set it manually](http://docs.armbian.com/Hardware_Allwinner/#how-to-reconfigure-video-output).
- drivers for [LVDS LCD display modules](http://www.lenovator.com/7-inch-LCD) are added. TS module: ft5x_ts, added configuration for 7″ – [other sizes](https://github.com/LeMaker/fex_configuration/tree/master/fex). (legacy kernel / [vanilla](https://github.com/igorpecovnik/lib/blob/master/patch/kernel/sunxi-next/bananapipro_lemaker_lcd.patch.disabled))

Connect your LCD display

I tried three different display connection types: I2C, (4bit) parallel and SPI. All of them are working perfectly with my image. I didn’t took a picture of the third one. It’s a standard Hitachi HD44780 based 20×4 LCD, wired and tested [according to Wiring(B)PI example](https://github.com/LeMaker/WiringBPi).

I2C

![](http://www.igorpecovnik.com/wp-content/uploads/2014/09/banana-i2c-display1.jpg)

I am using [this code](https://github.com/vvromanov/cb_i2c_lcd) for Vanilla kernel and with [changed line](https://github.com/vvromanov/cb_i2c_lcd/blob/master/i2c_lcd.c#L28): /dev/i2c-%u = /dev/i2c-2 for Legacy kernel.

SPI

![](http://www.igorpecovnik.com/wp-content/uploads/2014/09/banana-spi-display.jpg)

- I am using [2.4″ 240×320 SPI TFT LCD Serial Port Module+5/3.3V Pbc Adapter Micro SD ILI9341](http://www.google.com/search?q=2.4%E2%80%B3+240%C3%97320+SPI+TFT+LCD+Serial+Port+Module%2B5%2F3.3V+Pbc+Adapter+Micro+SD+ILI9341&oq=2.4%E2%80%B3+240%C3%97320+SPI+TFT+LCD+Serial+Port+Module%2B5%2F3.3V+Pbc+Adapter+Micro+SD+ILI9341)
- Wire according to [this map](http://blog.riyas.org/2014/07/quickly-test-il9341-22-inch-22-spi-tft-raspbmc-fbtft.html).
- You have to use Armbian 1.5 or newer. Currently working only under Legacy kernel.
- Add this to your /etc/modules:
`fbtft_device name=adafruit22a rotate=90 speed=48000000 fps=50 gpios=reset:25,led:19,dc:24`
- Reboot
- Test – display some picture on the screen:
`fbi -d /dev/fb2 -T 1 -noverbose -a yourimage.jpg`
- [Troubleshooting and settings for other displays
LVDS](https://github.com/notro/fbtft/wiki)

![](http://www.armbian.com/wp-content/uploads/2015/09/lvdsbanana.png)

Currently working only under Legacy kernel.

Image has pre-loaded settings for two LVDS display.

To enable 7 inch.

`ln -sf /boot/bin/bananapilcd7.bin /boot/script.bin`

To enable 5 inch.

`ln -sf /boot/bin/bananapilcd5.bin /boot/script.bin`

If you need touch screen support, add this module to your /etc/modules

`ft5x_ts`
