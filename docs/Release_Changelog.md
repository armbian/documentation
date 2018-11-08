**v5.66 / 8.11.2018**

- added Mediatek MT7623 family.
- added images for Bananapi R2 with kernel 4.19.y without official support.

**v5.66 / 7.11.2018**

- removing Odroid C2 official support, drop its default 3.16.y kernel from build engine and merge with the meson64 family.
- attach meson64 dev to 4.19.y
- drop Udoo Neo completly, drop Udoo Quad default and dev kernel.
- Odroid XU4: drop kernel 3.10.y, default branch is upgraded to offical 4.14.y, next becomes vanilla 4.19.y

**v5.65 / 6.11.2018**

- Cubox-i/Hummigboard: drop kernel 3.14.y and move 4.14.y to default, next becomes 4.19.y, dev 4.19.y with a mainline u-boot

**v5.64 / 9.10.2018**

- updated images and packages for Helios4.
- added images for Nanopi Neo4.

**v5.63 / 8.10.2018**

- updated images for Helios4 with SPI booting support.
- updated armbian-config. Added advanced ZSH shell install with most used plugins and tmux.

**v5.62 / 1.10.2018**

- updated armbian-config

**v5.61 / 26.9.2018**

- updated armbian-config,
- fixed Chromium on Debian builds with a workaround. We are overwriting package with last known working one. It will show some error on startup which is safe to ignore. This workaround will fade out with Chromium upstream update.

**v5.60 / 19.9.2018**

Changes overview:

General:

- Ubuntu Xenial was replaced with Bionic unless kernel was too old for the change,
- Debian Jessie becomes EOL and its building is not maintained anymore while you will still receive kernel updates,
- Emergency swap file creation is disabled by default since we use compressed memory (ZRAM) as an alternative,
- `vm.swappiness` has been changed from 0 to 100 (if you run databases on your board you might want to revert this change in `/etc/sysctl.conf`),
- RAM logging also uses ZRAM now and rotates logs automagically,
- all images were rebuilt, except boards for which support ended,
- significantly lighter - browser only - desktop images (< 1.5G),
- fixed hanging on headers installation,
- install boot script (BSP package) if not present. This fixes upgrade or kernel switching problems,
- Proper bind mount directory when installing to SATA/USB and booting from SD,
- update for wireless drivers 8812/11/14AU, 8188EU and AUFS,
- Bugfix when a temperature is not present or readings are invalid,
- Also showing bridge IP addresses in MOTD,
- storing package list compressed - saves 50-70Mb,
- enlarging automated apt-get update and purge intervals,
- smaller overhead for CLI images,
- improved alternative kernel switching,
- stop setting Google's DNS server as default for privacy reasons.

Family:

- sunxi and sunxi64, u-boot was bumped to 2018.05, NEXT branch was updated to the latest 4.14.y, DEV is attached to 4.18.y + fixed overlay support,
- mvebu64, default BSP kernel was upgraded to 4.14.y, NEXT to 4.18.y,
- odroidc1, experimental NEXT kernel branch was attached to 4.18.y,
- odroidc2 kernel was merged with meson64 on the source level,
- meson64 u-boot was pushed to 2018.05, a default was updated to the latest 4.14.y, NEXT to 4.18.y,
- rk3288, u-boot was pushed to 2018.05, legacy kernel cleaned and fixed after upstream troubles, NEXT branch was updated to the latest 4.14.y,
- rockchip64, rk3399 was split into rk3399 for Friendly ARM boards and rockchip64 for Rock64 and RockPro, Ayufan repository. Merging is postponed for the future,
- s5p6818 family support added NEXT branch was updated to the latest 4.14.y,
- mvebu, NEXT branch was updated to latest 4.14.y, DEV attached to 4.18.y,
- fixed randomly failing X server on imx6 family,

Board:

- added WIP support for Firefly RK3399, Lime A64, Renegade, Rockpro64, Olimex Teres
- added experimental images for Bananapi M3 and Cubietruck+,
- adeed support for: Tinkerboard S, Rock64, Orangepi Zero Plus, Nanopi Neo Core2, Nanopi M4,
- added NEO 1.1 regulator overlay,
- added Helios4 device tree with FAN control for modern kernel,
- enabled SPI access on Espressobin,
- updated SPI boot firmware on Espressobin (18.09.1) with many fixes and support for booting from USB, SATA, eMMC or SD,
- added Tinkerboard S DC-IN voltage to armbianmonitor,
- fixed network interface initialization,
- fixed clock drift on Bananapi boards,
- enabled concurrent AP/STA mode on Tinkerboard,
- improved support for NanoPi Fire 3 (added SPU1705, DVFS, thermal tables, etc.),
- fixed network crashing on high load. Affected: Odroid C1/C2, Le Potato kernel 4.18.y,
- fixed wireless, eMMC and Bluetooth on (unsupported) Z28 PRO and changed boot order,
- fixed eMMC install on NanoPC T3+ and Docker dependencies on Fire3, M3, NanoPC T3+,
- added eMMC and DVFS support on Espressobin mainline kernel, 
- ported Tinkerboard UMS to modern u-boot,
- enabled 1392 MHz cpufreq OPP on all RK3328 devices,
- enabled 1992/1512MHz cpufreq OPP on all RK3399 devices,
- added eMMC to OlinuXino A64 kernel and u-boot,
- added Sunvell R69 CSC target,
- OrangepiWin: fixed BT,
- fixed ethernet on (unsupported) Bananapi M64.

Build script:

- changed recommended build host to Bionic, Xenial still supported for everything except building Bionic images,
- added support for burning image directly to SD card when your build is done by using Etcher for CLI,
- added support for making LUKS encrypted root images, parameters: CRYPTROOT_ENABLE=yes, CRYPTROOT_PASSPHRASE=unlockpass,
- fixed building under Docker, bumped to Bionic host,
- added building Bionic and block building it for images with too old kernels,
- added multibranch support (LIB_TAG).

Infrastructure:

