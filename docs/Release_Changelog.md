# Changelog

* Note: If a new sub-version is released this does not necessarily mean all boards receive a new version number since most of the time these fixes are targeting a specific board or board family only.


## v21.08 (2021-08-31)

### Solved Bug

* [AR-886](https://armbian.atlassian.net/browse/AR-886) - u-boot package naming
* [AR-885](https://armbian.atlassian.net/browse/AR-885) - Odroid C4 / HC4 boot failure
* [AR-881](https://armbian.atlassian.net/browse/AR-881) - First login shows "degraded"
* [AR-879](https://armbian.atlassian.net/browse/AR-879) - RK3328 5.10 \+ GPU failure
* [AR-875](https://armbian.atlassian.net/browse/AR-875) - Homepage fix
* [AR-874](https://armbian.atlassian.net/browse/AR-874) - Add SATA fix for eBin
* [AR-873](https://armbian.atlassian.net/browse/AR-873) - khadas vim3 no sound
* [AR-872](https://armbian.atlassian.net/browse/AR-872) - When reverting u-boot to last known, some boards are broken
* [AR-867](https://armbian.atlassian.net/browse/AR-867) - H6 Freezing
* [AR-863](https://armbian.atlassian.net/browse/AR-863) - Unstable u-boot also noticed on H3 based boards
* [AR-862](https://armbian.atlassian.net/browse/AR-862) - normalize RK3399 xorg configs
* [AR-857](https://armbian.atlassian.net/browse/AR-857) - Qemu custom hook executing on non-targeted images
* [AR-854](https://armbian.atlassian.net/browse/AR-854) - Pinebook PRO desktop doesn't build in CI
* [AR-853](https://armbian.atlassian.net/browse/AR-853) - Missing folder when making BSP file
* [AR-852](https://armbian.atlassian.net/browse/AR-852) - Error when placing wallpaper
* [AR-850](https://armbian.atlassian.net/browse/AR-850) - Disable XFWM compositor on XFCE4 desktop to make it run smoother
* [AR-844](https://armbian.atlassian.net/browse/AR-844) - CI is picking up wrong kernel
* [AR-835](https://armbian.atlassian.net/browse/AR-835) - Amlogic GLX desktop fails
* [AR-834](https://armbian.atlassian.net/browse/AR-834) - edge v network weirdness
* [AR-833](https://armbian.atlassian.net/browse/AR-833) - Khadas Edge V no HDMI audio
* [AR-830](https://armbian.atlassian.net/browse/AR-830) - CI needs to rsync cache before start to building new images.
* [AR-829](https://armbian.atlassian.net/browse/AR-829) - CI pipeline could not find some files when signing rootfs cache
* [AR-825](https://armbian.atlassian.net/browse/AR-825) - Fixing I2S related errors on RK3399
* [AR-824](https://armbian.atlassian.net/browse/AR-824) - Broken wifi on Station boards and kernel 5.12.y
* [AR-823](https://armbian.atlassian.net/browse/AR-823) - Pine H64 doesn't boot kernel 5.12.y
* [AR-822](https://armbian.atlassian.net/browse/AR-822) - Motd false reporting of unsupported
* [AR-821](https://armbian.atlassian.net/browse/AR-821) - Docker creation failed to load repository keys
* [AR-820](https://armbian.atlassian.net/browse/AR-820) - Broken Odroid C2 audio patch
* [AR-819](https://armbian.atlassian.net/browse/AR-819) - Wireguard repo errors
* [AR-818](https://armbian.atlassian.net/browse/AR-818) - When building selected images via CI, status is changed to user-built
* [AR-816](https://armbian.atlassian.net/browse/AR-816) - ZRAM is missing in Jeston Nano legacy
* [AR-780](https://armbian.atlassian.net/browse/AR-780) - Nanopi R4S USB broken
* [AR-779](https://armbian.atlassian.net/browse/AR-779) - New bsp package is common. Per branch changes doesn't work anymore
* [AR-777](https://armbian.atlassian.net/browse/AR-777) - Docker doesn't install on Hirsute host
* [AR-776](https://armbian.atlassian.net/browse/AR-776) - Tinkerboard legacy have some troubles booting
* [AR-774](https://armbian.atlassian.net/browse/AR-774) - Orangepi Lite 2 EDGE is failing
* [AR-770](https://armbian.atlassian.net/browse/AR-770) - U-boot fails to install when switching kernel to EDGE
* [AR-764](https://armbian.atlassian.net/browse/AR-764) - Htop configuration exploit / vulnerability
* [AR-749](https://armbian.atlassian.net/browse/AR-749) - Allwinner A20 bootloops on 5.12.y / 2021.04
* [AR-748](https://armbian.atlassian.net/browse/AR-748) - Headers install broken
* [AR-747](https://armbian.atlassian.net/browse/AR-747) - Deeping Desktop doesn't want to reboot / poweroff
* [AR-744](https://armbian.atlassian.net/browse/AR-744) - Nanopi K2 S905 network is broken
* [AR-741](https://armbian.atlassian.net/browse/AR-741) - Pinebook pro desktop missing tweaks
* [AR-740](https://armbian.atlassian.net/browse/AR-740) - Vnstat throws out garbage
* [AR-737](https://armbian.atlassian.net/browse/AR-737) - Jetson nano throws out some error on boot loader compilation
* [AR-736](https://armbian.atlassian.net/browse/AR-736) - Rockpi S u-boot doesn't build on GCC.-10
* [AR-713](https://armbian.atlassian.net/browse/AR-713) - Board specific desktop things are going into common desktop package
* [AR-593](https://armbian.atlassian.net/browse/AR-593) - Rockpi S doesn't boot mainline based kernel


### Epic


* [AR-788](https://armbian.atlassian.net/browse/AR-788) - Add Official Support for Some Khadas devices


### Story


* [AR-877](https://armbian.atlassian.net/browse/AR-877) - build\_all needs separate logs per image
* [AR-847](https://armbian.atlassian.net/browse/AR-847) - Tinkerboard 2 Support
* [AR-746](https://armbian.atlassian.net/browse/AR-746) - Upgrade EDGE to 5.12.y
* [AR-734](https://armbian.atlassian.net/browse/AR-734) - CSC Support for Avnet MicroZed
* [AR-214](https://armbian.atlassian.net/browse/AR-214) - CI improvements
* [AR-202](https://armbian.atlassian.net/browse/AR-202) - Drop packaging patches and introduce own packaging
* [AR-42](https://armbian.atlassian.net/browse/AR-42) - Merge packaging patches


### Closed tasks


* [AR-892](https://armbian.atlassian.net/browse/AR-892) - Promoting Bullseye to supported
* [AR-890](https://armbian.atlassian.net/browse/AR-890) - Desktop analysis with 3D enabled
* [AR-887](https://armbian.atlassian.net/browse/AR-887) - Re-enable Debian Stretch repository update
* [AR-882](https://armbian.atlassian.net/browse/AR-882) - Optimise image compression
* [AR-876](https://armbian.atlassian.net/browse/AR-876) - Make package lists in one row
* [AR-869](https://armbian.atlassian.net/browse/AR-869) - Upgrade ZFS on Linux to v2.1.0 \(Focal / Bionic only\)
* [AR-865](https://armbian.atlassian.net/browse/AR-865) - Updating driver for 2.5G NIC on Helios64
* [AR-864](https://armbian.atlassian.net/browse/AR-864) - Upgrading EDGE to K5.13.y
* [AR-859](https://armbian.atlassian.net/browse/AR-859) - set - [apt.armbian.com](http://apt.armbian.com) - redirect default to http instead of https
* [AR-856](https://armbian.atlassian.net/browse/AR-856) - Basic RC Branch build support
* [AR-846](https://armbian.atlassian.net/browse/AR-846) - Add Ubuntu 21.10 Impish
* [AR-794](https://armbian.atlassian.net/browse/AR-794) - Khadas Edge-V support
* [AR-793](https://armbian.atlassian.net/browse/AR-793) - Khadas VIM3L support
* [AR-792](https://armbian.atlassian.net/browse/AR-792) - Preliminary Khadas VIM3 support
* [AR-791](https://armbian.atlassian.net/browse/AR-791) - Khadas VIM2 support
* [AR-790](https://armbian.atlassian.net/browse/AR-790) - Preliminary Khadas VIM1 support
* [AR-785](https://armbian.atlassian.net/browse/AR-785) - Move mainline boot console to UART0 on Rockpi S
* [AR-784](https://armbian.atlassian.net/browse/AR-784) - Add Nvidia Jetson Nano legacy kernel
* [AR-782](https://armbian.atlassian.net/browse/AR-782) - Provides NFS mount functionality out of the box on CLI images
* [AR-778](https://armbian.atlassian.net/browse/AR-778) - Do not pre-install obsolete apt-transport-https
* [AR-768](https://armbian.atlassian.net/browse/AR-768) - Move Odroid XU4 EDGE to mainline source
* [AR-745](https://armbian.atlassian.net/browse/AR-745) - chroot packaging: build script as separate function
* [AR-743](https://armbian.atlassian.net/browse/AR-743) - Delay first-run autologin
* [AR-732](https://armbian.atlassian.net/browse/AR-732) - Unlock Ubuntu Hirsute as supported target
* [AR-714](https://armbian.atlassian.net/browse/AR-714) - Adjusting support status
* [AR-665](https://armbian.atlassian.net/browse/AR-665) - rk3399 patch failure
* [AR-649](https://armbian.atlassian.net/browse/AR-649) - Adding Rockchip VPU support for 5.11.y
* [AR-635](https://armbian.atlassian.net/browse/AR-635) - Add legacy kernel for Zero2
* [AR-537](https://armbian.atlassian.net/browse/AR-537) - Create Armbian “virtual” build target to run as VM
* [AR-519](https://armbian.atlassian.net/browse/AR-519) - Odroid N2 Mainline u-boot for edge kernel
* [AR-315](https://armbian.atlassian.net/browse/AR-315) - Add support for GPT table inside nand-sata-install


## v21.05.6 (2021-06-21)

Solved Bugs

<ul>
<li>Updated images for Orangepi Zero</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-593">AR-593</a>] - Rockpi S doesn't boot mainline kernel</li>
</ul>
 
## v21.05.3 (2021-05-24)

Solved Bugs

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-780">AR-780</a>] - Nanopi R4S USB broken</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-780">AR-816</a>] - ZRAM is missing in Jeston Nano legacy</li>
</ul>
 
## v21.05.2 (2021-05-24)

Solved Bugs

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-748">AR-748</a>] - Headers install broken</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-740">AR-740</a>] - Vnstat throws out garbage</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-764">AR-764</a>] - Fixing Htop security issue</li> 
</ul> 
 
Closed Tasks 

<ul>
<li>ZFS updated to v2.0.4 (tested on 32bit Odroid HC1 and 64bit N2, Focal and Bionic userland)</li>
<li>Added Hirsute CLI images with EDGE Linux 5.12.y for most of the boards</li>
</ul>
 
## v21.05 (2021-05-09)

Solved Bugs
<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-730">AR-730</a>] -          Duplicate packages error when updating repository
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-729">AR-729</a>] -          Fix Partition Alignment for resizes and nand-sata-install
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-711">AR-711</a>] -          Network troubles on Nanopi K2 / Odroids
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-709">AR-709</a>] -          Tinkerboard AP crash on client connect
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-708">AR-708</a>] -          Missing library for compiling u-boot
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-707">AR-707</a>] -          Wrong keyboard code detected
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-705">AR-705</a>] -          Compilation issues when building old u-boot
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-698">AR-698</a>] -          XU4 - current kernel oddness with docker
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-697">AR-697</a>] -          Fix Meson64 Default Governor
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-688">AR-688</a>] -          Firefly boot broken
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-674">AR-674</a>] -          Users can't change desktop wallpaper on Gnome
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-666">AR-666</a>] -          ZSH is disabled on upgrade
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-662">AR-662</a>] -          Distribution support status is not written to the /etc/armbian-release
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-659">AR-659</a>] -          Rootfs image runs out of inodes during build
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-653">AR-653</a>] -          builder issue with gnome
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-647">AR-647</a>] -          Wireless driver 8811CU is broken on 5.11.y
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-646">AR-646</a>] -          Bootsplash breaks compilation on 5.11.y
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-644">AR-644</a>] -          Wireless driver 8188 EU broken and disabled since 5.9.y
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-636">AR-636</a>] -          Odroid N2+ lost additional freq values
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-585">AR-585</a>] -          HDMI-CEC not working on rockchip64 Legacy
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-88">AR-88</a>] -          Banana Pi M3 does not boot
</ul>
 
Finished projects

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-694">AR-694</a>] -          Create Jira-based checklist for Desktop Testing
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-457">AR-457</a>] -          Enable native arm/arm64 building
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-454">AR-454</a>] -          Additional Desktop Configurations for use with new framework
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-444">AR-444</a>] -          Improving download infrastructure Phase 2
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-200">AR-200</a>] -          Improving Desktop images
</ul>

Closed Tasks

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-714">AR-714</a>] -          Adjusting support status
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-710">AR-710</a>] -          Create imx edge branch
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-706">AR-706</a>] -          Bump Allwinner u-boot to 2021.04
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-704">AR-704</a>] -          Distinguish between edge and normal image in motd
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-696">AR-696</a>] -          Improve Nvidia Jetson Nano support
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-673">AR-673</a>] -          Add few missing packages
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-670">AR-670</a>] -          Add additonal mirros for linux-firmware beside kernel source
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-667">AR-667</a>] -          Move Meson64 DEV to 5.10.y
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-657">AR-657</a>] -          Add instructions how to manual flash boot loader
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-656">AR-656</a>] -          Implement timeout on cache download
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-654">AR-654</a>] -          Fix stability issues of NanoPi M4V2 in current and dev
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-651">AR-651</a>] -          NanoPC-T4 legacy: enable USB-C DisplayPort & eDP outs
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-648">AR-648</a>] -          Resolve GPIO & PWM patches on mvebu
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-645">AR-645</a>] -          Detach rtl8812au from fixed commit ID if it builds from master
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-643">AR-643</a>] -          Bump DEV kernels to 5.11.y
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-634">AR-634</a>] -          Add Orangepi R1 Plus
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-633">AR-633</a>] -          Enable  hardware PRNG/TRNG/SHA on sun8i-ce platform
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-613">AR-613</a>] -          test/beta img auto builder
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-612">AR-612</a>] -          Update pine64 install instructions
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-600">AR-600</a>] -          RK3399's: Add multimedia and OC overlays
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-599">AR-599</a>] -          Enable HDMI-CEC and ISP1 camera support for rk3399 and rockchip64 legacy
</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-369">AR-369</a>] -          Check kernel config changes
</ul>


## v21.02.4 (2021-04-04)

<ul>
<li> Added Nvidia Jetson Nano (community supported target)
</li>
<li>Rebuild images for Odroid N2, H4, HC4
</li>
</ul>

## v21.02.3 (2021-03-09)

<ul>
<li> All kernels received upstream updates
</li>
<li> All images has been rebuilt
</li>
<li>Fixed reboot troubles on meson64 family (Odroid N2, C2, H4, HC4)
</li>
<li>ZSH upgrade fixed
</li>
<li>Type-C DP support for the NanoPC T4
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-654'>AR-654</a>] -         NanoPi M4V2 stability fix for current and dev
</li>
<li>Allwinner a20 fail to init hdmi in many cases / fixed (all images need to be rebuilt)
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-660'>AR-660</a>] -         Attempt to improve stability on Helios64
</li>
</ul>

## v21.02.2 (2021-02-16)

<ul>
<li> All kernels received upstream updates
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-633'>AR-633</a>] -         Enable  hardware PRNG/TRNG/SHA on sun8i-ce platform
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-636'>AR-636</a>] -         Odroid N2+ lost additional freq values
</li>
</ul>

## v21.02.1 (2021-02-03)

Finished projects

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-235'>AR-235</a>] -         Implement Device Tree Editor
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-476'>AR-476</a>] -         Add sound to Odroid N2
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-485'>AR-485</a>] -         Improve multicore compilation
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-487'>AR-487</a>] -         Rework download pages
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-508'>AR-508</a>] -         Add Odroid HC4
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-546'>AR-546</a>] -         Added Pine64 Pinecube
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-566'>AR-566</a>] -         Add Nanopi R4S
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-568'>AR-568</a>] -         Add Orangepizero 2 WIP target
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-571'>AR-571</a>] -         Move Meson64 DEV to 5.10.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-589'>AR-589</a>] -         Add ZShell via armbian-zsh package
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-590'>AR-590</a>] -         ZRAM Enhancements - decouple swap config from tmp
</li>
</ul>

Solved bugs

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-365'>AR-365</a>] -         4k not detected properly on Amlogic, Rockchip devices
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-440'>AR-440</a>] -         Errors shown at 1st login under certain conditions
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-512'>AR-512</a>] -         Fix Ethernet for Opi3 and other devices with phymode for kernel 5.10
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-514'>AR-514</a>] -         Download and verify not fully reliable
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-547'>AR-547</a>] -         First login: adding a non-existing keyboard variant
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-548'>AR-548</a>] -         mvebu DFS seems to cause system hang under high I/O
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-557'>AR-557</a>] -         GCC compatibility issues
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-559'>AR-559</a>] -         First login script - not all locales have UTF8 encoding
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-565'>AR-565</a>] -         SATA on HC4 is not recognized
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-570'>AR-570</a>] -         Improper order in getty override.conf
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-584'>AR-584</a>] -         Nanopi M4V2 hangs on bluetooth loading
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-595'>AR-595</a>] -         Rockpi 4B 1GB not booting
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-605'>AR-605</a>] -         Booting troubles on Odroid C4 / HC4
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-606'>AR-606</a>] -         Force boot script update throws out some error
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-608'>AR-608</a>] -         Broken building out-of-tree modules
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-610'>AR-610</a>] -         Nanopi Neo2 black sometimes nic doesn&#39;t init
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-615'>AR-615</a>] -         Helios64 unstable 2.5Gbps Interface on LK5.x
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-616'>AR-616</a>] -         Ubuntu Bionic ZSH / BASH changing issue
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-617'>AR-617</a>] -         Locales detection doesn&#39;t work properly in some cases
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-627'>AR-627</a>] -         Ubuntu update is overwriting our welcome screen
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-629'>AR-629</a>] -         Odroid HC4 SATA failure
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-631'>AR-631</a>] -         Orangepi Zero2 broken network
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-632'>AR-632</a>] -         Desktop fails to load at second run
</li>
</ul>

Closed task

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-163'>AR-163</a>] -         Systematically cleanup distribution defaults
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-206'>AR-206</a>] -         Improve memory performance on Renegade (roc-rk3328-cc) in current
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-399'>AR-399</a>] -         Improve Pinebook PRO support
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-467'>AR-467</a>] -         Enable AUFS support back
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-472'>AR-472</a>] -         Added support for Ubuntu 20.10 Groovy
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-517'>AR-517</a>] -         Mark Bionic builds host as deprecated
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-520'>AR-520</a>] -         Move Rock64 to CSC in build script
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-525'>AR-525</a>] -         Bump Rockchip 32bit to 5.9.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-526'>AR-526</a>] -         Move mvebu-dev kernel to 5.9+
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-551'>AR-551</a>] -         Update fan configuration, enable network LED and enable UPS timer
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-552'>AR-552</a>] -         Re-enable UHS SDR104 mode for Helios64 and roc-rk3399-pc
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-553'>AR-553</a>] -         Update builder to retrieve web seeds from mirrors api
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-554'>AR-554</a>] -         OdroidN2 Ethernet Failure Pt2
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-556'>AR-556</a>] -         Adding vnstat and ZFS support to MOTD
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-558'>AR-558</a>] -         Switch mvebu current to K5.9
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-563'>AR-563</a>] -         Improve headers compilation
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-576'>AR-576</a>] -         Enabled debug on RockpiS
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-579'>AR-579</a>] -         Improve (oh-my)ZSH loading speed
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-587'>AR-587</a>] -         Fix kernel switching for rk3399 family
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-594'>AR-594</a>] -         Upgrade Meson64 u-boot to 2020.10
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-598'>AR-598</a>] -         Switch rockchip64 u-boot to 2020.10
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-601'>AR-601</a>] -         Move sunxi-current to 5.10.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-603'>AR-603</a>] -         Enable SPI boot option for roc-rk3399-pc
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-607'>AR-607</a>] -         Move Meson64 Current to 5.10.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-609'>AR-609</a>] -         Move Mvebu Current to 5.10.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-611'>AR-611</a>] -         Switch rockchip64-current to 5.10.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-614'>AR-614</a>] -         Upgrade ZFS packages
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-618'>AR-618</a>] -         Upgrade mvebu64 current to 5.10.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-619'>AR-619</a>] -         Bump rockchip current to 5.10.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-620'>AR-620</a>] -         Enable network link leds for NanoPi R4S by default
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-622'>AR-622</a>] -         Enable DMC for Station-M1 in current and dev
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-623'>AR-623</a>] -         Enable RTC (hym8563) for Station P1 in dev and current
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-624'>AR-624</a>] -         Provide an option to skip autodetection at first login
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-628'>AR-628</a>] -         Bump Meson64 u-boot to 2021.01
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-630'>AR-630</a>] -         Bump Odroid XU4 DEV to 5.10.y
</li>
</ul>
    


## v20.11.10 (2021-01-25)

<ul>
<li>All images rebuild due to torrent system corruption
</ul>

## v20.11.9 (2021-01-23)

<ul>
<li>Broken Nanopi Neo buster image rebuild, adding Station M1 and P1 legacy images, Odroid XU4 update
</ul>

## v20.11.8 (2021-01-17)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-614'>AR-614</a>] -         Upgrade ZFS on Focal and Buster (64bit only) to v2.0.1
</ul>

## v20.11.7 (2021-01-06)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-605'>AR-605</a>] -         Booting troubles on Odroid C4 / HC4
</li>
<li>all images were rebuilt - we had a few corrupted ones in previous build
</li>
</ul>

## v20.11.6 (2021-01-03)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-601'>AR-601</a>] -         Move sunxi-current to 5.10.y
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-235'>AR-235</a>] -         Implement Device Tree Editor in armbian-config
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-589'>AR-589</a>] -         Add armbian-zsh package
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-590'>AR-590</a>] -         ZRAM Enhancements - decouple swap config from tmp
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-554'>AR-554</a>] -         Fix Odroid N2 Ethernet Failure
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-556'>AR-556</a>] -         Adding vnstat and ZFS support to MOTD
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-579'>AR-579</a>] -         Improve (oh-my)ZSH loading speed
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-512'>AR-512</a>] -         Fix Ethernet for Opi3 and other devices with phymode for kernel 5.10
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-547'>AR-547</a>] -         First login: adding a non-existing keyboard variant
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-565'>AR-565</a>] -         Fix SATA on HC4 is not recognized
</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-595'>AR-595</a>] -         Fix Rockpi 4B 1GB not booting
</li>
</ul>

## v20.11.5 (2020-12-31)

<ul>
 <li>[<a href='https://armbian.atlassian.net/browse/AR-566'>AR-566</a>] - Add Nanopi R4S preview images</li>
</ul>

## v20.11.4 (2020-12-15)

<ul>
<li><a href=https://forum.armbian.com/topic/16476-eth1-25-vanished-upgrade-to-20113-5914-rockchip64/>Re-adding accidentally removed network driver on Helios64</a></li>
<li>added OpenHab 3 to the armbian-config software installer</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-587'>AR-587</a>] - Fix kernel switching for rk3399 family</li>
</ul>

## v20.11.3 (2020-12-12)

Bugfix release

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-559'>AR-559</a>] - First login script - not all locales have UTF8 encoding</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-163'>AR-163</a>] - Systematically cleanup distribution defaults</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-206'>AR-206</a>] - Improve memory performance on Renegade (roc-rk3328-cc) in current</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-472'>AR-472</a>] - Added support for Ubuntu 20.10 Groovy</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-476'>AR-476</a>] - Add sound to Odroid N2</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-485'>AR-485</a>] - Improve multicore compilation</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-487'>AR-487</a>] - Rework download pages</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-508'>AR-508</a>] - Add Odroid HC4</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-514'>AR-514</a>] - Download and verify not fully reliable</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-517'>AR-517</a>] - Mark Bionic builds host as deprecated</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-525'>AR-525</a>] - Bump Rockchip 32bit to 5.9.y</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-526'>AR-526</a>] - Move mvebu-dev kernel to 5.9+</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-546'>AR-546</a>] - Added Pine64 Pinecube</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-547'>AR-547</a>] - First login: adding a non-existing keyboard variant</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-548'>AR-548</a>] - mvebu DFS seems to cause system hang under high I/O</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-551'>AR-551</a>] - Update fan configuration, enable network LED and enable UPS timer</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-552'>AR-552</a>] - Re-enable UHS SDR104 mode for Helios64 and roc-rk3399-pc</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-553'>AR-553</a>] - Update builder to retrieve web seeds from mirrors api</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-556'>AR-556</a>] - Adding vnstat and ZFS support to MOTD</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-557'>AR-557</a>] - GCC compatibility issues</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-558'>AR-558</a>] - Switch mvebu current to K5.9</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-563'>AR-563</a>] - Improve headers compilation</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-565'>AR-565</a>] - SATA on HC4 is not recognized</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-568'>AR-568</a>] - Add Orangepizero 2 WIP target</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-570'>AR-570</a>] - Improper order in getty override.conf</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-571'>AR-571</a>] - Move Meson64 DEV to 5.10.y</li>
</ul>

## v20.11.1 (2020-12-04)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-551'>AR-551</a>] - Update fan configuration, enable network LED and enable UPS timer</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-565'>AR-565</a>] - SATA on HC4 is not recognized</li>
<li>Updated Odroid C4/HC4, Helios64, Rockpi 4* images and rockchip64 kernels</li>
</ul>	

## v20.11 (2020-11-24)

Finished projects

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-2">AR-2</a>] - Improving download infrastructure Phase 1</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-151">AR-151</a>] - Integrate JMCCs Multimedia script</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-230">AR-230</a>] - Decide what to do with TVboxes</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-412">AR-412</a>] - Update Odroid XU4 kernels</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-424">AR-424</a>] - Improve HTOP config</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-456">AR-456</a>] - Upgrading Allwinner u-boot to 2020.10</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-476">AR-476</a>] - Add sound to Odroid N2</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-485">AR-485</a>] - Improve multicore compilation</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-508">AR-508</a>] - Add Odroid HC4</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-509">AR-509</a>] - Upgrade meson64 to 5.9.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-510">AR-510</a>] - Move meson (Odroid C1) to 5.9.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-532">AR-532</a>] - Move Odroid C4 from legacy u-boot toward mainline</li>
</ul>

Solved bugs

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-314">AR-314</a>] - Links to SHA files at download pages are wrong</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-372">AR-372</a>] - Meson64 Reboot failure kernel 5.7</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-373">AR-373</a>] - Rock64 no HDMI (must be unplugged)</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-382">AR-382</a>] - Fix zram creation on bigger memory devices</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-391">AR-391</a>] - Warning a reboot is needed doesn't go away after reboot</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-407">AR-407</a>] - Bug in first login script</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-417">AR-417</a>] - HTOP in Bullseye needs higher package version</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-420">AR-420</a>] - GPIO SPI patch is failing on Rockchip64</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-422">AR-422</a>] - Improper version showing at upgrade</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-425">AR-425</a>] - Resize is finished but message doesn't disappear</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-428">AR-428</a>] - Firefox initial config has different location then ESR variant</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-436">AR-436</a>] - Rockpi S reports some error in postinst scripts</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-437">AR-437</a>] - MOTD cosmetic issue</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-439">AR-439</a>] - Automated rebuilds set image status to USER_BUILT</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-441">AR-441</a>] - Odroid C4 legacy bootscript problem</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-452">AR-452</a>] - Fix first boot locales selection and add desktop lang switching</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-459">AR-459</a>] - Missing package libreoffice-style-tango from Bullseye desktop</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-471">AR-471</a>] - Mitigate Git server failures</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-482">AR-482</a>] - Htop doesn't show CPU speed to normal user but shows properly to root</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-484">AR-484</a>] - Odroid C4 refuse to boot</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-491">AR-491</a>] - LEDs on Helios4 not working</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-493">AR-493</a>] - Patches are not creating</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-494">AR-494</a>] - Fix armbian-hardware-opitimization not being run</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-505">AR-505</a>] - armbian-hardware-optimization: eth0 tweak applied before it is appear on /proc/interrupts</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-527">AR-527</a>] - Rockchip 32bit sources were removed</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-528">AR-528</a>] - Improve creating images from repository</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-529">AR-529</a>] - Z28 PRO device tree doesn't exists in mainline</li>
</ul>

Closed tasks

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-284">AR-284</a>] - Discuss if there is a cleaner way to install Chromium</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-350">AR-350</a>] - Switch rock64 to mainline u-boot</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-351">AR-351</a>] - Switch rockpro64 to mainline u-boot</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-363">AR-363</a>] - Switch mvebu current to K5.8.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-380">AR-380</a>] - Revisit RTL8812AU driver</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-387">AR-387</a>] - Switch from rk3399-bluetooth service to btbcm for loading firmware/patchram in dev/current</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-388">AR-388</a>] - XU4 - Introduce new Mem freq scaling patch and re-enable</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-390">AR-390</a>] - Add Radxa Rockpi 4C</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-400">AR-400</a>] - Enable overlays in rockchip64-legacy</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-401">AR-401</a>] - Enable creation of SPI flash u-boot image for ROCK Pi 4</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-403">AR-403</a>] - Enable overlays in rk3399-legacy</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-404">AR-404</a>] - Switch renegade to mainline u-boot</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-409">AR-409</a>] - Move imx6 current kernels to 5.8.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-413">AR-413</a>] - Improve reliability of Helios64's eMMC module</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-415">AR-415</a>] - Improve reboot reliability for Helios64</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-416">AR-416</a>] - Move Rockchip 32bit to 5.8.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-419">AR-419</a>] - Add dedicated DT for Nanopi Neo3</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-445">AR-445</a>] - systemd-journal not rotated with armbian-ramlog</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-458">AR-458</a>] - Update board support statuses</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-461">AR-461</a>] - Add Armbian to Neofetch</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-462">AR-462</a>] - Adapt helios64 device tree name to match upstream Linux</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-464">AR-464</a>] - Move Libre Computer Renegade to mainline u-boot</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-472">AR-472</a>] - Added support for Ubuntu 20.10 Groovy</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-473">AR-473</a>] - Add interactive option to use precompiled packages from Armbian repository</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-477">AR-477</a>] - Advanced recovery options for rockchip64 boards</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-483">AR-483</a>] - Fix analog (3.5 jack) audio on ROCK Pi 4C</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-490">AR-490</a>] - Enable RTC on Odroid N2</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-495">AR-495</a>] - Allow building images with kernels 5.8.17+ and 5.9.2+</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-499">AR-499</a>] - Enable Watchdog for G12/Odroidn2</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-504">AR-504</a>] - Helios64: Switch fusb302 driver to mainline and enable DP over TypeC</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-511">AR-511</a>] - Switch rockchip64-current to linux 5.9.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-513">AR-513</a>] - Move Odroid XU4 kernels up</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-515">AR-515</a>] - Upgrade imx6 to 5.9.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-521">AR-521</a>] - Exchange mv with rsync</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-522">AR-522</a>] - Allow setting MTU for Rockchip64's dwmac interface</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-523">AR-523</a>] - enable CONFIG_TARGET_CORE for iSCSI target support</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-524">AR-524</a>] - Upgrade rockpis legacy kernel</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-531">AR-531</a>] - Check why disabling one update-initramfs breaks Ubuntu initrd making on update</li>
</ul>

## v20.08.22 (2020-11-8)

<ul>
<li>Added WIP images for Odroid HC4</li>
<li>Updated images for Odroid C4, N2, C2, Lafrite, Lepotato, KVIM1</li>
</ul>

## v20.08.13 (2020-10-19)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-363'>AR-363</a>] - Switch mvebu current to K5.8.y</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-466'>AR-466</a>] - Enable Recovery button on Helios64</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-416'>AR-416</a>] - Move Rockchip 32bit to 5.8.y</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-476'>AR-476</a>] - Add sound to Odroid N2</li>
<li>update all kernels</li>
<li>Rebuild images for Helios4, Helios64 and Odroid N2</li>
</ul>

## v20.08.11 (2020-10-16)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-465'>AR-465</a>] - Helios64 cannot boot from eMMC</li>
<li>enable Ubuntu 20.10 Groovy as a CSC build option (need build parameter EXPERT="yes")</li>
<li>update u-boot loader to 2020.10 on Allwinner platform</li>
<li>update all kernels</li>
<li>update images for Helios 64</li>
<li>add option to build images from prebuild packages from repository which drastically improves build time in case you don't need to rebuild kernel</li>
</ul>

## v20.08.8 (2020-10-05)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-463'>AR-463</a>] - Improve Helios64 Stability, updated images</li>
<li>Adapt Helios64 devicetree name to match upstream Linux</li>
</ul>

## v20.08.4 (2020-09-23)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-399'>AR-399</a>] - Improve Pinebook PRO support, updated images</li>
<li>Updated Helios64 images</li>
</ul>

## v20.08.3 (2020-09-21)

- updated mainline kernel based images to Linux 5.8.10
- all other kernels updated to respective latest version
- improved htop with showing network status dynamically, GPU temp, improved CPU speed display
- fixed usbip for sharing usb over network
- fixed Odroid C4 boot script bug; adding normal and higher CPU speeds
- added many improvements for Helios64
- enabled GPU temperatures in htop for XU4, meson64 (Odroid N2/N2+) and rockchip64/32
- fixed initial configuration for Firefox
- fixed tx offloading for Rockchip64 NIC’s
- move rockchip 32bit to 5.8.y (Tinkerboard / MiQi)
- improved RK3399 stability by mingling OPP
- fixed a bunch of bugs related to encrypted root filesystem
- enabled hardware watchdog support for mvebu64 / Espressobin
- cosmetic fixes to motd
- enabling I2S and spdif on Nanopi Neo3 by default
- fixes wrong memory calculation on ZRAM display
- fixing firstlogin bug preventing running xrdp 
- move Espressobin kernel to 5.8.y
- adjust / fix Kali Linux wifi injections patches

Known bugs:

- Some Rockpro64 boards have troubles with upgrade
- Bananapi M3 eMMC can’t boot from eMMC (solution is available)
- H6 stability issues on some boards
- RockpiS shows some error on upgrade but upgrade suceeds
- 4K and audio on mainline based meson64 boards

## v20.08 (2020-08-20)

Finished projects

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-45'>AR-45</a>] - Make first login more user friendly</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-71'>AR-71</a>] - Create a document: How we will use Jira</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-182'>AR-182</a>] - Unify / merge kernel configs</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-201'>AR-201</a>] - Introduce CI autotest facility</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-227'>AR-227</a>] - Move Espressobin current to K5.6</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-313'>AR-313</a>] - Ability to work in offline mode</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-320'>AR-320</a>] - Initial support for Rockpi E</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-324'>AR-324</a>] - Add Rockchip RK322X SoC support</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-328'>AR-328</a>] - Meson64 move current to 5.7.y</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-329'>AR-329</a>] - Switch sunxi dev target to kernel 5.7</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-331'>AR-331</a>] - Enable kernel boot splash as an option</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-335'>AR-335</a>] - Improve patch making</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-392'>AR-392</a>] - Add Odroid N2+</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-402'>AR-402</a>] - Add Helios64</li>
</ul>

Solved bugs

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-282">AR-282</a>] - Rockpi 4B 1Gb doesn't boot modern kernel / u-boot</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-295">AR-295</a>] - Odroid C2: no more USB devices after upgrade</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-298">AR-298</a>] - Missing default SElinux policy</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-303">AR-303</a>] - Create a download page for BPI M2 zero</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-305">AR-305</a>] - K-worker creates load on Allwinner devices</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-319">AR-319</a>] - Armbian config failed to switch kernels</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-330">AR-330</a>] - Shell check bugs</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-332">AR-332</a>] - When making all kernels - building sometimes fails</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-337">AR-337</a>] - Odroid XU4 Memcopy Slow on all Kernel 5.x 80MB/sec instead of 370+MB/sec</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-338">AR-338</a>] - Bananapi R2 does not boot at all</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-340">AR-340</a>] - Fix WiFi on Nanopi M4V2</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-348">AR-348</a>] - Confirm RK3399 TcpOffloading bug</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-352">AR-352</a>] - Fix Random MAC on H3 boards</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-354">AR-354</a>] - Support User Provided EDID Firmware</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-355">AR-355</a>] - backport Linux v5.8 fbtft/fb_st7789v invert colors, proper gamma</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-356">AR-356</a>] - Building multiple u-boot targets breaks</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-371">AR-371</a>] - CPU frequency scaling broken on H6</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-378">AR-378</a>] - Increase address room for initial ramdisk</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-381">AR-381</a>] - selinux-policy-default missing on Debian Bullseye</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-393">AR-393</a>] - Ask for setting locale at first run</li>
</ul>

Closed tasks

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-28">AR-28</a>] - Added new GCC compilers</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-225">AR-225</a>] - Introduce PACKAGE_LIST for BOARD and FAMILY</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-300">AR-300</a>] - Enable HDMI audio for OrangePi 4</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-317">AR-317</a>] - Move Odroid XU4 dev to mainline + patches</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-318">AR-318</a>] - Upgrade Odroid XU4 legacy kernel</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-321">AR-321</a>] - Upgrade Meson (C1) current to 5.7.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-323">AR-323</a>] - Allow install to SD NAND for Rockpi S</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-326">AR-326</a>] - Make USB3 support of ROCK Pi E on par with other rk3328 boards</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-327">AR-327</a>] - Bump imx6 current kernel to 5.7.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-333">AR-333</a>] - Update Odroid XU4 kernels</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-334">AR-334</a>] - Cleanup boot environment files</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-336">AR-336</a>] - Add support for cheap 2.5GB USB network dongles</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-341">AR-341</a>] - Follow-up N2 CPU Affinity</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-349">AR-349</a>] - Update mainline u-boot to v2020.07 for rockchip64 and rk3399</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-357">AR-357</a>] - IRQ affinity improvements for G12B</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-358">AR-358</a>] - Added initial support for Neo 3</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-361">AR-361</a>] - Update Odroid XU4 boot.ini</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-362">AR-362</a>] - HDMI sound support for Allwinner A10, A20, A31</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-364">AR-364</a>] - Change sunxi legacy to 5.4.y, current to 5.7.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-366">AR-366</a>] - Move rockchip/64 current to 5.7.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-383">AR-383</a>] - Upgrades for Tapatalk plugin</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-389">AR-389</a>] - Add PACKAGE_LIST_BOARD_REMOVE option</li>
</ul>

## v20.05.7 (2020-07-02)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-308'>AR-308</a>] - Disable HDMI in u-boot for rk3399 boards</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-338'>AR-338</a>] - Bananapi R2 does not boot at all</li> 
<li>[<a href='https://armbian.atlassian.net/browse/AR-337'>AR-337</a>] - Odroid XU4 Memcopy Slow on all Kernel 5.x 80MB/sec instead of 370+MB/sec</li>
<li>Update images for: NanoPC T4, Nanopi M4,Nanopi M4v2, Nanopi Neo4, Orangepi 4, Firefly RK3399, Bananapi R2, Odroid XU4</li>
</ul>

## v20.05.6 (2020-06-19)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-324'>AR-324</a>] - Add Rockchip RK322X SoC support</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-320'>AR-320</a>] - Initial support for Rockpi E</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-323'>AR-323</a>] - Allow install to SD NAND for Rockpi S</li>
</ul>

## v20.05.5

never released/skipped

## v20.05.4 (2020-06-16)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-311'>AR-311</a>] - Initrd on Focal can get corrupted followup fix</li>
</ul>

## v20.05.3 (2020-06-10)

<ul>
<li>[<a href='https://armbian.atlassian.net/browse/AR-300'>AR-300</a>] - Enable HDMI audio for OrangePi 4</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-305'>AR-305</a>] - K-worker creates load on Allwinner devices</li>
<li>[<a href='https://armbian.atlassian.net/browse/AR-282'>AR-282</a>] - Rockpi 4B 1Gb doesn&#39;t boot modern kernel / u-boot</li>
</ul>

## v20.05.2 (2020-06-05)

- [<a href="https://armbian.atlassian.net/browse/AR-294">AR-294</a>] - Initrd on Focal can get corrupted</li>

## v20.05.1 (2020-05-31)

Kagu

Finished projects

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-108">AR-108</a>] - Upgrade remaining kernels to 5.4.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-158">AR-158</a>] - Update 3rd party wireless drivers</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-159">AR-159</a>] - Switch fake-hwclock to hardware RTC on mvebu family</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-168">AR-168</a>] - Add NanoPi R2S board support</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-180">AR-180</a>] - Update Wireguard drivers on kernels below 5.4.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-184">AR-184</a>] - Improve slow booting on Rockchip RK3399 devices</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-185">AR-185</a>] - Change download images compression format</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-190">AR-190</a>] - Update wireless driver for RTL88x2BU</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-196">AR-196</a>] - Upgrade u-boot to 2020.04 where possible</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-201">AR-201</a>] - Introduce CI autotest facility</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-207">AR-207</a>] - Merge rockpis-dev into rockchip64</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-208">AR-208</a>] - Consolidate u-boot variants for mvebu family</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-210">AR-210</a>] - Add support for more HDMI resolutions on Rockchip RK3288 devices</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-215">AR-215</a>] - Move meson64 dev branch to 5.6.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-221">AR-221</a>] - Upgrade imx6 current to 5.6.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-222">AR-222</a>] - Port Docker image building to Ubuntu 20.04</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-226">AR-226</a>] - Add Hardkernel Odroid C4 mainline u-boot / kernel</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-236">AR-236</a>] - Attach Meson64 CURRENT to 5.6.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-238">AR-238</a>] - Updating hostapd, PSD and theme package in repository</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-247">AR-247</a>] - Revitalise Udoo board</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-250">AR-250</a>] - Improve usage of external patches</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-253">AR-253</a>] - Add prerm script for headers</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-254">AR-254</a>] - Add Banana Pi M2 Zero</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-257">AR-257</a>] - Bring Odroid C1 back from the EOL with latest upstream kernel</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-260">AR-260</a>] - Add Nanopi A64 board support</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-261">AR-261</a>] - Add Rockpi S mainline board support</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-262">AR-262</a>] - Move Allwinner development branch to 5.6.y</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-278">AR-278</a>] - Add snap free Chromium to Ubuntu Focal</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-279">AR-279</a>] - Add Hardkernel Odroid C4 stock kernel</li>
</ul>

Solved bugs
 
<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-109">AR-109</a>] - Upgrade is not done properly on some boards</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-165">AR-165</a>] - Instability with Rock64 and Rock PRO</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-177">AR-177</a>] - No serial gadget console on Nanopi Neo2 black</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-181">AR-181</a>] - Odroid N2 crashes during USB rsync backups</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-198">AR-198</a>] - Olimex Lime 2 doesn't boot from eMMC</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-204">AR-204</a>] - CPUfreq defaults missing on update</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-205">AR-205</a>] - No sound output with OrangePi 4 in dev and current</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-211">AR-211</a>] - Chrony fails to start on Ubuntu Focal</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-212">AR-212</a>] - Random MAC on Nanopi R2S</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-220">AR-220</a>] - Disable 3D support in Bionic due to broken mesa packages</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-231">AR-231</a>] - Unstable stmmac network driver on Meson64</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-237">AR-237</a>] - Desktop install on Ubuntu Focal installs Gnome3 desktop</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-239">AR-239</a>] - Chrony fails to start on Focal</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-240">AR-240</a>] - Broken VFAT kernel upgrade</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-244">AR-244</a>] - Thermal throttling on H5 doesn't work properly</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-245">AR-245</a>] - Hostapd doesn't go up</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-248">AR-248</a>] - Odroid C4 CPU speed is limited to 1.5Ghz</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-249">AR-249</a>] - Problems with CI testings</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-251">AR-251</a>] - Fix kernel 5.7.y packages patch</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-255">AR-255</a>] - Fix Debian mirrors URL</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-263">AR-263</a>] - Fix audio on Renegade</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-269">AR-269</a>] - Add correct CPU regulator configuration for the NanoPI R1</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-274">AR-274</a>] - Add missing iozone3 package to the minimal image</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-277">AR-277</a>] - Distinguish nightly and stable images at the download pages</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-286">AR-286</a>] - Armbian-resize-filesystem fails on first run due to missing fdisk in Bullseye</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-287">AR-287</a>] - Make sure cryptsetup-initramfs is installed in any case</li>
</ul>

