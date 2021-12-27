# Recovery

**Important: If you came here since you cannot get Armbian running on your board please keep in mind that in 95 percent of all cases it is either a faulty/fraud/counterfeit [SD card or an insufficient power supply](User-Guide_Basic-Troubleshooting.md) that is causing these sorts of _does not work_ issues!**

The following are presented in (more or less) increasing levels of despair.  But keep heart!  :)  And proceed in order.


## U-Boot Shell Access

If you broke the system you can try to get in this way.  You have to get to u-boot command prompt, using either a serial adapter or monitor and usb keyboard.

- Note: USB support in u-boot is currently not enabled on all H3 boards.

After switching power on or rebooting, when u-boot loads up, press some key on the keyboard (or send some key presses via terminal) to abort default boot sequence and get to the command prompt:

``` console
U-Boot SPL 2015.07-dirty (Oct 01 2015 - 15:05:21)
...
Hit any key to stop autoboot:  0
sunxi#
```

Enter the following commands, replacing root device path if necessary.

- Note: these are for booting with mainline kernel; check `boot.cmd` for your device for commands related to legacy kernel.

For serial:

``` console
sunxi# setenv bootargs init=/bin/bash root=/dev/mmcblk0p1 rootwait console=ttyS0,115200
```

For monitor:

``` console
sunxi# setenv bootargs init=/bin/bash root=/dev/mmcblk0p1 rootwait console=tty1
```

Then:

``` console
sunxi# ext4load mmc 0 0x49000000 /boot/dtb/${fdtfile}
sunxi# ext4load mmc 0 0x46000000 /boot/zImage
sunxi# env set fdt_high ffffffff
sunxi# bootz 0x46000000 - 0x49000000
```

System should eventually boot to bash shell:

``` console
root@host:/#
```

Now you can try to fix your broken system.


## Replacing /boot

When something goes terribly wrong and you are not able to boot the system (and cannot gain access via u-boot as outlined above), this is the way to proceed.  You will need some Debian based Linux machine where you can mount the failed SD card.  With this procedure you will reinstall the kernel and hardware settings.  In most cases this should be enough to unbrick the board.

It is recommended to issue a filesystem check before mounting.  Replace `X` and `Y` below with your device and partition(s), respectively (if not a flash based device, it may even be `/dev/sdXY`, etc).

``` console
/ # fsck /dev/mmcblkXpY -f
```
	
Mount the SD card.

``` console
/ # cd /mnt
/mnt # mkdir sdcard
/mnt # mount /dev/mmcblkXpY /mnt/sdcard
```

Make another temporary directory somewhere else (in our example `~/tmp/recovery`) and download the Linux root, kernel, firmware and dtb packages for your board and currently used OS.

- Note: This example is only for **Nanopi Neo 2** with **Ubuntu Focal**, **current** kernel (mainline) and **Armbian 20.08.13** firmware.  Alter package names according to your device name, SOC-family, kernel and firmware version!

``` console
/mnt $ cd
~ $ mkdir -p tmp/recovery
~ $ cd tmp/recovery

(Root file system):
~/tmp/recovery $ wget https://apt.armbian.com/pool/main/l/linux-focal-root-current-nanopineo2/linux-focal-root-current-nanopineo2_20.08.13_arm64.deb

(Kernel):
~/tmp/recovery $ wget https://apt.armbian.com/pool/main/l/linux-5.8.16-sunxi64/linux-image-current-sunxi64_20.08.13_arm64.deb

(Firmware):
~/tmp/recovery $ wget https://apt.armbian.com/pool/main/a/armbian-firmware/armbian-firmware_20.08.13_all.deb

(Device Tree Binary (DTB)):
~/tmp/recovery $ wget https://apt.armbian.com/pool/main/l/linux-5.8.16-sunxi64/linux-dtb-current-sunxi64_20.08.13_arm64.deb
```

Extract all the Debian packages (`.deb` files) to the mounted sd card.

``` console
~/tmp/recovery # for f in *.deb; do dpkg -x $f /mnt/sdcard; done
```

Navigate to `/mnt/sdcard/boot` and create symlinks:

``` console
~/tmp/recovery # cd /mnt/sdcard/boot
/mnt/sdcard/boot # ln -s vmlinuz-5.8.16-sunxi64 zImage
/mnt/sdcard/boot # ln -s uInitrd-5.8.16-sunxi64 uInitrd
/mnt/sdcard/boot # ln -s dtb-5.8.16 dtb
```

If you upgrade from some very old build, you might need to update your boot script.

- Note: The following example is for Allwinner boards.

- Note: You will need a `u-boot-tools` package on your host system.

``` console
/mnt/sdcard/boot # wget https://raw.githubusercontent.com/armbian/build/master/config/bootscripts/boot-sunxi.cmd
/mnt/sdcard/boot # mv boot-sunxi.cmd boot.cmd
/mnt/sdcard/boot # mkimage -C none -A arm -T script -d boot.cmd boot.scr
```

Unmount SD card.

``` console
/mnt/sdcard/boot # cd /
/ # umount /mnt/sdcard
```

Move it to the board and power on.  Check serial output for errors if problems persist.

## Flashing boot loader

Sometimes we need to flash boot loader from some other Linux. Attach an SD card reader with your SD card and proceed this way:

``` console
/mnt $ cd
~ $ mkdir -p tmp/recovery
~ $ cd tmp/recovery
~ $ wget https://imola.armbian.com/apt/pool/main/l/linux-u-boot-nanopineo2-current/linux-u-boot-current-nanopineo2_20.08.13_arm64.deb
~ $ dpkg-deb -x linux-u-boot-current-nanopineo2_20.08.13_arm64.deb pack
~ $ bash pack/usr/lib/u-boot/platform_install.sh pack/usr/lib/linux-u-boot-nanopineo2-current /dev/XXX # replace XXX with the actual device /dev/sdb
```

Move it to the board and power on.  Check serial output for errors if problems persist.