- build machine main SSD and memory upgrade, switched from bare metal Ubuntu Xenial to fully optimsed Debian KVM server, free build capacity is avaliable for any armbian related activity upon request,
- download server drive capacity and download speed upgrade, IPV6,
- geo load balancing for repository and download server is under testing,
- improved repository management. Possibility to add packages via Github,
- introducing new internal parameter, example: BUILD_ALL="yes" REBUILD_IMAGES="bananapi,udoo,rock64" to specify which images need rebuilding,
- main torrent server cleanup, removed deprecated images,
- creating report https://beta.armbian.com/buildlogs/report.html when building all kernels. Prepared to include simple per board testing report where exists https://github.com/armbian/testings.

Known bugs:

- modern kernel support on A64 boards is mainly broken.

**v5.59 / 18.8.2018**

- rebuilt images for Espressobin with kernel 4.18.y, Nanopc T4

**v5.58 / 13.8.2018**

- rebuilt images for Bananapi, Bananapi Pro, Bananapi+, Odroid C2, Odroid XU4
- updated repository for Odroid C2/XU4, changed NEXT from 4.9.y to 4.14.y

**v5.58 / 13.8.2018**

- rebuilt images for Bananapi, Bananapi Pro, Bananapi+

**v5.57 / 11.8.2018**

- added Bionic desktop and Stretch CLI images for RK3399 powered Nanopc T4

**v5.56 / 10.8.2018**

- rebuilt images for Pinebook. Added Bionic build

**v5.55 / 9.8.2018**

- rebuilt images for Orangepi One+, Orangepi Lite 2 and Pine H64. Enabled USB3, network, THS, DVFS, higher frequencies, HDMI on 4.18.y DEV branch images.

**v5.55 / 3.8.2018**

- added Stretch and Bionic mainline kernel images for Odroid C1 (testing), 
- rebuilt images for Bananapi M3 (fixed ethernet)

**v5.54 / 25.7.2018**