Closed tasks

<ul>
<li>[<a href="https://armbian.atlassian.net/browse/AR-150">AR-150</a>] - Disable Stretch image creation for Helios4 and Clearfog</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-157">AR-157</a>] - Add Ubuntu Focal 20.04 as a supported build host</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-186">AR-186</a>] - Blacklist 3D engine on headless images</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-189">AR-189</a>] - Move wireless driver for 8189ES from patch to git</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-195">AR-195</a>] - Adding Ubuntu 20.04 to all builds</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-209">AR-209</a>] - Disable CONFIG_VIDEO_DE2 in u-boot for Allwinner devices</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-213">AR-213</a>] - Make manual for .xz images and check their authentication</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-228">AR-228</a>] - Enable audio and USB on Nanopi A64</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-229">AR-229</a>] - Bump with AUFS for DEV kernels</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-232">AR-232</a>] - Switch Odroid XU4 DEV branch to Libreelec branch</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-234">AR-234</a>] - Disable ZSH update prompt on every two weeks</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-242">AR-242</a>] - Enable SELinux</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-252">AR-252</a>] - Improve source code cleaning</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-258">AR-258</a>] - Enables PCIE PHY with Mezzanine NVME</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-259">AR-259</a>] - Add mp8859 regulator to current for RK3399-ROC-PC</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-264">AR-264</a>] - Enable RTL8723DS WiFI driver</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-265">AR-265</a>] - Remove Xenial from supported host OS</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-266">AR-266</a>] - Fix dependency for native building on Linux Mint and Debian Buster</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-267">AR-267</a>] - Enable Cedrus video acceleration on Allwinner kernels</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-268">AR-268</a>] - Add higher clock for Allwinner H6</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-270">AR-270</a>] - Add support for alternate console UARTs in Allwinner H3 u-boot</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-271">AR-271</a>] - Lower DDR clock rate to 504MHz for H5 boards</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-280">AR-280</a>] - Update CONF, CSC and WIP statuses according to support level</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-285">AR-285</a>] - Improve thermal throttling on Allwinner H6</li>
<li>[<a href="https://armbian.atlassian.net/browse/AR-288">AR-288</a>] - Add vendor name to the board config files</li>
</ul>

