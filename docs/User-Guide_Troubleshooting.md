# Hardware troubleshooting guide

First aid video guide:
<iframe width="560" height="315" src="https://www.youtube.com/embed/UpVMO7gbnYM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

If you are experiencing at least one of these problems:

- board does not boot
- board freezes, crashes or reboots randomly or when connecting USB devices
- plugged in USB devices are not detected (not listed in `lsusb` output)
- error changing the root password at first boot (Authentication token manipulation error)
- error installing or updating packages due to read-only file system

and you are using a stable Armbian image, then most likely you have one of two common problems - **powering issue** or **SD card issue**.

Note that

- _"I know that my power supply is good", "it worked yesterday", "it works with a different device",_ etc. are **not objective reasons** to skip powering related diagnostics
- _"I know that my SD card is good", "it worked yesterday", "it works with a different device",_ etc. are **not objective reasons** to skip storage related diagnostics
- undervoltage can cause symptoms related to SD card problems such as filesystem corruptions and data loss, so powering has to be checked first


## Powering notes

- Most boards, even ones fitted with PMIC (power management integrated circuit) do not have any measures to react to undervoltage that could prevent instability
- It does not matter what voltage your power supply outputs, it matters what voltage will reach the onboard voltage regulators
- Peak power consumption of popular boards can vary from 0.9A at 5V (H3 based Orange Pi PC) to 1.7A at 5V (RK3288 based Tinkerboard), both without any attached peripherials like USB devices
- Due to the Ohm's law voltage drop due to cable and connector resistance will be proportional to the electric current, so most of the time problems will be experienced at current spikes caused by CPU load or peripherials like spinning up HDDs


### Power supply

- Cheap phone chargers may not provide the current listed on their label, especially for long time periods
- Some cheap phone chargers don't have proper feedback based stabilization, so output voltage may change depending on load
- Power supplies will degrade over time (especially when working 24/7)
- Some problems like degraded output filtering capacitors cannot be diagnosed even with a multimeter because of the non-linear voltage form


### Cable

- The longer and thinner the cable - the higher its resistance - the greater the voltage drop will be under load
- Even thick looking cable can have thin wires inside, so do not trust the outside cable diameter


### Connector

- MicroUSB connector is rated for the maximum current of 1.8A, but even this number cannot be guaranteed. Trying to pass larger current (even momentarily) may result in a voltage dropping below USB specifications
- Most of the boards can also be powered through GPIO pins. This can be used to bypass the microUSB connector and thus to improve stability


## SD card

- A SD card is a complex storage device with an embedded controller that processes read, erase and write operations, wear leveling, error and corruption detection, but it does not provide any diagnostic protocols like S.M.A.R.T.
- SD cards will degrade over time and may fail in the end in different ways - become completely or partially read-only or cause a silent data corruption


### SD card brand

- Based on current prices and performance tests done by Armbian users Samsung Evo, Samsung Evo Plus and Sandisk Ultra cards are recommended
- Other good alternatives may be added to this page in the future


### SD card size and speed class

- SD card speed class and size does not influence the reliability directly, but larger size means larger amount of lifetime data written, even if you are using 10-20% of the cards space


### SD card testing

- There are many fake SD card around. eBay and Amazon Marketplace are notorious for selling fakes, but sometimes even reputable retailers get fooled.
- Most commonly low capacity cards will be reprogrammed to appear as bigger, but any files written beyond the true capacity will be lost or corrupted.
- We recommend to always [test the capacity of each new SD cards using f3](https://fight-flash-fraud.readthedocs.io/en/latest/usage.html).


### Writing images to the SD card

- If you wrote an image to the card it does not mean that it was written successfully without any errors
- so always verify images after write using some tools like _balenaEtcher_ which is currently the only popular and cross-platform tool that does mandatory verify on write (more lightweight alternatives may be added to this page in the future)
- "Check for bad blocks" function available in some tools is mostly useless when dealing with SD cards
- Note that _balenaEtcher_ verifies only 1-2GB that are occupied by the initial unresized image, it does not verify the whole SD card


## Network


### MAC Address Conflicts

If you experience strange network problems, especially if you are running several of these SOC-boards with the same operating system, then the problems may be sourced by not having a real hardware MAC address. The operating systems try to generate a hardware MAC address from the CPUid, but what if that SOC has no CPUid either?

Then you have to do it manually. Depending on system and network installation, there are several possibilities:

- the preferred way: change `/boot/armbianEnv.txt` and add a line:

        ethaddr=XX:XX:XX:XX:XX:XX

but that file is interpreted by u-boot, which happens early in boot process, but not every u-boot is able to read that file.

- next possibility to set mac-address is changing network configuration. On systems with **ifupdown** you can do that by changing `/etc/network/interfaces`. Add these lines:

        auto eth0
        iface eth0 inet dhcp
            hwaddress ether XX:XX:XX:XX:XX:XX

- if the above does not work, then your network is probably controlled by **Network-manager** . In directory `/etc/Networkmanager/system-connections` is a file `Wired connection 1.nmconnection`. Change entry _cloned-mac-address_ of group **[ethernet]** :

        [connection]
        id=Wired connection 1
        type=ethernet

        [ethernet]
        cloned-mac-address=XX:XX:XX:XX:XX:XX


## Video


### No Screen on 4k Resolution

Some combination of boards/kernel versions does not support 4k resolution. This may cause black screen on connecting the board to 4k resolution devices. A workaround to solve this without changing the kernel is forcing the video mode to 1080p. Add this directive to the `/boot/armbianEnv.txt` and reboot your system:

    extraargs=video=HDMI-A-1:1920x1080@60

 - Despite of this config, some apps may try to use 4k resolution, example: _Retroarch_. In this case you have to change app configuration to use the 1080p resolution.

 - To edit files without video you could connect to the board using ssh. Other option is mount the sd card in another device.


## Board configuration

- Some boards require the setup of the correct device tree file or they will not boot. Check the board specific documentation for details.


## Recovery

In 95 percent of all cases it is either a faulty/fraud/counterfeit [SD card](#sd-card) or an [insufficient power supply](#power-supply) that is causing all sorts of _does not work_ issues! So, please, make sure you checked the sections above before proceeding.

The following options are presented in (more or less) increasing levels of despair.  But keep heart!  :)  And proceed in order.


### U-Boot Shell Access

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


### Replacing /boot

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


### Flashing boot loader

Sometimes we need to flash boot loader from some other Linux. Attach an SD card reader with your SD card and proceed this way:

``` console
/mnt $ cd
~ $ mkdir -p tmp/recovery
~ $ cd tmp/recovery
~ $ wget https://imola.armbian.com/apt/pool/main/l/linux-u-boot-nanopineo2-current/linux-u-boot-current-nanopineo2_20.08.13_arm64.deb
~ $ dpkg-deb -x linux-u-boot-current-nanopineo2_20.08.13_arm64.deb pack
~ $ source pack/usr/lib/u-boot/platform_install.sh
~ $ write_uboot_platform pack/usr/lib/linux-u-boot-nanopineo2-current /dev/XXX # replace XXX with the actual device /dev/sdb
```

Move it to the board and power on.  Check serial output for errors if problems persist.
