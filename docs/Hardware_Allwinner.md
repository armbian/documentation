Enable Hardware Features
========================

Some boards require some manual configuration to turn on/off certain features

In some cases, the procedure is "less than obvious", so we document some basic examples here.

# Generic howto for Allwinner devices

## Legacy or Vanilla kernel ?

Many Armbian images come in two flavours : Legacy (using an older kernel version) and Vanilla (up-to-date kernel). Depending on kernel version, the procedure to enable/disable features is not the same :

 * Legacy kernel : FEX
 * Vanilla kernel : DT (Device Tree)

## How to reconfigure video output? ##

This affect Vanilla kernel only.

U-Boot supports hdmi and lcd output on Allwinner sunxi SoCs, lcd output requires the `CONFIG_VIDEO_LCD_MODE` Kconfig value to be set.

The sunxi U-Boot driver supports the following video-mode options:

- `monitor=[none|dvi|hdmi|lcd|vga|composite-*]` - Select the video output to use
 
 - `none`:     Disable video output.
 -  `dvi/hdmi`: Selects output over the hdmi connector with dvi resp. hdmi output format, if edid is used the format is automatically selected.
 -  `lcd`:      Selects video output to a LCD screen.
 -  `vga`:      Selects video output over the VGA connector.
 -  `composite-pal/composite-ntsc/composite-pal-m/composite-pal-nc`: Selects composite video output, note the specified resolution is ignored with composite video output.
 -  Defaults to `monitor=dvi`.

- `hpd=[0|1]` - Enable use of the hdmi HotPlug Detect feature
 0: Disabled. Configure dvi/hdmi output even if no cable is detected
 1: Enabled.  Fallback to the lcd / vga / none in that order (if available)
 Defaults to `hpd=1`.

- `hpd_delay=<int>` - How long to wait for the hdmi HPD signal in milliseconds
 When the monitor and the board power up at the same time, it may take some time for the monitor to assert the HPD signal. This configures how long to wait for the HPD signal before assuming no cable is connected.
 Defaults to `hpd_delay=500`.

- `edid=[0|1]` - Enable use of DDC + EDID to get monitor info
 0: Disabled.
 1: Enabled. If valid EDID info was read from the monitor the EDID info will overrides the xres, yres and refresh from the video-mode env. variable.
 Defaults to `edid=1`.

- `overscan_x/overscan_y=<int>` - Set x/y overscan value
 This configures a black border on the left and right resp. top and bottom to deal with overscanning displays. Defaults to `overscan_x=32` and `overscan_y=20` for composite monitors, 0 for other monitors.

For example to always use the hdmi connector, even if no cable is inserted, using edid info when available and otherwise initalizing it at 1024x768@60Hz, use: `setenv video-mode sunxi:1024x768-24@60,monitor=dvi,hpd=0,edid=1`.

## What flavour am I using ?

Best way to know is by checking your kernel version :

```
root@bananapipro:~# uname -a
Linux bananapipro 4.5.2-sunxi #11 SMP Thu Apr 28 21:53:25 CEST 2016 armv7l GNU/Linux
```

In this example the kernel version is 4.5.2 so you can use DT to tweak some settings. If you get a kernel version 3.X then you'll be certainly using FEX like on an Orange Pi Plus 2E :

```
root@orangepiplus2e:~# uname -a
Linux orangepiplus2e 3.4.112-sun8i #10 SMP PREEMPT Wed Jun 1 19:43:08 CEST 2016 armv7l GNU/Linux
```

## FEX

### Which file should I edit

Armbian embed a lot of BIN files, but a symlink point to the one in use :

```
root@orangepiplus2e:~# ls -la /boot/script.bin
lrwxrwxrwx 1 root root 22 Jun  1 20:30 /boot/script.bin -> bin/orangepiplus2e.bin
```

### Updating a FEX

You may need to use `sudo` with all the following commands.

The whole process won't overwrite any of your files. If you're paranoid, you can make a proper backup of your BIN file :

```
cp /boot/script.bin /boot/bin/script.bin.backup
```

Then you can decompile your BIN into a FEX :

```
bin2fex /boot/script.bin /tmp/custom.fex
```

Finally you can edit your FEX file with your favorite text editor and compile it back to a BIN :

```
fex2bin /tmp/custom.fex /boot/bin/custom.bin
```

The last step is to change the symlink to use your custom BIN :

```
ln -sf /boot/bin/custom.bin /boot/script.bin
```

## Device Tree

### Which file should I edit

I use the following command and try to guess which file to use in `/boot/dtb/` :

```
cat /proc/device-tree/model
```

# H3 based Orange Pi, legacy kernel

## Enable serial /dev/ttyS3 on pins 8 and 10 of the 40 pin header

Update the FEX configuration (which is compiled into a .bin) located at /boot/script.bin

Decompile .bin to .fex
```
cd /boot
bin2fex script.bin > custom.fex
rm script.bin # only removes symbolic link
```

Edit .fex file
```
[uart3]
uart_used = 1 ; Change from 0 to 1
uart_port = 3
uart_type = 2 ; In this case we have a 2 pin UART
uart_tx = port:PA13<3><1><default><default>
uart_rx = port:PA14<3><1><default><default>
```

Compile .fex to .bin
```
fex2bin custom.fex > script.bin
```

Reboot

Notice that /dev/ttyS3 appears. That is your new UART device.

****