## v20.02.12 (2020-04-27)

- Added preview images for Odroid C4

## v20.02.8 (2020-03-26)

- update kernels with upstream versions, synchronise and test kernel sources download

## v20.02.7 (2020-03-26)

- Updated images for Rockpi S, Odroid XU4 and FriendlyARM Nanopc T3, T3+, M3, Fire3

## v20.02.6 (2020-03-23)

- Updated images for Rockpi S and Orangepi 4
- Updated armbian-config (fixed OMV installer)

## v20.02.5 (2020-03-19)

- Updated images for Orangepi 4, Bananapi and Rockpi S

## v20.02.4 (2020-03-18)

- Added images for Nanopi R2S and Bananapi M2 Zero
- Kernel update for Odroud XU4

## v20.02.3 (2020-02-21)

- Updating images for Le potato, Khadas Vim1,La Frite, Nanopik2 S905, Odroid N2/C2 - fixing audio
- Updating images for Orangepi 4 - boot loader problem

## v20.02.2 (2020-02-18)

Chiru

Tasks

- [<a href='https://armbian.atlassian.net/browse/AR-46'>AR-46</a>] - Support for single function run
- [<a href='https://armbian.atlassian.net/browse/AR-47'>AR-47</a>] - Adding Docker shell support
- [<a href='https://armbian.atlassian.net/browse/AR-49'>AR-49</a>] - Move sunxi kernel to 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-79'>AR-79</a>] - Check and adjust AUFS patch for 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-80'>AR-80</a>] - Move imx6 to 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-81'>AR-81</a>] - Enable Meson64 DEV at 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-82'>AR-82</a>] - Move Mvebu64 / Espressobin dev kernel to 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-84'>AR-84</a>] - Move rockchip64 current to 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-85'>AR-85</a>] - Adjusted Sunvell R69
- [<a href='https://armbian.atlassian.net/browse/AR-90'>AR-90</a>] - Add support for Nanopi M4 v2
- [<a href='https://armbian.atlassian.net/browse/AR-92'>AR-92</a>] - Enable stable MAC address from cpuid on rk3399
- [<a href='https://armbian.atlassian.net/browse/AR-96'>AR-96</a>] - Update Xradio wireless driver
- [<a href='https://armbian.atlassian.net/browse/AR-97'>AR-97</a>] - Tag supported builds properly at download pages
- [<a href='https://armbian.atlassian.net/browse/AR-98'>AR-98</a>] - Enable missing Kuberenetes kernel dependency
- [<a href='https://armbian.atlassian.net/browse/AR-100'>AR-100</a>] - Add Debian Bullseye and Ubuntu Focal 
- [<a href='https://armbian.atlassian.net/browse/AR-112'>AR-112</a>] - Enabled internal WLAN on RockPi S
- [<a href='https://armbian.atlassian.net/browse/AR-113'>AR-113</a>] - Install wireguard tools only when selected
- [<a href='https://armbian.atlassian.net/browse/AR-114'>AR-114</a>] - Enable audio codec on Orangepi Win
- [<a href='https://armbian.atlassian.net/browse/AR-115'>AR-115</a>] - Add drivers for Realtek RTL8811CU and RTL8821C chipsets
- [<a href='https://armbian.atlassian.net/browse/AR-116'>AR-116</a>] - Remove annoying debug message filling logs on 8189es
- [<a href='https://armbian.atlassian.net/browse/AR-117'>AR-117</a>] - Add Pine H64 model B
- [<a href='https://armbian.atlassian.net/browse/AR-124'>AR-124</a>] - Enable wireless on Rockpi-S
- [<a href='https://armbian.atlassian.net/browse/AR-127'>AR-127</a>] - Refactoring wifi patches
- [<a href='https://armbian.atlassian.net/browse/AR-128'>AR-128</a>] - Adding WIP support for Pinebook PRO
- [<a href='https://armbian.atlassian.net/browse/AR-129'>AR-129</a>] - Move NanopiM4 V2 and Pine H64 under supported
- [<a href='https://armbian.atlassian.net/browse/AR-134'>AR-134</a>] - Update AUFS version on Odroid XU4 and Nanopi Fire3/T3/T3+
- [<a href='https://armbian.atlassian.net/browse/AR-138'>AR-138</a>] - Update RK3399 legacy kernel (Nanopi M4, T4, Neo4) to latest upstream version
- [<a href='https://armbian.atlassian.net/browse/AR-139'>AR-139</a>] - Nanpi R1 - move primary serial console to ttyS1 which is on the chassis
- [<a href='https://armbian.atlassian.net/browse/AR-143'>AR-143</a>] - Create OpenHab installation instructions for their official documentation
- [<a href='https://armbian.atlassian.net/browse/AR-146'>AR-146</a>] - Update rockchip-legacy to most recent upstream kernel version
- [<a href='https://armbian.atlassian.net/browse/AR-147'>AR-147</a>] - Enable analogue audio on Allwinner H6
- [<a href='https://armbian.atlassian.net/browse/AR-148'>AR-148</a>] - [ mvebu-current ] Fix cpufreq (dynamic frequency scaling)
- [<a href='https://armbian.atlassian.net/browse/AR-149'>AR-149</a>] - [ mvebu-current ] Fix pcie issues 
- [<a href='https://armbian.atlassian.net/browse/AR-153'>AR-153</a>] - Enable USB3 for Rock64/Renegade with RK3328 on mainline kernel
- [<a href='https://armbian.atlassian.net/browse/AR-154'>AR-154</a>] - Add analogue audio driver to Allwinner H6
- [<a href='https://armbian.atlassian.net/browse/AR-155'>AR-155</a>] - Enable Cedrus video acceleration support on Allwinner boards
- [<a href='https://armbian.atlassian.net/browse/AR-167'>AR-167</a>] - Add upstream patches for Odroid XU4
- [<a href='https://armbian.atlassian.net/browse/AR-172'>AR-172</a>] - USB3 Support for Rockchip
           