- updated images for Odroid C2, Nanopi M3, Nanopi Fire 3 and NanoPC T3+, Espressobin, Cubox-i/HB and Le potato
- added preview images without end user support for [Bananapi M3](https://dl.armbian.com/bananapim3/),[Cubietruck+](https://dl.armbian.com/cubietruckplus/) and [Bananapi M2 Berry](https://dl.armbian.com/bananapim2ultra/).

**v5.53 / 23.7.2018**

- Z28PRO images updated. Fixed wireless and Bluetooth
- FriendlyARM Nanopi K2 S905 images updated. Fixed ethernet problems.
- FriendlyARM Nanopi K1+ images updated. Fixed HDMI out and wireless

**v5.51 / 4.7.2018**

- Helios4 Stretch and Bionic images update

**v5.50 / 28.6.2018**

- Espressobin images rebuild and repository update, default 4.4.138, next 4.17.3, dev 4.18.RC, hardware crypto support in 4.17.y, zram and zswap
- Odroid C2 bugfix update

**v5.49 / 28.6.2018**

- Amlogic Meson64 family (Odroid C2, Lepotato and FriendlyARM K2 S905) were merged into one kernel. Default images comes with kernel 4.14.52, next with 4.17.3 and DEV with 4.18.RC, updated boot scripts, implemented latest kernel bug fixes
- updated kernels, desktop packages and armbian config on the stable repository (apt update & upgrade)

**v5.48 / 26.6.2018**

- added nightly images for Odroid C2 with 4.16.y (NEXT) and 4.18.y (DEV) and hopefully fixed ethernet driver

**v5.47 / 22.6.2018**

- Odroid C2 images rebuild. Legacy kernel was upgraded to 3.16.57, next to 4.14.51, u-boot to 2018.05
- Added Tritium H5

**v5.46 / 20.6.2018**

- Added Olimex Teres nightly builds
- Added FriendlyARM Nanopi K1 plus

**v5.46 / 6.6.2018**

- Added Orange Pi Lite 2 and One plus nightly builds

**v5.45 / 23.5.2018**

- Orangepi Zero+ images rebuild

**v5.44 / 10.5.2018**

- Espressobin images were rebuilt and moved under stable. Kernel 4.14.40, Stretch, Xenial and Bionic. Fixed bootloader, ath10 wireless card support
- added initial Bionic storage to the main apt repository
- Cubox-i / Hummingboard bugfix update to 4.16.y and images rebuild
- Odroid C2 images rebuild


**v5.41 / 10.2.2018**

- fixed LED driver on Helios4
- bugfix update on sunxi/sunxi64 kernel. Updated to 4.14.18
- kernel update for MVEBU next (4.14.18 and default 4.4.115) for Clearfog and Helios4. Upstream fixes,AUFS and Realtek 881yAU drivers update 

**v5.40 / 5.2.2018**

- fixed eMMC support on Odroid C2 NEXT, kernel 4.14.y
- updated PWM driver on Helios4 
- kernel update for MVEBU next (Clearfog, Helios4) 

**v5.38 / 29.1.2018**

- updated all images
- added H3/H5 testing images with kernel 4.14.y
- added Nanopi M3/T3+/Fire testing image
- fixed Bluetooth on Orangepi Win
- main repository update with recent kernel on all NEXT builds


**v5.37 / 23.1.2018**

- bugfix release
- armbianmonitor -u fix
- setting cronjob permissions
- replace broken u-boot packages on A20 boards
- updated utilities: hostapd, sunxi-tools, armbian-config
- updated images: Bananapi, PRO, M2, BeelinkX2, Clearfog,Cubieboard2, Cubietruck, Cubox-i/HB, Espressobin, Helios4

**v5.36 / 3.12.2017**

- [bugfix release](https://forum.armbian.com/topic/5759-535-bug-questions-collection)

**v5.35 / 25.11.2017**

- mainline kernel updated to 4.13.y
- mainline u-boot updated to v2017.09
- added new sunxi Device Tree overlays, fixed and improved old overlays
- Micro-USB [g_serial](https://www.kernel.org/doc/Documentation/usb/gadget_serial.txt) console is enabled by default on most small Allwiner based boards
- Olimex Lime2 and Micro: merging eMMC and normal versions
- Odroid C2: next and dev branches migrated to mainline u-boot
- Odroid XU4: added dev branch, next branch migrated to mainline u-boot
- Clearfog: added dev branch with mainline u-boot
- added supports for [7" RPi display](https://www.raspberrypi.org/products/raspberry-pi-touch-display/) to Tinkerboard with legacy kernel
- All mainline kernels: added Realtek 8811AU/8812AU/8814AU USB wireless driver with monitor mode and frame injection
- All boards: added kernel source packages to the repository (Package names `linux-source-${BRANCH}-${LINUXFAMILY}`, i.e. `linux-source-sunxi-next`)
- Kernel headers are no longer installed by default to new images
- Additional out of tree drivers and USB Redirector are no longer installed by default to new images
- Switching from emergency swap to zram on new Ubuntu Xenial images
- New hardware support (stable/supported images): NanoPi Duo, Orange Pi R1, Pinebook
- New hardware support (experimental): Le Potato, NanoPi NEO 2, Orange Pi Zero Plus, Orange Pi Zero Plus 2 (H5)
- sunxi mainline u-boot: reenabled USB keyboard support and disabled stopping the boot sequence with any key - autoboot now can be aborted with <Ctrl-C>

Desktop images:

- xterm was replaced with full featured xfce terminal,
- added memory profile caching for Chromium,
- added OpenVPN connector,
- shortcuts to armbian-config, support and donate were moved to menu,
- default icon theme was changed to lighter one (Numix),
- fixed login greeter theme,
- changed wallpaper.
- changed [CMA handling](https://github.com/armbian/build/issues/744) on Allwinner legacy kernels

armbian-config:

- was splitted from board support packages to a new package `armbian-config`
- managing board hardware configurations, hotspot, Bluetooth, SSH server
- freezing/unfreezing kernel upgrade
- switching between stable and beta builds,
- switching between alternative kernels,
- installing/uninstalling kernel headers,
- changing timezone, locales, hostname,
- running diagnostic tools,
- enabling/disabling RDP server,
- 3rd party software installer: Samba, OMV, Pi hole, Transmission, ...

Build script:

- added Debian Stretch
- most tweaks moved from inline files to separate files in board support package
- firmware blobs moved to a separate repository
- disabled distcc in extra software compilation process due to toolchain compatibility issues

[Known problems](https://forum.armbian.com/topic/5759-535-bug-questions-collection/)

- Allwinner A20/sun7i legacy boards. Changed CMA settings prevents playing video. [You need to add cma=96M to kernel command line](https://github.com/armbian/build/issues/744)

**v5.34 / 18.10.2017**

- bugfix Odroid XU4/HC1 image rebuild [due to broken USB install on kernel 4.9.x](https://forum.armbian.com/index.php?/topic/5413-odroid-hc1-sata-install)
- added Le Potato and Orange Pi Zero testing image (mainline kernel)
- Tinkerboard, MiQi and Pinebook images rebuilt

**v5.33 / 24.09.2017**

- Odroid XU4/HC1 images were rebuilt.

**v5.33 / 21.09.2017**

- Tinkerboard and MiQi images were rebuilt. Rockchip legacy kernel was updated to 4.4.88 and mainline (NEXT) to 4.13.3.

**v5.32 / 23.06.2017**

- bugfix release [due to broken crypto functions on kernel 4.11.x](https://forum.armbian.com/index.php?/topic/4556-partial-bugfix-update/)

**v5.31 / 15.06.2017**

- bugfix release [due to network failure](https://forum.armbian.com/index.php?/topic/4498-no-boot-after-upgrade-to-530/) on some A10 / A20 boards

**End of support notice**

Following boards are no longer receiving support and updates since this version:

- Cubieboard (Allwinner A10) - not enough hardware samples to maintain support
- Lamobo R1 (Allwinner A20) - hardware design flaws, poor software support for the onboard switch
- Olimex Lime A10

**v5.30 / 14.06.2017**

- mainline kernel updated to 4.11
- mainline u-boot updated to v2017.05
- Firefox was replaced with Chromium (desktop images)
- sunxi mainline configuration: added Device Tree overlays support (new images only)
- sunxi mainline configuration: added `armbian-add-overlay` helper for compiling and activating DT overlays (new images only)
- log2ram: fixed saving `/var/log` contents on shutdown
- new hardware support (stable/supported images): Xunlong Orange Pi Zero Plus 2 (H3), ASUS TinkerBoard, MiQi
- reworked package updates MOTD script to speed up the login process
- added config file `/etc/default/armbian-motd` for disabling MOTD components
- added `armbian-config` dialog-based configuration program (WIP)
- Banana Pi M2: fixed HDMI video output
- Clearfog: adjusted temperature readout
- i.MX6 mainline: enabled support for HDMI audio and PCIe bus

**End of support notice**

Following boards are no longer receiving support and updates since this version:

- Orange Pi (Allwinner A20) - no hardware samples, out of stock
- Orange Pi Mini (Allwinner A20) - no hardware samples, out of stock
- LeMaker Guitar (Actions S500)
- Roseapple Pi (Actions S500)

**v5.26,5.27 / 24.02.2017**

- security update for most kernels (packages only)
- fixes for hostapd configuration

**v5.25 / 2.2.2017**

- nand-sata-install expanded functionality: you can partition destination and choose file-system type: ext2, ext3, ext4 and BTRFS (BTRFS requires kernel 4.4+)
- added new boards: Clearfog Base, Lime2 eMMC, Lime A33, NanoPi M1+, OrangePi Zero, OrangePi PC2 (mainline only, experimental)
- new default kernel for Clearfog(s), changed kernel family to "mvebu" to avoid conflicts
- disabled wireless power management by default to improve performance with certain drivers
- added wireless drivers to mainline kernels: OrangePi Zero, Neo Air
- implemented initrd loading support for all boards
- moved all images to single ext4 partition scheme
- changed default wallpaper, startup icon, shadows to windows on desktop builds
- Firefox web cache moved to memory
- added g_serial driver to boards without a network connector, working on both kernel (Opi Zero,Opi Lite,FA Neo Air)
- added "Software boutique" application installer on desktop builds (currently not working properly on arm64)
- added per board patching option
- added u-boot video driver and boot logo to H3 based boards
- added simplefb video driver (HDMI only) to mainline H3 kernel
- updated MALI driver on H3 platform, fixed problems on 2GB boards
- changed Ethernet switch driver on Lamobo R1 to DSA based one (mainline kernel)
- fixed soft cursor (CLI) for H3 legacy and Odroid C2
- expand and adjust multiple kernel configurations based on user requests
- adjusted sunxi boot script to support booting in SPI flash + USB storage scenario (w/o the SD card)
- dropped support for Debian Wheezy and Ubuntu Trusty releases
- sunxi mainline kernel was updated to 4.9.x, some dev kernels to 4.10
- added log2ram (Ramlog alternative) to default installation
- changed first run logic, disabled forced automatic reboot
- changed new user account creation logic, disabled forced reboot on user creation failure

**v5.24**

- this version is not released, it was used for the nightly or user-built images

**v5.23 / 23.10.2016**

- fixed bug in nand-sata-install
- fixed u-boot update bug on Allwinner platform

Known problems:

- Lamobo R1 fails to boot upon upgrade

**v5.22 / 22.10.2016**

- fixed eMMC install on Odroid C2
- firmware package was splitted into minimal (default) and full versions
- patched [Dirty COW exploit](http://thehackernews.com/2016/10/linux-kernel-exploit.html) on all kernels
- added Odroid XU4 mainline kernel image
- added Olimex A33 mainline kernel image
- added Overlay FS for Cubox, Udoo and Udoo Neo
- booting problems fixed on more boards
- updated wireless driver on M2+ (dhd)
- updated driver for OV5640 on sun8i default kernel
- sunxi-next kernel version updated to 4.8.4
- BananaPi M1+ now uses upstream DTB file `sun7i-a20-bananapi-m1-plus.dtb`, boot script adjusting may be required for existing images

Desktop images:

- prebuilt mpv and FFmpeg were removed in favor of providing only configuration files
- fixed an issue with video brightness on A10/A20 based boards

Build script:

- DEBUG_MODE was renamed to CREATE_PATCHES
- GLshim was moved to a private directory, it can be activated for selected applications by changing `LD_LIBRARY_PATH`

Known problems:

- eMMC install fails (will be fixed in bugfix update)
- H3 development kernel (4.8.4) update fails to boot
- C2 upgrade hangs on compiling headers (Jessie)

**v5.20 / 16.9.2016**

- added FriendlyARM Neo legacy and mainline images (experimental)
- added Orange Pi PC+ mainline kernel (experimental)
- added Pine64 / Pine64+ images with legacy kernel
- added UUID support for NAND/SATA/USB installer
- added desktop images for Cubox(s) / Hummingboard(s) with mainline kernel
- enabled MIDI sequencer and snd-rawmidi-seq in H3 legacy kernel
- added H3 consumption tool to control board consumtion level on legacy kernel
- fixed and enabled Bluetooth on Cubietruck and Cubox(s) / Hummigboard(s) desktop, both kernels
- masked p2p0 wifi direct device on Bluetooth legacy kernel
- Odroid C1/C2 upgrade fail fixed
- wireless enabled by default on Banana Pi PRO
- added new screen resolutions to H3 boards with legacy kernel
- DeviceTree Overlay ConfigFS interface for H3 mainline kernel
- update of mainline u-boot to 2016.09 should fix boot failures on H3 boards with eMMC
- disabled USB keyboard support in mainline u-boot should fix boot failures with connected USB devices

Desktop images:

- WICD was replaced with NetworkManager
- ALSA was replaced with PulseAudio
- sunxi boards: [GLshim](https://github.com/ptitSeb/glshim) was added to desktop images with Mali support (except for Orange Pi Plus and Orange Pi Plus 2e)
- sunxi boards: prebuilt mpv now supports OSD and subtitles, activated by setting environment variable `VDPAU_OSD=1`

Build script:

- complete desktop building rework - now packages are built from sources
- added Lime 2 eMMC as build target (WIP)
- added Pine64 / Pine64+ mainline (dev) target (experimental)
- added FriendlyArm Neo as build target
- fixed MT7601 wifi driver building
- github download rework
- external toolchain rework

Added additional packages, not installed by default:

- hostapd-realtek: replacement for hostapd with support for several Realtek Wi-Fi adapters
- fswebcam-gc2035: replacement for fswebcam with support for GC2035 camera driver for H3 based boards
- guvcview: replacement for stock guvcview with support for H3-based Orange Pi CMOS cameras

Known problems:

- Mali OpenGL ES does not work on H3 boards with 2GB RAM (Orange Pi Plus 2, Orange Pi Plus 2e)
- Hardware video decoding on A10/A20 based boards produces dark video
- Some applications that depend on livav libraries (i.e. minidlna) may not work on Jessie images

**v5.17 / 7.7.2016**

- bugfix release on some boards.

**v5.16 / 5.7.2016**

- bugfix release. In 5.15 we accidentaly overwrote default network settings. Check /etc/network/interfaces if you use advanced network settings or fixed ip.
- small changes.

**v5.15 / 1.7.2016**

- Added [improved camera driver](https://github.com/avafinger/gc2035) for Xunlong's cheap 2MP GC2035 camera
- Improved throttling/DRAM settings for the new 3 overheating H3 devices (BPi M2+, NanoPi M1, Beelink X2)
- Added official support for Beelink X2, NanoPi M1, Banana Pi M2+
- Improved console output (serial + display)
- Finally got rid of (broken) board auto detection. We do not ship any more one image for several devices that tries to detect/fix things on 1st boot but provide one dedicated image per board (Plus and Plus 2 and both NanoPi M1 variants being handled as the same device since only size of DRAM/eMMC differs)
- Tried to improve user experience with better/unified led handling (light directly after boot, communicate booting states through blinking)
- Improve partitioning and filesystem resize on 1st boot making it easier to clone every installation media afterwards
- fully support installation on eMMC on all H3 devices (`u-boot` and `nand-sata-install.sh` fixes)
- Improved performance/thermal/throttling behaviour on all H3 boards (especially newer Oranges)
- Prevent HDMI screen artefacts (disabling interfering TV Out by default)
- Enhanced 8189ETV driver for older Oranges
- Added support for OPi Lite, PC Plus and Plus 2E including new 8189FTV Wi-Fi (client, AP and monitoring mode, added fix for random MAC address)
- Added in-kernel corekeeper patch (bringing back killed CPU cores after heavy overheating situations when thermal situation is ok again)
- Added TV Out patch for Orange Pi PC
- Further improve driver compilation due to improved kernel headers scripts compilation
- Initrd support
- increased kernel version to 3.4.112
- Exchanged whole kernel source tree to [newer BSP variant](https://github.com/friendlyarm/h3_lichee), cleaned up sources, rebased all +100 patches (fixed display issues and kswapd bug, new and more performant GPU driver, increase Mali400MP2 clock to 600MHz)
- Added RTL2832U drivers to kernel (DVB-T)
- Fixed Docker on Odroid XU4
- Added overlay fs to Clearfog and Odroid XU4
- Many minor fixes

**v5.14 / 14.6.2016**

- all images rebuilt, most of them were manually tested
- added Beelink X2 image
- Cubox / Hummingboard kernel upgrade to 3.14.72 and 4.6.2
- Trusty was replaced with Xenial

**v5.12 / 31.5.2016**

- updated C1 images
- added wifi driver for new Oranges (modprobe 8189fs)
- added Orange Pi Lite, PC Plus and Plus 2E images

**v5.11 / 24.5.2016**

- Various bug fixes
- new working images for Actions Semi S500 boards

**v5.10 / 1.5.2016**

Images:

- all 3.10+ kernels [are Docker ready](http://forum.armbian.com/index.php/topic/490-docker-on-armbian/)
- all A10/A20/H3 comes with HW accelerated video playback in desktop build
- [fixed root exploit on H3 boards](https://github.com/igorpecovnik/lib/issues/282)
- [fixed kswapd 100% bug on H3 boards](https://github.com/igorpecovnik/lib/issues/219)
- fixed SPDIF / I2S audio driver in legacy kernel
- fixed Udoo Neo wireless
- fixed slow SD cards boot
- fixed Allwinner SS driver
- fixed bluetooth on Cubietruck, both kernels
- fixed wireless driver on H3 boards
- [fixed R1 switch driver](https://github.com/igorpecovnik/lib/commit/94194dc06529529015bfd04767865bbd04d29d9b)
- kernel for Allwinner boards was upgraded to 3.4.112 & 4.5.2
- kernel for iMx6 boards was upgraded to 3.14.67 & 4.5.2
- kernel for Armada (Clearfog) was upgraded to 3.10.101 & 4.5.2
- kernel for Udoo boards was updated to 3.14.67 & 4.4.8
- kernel for Guitar (Lemaker) was upgraded to 3.10.101
- kernel for H3/sun8i legacy come from new Allwinner updated source (friendlyarm)
- [added support for Olimex Lime2 eMMC](https://github.com/igorpecovnik/lib/issues/258)
- [increased MALI clockspeed on sun8i/legacy](https://github.com/igorpecovnik/lib/issues/265)
- added [Armbianmonitor](http://forum.armbian.com/index.php/topic/881-prepare-v51-v201604/?p=7095)
- added Odroid C1, C2(arm64), Nanopi M1, Banana M2+, Pcduino 2 and Pcduino 3. CLI and desktop
- added wifi radar to desktop
- added preview mainline kernel images for H3 boards (4.6.RC1)
- added initrd creation on all Allwinner images
- added Hummigboard 2 with working PCI and onboard wireless with legacy kernel 3.14.65
- added eMMC installer for H3
- added support for IFB and net scheduling for sun7i-legacy
- added ax88179_178a USB 3.0 Ethernet driver for sun7i-legacy
- hostapd comes as separate package (armbian-hostapd)
- changed first boot procedure and force user creation
- verbose / no verbose boot works almost on all boards
- enabled I2S on sun8i
- removed Debian Wheezy from auto build
- installing headers autocompile scripts
- all images come compressed with 7zip

Build script:

- GCC 5 support for mainline and allwinner legacy
- RAW images are not compressed by default
- added arm64 building support
- added docker as host
- Added Belink X2 (H3 based media player), and Roseapple (S500) as WIP target
- introducted CLI_TARGET per board
- prepared FEL boot
- prepared Xenial target
- fixed USB redirector building on all kernels
- support for Xenial as a build host is 95% ready.
- implemented automatic toolchain selection
- come cleanup, configurations are subfoldered
- extended_deboostrap becomes default

Known bugs:

- Udoo Neo reboots takes a while, 1min+
- headers within sun8i needs some fixing
- H3 board autodetection fail under certain conditions

**v5.06 / 18.3.2016**

- increase kernel version to 3.4.111
- headers auto creation while install (eases kernel/driver compilation)
- improved SD card partitioning to help old/slow cards with wear leveling and garbage collection
- Possible to use _Ubuntu Xenial Xerus_ as target
- changed behaviour of board leds (green == power, red == warning)
- speed improvements for 1st automated reboot
- Integrates OverlayFS backport

**v5.05 / 8.3.2016**

- Auto detection for the Orange Pi 2 does work now
- Mali acceleration works for all users not only root
- verbose boot logging on 1st boot and after crashes (you can toggle verbose logging using `sudo armbianmonitor -b`)
- more WiFi dongles supported due to backported firmware loader patch
- all 3 USB ports on Orange Pi One (Lite) available ([2 of them need soldering](http://forum.armbian.com/index.php/topic/755-tutorial-orange-pi-one-adding-usb-analog-audio-out-tv-out-mic-and-ir-receiver/))
- I2S possible on all Orange Pis (compare with the [mini tutorial](http://forum.armbian.com/index.php/topic/759-tutorial-i2s-on-orange-pi-h3/) since you need to tweak script.bin)
- default display resolution set to 720p60 to fix possible overscan issues on 1st boot
- HW accelerated video decoding works for most formats
- Booting from eMMC on OPi Plus now possible
- Udoo quad images upgraded to 4.4.4

**v5.04 / 1.3.2016**

- HDMI/DVI works (bug in boot.cmd settings)
- Reboot issues fixed (bug in fex settings)
- 1-Wire useable (we chose to stay compatible to loboris' images so the data pin is 37 by default. You're able to change this in the [fex file](https://github.com/igorpecovnik/lib/blob/6d995e31583e5361c758b401ea44634d406ac3da/config/orangepiplus.fex#L1284-L1286))
- changing display resolution and choosing between HDMI and DVI is now possible with the included _h3disp_ tool (should also work in the [stand-alone version](http://forum.armbian.com/index.php/topic/617-wip-orange-pi-one-support-for-the-upcoming-orange-pi-one/?p=5480) with Debian based OS images from loboris/Xunlong). Use `sudo h3disp` in a terminal to get the idea.
- Ethernet issues fixed (combination of kernel and fex fixes)
- USB-to-SATA bridge on the Orange Pi Plus works
- stability problems on Orange Pi One fixed (due to undervoltage based on wrong fex settings)
- problems with 2 USB ports on the PC fixed (wrong kernel config)
- Mali400MP acceleration (EGL/GLES) works now
- suspend to RAM and resume by power button works now (consumption less than 0.4W without peripherals)
- Enforce user account creation before starting the GUI
- USB and Ethernet IRQs distributed nicely accross CPU cores
- Full HDMI colour-range adjustable/accessible through _h3disp_ utility
- already useable as stable headless/server board
- rebuilt Cubieboard 1 & 2 with 3.4.110 and 4.4.3
- fixed Bluetooth on Cubietruck + rebuild with 3.4.110 and 4.4.3
- all new images has no login policy: forced user generation

**v5.03 / 20.2.2016**

- H3 images rebuilt

**v5.02 / 18.2.2016**

- H3 images rebuilt

**v5.01 / 17.2.2016**

- Bugfix update for [Allwinner boards](http://forum.armbian.com/index.php/topic/691-banana-pro-testers-wanted-sata-drive-not-working-on-some-boards/)
- Update [for H3 based boards](https://github.com/igorpecovnik/lib/commit/c93d7dfb3538c36739fb8841bd314d75e7d7cbe5)

**v5.00 / 12.2.2016**

- mainline kernel for Allwinner based boards upgraded to 4.4.1
- Allwinner audio driver playback and capture on kernel 4.4.1, [UAS](http://linux-sunxi.org/USB/UAS), USB OTG, battery readings,
- added Marvel Armada kernel 3.10.96, 4.4.1 and patches for changing mPCI to SATA
- added Cubox / Hummingboard kernel 4.4.1 (serial console only)
- firstrun does autoreboot only if needed: wheezy and some legacy kernels.
- [added motd](http://forum.armbian.com/index.php/topic/602-new-motd-for-ubuntudebian/#entry4223) to /etc/updated.motd ... redesign, added battery info for Allwinner boards, bugfix, coloring
- fixed temperature reading on Cubox / Hummingboard legacy kernel
- fixed FB turbo building on Allwinner
- fixed NAND install on A10 boards (Legacy kernel only)
- fixed USB boot, added PWM on mainline
- fixed Banana PRO/+ onboard wireless on mainline kernel - running with normal Banana DT.
- readded USB sound
- added [A13 Olimex SOM](https://www.olimex.com/Products/SOM/A13/A13-SOM-512/)
- added [LIRC GPIO receive and send driver](https://github.com/igorpecovnik/lib/issues/135) for legacy Allwinner
- added LED MMC activity to mainline kernels for Cubietruck and Cubieboard A10
- build script: option to build images with F2FS root filesystem for Allwinner boards
- build script: added alternative kernel for Lemaker Guitar (NEXT), Cubox (DEV)


**v4.81 / 28.12.2015**

- complete build script rework
- new development kernel package linux-image-dev-sunxi (4.4RC6) for Allwinner boards
- added Lemaker Guitar, kernel 3.10.55
- added Odroid XU3/4, kernel 3.10.94 and mainline 4.2.8
- mainline kernel for Allwinner based boards upgraded to 4.3.3
- Udoo mainline upgraded to 4.2.8, legacy to 3.14.58
- cubox / hummingboard upgraded to 3.14.58, added mainline kernel 4.4
- fixed Jessie RTC bug, systemd default on Jessie images

**v4.70 / 30.11.2015**

- Bugfix update(apt-get update && apt-get upgrade)
- small changes and fixes

**v4.6 / 24.11.2015**

- Update only (apt-get update && apt-get upgrade)
- mainline kernel for Allwinner based boards upgraded to 4.2.6
- Legacy kernel for Allwinner based boards upgraded to 3.4.110
- added new board: Udoo Neo
- added USB printer, CAN, CMA, ZSWAP, USB video class, CDROM fs, sensor classs, … to Allwinner mainline kernel
- nand-sata-install scripts rewrite. Now it’s possible to install to any partition.
- fixed nand install for Allwinner A10 based boards: Cubieboard 1 / Lime A10
- universal upgrade script bugfix / rewrite.
- 8 channel HDMI support for legacy Allwinner kernel
- unattended upgrade fixed
- sunxi tools fixed
- added two new options to build script: keep kernel config and use_ccache
- added kernel version to motd

**v4.5 / 14.10.2015**

- mainline kernel upgraded to 4.2.3 for Allwinner based boards
- legacy kernel for Allwinner compiled from new sources (linux-sunxi)
- udoo mainline upgraded to 4.2.3
- cubox / hummingboard upgraded to 3.14.54
- changed kernel naming: A10 = linux-image-sun4i, A20 = linux-image-sun7i
- new boards: Banana M2, Orange+(A31S), Cubieboard 1, Cubieboard 2 Dual SD, Lime A10
- fixed Udoo legacy wireless problems
- fixed Jessie boot problems by disabling systemd. It’s possible to re-enable within boot scripts
- added ramlog to Jessie because we don’t have systemd anymore
- changed wireless driver for Cubietruck and Banana PRO (now it’s ap6210)
- added ZRAM to mainline kernel
- fixed dvbsky modules

and a bunch of small fixes.

**v4.4 / 1.10.2015**

Images:

- mainline kernel upgrade to 4.2.2 (Allwinner, Udoo Quad),
- legacy kernel upgraded to 3.4.109 (Allwinner),
- added I2C support and bunch of multimedia modules (DVB) (mainline Allwinner),
- Udoo quad images with fixed legacy kernel 3.14.28,
- Cubox and Hummingboard kernel upgrade to 3.14.53,
- brcmfmac driver fixes for mainline kernel (Banana PRO / Cubietruck)
- performance tweak: choosing a closest Debian mirror (Debian images)
- added Astrometa DVB firmware and dvb-tools
- added Nikkov SPDIF / I2S recent patch (legacy Allwinner)
- added patch for rtl8192cu: Add missing case in rtl92cu_get_hw_reg (Lamobo R1)
- bigger NAND boot partition on install
- install script bug fixes

Script:

- force apt-get update on older rootfs cache,
- image harden manipulation security,
- packages NAND/FAT/same version install faling fixed,
- image shrinking function rework,
- better packages installation install checking,
- added Debian keys to suppress warnings in debootstrap process,
- added fancy progress bars,
- added whiptail downloading prior to usage (bugfix).

**v4.3 / 17.9.2015**

- kernel 4.2 for Allwinner based boards
- kernel 4.2 for Udoo Quad
- walk-around if ethernet is not detected on some boards due to RTC not set(?)
- update is done (semi) automatic if you are using Armbian 4.2. You only need to issue command: apt-get update && apt-get upgrade. If you are coming from older system, check Documentation
- U-boot on R1 is now updated to latest stable version (2015.07)
- Fixed AW SOM. Working with latest u-boot but you need to build image by yourself.
- Enabled whole USB net and HID section in kernel for Allwinner boards v4.2
- Fixed upgrade script – only some minor bugs remains.
- Fixes to build script that it’s working under Ubuntu 15.04
- Adding Bananapi Wireless driver (ap6210) back to legacy kernel
- Udoo official kernel (3.14.28) not updated due too many troubles.

**v4.2 / 1.9.2015**

Images:

- Upgraded NAND / SATA installer. Possible to install to SATA/NAND boot in one step.
- Easy kernel switching between old 3.4 and 4.x
- Automatic kernel updating (to disable comment armbian repo /etc/apt/sources.list)
- Allwinner boards share one 4.x kernel and two 3.4
- All boards share the same revision number
- One minimal Ubuntu Desktop per board (Wicd, Firefox, Word)
- u-boot v2015.07 for most boards
- Aufs file system support
- kernel 4.1.6 and 3.4.108
- Added Orangepi Mini, Cubieboard 1 (4.x only), Udoo with official kernel
- Repository for Wheezy, Jessie and Trusty
- enabled USB audio in kernel 4.x
- kernel headers fixed. No need to rebuild when you update the kernel.
- fixed boot scripts that can load from FAT partition too
- removed Cubox binnary repository because of troubles
- Docker support (kernel 4.x). Already here for a while / forget to mention.
- nodm change default login

Build script:

- changed structure: sources now in folder sources, output is what we produce, deb in one folder
- expanded desktop part
- possible to build all images at once, create package repository
- SD card initial size is 4Gb, variable transfered into configuration.sh
- Avaliable board list is now created from file configuration.sh
- Fixed image shrinking problem
- Patching part rework
- Using first FAT boot partition now fixes boot scripts
- Uboot TAG moved to configuration.sh and differs for some boards
- new variables for source branches. Only too remove errors when checking out

**v4.1 / 5.8.2015**

- Added desktop image
- U-Boot 2015.07 with many new features
- Added auto system update via repository apt.armbian.com
- Root password change is initialized at first boot.
- 3.4.108 kernel fixes, 4.1.4 Allwinner Security System

**v4.0 / 12.7.2015**

- Fixed stability issues, temperature display in 4.x
- Kernel upgrades to 3.4.108 and 4.1.2

**v3.9 / 11.6.2015**

- Bugfix release
- Kernel 4.0.5 traffic control support
- SATA / USB install fixed on kernel 4.x
- Added 256Mb emergency swap area, created automatically @first boot

**v3.8 / 21.5.2015**

- Bugfix release: Cubietruck images successfully booted on Cubietruck. I waited for automatic reboot than tested remote login.
- Kernel 4.0.4 added support for power on/off button
- Both: Jessie fixed, Ethernet init fixed (uboot)
- armbian.com introduction

**v3.7 / 14.5.2015**

- Kernel 4.0.3 some new functionality
- Kernel 3.4.107 added sunxi display manager to change FB on demand
- Both: Ubuntu and jessie install errors fixed, removed busybox-syslogd and changed to default logger due to problems in Jessie and Ubuntu, apt-get upgrade fixed, documentations update, Uboot fixed to 2015.4 – no more from dev branch
- Build script rework - image size shrink to actual size, possible to have fat boot partition on SD card, several script bug fixes

**v3.6 / 29.4.2015**

- Kernel 3.19.6
- Kernel 3.4.107 with better BT loading solution

**v3.5 / 18.4.2015**

- Kernel 3.19.4: fixed AP mode, fixed USB, added 8192CU module
- Common: apt-get upgrade ready but not enabled yet, serial console fixed, fixed hostapd under jessie, easy kernel switching, latest patched hostapd for best performance – normal and for realtek adaptors, auto IO scheduler script
- Build script: everything packed as DEB

**v3.4 / 28.3.2015**

- Kernel 3.19.3: docker support, apple hid, pmp, nfsd, sata peformance fix
- Kernel 3.4.106: pmp, a20_tp - soc temp sensor
- Common: console setup fixed, headers bugfix, nand install fix
- Build script: kernel build only, custom packets install, hardware accelerated desktop build as option

**v3.3 / 28.2.2015**

- Kernel 3.19.0: many new functionality and fixes.
- Bugfixes: CT wireless works in all kernels

**v3.2 / 24.1.2015**

- Possible to compile external modules on both kernels
- Kernel 3.19.0 RC5
- Bugfixes: install script, headers, bashrc, spi

**v3.1 / 16.1.2015**

- Kernel 3.19.0 RC4
- Added Cubieboard 1 images
- Dualboot for CB2 and CT dropped due to u-boot change. Now separate images.
- New user friendly SATA + USB installer, also on mainline

**v3.0 / 29.12.2014**

- Kernel 3.18.1 for mainline image
- Added Ubuntu Trusty (14.04 LTS) image
- Bugfixes: auto packages update

**v2.9 / 3.12.2014**

- Kernel 3.4.105 with new MALI driver and other fixes
- Added: Jessie image
- Major build script rewrite - much faster image building
- Fixed: failed MIN/MAX settings

**v2.8 / 17.10.2014**

- Added: ondemand governor, fhandle, squashfs and btrfs
- Removed: bootsplash, lvm, version numbering in issue
- Fixed: custom scripts, Jessie upgrade
- Disabled: BT firmware loading, enable back with: insserv brcm40183-patch
- Added working driver for RT 8188C, 8192C

**v2.7 / 1.10.2014**

- Kernel 3.4.104
- Automatic Debian system updates
- VGA output is now default but if HDMI is attached at first boot than it switch to HDMI for good. After first restart!
- Fixed NAND install script. /boot is mounted by default. Kernel upgrade is now the same as on SD systems.
 Cubieboard2 - disabled Cubietruck dedicated scripts (BT firmware, LED disable)
- Added network bonding and configuration for "notebook" mode (/etc/network/interfaces.bonding)
- IR receiver is preconfigured with default driver and LG remote (/etc/lirc/lircd.conf), advanced driver is present but disabled
- Added SPI and LVM functionality
- Added Debian logo boot splash image
- Added build essentials package

**v2.6 / 22.8.2014**

- Kernel 3.4.103 and 3.17.0-RC1
- Added GPIO patch (only for 3.4.103)

**v2.5 / 2.8.2014**

- Kernel 3.4.101 and 3.16.0-RC4
- major build script rewrite

**v2.4 / 11.7.2014**

- Kernel 3.4.98
- default root password (1234) expires at first login
- build script rewrite, now 100% non-interactive process, time zone as config option
- bug fixes: removed non-existing links in /lib/modules

**v2.3 / 2.7.2014**

- Kernel 3.4.96
- cpuinfo serial number added
- bug fixes: stability issues - downclocked to factory defaults, root SSH login enabled in Jessie, dedicated core for eth0 fix
- disp_vsync kernel patch

**v2.2 / 26.6.2014**

- Kernel 3.4.94
- Added Jessie distro image
- Updated hostapd, bashrc, build script
- bug fixes: disabled upgrade and best mirror search @firstboot, bluetooth enabler fix
- MD5 hash image protection

**v2.1 / 13.6.2014**

- Kernel 3.4.93
- Onboard Bluetooth finally works
- Small performance fix
- Allwinner Security System cryptographic accelerator

**v2.0 / 2.6.2014**

- Kernel 3.4.91 with many fixes
- Cubieboard 2 stability issues fix
- eth0 interrupts are using dedicated core
- Global bashrc /etc/bash.bashrc
- Verbose output and package upgrade @ first run

**v1.9 / 27.4.2014**

- Kernel headers included
- Clustering support
- Advanced IR driver with RAW RX and TX
- Bluetooth ready (working only with supported USB devices)
- Bugfixes: VLAN, login script, build script
- New packages: lirc, bluetooth

**v1.8 / 27.3.2014**

- Kernel 3.4.79
- Alsa I2S patch + basic ALSA utils
- Performance tweaks: CPU O.C. to 1.2Ghz, IO scheduler NOOP for SD, CFQ for sda, journal data writeback enabled
- Avaliable memory = 2000MB
- Minimized console output at boot
- MAC address from chip ID, manual optional
- Latest (Access point) hostapd, 2.1 final release
- Login script shows current CPU temp, hard drive temp & actual free memory
- Fastest Debian mirror auto selection @first boot
- New packages: alsa-utils netselect-apt sysfsutils hddtemp bc

**v1.7 / 26.2.2014**

- Flash media performance tweaks, reduced writings, tmp & logging to RAM with ramlog app – sync logs on shutdown
- SATA install script
- Dynamic MOTD: Cubieboard / Cubietruck
- Disabled Debian logo at startup
- New packages: figlet toilet screen hdparm libfuse2 ntfs-3g bash-completion

**v1.6 / 9.2.2014**

- Added support for Cubieboard 2
- Build script creates separate images for VGA and HDMI
- NAND install script added support for Cubieboard 2

**v1.52 / 7.2.2014**

- Various kernel tweaks, more modules enabled
- Root filesystem can be moved to USB drive
- Bugfixes: NAND install script

**v1.5 / 22.1.2014**

- Hotspot Wifi Access Point / Hostapd 2.1
- Bugfixes: MAC creation script, SSH keys creation, removed double packages, …
- Graphics desktop environment upgrade ready

**v1.4 / 12.1.2014**

- Patwood’s kernel 3.4.75+ with many features
- Optimized CPU frequency scaling 480-1010Mhz with interactive governor
- NAND install script included
- Cubietruck MOTD
- USB redirector – for sharing USB over TCP/IP

**v1.3 / 3.1.2014**

- CPU frequency scaling 30-1000Mhz
- Patch for gpio

**v1.23 / 1.1.2014**

- added HDMI version
- added sunxi-tools
- build.sh transfered to Github repository
- disabled LED blinking

**v1.2 / 26.12.2013**

- changed kernel and hardware config repository
- kernel 3.4.61+
- wi-fi working
- updated manual how-to

**v1.0 / 24.12.2013**

- total memory available is 2G (disabled memory for GPU by default)
- gigabit ethernet is fully operational
- sata driver enabled
- root filesystem autoresize
- MAC address fixed at first boot
- Kernel 3.4.75
- root password=1234
- Bugs: wifi and BT not working
