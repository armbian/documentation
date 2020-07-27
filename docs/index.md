[![](images/logo_middle.png)](http://www.armbian.com)

Linux for ARM development boards

# Welcome to the Armbian Documentation!

If you are **new to Armbian**, the [_Getting Started_](User-Guide_Getting-Started.md) section 
provides a tutorial for everything you need to get Armbian running,
and answers many **F**requently **A**sked **Q**uestions.
It then continues on to more advanced topics.

If you **need help**, and have read through _Getting Started_, check out [_Troubleshooting_](User-Guide_Advanced-Features.md#how-to-troubleshoot).

If you still cannot find what you need here, visit the [_Armbian forum_](http://forum.armbian.com/), where your input can help improve this documentation.

# What is Armbian?

*Armbian is a base operating system platform for single board computers (SBCs) that other projects can trust to build upon.*


- Lightweight Debian or Ubuntu based linux distribution specialized for ARM development boards
- Each system is compiled, assembled and optimized by [_Armbian Build Tools_](https://github.com/armbian/build) 
- It has powerful build and software development tools to make [_custom builds_](Developer-Guide_Build-Preparation.md)
- A vibrant community
- What is the [difference between](https://forum.armbian.com/topic/7787-what-is-the-difference-between-armbian-and-debian-linux/?tab=comments#comment-58689) Armbian and Debian Linux




### Common features

- Armbian Linux is availble as Debian and Ubuntu based images, compiled from scratch
- Images are reduced to actual data size and automatically resized at first boot
- Root password is `1234`. You are forced to change this password and (optional) create a normal user at first login
- Ethernet adapter with DHCP and SSH server ready on default port (22)
- Wireless adapter with DHCP ready (if present) but disabled. You can use `armbian-config` to connect to your router or create an AP 
- NAND, SATA, eMMC and USB install script is included (`nand-sata-install`)
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
    - 480-1260Mhz @Allwinner H3
    - 392-996Mhz @Freescale imx
    - 600-2000Mhz @Exynos & S905
- eth0 interrupts are using dedicated core (Allwinner based boards)

# What is supported?

"Supported" is not a guarantee. "Supported" implies a particular SBC is at a high level of software maturity, but has no intention to support all possible SBC functions.  Supported boards do receive preferential treatment to bugfix, improve, or add additional functionality based on any of the following, **non-exclusive** criteria:

1. The discretion of the "Armbian Development Team"
1. The availability of the "Armbian Development Team"
1. The availability of sample boards and ease of testing
1. The mainline kernel maturity for the particular SoC or SBC platform
1. Paid engagements, long-term sponsorship to the Armbian Project or volunteer developers
1. Vendor or 3rd party has a **designated** resource providing support for a SBC or platform ON BEHALF OF THE COMMUNITY and is contributing to the project

### Supported chips

- Allwinner A10, A20, A31, H2+, H3, H5, H6, A64
- Amlogic S805 and S905 (Odroid boards), S802/S812, S805, S905, S905X and S912 (fork by `@balbes150`)
- Actionsemi S500
- Freescale / NXP iMx6
- Marvell Armada A380
- Rockchip RK3288
- Samsung Exynos 5422

### Supported boards

Check [download page](http://www.armbian.com/download/) for recently supported list.
# Get Involved! #

* [Contribute](Process_Contribute)
* [Community](http://forum.armbian.com)
* [Contact](http://www.armbian.com/contact/)

Our IRC channel is [#armbian](https://webchat.freenode.net/?channels=armbian) on [freenode](https://freenode.net/). More details [here](https://docs.armbian.com/Community_IRC/)