Bugs

- [<a href='https://armbian.atlassian.net/browse/AR-74'>AR-74</a>] - User patches directories not created
- [<a href='https://armbian.atlassian.net/browse/AR-76'>AR-76</a>] - Rockchip64 missing CPU_MIN variable
- [<a href='https://armbian.atlassian.net/browse/AR-77'>AR-77</a>] - Wrong board name variable for Orangepi RK 3399
- [<a href='https://armbian.atlassian.net/browse/AR-83'>AR-83</a>] - Packaging patch broken for kernel 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-86'>AR-86</a>] - CPU freq scaling for H6 doesn&#39;t work in K5.4
- [<a href='https://armbian.atlassian.net/browse/AR-88'>AR-88</a>] - Banana Pi M3 does not boot
- [<a href='https://armbian.atlassian.net/browse/AR-89'>AR-89</a>] - Tinkerboard S doesn&#39;t start from eMMC
- [<a href='https://armbian.atlassian.net/browse/AR-91'>AR-91</a>] - Broken Allwinner overlays
- [<a href='https://armbian.atlassian.net/browse/AR-94'>AR-94</a>] - Espressobin v7 with 2gb of ram fail to boot
- [<a href='https://armbian.atlassian.net/browse/AR-102'>AR-102</a>] - Missing packaging patch for Rockpis legacy kernel
- [<a href='https://armbian.atlassian.net/browse/AR-103'>AR-103</a>] - PPA way of adding sources are failing on Ubuntu
- [<a href='https://armbian.atlassian.net/browse/AR-104'>AR-104</a>] - 32bit rust compiler doesn&#39;t run new kernels
- [<a href='https://armbian.atlassian.net/browse/AR-105'>AR-105</a>] - Orangepi Zero Plus 2 doesn&#39;t boot
- [<a href='https://armbian.atlassian.net/browse/AR-106'>AR-106</a>] - Wireguard breaks building on 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-107'>AR-107</a>] - Improve compiler and rootfs download process
- [<a href='https://armbian.atlassian.net/browse/AR-110'>AR-110</a>] - Missing Bionic image for Nanopi Neo Plus2
- [<a href='https://armbian.atlassian.net/browse/AR-111'>AR-111</a>] - Some versions of Orangepi Win does not boot modern kernel
- [<a href='https://armbian.atlassian.net/browse/AR-118'>AR-118</a>] - NanoPi M4V2 ethernet partialy broken in one side
- [<a href='https://armbian.atlassian.net/browse/AR-123'>AR-123</a>] - OpenHAB2 installation is failing
- [<a href='https://armbian.atlassian.net/browse/AR-125'>AR-125</a>] - Wireless driver for 8188EUS breaks on K4.14
- [<a href='https://armbian.atlassian.net/browse/AR-126'>AR-126</a>] - Nanopi M3/Fire3/PC3 compilation breaks
- [<a href='https://armbian.atlassian.net/browse/AR-130'>AR-130</a>] - Instability with various A64 boards
- [<a href='https://armbian.atlassian.net/browse/AR-131'>AR-131</a>] - Add support for 3rd version of Pinebook A64 panel
- [<a href='https://armbian.atlassian.net/browse/AR-133'>AR-133</a>] - Odroid XU4 legacy kernel images instability
- [<a href='https://armbian.atlassian.net/browse/AR-141'>AR-141</a>] - Odroid XU4 current with kernel 5.4.y seems unstable
- [<a href='https://armbian.atlassian.net/browse/AR-142'>AR-142</a>] - Cryptsetup disk encryption build feature broken
- [<a href='https://armbian.atlassian.net/browse/AR-144'>AR-144</a>] - Tinkerboard break booting
- [<a href='https://armbian.atlassian.net/browse/AR-145'>AR-145</a>] - Missing HDMI audio on H3 boards
- [<a href='https://armbian.atlassian.net/browse/AR-152'>AR-152</a>] - Display issues with Bionic Mesa update
- [<a href='https://armbian.atlassian.net/browse/AR-164'>AR-164</a>] - Htop package does not build in qemu under Ubuntu Focal 20.04
- [<a href='https://armbian.atlassian.net/browse/AR-166'>AR-166</a>] - Rootfs cache number creates a window of 12h when users are forced to rebuild cache
- [<a href='https://armbian.atlassian.net/browse/AR-170'>AR-170</a>] - Wireless not connecting for SBCs
- [<a href='https://armbian.atlassian.net/browse/AR-171'>AR-171</a>] - Fix broken loading process on MiQi
- [<a href='https://armbian.atlassian.net/browse/AR-173'>AR-173</a>] - Fix makefile of kernel headers 4.4.210 for rk3399
- [<a href='https://armbian.atlassian.net/browse/AR-174'>AR-174</a>] - Teres Keyboard Not Working

