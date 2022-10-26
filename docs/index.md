[![](images/logo_middle.png)](https://www.armbian.com)

Linux for ARM development boards

# Welcome to the Armbian Documentation!

If you are **new to Armbian**, the [_Getting Started_](User-Guide_Getting-Started.md) section 
provides a tutorial for everything you need to get Armbian running
and answers many **F**requently **A**sked **Q**uestions.
It then continues on to more advanced topics.

If you **need help** and have read through _Getting Started_ check out [_Troubleshooting_](User-Guide_Advanced-Features.md#how-to-troubleshoot).

If you still cannot find what you need here visit the [_Armbian forum_](https://forum.armbian.com/) where your input can help to improve this documentation.

## What is Armbian?

*Armbian is a base operating system platform for single board computers (SBCs) that other projects can trust to build upon.*


- Lightweight Debian or Ubuntu based Linux distribution specialized for ARM development boards
- Each system is compiled, assembled and optimized by [_Armbian Build Tools_](https://github.com/armbian/build) 
- It has powerful build and software development tools to make [_custom builds_](Developer-Guide_Build-Preparation.md)
- A vibrant community


### What is the difference between Armbian and Debian/Ubuntu?

- Debian or Ubuntu officially do not support most of those boards/boxes. Armbian does.
- Armbian userspace has many small but vital performance or security adjustments
- Armbian fancy some kernel development and a lot of its maintaining. Debian relies on upstream sources for ARM hardware which can be **years** behind and/or lack of many functions
- Armbian userspace is lean, clean but 100% Debian/Ubuntu compatible
- Many stock Debian bugs are fixed on the way, "better than original :)"
- The Armbian build system is a central part of this whole ecosystem. You can DIY. Debian is much harder.
- Dedicated support forums per boards/boxes
- Plug'n'Play vs. complicated install scenarios on stock Debian
- unified development scenarios and user experience vs. mess of different setup instructions scattered all around 

### Common features

- Armbian Linux is available as Debian and Ubuntu based images, compiled from scratch
- Images are reduced to actual data size and automatically expand across the SDcard at first boot
- Root password is `1234`. You are forced to change this password and (optional) create a normal user at first login
- Ethernet adapter with DHCP and SSH server ready on default port (22)
- Wireless adapter with DHCP ready (if present) but disabled. You can use `armbian-config` to connect to your router or create an access point
- NAND, SATA, eMMC and USB install script is included (`armbian-install`)
- Upgrades are done via standard `apt upgrade` method
- Login script shows: board name with large text, distribution base, kernel version, system load, uptime, memory usage, IP address, CPU  and drive temperature, ambient temperature from Temper if exits, SD card usage, battery conditions and number of updates to install

### Performance tweaks

- `/var/log` is mounted as compressed device (zram, lzo), log2ram service saves logs to disk daily and on shutdown
- Half of memory is allocated/extended for/with compressed swap
- `/tmp` is mounted as `tmpfs` (optionally compressed)
- Browser profile memory caching
- Optimized IO scheduler (check `/etc/init.d/armhwinfo`)
- Journal data writeback enabled. (`/etc/fstab`)
- `commit=600` to flush data to the disk every 10 minutes (`/etc/fstab`)
- Optimized CPU frequency scaling with `interactive` governor (`/etc/init.d/cpufrequtils`)
    - 480-1010Mhz @Allwinner A10/A20
    - 480-1368Mhz @Allwinner H2+/H3
    - 392-996Mhz @Freescale imx
    - 600-2000Mhz @Exynos & S905
- eth0 interrupts are using dedicated core (Allwinner based boards)

## What is supported?

Armbian will publish and distribute “stable” CLI images for supported boards through its mirror network. *Supported* is not a guarantee. *Supported* has a named maintainer and implies a particular SBC is at a high level of software maturity. Due to the complexity and lack-of-openness in the ecosystem it is unlikely that all accelerated and specialized functionalities (like 3D, VE, I²C...) will be available.

For more information is see the [Board Support Guide](User-Guide_Board-Support-Rules)

### Supported boards

Check [download page](https://www.armbian.com/download/) for recently supported list.


## How to report bugs

Due to lack of manpower we unfortunately have to be very picky about bug reports. Make sure to follow the bug reporting form available [here](https://armbian.com/bugs) to learn how to collect necessary information and where to put your report depending on type of issue.  

# Get Involved! #

* [Contribute](Process_Contribute/)
* [Community](https://forum.armbian.com/)
* [Contact](https://www.armbian.com/#contact)

Our IRC channel is [#armbian](https://web.libera.chat/#armbian) on [Libera.Chat](https://libera.chat/). More details [here](https://docs.armbian.com/Community_IRC/)
