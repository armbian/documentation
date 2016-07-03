# Allwinner H3 boards

**Important to know**

- Updating Armbian images prior to 5.13 to 5.15 or higher is **not** recommended -- see below
- 1st boot takes longer (up to 5 minutes). Please do not interrupt while the red LED is blinking, the board reboots automatically one time and the green LED starts to blink when ready
- our [User documentation](http://www.armbian.com/documentation/) (one exception currently: use _h3disp_ to adjust display settings)
- our [Geek documentation](http://www.armbian.com/using-armbian-tools/) (in case you want to build your own images)
- CPU frequency settings are 240-1200 MHz on BPi M2+, NanoPi M1 and Beelink X2, 480-1200 MHz on OPi One/Lite and 480-1296 MHz on the other boards (cpufreq governor is _interactive_ therefore the boards only increase CPU speed and consumption when needed)
- In case you experience instabilities check your SD card using `armbianmonitor -c $HOME` and think about installing [RPi-Monitor for H3](http://www.cnx-software.com/2016/03/17/rpi-monitor-is-a-web-based-remote-monitor-for-arm-development-boards-such-as-raspberry-pi-and-orange-pi/) to get an idea whether you suffer from overheating (`sudo armbianmonitor -r` will install everything needed)
- In case you're unsure whether to test a desktop or CLI image simply try out the GUI version since you can always get 'CLI behaviour' by running `sudo update-rc.d -f nodm disable` later (this disables the start of X windows and desktop images behave like those made for headless use afterwards. If you're experienced you could also reclaim disk space by removing the `libxfce4util-common` package and doing an `apt-get autoremove` later)
- especially for desktop images the speed of your SD card matters. If possible try to use our _nand-sata-install_ script to move the rootfs away from SD card. The script also works with USB disks flawlessly ([some background information](http://forum.armbian.com/index.php/topic/793-moving-to-harddisk/))

**Upgrading from older images**

Upgrading from any of the H3 pre-built images (read as: all between version 5.03 and 5.12) is **not** recommended. We had one fundamental change while developing/improving H3 board support (switching away from providing one OS image for various boards and trying to rely on _board auto detection_ at first boot) that might cause loads of problems when upgrading.

Therefore it's strongly recommended to backup settings and `$HOME` contents, start with a fresh 5.15 OS image from scratch and then copy back stuff. We're sorry for any inconveniences caused by this and [provide a few tips/tweaks in the forum](http://forum.armbian.com/index.php/topic/1400-upgrading-h3-pre-built-armbian-images-to-515-or-above/)

# OS images with legacy Kernel (3.4.112)

Armbian started beginning with release 5.04 to support all available H3 based Orange Pi boards back then and extended the support to a few more H3 devices (also from other vendors) in the meantime. For a board overview you can look through our [buyer's guide](http://forum.armbian.com/index.php/topic/1351-h3-board-buyers-guide/) and/or Jean-Luc's [nice comparison table](http://www.cnx-software.com/2016/06/08/allwinner-h3-boards-comparison-tables-with-orange-pi-banana-pi-m2-nanopi-p1-and-h3-olinuxino-nano-boards/#comments).

**Known issues with 5.15**

- Playing HEVC/H.265 video with 10 bit depth not supported since H3 lacks this feature
- (still) not possible to upgrade _server_ to _desktop_ images -- better go the other way around if unsure

**What you can do to improve the situation**

- get back to us with [feedback regarding our OS images](http://forum.armbian.com/index.php/topic/617-wip-orange-pi-one-support-for-the-upcoming-orange-pi-one/?view=getlastpost)
- fork our repo, fix things and send pull requests

**Known to NOT work (reliably) yet**

- live display resolution switching. Fixes welcome (anyone willing to port the stuff from the [H3 OpenELEC port](https://github.com/jernejsk/OpenELEC-OPi2)?)

#OS images with vanilla Kernel (4.x)

**Important: Currently no thermal readouts and no throttling/cpufreq adjustments are implemented in mainline kernel (THS). Therefore it's possible to permanently damage your H3 when running demanding workloads on it. Keep this in mind especially when you use any of the H3 devices not from Xunlong since they all overheat badly and think about reducing maximum clockspeed in u-boot (816 MHz max for example)**

Mainlining effort for H3 and Orange Pi's is progressing nicely but since Ethernet is still missing some bits and especially THS support isn't ready we currently do not provide OS images with vanilla kernel. Our build system is already prepared, so as soon as THS and Ethernet are fully ready we'll release OS images (in the lab an Orange Pi PC is serving files as NAS since months stable with kernel 4.4 and USB-Ethernet and now 4.6.2 with native Ethernet driver).
