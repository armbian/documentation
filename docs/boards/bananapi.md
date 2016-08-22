- total memory is 1000Mb (disabled all memory reservations for GPU on CLI images)
- EDID detect video mode will fail on 4k monitor - you need to [set it manually](http://docs.armbian.com/Hardware_Allwinner/#how-to-reconfigure-video-output).
- drivers for [LVDS LCD display modules](http://www.lenovator.com/7-inch-LCD) are added. TS module: ft5x_ts, added configuration for 7″ – [other sizes](https://github.com/LeMaker/fex_configuration/tree/master/fex). (legacy kernel / [vanilla](https://github.com/igorpecovnik/lib/blob/master/patch/kernel/sunxi-next/bananapipro_lemaker_lcd.patch.disabled))