Stories

- [<a href='https://armbian.atlassian.net/browse/AR-48'>AR-48</a>] - Bump u-boot to 2020.01 on RK3399 boards
- [<a href='https://armbian.atlassian.net/browse/AR-156'>AR-156</a>] - WIP orangepi 4 preliminary support

## v19.11.3 (2019-11-20)

Tasks

- [<a href='https://armbian.atlassian.net/browse/AR-1'>AR-1</a>] - Adding support category for distributions
- [<a href='https://armbian.atlassian.net/browse/AR-4'>AR-4</a>] - Remove Allwinner legacy
- [<a href='https://armbian.atlassian.net/browse/AR-5'>AR-5</a>] - Drop Udoo family and move Udoo board into newly created imx6 family
- [<a href='https://armbian.atlassian.net/browse/AR-9'>AR-9</a>] - Rename sunxi-next to sunxi-legacy
- [<a href='https://armbian.atlassian.net/browse/AR-10'>AR-10</a>] - Rename sunxi-dev to sunxi-current
- [<a href='https://armbian.atlassian.net/browse/AR-11'>AR-11</a>] - Adding Radxa Rockpi S support
- [<a href='https://armbian.atlassian.net/browse/AR-13'>AR-13</a>] - Rename rockchip64-default to rockchip64-legacy
- [<a href='https://armbian.atlassian.net/browse/AR-14'>AR-14</a>] - Add rockchip64-current as mainline source
- [<a href='https://armbian.atlassian.net/browse/AR-15'>AR-15</a>] - Drop Rockchip 4.19.y NEXT, current become 5.3.y
- [<a href='https://armbian.atlassian.net/browse/AR-16'>AR-16</a>] - Rename RK3399 default to legacy
- [<a href='https://armbian.atlassian.net/browse/AR-17'>AR-17</a>] - Rename Odroid XU4 next and default to legacy 4.14.y, add DEV 5.4.y
- [<a href='https://armbian.atlassian.net/browse/AR-18'>AR-18</a>] - Add Odroid N2 current mainline
- [<a href='https://armbian.atlassian.net/browse/AR-19'>AR-19</a>] - Move Odroid C1 to meson family
- [<a href='https://armbian.atlassian.net/browse/AR-20'>AR-20</a>] - Rename mvebu64-default to mvebu64-legacy
- [<a href='https://armbian.atlassian.net/browse/AR-21'>AR-21</a>] - Rename mvebu-default to mvebu-legacy
- [<a href='https://armbian.atlassian.net/browse/AR-22'>AR-22</a>] - Rename mvebu-next to mvebu-current
- [<a href='https://armbian.atlassian.net/browse/AR-23'>AR-23</a>] - Drop meson64 default and next, current becomes former DEV 5.3.y
- [<a href='https://armbian.atlassian.net/browse/AR-24'>AR-24</a>] - Drop cubox family and move Cubox/Hummingboard boards under imx6
- [<a href='https://armbian.atlassian.net/browse/AR-26'>AR-26</a>] - Adjust motd
- [<a href='https://armbian.atlassian.net/browse/AR-27'>AR-27</a>] - Enabling distribution release status
- [<a href='https://armbian.atlassian.net/browse/AR-28'>AR-28</a>] - Added new GCC compilers
- [<a href='https://armbian.atlassian.net/browse/AR-29'>AR-29</a>] - Implementing Ubuntu Eoan
- [<a href='https://armbian.atlassian.net/browse/AR-30'>AR-30</a>] - Add desktop packages per board or family
- [<a href='https://armbian.atlassian.net/browse/AR-31'>AR-31</a>] - Remove (Ubuntu/Debian) distribution name from image filename
- [<a href='https://armbian.atlassian.net/browse/AR-32'>AR-32</a>] - Move arch configs from configuration.sh to separate arm64 and armhf config files
- [<a href='https://armbian.atlassian.net/browse/AR-33'>AR-33</a>] - Revision numbers for beta builds changed to day_in_the_year
- [<a href='https://armbian.atlassian.net/browse/AR-34'>AR-34</a>] - Patches support linked patches
- [<a href='https://armbian.atlassian.net/browse/AR-35'>AR-35</a>] - Break meson64 family into gxbb and gxl 
- [<a href='https://armbian.atlassian.net/browse/AR-36'>AR-36</a>] - Add Nanopineo2 Black
- [<a href='https://armbian.atlassian.net/browse/AR-38'>AR-38</a>] - Upgrade option from old branches to new one via armbian-config
- [<a href='https://armbian.atlassian.net/browse/AR-41'>AR-41</a>] - Show full timezone info
- [<a href='https://armbian.atlassian.net/browse/AR-43'>AR-43</a>] - Merge Odroid N2 to meson64
- [<a href='https://armbian.atlassian.net/browse/AR-44'>AR-44</a>] - Enable FORCE_BOOTSCRIPT_UPDATE for all builds
- [<a href='https://armbian.atlassian.net/browse/AR-57'>AR-57</a>] - New kernel feature requested CONFIG_BLK_DEV_DRBD
- [<a href='https://armbian.atlassian.net/browse/AR-60'>AR-60</a>] - Modified logrotate.service
- [<a href='https://armbian.atlassian.net/browse/AR-63'>AR-63</a>] - Docker maintenance features

