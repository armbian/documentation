# How to customize keyboard, time zone?

keyboard: 

	dpkg-reconfigure keyboard-configuration
	
system language:

	# Debian --> https://wiki.debian.org/ChangeLanguage
	dpkg-reconfigure locales
	# Ubuntu --> https://help.ubuntu.com/community/Locale
	update-locale LANG=[options] && dpkg-reconfigure locales

console font, codepage:

	dpkg-reconfigure console-setup

time zone: 

	dpkg-reconfigure tzdata
	
screen settings on H3 devices:

	# Example to set resolution to 1920 x 1080, full colour-range and DVI
	h3disp -m 1080p60 -d -c 1

screen resolution on other boards: 

	nano /boot/boot.cmd 

	# example:
	# change example from 
	# disp.screen0_output_mode=1920x1080p60 
	# to 
	# disp.screen0_output_mode=1280x720p60

	mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr

screen resolution interactive - only Allwinner boards with A10 and A20 with legacy kernel:
	
	# Example to set console framebuffer resolution to 1280 x 720
	a10disp changehdmimodeforce 4

Other modes:

	0 480i
	1 576i
	2 480p
	3 576p
	4 720p 50Hz
	5 720p 60Hz
	6 1080i 50 Hz
	7 1080i 60 Hz
	8 1080p 24 Hz
	9 1080p 50 Hz
	10 1080p 60 Hz
	
# How to alter CPU frequency?

Some boards allow to adjust CPU speed.

	nano /etc/default/cpufrequtils

Alter **min_speed** or **max_speed** variable.

	service cpufrequtils restart

# How to downgrade a package via apt-get?

This is useful when you need to fall back to previous kernel version. 

	apt-get install linux-image-sun8i=5.13

This example is for H3 legacy kernel. Check [this page](http://www.armbian.com/kernel/) for others.

# How to toggle boot output?

Edit and change [boot parameters](http://redsymbol.net/linux-kernel-boot-parameters/) in `/boot/boot.cmd` (not recommended) or variables in `/boot/armbianEnv.txt`:

    - console=both
    + console=serial

Recompile boot.cmd to boot.scr if it was changed:

	mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr

Reboot.

Serial console on imx6 boards are ttymxc0 (Hummingboard, Cubox-i) or ttymxc1 (Udoo).

# How to toggle verbose boot?

Using Armbian 5.05 to 5.20 you would need to touch/rm `/boot/.force-verbose` to increase boot verbosity. With more recent Armbian builds you would have to alter the `verbosity=` line in `/boot/armbianEnv.txt` (defaults to 1 which means less verbose, maximum value is 7).

# How to provide boot logs for inspection?

When computer behaves strange first step is to check power supply and integrity of boot media (`armbianmonitor -c "$HOME"`). Then look into kernel logs. We made a tool that grabs info and paste it to an online pasteboard service. Please increase boot verbosity as shown above (`verbosity=7`), reboot and then run

	sudo armbianmonitor -u
	
Copy and past URL of your log to the forum, mail, ...

# How to change network configuration?

To get Wi-Fi working simply use `nmtui`, a simple console based UI for network-manager (an example how to set up an AP with network-manager can be found [here](http://forum.odroid.com/viewtopic.php?f=52&t=25472&)). To deal with different Ethernet/Wi-Fi combinations there are six predefined configurations available, you can find them in those files:

	/etc/network/interfaces.bonding
	/etc/network/interfaces.default
	/etc/network/interfaces.hostapd
	/etc/network/interfaces.network-manager
	/etc/network/interfaces.r1
	/etc/network/interfaces.r1switch

By default **/etc/network/interfaces** is a copy of **/etc/network/interfaces.default**

1. BONDING: your network adapters are bonded in fail safe / "notebook" way.
2. DEFAULT: your network adapters are connected classical way. 
3. HOSTAPD: your network adapters are bridged together and bridge is connected to the network. This allows you to have your AP connected directly to your router.
4. All interfaces are handled by network-manager (`nmtui`/`nmcli` or using the GUI) 
4. Router configuration for Lamobo R1 / Banana R1.
5. Switch configuration for Lamobo R1 / Banana R1.

You can switch configuration with copying.

	cd /etc/network
	cp interfaces.x interfaces
	
(x = default,hostapd,bonding,r1)

Then check / alter your interfaces:

	nano /etc/network/interfaces

