# Customize the Armbian system

<!-- TODO: Probably move stuff like sound or screen resolution to Advanced tasks?? Or at least some?? -->

While the underlying operating system offers tools and processes to make customizations, the **preferred method** to change most settings is using the interactive [_armbian-config_](User-Guide_Armbian-Config.md) tool which is shipped with all Armbian images. It also provides means to install [preconfigured applications and advanced services](User-Guide_Armbian-Software.md).

Usually all of the following commands require elevated permissions, and must be run as root or prefixed by the _sudo_ command.


## Keyboard layout

This is typically handled by [_armbian-config_](TODO). For some corner cases, changing the keyboard layout can also be done with:

```sh
dpkg-reconfigure keyboard-configuration
```

If the chosen standard is not available with the previous command, you may also need to set the keymap config.

```sh
# Check the actual keymap config
localectl status | grep -i keymap

# Set the desired keymap config. In the example below it is set to 'br-abnt2'
localectl set-keymap br-abnt2
```


## System language

This is typically handled by [_armbian-config_](TODO). If necessary, to handle it with system tools, for [Debian](https://wiki.debian.org/ChangeLanguage) run:

```sh
dpkg-reconfigure locales
```

And for [Ubuntu](https://help.ubuntu.com/community/Locale)

```sh
update-locale LANG=[options] && dpkg-reconfigure locales
```


## Console font and codepage

```sh
dpkg-reconfigure console-setup
```


## Time zone

This is typically handled by [_armbian-config_](TODO). If necessary, one can also run:

```sh
dpkg-reconfigure tzdata
```


## Sound output:

	# Check the available sound output options:
	pacmd list-sinks | less
	# The default will be marked with "*"
	# Press "q" to close


	# Define the new default sound output
	pacmd set-default-sink <NAME-OF-DESIRED-OPTION>


The name of HDMI sound output may change accordingly to the device. If you don't wanna deal with different names you can:

	pacmd set-default-sink $(pactl list short sinks | grep -i 'hdmi' | awk '{print $2}')

The command to define the default sound output is not persistent, to make it persistent add it to the file `~/.bashrc`

## Screen resolution on other boards:

	nano /boot/boot.cmd

	# example:
	# change example from
	# disp.screen0_output_mode=1920x1080p60
	# to
	# disp.screen0_output_mode=1280x720p60

	mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr

## Screen resolution within Xorg

- Thanks to user @maxlinux2000 in [this](https://forum.armbian.com/topic/10403-add-undetected-hdmi-resolution-to-x11xorg/) forum post.

Find matching HDMI output:

	xrandr --listmonitors

Calculate VESA CVT mode lines (example for 1440x900)

	cvt 1440 900

Sample output:

	1440x900 59.89 Hz (CVT 1.30MA) hsync: 55.93 kHz; pclk: 106.50 MHz
	Modeline "1440x900_60.00"  106.50  1440 1528 1672 1904  900 903 909 934 -hsync +vsync )

Create new mode (example):

	xrandr --newmode "1440x900_60.00" 106.50 1440 1528 1672 1904 900 903 909 934 -hsync +vsync

Add resolution (example):

	xrandr --addmode HDMI-1 1440x900_60.00

Set current resolution (example):

	xrandr --output HDMI-1 --mode 1440x900_60.00

If it works as expected add it to Xorg by editing `/etc/X11/xorg.conf.d/40-monitor.conf` and add (example):

	Section "Monitor"
	Identifier "HDMI-1"
	Modeline "1440x900_60.00" 106.50 1440 1528 1672 1904 900 903 909 934 -hsync +vsync
	Option "PreferredMode" "1440x900"
	EndSection

Restart Xorg or reboot

## How to alter CPU frequency?

Some boards allow to adjust CPU speed

	nano /etc/default/cpufrequtils

Alter **min_speed** or **max_speed** variable.

	systemctl restart cpufrequtils

## Swap for experts

By default Armbian implements ZRAM (writing nothing to 'disk' but compressing memory pages in RAM) but in case you often run into out of memory errors and your device has some capable storage (e.g. a securely attached NVMe or SATA SSD) you might want to use ZSWAP instead.

Check whether your kernel has zswap enabled (`dmesg | grep zswap` should output something) and if so create a swapfile or swap partition the traditional way, edit/uncomment `/etc/default/armbian-zram-config` so that it reads `SWAP=false`, reboot and you're done.

Zswap performs a lot better than the combination of ZRAM and 'swap on disk' in parallel.

## How to downgrade a package via apt?

This is useful when you need to fall back to previous kernel version.

	apt install linux-image-sun8i=5.13

This example is for H3 legacy kernel. Check [this page](https://www.armbian.com/kernel/) for others.

## How to toggle boot output?

Edit and change [boot parameters](http://redsymbol.net/linux-kernel-boot-parameters/) in `/boot/boot.cmd` (not recommended) or variables in `/boot/armbianEnv.txt`:

    - console=both
    + console=serial

To disable console entirely (not recommended) set console to `none`.  

Recompile boot.cmd to boot.scr if it was changed:

	mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr

Reboot.

Serial console on imx6 boards are ttymxc0 (Hummingboard, Cubox-i) or ttymxc1 (Udoo).

## How to toggle verbose boot?

Using Armbian 5.05 to 5.20 you would need to touch/rm `/boot/.force-verbose` to increase boot verbosity. With more recent Armbian builds you would have to alter the `verbosity=` line in `/boot/armbianEnv.txt` (defaults to 1 which means less verbose, maximum value is 7).

## How to provide boot logs for inspection?

When your SBC behaves strange first step is to check power supply and integrity of boot media (`armbianmonitor -c "$HOME"`). Then look into your kernel logs. We made a tool that grabs info and pastes it to an online pasteboard service. Please increase boot verbosity as shown above (`verbosity=7`), reboot and then run

	sudo armbianmonitor -u

Copy and past URL of your log to the forum, mail, ...

## How to change network configuration?

To get Wi-Fi working simply use `nmtui`, a simple console based UI for network-manager (an example how to set up an AP with network-manager can be found [here](https://forum.odroid.com/viewtopic.php?f=52&t=25472&)). To deal with different Ethernet/Wi-Fi combinations there are six predefined configurations available, you can find them in those files:

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

## Choosing an apt mirror

Armbian has its own apt repository and mirrors for armbian-specific packages.  The default of `http://apt.armbian.com` is a round-robin to all mirrors.   If you are having trouble updating or slow speeds you may want to choose a specific mirror.

Do the following:

Assure `jq` is installed

`apt install -y jq`

Get a list of available mirrors from our `https://apt.armbian.com/mirrors` endpoint.

```bash
curl -s http://apt.armbian.com/mirrors | jq
```

You will see a result set similar to this, listing mirrors by region:
```json
{
  "AS": [
    "https://mirrors.tuna.tsinghua.edu.cn/armbian/",
    "https://minio.k-space.ee/armbian/apt/"
  ],
  "NA": [
    "https://armbian.tnahosting.net/apt/",
    "https://us.mirrors.fossho.st/armbian/apt/"
  ],
  "EU": [
    "https://minio.k-space.ee/armbian/apt/",
    "https://armbian.systemonachip.net/apt/",
    "https://mirrors.netix.net/armbian/apt/",
    "https://mirrors.dotsrc.org/armbian-apt/",
    "https://armbian.hosthatch.com/apt/"
  ],
  "default": [
    "https://armbian.tnahosting.net/apt/",
    "https://us.mirrors.fossho.st/armbian/apt/",
    "https://minio.k-space.ee/armbian/apt/",
    "https://armbian.systemonachip.net/apt/",
    "https://mirrors.netix.net/armbian/apt/",
    "https://mirrors.dotsrc.org/armbian-apt/",
    "https://armbian.hosthatch.com/apt/"
  ]
}
```

Edit `/etc/apt/sources.list.d/armbian.sources` and replace the URL `https://apt.armbian.com` with your preferred mirror.
