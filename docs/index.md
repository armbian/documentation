[![](http://www.armbian.com/wp-content/uploads/2016/06/logo_middle.png)](http://www.armbian.com)

linux for ARM development boards

<h3>Welcome to the Armbian Documentation!</h3>

If you're **new to Armbian**, the [Getting Started](User-Guide_Getting-Started.md) section 
provides a tutorial for everything you need to get Armbian running,
and answers many Frequently Asked Questions.
It then continues on to more advanced topics.

If you **need help**, and have read through Getting Started, check out [Troubleshooting](User-Guide_Advanced-Features.md#how-to-troubleshoot).

If you still can't find what you need here, visit the [Armbian forum](http://forum.armbian.com/), where your input can help improve this documentation.

# What is Armbian? #

- Lightweight Debian or Ubuntu based distribution specialized for ARM developing boards. [Compiled from scratch](https://github.com/igorpecovnik/lib),
- It has powerfull build and software development tools,
- A vibrant community.

# Supported chips

- Allwinner A10, A20, A31, H2+, H3, H5, A64
- Amlogic S805 and S905 (Odroid boards), S802/S812, S805, S905, S905X and S912 (fork by `@balbes150`)
- Actionsemi S500
- Freescale / NXP iMx6
- Marvell Armada A380
- Samsung Exynos 5422

# Supported boards

Beelink X2, Orange Pi PC plus, Orange Pi Plus 2E, Orange Pi Lite, Roseapple Pi, NanoPi M1, pcDuino2, pcDuino3, Odroid C0/C1/C1+, Banana Pi M2+, Hummingboard 2, Odroid C2, Orange Pi 2, Orange Pi One, Orange Pi PC, Orange Pi Plus 1 & 2, Clearfog, Lemaker Guitar, Odroid XU4, Udoo Neo, Banana Pi M2, Orange Pi A31S, Cubieboard 1, Cubieboard 2, Hummingboard, Lamobo R1, Banana Pi PRO, Orange Pi mini A20, Olimex Lime A10, Olimex Micro, Olimex Lime 2, pcDuino3 nano, Banana Pi Plus A20, Udoo quad, Orange Pi A20, Olimex Lime 1, Banana Pi, Cubox-i, Cubietruck

Check [download page](http://www.armbian.com/download/) for recently supported list.

# Common features

- Debian Jessie or Ubuntu Xenial based. Compiled from scratch,
- Install images are reduced to actual data size with small reserve and are resized at first boot,
- Root password is `1234`. You will be prompted to change this password and to create a normal user at first login.
- First boot takes longer (up to few minutes) than usual (20s) because it updates package list, regenerates SSH keys and expand partition to fit your SD card. It might reboot one time automatically.
- [Ready to compile external modules](User-Guide_Advanced-Features/#how-to-build-a-wireless-driver)
- Ethernet adapter with DHCP and SSH server ready on default port (22)
- Wireless adapter with DHCP ready if present but disabled (/etc/network/interfaces, WPA2: normal connect or AP mode)
- NAND, SATA, eMMC and USB install script is included (nand-sata-install)
- Serial console enabled
- Enabled automatic security update download for basic system and kernel. Upgrades are done via standard apt-get upgrade method
- Login script shows: board name with large text, distribution base, kernel version, system load, up time, memory usage, IP address, CPU temp, drive temp, ambient temp from Temper if exits, SD card usage, battery conditions and number of updates to install.

# Performance tweaks

- /tmp and /var/log are mounted as tmpfs, log2ram service saves logs to disk daily and on shutdown
- optimized IO scheduler. (check /etc/init.d/armhwinfo)
- journal data writeback enabled. (/etc/fstab)
- commit=600 to flush data to the disk every 10 minutes (/etc/fstab)
- optimized CPU frequency scaling with interactive governor (/etc/init.d/cpufrequtils)
	- 480-1010Mhz @Allwinner A10/A20
	- 480-1260Mhz @Allwinner H3
	- 392-996Mhz @Freescale imx
	- 600-2000Mhz @Exynos & S905
- eth0 interrupts are using dedicated core (Allwinner based boards)

![YOUTUBE](6K9zJULoFpU)

# Get Involved! #

* [Contribute](Process_Contribute)
* [Community](http://forum.armbian.com)
* [Contact](http://www.armbian.com/contact/)
