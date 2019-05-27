# How to switch kernels?

Check [this for](http://www.armbian.com/kernel/) more info.

# How to troubleshoot?

**Important: If you came here since you can't get Armbian running on your board please keep in mind that in 95 percent of all cases it's either a faulty/fraud/counterfeit SD card or an insufficient power supply that's causing these sorts of _doesn't work_ issues!**

If you broke the system you can try to get in this way. You have to get to u-boot command prompt, using either a serial adapter or monitor and usb keyboard (USB support in u-boot currently not enabled on all H3 boards).

After switching power on or rebooting, when u-boot loads up, press some key on the keyboard (or send some key presses via terminal) to abort default boot sequence and get to the command prompt:

	U-Boot SPL 2015.07-dirty (Oct 01 2015 - 15:05:21)
	...
	Hit any key to stop autoboot:  0
	sunxi#

Enter these commands, replacing root device path if necessary. Select setenv line with ttyS0 for serial, tty1 for keyboard+monitor (these are for booting with mainline kernel, check boot.cmd for your device for commands related to legacy kernel):

	setenv bootargs init=/bin/bash root=/dev/mmcblk0p1 rootwait console=ttyS0,115200
	# or
	setenv bootargs init=/bin/bash root=/dev/mmcblk0p1 rootwait console=tty1

	ext4load mmc 0 0x49000000 /boot/dtb/${fdtfile}
	ext4load mmc 0 0x46000000 /boot/zImage
	env set fdt_high ffffffff
	bootz 0x46000000 - 0x49000000

System should eventually boot to bash shell:

	root@(none):/#

Now you can try to fix your broken system.


- [Fix a Jessie systemd problem due to upgrade from 3.4 to 4.x](https://github.com/igorpecovnik/lib/issues/111)

# How to unbrick the system?

When something goes terribly wrong and you are not able to boot the system, this is the way to proceed. You need some linux machine, where you can mount the failed SD card. With this procedure you will reinstall the u-boot, kernel and hardware settings. In most cases this should be enough to unbrick the board. It's recommended to issue a filesystem check before mounting:

	fsck /dev/sdX -f

Than mount the SD card and download those files (This example is only for Banana R1):

	http://apt.armbian.com/pool/main/l/linux-trusty-root-next-lamobo-r1/linux-trusty-root-next-lamobo-r1_4.5_armhf.deb
	http://apt.armbian.com/pool/main/l/linux-upstream/linux-image-next-sunxi_4.5_armhf.deb
	http://apt.armbian.com/pool/main/l/linux-upstream/linux-firmware-image-next-sunxi_4.5_armhf.deb
	http://apt.armbian.com/pool/main/l/linux-upstream/linux-dtb-next-sunxi_4.5_armhf.deb
	 

This is just an example for: **Ubuntu Trusty, Lamobo R1, mainline kernel** (next). Alter packages naming according to [this](https://forum.armbian.com/topic/211-kernel-update-procedure-has-been-changed/).

Mount SD card and extract all those deb files to it's mount point.

	dpkg -x DEB_FILE /mnt

Go to /mnt/boot and link (or copy) **vmlinuz-4.x.x-sunxi** kernel file to **zImage**.

If you upgrade from some very old build, you might need to update your boot script. Example goes for Allwinner boards:

	cd /mnt/boot
	wget https://raw.githubusercontent.com/armbian/build/master/config/bootscripts/boot-sunxi.cmd
	mv boot-sunxi.cmd boot.cmd
	mkimage -C none -A arm -T script -d boot.cmd boot.scr # you need a u-boot-tools package on your host system

Unmount SD card, move it to the board and power on.

# How to build a wireless driver?

Install and recreate kernel headers scripts (optional)

	armbian-config -> install kernel headers
	exit

	cd /usr/src/linux-headers-$(uname -r)
	make scripts

Go back to root directory and fetch sources (working example, use ARCH=arm64 on 64bit system)

	cd
	git clone https://github.com/pvaret/rtl8192cu-fixes.git
	cd rtl8192cu-fixes
	make ARCH=arm
Load driver for test

	insmod 8192cu.ko

Check dmesg and the last entry will be:

	usbcore: registered new interface driver rtl8192cu

Plug the USB wireless adaptor and issue a command:

	iwconfig wlan0
You should see this:

	wlan0   unassociated  Nickname:"<WIFI@REALTEK>"
			Mode:Auto  Frequency=2.412 GHz  Access Point: Not-Associated
			Sensitivity:0/0
			Retry:off   RTS thr:off   Fragment thr:off
			Encryption key:off
			Power Management:off
			Link Quality=0/100  Signal level=0 dBm  Noise level=0 dBm
			Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
			Tx excessive retries:0  Invalid misc:0   Missed beacon:0

Check which wireless stations / routers are in range

	iwlist wlan0 scan | grep ESSID

# How to freeze your filesystem?

In certain situations it is desirable to have a virtual read-only root filesystem. This prevents any changes from occurring on the root filesystem that may alter system behavior and it allows a simple reboot to restore a system to its clean state.

You need an ODROID XU4 or Allwinner A10, A20 or H3 board with legacy kernel where we added support for overlayfs. Works only on Ubuntu Xenial. Login as root and execute:

	apt-get install overlayroot
	echo 'overlayroot="tmpfs"' >> /etc/overlayroot.conf
	reboot

After your system boots up it will always remain as is. If you want to make any permanent changes, you need to run:

	overlayroot-chroot

Changes inside this will be preserved.

# How to run Docker?

Preinstallation requirements:

- Armbian 5.1 or newer with Kernel 3.10 or higher
- Debian Jessie (might work elsewhere with some modifications)
- root access

Execute this as root:

	curl  https://get.docker.com | sh

Test if Docker works correctly:

	docker run -d -p 80:80 hypriot/rpi-busybox-httpd

... and point the browser of any device in the same network to `http://<IP OF YOUR DEVICE>/`

[More info in this forum topic](https://forum.armbian.com/topic/490-docker-on-armbian/)

# How to set wireless access point?

There are two different hostap daemons. One is **default** and the other one is for some **Realtek** wifi cards. Both have their own basic configurations and both are patched to gain maximum performances.

Sources: [https://github.com/igorpecovnik/hostapd](https://github.com/igorpecovnik/hostapd "https://github.com/igorpecovnik/hostapd")

Default binary and configuration location:

	/usr/sbin/hostapd
	/etc/hostapd.conf

Realtek binary and configuration location:

	/usr/sbin/hostapd-rt
	/etc/hostapd.conf-rt

Since its hard to define when to use which you always try both combinations in case of troubles. To start AP automatically:

1. Edit /etc/init.d/hostapd and add/alter location of your conf file **DAEMON_CONF=/etc/hostapd.conf** and binary **DAEMON_SBIN=/usr/sbin/hostapd**
2. Copy **/etc/network/interfaces.hostapd** to **/etc/network/interfaces**
3. Reboot
4. Predefined network name: "BOARD NAME" password: 12345678
5. To change parameters, edit /etc/hostapd.conf BTW: You can get WPAPSK the long blob from wpa_passphrase YOURNAME YOURPASS

# How to connect IR remote?

Required conditions:

- IR hardware
- loaded driver

Get your [remote configuration](http://lirc.sourceforge.net/remotes/) (lircd.conf) or [learn](http://kodi.wiki/view/HOW-TO:Setup_Lirc#Learning_Commands). You are going to need the list of all possible commands which you can map to your IR remote keys:

	irrecord --list-namespace

To start with learning process you need to delete old config:

	rm /etc/lircd.conf

Than start the process with:

	irrecord --driver=default --device=/dev/lirc0 /etc/lircd.conf

And finally start your service when done with learning:

	service lirc start

Test your remote:

	irw /dev/lircd
****
