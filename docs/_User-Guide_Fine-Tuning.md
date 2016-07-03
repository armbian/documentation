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

# How to upgrade into simple desktop environment?

	apt-get -y install xorg lightdm xfce4 tango-icon-theme gnome-icon-theme
	reboot

Check [this site](http://namhuy.net/1085/install-gui-on-debian-7-wheezy.html) for others and be prepared that some desktop image features currently might not work afterwards (eg. 2D/3D/video HW acceleration, so downgrading a _desktop_ image, removing the `libxfce4util-common` package and doing an `apt-get autoremove` later might be the better idea in such cases)

# How to upgrade Debian from Wheezy to Jessie?

	dpkg -r ramlog	
	cp /etc/apt/sources.list{,.bak}
	sed -i -e 's/ \(old-stable\|wheezy\)/ jessie/ig' /etc/apt/sources.list
	apt-get update
	apt-get --download-only dist-upgrade
	apt-get dist-upgrade


# How to upgrade from Ubuntu Trusty to Xenial?

	apt-get install update-manager-core
	do-release-upgrade -d
  	# further to xenial
	apt-get dist-upgrade

# How to toggle boot output?

Edit and change [boot parameters](http://redsymbol.net/linux-kernel-boot-parameters/) in /boot/boot.cmd:

    - console=ttyS0,115200
    + console=tty1

and convert it to boot.scr with this command:

	mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr

Reboot.

Serial console on imx6 boards are ttymxc0 (Hummingboard, Cubox-i) or ttymxc1 (Udoo).

# How to toogle verbose boot?

    touch /boot/.force-verbose # enable

You need to reboot to conduct changes.

	rm /boot/.force-verbose # disable

# How to provide boot logs for inspection?

When computer behaves strange first step is to look into kernel logs. We made a tool that grabs info and paste it to the website.

	sudo armbianmonitor -b
	reboot
	sudo armbianmonitor -u  
Copy and past URL of your log to the forum, mail, ...

# How to change network configuration?

There are five predefined configurations, you can find them in those files:

	/etc/network/interfaces.default
	/etc/network/interfaces.hostapd	
	/etc/network/interfaces.bonding
	/etc/network/interfaces.r1
	/etc/network/interfaces.r1switch

By default **/etc/network/interfaces** is symlinked to **/etc/network/interfaces.default**

1. DEFAULT: your network adapters are connected classical way. 
2. HOSTAPD: your network adapters are bridged together and bridge is connected to the network. This allows you to have your AP connected directly to your router.
3. BONDING: your network adapters are bonded in fail safe / "notebook" way.
4. Router configuration for Lamobo R1 / Banana R1.
5. Switch configuration for Lamobo R1 / Banana R1.

You can switch configuration with re-linking.

	cd /etc/network
	ln -sf interfaces.x interfaces
(x = default,hostapd,bonding,r1)

Than check / alter your interfaces:

	nano /etc/network/interfaces