Bugs

- [<a href='https://armbian.atlassian.net/browse/AR-25'>AR-25</a>] - Armbian resize stopped working in Ubuntu 19.10 or higher
- [<a href='https://armbian.atlassian.net/browse/AR-40'>AR-40</a>] - When changing console layout it does not change
- [<a href='https://armbian.atlassian.net/browse/AR-51'>AR-51</a>] - Prevent configuring locale
- [<a href='https://armbian.atlassian.net/browse/AR-52'>AR-52</a>] - Broken desktop install
- [<a href='https://armbian.atlassian.net/browse/AR-54'>AR-54</a>] - Upstream package name changed
- [<a href='https://armbian.atlassian.net/browse/AR-55'>AR-55</a>] - Wireless driver remove patch for Odroid XU4 broke down
- [<a href='https://armbian.atlassian.net/browse/AR-56'>AR-56</a>] - Missing CPU regulator
- [<a href='https://armbian.atlassian.net/browse/AR-58'>AR-58</a>] - Troubles with wireless on Nanopi DUO &amp; Opi Zero
- [<a href='https://armbian.atlassian.net/browse/AR-59'>AR-59</a>] - Compressed files are getting back to /var/log
- [<a href='https://armbian.atlassian.net/browse/AR-62'>AR-62</a>] - No HDMI sound on various meson64 boards
- [<a href='https://armbian.atlassian.net/browse/AR-64'>AR-64</a>] - Docker require root
- [<a href='https://armbian.atlassian.net/browse/AR-68'>AR-68</a>] - Broken Ethernet on Pine64+
     
Stories

- [<a href='https://armbian.atlassian.net/browse/AR-61'>AR-61</a>] - Adding support for LOCAL_MIRROR
- [<a href='https://armbian.atlassian.net/browse/AR-65'>AR-65</a>] - Moving configs under userpatches
- [<a href='https://armbian.atlassian.net/browse/AR-66'>AR-66</a>] - Enable build system torrent download by default
- [<a href='https://armbian.atlassian.net/browse/AR-67'>AR-67</a>] - Install Docker when we want to build under Docker
- [<a href='https://armbian.atlassian.net/browse/AR-69'>AR-69</a>] - Use kernel command line instead of a patch
- [<a href='https://armbian.atlassian.net/browse/AR-70'>AR-70</a>] - Enable Lima kernel driver on meson64
- [<a href='https://armbian.atlassian.net/browse/AR-73'>AR-73</a>] - Enable PCI on Rockpi 4 and overlay for GEN2 speed    

## v5.98 (2019-10-09)

- changed ntptime with chrony
- fixed serial console on several hosts
- added FriendlyARM ZeroPi
- enabled gadgets on rockchip64
- bumped RK3399 boards to latest kernel, recreate images and repository
- merged odroidxu4 down to default since we only have one kernel
- fixed Cubox images, move them to stock kernel
- fixed low Synaptic search speed

Build script:

- script configurations were migrated to userpatches
- added option to create minimal images with around 500Mb in size BUILD_MINIMAL="yes"
- added initial support of MCIMX7SABRE board (CSC)
- updates for xt-q8l-v10 (CSC)
- vagrant-disksize is beeing determined automatically
- Docker is installed automatically if one want use it (Debian based build host only)
- refactor build all images scripting that images can be build in full parallel mode
- added one file for storing which combinations shell be made for each board
- replaced Etcher with dd + verify for directly burning images when done
- cleaned initial config and remove confusing advanced options out

## v5.92 (2019-08-02)

- updated sunxi NEXT (4.19.63) and DEV (5.2.5) kernels
- updated htop application to show cpu speed and temperature (buster / disco)

## v5.91 (2019-07-31)

- created new images for Helios4 and Clearfog Pro/Base
- moved mvebu DEFAULT, NEXT and DEV branch to next kernel (LTS) and U-boot version
- fixed armada_thermal sensor reading, adjusted Helios4 fancontrol configuration
- fixed ODT on data signals of DDR RAM for Armada A388 SOMs
- recreated Armbian Buster images due to a bug in Network manager which in some cases failed to initiate network connection

Armbian-config:

- added Emby installation
- updated Plex install to use official repo
- added netmask-to-CIDR function for manual IP configuration

## v5.90 (2019-07-07)

