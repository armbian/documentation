# Advanced features and tasks

While the underlying operating system offers tools and processes to make customizations, the **preferred method** to change most settings is using the interactive [_armbian-config_](User-Guide_Armbian-Config.md) tool which is shipped with all Armbian images. It also provides means to install [preconfigured applications and advanced services](User-Guide_Armbian-Software.md).

Usually, all of the following commands require elevated permissions, and must be run as root or prefixed by the _sudo_ command.


## Keyboard layout

This is typically handled by [_armbian-config_](User-Guide_Armbian-Config/Localisation.md#change-keyboard-layout). For some corner cases, changing the keyboard layout can also be done with:

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

This is typically handled by [_armbian-config_](User-Guide_Armbian-Config/Localisation.md#change-locales-reconfigure-the-language-and-character-set). If necessary, to handle it with system tools, for [Debian](https://wiki.debian.org/ChangeLanguage) run:

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

This is typically handled by [_armbian-config_](User-Guide_Armbian-Config/Localisation.md#change-global-timezone). If necessary, one can also run:

```sh
dpkg-reconfigure tzdata
```


## Default sound output

!!! note

    In recent versions of Debian and Ubuntu, `pulseaudio` got replaced by `pipewire`. The following suggestions won't work in that case.

To check the available sound output options ("sinks") with pulseaudio:

```sh
pacmd list-sinks | less
```

The default sink will be marked with an asterisk "\*". Press <kbd>q</kbd> to exit.

To define a new default sound output:

```sh
pacmd set-default-sink <NAME-OF-DESIRED-OPTION>
```

The name of HDMI sound output devices may change accordingly to the device. If you don't want to deal with different names, you can run:

```sh
pacmd set-default-sink $(pactl list short sinks | grep -i 'hdmi' | awk '{print $2}')
```

The command to define the default sink is not persistent. To make it persistent, add it to the file `~/.bashrc`.


## Fix HDMI screen resolution for SunXi/Allwinner SoC

In rare cases, some SunXi/Allwinner boards failed to detect Full-HD support for HDMI and boot with only 720p. This issue should now be resolved, and the following steps are provided only for reference if it still occurs.
!!! tip "Legacy versions"

    Open the `/boot/boot.cmd` file with an editor of your choice (e.g. `nano`) and add or change the [`disp.screen0_output_mode`](https://linux-sunxi.org/Display#HDMI) option to the kernel command line. For a fixed mode (e.g. 1280x720 at 60 Hz), set it to:

    ```sh
    disp.screen0_output_mode=1280x720p60
    ```

    Then run

    ```sh
    mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr
    ```


## Enable a custom screen resolution within X.Org

Sometimes, not all desired resolutions are supported out of the box. The following short howto shows how to enable a custom resolution and add it to your X.Org configuration. It is based on [this forum post](https://forum.armbian.com/topic/10403-add-undetected-hdmi-resolution-to-x11xorg/) by user @maxlinux2000 (Thanks!). The `xrandr` and `cvt` commands must be executed as the current user in a graphical session, **not** by the root user!

First, find the matching HDMI output (the `x11-xserver-utils` package must be installed):

```sh
xrandr --listmonitors
```

Then, calculate the VESA CVT mode line. The following command does this for a custom resolution of 1440x900.

```sh
cvt 1440 900
```

The command will output a new modeline. For our example, it may look like this:

```
# 1440x900 59.89 Hz (CVT 1.30MA) hsync: 55.93 kHz; pclk: 106.50 MHz
Modeline "1440x900_60.00"  106.50  1440 1528 1672 1904  900 903 909 934 -hsync +vsync )
```

The new modeline can then be used directly to create and add the new mode, and enable it. The following commands will do that for the output device _HDMI-1_.

```sh
xrandr --newmode "1440x900_60.00" 106.50 1440 1528 1672 1904 900 903 909 934 -hsync +vsync
xrandr --addmode HDMI-1 1440x900_60.00
xrandr --output HDMI-1 --mode 1440x900_60.00
```

If it works well, the new mode can also be added to X.Org's configuration in `/etc/X11/xorg.conf.d/` to make it permanently available/active. Otherwise, these commands will have to be executed after every reboot. To load this resolution automatically after starting the device, add the following section to e.g. `/etc/X11/xorg.conf.d/40-monitor.conf` (create the file if it does not exist):

```
Section "Monitor"
	Identifier "HDMI-1"
	Modeline "1440x900_60.00" 106.50 1440 1528 1672 1904 900 903 909 934 -hsync +vsync
	Option "PreferredMode" "1440x900"
EndSection
```

After a restart, the graphical session should automatically be shown in the chosen resolution.


## Alter the CPU frequency

<!--TODO: new boards? -->

!!! tip "Legacy versions"

    Some boards allow to adjust the CPU speed by editing the file `/etc/default/cpufrequtils` and alter the  **min_speed** and/or **max_speed** variable. Changing these values require restarting `cpufrequtils.service` to activate the new settings:

    ```sh
    systemctl restart cpufrequtils.service
    ```


## Swap for experts

By default, Armbian implements ZRAM (writing nothing to 'disk', but compressing memory pages in RAM). In case you often run into out-of-memory (OOM) errors and your device has some capable storage (e.g. a securely attached NVMe or SATA SSD), you might want to use ZSWAP instead.

Check whether your kernel has zswap enabled. If yes, the following command

```sh
dmesg | grep zswap
```

should return some output. If that is the case, create a swapfile or a swap partition the traditional way: edit `/etc/default/armbian-zram-config` so that it reads `SWAP=false`. Reboot, and you're done.

Zswap performs a lot better than the combination of ZRAM and 'swap on disk' in parallel.


## Switch or downgrade kernels

This is typically handled by [_armbian-config_](User-Guide_Armbian-Config/System.md#alternative-kernels).

```bash
armbian-config --cmd KER001
```

In rare cases, it can be necessary to downgrade a kernel package, e.g. to fall back to a previous version.

!!! danger

    Version dependencies between packages can create serious conflicts when attempting a package downgrade. If you force anything here, you can easily destroy your system beyond the point of repair. Don't use that command lightly and better ask twice.

```sh
apt install linux-image-current-rockchip64=25.5
```


## Build a wireless driver

The kernels provided by the project should contain the drivers, modules, and firmware to support most commonly used network devices/dongles. If you encounter that you have to build your own module and load it, the following example shows the general procedure because most modules follow the same structure and setup. It is, however, rarely necessary to build and load so-called "out-of-tree" kernel modules as shown in this example. Even the module we use here as an example is already supported by the current kernels.

First, building a module always requires having the kernel headers installed. The correct version can be installed with:

```sh
armbian-config --cmd HEAD01
```

Then download the driver's sources. Most drivers can probably be found in a Git repository like in our example.

```sh
git clone https://github.com/morrownr/8821au-20210708.git
cd 8821au-20210708
```

The build and install instructions can usually be found on the driver's homepage or in a file called `README.md` in the source. Read these instructions carefully. Usually, the following commands will suffice and result in an output as shown below.

```sh
make
make install
```

??? "Build log"

    ```text
    make ARCH=arm64 CROSS_COMPILE= -C /lib/modules/6.6.62-current-sunxi64/build M=/root/8821au-20210708  modules
    make[1]: Entering directory '/usr/src/linux-headers-6.6.62-current-sunxi64'
      CC [M]  /root/8821au-20210708/core/rtw_cmd.o
      CC [M]  /root/8821au-20210708/core/rtw_security.o
      CC [M]  /root/8821au-20210708/core/rtw_debug.o
      CC [M]  /root/8821au-20210708/core/rtw_io.o
      CC [M]  /root/8821au-20210708/core/rtw_ioctl_query.o
      CC [M]  /root/8821au-20210708/core/rtw_ioctl_set.o
      CC [M]  /root/8821au-20210708/core/rtw_ieee80211.o
      CC [M]  /root/8821au-20210708/core/rtw_mlme.o
      CC [M]  /root/8821au-20210708/core/rtw_mlme_ext.o
      ...
      [ goes on for a while ]
      ...
      LD [M]  /root/8821au-20210708/8821au.o
      MODPOST /root/8821au-20210708/Module.symvers
      CC [M]  /root/8821au-20210708/8821au.mod.o
      LD [M]  /root/8821au-20210708/8821au.ko
    make[1]: Leaving directory '/usr/src/linux-headers-6.6.62-current-sunxi64'
    ```

If make succeeded, attempt to load the driver and check the `dmesg` output.

```sh
insmod 8821au.ko
usbcore: registered new interface driver rtl8821au
```

If everything was successful, plug the USB wireless adaptor in and proceed with the [network configuration](User-Guide_Networking.md).


## Toggle boot output

[Boot parameters](http://redsymbol.net/linux-kernel-boot-parameters/) are edited or changed directly in `/boot/boot.cmd` (**not recommended**) or via variables in `/boot/armbianEnv.txt`:

```diff
- console=both
+ console=serial
```

To disable the console entirely (also **not recommended** and only as an example) one would set `console=none`.

To recompile `boot.cmd` to `boot.scr` if it was changed:

```sh
mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr
```

And reboot.

The serial console on imx6 boards is `ttymxc0` (Hummingboard, Cubox-i) or `ttymxc1` (Udoo).


## Toggle boot verbosity

<!-- TODO: Isn't this better suited for Troubleshooting; at least cross-link from there here -->

To change the boot verbosity, alter the `verbosity=` line in `/boot/armbianEnv.txt`. The lower the value, the lower the verbosity. The default is `1` and the maximum is `7`.

!!! tip "Legacy versions"

    Using Armbian from version 5.05 to 5.20, you have to touch or delete `/boot/.force-verbose` to increase the boot verbosity.


## Enable boot logs for inspection

If your SBC behaves strange, the first step is to check the power supply and the integrity of the boot media as detailed in the [_Troubleshooting_](User-Guide_Troubleshooting.md) section. Also, run

```sh
armbianmonitor -c "$HOME"`
```

Then look into your kernel logs. Armbian also provides a tool that grabs some information and pastes it to an online pasteboard service. Please increase the boot verbosity to its maximum level (`verbosity=7`) as shown above, reboot and then run:

```sh
sudo armbianmonitor -u
```

Then copy and past the URL of your log to the [forum, mail, etc](index.md#where-to-find-additional-help).


## APT mirror selection

Armbian has its own APT repository `http://apt.armbian.com` and mirrors for armbian-specific packages. The default domain is a round-robin to all mirrors. If you are having trouble updating or expereince slow speeds, you may want to choose a specific mirror.

First, make sure that you have the `jq` package installed:

```sh
apt install -y jq
```

To get a list of available mirrors from our `https://apt.armbian.com/mirrors` endpoint in JSON format, run:

```bash
curl -s http://apt.armbian.com/mirrors | jq
```

You will see a result set similar to this (shortened), listing mirrors by region:

```json
{
  "AS": [
    "http://mirror.twds.com.tw/armbian-apt/",
    "http://mirror.albony.in/armbian/",
    "http://jp.mirrors.naho.moe/armbian/",
    ...
  ],
  "EU": [
    "http://netcup-02.armbian.com/apt/",
    "http://fi.mirror.armbian.de/apt/",
    "http://armbian.nardol.ovh/apt/",
    ...
  ],
  "NA": [
    "http://mirrors.jevincanders.net/armbian/apt/"
  ],
  "OC": [
    "http://au.sbcmirror.org/armbian/apt/"
  ],
  "default": [
    "http://mirrors.jevincanders.net/armbian/apt/",
    "http://netcup-02.armbian.com/apt/",
    "http://fi.mirror.armbian.de/apt/",
    ...
  ]
}
```

Choose a mirror, edit `/etc/apt/sources.list.d/armbian.sources`, and replace the URL `http(s)://apt.armbian.com` with your preferred mirror.


## Install Docker

Install either the minimal package ...

```bash
armbian-config --CON001
```

... or the fully featured one.

```bash
armbian-config --CON002
```

To test if Docker works correctly:

<!-- TODO: Will the above have added the current user to the docker group? -->

```bash
docker run hello-world
```

If you get that kind of output, then Docker install went fine:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