- added Armbian Buster images for all boards
- added [Macchiatobin Doubleshot](https://www.armbian.com/macchiatobin-double-shot/) CSS target and images
- added images with test kernel v5.1.y for: Orangepi3, Lite2, One+, PineH64, Odroid C1, Teres, Pinebook
- added wireless [drivers for 88x2bu](https://forum.armbian.com/topic/10549-rtl88x2bu-support-in-armbian/)
- added eMMC support for Nanopi K2 (booting from doesn't work yet)
- added dual w1 overlay for meson64 family
- updated wireless [drivers for Realtek 8811, 8812, 8814 and 8821](https://github.com/aircrack-ng/rtl8812au)
- updated wireless [drivers for rtl8188eus & rtl8188eu & rtl8188etv](https://github.com/aircrack-ng/rtl8188eus)
- added latest [Wireguard driver](https://www.wireguard.com/)
- enable eMMC on Orangepi Win Plus
- enable Bluetooth on Tinkerboard, Nanopi4, Rockpi 4 CLI images
- improved ALSA config on Tinkerboard
- fixed Bluetooth on Nanopi M4/Neo4/T4 and Rockpi4
- fixed wireless drivers on OPi3 & Lite2
- fixed temperature readout on Allwinner H5 boards
- fixed SPI related bug on Allwinner 5.1.y kernel
- fixed HDMI output and bump kernel to 5.1.y on imx6 boards
- fixed eMMC install, add rootdev= to armbianEnv if missing
- fixed A10/A20 [SATA write speed](https://twitter.com/armbian/status/1127638533630459904)
- set default build target from Debian Stretch to Buster for all boards
- changed CPU clock back to 1.5/1.8Ghz defaults on boards with RK3399 to minimise thermal throttling
- changed motd console welcome text to: "Welcome to Debian Stretch with Armbian Linux 5.1.6-sunxi"
- changed display manager to lightdm by default and remove nodm completely
- changed u-boot for A64 to upstream sources
- changed RK3399 to U-boot 2019.04
- added URL to the build script and commit hash to /etc/armbian-release file
- added synaptic package manager and on-board keyboard to the desktop base
- added "logout" to the panel/menu
- added normal users to additional groups: disk tty users games
- updated all kernels with upstream
- updated ATF and bootloader on Espressobin, supporting all versions

Build script:

- added mirrors for speed-up building in China mainland
- added support for download compilers and rootfs cache via torrent network
- added new output image compression option (xz)
- enabled Debian Buster and Ubuntu Disco (unsupported) targets
- few Docker building improvements, caching image
- replace curl with aria2
- Linaro compilers update to 2019.02

Armbian-config:

- added Gimp installation
- added enable/disable Avahi
- updated OMV installer, OMV5 preparations
- enable screen resolution changer for Odroid N2
- enable CPU speed and governor adjustment

## v5.87 (2019-05-26)

- added support for [Odroid N2](https://www.armbian.com/odroid-n2/), [Nanopi R1](https://www.armbian.com/nanopi-r1/), [Nanopi Duo2](https://www.armbian.com/nanopi-duo-2/)
- enabled nightly images for Orangepi3, One+, Lite2, PineH64, Rock64pro, RockPi4b
- enabled nigtly Buster and Disco images for Le Potato
- recompiled all images and pushed update where updates are known to work (sunxi, sunxi64, meson64, ...)
- improved SATA write speed on [A20 chips for up to 300%](https://forum.armbian.com/topic/10352-a20-sata-write-speed-improvement/)
- fixed thermal throtling for H5 devices
- mainline u-boot moved 2019.04
- most development kernels moved to 5.1.y
- added separate DT for espressobinv7, updated boot loader
- enable WoL for eth0 on Helios4

Build script:

- added Debian Buster and Ubuntu Disco (WIP)
- improved building under Docker. Source code is not copied to docker image, caching image
- Linaro compilers update to 2019.02
- fixed incomplete cleaning of the source code

Armbian-config:

- fixed kernel changing
- fixed sources download
- fixed Hass.IO and TVheadend install
- added menu driven CPU frequency/governor adjustement
- improved two-factor authentication
- added meson64 and rockchip to overlay/hardware configuration
- improved hostapd management

Infrastructure:

- main download server has been hooked to 10GbE connection.
- added [web/http seeds](https://forum.armbian.com/topic/4198-seed-our-torrents) to torrent download. Torrent download could/should fully utilize your download capacity.
- major forum upgrade ([v4.4.3](https://invisioncommunity.com/release-notes/))
- added another IPV6 capable EU mirror https://mirrors.dotsrc.org

## v5.76 (2019-02-11)

- remove Exagear Desktop

## v5.75 (2019-02-10)

- added updated driver for Realtek 8811, 8812, 8814 and 8821 chipsets
- added Wireguard support to remaining kernels (except lower than 3.10)
- images rebuild with latest upstream sources, mainline u-boot was bumped to 2018.11

## v5.74 (2019-01-31)

- fixing systemd related [bug found](https://forum.armbian.com/topic/9289-ssh-not-working-after-upgrade-orange-pi-lite-armbian_ubuntu_xenial/) in sunxi legacy 3.4.y kernels

## v5.73 (2019-01-29)

- much faster nand-sata-install operations. Thanks to @dedalodaelus
- added support for @wireguard on all kernels higher than 3.10.y
- fixed drivers for popular DVB tuner S960 (all kernels)
- fixed bug in wireless drivers on Cubietruck, BananpiPRO, Bananapi+
- fixed AP mode on Orangepi PC+, Prime, One, .. when using kernel 4.19.y
- added prolific USB-to-USB bridges in mvebu-next/dev
- added nftables masquerade in mvebu64-next
- added MD raid support for SUNXI64
- upgrade bugfix for Helios4
- updated hostapd to 2.7
- fixed 1512MHz OPP on Renegade
- fixed DRM crashing for rockchip64
- mainline u-boot bumped to 2018.11 (update goes manually from nand-sata-install utility)
- added testing images for Orangepi RK3399 and Radxa Rockpi 4B

## v5.72 (2019-01-16)

- added additional repository mirror (updated armbian-config)
- [fixed Tinkerboard DTB](https://forum.armbian.com/topic/9312-tinkerboard-ss-bricked-after-570-upgrade/?tab=comments#comment-69964) in repository and images rebuild

## v5.71 (2019-01-16)

- updated images for Odroid C2, Lepotato and Nanopik2-S905 due to [this bug](https://github.com/armbian/build/commit/01571c0a4c6c3e7cdb1fec8c99465d8fc00c8c90)

## v5.70 (2019-01-12)

- sunxi-next and sunxi64-next were moved from 4.14.y to 4.19.y (remake of all AW images)
- better DVFS on H3/H5/A64, enabled higher cpu speed.
- added overlay support for Tinkerboard/rockchip next and kernel upped to 4.19.y
- updated next kernel for Odroid XU4 to 4.19.y
- updated next kernel for Odroid C2, Lepotato and Nanopik2-S905 to 4.19.y with overlay support
- fixed poweroff on H5
- H5/A64 lost experimental status,
- upgraded images and upstream/bugfix kernel upgrade for Rock64, Renegade,
- u-boot update is moved from automated to manual (armbian-config) to minimize boot related troubles
- added two repository mirrors: China and France (armbian-config -> Personal -> Mirror)
- changed switching to alternative kernels from armbian-config. It is possible to select a direct version and it only replaces kernel (safer)
- first official build for Olimex Teres
- mainline kernel builds for: Pine64, Pine64so, Olinuxino A64, OrangepiWin
- added more download variants for Rock64, Renegade, Tritium H3&H5
- updated images for Z28PRO, Bananapi PRO, Espressobin, Olimex Micro, Lime, Udoo, Bananapi M2, Bananapi M2U,

## v5.68 (2018-12-30)

- updated Espressobin images, kernel updated to 4.19.y

## v5.67 (2018-11-26)

- updated Helios4 images
- added experimental mainline kernel images for Pinebook and Pinebook 1080p

## v5.67 (2018-11-12)

- updated images for Bananapi R2 with eMMC install support.

## v5.66 (2018-11-08)

- added Mediatek MT7623 family.
- added images for Bananapi R2 with kernel 4.19.y without official support.

## v5.66 (2018-11-07)

- removing Odroid C2 official support, drop its default 3.16.y kernel from build engine and merge with the meson64 family.
- attach meson64 dev to 4.19.y
- drop Udoo Neo completly, drop Udoo Quad default and dev kernel.
- Odroid XU4: drop kernel 3.10.y, default branch is upgraded to offical 4.14.y, next becomes vanilla 4.19.y

## v5.65 (2018-11-06)

- Cubox-i/Hummigboard: drop kernel 3.14.y and move 4.14.y to default, next becomes 4.19.y, dev 4.19.y with a mainline u-boot

## v5.64 (2018-10-09)

- updated images and packages for Helios4.
- added images for Nanopi Neo4.

## v5.63 (2018-10-08)

- updated images for Helios4 with SPI booting support.
- updated armbian-config. Added advanced ZSH shell install with most used plugins and tmux.

## v5.62 (2018-10-01)

- updated armbian-config

## v5.61 (2018-09-26)

- updated armbian-config,
- fixed Chromium on Debian builds with a workaround. We are overwriting package with last known working one. It will show some error on startup which is safe to ignore. This workaround will fade out with Chromium upstream update.

## v5.60 (2018-09-19)

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

## v5.59 (2018-08-18)

- rebuilt images for Espressobin with kernel 4.18.y, Nanopc T4

## v5.58 (2018-08-13)

- rebuilt images for Bananapi, Bananapi Pro, Bananapi+, Odroid C2, Odroid XU4
- updated repository for Odroid C2/XU4, changed NEXT from 4.9.y to 4.14.y

## v5.58 (2018-08-13)

- rebuilt images for Bananapi, Bananapi Pro, Bananapi+

## v5.57 (2018-08-11)

- added Bionic desktop and Stretch CLI images for RK3399 powered Nanopc T4

## v5.56 (2018-08-10)

- rebuilt images for Pinebook. Added Bionic build

## v5.55 (2018-08-09)

- rebuilt images for Orangepi One+, Orangepi Lite 2 and Pine H64. Enabled USB3, network, THS, DVFS, higher frequencies, HDMI on 4.18.y DEV branch images.

## v5.55 (2018-08-03)

- added Stretch and Bionic mainline kernel images for Odroid C1 (testing),
- rebuilt images for Bananapi M3 (fixed ethernet)

## v5.54 (2018-07-25)

- updated images for Odroid C2, Nanopi M3, Nanopi Fire 3 and NanoPC T3+, Espressobin, Cubox-i/HB and Le potato
- added preview images without end user support for [Bananapi M3](https://www.armbian.com/bananapi-m3/),Cubietruck+ and [Bananapi M2 Berry](https://www.armbian.com/bananapi-m2u/).

## v5.53 (2018-07-23)

- Z28PRO images updated. Fixed wireless and Bluetooth
- FriendlyARM Nanopi K2 S905 images updated. Fixed ethernet problems.
- FriendlyARM Nanopi K1+ images updated. Fixed HDMI out and wireless

## v5.51 (2018-07-04)

- Helios4 Stretch and Bionic images update

## v5.50 (2018-06-28)

- Espressobin images rebuild and repository update, default 4.4.138, next 4.17.3, dev 4.18.RC, hardware crypto support in 4.17.y, zram and zswap
- Odroid C2 bugfix update

## v5.49 (2018-06-28)

- Amlogic Meson64 family (Odroid C2, Lepotato and FriendlyARM K2 S905) were merged into one kernel. Default images comes with kernel 4.14.52, next with 4.17.3 and DEV with 4.18.RC, updated boot scripts, implemented latest kernel bug fixes
- updated kernels, desktop packages and armbian config on the stable repository (apt update & upgrade)

## v5.48 (2018-06-26)

- added nightly images for Odroid C2 with 4.16.y (NEXT) and 4.18.y (DEV) and hopefully fixed ethernet driver

## v5.47 (2018-06-22)

- Odroid C2 images rebuild. Legacy kernel was upgraded to 3.16.57, next to 4.14.51, u-boot to 2018.05
- Added Tritium H5

## v5.46 (2018-06-20)

- Added Olimex Teres nightly builds
- Added FriendlyARM Nanopi K1 plus

## v5.46 (2018-06-06)

- Added Orange Pi Lite 2 and One plus nightly builds

## v5.45 (2018-05-23)

- Orangepi Zero+ images rebuild

## v5.44 (2018-05-10)

- Espressobin images were rebuilt and moved under stable. Kernel 4.14.40, Stretch, Xenial and Bionic. Fixed bootloader, ath10 wireless card support
- added initial Bionic storage to the main apt repository
- Cubox-i / Hummingboard bugfix update to 4.16.y and images rebuild
- Odroid C2 images rebuild

## v5.41 (2018-02-10)

- fixed LED driver on Helios4
- bugfix update on sunxi/sunxi64 kernel. Updated to 4.14.18
- kernel update for MVEBU next (4.14.18 and default 4.4.115) for Clearfog and Helios4. Upstream fixes,AUFS and Realtek 881yAU drivers update

## v5.40 (2018-02-05)

- fixed eMMC support on Odroid C2 NEXT, kernel 4.14.y
- updated PWM driver on Helios4
- kernel update for MVEBU next (Clearfog, Helios4)

## v5.38 (2018-01-29)

- updated all images
- added H3/H5 testing images with kernel 4.14.y
- added Nanopi M3/T3+/Fire testing image
- fixed Bluetooth on Orangepi Win
- main repository update with recent kernel on all NEXT builds


## v5.37 (2018-01-23)

- bugfix release
- armbianmonitor -u fix
- setting cronjob permissions
- replace broken u-boot packages on A20 boards
- updated utilities: hostapd, sunxi-tools, armbian-config
- updated images: Bananapi, PRO, M2, BeelinkX2, Clearfog,Cubieboard2, Cubietruck, Cubox-i/HB, Espressobin, Helios4

## v5.36 (2017-12-03)

- [bugfix release](https://forum.armbian.com/topic/5759-535-bug-questions-collection)

## v5.35 (2017-11-25)

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

## v5.34 (2017-10-18)

- bugfix Odroid XU4/HC1 image rebuild [due to broken USB install on kernel 4.9.x](https://forum.armbian.com/topic/5413-odroid-hc1-sata-install)
- added Le Potato and Orange Pi Zero testing image (mainline kernel)
- Tinkerboard, MiQi and Pinebook images rebuilt

## v5.33 (2017-09-24)

- Odroid XU4/HC1 images were rebuilt.

## v5.33 (2017-09-21)

- Tinkerboard and MiQi images were rebuilt. Rockchip legacy kernel was updated to 4.4.88 and mainline (NEXT) to 4.13.3.

## v5.32 (2017-06-23)

- bugfix release [due to broken crypto functions on kernel 4.11.x](https://forum.armbian.com/topic/4556-partial-bugfix-update/)

## v5.31 (2017-06-15)

- bugfix release [due to network failure](https://forum.armbian.com/topic/4498-no-boot-after-upgrade-to-530/) on some A10 / A20 boards

**End of support notice**

Following boards are no longer receiving support and updates since this version:

- Cubieboard (Allwinner A10) - not enough hardware samples to maintain support
- Lamobo R1 (Allwinner A20) - hardware design flaws, poor software support for the onboard switch
- Olimex Lime A10

## v5.30 (2017-06-14)

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

## v5.26, v5.27 (2017-02-24)

- security update for most kernels (packages only)
- fixes for hostapd configuration

## v5.25 (2017-02-02)

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

## v5.24

- this version is not released, it was used for the nightly or user-built images

## v5.23 (2016-10-23)

- fixed bug in nand-sata-install
- fixed u-boot update bug on Allwinner platform

Known problems:

- Lamobo R1 fails to boot upon upgrade

## v5.22 (2016-10-22)

- fixed eMMC install on Odroid C2
- firmware package was splitted into minimal (default) and full versions
- patched [Dirty COW exploit](https://thehackernews.com/2016/10/linux-kernel-exploit.html) on all kernels
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

## v5.20 (2016-09-16)

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
- sunxi boards: [GLshim](https://github.com/ptitSeb/gl4es) was added to desktop images with Mali support (except for Orange Pi Plus and Orange Pi Plus 2e)
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

## v5.17 (2016-07-07)

- bugfix release on some boards.

## v5.16 (2016-07-05)

- bugfix release. In 5.15 we accidentaly overwrote default network settings. Check /etc/network/interfaces if you use advanced network settings or fixed ip.
- small changes.

## v5.15 (2016-07-01)

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

## v5.14 (2016-06-14)

- all images rebuilt, most of them were manually tested
- added Beelink X2 image
- Cubox / Hummingboard kernel upgrade to 3.14.72 and 4.6.2
- Trusty was replaced with Xenial

## v5.12 (2016-05-31)

- updated C1 images
- added wifi driver for new Oranges (modprobe 8189fs)
- added Orange Pi Lite, PC Plus and Plus 2E images

## v5.11 (2016-05-24)

- Various bug fixes
- new working images for Actions Semi S500 boards

## v5.10 (2016-05-01)

Images:

- all 3.10+ kernels [are Docker ready](https://forum.armbian.com/topic/490-docker-on-armbian/)
- all A10/A20/H3 comes with HW accelerated video playback in desktop build
- [fixed root exploit on H3 boards](https://github.com/armbian/build/issues/282)
- [fixed kswapd 100% bug on H3 boards](https://github.com/armbian/build/issues/219)
- fixed SPDIF / I2S audio driver in legacy kernel
- fixed Udoo Neo wireless
- fixed slow SD cards boot
- fixed Allwinner SS driver
- fixed bluetooth on Cubietruck, both kernels
- fixed wireless driver on H3 boards
- [fixed R1 switch driver](https://github.com/armbian/build/commit/94194dc06529529015bfd04767865bbd04d29d9b)
- kernel for Allwinner boards was upgraded to 3.4.112 & 4.5.2
- kernel for iMx6 boards was upgraded to 3.14.67 & 4.5.2
- kernel for Armada (Clearfog) was upgraded to 3.10.101 & 4.5.2
- kernel for Udoo boards was updated to 3.14.67 & 4.4.8
- kernel for Guitar (Lemaker) was upgraded to 3.10.101
- kernel for H3/sun8i legacy come from new Allwinner updated source (friendlyarm)
- [added support for Olimex Lime2 eMMC](https://github.com/armbian/build/issues/258)
- [increased MALI clockspeed on sun8i/legacy](https://github.com/armbian/build/issues/265)
- added [Armbianmonitor](https://forum.armbian.com/topic/881-prepare-v51-v201604/?tab=comments#comment-7095)
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

## v5.06 (2016-03-18)

- increase kernel version to 3.4.111
- headers auto creation while install (eases kernel/driver compilation)
- improved SD card partitioning to help old/slow cards with wear leveling and garbage collection
- Possible to use _Ubuntu Xenial Xerus_ as target
- changed behaviour of board leds (green == power, red == warning)
- speed improvements for 1st automated reboot
- Integrates OverlayFS backport

## v5.05 (2016-03-08)

- Auto detection for the Orange Pi 2 does work now
- Mali acceleration works for all users not only root
- verbose boot logging on 1st boot and after crashes (you can toggle verbose logging using `sudo armbianmonitor -b`)
- more WiFi dongles supported due to backported firmware loader patch
- all 3 USB ports on Orange Pi One (Lite) available ([2 of them need soldering](https://forum.armbian.com/topic/755-tutorial-orange-pi-one-adding-usb-analog-audio-out-tv-out-mic-and-ir-receiver/))
- I2S possible on all Orange Pis (compare with the [mini tutorial](https://forum.armbian.com/topic/759-tutorial-i2s-on-orange-pi-h3/) since you need to tweak script.bin)
- default display resolution set to 720p60 to fix possible overscan issues on 1st boot
- HW accelerated video decoding works for most formats
- Booting from eMMC on OPi Plus now possible
- Udoo quad images upgraded to 4.4.4

## v5.04 (2016-03-01)

- HDMI/DVI works (bug in boot.cmd settings)
- Reboot issues fixed (bug in fex settings)
- 1-Wire useable (we chose to stay compatible to loboris' images so the data pin is 37 by default. You're able to change this in the [fex file](https://github.com/armbian/build/blob/6d995e31583e5361c758b401ea44634d406ac3da/config/orangepiplus.fex#L1284-L1286))
- changing display resolution and choosing between HDMI and DVI is now possible with the included _h3disp_ tool (should also work in the [stand-alone version](https://forum.armbian.com/topic/617-wip-orange-pi-one-support-for-the-upcoming-orange-pi-one/page/6/?tab=comments#comment-5480) with Debian based OS images from loboris/Xunlong). Use `sudo h3disp` in a terminal to get the idea.
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

## v5.03 (2016-02-20)

- H3 images rebuilt

## v5.02 (2016-02-18)

- H3 images rebuilt

## v5.01 (2016-02-17)

- Bugfix update for [Allwinner boards](https://forum.armbian.com/topic/691-banana-pro-testers-wanted-sata-drive-not-working-on-some-boards/)
- Update [for H3 based boards](https://github.com/armbian/build/commit/c93d7dfb3538c36739fb8841bd314d75e7d7cbe5)

## v5.00 (2016-02-12)

- mainline kernel for Allwinner based boards upgraded to 4.4.1
- Allwinner audio driver playback and capture on kernel 4.4.1, [UAS](https://linux-sunxi.org/USB/UAS), USB OTG, battery readings,
- added Marvel Armada kernel 3.10.96, 4.4.1 and patches for changing mPCI to SATA
- added Cubox / Hummingboard kernel 4.4.1 (serial console only)
- firstrun does autoreboot only if needed: wheezy and some legacy kernels.
- [added motd](https://forum.armbian.com/topic/602-new-motd-for-ubuntudebian/?tab=comments#comment-4223) to /etc/updated.motd ... redesign, added battery info for Allwinner boards, bugfix, coloring
- fixed temperature reading on Cubox / Hummingboard legacy kernel
- fixed FB turbo building on Allwinner
- fixed NAND install on A10 boards (Legacy kernel only)
- fixed USB boot, added PWM on mainline
- fixed Banana PRO/+ onboard wireless on mainline kernel - running with normal Banana DT.
- readded USB sound
- added [A13 Olimex SOM](https://www.olimex.com/Products/SOM/A13/A13-SOM-512/)
- added [LIRC GPIO receive and send driver](https://github.com/armbian/build/issues/135) for legacy Allwinner
- added LED MMC activity to mainline kernels for Cubietruck and Cubieboard A10
- build script: option to build images with F2FS root filesystem for Allwinner boards
- build script: added alternative kernel for Lemaker Guitar (NEXT), Cubox (DEV)

## v4.81 (2015-12-28)

- complete build script rework
- new development kernel package linux-image-dev-sunxi (4.4RC6) for Allwinner boards
- added Lemaker Guitar, kernel 3.10.55
- added Odroid XU3/4, kernel 3.10.94 and mainline 4.2.8
- mainline kernel for Allwinner based boards upgraded to 4.3.3
- Udoo mainline upgraded to 4.2.8, legacy to 3.14.58
- cubox / hummingboard upgraded to 3.14.58, added mainline kernel 4.4
- fixed Jessie RTC bug, systemd default on Jessie images

## v4.70 (2015-11-30)

- Bugfix update(apt-get update && apt-get upgrade)
- small changes and fixes

## v4.6 (2015-11-24)

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

## v4.5 (2015-10-14)

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

## v4.4 (2015-10-01)

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

## v4.3 (2015-09-17)

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

## v4.2 (2015-09-01)

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

## v4.1 (2015-08-05)

- Added desktop image
- U-Boot 2015.07 with many new features
- Added auto system update via repository apt.armbian.com
- Root password change is initialized at first boot.
- 3.4.108 kernel fixes, 4.1.4 Allwinner Security System

## v4.0 (2015-07-12)

- Fixed stability issues, temperature display in 4.x
- Kernel upgrades to 3.4.108 and 4.1.2

## v3.9 (2015-06-11)

- Bugfix release
- Kernel 4.0.5 traffic control support
- SATA / USB install fixed on kernel 4.x
- Added 256Mb emergency swap area, created automatically @first boot

## v3.8 (2015-05-21)

- Bugfix release: Cubietruck images successfully booted on Cubietruck. I waited for automatic reboot than tested remote login.
- Kernel 4.0.4 added support for power on/off button
- Both: Jessie fixed, Ethernet init fixed (uboot)
- armbian.com introduction

## v3.7 (2015-05-14)

- Kernel 4.0.3 some new functionality
- Kernel 3.4.107 added sunxi display manager to change FB on demand
- Both: Ubuntu and jessie install errors fixed, removed busybox-syslogd and changed to default logger due to problems in Jessie and Ubuntu, apt-get upgrade fixed, documentations update, Uboot fixed to 2015.4 – no more from dev branch
- Build script rework - image size shrink to actual size, possible to have fat boot partition on SD card, several script bug fixes

## v3.6 (2015-04-29)

- Kernel 3.19.6
- Kernel 3.4.107 with better BT loading solution

## v3.5 (2015-04-18)

- Kernel 3.19.4: fixed AP mode, fixed USB, added 8192CU module
- Common: apt-get upgrade ready but not enabled yet, serial console fixed, fixed hostapd under jessie, easy kernel switching, latest patched hostapd for best performance – normal and for realtek adaptors, auto IO scheduler script
- Build script: everything packed as DEB

## v3.4 (2015-03-28)

- Kernel 3.19.3: docker support, apple hid, pmp, nfsd, sata peformance fix
- Kernel 3.4.106: pmp, a20_tp - soc temp sensor
- Common: console setup fixed, headers bugfix, nand install fix
- Build script: kernel build only, custom packets install, hardware accelerated desktop build as option

## v3.3 (2015-02-28)

- Kernel 3.19.0: many new functionality and fixes.
- Bugfixes: CT wireless works in all kernels

## v3.2 (2015-01-24)

- Possible to compile external modules on both kernels
- Kernel 3.19.0 RC5
- Bugfixes: install script, headers, bashrc, spi

## v3.1 (2015-01-16)

- Kernel 3.19.0 RC4
- Added Cubieboard 1 images
- Dualboot for CB2 and CT dropped due to u-boot change. Now separate images.
- New user friendly SATA + USB installer, also on mainline

## v3.0 (2014-12-29)

- Kernel 3.18.1 for mainline image
- Added Ubuntu Trusty (14.04 LTS) image
- Bugfixes: auto packages update

## v2.9 (2014-12-03)

- Kernel 3.4.105 with new MALI driver and other fixes
- Added: Jessie image
- Major build script rewrite - much faster image building
- Fixed: failed MIN/MAX settings

## v2.8 (2014-10-17)

- Added: ondemand governor, fhandle, squashfs and btrfs
- Removed: bootsplash, lvm, version numbering in issue
- Fixed: custom scripts, Jessie upgrade
- Disabled: BT firmware loading, enable back with: insserv brcm40183-patch
- Added working driver for RT 8188C, 8192C

## v2.7 (2014-10-01)

- Kernel 3.4.104
- Automatic Debian system updates
- VGA output is now default but if HDMI is attached at first boot than it switch to HDMI for good. After first restart!
- Fixed NAND install script. /boot is mounted by default. Kernel upgrade is now the same as on SD systems.
- Cubieboard2 - disabled Cubietruck dedicated scripts (BT firmware, LED disable)
- Added network bonding and configuration for "notebook" mode (/etc/network/interfaces.bonding)
- IR receiver is preconfigured with default driver and LG remote (/etc/lirc/lircd.conf), advanced driver is present but disabled
- Added SPI and LVM functionality
- Added Debian logo boot splash image
- Added build essentials package

## v2.6 (2014-08-22)

- Kernel 3.4.103 and 3.17.0-RC1
- Added GPIO patch (only for 3.4.103)

## v2.5 (2014-08-02)

- Kernel 3.4.101 and 3.16.0-RC4
- major build script rewrite

## v2.4 (2014-07-11)

- Kernel 3.4.98
- default root password (1234) expires at first login
- build script rewrite, now 100% non-interactive process, time zone as config option
- bug fixes: removed non-existing links in /lib/modules

## v2.3 (2014-07-02)

- Kernel 3.4.96
- cpuinfo serial number added
- bug fixes: stability issues - downclocked to factory defaults, root SSH login enabled in Jessie, dedicated core for eth0 fix
- disp_vsync kernel patch

## v2.2 (2014-06-26)

- Kernel 3.4.94
- Added Jessie distro image
- Updated hostapd, bashrc, build script
- bug fixes: disabled upgrade and best mirror search @firstboot, bluetooth enabler fix
- MD5 hash image protection

## v2.1 (2014-06-13)

- Kernel 3.4.93
- Onboard Bluetooth finally works
- Small performance fix
- Allwinner Security System cryptographic accelerator

## v2.0 (2014-06-02)

- Kernel 3.4.91 with many fixes
- Cubieboard 2 stability issues fix
- eth0 interrupts are using dedicated core
- Global bashrc /etc/bash.bashrc
- Verbose output and package upgrade @ first run

## v1.9 (2014-04-27)

- Kernel headers included
- Clustering support
- Advanced IR driver with RAW RX and TX
- Bluetooth ready (working only with supported USB devices)
- Bugfixes: VLAN, login script, build script
- New packages: lirc, bluetooth

## v1.8 (2014-03-27)

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

## v1.7 (2014-02-26)

- Flash media performance tweaks, reduced writings, tmp & logging to RAM with ramlog app – sync logs on shutdown
- SATA install script
- Dynamic MOTD: Cubieboard / Cubietruck
- Disabled Debian logo at startup
- New packages: figlet toilet screen hdparm libfuse2 ntfs-3g bash-completion

## v1.6 (2014-02-09)

- Added support for Cubieboard 2
- Build script creates separate images for VGA and HDMI
- NAND install script added support for Cubieboard 2

## v1.52 (2014-02-07)

- Various kernel tweaks, more modules enabled
- Root filesystem can be moved to USB drive
- Bugfixes: NAND install script

## v1.5 (2014-01-22)

- Hotspot Wifi Access Point / Hostapd 2.1
- Bugfixes: MAC creation script, SSH keys creation, removed double packages, …
- Graphics desktop environment upgrade ready

## v1.4 (2014-01-12)

- Patwood’s kernel 3.4.75+ with many features
- Optimized CPU frequency scaling 480-1010Mhz with interactive governor
- NAND install script included
- Cubietruck MOTD
- USB redirector – for sharing USB over TCP/IP

## v1.3 (2014-01-03)

- CPU frequency scaling 30-1000Mhz
- Patch for gpio

## v1.23 (2014-01-01)

- added HDMI version
- added sunxi-tools
- build.sh transfered to Github repository
- disabled LED blinking

## v1.2 (2013-12-26)

- changed kernel and hardware config repository
- kernel 3.4.61+
- wi-fi working
- updated manual how-to

## v1.0 (2013-12-24)

- total memory available is 2G (disabled memory for GPU by default)
- gigabit ethernet is fully operational
- sata driver enabled
- root filesystem autoresize
- MAC address fixed at first boot
- Kernel 3.4.75
- root password=1234
- Bugs: wifi and BT not working
