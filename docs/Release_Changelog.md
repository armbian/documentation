# Changelog

* Note: If a new sub-version is released this does not necessarily mean all boards receive a new version number since most of the time these fixes are targeting a specific board or board family only.

## What's Changed

## v25.8.1 (2025-8-17)

 
    • Fix - Package apt-xapian-index missing on Trixie by @Grippy98 in #8202 
    • Fix and improve Armbian GH Action by @igorpecovnik in #8201 
    • partitioning: fix compressed BTRFS creation by @alex3d in #8200 
    • Allwinner: replace bc with awk in temperature check by @igorpecovnik in #8205 
    • Work if no customize-image.sh present by @iav in #8222 
    • grub: ensure tty0 console if others used by @rpardini in #8247 
    • artifacts: force fsync() before caching by @rpardini in #8242 
    • rootfs-to-image: drop --sparse (too slow) by @rpardini in #8249 
    • docker: speed up extension checks by @rpardini in #8248 
    • kernel-debs: retry make clean with logs by @rpardini in #8241 
    • Signing key: keep symlink to old location by @igorpecovnik in #8282 
    • motd: fix login screen alignment by @leggewie in #8322 
    • README cleanup, update logo, declutter by @igorpecovnik in #8391 
    • Plymouth: update boot logo by @igorpecovnik in #8381 
    • fix firstlogin password creation on sid by @amazingfate in #8415 
    • gcc-arm-linux-gnueabi: install conditionally by @leggewie in #8401 
    • Don’t copy id_ecdsa if not needed by @gbrdead in #8446 
    • minor spelling mistakes by @leggewie in #8450 
    • APA extension: small fixes by @leggewie in #8509 
    • Trixie: drop non-existing packages by @igorpecovnik in #8279 
    • Bullseye: drop backports repo (gone) by @igorpecovnik in #8437 
    • Debian: drop security repo from package lists by @igorpecovnik in #8444 
    • Debian Trixie: declare supported by @igorpecovnik in #8470 
    • Wireless drivers: bump commit hash, mark deprecated by @igorpecovnik in #8408 
    • kernel-debs: use dynamic kernel image names by @amazingfate in #8451 
    • Improve WiFi support for sun50iw1 family by @leggewie in #8467 
    • drop apt-xapian-index and pavumeter from desktops by @leggewie in #8356 
    • update plasma-workspace pkgs for RB5 by @leggewie in #8357 
    • config/desktop: disable mate-sntray-plugin on Trixie by @leggewie in #8491 
    • config/desktop: update gnome-bluetooth in Noble/Trixie by @leggewie in #8502 
    • Preparation for HTTP proxy caching by @EvilOlaf in #8281 
    • Add dual signing support by @igorpecovnik in #8320 
    • Add new repository key by @igorpecovnik in #8323 
    • mvebu: bump EDGE kernel to 6.12 by @igorpecovnik in #8193 
    • sunxi 6.12: switch to v6.12.30 by @The-going in #8233 
    • sunxi-6.15: bump EDGE to v6.15 by @The-going in #8270 
    • Allwinner: bump current to 6.12.35 & edge to 6.15.4 by @igorpecovnik in #8337 
    • rockchip64: bump edge to 6.16-rc3 by @EvilOlaf in #8328 
    • mainline-kernel: bump 6.16 → released by @amazingfate in #8443 
    • uefi-arm64: bump to 6.16 by @amazingfate in #8453 
    • rockchip edge: bump to 6.16 by @paolosabatino in #8435 
    • rpi4b: bump edge to 6.16 by @EvilOlaf in #8390 
    • BPI-F3: update linux-6.6.95 → 99 by @pyavitz in #8411 
    • SpacemiT: linux-6.6.93 → 95 by @pyavitz in #8333 
    • odroidxu4: bump to 6.6.93 → 100 by @belegdol in #8277, #8442 
    • Bump rockchip32 edge kernel to 6.15 by @paolosabatino in #8262 
    • Bump imx6, mvebu, xu4 kernels, mark wdk2023 EoS by @igorpecovnik in #8410 
    • khadas-edge2: fix u-boot by @efectn in #8220 
    • Gateway GZ80x: switch back to u-boot v2024.10 by @pyavitz in #8216 
    • nanopct6(-lts): bump u-boot to v2025.04 final by @rpardini in #8239 
    • odroidhc4: u-boot v2025.04, unify configs by @rpardini in #8244 
    • mixtible-blade3: revert to radxa u-boot v2024.03 by @rpardini in #8243 
    • khadas-vim3: bump u-boot v2025.04 final by @rpardini in #8238 
    • nanopct6(-lts): switch to mainline ATF + u-boot for current by @rpardini in #8219 
    • tinkerboard-2: bump u-boot v2025.04 by @hyx0329 in #8268 
    • quartz64a: bump u-boot to v2025.04 final by @rpardini in #8250 
    • BananaPi BPI-M4-Zero: bump u-boot v2025.01 & v2025.07 by @pyavitz in #8339, #8434 
    • orangepi5pro: bump u-boot v2025.07 (eMMC) by @c127dev in #8417 
    • MBa8MPxL: bump u-boot to v2024.04 by @schmiedelm in #8291 
    • station-m3: update u-boot patches by @chainsx in #8424 
    • lckfb-taishanpi: update u-boot patches by @chainsx in #8428 
    • rock-4se: binman boot with mainline ATF by @jclds139 in #8449 
    • Update Realtek RTL8822CS external driver by @adeepn in #8195 
    • Unlock radios on RPi with service by @igorpecovnik in #8210 
    • helios4: fix WOL service by @djurny in #8235 
    • Rock-5C: enable thermal sensors by @mdziekon in #8430 
    • Fix DSI display on RPi5 by @CaWeissWz in #8294 
    • Restore RockPI-S audio by @brentr in #8360 
    • SMART AM40: add PHY LED config by @retro98boy in #8431 
    • Gateway GZ80x: add rtl8723ds BT support by @pyavitz in #8351 
    • Orangepi Zero: drop Crust support (fix reboot) by @igorpecovnik in #8503 
    • linux-rk35xx-vendor: add LTE em05 driver by @rafayahmed317 in #8484, #8508 
    • Xradio: adjust for kernel 6.16+ by @igorpecovnik in #8469 
    • Innosilicon USB3 phy driver for rk3328 by @paolosabatino in #8510 
    • Netplan: DHCP on lan*/wan* interfaces by @djurny in #8259 
    • sunxi-6.14: bananapi_m4_berry → supported by @The-going in #8226 
    • SpacemiT: enable audio, bump kernels by @pyavitz in #8221, #8333, #8481 
    • CAINIAO CNIoT-CORE initial support by @retro98boy in #8208 
    • NanoPi R3S LTS added by @pyavitz in #8300 
    • BananaPi BPI-CM4 Waveshare IO-BASE-B fixes by @pyavitz in #8303 
    • Add imb3588 board by @JackHuang021 in #8267 
    • Add KickPi K2B board by @pyavitz in #8452 
    • Add DshanPi A1 (RK3576) by @chainsx in #8380 
    • Orange Pi 5 Pro initial support by @c127dev in #8348 
    • Orange Pi 5 Ultra fixes & improvements by @khusika in #8373 
    • Rock-5B-Plus: align Edge with upstream by @HeyMeco in #8338 
    • BananaPi BPI-M4-Zero DTS + overlays fixes by @pyavitz in #8339, #8434, #8448, #8454, #8498 
    • BananaPi CM4/M2S: revert SDIO WiFi change by @pyavitz in #8495 
    • Nanopi R6/R5: netplan fix (wan→wan1) by @igorpecovnik in #8325 
    • PocketBeagle2: image fixes + USB serial enable by @Ayush1325 in #8283, #8349, #8370 
    • Pcduino2/3: add HDMI, fix drm regression by @Ryzer58 in #8341 
    • MediaTek Filogic: BananaPi R4 community support by @chainsx in #8407 
    • Radxa Cubie A5E: migrate to mainline 6.16 by @juanesf in #8447 
    • coolpi-genbook: vendor branch by @andyshrk in #8275 
    • Inovato quadra bootfix + u-boot bump by @igorpecovnik in #8334 


## v25.5.1 (2025-5-26)

* [Bugfix] Fixed Non supported OS warning message.  by @Tearran in https://github.com/armbian/configng/pull/498 
* [Bugfix] feature array names,  by @Tearran in https://github.com/armbian/configng/pull/305
* [Bugfix] Unexpected command executed when config overlays #349 by @Tearran in https://github.com/armbian/configng/pull/355
* Activate the specified network interface, before applying IP stack by @igorpecovnik in https://github.com/armbian/configng/pull/411
* Add _out of date_ notice to example config by @EvilOlaf in https://github.com/armbian/build/pull/8106
* Add a collection of applications for downloading by @igorpecovnik in https://github.com/armbian/configng/pull/270
* Add arch to the module template by @igorpecovnik in https://github.com/armbian/configng/pull/471
* Add armbian-router to software section by @efectn in https://github.com/armbian/configng/pull/429
* Add bananapim7 description - interactive build fix by @Grippy98 in https://github.com/armbian/build/pull/8155
* Add BeagleY & K3 Kernel Updates by @Grippy98 in https://github.com/armbian/build/pull/7950
* Add buttons for editing or adding header and footer by @igorpecovnik in https://github.com/armbian/configng/pull/602
* Add code style checking exception for Prometheus by @igorpecovnik in https://github.com/armbian/configng/pull/477
* Add configurable EFI partition alignment to support UFS devices by @FantasyGmm in https://github.com/armbian/build/pull/8053
* Add e2fspros as it fell out of default dependency by @igorpecovnik in https://github.com/armbian/build/pull/7894
* Add GPG key download for 3rd party distro by @igorpecovnik in https://github.com/armbian/configng/pull/381
* Add initial support for BeagleBoard PocketBeagle2 by @Grippy98 in https://github.com/armbian/build/pull/7897
* Add initial support for BeagleBone AI-64 by @Grippy98 in https://github.com/armbian/build/pull/7918
* Add initial support for BeaglePlay by @Grippy98 in https://github.com/armbian/build/pull/7917
* Add initial support for TI SK-AM69 board by @glneo in https://github.com/armbian/build/pull/7885
* Add lcd panel of hinlink-h88k support to rockchip64 current and edge by @amazingfate in https://github.com/armbian/build/pull/7901
* Add Mediatek Genio Family + Radxa Nio-12L by @HeyMeco in https://github.com/armbian/build/pull/8006
* Add missing cockpit module by @Tearran in https://github.com/armbian/configng/pull/342
* Add missing deps for generating deb file by @igorpecovnik in https://github.com/armbian/configng/pull/314
* Add Odroid board selection by @GeoffClements in https://github.com/armbian/configng/pull/298
* Add option to disable kernel patching by @timsurber in https://github.com/armbian/build/pull/8149
* Add Qcom Robotics RB5 Support by @FantasyGmm in https://github.com/armbian/build/pull/8017
* Add Radxa Cubie A5E (sun55i-a527) by @juanesf in https://github.com/armbian/build/pull/7852
* Add reset and power down support for both ODROID SM1 units by @pyavitz in https://github.com/armbian/build/pull/7900
* Add sandboxed SSH server port [2222] to the menu by @igorpecovnik in https://github.com/armbian/configng/pull/514
* Add Scheduled Workflow to Clean Old GitHub Action Logs by @igorpecovnik in https://github.com/armbian/configng/pull/569
* Add screenshot for several section of auto-made documentation by @igorpecovnik in https://github.com/armbian/configng/pull/486
* add SMART AM40 support by @retro98boy in https://github.com/armbian/build/pull/8002
* Add software package: Home Assistant by @igorpecovnik in https://github.com/armbian/configng/pull/235
* Add support for MOTD logo colors by @igorpecovnik in https://github.com/armbian/build/pull/8018
* Add support for NanoPi R2S Plus by @ig3 in https://github.com/armbian/build/pull/7913
* Add VENDOR color to BSP and artifacts hashing by @igorpecovnik in https://github.com/armbian/build/pull/8026
* Add wrapper for package manipulation by @dimitry-ishenko in https://github.com/armbian/configng/pull/320
* Add wrapper for service manipulation by @dimitry-ishenko in https://github.com/armbian/configng/pull/323
* Add Zerotier into configng by @jnovos in https://github.com/armbian/configng/pull/470
* Add ZeroTier short description to fit menu by @igorpecovnik in https://github.com/armbian/configng/pull/580
* Adding a warning to welcome screen by @Tearran in https://github.com/armbian/configng/pull/276
* Adding schematic for network settings by @igorpecovnik in https://github.com/armbian/configng/pull/280
* AdGuardHome and unbound DNS by @igorpecovnik in https://github.com/armbian/configng/pull/415
* Adjust condition to use proper if then fi style by @igorpecovnik in https://github.com/armbian/configng/pull/510
* Adjust images and markdown files by @igorpecovnik in https://github.com/armbian/configng/pull/570
* Adjust keywords for displaying links with ports in the menu by @igorpecovnik in https://github.com/armbian/configng/pull/547
* Adjust software module options to match recent changes by @igorpecovnik in https://github.com/armbian/configng/pull/332
* After changing apt lists methodology, we need to rebuild rootfs cache by @igorpecovnik in https://github.com/armbian/build/pull/7877
* Allow NetworkManager and systemd-networkd by @ig3 in https://github.com/armbian/build/pull/7961
* Allwinner: bump to latest tags - booted on H5 by @igorpecovnik in https://github.com/armbian/build/pull/8100
* Application logos: fix some of images by @igorpecovnik in https://github.com/armbian/configng/pull/564
* Apply several fixes to NFS service by @igorpecovnik in https://github.com/armbian/configng/pull/313
* Armbian internal: deploy Armbian qemu KVM instances by @igorpecovnik in https://github.com/armbian/configng/pull/365
* Armbian internal: GitHub runners deployment script by @igorpecovnik in https://github.com/armbian/configng/pull/364
* Armbian kernel: add ZRAM and DOCKER configurations by @igorpecovnik in https://github.com/armbian/build/pull/8014
* Armbian rsyncd: fix port used in the module by @igorpecovnik in https://github.com/armbian/configng/pull/463
* Armbian runners deploy: fixing bugs by @igorpecovnik in https://github.com/armbian/configng/pull/369
* Armbian system: manage rsyncd server for armbian download instances by @igorpecovnik in https://github.com/armbian/configng/pull/457
* Automation: automatically close issues marked as "Can be closed?"  by @igorpecovnik in https://github.com/armbian/configng/pull/387
* BananaPi BPI-M4-Zero: `Enable GPU and add Audio nodes` by @pyavitz in https://github.com/armbian/build/pull/8191
* BananaPi BPI-M4-Zero: `sunxi: mmc: Improve reset procedure` by @pyavitz in https://github.com/armbian/build/pull/7943
* BananaPi SM1: `Fixup patch name association` by @pyavitz in https://github.com/armbian/build/pull/8099
* BigTreeTech CB2: use mainline device tree on edge (6.14) by @JohnTheCoolingFan in https://github.com/armbian/build/pull/7892
* board: youyeetoo-r1 v3  by @amazingfate in https://github.com/armbian/configng/pull/299
* manage_overlayfs: Keep the default value of overlayroot_cfgdisk by @slowpeek in https://github.com/armbian/configng/pull/372
* Match JSON and modules in order to read data stored in modules by @igorpecovnik in https://github.com/armbian/configng/pull/584
* MBa8MPxL:  add Pi Camera support, fix config | fix in armbian-firstlogin by @schmiedelm in https://github.com/armbian/build/pull/8010
* mekotronics-rk3588: u-boot: back to radxa's v2024.03, as .10 breaks GMAC stable MAC patch by @rpardini in https://github.com/armbian/build/pull/7971
* Mekotronics: move two boards from community supported to supported by @igorpecovnik in https://github.com/armbian/build/pull/8187
* Meson64: adjust patch to match upstream changes by @igorpecovnik in https://github.com/armbian/build/pull/7989
* mksklipad50: add DT overlays for edge kernel by @torte71 in https://github.com/armbian/build/pull/7983
* mksklipad50: Switch to u-boot v2025.01 (resend) by @torte71 in https://github.com/armbian/build/pull/7936
* Module Docker: Check if SUDO_USER variable is defined by @igorpecovnik in https://github.com/armbian/configng/pull/366
* Module ZSH: update package before installing ZSH package by @igorpecovnik in https://github.com/armbian/configng/pull/456
* Move Armbian related services in dedicated section by @igorpecovnik in https://github.com/armbian/configng/pull/581
* Move Domoticz logo to the correct location by @igorpecovnik in https://github.com/armbian/configng/pull/399
* Move wireguard to software section VPN by @igorpecovnik in https://github.com/armbian/configng/pull/578
* Multiple sources fix: after changing to deb822 we forgot on leftovers by @igorpecovnik in https://github.com/armbian/build/pull/7909
* mvebu: bootscript fixes & enhancements by @djurny in https://github.com/armbian/build/pull/8189
* nanopi-r3s, radxa-zero3, rock-3a: board config cleanup & maint by @EvilOlaf in https://github.com/armbian/build/pull/8045
* nanopi-r3s: bump uboot to v2025.04 by @EvilOlaf in https://github.com/armbian/build/pull/8070
* Navidrom: fix problems that are popping up on unit tests by @igorpecovnik in https://github.com/armbian/configng/pull/426
* Network config: Show the "disable hotspot" dialog only if there is an active hotspot on the selected interface. by @fvalasiad in https://github.com/armbian/configng/pull/596
* NFS: several fixes to improve handling by @igorpecovnik in https://github.com/armbian/configng/pull/396
* Odroid XU4: fix broken patch by @igorpecovnik in https://github.com/armbian/build/pull/8146
* odroidm2: use standard `v2025.04` (drop `-rc4`) from u-boot patch folder name; bump `v2025.04-rc4` -> `v2025.04-rc5` by @rpardini in https://github.com/armbian/build/pull/8035
* odroidxu4: fix uboot compilation for Noble hosts by @EvilOlaf in https://github.com/armbian/build/pull/8168
* officially support Banana Pi M2+ by @leggewie in https://github.com/armbian/build/pull/8127
* Opi5max - remove `current` builds by @EvilOlaf in https://github.com/armbian/build/pull/7993
* Optimize JSON Validation Workflow by @igorpecovnik in https://github.com/armbian/configng/pull/568
* Optimizing images - no other changes by @igorpecovnik in https://github.com/armbian/configng/pull/582
* Oracular Ubuntu is no more, switching to Plucky by @igorpecovnik in https://github.com/armbian/configng/pull/392
* orangepi-5-max: switch `edge` u-boot to mainline by @EvilOlaf in https://github.com/armbian/build/pull/8082
* Orangepi5 maintenance by @EvilOlaf in https://github.com/armbian/build/pull/7893
* orangepi5b: split opi5b board from opi5 board config by @efectn in https://github.com/armbian/build/pull/8126
* orangepi5pro: Fix uboot compilation by @EvilOlaf in https://github.com/armbian/build/pull/8181
* Orangepi5PRO: move to EOS as it has broken u-boot compilation on Noble by @igorpecovnik in https://github.com/armbian/build/pull/8172
* Overlay management: disable showing this option where its not supported by @igorpecovnik in https://github.com/armbian/configng/pull/285
* Overlayfs: refactor module structure by @igorpecovnik in https://github.com/armbian/configng/pull/378
* partitioning: Add BTRFS_ROOT_SUBVOLUME switch by @kageurufu in https://github.com/armbian/build/pull/8144
* Pi-hole and adguardhome: addressing small bugs, hardening by @igorpecovnik in https://github.com/armbian/configng/pull/417
* qemu arm64: bump u-boot and fix wrong boot script parameter by @igorpecovnik in https://github.com/armbian/build/pull/7994
* Radxa Nio 12l: dropping vendor kernel as its broken and generally in bad shape by @igorpecovnik in https://github.com/armbian/build/pull/8093
* radxa-zero3: bump mainline uboot by @EvilOlaf in https://github.com/armbian/build/pull/8071
* radxa-zero3: enable wifi extension by default by @EvilOlaf in https://github.com/armbian/build/pull/8049
* RaspberryPi: add support for managing overlays by @igorpecovnik in https://github.com/armbian/configng/pull/451
* RaspberryPi: add brcm firmware package to fix missing wireless support by @igorpecovnik in https://github.com/armbian/build/pull/8118
* RaspberryPi: suppress warnings for missing firmware by @igorpecovnik in https://github.com/armbian/build/pull/8116
* Raspbery Pi: legacy kernel is missing support for CONFIG_FW_LOADER_COMPRESS by @igorpecovnik in https://github.com/armbian/build/pull/7916
* Refactor and cleanup of documentation making code by @igorpecovnik in https://github.com/armbian/configng/pull/544
* Refactor conditions to use if then fi otherwise tests cases are failing by @igorpecovnik in https://github.com/armbian/configng/pull/506
* Refactor patches for NanoPC T6 & LTS by @SuperKali in https://github.com/armbian/build/pull/7980
* Refactoring Desktop installation by @igorpecovnik in https://github.com/armbian/configng/pull/436
* Remove `lib.config` from README.me, create proper example by @EvilOlaf in https://github.com/armbian/build/pull/8090
* Remove deprecated CM3588 devicetree by @timsurber in https://github.com/armbian/build/pull/8150
* Remove escape character from runtime by @Tearran in https://github.com/armbian/configng/pull/341
* Remove mainlined patch in 6.14.5 by @timsurber in https://github.com/armbian/build/pull/8148
* Remove OMV after test install by @igorpecovnik in https://github.com/armbian/configng/pull/594
* Remove wrong unit test definitions by @igorpecovnik in https://github.com/armbian/configng/pull/318
* Remove Xiaomi umi Support by @FantasyGmm in https://github.com/armbian/build/pull/7932
* Repository consistency: rename armbian-development to armbian-config.list by @igorpecovnik in https://github.com/armbian/configng/pull/383
* RESEND - Add initial support for Orangepi 5 Ultra by @EvilOlaf in https://github.com/armbian/build/pull/7902
* RFC: Networking - add simple way without using bridge by @igorpecovnik in https://github.com/armbian/configng/pull/394
* RK3588 add HDMI sound, add support for OPi5 Max by @palachzzz in https://github.com/armbian/build/pull/7884
* rock-3a: bump mainline uboot to v2025.04 by @EvilOlaf in https://github.com/armbian/build/pull/8072
* Rock5 mainline hs400 mode fix by @amazingfate in https://github.com/armbian/build/pull/7921
* Rockchip - Adjustin broken patch for EDGE kernel by @igorpecovnik in https://github.com/armbian/build/pull/8107
* Rockchip RK3588: Adjust mainlined patch by @igorpecovnik in https://github.com/armbian/build/pull/8064
* rockchip-rk3308-current: fix uart dma by @ssp97 in https://github.com/armbian/build/pull/8074
* rockchip/64: bump rk322x-box and rk3318-box to u-boot v2025.01 by @paolosabatino in https://github.com/armbian/build/pull/7895
* rockchip64-6.12: fix compatible for CPU regulator on BTT PI2/CB2 by @anarsoul in https://github.com/armbian/build/pull/7974
* rockchip64-6.14: Add HDMI audio support and missing stuff on Youyeetoo R1 v3 by @SuperKali in https://github.com/armbian/build/pull/7934
* rockchip64-6.14: Add missing opp nodes by @SuperKali in https://github.com/armbian/build/pull/8048
* rockchip64-6.14: Add patch to fix USB 3.0 A on NanoPC T6 by @SuperKali in https://github.com/armbian/build/pull/7969
* rockchip64-6.14: Enabled HDMI1 video and audio on NanoPC T6/LTS by @SuperKali in https://github.com/armbian/build/pull/7933
* rockchip64-6.14: rewrite rock5b hdmi audio patch by @SuperKali in https://github.com/armbian/build/pull/7929
* rockchip64-6.14: Set dma mask to 64 bit by @SuperKali in https://github.com/armbian/build/pull/7924
* rockchip64-edge: bump to 6.14 by @amazingfate in https://github.com/armbian/build/pull/7835
* rockchip64: add multiple SPI images support to armbian-install by @efectn in https://github.com/armbian/build/pull/8123
* rockchip64: bump orangepi4 lts uboot to v2025.01 by @paolosabatino in https://github.com/armbian/build/pull/7964
* rockchip64: bump rockpi-e to u-boot v2025.01 by @paolosabatino in https://github.com/armbian/build/pull/7965
* rockchip64: Enable CAN FD driver MCP251XFD by @mickeprag in https://github.com/armbian/build/pull/8136
* rockchip64: fix atf build by @EvilOlaf in https://github.com/armbian/build/pull/8097
* rockchip64: fix OrangePi 4 LTS boot with BTF, bump uboot to 2024.10 by @paolosabatino in https://github.com/armbian/build/pull/7887
* rockchip64: rk3318-box: fix wifi with alternate sdio bus by @paolosabatino in https://github.com/armbian/build/pull/7959
* rockchip64: rk356x: add PLL rate for 33.3MHz by @anarsoul in https://github.com/armbian/build/pull/7970
* rockchip64: uboot: fix stable mac address for rk3318-box by @paolosabatino in https://github.com/armbian/build/pull/7930
* rockchip: bump tinkerboard and xt-q8l-v10 u-boot to v2025.01 by @paolosabatino in https://github.com/armbian/build/pull/7967
* Rpi bugfix: Split Debian and Ubuntu packages  by @igorpecovnik in https://github.com/armbian/build/pull/8087
* Runner install: add missing dependencies by @igorpecovnik in https://github.com/armbian/configng/pull/606
* sakurapi-rk3308b: several updates for the board by @TheSnowfield in https://github.com/armbian/build/pull/8047
* Sandboxed SSH server: add rsync to the Docker container by @igorpecovnik in https://github.com/armbian/configng/pull/357
* Software title: Actual budget by @igorpecovnik in https://github.com/armbian/configng/pull/419
* Software title: ANSI hastebin docker instance by @efectn in https://github.com/armbian/configng/pull/461
* Software title: Immich as a self-hosted photo/video backup option by @igorpecovnik in https://github.com/armbian/configng/pull/575
* Software title: NetBox full Docker module with automated configuration by @igorpecovnik in https://github.com/armbian/configng/pull/559
* Software title: Redis Module Support by @igorpecovnik in https://github.com/armbian/configng/pull/561
* Software title: Duplicati backup service by @igorpecovnik in https://github.com/armbian/configng/pull/555
* Software title: File browser by @igorpecovnik in https://github.com/armbian/configng/pull/590
* Software title: Grafana monitoring dashboards by @igorpecovnik in https://github.com/armbian/configng/pull/351
* Software title: NetAlertX - scan, monitor and visualize your networks by @igorpecovnik in https://github.com/armbian/configng/pull/479
* Software title: NetData by @igorpecovnik in https://github.com/armbian/configng/pull/289
* Software title: OMV (openmediavault) by @igorpecovnik in https://github.com/armbian/configng/pull/588
* Software title: Samba module by @Tearran in https://github.com/armbian/configng/pull/529
* Software title: Add PostgreSQL Module Support by @igorpecovnik in https://github.com/armbian/configng/pull/560
* Software title: Add prometheus by @efectn in https://github.com/armbian/configng/pull/469
* Software title: Armbianrouter: add cdn.armbian.com container  by @efectn in https://github.com/armbian/configng/pull/460
* Software title: Switch hastebin to golang version by @efectn in https://github.com/armbian/configng/pull/481
* SpacemiT: Defconfig: `Add CONFIG_NFT_FLOW_OFFLOAD=m` by @pyavitz in https://github.com/armbian/build/pull/7951
* SpacemiT: Defconfig: `Add CONFIG_TUN=m` by @pyavitz in https://github.com/armbian/build/pull/8162
* SpacemiT: Defconfig: `Enable PPPoe Module` by @pyavitz in https://github.com/armbian/build/pull/8073
* Standardize naming in Kernel/firmware upgrades by @squassina in https://github.com/armbian/configng/pull/574
* Starfive: bump kernel to v6.6 for starfive2 by @libiunc in https://github.com/armbian/build/pull/8033
* station-m3: delete the redundant function. by @chainsx in https://github.com/armbian/build/pull/8068
* station-p2: bump u-boot to 2025.04 by @chainsx in https://github.com/armbian/build/pull/8081
* station: Clean firmware by @chainsx in https://github.com/armbian/build/pull/8084
* Stop altering global git config file and set safe per cloned repository by @igorpecovnik in https://github.com/armbian/build/pull/7910
* sunxi 6.12: Switch to v6.12.16, Add HDMI support by @The-going in https://github.com/armbian/build/pull/7752
* sunxi 6.13: Switching to v6.13.11; Add pwm, dma, fix hardware decoding video, audio by @The-going in https://github.com/armbian/build/pull/8086
* sunxi-6.12: BUGFIX: Remove the incomplete patch. by @The-going in https://github.com/armbian/build/pull/7947
* sunxi-6.12: sunxi:  by @The-going in https://github.com/armbian/build/pull/8004
* sunxi-6.13: Add all patches by @The-going in https://github.com/armbian/build/pull/7705
* sunxi-6.14: Add all patches by @The-going in https://github.com/armbian/build/pull/8147
* sunxi64: bump ATF to latest LTS tag by @EvilOlaf in https://github.com/armbian/build/pull/8111
* switch `current` u-boot to v2025.01 by @EvilOlaf in https://github.com/armbian/build/pull/8012
* Switch adguard home to network host for accurate client ip address logging by @aancw in https://github.com/armbian/configng/pull/537
* Switch CM3588 to mainline A-TF by @timsurber in https://github.com/armbian/build/pull/7898
* Switch from rkr5 to rkr5.1 by @HeyMeco in https://github.com/armbian/build/pull/8089
* Switch Netdata to host network for proper metrics and accessibility by @fbernier in https://github.com/armbian/configng/pull/516
* System: add NFS daemon install and manipulation by @igorpecovnik in https://github.com/armbian/configng/pull/292
* System: add ZFS compilation support by @igorpecovnik in https://github.com/armbian/configng/pull/282
* Transmission: add docker subnet to the whitelist by @igorpecovnik in https://github.com/armbian/configng/pull/346
* uboot: mainline board: youyeetoo r1 add uboot patches by @SuperKali in https://github.com/armbian/build/pull/8175
* Unattended Upgrade Manager module - reconfiguring automatic updates by @igorpecovnik in https://github.com/armbian/configng/pull/459
* Unit tests: drop several old test cases by @igorpecovnik in https://github.com/armbian/configng/pull/380
* Unit tests: improve configuration and fix bugs by @igorpecovnik in https://github.com/armbian/configng/pull/442
* Unit tests: upgrade unit tests components to mitigate deprecation by @igorpecovnik in https://github.com/armbian/configng/pull/347
* Update all missing connections between JSON and modules by @igorpecovnik in https://github.com/armbian/configng/pull/585
* Update boot-mvebu.cmd by @djurny in https://github.com/armbian/build/pull/8166
* Update IMM001-footer.md for immich by @hartraft in https://github.com/armbian/configng/pull/600
* Update issue template by @igorpecovnik in https://github.com/armbian/configng/pull/386
* Update K3 Family to use Github Mirror over TI Cgit by @Grippy98 in https://github.com/armbian/build/pull/7952
* Update kernel configs with enabled wifi drivers from rtw88/9 by @igorpecovnik in https://github.com/armbian/build/pull/8051
* Update linux-sun55iw3-dev.config by @juanesf in https://github.com/armbian/build/pull/8058
* Update Odin2 Config by @FantasyGmm in https://github.com/armbian/build/pull/7946
* Update odroidxu4-current to 6.6.81 by @belegdol in https://github.com/armbian/build/pull/7931
* Update odroidxu4-current to 6.6.88 by @belegdol in https://github.com/armbian/build/pull/8135
* Update prepare-host.sh to use ntpsec-ntpdate by @squassina in https://github.com/armbian/build/pull/8177
* Update README.md by @leggewie in https://github.com/armbian/configng/pull/464
* Update the version of U-boot used with Radxa rock 4 se to v2025.04 by @trappiz in https://github.com/armbian/build/pull/8115
* Updating maintainers: switch to new location of JSON file by @igorpecovnik in https://github.com/armbian/build/pull/8179
* Upgrade Cherryba-m1 to latest u-boot, move patch to new folder by @igorpecovnik in https://github.com/armbian/build/pull/8131
* Userspace status changes to EOS for bullseye, focal and jammy by @igorpecovnik in https://github.com/armbian/build/pull/8114
* V2 - Update the version of U-boot used with Radxa rock 4 se to v2025.04 by @trappiz in https://github.com/armbian/build/pull/8129
* We need to escape $ otherwise this will be executed on host by @igorpecovnik in https://github.com/armbian/build/pull/8060
* Webserver & reverse proxy with php and SSL support by @igorpecovnik in https://github.com/armbian/configng/pull/329
* Wireless discovery hardening by @igorpecovnik in https://github.com/armbian/configng/pull/302
* Wireless networking: retry 3 times for getting stations by @igorpecovnik in https://github.com/armbian/configng/pull/286
* ZFS: define architecture for ZFS module by @igorpecovnik in https://github.com/armbian/configng/pull/410

## v25.2.2 (2025-2-25)

* Adjusting aml-s9xx as armbian-install was moved to another location by @igorpecovnik in https://github.com/armbian/build/pull/7499
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7496
* thinkpad-x13s: bump to jhovold's wip/sc8280xp-6.12 final by @rpardini in https://github.com/armbian/build/pull/7498
* meson64: bump `edge` from `6.11` to `6.12` via rename by @rpardini in https://github.com/armbian/build/pull/7490
* apt-utils.sh: get base-files package version from GHA by @amazingfate in https://github.com/armbian/build/pull/7473
* sunxi-6.6: Switch to v6.6.62 by @The-going in https://github.com/armbian/build/pull/7503
* sunxi-6.11: Switch to v6.11.9; Fix build dtb package by @The-going in https://github.com/armbian/build/pull/7502
* mainline-kernel.conf.sh: bump 6.12 to final by @rpardini in https://github.com/armbian/build/pull/7497
* rk3576: use boot_merger to generate idbloader.img by @amazingfate in https://github.com/armbian/build/pull/7500
* Add Rockchip u-boot "binman" BOOT_SCENARIO by @brentr in https://github.com/armbian/build/pull/7505
* Adjust build target statuses by @igorpecovnik in https://github.com/armbian/build/pull/7513
* Enable CONFIG_VHOST_VSOCK on rockchip64 by @halfa in https://github.com/armbian/build/pull/7512
* rockchip64-edge: enable rtw89 driver by @amazingfate in https://github.com/armbian/build/pull/7511
* shellfmt: no changes by @rpardini in https://github.com/armbian/build/pull/7510
* Retro* CM5: Enable display and touchscreen by @ginkage in https://github.com/armbian/build/pull/7506
* Add another paste server by @EvilOlaf in https://github.com/armbian/build/pull/7493
* rockchip64: rk3308 tidy up and rockpi-s fixes by @paolosabatino in https://github.com/armbian/build/pull/7519
* Reduce the size of the Rock S0 CMA to match Rock PI-S + include fixMACaddress script by @brentr in https://github.com/armbian/build/pull/7522
* Add new device Retroid Pocket RP5 and RPMini by @tjstyle in https://github.com/armbian/build/pull/7521
* nanopi-r6s: fix mmc0/mmc1 ordering by @efectn in https://github.com/armbian/build/pull/7528
* rockchip: bump edge kernel to 6.12 by @paolosabatino in https://github.com/armbian/build/pull/7526
* radxa-e20c - `WIREGUARD` is deprecated by @EvilOlaf in https://github.com/armbian/build/pull/7520
* rk35xx-vendor: bump to 6.1 rkr4.1 sdk kernel by @amazingfate in https://github.com/armbian/build/pull/7531
* extension: mesa-vpu: remove adding chromium ppa by @amazingfate in https://github.com/armbian/build/pull/7515
* hinlink-h88k: edge: add rfkill nodes to devicetree for m.2 wifi and b… by @amazingfate in https://github.com/armbian/build/pull/7516
* Add support for rk3588 based GenBook by @andyshrk in https://github.com/armbian/build/pull/7530
* build(deps): bump setuptools from 75.3.0 to 75.6.0 by @dependabot in https://github.com/armbian/build/pull/7518
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7508
* BananaPi BPI-CM4: `Enable i2c2 via overlay` by @pyavitz in https://github.com/armbian/build/pull/7540
* rockchip: various fixes (usb, alsa, ...) for rk3288/rk322x by @paolosabatino in https://github.com/armbian/build/pull/7539
* fix: add some patch to repair eMMC startup issues by @CodeChenL in https://github.com/armbian/build/pull/7538
* sm8250: bump current and edge to 6.12 by @amazingfate in https://github.com/armbian/build/pull/7532
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7534
* BigTreeTech CB2/Pi2 config by @JohnTheCoolingFan in https://github.com/armbian/build/pull/6860
* mixtile-edge2: bump vendor to `branch:rk-6.1-rkr4.1` by @rpardini in https://github.com/armbian/build/pull/7546
* feat: add ST7796 kernel module (fbtft) by @redrathnure in https://github.com/armbian/build/pull/7550
* fix: ST7796 kernel module patch by @redrathnure in https://github.com/armbian/build/pull/7552
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7545
* add community support for LonganPi 3H by @chainsx in https://github.com/armbian/build/pull/7547
* u-boot: check the produced `platform_install.sh` (created from functions like write_uboot_platform) for shellcheck errors by @rpardini in https://github.com/armbian/build/pull/7509
* bootscripts: Allwinner: Bugfix: Remove "allwinner/" from 3 boards configurations by @The-going in https://github.com/armbian/build/pull/7535
* Temporally disable BPI F3 as it has broken way of compiling u-boot by @igorpecovnik in https://github.com/armbian/build/pull/7557
* extensions: image-output-abl: set rootfs image larger for kde by @amazingfate in https://github.com/armbian/build/pull/7558
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7561
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7564
* Add missing deps for armbian-config by @dimitry-ishenko in https://github.com/armbian/build/pull/7562
* Improvements and Fixes for Youyeetoo R1 Board by @SuperKali in https://github.com/armbian/build/pull/7565
* Add Radxa Zero GPIO names to support libgpiod by @way5 in https://github.com/armbian/build/pull/7563
* H6xk boards: toggle to mainline kernel instead of vendor by @amazingfate in https://github.com/armbian/build/pull/7559
* Rpi: update RPi config - merge with upstream, rewrite patches by @igorpecovnik in https://github.com/armbian/build/pull/7569
* Bump VERSION by @EvilOlaf in https://github.com/armbian/build/pull/7571
* Keep old key management support for Focal and Bullseye by @igorpecovnik in https://github.com/armbian/build/pull/7524
* Feat add MKS-PI, SKIPR and few other boards  by @redrathnure in https://github.com/armbian/build/pull/7553
* rockchip64: rk3399 fix pcie being stuck at 1x width after a warm phy reset by @walmis in https://github.com/armbian/build/pull/7572
* Github Action fix for  newer build version ,make release tag configurable as action input  &  checkout build branch directly by @pykpkg47 in https://github.com/armbian/build/pull/7570
* Allwinner A10 DTS fix for ARM PMU IRQ and EMAC DMA by @Ryzer58 in https://github.com/armbian/build/pull/7567
* Revert "shellfmt: config/sources; no changes" by @The-going in https://github.com/armbian/build/pull/7554
* fix lvm extension and fs-cryptroot extension by @swissiety in https://github.com/armbian/build/pull/7527
* BananaPi BPI-M4-Zero: `Add overlay support and pin ctrl` by @pyavitz in https://github.com/armbian/build/pull/7568
* Repository management: disable broken and not needed functionality `Acquire-By-Hash` by @igorpecovnik in https://github.com/armbian/build/pull/7574
* Disable ROCKCHIP_THUNDER_BOOT_DEFER_FREE_MEMBLOCK by @nyanmisaka in https://github.com/armbian/build/pull/7580
* Add KERNEL_TEST_TARGET Variable to Rock-5B-Plus by @HeyMeco in https://github.com/armbian/build/pull/7582
* Update odroidxu4-current to 6.6.65 by @belegdol in https://github.com/armbian/build/pull/7578
* rockchip: remove mainlined patches by @paolosabatino in https://github.com/armbian/build/pull/7583
* meson64 kernels HDMI patch is obsolete by @way5 in https://github.com/armbian/build/pull/7579
* Starfive: fix broken patch due to kernel upgrade by @igorpecovnik in https://github.com/armbian/build/pull/7585
* Starfive: adjust kernel config and fix UART driver by @igorpecovnik in https://github.com/armbian/build/pull/7588
* avaota-a1: fix typo by @chainsx in https://github.com/armbian/build/pull/7589
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7573
* Fix BigTreetech CB1 tsc2007 ghost touches by @JohnTheCoolingFan in https://github.com/armbian/build/pull/7584
* Add neofetch to fastfetch alias by @JohnTheCoolingFan in https://github.com/armbian/build/pull/7575
* apt-utils: fix hard-coded GHPROXY_ADDRESS by @amazingfate in https://github.com/armbian/build/pull/7592
* sm8250: clean up patches for old version of kernel 6.9 and 6.10 by @amazingfate in https://github.com/armbian/build/pull/7591
* sunxi-6.6: Switch to v6.6.65, re-export patches by @The-going in https://github.com/armbian/build/pull/7587
* Add new TVBox aml-c400-plus: Magicsee C400 Plus by @jomadeto in https://github.com/armbian/build/pull/7581
* merge rockchip64 and rockchip-rk3588 by @amazingfate in https://github.com/armbian/build/pull/7566
* rk35xx-vendor: enable CONFIG_DRM_PANEL_MIPI_DBI by @amazingfate in https://github.com/armbian/build/pull/7597
* ghproxy: update GHPROXY_ADDRESS to ghgo.xyz by @amazingfate in https://github.com/armbian/build/pull/7596
* rk35xx-vendor: build DRM_PANEL_MIPI_DBI as builtin by @amazingfate in https://github.com/armbian/build/pull/7599
* coolpi-cm5: fix uboot patch dir by @amazingfate in https://github.com/armbian/build/pull/7600
* longanpi-4b: fix typo. by @chainsx in https://github.com/armbian/build/pull/7595
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7594
* rockchip64: revert rk3308 analog codec to vendor code by @paolosabatino in https://github.com/armbian/build/pull/7598
* Odroid XU4: remove deprecated patches by @igorpecovnik in https://github.com/armbian/build/pull/7609
* build(deps): bump actions/upload-artifact from 4.4.3 to 4.5.0 by @dependabot in https://github.com/armbian/build/pull/7605
* add community support for DShanPI-R1 by @chainsx in https://github.com/armbian/build/pull/7610
* Fix orangepizero wifi and usb otg by @ArendJan in https://github.com/armbian/build/pull/7614
* JetHome: update JetHub D2 support for current revision by @adeepn in https://github.com/armbian/build/pull/7611
* rootfs-to-image: preserve sparse files when moving artefacts to final destination with rsync by @alex3d in https://github.com/armbian/build/pull/7492
* Fix uwe5622 "spanning-writes" warning messages in dmesg by @paolosabatino in https://github.com/armbian/build/pull/7615
* hinlink-h88k: add spi lcd firmware to bsp package by @amazingfate in https://github.com/armbian/build/pull/7601
* Add support on Rock 5 ITX kernel edge and current by @SuperKali in https://github.com/armbian/build/pull/7618
* rockchip: enable 8189es kernel module by @paolosabatino in https://github.com/armbian/build/pull/7617
* build(deps): bump jinja2 from 3.1.4 to 3.1.5 by @dependabot in https://github.com/armbian/build/pull/7606
* sunxi-6.6: add NextThing C.H.I.P (PocketChip) initial support by @TheSnowfield in https://github.com/armbian/build/pull/7602
* fixed tinker-edge-r HDMI 4K display bug, bump to linux6.12 branch by @ARC-MX in https://github.com/armbian/build/pull/7608
* bump rockchip64 edge to 6.13 by @amazingfate in https://github.com/armbian/build/pull/7604
* rock-3a:add u-boot image for sata boot on m.2 e.key by @pykpkg47 in https://github.com/armbian/build/pull/7254
* sunxi/sunxi64: bump `edge` to 6.12 via copy by @The-going in https://github.com/armbian/build/pull/7577
* rockchip64 - egde - bump mainline to 6.13-rc5 by @EvilOlaf in https://github.com/armbian/build/pull/7626
* remove patches disabling sched_ext clean in tools for 6.12 and later kernels by @amazingfate in https://github.com/armbian/build/pull/7625
* armbian-kernel: enable BTF (and CO-RE) for all kernels by @rpardini in https://github.com/armbian/build/pull/7629
* kernel-config: switch to exporting defconfig's for all .config files by @rpardini in https://github.com/armbian/build/pull/7628
* thinkpad-x13s: bump to jhovold's wip/sc8280xp-6.13-rc4 by @rpardini in https://github.com/armbian/build/pull/7627
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7624
* Enable odroid-c4 i2c-0 by @janvolck in https://github.com/armbian/build/pull/7622
* don't ship qemu binary in rootfs cache + armhf image/rootfs building on non-armhf-capable-arm64 hosts (Apple M1+) by @rpardini in https://github.com/armbian/build/pull/7621
* cli: kernel-dtb: don't output preprocessed dts unless BOOT_FDT_FILE is in `<vendor>/<board>.dtb` format by @rpardini in https://github.com/armbian/build/pull/7620
* Bump oras-project/oras from 1.2.0 to 1.2.1 in `lib/functions/general/oci-oras.sh` by @github-actions in https://github.com/armbian/build/pull/7586
* RTW88: Add RTL88XXAU support to 6.12.y by @pyavitz in https://github.com/armbian/build/pull/7634
* Disable boards in Visionfive2 family as kernel compilation breaks by @igorpecovnik in https://github.com/armbian/build/pull/7636
* Update linux-uefi-arm64-edge.config by @bmilde in https://github.com/armbian/build/pull/7635
* rockchip: bump current kernel to 6.12 and edge to 6.13 by @paolosabatino in https://github.com/armbian/build/pull/7633
* riscv64: enable support in Debian Trixie, enable UEFI grub by @igorpecovnik in https://github.com/armbian/build/pull/7632
* Debian SID: drop broken package by @igorpecovnik in https://github.com/armbian/build/pull/7630
* BananaPi BPI-F3: `Update kernel to 6.6.y and other fixups` by @pyavitz in https://github.com/armbian/build/pull/7616
* rootfs: fix: don't try to use chroot binaries after qemu was undeployed by @rpardini in https://github.com/armbian/build/pull/7638
* rockchip64-6.13: add missing patch to fix rk356x pcie2 for rc5 by @amazingfate in https://github.com/armbian/build/pull/7640
* rockchip64-6.13: fix mbox formatting of `rk356x-fix-pcie2-reset.patch` by @rpardini in https://github.com/armbian/build/pull/7645
* cli-docker: avoid `argument list too long` errors when too many git changes present; fixes #6993 by @rpardini in https://github.com/armbian/build/pull/7644
* runners: fix `if_error_find_files_sdcard` if looking for full paths (shows DKMS log correctly) by @rpardini in https://github.com/armbian/build/pull/7653
* fix typo by @marcone in https://github.com/armbian/build/pull/7649
* rewrite all kernel patches and configs by @rpardini in https://github.com/armbian/build/pull/7651
* add hdmi rx configuration for friendlyelec cm3588 by @timsurber in https://github.com/armbian/build/pull/7648
* v4l2loopback-dkms: do not restrict to desktops only by @rpardini in https://github.com/armbian/build/pull/7655
* kernel-debs: headers: postinst: switch from `oldconfig` to `olddefconfig` for less messy output; better logging by @rpardini in https://github.com/armbian/build/pull/7654
* add typec role switch and pd negotiation support to oneplus 8T by @amazingfate in https://github.com/armbian/build/pull/7657
* `rock-s0` / `rockpi-s`: quote board vars by @rpardini in https://github.com/armbian/build/pull/7650
* Bump arm-trusted-firmware to 2.12 for rockchip64 by @timsurber in https://github.com/armbian/build/pull/7646
* uboot: completely clean before building each target; slower but correct by @rpardini in https://github.com/armbian/build/pull/7659
* rpi5b: drop `LINUXFAMILY=bcm2712` as it is exactly the same as `bcm2711` by @rpardini in https://github.com/armbian/build/pull/7642
* `rk35xx`/`legacy`: rewrite-kernel-patches & rewrite-kernel-config, no changes by @rpardini in https://github.com/armbian/build/pull/7658
* Add Sweet Potato to xorg conf in family config by @Tonymac32 in https://github.com/armbian/build/pull/7668
* Bump setuptools from 75.6.0 to 75.7.0 by @dependabot in https://github.com/armbian/build/pull/7665
* Bump gitpython from 3.1.43 to 3.1.44 by @dependabot in https://github.com/armbian/build/pull/7664
* Sm8250: build abl boot recovery image by @amazingfate in https://github.com/armbian/build/pull/7663
* nanopct6(-lts): edge: bump u-boot to 2025.01-rc6; enable UMS and fix non-LTS dtsi by @rpardini in https://github.com/armbian/build/pull/7662
* RPi CM5: Enable DWC2 host mode support by default by @AaronDewes in https://github.com/armbian/build/pull/7660
* nanopi-m6: add support for SPI flash boot by @efectn in https://github.com/armbian/build/pull/7652
* sunxi-6.6: NextThing C.H.I.P (PocketChip) community support by @TheSnowfield in https://github.com/armbian/build/pull/7647
* cm3588-nas: u-boot: 2025.01-rc6 with working UMS by @rpardini in https://github.com/armbian/build/pull/7667
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7669
* nanopct6(-lts): u-boot: edge: bump to 2025.01 final by @rpardini in https://github.com/armbian/build/pull/7670
* cm3588-nas: u-boot: bump to 2025.01 final by @rpardini in https://github.com/armbian/build/pull/7671
* Orange Pi Zero: Fix usb otg after 6.12 update by @ArendJan in https://github.com/armbian/build/pull/7661
* xiaomi-elish: fix bsp package build by @amazingfate in https://github.com/armbian/build/pull/7674
* PocketChip: removing patch also from series by @igorpecovnik in https://github.com/armbian/build/pull/7673
* BananaPi BPI-M4-Zero: REV1 uart1 support via overlay by @pyavitz in https://github.com/armbian/build/pull/7672
* K3: Use sfdisk instead of parted for setting flag in boot partition by @3V3RYONE in https://github.com/armbian/build/pull/7677
* Partition process: fix handling loop devices by @igorpecovnik in https://github.com/armbian/build/pull/7679
* AIC wifi and v4l2 extensions: disable them for kernel 6.12 and higher by @igorpecovnik in https://github.com/armbian/build/pull/7680
* UEFI-arm64: disable broken Phytium network driver patch by @igorpecovnik in https://github.com/armbian/build/pull/7684
* BananaPi BPI-F3: `Update to linux-6.6.70 & overclock to 1.8GHz` by @pyavitz in https://github.com/armbian/build/pull/7685
* rockchip64: fix rkvenc dtbo build by @amazingfate in https://github.com/armbian/build/pull/7689
* rockpro64: u-boot: bump to 2025.01 by @rpardini in https://github.com/armbian/build/pull/7688
* odroidm1: u-boot: bump to 2025.01; kernel: add nodes for overlays by @rpardini in https://github.com/armbian/build/pull/7686
* rockchip64-6.13: NanoPi R6C/R6S SD card detect patch by @rpardini in https://github.com/armbian/build/pull/7681
* sunxi 6.12: Switch to v6.12.9 by @The-going in https://github.com/armbian/build/pull/7691
* sunxi-6.6: Switch to v6.6.70 by @The-going in https://github.com/armbian/build/pull/7690
* armbian-install UEFI: EFI partition generation, hiding non Linux partitions by @igorpecovnik in https://github.com/armbian/build/pull/7631
* RaspberryPi BCM2711: `Enable FW_LOADER_COMPRESS support` by @pyavitz in https://github.com/armbian/build/pull/7694
* Firstlogin: run provision script if it does exists by @igorpecovnik in https://github.com/armbian/build/pull/7696
* update rtl8822cs driver link to latest commit (update for kernel 6.13+) by @adeepn in https://github.com/armbian/build/pull/7699
* not enable BTF for rk35xx vendor kernel by @amazingfate in https://github.com/armbian/build/pull/7697
* ghproxy: update GHPROXY_ADDRESS to ghfast.top by @amazingfate in https://github.com/armbian/build/pull/7702
* dockerproxy: update GHCR_MIRROR_ADDRESS by @amazingfate in https://github.com/armbian/build/pull/7713
* BananaPI BPI-F3: `Pull branch instead of commit` by @pyavitz in https://github.com/armbian/build/pull/7722
* Nanopi R5S: proper pci phy reset - fixing missing LAN1 by @lanefu in https://github.com/armbian/build/pull/7721
* Bump uboot to youyeetoo r1 v3 to the next release by @SuperKali in https://github.com/armbian/build/pull/7720
* hooks: introduce `post_armbian_repo_customize_image` and `post_repo_customize_image` by @rpardini in https://github.com/armbian/build/pull/7719
* Family Visionfive: seems unmaintained, disabling targets by @igorpecovnik in https://github.com/armbian/build/pull/7718
* UEFI kernels, legacy = 6.6, current 6.12 & edge 6.13 by @igorpecovnik in https://github.com/armbian/build/pull/7717
* WIP sunxi 6.6: Cleaning up the patches before the changes. Swith to v6.6.72 by @The-going in https://github.com/armbian/build/pull/7714
* enable current kernel for hinlink-h6xk boards by @amazingfate in https://github.com/armbian/build/pull/7711
* MBa8MPxL: update linux-tqma-current to 6.12 by @schmiedelm in https://github.com/armbian/build/pull/7704
* build(deps): bump actions/upload-artifact from 4.5.0 to 4.6.0 by @dependabot in https://github.com/armbian/build/pull/7700
* 3rd party wifi: partially revert rtl8811cu driver as it breaks on K6.6 by @igorpecovnik in https://github.com/armbian/build/pull/7723
* Macchiatobin: move board to eos so we don't build this family kernel anymore by @igorpecovnik in https://github.com/armbian/build/pull/7724
* Refactor armbian-config into install as external package by @igorpecovnik in https://github.com/armbian/build/pull/7716
* meson: remove tag defined in KERNELBRANCH for 6.6 mainline kernel by @amazingfate in https://github.com/armbian/build/pull/7712
* coolpi-genbook: bump u-boot to 2025.01 by @andyshrk in https://github.com/armbian/build/pull/7734
* Moving Odroid C1 and OneCloud to EOS since kernel is not assembling anymore by @igorpecovnik in https://github.com/armbian/build/pull/7733
* Rk35xx btf back by @amazingfate in https://github.com/armbian/build/pull/7732
* kernel: call oldconfig _after_ kernel config hooks; add hook for `CONFIG_CFG80211=m` and `CONFIG_MAC80211=m` on 6.13+ by @rpardini in https://github.com/armbian/build/pull/7728
* mainline-kernel.conf.sh: bump 6.13 to final by @rpardini in https://github.com/armbian/build/pull/7726
* git: squash spurious warning when checking safe.directory by @rpardini in https://github.com/armbian/build/pull/7725
* actions(update-tools): avoid notifying our outdated deps everywhere by @akinomyoga in https://github.com/armbian/build/pull/7709
* meson64: current 6.6 -> 6.12; edge 6.12 -> 6.13 by @rpardini in https://github.com/armbian/build/pull/7727
* Bump oras-project/oras from 1.2.1 to 1.2.2 in `lib/functions/general/oci-oras.sh` by @github-actions in https://github.com/armbian/build/pull/7707
* Bump sharkdp/bat from 0.24.0 to 0.25.0 in `lib/functions/general/bat-cat.sh` by @github-actions in https://github.com/armbian/build/pull/7706
* build(deps): bump setuptools from 75.7.0 to 75.8.0 by @dependabot in https://github.com/armbian/build/pull/7701
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7735
* wireless: fix build with kernel 6.13 by @amazingfate in https://github.com/armbian/build/pull/7736
* wifi drivers: update commit id of rtl8811cu and rtl88x2bu by @amazingfate in https://github.com/armbian/build/pull/7737
* disable ccache in a friendly way by @lanefu in https://github.com/armbian/build/pull/7730
* fix cpu internal ethernet on nanopi-r4se standard version without EEPROM by @jpy794 in https://github.com/armbian/build/pull/7739
* Add upstream release as csc target: Ubuntu plucky 25.04, Oracular to EOS by @igorpecovnik in https://github.com/armbian/build/pull/7738
* Ubuntu Plucky: disable missing packages by @igorpecovnik in https://github.com/armbian/build/pull/7740
* nanopi-r6s: u-boot: bump to 2025.01 final, with working UMS and SD -> NVMe -> eMMC boot order by @rpardini in https://github.com/armbian/build/pull/7683
* nanopi-r6c: u-boot: bump to 2025.01 final, with working UMS and SD -> NVMe -> eMMC boot order by @rpardini in https://github.com/armbian/build/pull/7682
* Ubuntu Plucky: fixing remaining problem. by @igorpecovnik in https://github.com/armbian/build/pull/7741
* Update Odin2 Config by @FantasyGmm in https://github.com/armbian/build/pull/7742
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7743
* BigTreeTech CB1 patches adjustments by @JohnTheCoolingFan in https://github.com/armbian/build/pull/7745
* h96max-v56: u-boot: bump to 2025.01 by @hqnicolas in https://github.com/armbian/build/pull/7746
* Rockpi-S: enable automatic u-boot flashing upon package install by @igorpecovnik in https://github.com/armbian/build/pull/7750
* thinkpad-x13s: bump to jhovold's wip/sc8280xp-6.13 final by @rpardini in https://github.com/armbian/build/pull/7749
* Limit curl execution time to 2s to find WAN IP by @WiseLord in https://github.com/armbian/build/pull/7755
* MBa8MPxL: cleanup board configs by @schmiedelm in https://github.com/armbian/build/pull/7751
* Switch linux-rockchip to from rkr4.1 to rkr5 by @HeyMeco in https://github.com/armbian/build/pull/7758
* TI K3 updates by @glneo in https://github.com/armbian/build/pull/7762
* nanopc t4: fix sdram unstable by @msdos03 in https://github.com/armbian/build/pull/7761
* MBa8MPxL: cleanup fix X11 settings by @schmiedelm in https://github.com/armbian/build/pull/7759
* aml-c400-plus: Remove duplicated code present in meson-gx-p23x-q20x.dtsi by @jomadeto in https://github.com/armbian/build/pull/7760
* Add support for NanoPi R3S by @EvilOlaf in https://github.com/armbian/build/pull/7556
* nanopi-m6: add support for edge, current kernels by @efectn in https://github.com/armbian/build/pull/7763
* helios64: restore hs400 support after enabling strobe line internal p… by @prahal in https://github.com/armbian/build/pull/7756
* sm8250-current: enable CONFIG_USB_SERIAL_CH341 by @amazingfate in https://github.com/armbian/build/pull/7764
* Add missing firmware package for build-in driver cfg80211 by @igorpecovnik in https://github.com/armbian/build/pull/7766
* nanopct6(-lts): bump u-boot to 2025.04-rc1 by @rpardini in https://github.com/armbian/build/pull/7774
* rock-3a: bump `edge` u-boot to 2025.01 by @EvilOlaf in https://github.com/armbian/build/pull/7770
* helios64: fix helios64-heartbeat-led.service by @prahal in https://github.com/armbian/build/pull/7765
* BananaPI BPI-F3: `Update DTS and Defconfig` by @pyavitz in https://github.com/armbian/build/pull/7773
* BananaPi BPI-F3: `patch fail fixup` by @pyavitz in https://github.com/armbian/build/pull/7777
* Mesa VPU: allow package downgrading at apt upgrade by @igorpecovnik in https://github.com/armbian/build/pull/7778
* mesa-vpu: only add kisak ppa for jammy by @amazingfate in https://github.com/armbian/build/pull/7779
* BananaPi BPI-F3: U-Boot: `Update to tag k1-bl-v2.1-release` by @pyavitz in https://github.com/armbian/build/pull/7780
* Add support for MKS-KLIPAD50 by @torte71 in https://github.com/armbian/build/pull/7771
* nanopi-r3s: add support for `current` by @EvilOlaf in https://github.com/armbian/build/pull/7768
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7781
* feat: Use deb822 APT source for armbian-config by @blieque in https://github.com/armbian/build/pull/7782
* Armbian-config sources lists - remove double quotes from EOT by @igorpecovnik in https://github.com/armbian/build/pull/7785
* Rock-S0: enable automatic u-boot flashing upon package install by @brentr in https://github.com/armbian/build/pull/7784
* rockchip/64: fix pl330 cyclic dma transfers by @paolosabatino in https://github.com/armbian/build/pull/7695
* imx6: move current to 6.12.y by @igorpecovnik in https://github.com/armbian/build/pull/7786
* BananaPi CM4/M2S: `Update u-boot to v2025.01` by @pyavitz in https://github.com/armbian/build/pull/7788
* Amper Gateway AM-GZ80x: `Update u-boot to v2025.01` by @pyavitz in https://github.com/armbian/build/pull/7789
* IMX8: switch u-boot sources to last known working commit  by @igorpecovnik in https://github.com/armbian/build/pull/7793
* rockchip: fix tinkerboard out-of-the-box pulseaudio configuration by @paolosabatino in https://github.com/armbian/build/pull/7796
* Update rock-5c.conf - add KERNEL_TEST_TARGET by @schwar3kat in https://github.com/armbian/build/pull/7799
* Revert commit that breaks compilation by @igorpecovnik in https://github.com/armbian/build/pull/7804
* firstlogin: bring up wifi device before scanning by @torte71 in https://github.com/armbian/build/pull/7803
* Update odroidxu4-current to 6.6.75 by @belegdol in https://github.com/armbian/build/pull/7787
* Add board config for MXQ TV box by @domin144 in https://github.com/armbian/build/pull/7501
* meson: kernel update: legacy -> 6.6, current -> 6.12 by @domin144 in https://github.com/armbian/build/pull/7801
* UX / cosmetics: MOTD ip display needs some limiting by @igorpecovnik in https://github.com/armbian/build/pull/7798
* Fix orangepi 3b audio jack boot download 'button' by @ArendJan in https://github.com/armbian/build/pull/7794
* hinlink-h88k: fix usb dr_mode by @qbisi in https://github.com/armbian/build/pull/7797
* armbian-kernel.sh: introduce `KERNEL_BTF=no` to opt-out of BTF/CO-RE type-info on low-RAM machines by @rpardini in https://github.com/armbian/build/pull/7675
* nanopi-r3s: set `HAS_VIDEO_OUTPUT` by @EvilOlaf in https://github.com/armbian/build/pull/7810
* extensions: fix outdated ghproxy mirror address by @amazingfate in https://github.com/armbian/build/pull/7816
* `Automatic` board configs status synchronise by @github-actions in https://github.com/armbian/build/pull/7806
* Chore mkspi cli only images by @redrathnure in https://github.com/armbian/build/pull/7809
* mksklipad50: Build only CLI images by @torte71 in https://github.com/armbian/build/pull/7807
* Meson: drop (long) broken legacy code which is also breaking CI by @igorpecovnik in https://github.com/armbian/build/pull/7808
* rockchip64: disable pl330 patch due to pulseaudio issues by @paolosabatino in https://github.com/armbian/build/pull/7813
* build(deps): bump dtschema from 2024.11 to 2025.2 by @dependabot in https://github.com/armbian/build/pull/7818
* MBa8MPxL update uboot patch and fix firmware installation by @schmiedelm in https://github.com/armbian/build/pull/7817
* Bugfix: Remove directories from sha files by @igorpecovnik in https://github.com/armbian/build/pull/7814
* Bump radxa rk35xx uboot to next-dev-v2024.10 by @amazingfate in https://github.com/armbian/build/pull/7776
* Radxa uboot 202410 fix by @amazingfate in https://github.com/armbian/build/pull/7819
* Cosmetical: switch edge and current kernel order by @igorpecovnik in https://github.com/armbian/build/pull/7821
* Revert "fxblox-rk1: add missing patch for latest radxa uboot" by @amazingfate in https://github.com/armbian/build/pull/7822
* Odroid XU4: disable BTF as it crashes kernel load by @igorpecovnik in https://github.com/armbian/build/pull/7824
* Revert "imx6: move current to 6.12.y" by @igorpecovnik in https://github.com/armbian/build/pull/7825
* rockchip64: remove patch to fix rockpi-e gigabit eth by @paolosabatino in https://github.com/armbian/build/pull/7823
* Radxa Zero, fix for overlay prefix name by @way5 in https://github.com/armbian/build/pull/7826
* BananaPi BPI-F3: `General update to improve overall support` by @pyavitz in https://github.com/armbian/build/pull/7833
* add spi flash overlay for NanoPi M6 edge, current kernels by @efectn in https://github.com/armbian/build/pull/7837
* Bump two leftover radxa rk35xx uboot to next-dev-v2024.10 by @nyanmisaka in https://github.com/armbian/build/pull/7832
* Odroid M2: initial support by @mlegenovic in https://github.com/armbian/build/pull/7828
* remove software-properties-common/gtk for trixie and sid by @amazingfate in https://github.com/armbian/build/pull/7827
* Add Support for Rock 5T by @HeyMeco in https://github.com/armbian/build/pull/7841
* rockchip64: fix rocks0 patch breaking current compilation by @paolosabatino in https://github.com/armbian/build/pull/7815
* Orangepi 5 MAX -  add support for `current` by @EvilOlaf in https://github.com/armbian/build/pull/7842
* mesa-vpu: add chromium back for debian and noble by @amazingfate in https://github.com/armbian/build/pull/7839
* Ubuntu Plucky: add architecture dependent packages by @igorpecovnik in https://github.com/armbian/build/pull/7847
* Magicsee C400-Plus: Switch to standard support by @jomadeto in https://github.com/armbian/build/pull/7846
* RPi family: read board name from DT and bump CURRENT to 6.12.y by @igorpecovnik in https://github.com/armbian/build/pull/7845
* station-p2: delete the redundant function. by @chainsx in https://github.com/armbian/build/pull/7844
* station-m2: delete the redundant function. by @chainsx in https://github.com/armbian/build/pull/7843
* Hinlink-h88k: some fix to dts by @qbisi in https://github.com/armbian/build/pull/7840
* Add support for Rock 2A and 2F by @CodeChenL in https://github.com/armbian/build/pull/7820
* ssv6051 and panel-dsi-simple driver patch for kernel 6.6, 6.9, 6.12 and 6.13 by @qbisi in https://github.com/armbian/build/pull/7795
* odroidm1: u-boot: enable `setexpr`; patch 2025.01 for `fileenv`; enable squashfs support by @rpardini in https://github.com/armbian/build/pull/7769
* Bump VERSION by @EvilOlaf in https://github.com/armbian/build/pull/7791
* Raspberry PI: move EDGE kernel from 6.14 to 6.13 as it doesn't build by @igorpecovnik in https://github.com/armbian/build/pull/7848
* Plucky: drop non existing packages by @igorpecovnik in https://github.com/armbian/build/pull/7849
* station-m2: use mainline devicetree name by @chainsx in https://github.com/armbian/build/pull/7858
* MKS-Klipad50: Switch to standard support by @torte71 in https://github.com/armbian/build/pull/7851
* SM8250: drop upstreamed patch as it breaks compilation by @igorpecovnik in https://github.com/armbian/build/pull/7860
* kernel: fix for 6.14 make clean fail at tools dir due to upstream dir change by @amazingfate in https://github.com/armbian/build/pull/7850
* export-logs: use multiple paste servers in order until one works by @rpardini in https://github.com/armbian/build/pull/7861
* sun55iw3-syterkit: update kernel config by @chainsx in https://github.com/armbian/build/pull/7855
* rockchip64-6.6/6.12/6.13: rk3308b: add vop and internal rgb lcdc output by @TheSnowfield in https://github.com/armbian/build/pull/7866
* sunxi-6.6: Switch to v6.6.75. Add BananaPi M4 Berry board as WIP by @The-going in https://github.com/armbian/build/pull/7865
* Bump Vim1-2 u-boot binaries (stopgap) by @Tonymac32 in https://github.com/armbian/build/pull/7871
* BananaPi BPI-F3: `BOARD_MAINTAINER="pyavitz"` by @pyavitz in https://github.com/armbian/build/pull/7870
* rockchip64:loaderimage: fix rk3308 uboot loader offset by @TheSnowfield in https://github.com/armbian/build/pull/7867
* rockchip64: fix wrong GPIO direction in DP virtual extcon driver by @retro98boy in https://github.com/armbian/build/pull/7857
* rockchip/64: fix again periodic dma and audio stuttering by @paolosabatino in https://github.com/armbian/build/pull/7853
* small cleanup Meson64 by @Tonymac32 in https://github.com/armbian/build/pull/7868
* rockchip64: RK3588 update DDR & BL31 blobs by @HeyMeco in https://github.com/armbian/build/pull/7872
* generate_CODEOWNERS.sh: fix issues and support BOOTPATCHDIR and ATFPATCHDIR by @hzyitc in https://github.com/armbian/build/pull/7869
* Move Meson GX to LibreElec FIP by @Tonymac32 in https://github.com/armbian/build/pull/7875
* arm64: dts: rockchip: fix gpio-line-names to radxa-rock-3a by @EvilOlaf in https://github.com/armbian/build/pull/7874
* python3: do not rely on hostdeps python3-pip nor python3-dev; deploy pip via get-pip.py by @rpardini in https://github.com/armbian/build/pull/7873
* Status changes: csc to conf and vice versa by @igorpecovnik in https://github.com/armbian/build/pull/7854
* feat: Use deb822 APT sources by @blieque in https://github.com/armbian/build/pull/7790

## v24.11.1 (2024-11-28)

* `6.1-rkr3`: sync FriendlyElec's DTs from vendor (common, R6S, R6C, T6, CM3588) + add T6-LTS DT by @rpardini in https://github.com/armbian/linux-rockchip/pull/209
* A collection of fixes and new drivers for the Retro*CM5 devices by @ginkage in https://github.com/armbian/linux-rockchip/pull/267
* Add a label "not armbian-config" bug by @igorpecovnik in https://github.com/armbian/configng/pull/245
* Add a warning when tool runs with outdated BSP package by @igorpecovnik in https://github.com/armbian/configng/pull/254
* Add BananaPi `BPI-M4-Zero` updates, fixups and rev2 support by @pyavitz in https://github.com/armbian/build/pull/7317
* add board mekotronics r57 rk3576 by @monkaBlyat in https://github.com/armbian/linux-rockchip/pull/257
* Add community support for Cyber Aib RK3588 by @chainsx in https://github.com/armbian/build/pull/7404
* Add community support for Rock5B+ by @HeyMeco in https://github.com/armbian/build/pull/7445
* Add contribute information to the About app and show it on the exit by @igorpecovnik in https://github.com/armbian/configng/pull/189
* Add dedicated CONTRIBUTION.md and adjust README.md by @igorpecovnik in https://github.com/armbian/configng/pull/220
* Added device tree overlays files for armsom-sige7 board:two OV13850 c… by @itlhd in https://github.com/armbian/linux-rockchip/pull/244
* Added support of core3566 by @btbxbob in https://github.com/armbian/build/pull/7018
* Add hexagonrpc service to xiaomi-elish by @amazingfate in https://github.com/armbian/build/pull/7394
* Adding missing udev audio rules for NanoPC T6 & LTS by @SuperKali in https://github.com/armbian/build/pull/7323
* Adding OVERLAYDIR variable to hash calculating mechanisms by @igorpecovnik in https://github.com/armbian/build/pull/7256
* Adding USB ports on Youyeetoo R1 v3 by @SuperKali in https://github.com/armbian/linux-rockchip/pull/227
* Adding Youyeetoo R1 v3 on current & edge kernel by @SuperKali in https://github.com/armbian/build/pull/7173
* add itc type to hdmirx by @benhoff in https://github.com/armbian/linux-rockchip/pull/262
* Additional cosmetic fixes to MOTD by @igorpecovnik in https://github.com/armbian/build/pull/7306
* Add JSON generation to the docs generation by @igorpecovnik in https://github.com/armbian/configng/pull/194
* Add link to adding new feature by @igorpecovnik in https://github.com/armbian/configng/pull/257
* Add missing node for youyeetoo r1 on current kernel by @SuperKali in https://github.com/armbian/build/pull/7472
* add new board armsom-cm5-io by @amazingfate in https://github.com/armbian/build/pull/7211
* add new board armsom-cm5-rpi-cm4-io by @amazingfate in https://github.com/armbian/build/pull/7436
* add new board armsom-sige3 by @amazingfate in https://github.com/armbian/build/pull/7196
* add new board orangepi5 max by @amazingfate in https://github.com/armbian/build/pull/7262
* Add new device OnePlus 8T by @amazingfate in https://github.com/armbian/build/pull/7386
* Add ok3568-c by @amazingfate in https://github.com/armbian/linux-rockchip/pull/273
* Add Radxa E20C board by @mattx433 in https://github.com/armbian/build/pull/7157
* Add Radxa Rock5B+ device tree by @HeyMeco in https://github.com/armbian/linux-rockchip/pull/277
* Add repository list to the Debian package by @igorpecovnik in https://github.com/armbian/configng/pull/261
* Add reserved-memory node for hdmirx-controller on Youyeetoo R1 v3 by @SuperKali in https://github.com/armbian/linux-rockchip/pull/241
* Add software package: Pi-hole DNS blocker by @igorpecovnik in https://github.com/armbian/configng/pull/238
* Add `sun50i-h616-light` dt overlay fix to 6.10 by @JohnTheCoolingFan in https://github.com/armbian/build/pull/7204
* Add support for changing / spoofing MAC address by @igorpecovnik in https://github.com/armbian/configng/pull/191
* Add support for dln2 in orangepi zero and orangepi zero 3 by @MrSuicideParrot in https://github.com/armbian/build/pull/7336
* Add support for NanoPi M6 by @efectn in https://github.com/armbian/build/pull/7341
* Add support for Radxa CM5 on RPi CM4 IO by @AaronDewes in https://github.com/armbian/build/pull/7470
* Add support for Retro Lite CM5 device by @ginkage in https://github.com/armbian/linux-rockchip/pull/211
* Add support for webp images and fix path for them by @igorpecovnik in https://github.com/armbian/configng/pull/197
* Add timeout on check wan address on motd by @SuperKali in https://github.com/armbian/build/pull/7297
* add: -t "test" and -p "production" option to json assembiling by @Tearran in https://github.com/armbian/configng/pull/202
* Add TV Box Magicsee C400 Plus Linux support by @jomadeto in https://github.com/armbian/build/pull/7469
* Adjust patches due to kernel bump by @igorpecovnik in https://github.com/armbian/build/pull/7316
* Align KERNEL_TARGET_TEST from edge to vendor for Youyeetoo R1 board by @SuperKali in https://github.com/armbian/build/pull/7222
* arch: arm64: add new board armsom-sige3 by @amazingfate in https://github.com/armbian/linux-rockchip/pull/236
* arch: arm64 board: armsom sige5 add Display 10 HD by @itlhd in https://github.com/armbian/linux-rockchip/pull/233
* arch: arm64: dts: add board orangepi5 max by @amazingfate in https://github.com/armbian/linux-rockchip/pull/240
* arch: arm64: dts: delete ufs nodes from armsom cm5-io by @amazingfate in https://github.com/armbian/linux-rockchip/pull/278
* arch: arm64: dts: fix armsom sige1 sd card boot by @amazingfate in https://github.com/armbian/linux-rockchip/pull/218
* arch: arm64: dts: fix sdio wifi clk for armsom-sige1 by @amazingfate in https://github.com/armbian/linux-rockchip/pull/239
* arch: arm64: dts: rework devicetree of armsom-sige7 by @amazingfate in https://github.com/armbian/linux-rockchip/pull/222
* arch: arm64: rockchip: use panfrost driver for gpu of rk3576 by @amazingfate in https://github.com/armbian/linux-rockchip/pull/249
* arm64: dts:  Add DTS for Cyber Aib RK3588 device by @chainsx in https://github.com/armbian/linux-rockchip/pull/268
* arm64: dts: DTS for Luckfox Core3566 by @buldo in https://github.com/armbian/linux-rockchip/pull/254
* arm64: dts: rk3566-orangepi-3b-v2.1: Rework USB fix by @dust-7 in https://github.com/armbian/linux-rockchip/pull/256
* arm64: dts: rk3568-mixtile-edge2: add Mixtile Edge 2 by @rpardini in https://github.com/armbian/linux-rockchip/pull/245
* arm64: dts: rk3588-blade3-v101-linux: fixes by @rpardini in https://github.com/armbian/linux-rockchip/pull/251
* arm64: dts: rock-3a:  add overlay to enable sata on m.2 e-key slot by @pykpkg47 in https://github.com/armbian/linux-rockchip/pull/237
* arm64: dts:  rock 3a  add spi flash, disable rk809 rtc and enable rockchip crypto device by @pykpkg47 in https://github.com/armbian/linux-rockchip/pull/235
* arm64: dts: rockchip: add armsom-aim7-io by @amazingfate in https://github.com/armbian/linux-rockchip/pull/214
* arm64: dts: rockchip: add armsom-cm5-io by @amazingfate in https://github.com/armbian/linux-rockchip/pull/215
* arm64: dts: rockchip: add armsom-sige5 by @amazingfate in https://github.com/armbian/linux-rockchip/pull/212
* arm64: dts: rockchip: Add Orange Pi 3B v2.1 by @dust-7 in https://github.com/armbian/linux-rockchip/pull/234
* arm64: dts: rockchip: add radxa-e20c by @mattx433 in https://github.com/armbian/linux-rockchip/pull/231
* arm64: dts: rockchip: add support for NanoPi M6 by @efectn in https://github.com/armbian/linux-rockchip/pull/258
* arm64: dts: rockchip: Adopt mainline naming for Friendlyelec CM3588 NAS by @ColorfulRhino in https://github.com/armbian/linux-rockchip/pull/220
* arm64: dts: rockchip: fix gmac PHY attach error on ROCK Pi E by @RadxaNaoki in https://github.com/armbian/build/pull/7202
* arm64: rockchip: add YX35 LCD overlays for NanoPi M6 by @efectn in https://github.com/armbian/linux-rockchip/pull/259
* armbian-bsp-cli-deb: fix shellcheck breakage; fixes #7303 by @rpardini in https://github.com/armbian/build/pull/7321
* armbian-firstrun: Optionally skip OpenSSH host key regeneration by @davidandreoletti in https://github.com/armbian/build/pull/7216
* armbian-led-state: avoid binary parameters, other minor cleanups by @paolosabatino in https://github.com/armbian/build/pull/7337
* armbianmonitor: call `curl` with `--fail` flag so server 400/500 errors actually trigger a retry by @rpardini in https://github.com/armbian/build/pull/7487
* Armsom cm5 rpi cm4 io by @itlhd in https://github.com/armbian/linux-rockchip/pull/281
* armsom-sige5: update uboot from latest SDK by @amazingfate in https://github.com/armbian/build/pull/7132
* armsom-w3: fix m.2 usb bluetooth by @amazingfate in https://github.com/armbian/build/pull/7274
* avaota-a1: move to .csc support by @chainsx in https://github.com/armbian/build/pull/7395
* BananaPi BPI-M4-Zero: `Fixup U-Boot and Linux DTS/DTSI and add WiFi / BT overlay` by @pyavitz in https://github.com/armbian/build/pull/7332
* BananaPi BPI-M4-Zero: `Improve support` by @pyavitz in https://github.com/armbian/build/pull/7355
* BananaPi CM4: `improve SDIO WiFi speeds` by @pyavitz in https://github.com/armbian/build/pull/7193
* Bananapi M2 pro: move to most recent boot loader by @igorpecovnik in https://github.com/armbian/build/pull/7491
* Board: NanoPC T6 & LTS - Bump uboot from 2024.07 to 2024.10 mainline by @SuperKali in https://github.com/armbian/build/pull/7393
* board: NanoPi R6C and R6S: Bump U-Boot from 2024.07 to 2024.10 by @ColorfulRhino in https://github.com/armbian/build/pull/7371
* board: orangepi3b: Fix U-Boot `BOOTPATCHDIR` and bump to 2024.10 by @ColorfulRhino in https://github.com/armbian/build/pull/7377
* boogie's vop2 rbga2101010 capability fix (6.1-rkr3 adapted version) by @rpardini in https://github.com/armbian/linux-rockchip/pull/252
* bootscript: sunxi: Add a dtb file path analyzer by @The-going in https://github.com/armbian/build/pull/7484
* BSP: Expand distribution status with possible upgrade information by @igorpecovnik in https://github.com/armbian/build/pull/7303
* BSP: store kernel and kernel test target definition  by @igorpecovnik in https://github.com/armbian/build/pull/7279
* BSP: store overlay folder definition to /etc/armbian-release to be used in armbian-config by @igorpecovnik in https://github.com/armbian/build/pull/7198
* Bugfix: add missing character from character manipulation by @igorpecovnik in https://github.com/armbian/configng/pull/227
* Bugfix: BigTreeTech CB1 patches and edge dts by @JohnTheCoolingFan in https://github.com/armbian/build/pull/7159
* Bugfix: patch writing style caused breakage by @igorpecovnik in https://github.com/armbian/build/pull/7417
* Bugfix: put repository list into correct folder by @igorpecovnik in https://github.com/armbian/configng/pull/262
* Bugfix: resolve boot loader compilation issues on X96-mate and Orangepizero2 by @igorpecovnik in https://github.com/armbian/build/pull/7281
* Bugfix: sunxi-6.6: fix inapplicable and Re-export patches, switch to v6.6.54 by @The-going in https://github.com/armbian/build/pull/7358
* Bugfix: u-boot changes for x96q broke most of other Allwinner uboot compilation by @igorpecovnik in https://github.com/armbian/build/pull/7280
* Bugfix: we can't fully disable desktop due to automation by @igorpecovnik in https://github.com/armbian/configng/pull/232
* Bugfix: xradio wireless stopped working if those files were removed. by @igorpecovnik in https://github.com/armbian/build/pull/7292
* [bug] Need at least one enabled sub by @Tearran in https://github.com/armbian/configng/pull/260
* Bump mvdan/sh from 3.8.0 to 3.9.0 in `lib/tools/shellfmt.sh` by @github-actions in https://github.com/armbian/build/pull/7255
* Bump mvdan/sh from 3.9.0 to 3.10.0 in `lib/tools/shellfmt.sh` by @github-actions in https://github.com/armbian/build/pull/7433
* Bump pascalgn/size-label-action from 0.5.4 to 0.5.5 by @dependabot in https://github.com/armbian/configng/pull/209
* Bump Rockchip 32bit edge kernel to 6.11 by @paolosabatino in https://github.com/armbian/build/pull/7273
* bump rockchip64 edge kernel to v6.11 by @paolosabatino in https://github.com/armbian/build/pull/7278
* Change development repository domain name to github.armbian.com by @igorpecovnik in https://github.com/armbian/build/pull/7477
* Change development repository domain name to github.armbian.com by @igorpecovnik in https://github.com/armbian/configng/pull/258
* Change pull request trigger in order to get permissions back in order by @igorpecovnik in https://github.com/armbian/build/pull/7421
* Change to armbian-config also in Unit test CI by @igorpecovnik in https://github.com/armbian/configng/pull/186
* Cherryba M1: switch legacy branch to EDGE to fix compliation breaking by @igorpecovnik in https://github.com/armbian/build/pull/7236
* CI: Improve automatic labelling system on pull requests by @igorpecovnik in https://github.com/armbian/build/pull/7409
* CM3588-NAS: Go fully mainline by adopting the latest mainline changes from kernel 6.11 and U-Boot v2024.10 by @ColorfulRhino in https://github.com/armbian/build/pull/7082
* compilation: armbian-kernel: Change forced uncompressed modules option for kernels >=v6.12 by @ColorfulRhino in https://github.com/armbian/build/pull/7389
* Cosmetic bugfix - we need to limit grep to match first character only by @igorpecovnik in https://github.com/armbian/build/pull/7444
* Cosmetic: fixing link in the bug issue template by @igorpecovnik in https://github.com/armbian/configng/pull/223
* Cosmetic / UX: Display VENDORPRETTYNAME instead of VENDOR  by @igorpecovnik in https://github.com/armbian/build/pull/7261
* cyber-aib-rk3588: add edge kernel support by @chainsx in https://github.com/armbian/build/pull/7446
* Debian desktops: disable Pidgin as its broken. Can stay that way. by @igorpecovnik in https://github.com/armbian/build/pull/7384
* debsums: changing default checking as it will fail on base-files by @igorpecovnik in https://github.com/armbian/build/pull/7301
* Deprecated `WIREGUARD` once and for all by @EvilOlaf in https://github.com/armbian/build/pull/7452
* desktop: amd64: drop nvidia-drivers forced ppa (focal stuff? no thanks) by @rpardini in https://github.com/armbian/build/pull/7168
* Desktop: two packages are missing from Trixie by @igorpecovnik in https://github.com/armbian/build/pull/7305
* Disable desktops as we don't have consistency at build side by @igorpecovnik in https://github.com/armbian/configng/pull/228
* Disable distribution upgrade as its still pretty fragile by @igorpecovnik in https://github.com/armbian/configng/pull/234
* distro-specific: systemd-resolved: don't impose 1.0.0.1 DNS server on users by @rpardini in https://github.com/armbian/build/pull/7166
* Documentation CI: assemble parts before making it by @igorpecovnik in https://github.com/armbian/configng/pull/211
* drm/panthor: Restrict high priorities on group_create by @amazingfate in https://github.com/armbian/linux-rockchip/pull/260
* dt_makefile_patcher: fix dtbs with dot in filename by @amazingfate in https://github.com/armbian/build/pull/7194
* dts: fxblox remove sd pwr gpio and correct bt wake gpio by @mahdichi in https://github.com/armbian/linux-rockchip/pull/286
* dynamic document (software) FInal draft by @Tearran in https://github.com/armbian/configng/pull/188
* enable ap6275s bleutooth on armsom sige1 and sige3 by @amazingfate in https://github.com/armbian/linux-rockchip/pull/271
* enable edge kernel to h96-tvbox-3566 TV-box by @hqnicolas in https://github.com/armbian/build/pull/7310
* Enable hs200 mode for RockPi S, set CMA to 16M by @paolosabatino in https://github.com/armbian/build/pull/7463
* Enable ksmbd consistently across configurations by @lpapadakos in https://github.com/armbian/build/pull/7171
* Enable oras pull to use system proxy by @IsMrX in https://github.com/armbian/build/pull/7227
* enable panfrost driver for rk3576 boards by @amazingfate in https://github.com/armbian/build/pull/7307
* enable pd negotiation support for bananapim7 by @amazingfate in https://github.com/armbian/build/pull/7483
* enable wifi on opi3b v1.1 with 6.11 kernel by @amazingfate in https://github.com/armbian/build/pull/7406
* Example of adding a software title: Portainer by @igorpecovnik in https://github.com/armbian/configng/pull/210
* Expand dynamic documentation generation with headers, footer and image by @igorpecovnik in https://github.com/armbian/configng/pull/196
* First login automation - add support for SSH key download by @igorpecovnik in https://github.com/armbian/build/pull/7396
* Fix and update GitHub Actions workflow for building the kernel on PR by @ColorfulRhino in https://github.com/armbian/linux-rockchip/pull/225
* fix : armsom-w3 screen and camera loading method by @as-jackson in https://github.com/armbian/linux-rockchip/pull/285
* Fix connecting to wifi networks where SSID contains a space or comma by @viraniac in https://github.com/armbian/build/pull/7293
* Fix error on load Headphone on NanoPC T6 by @SuperKali in https://github.com/armbian/linux-rockchip/pull/253
* fix: export memblock_free by @AaronDewes in https://github.com/armbian/linux-rockchip/pull/287
* fix: fix rk3588-cyber-aib hdmi out by @chainsx in https://github.com/armbian/linux-rockchip/pull/275
* Fix HDMI resolutions by @efectn in https://github.com/armbian/linux-rockchip/pull/232
* Fixing unit tests execution by @igorpecovnik in https://github.com/armbian/configng/pull/187
* Fixing wrong ID for portainer and few cosmetic fixes by @igorpecovnik in https://github.com/armbian/configng/pull/216
* Fixing wront number in JSON structure by @igorpecovnik in https://github.com/armbian/configng/pull/251
* fix `iostat` error on `MINIMAL` by @EvilOlaf in https://github.com/armbian/build/pull/7454
* Fix issue 7210, rootdevice altering extensions by @rvalle in https://github.com/armbian/build/pull/7217
* Fix markdown documentation generation by @igorpecovnik in https://github.com/armbian/configng/pull/215
* fix: module_option for install_portainer.sh by @Tearran in https://github.com/armbian/configng/pull/218
* Fix partitioning root UUID bug in /etc/crypttab. New option: CRYPTROOT_MAPPER. by @siis2992 in https://github.com/armbian/build/pull/7443
* fix PS4 controller LED's on current and edge rk3588 kernel configs by @monkaBlyat in https://github.com/armbian/build/pull/7138
* Fix slightly broken network configuration by @igorpecovnik in https://github.com/armbian/configng/pull/249
* Fix small troubles with unit tests by @igorpecovnik in https://github.com/armbian/configng/pull/204
* Fix `sun50i-h616-light` device tree overlay by @JohnTheCoolingFan in https://github.com/armbian/build/pull/7183
* fix typo: catagory => category by @dimitry-ishenko in https://github.com/armbian/configng/pull/246
* Framework: Revert ORAS and setuptools upgrades by @igorpecovnik in https://github.com/armbian/build/pull/7213
* fxblox-rk1: update vendor version by @igorpecovnik in https://github.com/armbian/build/pull/7480
* Gateway GZ80x: add dtsi and power off support via pwr button by @pyavitz in https://github.com/armbian/build/pull/7251
* Gateway GZ80x: `update to u-boot-v2024.07` by @pyavitz in https://github.com/armbian/build/pull/7328
* GHA conditions syntax fix by @igorpecovnik in https://github.com/armbian/build/pull/7423
* GitHub Actions: add log cleaner, adjust names, fix labelling on approve by @igorpecovnik in https://github.com/armbian/build/pull/7434
* Git hub actions: add watchdog to repeat unit tests once and issue auto welcome by @igorpecovnik in https://github.com/armbian/configng/pull/229
* Giveaway: remove additional label that otherwise makes no sense by @igorpecovnik in https://github.com/armbian/build/pull/7387
* Gnome desktops: add gvfs-backends package as its missing only here by @igorpecovnik in https://github.com/armbian/build/pull/7373
* hack: trixie has lost its software-properties-common package so get rid of it for all Debian releases by @rpardini in https://github.com/armbian/build/pull/7464
* Improve Armbian welcome MOTD by @igorpecovnik in https://github.com/armbian/build/pull/7155
* Improvements and bug fixes to Armbian user-space services by @igorpecovnik in https://github.com/armbian/build/pull/6840
* Improvement: Update MOTD to include IPv6 local addresses by @SuperKali in https://github.com/armbian/build/pull/7315
* Improve packaging process and change name to armbian-config by @igorpecovnik in https://github.com/armbian/configng/pull/182
* Install nc to the unit test environment for port testing by @igorpecovnik in https://github.com/armbian/configng/pull/200
* Install netcat-traditional instead of netcat by @igorpecovnik in https://github.com/armbian/configng/pull/201
* introcude devicetree property rockchip,default-link-up to fix rtl8125 on opi5plus by @amazingfate in https://github.com/armbian/linux-rockchip/pull/283
* Introduce new parameter that will execute a script prior to packing by @igorpecovnik in https://github.com/armbian/configng/pull/214
* Introduce the Turing RK1 by @Joshua-Riek in https://github.com/armbian/build/pull/7228
* JetHome: Update JetHub D2 support by @adeepn in https://github.com/armbian/build/pull/6928
* JSON cleanup with unit tests adjustements by @igorpecovnik in https://github.com/armbian/configng/pull/207
* KDE wallet: ship KDE distro with default disabled KDE Wallet by @igorpecovnik in https://github.com/armbian/build/pull/7302
* Kernel bump: adjust broken patches by @igorpecovnik in https://github.com/armbian/build/pull/7335
* Kernel config maint: rewrite kernel config with ./compile rewrite-kernel-config by @igorpecovnik in https://github.com/armbian/build/pull/7249
* kernel-debs: show 3 levels of dirs in tree output for kernel-dtb, so overlays are shown by @rpardini in https://github.com/armbian/build/pull/7238
* kernel-dtb: copy also the dtb binary for the board to output by @rpardini in https://github.com/armbian/build/pull/7163
* kernel: mainline: Bump v6.12-rc4 to v6.12-rc7 by @rpardini in https://github.com/armbian/build/pull/7466
* Let rk35xx and rockchip-rk3588 family use same boot script for legacy/vendor branch by @amazingfate in https://github.com/armbian/build/pull/7288
* Limit default labelling to opened, reopened and synchronise PR by @igorpecovnik in https://github.com/armbian/build/pull/7410
* linux-rk35xx-vendor: enable `CONFIG_KPROBES` by @rpardini in https://github.com/armbian/build/pull/7162
* linux-rockchip-rk3588-6.11.config: enable `CONFIG_INPUT_PWM_BEEPER=m` by @rpardini in https://github.com/armbian/build/pull/7167
* main-config: update China mirror address by @aiamadeus in https://github.com/armbian/build/pull/7420
* mainline-kernel: bump from v6.11-rc4 to v6.11-rc7 by @rpardini in https://github.com/armbian/build/pull/7239
* mainline-kernel: bump to 6.12-rc2 by @rpardini in https://github.com/armbian/build/pull/7366
* mainline-kernel: v6.11 was released by @rpardini in https://github.com/armbian/build/pull/7259
* MBa8MPxL: Bump current kernel from 6.6.43 to 6.11.x by @schmiedelm in https://github.com/armbian/build/pull/7400
* MBa8MPxL: update atf to v2.10 by @schmiedelm in https://github.com/armbian/build/pull/7147
* MBa8MPxL: use nxp WLAN/BT firmware, cleanup board files, leave WIP by @schmiedelm in https://github.com/armbian/build/pull/7324
* media: rockchip: hdmirx: add VIDIOC_G_PARM by @amazingfate in https://github.com/armbian/linux-rockchip/pull/242
* mesa-vpu: don't install mesa-vpu on minimal images by @igorpecovnik in https://github.com/armbian/build/pull/7331
* mesa-vpu: fix dist-upgrade when upstream release new conf file by @amazingfate in https://github.com/armbian/build/pull/7284
* mesa-vpu: support CLI builds as well as desktop by @rpardini in https://github.com/armbian/build/pull/7318
* mesa-vpu: use mesa from debian bookworm-backports by @amazingfate in https://github.com/armbian/build/pull/7356
* Mesa-vpu: we also need to have conditions in the install part  by @igorpecovnik in https://github.com/armbian/build/pull/7339
* meson64: bump edge to 6.11 (currently v6.11-rc7) by @rpardini in https://github.com/armbian/build/pull/7241
* mixtile-edge2: add rk3568 board (current/edge/vendor) by @rpardini in https://github.com/armbian/build/pull/7285
* Modules assemble by @Tearran in https://github.com/armbian/configng/pull/203
* Module template example - Practical use webmin by @Tearran in https://github.com/armbian/configng/pull/240
* MOTD: declutter list of commands in motd. Everything starts with armbian-config by @igorpecovnik in https://github.com/armbian/build/pull/7449
* MOTD: display hostapd parameters if AP is in operation by @igorpecovnik in https://github.com/armbian/build/pull/7353
* MOTD: fix error when traffic info is enabled by @igorpecovnik in https://github.com/armbian/build/pull/7247
* Move board Youyeetoo R1 v3 from WIP to CSC by @SuperKali in https://github.com/armbian/build/pull/7149
* Move LicheePi-4A to eos because its chip design has security vulnerabilities. by @chainsx in https://github.com/armbian/build/pull/7179
* Move maintainers update function from https://github.com/armbian/scripts by @igorpecovnik in https://github.com/armbian/build/pull/7407
* Move support of nanopc t6 & lts from edge to current by @SuperKali in https://github.com/armbian/build/pull/7476
* nanopi-m6: add LCD overlay as default by @efectn in https://github.com/armbian/build/pull/7344
* nanopi-m6: make it standard supported by @efectn in https://github.com/armbian/build/pull/7380
* Nanopi R6: adjust kernel build target to have correct images built by @igorpecovnik in https://github.com/armbian/build/pull/7246
* nanopi-r6s: mark as supported by @igorpecovnik in https://github.com/armbian/build/pull/7244
* New software title: OpenHab by @igorpecovnik in https://github.com/armbian/configng/pull/230
* Odroid M1: resolve lowered network speed by @igorpecovnik in https://github.com/armbian/build/pull/7245
* Odroid XU4 kernel: remove deprecated patches by @igorpecovnik in https://github.com/armbian/build/pull/7349
* Odroid XU4: remove deprecated patches by @igorpecovnik in https://github.com/armbian/build/pull/7208
* oneplus-kebab: disable edge build by @amazingfate in https://github.com/armbian/build/pull/7427
* Op5+/HDMI-RX: expose ITC type to v4l2 in synopsys hdmir rx by @benhoff in https://github.com/armbian/build/pull/7224
* Op5+/HDMI-RX: fix spurious triggering of irq 5v while plugout code is running by @benhoff in https://github.com/armbian/build/pull/7212
* opi3b: fix mainline uboot with vendor kernel and fix uwe5622 bt for rk35xx by @amazingfate in https://github.com/armbian/build/pull/7025
* opi5pro: change dr_mode to host by @EvilOlaf in https://github.com/armbian/linux-rockchip/pull/217
* Orange Pi 3B: Edge: Switch to mainline dts by @dust-7 in https://github.com/armbian/build/pull/7290
* Orange Pi 3B: Update board config to support v2.1 boards by @dust-7 in https://github.com/armbian/build/pull/7233
* Orange Pi 3B: Vendor: Enable audio via headphone jack by @dust-7 in https://github.com/armbian/build/pull/7330
* Overlay management - reverting to previous logic  by @igorpecovnik in https://github.com/armbian/configng/pull/256
* Overlay management: somewhere we had OVERLAY_DIR and somewhere OVERLAYDIR by @igorpecovnik in https://github.com/armbian/build/pull/7351
* patching: emit warnings when files in `dt` folder overwrite pre-existing files (DTs that landed upstream) by @rpardini in https://github.com/armbian/build/pull/7271
* Patch: refactor broken patch due to upstream changes by @igorpecovnik in https://github.com/armbian/build/pull/7190
* Phytiumpi: switch default branch for images and testing to CURRENT by @igorpecovnik in https://github.com/armbian/build/pull/7206
* power: supply: add Simple ADC power supply driver for NanoPi boards by @efectn in https://github.com/armbian/linux-rockchip/pull/261
* prepare-host: trixie and sid don't carry python3-distutils anymore by @rpardini in https://github.com/armbian/build/pull/7165
* radxa-aic8800: remove kernel version check by @amazingfate in https://github.com/armbian/build/pull/7283
* Radxa Rock-3a - edge - add GPIO names by @mr-toolcraft in https://github.com/armbian/build/pull/7403
* Radxa rock-3a - edge - add overlay to disable debug console by @mr-toolcraft in https://github.com/armbian/build/pull/7402
* Radxa Rock-3a - edge - use mainline uboot by @mr-toolcraft in https://github.com/armbian/build/pull/7401
* radxa-zero2: bump to u-boot 2024.07 (from 2023.10) by @rpardini in https://github.com/armbian/build/pull/7258
* Radxa Zero 3W/E - edge - switch to mainline uboot 2024.10 by @mr-toolcraft in https://github.com/armbian/build/pull/7411
* ramlog: remove obsolete nocache; fixes #6890 by @alex3d in https://github.com/armbian/build/pull/7378
* Readme: fix broken links to documentation due to structural changes by @igorpecovnik in https://github.com/armbian/build/pull/7467
* rebase commits from rk-6.1-rk1 to rk-6.1-rkr3 by @amazingfate in https://github.com/armbian/linux-rockchip/pull/200
* refactored see_full_list by @Tearran in https://github.com/armbian/configng/pull/184
* reinstate tinker edge r dts by @Tonymac32 in https://github.com/armbian/build/pull/7311
* Release preparation MBa8MPxL by @schmiedelm in https://github.com/armbian/build/pull/7450
* Remove deprecated patch by @igorpecovnik in https://github.com/armbian/build/pull/7425
* Remove duplicated items on youyeetoo r1 dts file by @SuperKali in https://github.com/armbian/linux-rockchip/pull/255
* Remove edge kernel on youyeetoo r1 by @SuperKali in https://github.com/armbian/build/pull/7475
* remove redundant "add Xiaobao-nas" patch by @Tonymac32 in https://github.com/armbian/build/pull/7312
* Remove wireless tools dependency from all user space variants by @igorpecovnik in https://github.com/armbian/build/pull/7314
* RetrOLED CM5: Add missing Makefile entry by @ginkage in https://github.com/armbian/linux-rockchip/pull/280
* RetrOLED CM5: Fix PWM fan frequency and display rotation by @ginkage in https://github.com/armbian/linux-rockchip/pull/274
* Revert "Move support of nanopc t6 & lts from edge to current" by @SuperKali in https://github.com/armbian/build/pull/7481
* Revert "PCI: rockchip: dw: remove .link_up() hook from struct dw_pcie… by @RadxaStephen in https://github.com/armbian/linux-rockchip/pull/221
* Revert "Update odroidxu4-current to 6.6.54" by @igorpecovnik in https://github.com/armbian/build/pull/7348
* Revert "Update odroidxu4-current to 6.6.59" by @igorpecovnik in https://github.com/armbian/build/pull/7438
* Review and refactor DTS code for Youyeetoo R1 V3 by @SuperKali in https://github.com/armbian/linux-rockchip/pull/238
* RFC: initial Rock 5B+ edge kernel support by @fridtjof in https://github.com/armbian/build/pull/7457
* rk3318-box: enable usb3 port in uboot by @alex3d in https://github.com/armbian/build/pull/7253
* rk3318-box: fix usb2 functionality in u-boot, that was broken since update to v2024.07 by @alex3d in https://github.com/armbian/build/pull/7235
* rk3318: enable rng-seed population in u-boot by @alex3d in https://github.com/armbian/build/pull/7364
* rk3576: use boot.scr instead of extlinux by @amazingfate in https://github.com/armbian/build/pull/7426
* RK3588: add 580 encoding by @benhoff in https://github.com/armbian/build/pull/7298
* Rk3588: bump to 6.12 for edge and current by @amazingfate in https://github.com/armbian/build/pull/7455
* Rock-5c add an asound.state file to fix mic and sound issues by @schwar3kat in https://github.com/armbian/build/pull/7361
* rockchip64-6.10: rebase/rewrite all patches against v6.10.10 by @rpardini in https://github.com/armbian/build/pull/7237
* [rockchip64] add tm16xx led driver for display panels by @paolosabatino in https://github.com/armbian/build/pull/7338
* rockchip64-edge: bump to 6.12 by @amazingfate in https://github.com/armbian/build/pull/7447
* rockchip64: enable i2c-gpio bitbang driver by @paolosabatino in https://github.com/armbian/build/pull/7334
* rockchip64: fix crash dump on eager led setting with tm16xx led driver by @paolosabatino in https://github.com/armbian/build/pull/7462
* rockchip64: make rockchip64 bootable in VM by @alex3d in https://github.com/armbian/build/pull/7392
* Rockchip64: remove deprecated patches that breaks compilation by @igorpecovnik in https://github.com/armbian/build/pull/7180
* [rockchip64] Remove mainlined hunk from patches by @paolosabatino in https://github.com/armbian/build/pull/7333
* rockchip64/uboot: increase rng-seed size to make it sufficient for modern linux by @alex3d in https://github.com/armbian/build/pull/7365
* Rockchip armhf: remove parts of code from the patch which has been upstreamed by @igorpecovnik in https://github.com/armbian/build/pull/7478
* [rockchip] Provide dtb overlay to enable pwm node for rk3288 by @paolosabatino in https://github.com/armbian/build/pull/7369
* rockchip: remove patch breaking HDMI 7" displays on Tinkerboard by @paolosabatino in https://github.com/armbian/build/pull/7479
* rockchip-rk3588/6.11: backport Marcin Juszkiewicz's "FriendlyELEC NanoPC-T6 improvements" v6 series to fix non-LTS and split LTS version of NanoPC T6 by @rpardini in https://github.com/armbian/build/pull/7272
* rockchip-rk3588-6.11: bump to v6.11-rc7; manually rebase `0001-general-add-overlay-support.patch` by @rpardini in https://github.com/armbian/build/pull/7240
* rockchip-rk3588: current edge: add a pwm fan control overlay by @alexl83 in https://github.com/armbian/build/pull/7137
* rockchip-rk3588-current: update kernel to 6.11 by @efectn in https://github.com/armbian/build/pull/7326
* rockchip-rk3588: Enable CONFIG_NETKIT kernel option by @mschirrmeister in https://github.com/armbian/build/pull/7385
* rockchip-rk3588: fanctrl overlay: fix `<&fan>` alias for device tree by @alexl83 in https://github.com/armbian/build/pull/7151
* rockchip-rk3588: fix hdmi display of armsom-sige7 for edge and current by @amazingfate in https://github.com/armbian/build/pull/7243
* rockchip-rk3588 / legacy: bump to 5.10-rkr8 (5.10.209) by @rpardini in https://github.com/armbian/build/pull/7319
* rockchip-rk3588: orangepi5-plus current, edge: u-boot: bump to mainline 2024.10-rc3 by @alexl83 in https://github.com/armbian/build/pull/7136
* rockchip-rk3588: use rkvdec2 patch from rockchip64 by @amazingfate in https://github.com/armbian/build/pull/7429
* rockchip-rk3588 / vendor: add CONFIG_RC_CORE and all IR remote modules by @rpardini in https://github.com/armbian/build/pull/7320
* rockchip-rk3588-vendor: enable CONFIG_NANOPI_ADC_POWER by @efectn in https://github.com/armbian/build/pull/7357
* Rockchip vendor: enable several options in Rockchip kernel by @igorpecovnik in https://github.com/armbian/build/pull/7300
* Rockpis family by @brentr in https://github.com/armbian/build/pull/7382
* rockpro64: bump u-boot to 2024.07; make fancy configs; drop bin size limit as fix landed upstream by @rpardini in https://github.com/armbian/build/pull/7161
* rockpro64: u-boot: patch u-boot's dtsi to enable otg port for UMS/Gadget capabilities by @rpardini in https://github.com/armbian/build/pull/7231
* rootfs cache: after updating github cli key, we need to rebuild rootfs cache by @igorpecovnik in https://github.com/armbian/build/pull/7215
* rootfs: don't use the Armbian repo when building rootfs from both GHA pipelines and CLI; fixes #7123 by @rpardini in https://github.com/armbian/build/pull/7313
* rtc: rockchip: dts disable check add other variants by @pykpkg47 in https://github.com/armbian/linux-rockchip/pull/230
* s4t7: Add panfrost driver by @viraniac in https://github.com/armbian/build/pull/7248
* Simplify sudo check require it always. by @Tearran in https://github.com/armbian/configng/pull/183
* sm8250-current: update to 6.11 by @amazingfate in https://github.com/armbian/build/pull/7277
* sm8250: disable broken patch due upstream changes by @igorpecovnik in https://github.com/armbian/build/pull/7424
* Software title: add Uptime Kuma, self-hosted monitoring tool by @igorpecovnik in https://github.com/armbian/configng/pull/237
* Some more Panthor fixes by @ginkage in https://github.com/armbian/linux-rockchip/pull/210
* spacemit: opensbi, u-boot, kernel legacy: Update for v1.0.15 by @The-going in https://github.com/armbian/build/pull/7350
* Store list of installed extensions and image vendor to image and not to BSP by @igorpecovnik in https://github.com/armbian/build/pull/7182
* Store two additional variables to /etc/armbian-release by @igorpecovnik in https://github.com/armbian/build/pull/7156
* sunxi-6.10: Add armbian patches by @The-going in https://github.com/armbian/build/pull/7127
* Sunxi-6.11: Fix a broken package for EDGE by @The-going in https://github.com/armbian/build/pull/7474
* sunxi-6.11 Switch EDGE to v6.11 by @The-going in https://github.com/armbian/build/pull/7289
* sunxi 6.11: Switch kernel version to v6.11.2, Re-extract patches by @The-going in https://github.com/armbian/build/pull/7352
* sunxi 6.11: Switch to v6.11.6, bugfix temperature interface for h616, h618 by @The-going in https://github.com/armbian/build/pull/7442
* Support CherryBa M1 board by @IsMrX in https://github.com/armbian/build/pull/7226
* Support for Luckfox Core3566 by @buldo in https://github.com/armbian/build/pull/7354
* Sync drm/panthor and drm/sched with 6.12-rc2 by @ginkage in https://github.com/armbian/linux-rockchip/pull/264
* systemd-networkd: default to DUIDType=link-layer for ipv6; via networkd.conf.d by @rpardini in https://github.com/armbian/build/pull/7232
* thinkpad-x13s: bump to jhovold's `wip/sc8280xp-6.11` (final) from -rc5 by @rpardini in https://github.com/armbian/build/pull/7260
* thinkpad-x13s: bump to jhovold's wip/sc8280xp-6.11-rc5; userspace fixes by @rpardini in https://github.com/armbian/build/pull/7164
* thinkpad-x13s: bump to jhovold's wip/sc8280xp-6.12-rc2 by @rpardini in https://github.com/armbian/build/pull/7367
* thinkpad-x13s: bump to jhovold's wip/sc8280xp-6.12-rc4 by @rpardini in https://github.com/armbian/build/pull/7465
* tqma-current and xfce: fixes by @schmiedelm in https://github.com/armbian/build/pull/7405
* u-boot-sunxi: Fix loading of bananapim3 board from eMMC by @The-going in https://github.com/armbian/build/pull/7252
* Ubuntu Focal: Change from EOS to CSC in order to generate base-files by @igorpecovnik in https://github.com/armbian/build/pull/7309
* uefi-* / edge: bump to 6.12; rework arm64 Phytium stmmac acpi patches by @rpardini in https://github.com/armbian/build/pull/7368
* Unit test bug-fix - broken if checking one test at PR by @igorpecovnik in https://github.com/armbian/configng/pull/199
* Update docs.yml to correct json name by @Tearran in https://github.com/armbian/configng/pull/213
* Update GitHub CLI GPG key by @williammartin in https://github.com/armbian/build/pull/7192
* Update linux-uefi-arm64-edge.config by @bmilde in https://github.com/armbian/build/pull/7419
* Update odroidxu4-current to 6.6.51 by @belegdol in https://github.com/armbian/build/pull/7230
* Update odroidxu4-current to 6.6.54 by @belegdol in https://github.com/armbian/build/pull/7340
* Update odroidxu4-current to 6.6.59 by @belegdol in https://github.com/armbian/build/pull/7435
* Update radxa 5 itx from upstream by @SuperKali in https://github.com/armbian/linux-rockchip/pull/263
* Userspace: add information about read only rootfs feature by @igorpecovnik in https://github.com/armbian/build/pull/7218
* Userspace: remove System Activity Reporter (SAR) from server package base by @igorpecovnik in https://github.com/armbian/build/pull/7203
* `Userspace` Switching armbian-config to new generation. by @igorpecovnik in https://github.com/armbian/build/pull/7189
* `Userspace`: UX changes at MOTD and first login by @igorpecovnik in https://github.com/armbian/build/pull/7174
* UX bugfix: on first run we display some warnings if userspace is unsupported by @igorpecovnik in https://github.com/armbian/build/pull/7431
* UX: cosmetic improvements on motd and armbian-install by @igorpecovnik in https://github.com/armbian/build/pull/7264
* VIM1S: Use panfrost by default by @viraniac in https://github.com/armbian/build/pull/7329
* WIP: adding some fixes in the drivers by @SuperKali in https://github.com/armbian/linux-rockchip/pull/248
* WIP: arch: arm64 board: youyeetoo r1 v3 add rewrited dts code. by @SuperKali in https://github.com/armbian/linux-rockchip/pull/223
* Wireless drivers: remove driver for 8822BS applicable for old kernels by @igorpecovnik in https://github.com/armbian/build/pull/7390
* Wireless drivers: rtw88: remove deprecated sections in patch by @igorpecovnik in https://github.com/armbian/build/pull/7219
* X96Q LPDDR3 Improvements by @sicXnull in https://github.com/armbian/build/pull/7276
* xiaomi-elish 6.11 fixes by @amazingfate in https://github.com/armbian/build/pull/7359
* ZSH: move functions from JSON to separate modules by @igorpecovnik in https://github.com/armbian/configng/pull/224

## v24.8.4 (2024-10-12)

* Recreated images for Radxa Rock 5C, Nanopi M6

## v24.8.3 (2024-09-13)

* Recreated images for Radxa Rock 5 ITX, Rockpi E, Odroid M1, Nanopi R6S

## v24.8.1 (2024-08-31)

* [Add audio support to hdmi output (meson) by @kernelzru](https://github.com/armbian/build/pull/6730)
* [Temporally disable broken build configuration by @igorpecovnik](https://github.com/armbian/build/pull/6733)
* [Odroid XU4: Remove deprecated patches by @igorpecovnik](https://github.com/armbian/build/pull/6732)
* [RK3588 edge kernel: Add support for Linux 6.10 + introduce stable `current` branch (6.8) by @ColorfulRhino](https://github.com/armbian/build/pull/6699)
* [rk3588: Add board NanoPi R6C by @ColorfulRhino](https://github.com/armbian/build/pull/6738)
* [re-add some Khadas Edge 2 patches to edge kernel by @efectn](https://github.com/armbian/build/pull/6737)
* [Update JetHome JetHub D2 support by @adeepn](https://github.com/armbian/build/pull/6736)
* [rockchip-rk3588 6.8.y: nanopct6: Add NanoPC T6 SPI Flash (v6.8.y version) by @rpardini](https://github.com/armbian/build/pull/6735)
* [rockchip64/rk3318-box: move stack further from base addr to allow bigger uboot image by @alex3d](https://github.com/armbian/build/pull/6731)
* [RK3588 edge: Add H.264 decoder support by @ColorfulRhino](https://github.com/armbian/build/pull/6734)
* [GH Actions: Fix auto-labeler for "Desktop" category and add categories "Patches" and "Documentation" by @ColorfulRhino](https://github.com/armbian/build/pull/67)
* [extlinux: add DEFAULT_OVERLAYS support by @efectn](https://github.com/armbian/build/pull/6744)
* [Disable autosuspend on Gnome based desktops by @igorpecovnik](https://github.com/armbian/build/pull/6742)
* [actions: Fix typo in actions/labeler labeler.yml by @ColorfulRhino](https://github.com/armbian/build/pull/6745)
* [cli: Fix DEFAULT_OVERLAYS array by @ColorfulRhino](https://github.com/armbian/build/pull/6746)
* [khadas-edge2: rename audios by @efectn](https://github.com/armbian/build/pull/6750)
* [Fix boot from btrfs fs in uboot 2024.01/2024.04 by @alex3d](https://github.com/armbian/build/pull/6748)
* [rockchip-rk3588-edge: fix vepu of rk3588 by @amazingfate](https://github.com/armbian/build/pull/6752)
* [board: orangepi-5-plus: Add mainline U-Boot for edge kernel by @ColorfulRhino](https://github.com/armbian/build/pull/6719)
* [khadas-edge2: add vendor uboot to images by @igorpecovnik](https://github.com/armbian/build/pull/6754)
* [board: nanopi-r6s: Add system-power-controller to pmic by @ColorfulRhino](https://github.com/armbian/build/pull/6755)
* [kernel: mainline: Bump 6.10-rc3 to 6.10-rc4 by @ColorfulRhino](https://github.com/armbian/build/pull/6753)
* [Sm8250 6.9 by @amazingfate](https://github.com/armbian/build/pull/6727)
* [Add support for rk3399 based SBC Leez P710 by @andyshrk](https://github.com/armbian/build/pull/6749)
* [Debian buster: disable non-existing backports repository by @igorpecovnik](https://github.com/armbian/build/pull/6758)
* [packages: Enable bash-completion on all images by @ColorfulRhino](https://github.com/armbian/build/pull/6759)
* [station-m2: Use Raxda u-boot 2024.01 by @chainsx](https://github.com/armbian/build/pull/6760)
* [actions: Fix auto-labeler by checking subdirectories by @ColorfulRhino](https://github.com/armbian/build/pull/6764)
* [aic8800: update firmware package URL by @RadxaYuntian](https://github.com/armbian/build/pull/6768)
* [Move Network Manager bits into extensions by @igorpecovnik](https://github.com/armbian/build/pull/6756)
* [fix armbian-leds-state-save.sh: by @alexl83](https://github.com/armbian/build/pull/6765)
* [add community support for lckfb taishanpi by @chainsx](https://github.com/armbian/build/pull/6767)
* [Deboostrap: switch to last known working tag by @igorpecovnik](https://github.com/armbian/build/pull/6775)
* [i3-wm: remove conflicting userspace packages by @igorpecovnik](https://github.com/armbian/build/pull/6776)
* [partitioning: fix race condition on loop device allocation by @alex3d](https://github.com/armbian/build/pull/6729)
* [rockchip-rk3588: edge: add rkvdec2 support by @amazingfate](https://github.com/armbian/build/pull/6777)
* [Rootfs cache is repeating generation over and over again by @igorpecovnik](https://github.com/armbian/build/pull/6778)
* [add device-tree-compiler to bsp-cli debian dependencies by @alexl83](https://github.com/armbian/build/pull/6779)
* [Run shellfmt to complete code by @igorpecovnik](https://github.com/armbian/build/pull/6782)
* [Networking: set proper hook location for extensions by @igorpecovnik](https://github.com/armbian/build/pull/6780)
* [ext: fs-cryptroot-support: don't abuse `add_host_dependencies` by @rpardini](https://github.com/armbian/build/pull/6785)
* [rockchip-rk3588 6.8/610: add `i2c8-m2` overlay by @rpardini](https://github.com/armbian/build/pull/6784)
* [rk3588: Enable `current` kernel branch for some boards by @ColorfulRhino](https://github.com/armbian/build/pull/6740)
* [Add orangepi5-plus UART overlays by @alexl83](https://github.com/armbian/build/pull/6787)
* [networking: main-config: introduce `NETWORKING_STACK` to control network exts; allow "none"; fix typo by @rpardini](https://github.com/armbian/build/pull/6786)
* [Helios64: move to supported section by @igorpecovnik](https://github.com/armbian/build/pull/6789)
* [phytium-embedded: add bpf_syscall support by @chainsx](https://github.com/armbian/build/pull/6788)
* [Use random-mac only with systemd-networkd (minimal images) by @igorpecovnik](https://github.com/armbian/build/pull/6783)
* [Rockcchip RK3588: Rename overlay suffix to match reality by @igorpecovnik](https://github.com/armbian/build/pull/6791)
* [distro: trixie: Add riscv64 to supported architectures by @ColorfulRhino](https://github.com/armbian/build/pull/6793)
* [Revert "distro: trixie: Add riscv64 to supported architectures" by @ColorfulRhino](https://github.com/armbian/build/pull/6794)
* [kernel: mainline: Bump 6.10-rc4 to 6.10-rc5 by @ColorfulRhino](https://github.com/armbian/build/pull/6792)
* [cli: Add command "dts-check" to validate dts files and improve board & patch development overall (resubmission) by @ColorfulRhino](https://github.com/armbian/bu)
* [tools: Update shellfmt from version 3.6.0 to 3.8.0 by @ColorfulRhino](https://github.com/armbian/build/pull/6795)
* [actions: Use "all-globs" instead of "any-glob" for negated checks by @ColorfulRhino](https://github.com/armbian/build/pull/6796)
* [Fix aml-s9xx-box bsp-cli package upgrade by @SteeManMI](https://github.com/armbian/build/pull/6797)
* [DTS-check: Python librarires have troubles to build, disabling for now by @igorpecovnik](https://github.com/armbian/build/pull/6798)
* [Fix `dts-check` command and use Pip for some Python packages instead of APT by @ColorfulRhino](https://github.com/armbian/build/pull/6799)
* [bootscript: Remove deprecated bootarg "swapaccount=1" by @ColorfulRhino](https://github.com/armbian/build/pull/6705)
* [Odroid M1: add a network rule to rename default name by @igorpecovnik](https://github.com/armbian/build/pull/6757)
* [Add new "BSP" and "GitHub" label for the auto-labeler by @ColorfulRhino](https://github.com/armbian/build/pull/6805)
* [rk3588: bump default blobs (DDR:1.16, BL31:1.45); remove board-specific blobs from boards that used those versions by @rpardini](https://github.com/armbian/build/pull/6810)
* [fix: partitioning: disable `orphan_file` (`FEATURE_C12`) for ext4 filesystems on 1.47+ e2fsprogs host by @rpardini](https://github.com/armbian/build/pull/6809)
* [aml-s9xx-box: Remove u-boot and update generated extlinux.conf by @SteeManMI](https://github.com/armbian/build/pull/6803)
* [GitHub: Improve issue templates and add new `Task` template for project management by @ColorfulRhino](https://github.com/armbian/build/pull/6813)
* [station-m2: update u-boot patches by @chainsx](https://github.com/armbian/build/pull/6812)
* [kde-neon: use Neon's "user" repo for Jammy & return it to `csc` status by @rpardini](https://github.com/armbian/build/pull/6808)
* [actions: labeler: Fix label colors by removing `#` prefix by @ColorfulRhino](https://github.com/armbian/build/pull/6807)
* [Move board-specific config (Odroid C1) away from family config by @ColorfulRhino](https://github.com/armbian/build/pull/6801)
* [Remove haveged to save space and resources by @alexl83](https://github.com/armbian/build/pull/6781)
* [Lets not spam users with error message on fresh checkout by @viraniac](https://github.com/armbian/build/pull/6814)
* [BPI-CM4: bluetooth: `fw version 0xb5d66dcb` by @pyavitz](https://github.com/armbian/build/pull/6816)
* [Update odroidxu4-current to 6.6.36 by @belegdol](https://github.com/armbian/build/pull/6815)
* [Odroid XU4: remove deprecated patch by @igorpecovnik](https://github.com/armbian/build/pull/6825)
* [Add Matrix to README by @EvilOlaf](https://github.com/armbian/build/pull/6826)
* [extensions/radxa-aic8800: fix aic8800_dkms_file_name for sdio by @andyshrk](https://github.com/armbian/build/pull/6827)
* [Bump default boot blobs for RK3528, RK3566 and RK3568 and use them for NanoPi R5C by @ColorfulRhino](https://github.com/armbian/build/pull/6822)
* [armbianmonitor `-u`: rationalize paste server retrying, use ANSI dmesg by @rpardini](https://github.com/armbian/build/pull/6836)
* [cli: uboot: Include PYTHONPATH in env for compiling U-Boot by @ColorfulRhino](https://github.com/armbian/build/pull/6819)
* [Integrate `media` boards into the `rockchip64` family by @ColorfulRhino](https://github.com/armbian/build/pull/6834)
* [Cleanup: Remove old torrents by @ColorfulRhino](https://github.com/armbian/build/pull/6829)
* [Cleanup: Remove leftovers of former `BOARDFAMILY` `rk322x` (now integrated into the `rockchip` family) by @ColorfulRhino](https://github.com/armbian/build/pull/6832)
* [odroidm1/orangepi3b: use default (newer) blobs; rewrite patches; bump -rc u-boot to final by @rpardini](https://github.com/armbian/build/pull/6837)
* [Cleanup: Clean leftovers in `packages/extras-buildpkgs` by @ColorfulRhino](https://github.com/armbian/build/pull/6830)
* [Cleanup: Remove some leftover kernel patch folders by @ColorfulRhino](https://github.com/armbian/build/pull/6831)
* [radxa-zero3: add `edge` branch (6.9.y) by picking DT from linux-rockchip#for-next & using Kwiboo's 24.07 u-boot by @rpardini](https://github.com/armbian/build/pull/6842)
* [u-boot: add HOME env for make invocations to avoid binman/Python problems with older u-boot versions by @rpardini](https://github.com/armbian/build/pull/6845)
* [rockchip: fix rk322x-box uboot boot order by @paolosabatino](https://github.com/armbian/build/pull/6844)
* [Addressing two problems related to `wireless at firstlogin script` by @igorpecovnik](https://github.com/armbian/build/pull/6823)
* [Remove OrangepiZero2 heavily outdated legacy kernel by @igorpecovnik](https://github.com/armbian/build/pull/6854)
* [v3: Add new RISCV family "SpacemiT" and board BananaPi F3 by @ColorfulRhino](https://github.com/armbian/build/pull/6850)
* [Fix btrfs and xfs resize by @Ratio2](https://github.com/armbian/build/pull/6846)
* [aml-s9xx-box: bsp-cli hashing fixes by @rpardini](https://github.com/armbian/build/pull/6839)
* [Bump sunxi-current and sunxi64 to latest tag by @EvilOlaf](https://github.com/armbian/build/pull/6861)
* [improve fs-cryptroot-support.sh by @alexl83](https://github.com/armbian/build/pull/6858)
* [build(deps): bump setuptools from 70.1.1 to 70.2.0 by @dependabot](https://github.com/armbian/build/pull/6856)
* [nanopi-r5s: bump blobs & u-boot enhancements for UMS/otg/bootorder by @rpardini](https://github.com/armbian/build/pull/6833)
* [Update support for recore boards by @eliasbakken](https://github.com/armbian/build/pull/6859)
* [Fixing syntax at Recore and add missing board level variables by @igorpecovnik](https://github.com/armbian/build/pull/6863)
* [rootfs: add comment to force rootfs rebuild by @rpardini](https://github.com/armbian/build/pull/6864)
* [Test automation - adjust kernel test targets. by @igorpecovnik](https://github.com/armbian/build/pull/6865)
* [Fix Khadas Edge 2 uboot build by @efectn](https://github.com/armbian/build/pull/6868)
* [Add recore dts patch to series.conf so it gets applied by @eliasbakken](https://github.com/armbian/build/pull/6866)
* [bsp-cli/bsp-desktop: hashing fixes by @rpardini](https://github.com/armbian/build/pull/6838)
* [Fix several issues related to building U-Boot by @ColorfulRhino](https://github.com/armbian/build/pull/6867)
* [Bump rk322x-box and rk3318-box to u-boot v2024.07-rc5 by @paolosabatino](https://github.com/armbian/build/pull/6855)
* [fix: firefly-itx-3588j fails to boot, and audio output by @SeeleVolleri](https://github.com/armbian/build/pull/6849)
* [u-boot: use `pipetty` in place of `unbuffer` by @rpardini](https://github.com/armbian/build/pull/6873)
* [Purge `s5p6818` board family by @ColorfulRhino](https://github.com/armbian/build/pull/6869)
* [git: git_ensure_safe_directory(): use env vars instead of changing config by @rpardini](https://github.com/armbian/build/pull/6870)
* [Spacemit: use same kernel config as on known to work image by @igorpecovnik](https://github.com/armbian/build/pull/6875)
* [Update JetHub boards support by @adeepn](https://github.com/armbian/build/pull/6876)
* [Next set of U-Boot compilation fixes by @ColorfulRhino](https://github.com/armbian/build/pull/6877)
* [fix uboot compilation issues on Orange Pi 5/5 Plus by @efectn](https://github.com/armbian/build/pull/6878)
* [Reverting attempted git-safe folder problem by @igorpecovnik](https://github.com/armbian/build/pull/6882)
* [Test automation - optimise testing on targets by @igorpecovnik](https://github.com/armbian/build/pull/6883)
* [mixtile-blade3: use default blobs & bump vendor u-boot to `next-dev-v2024.03` by @rpardini](https://github.com/armbian/build/pull/6872)
* [mekotronics: rk3588: u-boot: borrow patch to fix build on newer gcc by @rpardini](https://github.com/armbian/build/pull/6871)
* [Move OPi5/5B/5 Plus uboots to Radxa git tree by @efectn](https://github.com/armbian/build/pull/6884)
* [rk35xx: Remove `legacy` kernel target from board configs by @ColorfulRhino](https://github.com/armbian/build/pull/6881)
* [rockpi-s: Remove `legacy` kernel 4.4 support by @ColorfulRhino](https://github.com/armbian/build/pull/6879)
* [Armbian-install: add option to wipe target destination by @igorpecovnik](https://github.com/armbian/build/pull/6828)
* [Allow to pass docker login when in CI, but not in GitHub actions by @adeepn](https://github.com/armbian/build/pull/6702)
* [Adjust Rockpi S patch to align with upstream changes by @igorpecovnik](https://github.com/armbian/build/pull/6886)
* [RTW88: 6.6: upstream wireless: `fixups` by @pyavitz](https://github.com/armbian/build/pull/6888)
* [Allwinner: set legacy 6.1.y to last known build tag by @igorpecovnik](https://github.com/armbian/build/pull/6889)
* [add new board radxa-e52c by @amazingfate](https://github.com/armbian/build/pull/6891)
* [Bananapi M5: Bump u-boot to v2024.07 final by @igorpecovnik](https://github.com/armbian/build/pull/6900)
* [u-boot: embed armbian artifact version in CONFIG_LOCALVERSION by @rpardini](https://github.com/armbian/build/pull/6898)
* [odroidm1: bump to u-boot v2024.07; replace defconfig patches with hook by @rpardini](https://github.com/armbian/build/pull/6897)
* [bump rk3288 tinkerboard to uboot v2024.07 by @paolosabatino](https://github.com/armbian/build/pull/6895)
* [Move the `NETWORKING_STACK` in main config and add armhf support to Trixie by @ColorfulRhino](https://github.com/armbian/build/pull/6911)
* [multiple boards: bump u-boot from v2024.07-rcX to v2024.07 final by @rpardini](https://github.com/armbian/build/pull/6899)
* [Beautify `shellfmt` and add board configs to formatting list by @ColorfulRhino](https://github.com/armbian/build/pull/6910)
* [thinkpad-x13s: bump to jhovold's `wip/sc8280xp-6.10-rc6`; add fprintd back to Trixie; fixes by @rpardini](https://github.com/armbian/build/pull/6913)
* [mixtile-blade3: u-boot: join rockchip-rk3588's default `u-boot-radxa-rk35xx` scheme by @rpardini](https://github.com/armbian/build/pull/6915)
* [nanopi-r6s: Use mainline U-Boot by @ColorfulRhino](https://github.com/armbian/build/pull/6908)
* [mekotronics: u-boot: join rockchip-rk3588's default `u-boot-radxa-rk35xx` scheme by @rpardini](https://github.com/armbian/build/pull/6916)
* [Trixie: remove / replace missing packages by @igorpecovnik](https://github.com/armbian/build/pull/6917)
* [build(deps): bump actions/upload-artifact from 4.3.3 to 4.3.4 by @dependabot](https://github.com/armbian/build/pull/6918)
* [partitioning: Reduce `commit` mount option for btrfs and ext4 to 120 by @ColorfulRhino](https://github.com/armbian/build/pull/6919)
* [sunxi-6.1: switch to tag:v6.1.97, re-extracting the corrected ones by @The-going](https://github.com/armbian/build/pull/6893)
* [To modify the PWM-fan temperature control policy of fine3399 to adjust the fan speed to a lower level by @Lemon1151](https://github.com/armbian/build/pull/6843)
* [mt7623: Bump `legacy` 4.19 to `current` 6.6 kernel by @ColorfulRhino](https://github.com/armbian/build/pull/6902)
* [nanopi-r5s: u-boot: pci enum in preboot; disable armbian-led-state by @rpardini](https://github.com/armbian/build/pull/6896)
* [wifi: rtl8852bs: fix build for rockchip by @amazingfate](https://github.com/armbian/build/pull/6926)
* [Fix armbian-firstrun service not disabled on start. by @adeepn](https://github.com/armbian/build/pull/6930)
* [Add MKNOD capability to dockershell container by @JohnTheCoolingFan](https://github.com/armbian/build/pull/6927)
* [Improve Actions UI, introduce Actions run names for all workflows by @ColorfulRhino](https://github.com/armbian/build/pull/6925)
* [Inovato Quadra: enable correct PIN to get wifi working by @igorpecovnik](https://github.com/armbian/build/pull/6892)
* [Spacemit-k1 / Banananpi F3: adjust u-boot patch by @igorpecovnik](https://github.com/armbian/build/pull/6931)
* [thinkpad-x13s: bump to jhovold's `wip/sc8280xp-6.10-rc7` by @rpardini](https://github.com/armbian/build/pull/6934)
* [mainline-kernel: bump to `6.10-rc7` by @rpardini](https://github.com/armbian/build/pull/6935)
* [wifi: rtl8852bs: add driver for family instead of board by @amazingfate](https://github.com/armbian/build/pull/6932)
* [Desktops: replace missing packages with correct ones by @igorpecovnik](https://github.com/armbian/build/pull/6939)
* [firstlogin: quote values if space is legal by @jkt628](https://github.com/armbian/build/pull/6942)
* [rockchip-rk35xx-vendor enable rtw89_8852be as module by @alexl83](https://github.com/armbian/build/pull/6947)
* [sunxi-6.1: Reverse commit 75317a0, fix real reason inability to load kernel by @The-going](https://github.com/armbian/build/pull/6945)
* [BananaPi CM4/M2S: `Bump u-boot to v2024.07` by @pyavitz](https://github.com/armbian/build/pull/6943)
* [u-boot: 2024.07: fix boot from btrfs by @alex3d](https://github.com/armbian/build/pull/6946)
* [Move teres-i in supported by @Kreyren](https://github.com/armbian/build/pull/6948)
* [Add Libre Computer Alta and Solitude by @Tonymac32](https://github.com/armbian/build/pull/6952)
* [SpacemiT: BananaPi F3: U-Boot: use TAG and add SCRIPT support. by @pyavitz](https://github.com/armbian/build/pull/6953)
* [SpacemiT: BananaPi F3: `update to BL v1.0.8` by @pyavitz](https://github.com/armbian/build/pull/6954)
* [cli: uboot: Move `uboot_cflags` variable to before its first use by @ColorfulRhino](https://github.com/armbian/build/pull/6960)
* [actions: forked-helper: Don't escape multiline strings by @ColorfulRhino](https://github.com/armbian/build/pull/6961)
* [Trixie: remove non-existing packages from Budgie desktop by @igorpecovnik](https://github.com/armbian/build/pull/6959)
* [SpacemiT: Legacy: Wireless RTL8852BS: `Fixups` by @pyavitz](https://github.com/armbian/build/pull/6957)
* [VIM1S/4: follow Khadas's branch for u-boot by @viraniac](https://github.com/armbian/build/pull/6955)
* [add customized GHCR_MIRROR_ADDRESS support by @amazingfate](https://github.com/armbian/build/pull/6951)
* [actions: Create workflow to update shell tools via auto-PR by @ColorfulRhino](https://github.com/armbian/build/pull/6922)
* [extensions: Establish some consistency with extension logging by @ColorfulRhino](https://github.com/armbian/build/pull/6920)
* [rk35xx-vendor: bump to latest sdk release rkr3 by @amazingfate](https://github.com/armbian/build/pull/6853)
* [JetHome: Update bsp: fix jethub-init to support /etc/defaults by @adeepn](https://github.com/armbian/build/pull/6970)
* [add rk3576 support to rk35xx and armsom sige5 by @amazingfate](https://github.com/armbian/build/pull/6554)
* [Enable sound and battery for Retro Lite CM5 by @ginkage](https://github.com/armbian/build/pull/6971)
* [Bump koalaman/shellcheck from 0.9.0 to 0.10.0 in `lib/functions/general/shellcheck.sh` by @github-actions](https://github.com/armbian/build/pull/6963)
* [build(deps): bump setuptools from 70.2.0 to 70.3.0 by @dependabot](https://github.com/armbian/build/pull/6950)
* [Bump oras-project/oras from 0.16.0 to 1.2.0 in `lib/functions/general/oci-oras.sh` by @github-actions](https://github.com/armbian/build/pull/6964)
* [Bump sharkdp/bat from 0.23.0 to 0.24.0 in `lib/functions/general/bat-cat.sh` by @github-actions](https://github.com/armbian/build/pull/6965)
* [Add board config for Retro Lite CM5 by @ginkage](https://github.com/armbian/build/pull/6972)
* [oci-oras: fix for ORAS > 1.x, as it now requires `HOME` to be set (fixes `download-artifact`) by @rpardini](https://github.com/armbian/build/pull/6976)
* [mesa-vpu: use kisak mesa ppa instead of oibaf by @amazingfate](https://github.com/armbian/build/pull/6979)
* [utils-dpkgdeb: force rebuild of all artifacts, due to https://github.com/armbian/build/pull/6964 (ORAS change) by @rpardini](https://github.com/armbian/build/pull/6977)
* [Temporally move TI build targets to EOS as Git is out of reach by @igorpecovnik](https://github.com/armbian/build/pull/6981)
* [urgent: Hotfix for rk3399 boot by @paolosabatino](https://github.com/armbian/build/pull/6982)
* [Bump rockchip64 edge kernel to 6.10 by @paolosabatino](https://github.com/armbian/build/pull/6980)
* [rockchip: bump edge kernel to 6.10 by @paolosabatino](https://github.com/armbian/build/pull/6975)
* [Fix rtl8189fs WiFi driver by @schwar3kat](https://github.com/armbian/build/pull/6984)
* [Update odroidxu4-current to 6.6.41 by @belegdol](https://github.com/armbian/build/pull/6985)
* [build(deps): bump setuptools from 70.3.0 to 71.1.0 by @dependabot](https://github.com/armbian/build/pull/6983)
* [Add HDMI-rx to linux 6-10 for rk3588 by @benhoff](https://github.com/armbian/build/pull/6986)
* [SpacemiT: `write_uboot_platform`: eMMC Support by @pyavitz](https://github.com/armbian/build/pull/6958)
* [fix rk3568-roc-pc by @chainsx](https://github.com/armbian/build/pull/6992)
* [Fixed Tinker-edge-r HDMI 4K bug by @ARC-MX](https://github.com/armbian/build/pull/6991)
* [Fix for no network inside Docker container by @igorpecovnik](https://github.com/armbian/build/pull/6990)
* [add new board armsom-aim7-io by @amazingfate](https://github.com/armbian/build/pull/6987)
* [Repo management: rework to increase reliability and speed by @igorpecovnik](https://github.com/armbian/build/pull/6924)
* [add new board RK3328 Heltec HT-M2808 by @sicXnull](https://github.com/armbian/build/pull/6989)
* [mesa-vpu: install backported mesa from obs for bookworm panthor driver by @amazingfate](https://github.com/armbian/build/pull/6994)
* [Awarding regular contributors - adding a special PR tag by @igorpecovnik](https://github.com/armbian/build/pull/6997)
* [UEFI x86 and arm64: Bump EDGE kernels to 6.10.y by @igorpecovnik](https://github.com/armbian/build/pull/6996)
* [Debian: drop support for Budgie on Trixe / Bookworm.  by @igorpecovnik](https://github.com/armbian/build/pull/7001)
* [rockchip64-edge: add rkvdec2 for rk356x by @amazingfate](https://github.com/armbian/build/pull/6804)
* [Switch Retro Lite CM5 back to legacy U-Boot by @ginkage](https://github.com/armbian/build/pull/7004)
* [mesa-vpu: install chromium package instead of chromium-browser by @efectn](https://github.com/armbian/build/pull/7005)
* [Extend mesa-vpu extension to load unpatched Chromium by default by @igorpecovnik](https://github.com/armbian/build/pull/6657)
* [sun55iw3-syterkit: update kernel config by @chainsx](https://github.com/armbian/build/pull/7003)
* [Meson64 edge to 6.10 by @SteeManMI](https://github.com/armbian/build/pull/7000)
* [kernel: meson-s4t7: update config to match latest fenix changes by @viraniac](https://github.com/armbian/build/pull/7013)
* [Update odroidxu4-current to 6.6.43 by @belegdol](https://github.com/armbian/build/pull/7014)
* [thinkpad-x13s: bump to jhovold's 6.10 (from -rc7) by @rpardini](https://github.com/armbian/build/pull/7016)
* [Update sunxi-6.6, switch to v6.6.43 by @The-going](https://github.com/armbian/build/pull/6887)
* [build(deps): bump setuptools from 71.1.0 to 72.1.0 by @dependabot](https://github.com/armbian/build/pull/7009)
* [build(deps): bump ossf/scorecard-action from 2.3.3 to 2.4.0 by @dependabot](https://github.com/armbian/build/pull/7008)
* [Adjust patches that are broken or they found a way upstream by @igorpecovnik](https://github.com/armbian/build/pull/7022)
* [Update board config h96-max to mainline u-boot by @hqnicolas](https://github.com/armbian/build/pull/7021)
* [Repo management: base-files are placed under wrong repo key by @igorpecovnik](https://github.com/armbian/build/pull/7019)
* [config: rk35xx: vendor: enable CONFIG_NVMEM_ROCKCHIP_OTP by @amazingfate](https://github.com/armbian/build/pull/7024)
* [Cosmetic fix: do not show repository keys that doesn't exits by @igorpecovnik](https://github.com/armbian/build/pull/7023)
* [Set fixed MAC address for Nanaopi R6S series by @igorpecovnik](https://github.com/armbian/build/pull/7028)
* [bsp: armbian-install: fix the search for eMMC and SD card devices by @The-going](https://github.com/armbian/build/pull/7017)
* [Move meson edge 6.10 by @SteeManMI](https://github.com/armbian/build/pull/7010)
* [Armsom5 - switch to vendor branch and add BOARD_MAINTAINER field to suppress warnings by @igorpecovnik](https://github.com/armbian/build/pull/7026)
* [Re-enabling KDE Neon Jammy builds by @igorpecovnik](https://github.com/armbian/build/pull/7031)
* [Meson 6.10: adjust patches to align with upstream changes by @igorpecovnik](https://github.com/armbian/build/pull/7034)
* [Bump Marvell mvebu EDGE family to 6.10.y by @igorpecovnik](https://github.com/armbian/build/pull/7029)
* [Add latest Linux Mint versions, Virginia and Wilma, to supported hosts. by @schwar3kat](https://github.com/armbian/build/pull/7033)
* [MBa8MPxL fixes and updates by @tq-schmiedel](https://github.com/armbian/build/pull/7036)
* [build(deps): bump actions/upload-artifact from 4.3.4 to 4.3.5 by @dependabot](https://github.com/armbian/build/pull/7040)
* [Odroid XU4: bump EDGE kernel to 6.10.y by @igorpecovnik](https://github.com/armbian/build/pull/7039)
* [Udoo & Cubox: imx6: bump EDGE kernel to 6.10.y by @igorpecovnik](https://github.com/armbian/build/pull/7038)
* [RaspberryPi: bump EDGE kernel to 6.10.y by @igorpecovnik](https://github.com/armbian/build/pull/7037)
* [Improve partitioning, set correct partition type UUID for root filesystem by @ColorfulRhino](https://github.com/armbian/build/pull/6923)
* [MBa8MPxL: rework uboot patches by @tq-schmiedel](https://github.com/armbian/build/pull/7044)
* [Clarify label for entering giveaway - code completion, all authors counts by @igorpecovnik](https://github.com/armbian/build/pull/7035)
* [Odroid XU4: Remove deprecated patches on CURRENT branch by @igorpecovnik](https://github.com/armbian/build/pull/7050)
* [uboot: rk3576: add patches to enable tf card boot by @amazingfate](https://github.com/armbian/build/pull/7049)
* [nanopi-r5c: enable KASLR (current|edge) by @alexl83](https://github.com/armbian/build/pull/7047)
* [orangepi5-plus: patch u-boot 2024.07 to support KASLR by @alexl83](https://github.com/armbian/build/pull/7046)
* [orangepi5: fix SPI flash boot by @efectn](https://github.com/armbian/build/pull/7053)
* [sunxi-6.9: Add megous patches and switch EDGE to tag:v6.9.12 by @The-going](https://github.com/armbian/build/pull/6941)
* [add general 2024.07 patches to orangepi5-plus u-boot by @alexl83](https://github.com/armbian/build/pull/7057)
* [nanopi-r5c: add general u-boot 2024.07 patches by @alexl83](https://github.com/armbian/build/pull/7056)
* [Send summaries of PR and merges to main chat by @EvilOlaf](https://github.com/armbian/build/pull/7060)
* [BigTreeTech CB1 upstreaming by @JohnTheCoolingFan](https://github.com/armbian/build/pull/6656)
* [disable saving state for invalid leds brought up in latest kernels by @alexl83](https://github.com/armbian/build/pull/7062)
* [Fix armbian-firmware-full package build. by @h-s-c](https://github.com/armbian/build/pull/7045)
* [BigTreeTech CB1: current: Enable IR Receiver by @JohnTheCoolingFan](https://github.com/armbian/build/pull/7066)
* [Allwinner legacy and current - bump to latest version by @igorpecovnik](https://github.com/armbian/build/pull/7027)
* [Fixed tinker-edgr-r board GPU bug, drivers:regulator:fan53555:add new device chip id by @ARC-MX](https://github.com/armbian/build/pull/6998)
* [Link to the actual pr rather than commit with no reference by @EvilOlaf](https://github.com/armbian/build/pull/7067)
* [Discord: fix pr being announce multiple times by @EvilOlaf](https://github.com/armbian/build/pull/7070)
* [RaspberryPi: Rewrite kernel configs for legacy and current by @igorpecovnik](https://github.com/armbian/build/pull/7068)
* [UEFI kernels: rewrite kernel config for legacy - current - edge by @igorpecovnik](https://github.com/armbian/build/pull/7069)
* [Add aic8800 driver for Rock 3C variant by @Zokhoi](https://github.com/armbian/build/pull/6672)
* [Prevent running announce script in forks by @igorpecovnik](https://github.com/armbian/build/pull/7073)
* [fix firefly itx3588j u-boot patches not applied by @SeeleVolleri](https://github.com/armbian/build/pull/7063)
* [aic8800 DKMS driver: fix logic when extension is used by @igorpecovnik](https://github.com/armbian/build/pull/7074)
* [build(deps): bump actions/upload-artifact from 4.3.5 to 4.3.6 by @dependabot](https://github.com/armbian/build/pull/7072)
* [build(deps): bump pyyaml from 6.0.1 to 6.0.2 by @dependabot](https://github.com/armbian/build/pull/7071)
* [attempt to fix pr announce for all contributors by @EvilOlaf](https://github.com/armbian/build/pull/7081)
* [Add board Alfred Smart Gateway GZ80X by @pyavitz](https://github.com/armbian/build/pull/7058)
* [JetHome: Put module blacklist in the board configs of the respective boards by @adeepn](https://github.com/armbian/build/pull/7076)
* [Gateway GZ80X: `use actual u-boot.bin` by @pyavitz](https://github.com/armbian/build/pull/7085)
* [JetHome: fix uboot patchset for JetHub D2 by @adeepn](https://github.com/armbian/build/pull/7084)
* [meson64: refresh `drv-spi-spidev-remove-warnings.patch` by @alexl83](https://github.com/armbian/build/pull/7089)
* [JetHome: Update JetHub D2 dts by @adeepn](https://github.com/armbian/build/pull/7092)
* [rockchip64: refresh `drv-spi-spidev-remove-warnings.patch` by @alexl83](https://github.com/armbian/build/pull/7088)
* [Support kernel compilation with Clang/LLVM by @Randl](https://github.com/armbian/build/pull/7086)
* [rockchip64: Enable `CONFIG_SECURITY_DMESG_RESTRICT` kernel option by @alexl83](https://github.com/armbian/build/pull/7080)
* [JetHome: update list of preinstalled packages for JetHub devices by @adeepn](https://github.com/armbian/build/pull/7093)
* [RFC: provide KASLR support to u-boot v2024.07 general availability by @alexl83](https://github.com/armbian/build/pull/7078)
* [Change KBUILD to `build@armbian` for kernel builds by @ColorfulRhino](https://github.com/armbian/build/pull/6909)
* [rootfs: add comment to force rootfs rebuild by @igorpecovnik](https://github.com/armbian/build/pull/7097)
* [Mesa extension: adjust KDE related troubles with packages downgrade by @igorpecovnik](https://github.com/armbian/build/pull/7098)
* [sunxi 6.10: Add megous patches by @The-going](https://github.com/armbian/build/pull/7095)
* [rockchip-rk3588: Bump `edge` kernel from 6.10 to 6.11-rc and `current` from 6.8 to 6.10 by @efectn](https://github.com/armbian/build/pull/7015)
* [fix ps4 controllers and clones on rk3588 vendor and legacy kernel by @monkaBlyat](https://github.com/armbian/build/pull/7096)
* [actions: forked-helper: Run only if secret is set and simplify workflow by @ColorfulRhino](https://github.com/armbian/build/pull/7094)
* [Fix loop device search in docker when there are no loop devices before container launch by @JohnTheCoolingFan](https://github.com/armbian/build/pull/7090)
* [build-framework: Switch to next VERSION and update main README by @igorpecovnik](https://github.com/armbian/build/pull/7083)
* [rockchip-rk3588: Enable `CONFIG_SECURITY_DMESG_RESTRICT` kernel option by @alexl83](https://github.com/armbian/build/pull/7079)
* [KDE Neon: hack must be implemented only on Ubuntu Noble / Oracular by @igorpecovnik](https://github.com/armbian/build/pull/7104)
* [Revert "Temporally move TI build targets to EOS as Git is out of reach" by @igorpecovnik](https://github.com/armbian/build/pull/7105)
* [Release: board status check and adjustment by @igorpecovnik](https://github.com/armbian/build/pull/7103)
* [Add Board X96Q TV Box LPDDR3 H313 by @sicXnull](https://github.com/armbian/build/pull/7101)
* [Discord announcement: push only when label "Needs review" is set by @igorpecovnik](https://github.com/armbian/build/pull/7075)
* [WIP: add initial support for Youyeetoo R1 V3 by @SuperKali](https://github.com/armbian/build/pull/7108)
* [Build automation: update kernel test targets for many boards by @igorpecovnik](https://github.com/armbian/build/pull/7116)
* [Build automation: Adjust test targets for remaining boards by @igorpecovnik](https://github.com/armbian/build/pull/7117)
* [cli: packages: use iputils-ping instead of inetutils-ping by @amazingfate](https://github.com/armbian/build/pull/7118)
* [rockchip-rk3588: current: add `rfkill-bt` device node to Radxa Rock-5B by @alexl83](https://github.com/armbian/build/pull/7114)
* [BananaPi M2S: `remove fan control` by @pyavitz](https://github.com/armbian/build/pull/7119)
* [Gateway AM-GZ80x: `Re-brand as Amper & update u-boot to v2024.04` by @pyavitz](https://github.com/armbian/build/pull/7113)
* [Update odroidxu4-current to 6.6.47 by @belegdol](https://github.com/armbian/build/pull/7111)
* [rk3588: Bump kernel from 6.11-rc3 to 6.11-rc4 by @ColorfulRhino](https://github.com/armbian/build/pull/7109)
* [Add OpenSBI compilation to D1 by @Randl](https://github.com/armbian/build/pull/7077)
* [Debian Trixie Cinnamon: remove deprecated package by @igorpecovnik](https://github.com/armbian/build/pull/7120)
* [Framework: disable armbian repository while generating rootfs cache by @igorpecovnik](https://github.com/armbian/build/pull/7123)
* [build(deps): bump setuptools from 72.1.0 to 72.2.0 by @dependabot](https://github.com/armbian/build/pull/7107)
* [Framework: expand package installing function with custom parameter by @igorpecovnik](https://github.com/armbian/build/pull/7124)
* [Expand MESA extension fix to Jammy userspace by @igorpecovnik](https://github.com/armbian/build/pull/7125)
* [Framework: bump tmpfs size as we are going over by @igorpecovnik](https://github.com/armbian/build/pull/7126)
* [Mesa fixes applies only to armhf and arm64. Adjusting by @igorpecovnik](https://github.com/armbian/build/pull/7128)
* [Repository management: add config driven BSP package modification by @igorpecovnik](https://github.com/armbian/build/pull/7129)
* [Board config ayn-odin2 temporally disable broken build by @igorpecovnik](https://github.com/armbian/build/pull/7134)
* [Improved freezing mechanism and README by @igorpecovnik](https://github.com/armbian/build/pull/7133)

## v24.5.5 (2024-25-7)

* Recreated Bananapi M7, Khadas Edge 2, Orangepi 5, Orangepi 5 Plus
* Sent rk35xx-vendor (6.1.75) and rk35xx-edge (6.10.y) kernel to the stable repository

## v24.5.4 (2024-21-7)

* Recreated Radxa ROCK5 ITX images
* Recreated Olimex Teres images since they were broken
* Sent sunxi64-current kernel to the stable repository
* Sent rk35xx-vendor kernel to the stable repository

## v24.5.3 (2024-01-7)

* Recreated Helios64 since board was moved under supported
* Sent rockchip64-current kernel to the stable repository

## v24.5.2 (2024-18-6)

* Recreated [Khadas Edge 2 images](https://www.armbian.com/khadas-edge-2/) due to lack of 3D / video acceleration support in 6.1.y
* Recreated Orangepi 5 plus images due to missing support for 32GB variant
* Recreated Odroid M1 images with new minimal images and KDE Neon desktop
* Added Orangepi 5 Pro images

## v24.5.1 (2024-25-5)

### Closed projects

* [AR-1759](https://armbian.atlassian.net/browse/AR-1759) Improve Khadas support
* [AR-1988](https://armbian.atlassian.net/browse/AR-1988) Resolve Rockchip patch maintenance nightmare
* [AR-2087](https://armbian.atlassian.net/browse/AR-2087) Add functionality to freeze git resources
* [AR-2095](https://armbian.atlassian.net/browse/AR-2095) Improve support for Radxa Rock S 0 and test USB and Ethernet
* [AR-2100](https://armbian.atlassian.net/browse/AR-2100) Add KDE Neon desktop to Armbian Jammy
* [AR-2144](https://armbian.atlassian.net/browse/AR-2144) Add support for the Orange Pi 5 Pro
* [AR-2145](https://armbian.atlassian.net/browse/AR-2145) Add mainline Panthor driver to 6.1
* [AR-2148](https://armbian.atlassian.net/browse/AR-2148) Add board Bananapi M7 to vendor kernel 5.10 and 6.1
* [AR-2153](https://armbian.atlassian.net/browse/AR-2153) Add board FriendlyElec CM3588 NAS board
* [AR-2156](https://armbian.atlassian.net/browse/AR-2156) Add support for Radxa ROCK 5 ITX
* [AR-2158](https://armbian.atlassian.net/browse/AR-2158) Add board Radxa Zero 3 with overlays
* [AR-2171](https://armbian.atlassian.net/browse/AR-2171) Drop DEBUG\_KERNEL/DEBUG\_INFO disables; force EXPERT=y and bring back CONFIG\_GPIO\_SYSFS=y for all kernels
* [AR-2172](https://armbian.atlassian.net/browse/AR-2172) Update meson edge to 6.8 kernel
* [AR-2173](https://armbian.atlassian.net/browse/AR-2173) Change the way APT repository is getting updated
* [AR-2174](https://armbian.atlassian.net/browse/AR-2174) Thinkpad-x13s: drop steev's kernel and switch to jhovold's wip/sc8280xp-6.9
* [AR-2178](https://armbian.atlassian.net/browse/AR-2178) Fix u-boot build for Odroid C1 \+ fix onboard usb hub on Odroid C1
* [AR-2179](https://armbian.atlassian.net/browse/AR-2179) Phytium\_embedded: update kernel config from phytium repo
* [AR-2180](https://armbian.atlassian.net/browse/AR-2180) Rockchip-rk3308-current: sakura pi rk3308b adds kernel 6.6 and 6.8 support
* [AR-2185](https://armbian.atlassian.net/browse/AR-2185) Switch odroidxu4-current kernel to 6.6
* [AR-2186](https://armbian.atlassian.net/browse/AR-2186) VIM1S/VIM4: Allow building on arm64 platform
* [AR-2187](https://armbian.atlassian.net/browse/AR-2187) VIM1S/VIM4: Add support for emmc \+ NVME/USB booting
* [AR-2196](https://armbian.atlassian.net/browse/AR-2196) CLI: Add command "dts-check" to validate dts files and improve board & patch development overall
* [AR-2197](https://armbian.atlassian.net/browse/AR-2197) Add support for allwinner T527 Avaota-A1
* [AR-2203](https://armbian.atlassian.net/browse/AR-2203) Rockchip-rk3308-current: add support for sakura pi rk3308b
* [AR-2208](https://armbian.atlassian.net/browse/AR-2208) Update sm8250: kernel add current and edge branch And Update Odin2: add kernel update hook script
* [AR-2212](https://armbian.atlassian.net/browse/AR-2212) H96-TVbox-rk3566 Board Bring Up
* [AR-2215](https://armbian.atlassian.net/browse/AR-2215) Enable vendor kernel branch on Khadas Edge 2
* [AR-2216](https://armbian.atlassian.net/browse/AR-2216) arm64: swiotlb: Reduce the default size if no ZONE\_DMA bouncing needed
* [AR-2218](https://armbian.atlassian.net/browse/AR-2218) FriendlyElec CM3588-NAS: device tree fixes & improvements
* [AR-2222](https://armbian.atlassian.net/browse/AR-2222) Rock-5b: move edge \(only\) to mainline/Kwiboo u-boot 2024.04
* [AR-2226](https://armbian.atlassian.net/browse/AR-2226) FriendlyElec CM3588 NAS: Add mainline kernel support
* [AR-2227](https://armbian.atlassian.net/browse/AR-2227) mekotronics: mainline u-boot \(next/Kwiboo rk3xxx-2024.04, generic-rk3588\_defconfig\)
* [AR-2229](https://armbian.atlassian.net/browse/AR-2229) rk3588: vendor-boogie-panthor
* [AR-2230](https://armbian.atlassian.net/browse/AR-2230) rockchip-rk3588: it's vendor boogie panthor time \(experimental\)
* [AR-2235](https://armbian.atlassian.net/browse/AR-2235) Bump meson64 edge from 6.7 to 6.8
* [AR-2246](https://armbian.atlassian.net/browse/AR-2246) Add support for Radxa ZERO 3E/3W
* [AR-2250](https://armbian.atlassian.net/browse/AR-2250) Rock 4C\+: update and cleanup boot config
* [AR-2265](https://armbian.atlassian.net/browse/AR-2265) cli: rewrite-<uboot,kernel>-patches: rewrite only patches needing a rebase
* [AR-2267](https://armbian.atlassian.net/browse/AR-2267) Add SK-AM68 board support
* [AR-2270](https://armbian.atlassian.net/browse/AR-2270) rk35xx/rockchip-rk3588: vendor: switch to armbian/linux-rockchip#rk-6.1-rkr1
* [AR-2274](https://armbian.atlassian.net/browse/AR-2274) Add tqma8mpxl boards support
* [AR-2276](https://armbian.atlassian.net/browse/AR-2276) cli: introduce rewrite-uboot-patches cli command, works similar to the kernel one
* [AR-2281](https://armbian.atlassian.net/browse/AR-2281) Add csc hinlink h6xk boards
* [AR-2282](https://armbian.atlassian.net/browse/AR-2282) Kernel: Enable \*NVMe-over-TCP\* for rk35xx/rk3588/rockchip64/uefi/wsl
* [AR-2289](https://armbian.atlassian.net/browse/AR-2289) qemu-uefi-x86: new board for virtualized environment with serial console support, kernel boot messages
* [AR-2290](https://armbian.atlassian.net/browse/AR-2290) cli: introduce kernel-dtb cli command, to build only DTB, and output full preprocessed dts source
* [AR-2291](https://armbian.atlassian.net/browse/AR-2291) cli: introduce inventory-boards cli command, for hopefully painless & useful one-board-per-line CSV output
* [AR-2292](https://armbian.atlassian.net/browse/AR-2292) Add board: FriendlyElec CM3588 NAS
* [AR-2293](https://armbian.atlassian.net/browse/AR-2293) Add vendor branch for new 6.1-rkr1 BSP vendor kernel, and keep legacy for the 5.10-rkr6 BSP vendor kernel
* [AR-2294](https://armbian.atlassian.net/browse/AR-2294) Phytium-embedded: add support for 4Gb Phytium Pi
* [AR-2295](https://armbian.atlassian.net/browse/AR-2295) Rockchip RK3588-edge: rewrite kernel patches and configs against v6.8-rc6
* [AR-2297](https://armbian.atlassian.net/browse/AR-2297) Refactor automatic armbian-firstlogin
* [AR-2299](https://armbian.atlassian.net/browse/AR-2299) Develop build config for board BananaPi M4 Zero
* [AR-2301](https://armbian.atlassian.net/browse/AR-2301) Develop and add Ayn Odin2 build config
* [AR-2307](https://armbian.atlassian.net/browse/AR-2307) Thinkpad-x13s: bump to steev's 6.7.y; enable noble userspace; bump alsa-ucm-conf hack to master
* [AR-2308](https://armbian.atlassian.net/browse/AR-2308) Debootstrap: use latest git for Ubuntu/Debian debootstrap instead of host-installed
* [AR-2322](https://armbian.atlassian.net/browse/AR-2322) Develop PPA for \(patched\) aarch64 Chromium
* [AR-2327](https://armbian.atlassian.net/browse/AR-2327) Add support for RK3588 based Cool PI CM5 EVB

### Closed Tasks

* [AR-2043](https://armbian.atlassian.net/browse/AR-2043) armbian-install should do rsync --one-file-system
* [AR-2057](https://armbian.atlassian.net/browse/AR-2057) enable DRBD in the kernel config of mvebu
* [AR-2077](https://armbian.atlassian.net/browse/AR-2077) Orangepi 5: update memory blobs
* [AR-2079](https://armbian.atlassian.net/browse/AR-2079) Enable ssdm autologin and apply theme
* [AR-2092](https://armbian.atlassian.net/browse/AR-2092) Drop repository for unsupported Releases
* [AR-2096](https://armbian.atlassian.net/browse/AR-2096) USB Gadget mode for rockchip 32 bit
* [AR-2101](https://armbian.atlassian.net/browse/AR-2101) Cleanup desktop packages
* [AR-2102](https://armbian.atlassian.net/browse/AR-2102) Adjusting pull request template for documentation
* [AR-2103](https://armbian.atlassian.net/browse/AR-2103) Disable automatic enablement of Nvidia proprietary drivers on x86
* [AR-2105](https://armbian.atlassian.net/browse/AR-2105) Rockchip bootscripts: \`Failed to load '...-fixup.scr'\` and \`Unknown command 'kaslrseed'\`
* [AR-2110](https://armbian.atlassian.net/browse/AR-2110) Fix rtl8723cs for kernel 6.8
* [AR-2111](https://armbian.atlassian.net/browse/AR-2111) Bump rockchip edge kernel to 6.8
* [AR-2112](https://armbian.atlassian.net/browse/AR-2112) Bump rockchip64 edge kernel to 6.8
* [AR-2131](https://armbian.atlassian.net/browse/AR-2131) Builds fail for EOS distributions \(for example focal\)
* [AR-2132](https://armbian.atlassian.net/browse/AR-2132) Fail at check\_loop\_device: device node doesn't exist and \`$LOOP=\`
* [AR-2135](https://armbian.atlassian.net/browse/AR-2135) Move Firefly station M2 to RK35xx family
* [AR-2136](https://armbian.atlassian.net/browse/AR-2136) Synchronise Rock 5 ITX from Radxa repository
* [AR-2137](https://armbian.atlassian.net/browse/AR-2137) Cleanup and merge OPi5 Plus device tree 
* [AR-2138](https://armbian.atlassian.net/browse/AR-2138) Add support for the Orange Pi 5 Pro to 6.1 
* [AR-2139](https://armbian.atlassian.net/browse/AR-2139) Add armsom sige1 support to 6.1
* [AR-2140](https://armbian.atlassian.net/browse/AR-2140) Add Radxa Rock 5c support to 6.1
* [AR-2141](https://armbian.atlassian.net/browse/AR-2141) Add dynamic-power-coefficient properties to all cores
* [AR-2142](https://armbian.atlassian.net/browse/AR-2142) Sync Panthor with drm-misc-next by adding missing commits
* [AR-2146](https://armbian.atlassian.net/browse/AR-2146) Upgrade RKNPU driver to 0.9.6
* [AR-2147](https://armbian.atlassian.net/browse/AR-2147) Cleanup Khadas edge 2 device tree
* [AR-2149](https://armbian.atlassian.net/browse/AR-2149) Use simple-audio-card for HDMI sound for rk3528
* [AR-2151](https://armbian.atlassian.net/browse/AR-2151) Carrying over some CM5-related commits from Radxa 3.4 branch
* [AR-2152](https://armbian.atlassian.net/browse/AR-2152) Add missing led gpio for hinlink h66k
* [AR-2155](https://armbian.atlassian.net/browse/AR-2155) Add cooling-maps and pwm-fan support for Station M3
* [AR-2159](https://armbian.atlassian.net/browse/AR-2159) Allow FFmpeg to capture from HDMI input
* [AR-2160](https://armbian.atlassian.net/browse/AR-2160) Add Ubuntu Noble support for Rockchip multimedia extension
* [AR-2161](https://armbian.atlassian.net/browse/AR-2161) Switch CM3588 NAS to kwiboo uboot
* [AR-2162](https://armbian.atlassian.net/browse/AR-2162) Declare Ubuntu Noble as supported build target
* [AR-2164](https://armbian.atlassian.net/browse/AR-2164) Rockchip rk3588 edge: add Hantro G1 VDPU and RGA2
* [AR-2165](https://armbian.atlassian.net/browse/AR-2165) Rockchip RK3588 EDGE: add generic pwm overlays from vendor kernel
* [AR-2166](https://armbian.atlassian.net/browse/AR-2166) rk35xx: drop vendor-boogie-panthor BRANCH; it has been integrated into vendor
* [AR-2167](https://armbian.atlassian.net/browse/AR-2167) Multiple boards: fixes for board file syntax / missing vars \(fixing JSON matrix prepare
* [AR-2168](https://armbian.atlassian.net/browse/AR-2168) VIM1S/VIM4: initialize video firmware symlink
* [AR-2169](https://armbian.atlassian.net/browse/AR-2169) Use oibaf and v4l2 extension in desktops only
* [AR-2170](https://armbian.atlassian.net/browse/AR-2170) Treat sid and unstable as synonyms in distro-specific.sh
* [AR-2175](https://armbian.atlassian.net/browse/AR-2175) Add latest Ubuntu development branch Oracular
* [AR-2176](https://armbian.atlassian.net/browse/AR-2176) Armsom rk3588 boards: use radxa's new uboot
* [AR-2177](https://armbian.atlassian.net/browse/AR-2177) Phytium\_embedded: update phytium u-boot binary
* [AR-2182](https://armbian.atlassian.net/browse/AR-2182) Enable android binder to support android containers like anbox or waydroid on rk3588 edge kernel builds
* [AR-2190](https://armbian.atlassian.net/browse/AR-2190) Rockchip: bump rk322x u-boot to v2024.01 and support HDMI
* [AR-2191](https://armbian.atlassian.net/browse/AR-2191) Switch Radxa u-boot to more recent branch
* [AR-2192](https://armbian.atlassian.net/browse/AR-2192) Odroidn2: u-boot: fix eMMC stability
* [AR-2198](https://armbian.atlassian.net/browse/AR-2198) Rockchip64: cleanup rk3318-box hdmi patches
* [AR-2199](https://armbian.atlassian.net/browse/AR-2199) Add current kernel support for phytium-embedded
* [AR-2201](https://armbian.atlassian.net/browse/AR-2201) Board: h96 rk3566 HDMI sound & audio fix
* [AR-2202](https://armbian.atlassian.net/browse/AR-2202) Odin2 Use Custom ABL, boot from TF Card
* [AR-2204](https://armbian.atlassian.net/browse/AR-2204) H96-tvbox-3566 device tree fixes & improvements: wifi fix, Led and IR enable
* [AR-2206](https://armbian.atlassian.net/browse/AR-2206) rk35xx-vendor: enable panthor gpu driver
* [AR-2207](https://armbian.atlassian.net/browse/AR-2207) Rockchip64: bump rk3318-box uboot to v2024.01
* [AR-2209](https://armbian.atlassian.net/browse/AR-2209) Typo: while Fosstodon is the instance, Mastodon is the software used.
* [AR-2210](https://armbian.atlassian.net/browse/AR-2210) Rockchip64-edge: add pcie support to orangepi rk3399
* [AR-2214](https://armbian.atlassian.net/browse/AR-2214) Rockchip-rk3588-edge: opi5b: add support for pcie wifi 
* [AR-2217](https://armbian.atlassian.net/browse/AR-2217) rockchip-rk3588-edge: opi5: fix typec and add support for GPU
* [AR-2219](https://armbian.atlassian.net/browse/AR-2219) Unlock Code and Thunderbird from all distributions
* [AR-2223](https://armbian.atlassian.net/browse/AR-2223) Add bluedevil for bluetooth support
* [AR-2231](https://armbian.atlassian.net/browse/AR-2231) rockchip: rewrite dts for rock3c
* [AR-2233](https://armbian.atlassian.net/browse/AR-2233) DE: KDE: add package kscreen
* [AR-2236](https://armbian.atlassian.net/browse/AR-2236) Rockpro64: bump u-boot to v2024.04-rc4; use binman-produced bins
* [AR-2237](https://armbian.atlassian.net/browse/AR-2237) Fix kernel compilation for meson-s4t7 due to Khadas vendor common\_drivers not working without DEBUG enabled
* [AR-2238](https://armbian.atlassian.net/browse/AR-2238) Fix forced kernel options and make kernel-config consistent with rewrite-kernel-config
* [AR-2239](https://armbian.atlassian.net/browse/AR-2239) Rockchip RK3588 edge: enable nodes for armsom-sige7, rock 5a and h88k
* [AR-2240](https://armbian.atlassian.net/browse/AR-2240) armsom-sige7: add ap6275p wifi support
* [AR-2241](https://armbian.atlassian.net/browse/AR-2241) Rockchip-rk3588-edge: refresh cpufreq patches and auto fan control for Edge2
* [AR-2242](https://armbian.atlassian.net/browse/AR-2242) GH Actions: Beautify kernel hardening analysis
* [AR-2243](https://armbian.atlassian.net/browse/AR-2243) Khadas-vim3l/khadas-vim3: enable networking cmds in u-boot
* [AR-2244](https://armbian.atlassian.net/browse/AR-2244) Rockchip-rk3588-edge: khadas-edge2: add support for GPU and improve display modes
* [AR-2245](https://armbian.atlassian.net/browse/AR-2245) Build script: configuration: Check if ROOTFS\_TYPE is supported by build host
* [AR-2247](https://armbian.atlassian.net/browse/AR-2247) Create linux-libc-dev when building kernel packages
* [AR-2248](https://armbian.atlassian.net/browse/AR-2248) bsp-cli: include BOOT\_SOC to /etc/armbian-release and bsp-cli hash
* [AR-2255](https://armbian.atlassian.net/browse/AR-2255) Enable module snd\_aloop for linux-rk35xx legacy and vendor
* [AR-2260](https://armbian.atlassian.net/browse/AR-2260) BananaPi M4 Zero: add gpu and uart nodes
* [AR-2262](https://armbian.atlassian.net/browse/AR-2262) GH Actions: Kernel hardening analysis: Exclude RISC-V configs
* [AR-2266](https://armbian.atlassian.net/browse/AR-2266) Expand predicted size for rootfs for abl type of images
* [AR-2269](https://armbian.atlassian.net/browse/AR-2269) Extend PR template when asking for documentation
* [AR-2271](https://armbian.atlassian.net/browse/AR-2271) rk35xx-vendor: Add kernel patching config
* [AR-2272](https://armbian.atlassian.net/browse/AR-2272) rk35xx-vendor: add rk3528 and lima driver support 
* [AR-2275](https://armbian.atlassian.net/browse/AR-2275) GH Actions: Update forked-helper and add some doc on secrets in workflow's README.md
* [AR-2277](https://armbian.atlassian.net/browse/AR-2277) u-boot: rewrite/rebase u-boot patches for a few boards; bump odroidm1 and orangepi3b
* [AR-2280](https://armbian.atlassian.net/browse/AR-2280) Show correct reason about omit tmpfs usage if FORCE\_USE\_RAMDISK is set
* [AR-2286](https://armbian.atlassian.net/browse/AR-2286) BananaPi M4 Zero: enable 8821cu and blacklist rtw88\_8821cu
* [AR-2287](https://armbian.atlassian.net/browse/AR-2287) lib: drop old boot\_logo code; keep png/gif as they're used for plymouth
* [AR-2288](https://armbian.atlassian.net/browse/AR-2288) Rk35xx vendor kernel: add some network drivers
* [AR-2296](https://armbian.atlassian.net/browse/AR-2296) meson-6.7: Copy patches from 6.6
* [AR-2298](https://armbian.atlassian.net/browse/AR-2298) Prepare-host/host-release: enable noble for building
* [AR-2303](https://armbian.atlassian.net/browse/AR-2303) kernel: call make with INSTALL\_MOD\_STRIP=1 so modules are stripped
* [AR-2304](https://armbian.atlassian.net/browse/AR-2304) wsl2: arm64: current: DRM/FB stuff so wsl2-arm64 can be used in HyperV with video & keyboard
* [AR-2305](https://armbian.atlassian.net/browse/AR-2305) mekotronics 3588: add SRC\_CMDLINE, for use with u-boot-menu extension
* [AR-2306](https://armbian.atlassian.net/browse/AR-2306) khadas-vim3/khadas-vim3l: u-boot v2024.01: enable more compression, kaslr, and led config options via hook
* [AR-2324](https://armbian.atlassian.net/browse/AR-2324) Optimize the kernel device tree patch for rk3399-firefly
* [AR-2325](https://armbian.atlassian.net/browse/AR-2325) Give shellcheck directions \(to /dev/null for dynamic, to repo-relative path for static\) for all sourced references
* [AR-2328](https://armbian.atlassian.net/browse/AR-2328) Extensions: rk-panthor: mesa-oibaf \+ DEFAULT\_OVERLAYS="panthor-gpu"
* [AR-2333](https://armbian.atlassian.net/browse/AR-2333) Set linux-image packages to provide wireguard-modules
* [AR-2335](https://armbian.atlassian.net/browse/AR-2335) Add chromium v4l2 encoder/decoder udev rules for all boards

### Solved Bugs

* [AR-650](https://armbian.atlassian.net/browse/AR-650) Odroid N2\+ possible boot problems on eMMC
* [AR-1582](https://armbian.atlassian.net/browse/AR-1582) CI on our runners sometimes throws out error regarding loop devices
* [AR-2034](https://armbian.atlassian.net/browse/AR-2034) RockPI-S does WiFi broken on kernels >6.5
* [AR-2045](https://armbian.atlassian.net/browse/AR-2045) Resolve extensions rootfs encryption conflicts
* [AR-2070](https://armbian.atlassian.net/browse/AR-2070) VIM1S/VIM4: Booting from UHS sdcard only works intermittently
* [AR-2076](https://armbian.atlassian.net/browse/AR-2076) Fix random MAC address on Orangepi 5 series
* [AR-2080](https://armbian.atlassian.net/browse/AR-2080) Lightdm greeter is without wallpaper - black background
* [AR-2086](https://armbian.atlassian.net/browse/AR-2086) Home assistant supervised fails to install on Khadas VIM1S
* [AR-2090](https://armbian.atlassian.net/browse/AR-2090) Debootstrap is again too old for latest releases
* [AR-2094](https://armbian.atlassian.net/browse/AR-2094) Build failed during partprobing of /dev/loop device.
* [AR-2097](https://armbian.atlassian.net/browse/AR-2097) GH Actions: "Kernel hardening analysis \(pull request\)" kconfig-hardened-check: No such file or directory
* [AR-2098](https://armbian.atlassian.net/browse/AR-2098) Torrent generation fails silently
* [AR-2121](https://armbian.atlassian.net/browse/AR-2121) RockPi-S WiFi broken again on kernel's >6.7
* [AR-2125](https://armbian.atlassian.net/browse/AR-2125) Deboostrap trixie fails at stage 2 
* [AR-2143](https://armbian.atlassian.net/browse/AR-2143) Fix Orange Pi 5 Plus load average >= 1
* [AR-2150](https://armbian.atlassian.net/browse/AR-2150) Fixing deadlock issue with spin\_lock in interrupt handling
* [AR-2154](https://armbian.atlassian.net/browse/AR-2154) Fix CEC on rk356X on tv restart
* [AR-2157](https://armbian.atlassian.net/browse/AR-2157) Rock-5a: pull down data-strobe to fix emmc compatibility
* [AR-2163](https://armbian.atlassian.net/browse/AR-2163) Restore armbian-config desktop icon
* [AR-2181](https://armbian.atlassian.net/browse/AR-2181) Rockchip Rock 5C: Fix RK3582 with disabled rkvdec node
* [AR-2183](https://armbian.atlassian.net/browse/AR-2183) Fix memory size detection for 1.5GB Orange Pi Zero 3 board on v2024.01 u-boot release
* [AR-2184](https://armbian.atlassian.net/browse/AR-2184) rockchip64: rework drm hunk due to mainlined patch
* [AR-2188](https://armbian.atlassian.net/browse/AR-2188) Make debian/trixie debootstrap-able again
* [AR-2189](https://armbian.atlassian.net/browse/AR-2189) Fix PCIe for RK35xx\+Fix ROCK5A PCIe device tree
* [AR-2193](https://armbian.atlassian.net/browse/AR-2193) Hostdep fixes for Noble distutils and pyelftools removed hooks
* [AR-2200](https://armbian.atlassian.net/browse/AR-2200) Fixing broken device tree for H96 tvbox 3566
* [AR-2205](https://armbian.atlassian.net/browse/AR-2205) Fixing not operational USB port on Udoo quad
* [AR-2211](https://armbian.atlassian.net/browse/AR-2211) Ramlog: harden the zram mounting
* [AR-2213](https://armbian.atlassian.net/browse/AR-2213) Restore wireless functionality on Rock Pi S
* [AR-2220](https://armbian.atlassian.net/browse/AR-2220) Rockchip: update DTS patches for Orangepi R1 Plus
* [AR-2221](https://armbian.atlassian.net/browse/AR-2221) riscv64: fixes/skips for building \(sans Docker\) ON riscv64
* [AR-2224](https://armbian.atlassian.net/browse/AR-2224) Disable mtd-tools on Armbian Noble for armhf architecture
* [AR-2225](https://armbian.atlassian.net/browse/AR-2225) Fixing broken user space packages dependencies and small optimisations
* [AR-2228](https://armbian.atlassian.net/browse/AR-2228) RTW88: 6.x.y patches adjustment due to upstream changes
* [AR-2232](https://armbian.atlassian.net/browse/AR-2232) Raspberry 5 has troubles booting when faster memory access is enabled
* [AR-2234](https://armbian.atlassian.net/browse/AR-2234) BananaPi CM4/M2S: The fan on the unit is constantly running. So lets set thermal trip points
* [AR-2252](https://armbian.atlassian.net/browse/AR-2252) Rockchip RK3588 edge: fix wrong gpu node patch
* [AR-2253](https://armbian.atlassian.net/browse/AR-2253) Rockchip RK3588 edge: improve display modes support
* [AR-2273](https://armbian.atlassian.net/browse/AR-2273) Xiaomi elish fix 6.7: fixing broken dsi panel
* [AR-2283](https://armbian.atlassian.net/browse/AR-2283) Remove hard-coded defaults from repository management tool
* [AR-2285](https://armbian.atlassian.net/browse/AR-2285) Several small fixes for Banana Pi M4 Zero
* [AR-2300](https://armbian.atlassian.net/browse/AR-2300) Rockchip RK3588 edge: Orangepi 5 pluse: fix USB3 Host
* [AR-2309](https://armbian.atlassian.net/browse/AR-2309) Fixing small problems in wireless driver RTW88: RTL8822/21CU code
* [AR-2311](https://armbian.atlassian.net/browse/AR-2311) Meson64: fixing Librecomputer Lafrite boot failure
* [AR-2323](https://armbian.atlassian.net/browse/AR-2323) Resolving Armbian Noble incompatibility with Rockchip VPU extension
* [AR-2326](https://armbian.atlassian.net/browse/AR-2326) Radxa rock-5c: rename wireless interface name to a static one
* [AR-2329](https://armbian.atlassian.net/browse/AR-2329) Add new user to render group, otherwise the non-root user do not have access /dev/dri/renderD128 on RK3399
* [AR-2334](https://armbian.atlassian.net/browse/AR-2334) Resolve dependency issues with armbian-config

### Closed Sub-task

* [AR-2082](https://armbian.atlassian.net/browse/AR-2082) Make initial devicetree to make most parts work \(USB2, USB3, SD etc.\)
* [AR-2083](https://armbian.atlassian.net/browse/AR-2083) Add Type-C support
* [AR-2084](https://armbian.atlassian.net/browse/AR-2084) Make AP6275P work on upstream kernel
* [AR-2085](https://armbian.atlassian.net/browse/AR-2085) Add Khadas Edge2 support to upstream Khadas MCU driver

## v24.2.6 (2024-6-5)

* recreated images for [Bananapi CM40IO](https://www.armbian.com/bananapicm4io/), [Bananapi M7](https://www.armbian.com/bananapi-m7/)

## v24.2.5 (2024-4-2)

* recreated images for [Rpi5](https://www.armbian.com/rpi5b/) due to a [bug](https://github.com/armbian/build/pull/6461)

## v24.2.4 (2024-3-12)

* added KDE Neon 6 desktop images for generic UEFI targets, Orangepi 5 / 5+ (with new vendor kernel 6.1.y) and Odroid M1

## v24.2.3 (2024-2-26)

* recreated images for [Bigtreetech CB1](https://www.armbian.com/bigtreetech-cb1/)

## v24.2.1 (2024-02-18)

### Closed projects

* [AR-1657](https://armbian.atlassian.net/browse/AR-1657) Address DNS resolve with Debian Bookworm
* [AR-1797](https://armbian.atlassian.net/browse/AR-1797) Auto-testing: install all kernels that are defined
* [AR-1888](https://armbian.atlassian.net/browse/AR-1888) fix sluggish hdmi console for vim1s and vim4
* [AR-1988](https://armbian.atlassian.net/browse/AR-1988) Resolve Rockchip patch maintenance nightmare
* [AR-2061](https://armbian.atlassian.net/browse/AR-2061) Add Orangepi Zero3
* [AR-2062](https://armbian.atlassian.net/browse/AR-2062) Mixtile Blade 3 refactor / rockchip-rk3588 edge 6.7
* [AR-2063](https://armbian.atlassian.net/browse/AR-2063) Add new board of ASUS Tinker-Edge-R
* [AR-2064](https://armbian.atlassian.net/browse/AR-2064) Khadas VIM1S & VIM4 - 5.15 kernel bump
* [AR-2065](https://armbian.atlassian.net/browse/AR-2065) Add Xiaomi Mi10\(umi\) support
* [AR-2066](https://armbian.atlassian.net/browse/AR-2066) aml-s9xx-box: Update u-boot-s905x2-s922 to u-boot version 2024.01

### Closed Tasks
* [AR-1879](https://armbian.atlassian.net/browse/AR-1879) JetHome: update u-boot to 2023.10
* [AR-1985](https://armbian.atlassian.net/browse/AR-1985) Generate new function to display download links
* [AR-1990](https://armbian.atlassian.net/browse/AR-1990) Move forgotten overlays from Odroid M1
* [AR-2033](https://armbian.atlassian.net/browse/AR-2033) revert JetHub H1/D1 wifi driver from rtw88 to vendor
* [AR-1552](https://armbian.atlassian.net/browse/AR-1552) Rework support for jethub devices
* [AR-1696](https://armbian.atlassian.net/browse/AR-1696) Khadas Edge \(RK3399\) has wrong name and picture
* [AR-1737](https://armbian.atlassian.net/browse/AR-1737) Merge Odroid M1 into rockchip64 family
* [AR-1870](https://armbian.atlassian.net/browse/AR-1870) Git workaround failure
* [AR-1925](https://armbian.atlassian.net/browse/AR-1925) Move wifi-4003-uwe5622-adjust-for-rockchip to the wireless section
* [AR-1984](https://armbian.atlassian.net/browse/AR-1984) Move live patch to extension
* [AR-2000](https://armbian.atlassian.net/browse/AR-2000) Several small maintainace tasks
* [AR-2004](https://armbian.atlassian.net/browse/AR-2004) Add Ubuntu Noble to the build framework
* [AR-2005](https://armbian.atlassian.net/browse/AR-2005) Bump all current kernels to 6.6 LTS
* [AR-2012](https://armbian.atlassian.net/browse/AR-2012) Please set dpkg vendor to Armbian in all images
* [AR-2016](https://armbian.atlassian.net/browse/AR-2016) Patchset for Rockchip \(32b\) needs to be ported to 6.7
* [AR-2017](https://armbian.atlassian.net/browse/AR-2017) Patchset for Rockchip 64b needs to be ported to 6.7
* [AR-2021](https://armbian.atlassian.net/browse/AR-2021) Add Home assistant extensions
* [AR-2032](https://armbian.atlassian.net/browse/AR-2032) LVM support, CRYPTROOT and current implementation.
* [AR-2035](https://armbian.atlassian.net/browse/AR-2035) Cloud-Init Supprot and Armbian First
* [AR-2050](https://armbian.atlassian.net/browse/AR-2050) Add support for Radxa Rock S 0

### Solved Bugs

* [AR-1704](https://armbian.atlassian.net/browse/AR-1704) Bookworm Gnome lacks wallpaper withing lightdm
* [AR-1735](https://armbian.atlassian.net/browse/AR-1735) Command docker-shell seems to be broken
* [AR-1813](https://armbian.atlassian.net/browse/AR-1813) Orangepi One \+ fails to bring up NIC
* [AR-1861](https://armbian.atlassian.net/browse/AR-1861) Hashing on wireless patches seems to not work
* [AR-1908](https://armbian.atlassian.net/browse/AR-1908) Khadas VIM3 problem with high res displays
* [AR-1915](https://armbian.atlassian.net/browse/AR-1915) Extlinux / Khadas Edge 2 install to eMMC fails
* [AR-1933](https://armbian.atlassian.net/browse/AR-1933) Fix GitHub labeling anomaly 
* [AR-1981](https://armbian.atlassian.net/browse/AR-1981) Edge Kernel \(6.6.x\) breaks WiFi and Bluetooth support for RockPI-S
* [AR-1987](https://armbian.atlassian.net/browse/AR-1987) Error when removing BSP package
* [AR-2003](https://armbian.atlassian.net/browse/AR-2003) None of the builds of Raspberry Pi 5 goes into desktop
* [AR-2007](https://armbian.atlassian.net/browse/AR-2007) Fix armbian.list.disabled exists
* [AR-2009](https://armbian.atlassian.net/browse/AR-2009) Extensions from USERPATCHES\_PATH are not supported
* [AR-2010](https://armbian.atlassian.net/browse/AR-2010) Remove broken symlink
* [AR-2020](https://armbian.atlassian.net/browse/AR-2020) RK35xx is seeking for rk35xx config
* [AR-2027](https://armbian.atlassian.net/browse/AR-2027) Compressed images failed to upload to GitHub releases
* [AR-2034](https://armbian.atlassian.net/browse/AR-2034) RockPI-S does WiFi broken on kernels >6.5
* [AR-2038](https://armbian.atlassian.net/browse/AR-2038) KHADAS\_OOWOW\_BOARD\_ID is not set, can't use image-output-oowow
* [AR-2051](https://armbian.atlassian.net/browse/AR-2051) All installed systemd units are forcefully enabled on first boot
* [AR-2052](https://armbian.atlassian.net/browse/AR-2052) Cinnamon desktop doesn't work on vim4
* [AR-2053](https://armbian.atlassian.net/browse/AR-2053) Desktop environment takes a long time to load on vim4
* [AR-2054](https://armbian.atlassian.net/browse/AR-2054) Image takes a lot of time to load on vim1s/vim4 bookworm image

## v23.11.3 (2023-12-20)

* [Bugfix: some desktop images on Raspberry Pi 5 didn't load desktop](https://github.com/armbian/build/commit/a82589e683471911cad04f4d4615bb6a3656eb85).

## v23.11.2 (2023-12-18)

* added standard support images for Raspberry Pi 5, Odroid N2/N2+, Odroid M1 due to the boards support status change
* recreated images for Raspberry Pi 4, Nanopi R4S, Orangepi Zero2 due to several bug fixes (check commit log / newsletter for details)

## v23.11.1 (2023-11-30)

### Closed projects

* [AR-1702](https://armbian.atlassian.net/browse/AR-1702) Switch default login manager
* [AR-1886](https://armbian.atlassian.net/browse/AR-1886) Enable artifacts creation at pull request
* [AR-1924](https://armbian.atlassian.net/browse/AR-1924) Add support for Hikey 960
* [AR-1928](https://armbian.atlassian.net/browse/AR-1928) K3: Update edge kernel to v6.5
* [AR-1929](https://armbian.atlassian.net/browse/AR-1929) New Armbian Wallpapers
* [AR-1930](https://armbian.atlassian.net/browse/AR-1930) Add orangepi3b build config
* [AR-1940](https://armbian.atlassian.net/browse/AR-1940) Add edge kernel support for NanoPi R6S/R6C
* [AR-1941](https://armbian.atlassian.net/browse/AR-1941) Rework ac200 patches and config for current and edge kernel.
* [AR-1943](https://armbian.atlassian.net/browse/AR-1943) Add initial support for TI SK-TDA4VM board
* [AR-1951](https://armbian.atlassian.net/browse/AR-1951) add new device xiaomi-elish
* [AR-1957](https://armbian.atlassian.net/browse/AR-1957) Improve labeling system - refactor labeling logic
* [AR-1958](https://armbian.atlassian.net/browse/AR-1958) rk3588: configure UEFI\_EDK2\_BOARD\_ID for all UEFI-supported boards
* [AR-1959](https://armbian.atlassian.net/browse/AR-1959) use GHPROXY\_ADDRESS to customize ghproxy url

### Closed Tasks

* [AR-1784](https://armbian.atlassian.net/browse/AR-1784) Remove FriendlyElec vendor "driver" patch in mainline
* [AR-1907](https://armbian.atlassian.net/browse/AR-1907) Add latest patch for eeprom support in JetHub D1\+
* [AR-1811](https://armbian.atlassian.net/browse/AR-1811) Drop host OS-es that can't compile Crust
* [AR-1882](https://armbian.atlassian.net/browse/AR-1882) Clean remaining legacy Rockchip kernels
* [AR-1897](https://armbian.atlassian.net/browse/AR-1897) KDE build seems to be missing features
* [AR-1913](https://armbian.atlassian.net/browse/AR-1913) Remove midstream kernel
* [AR-1919](https://armbian.atlassian.net/browse/AR-1919) Change support status to multiple selection
* [AR-1942](https://armbian.atlassian.net/browse/AR-1942) Add board config for Tanix TX6 tvbox
* [AR-1944](https://armbian.atlassian.net/browse/AR-1944) Add support for Inovato Quadra
* [AR-1945](https://armbian.atlassian.net/browse/AR-1945) hinlink-h28k \[new board\]: support new SoC Rockchip rk3528
* [AR-1946](https://armbian.atlassian.net/browse/AR-1946) rockchip64/edge 6.6.y: update overlay configfs patch from rpi
* [AR-1947](https://armbian.atlassian.net/browse/AR-1947) meson-s4t7: Add option to force 16x9 display resolution
* [AR-1948](https://armbian.atlassian.net/browse/AR-1948) meson-s4t7: add systemd service to enable fan in automatic mode
* [AR-1949](https://armbian.atlassian.net/browse/AR-1949) mekotronics-r58x-pro.wip: add new board Mekotronics R58X-Pro
* [AR-1950](https://armbian.atlassian.net/browse/AR-1950) mixtile-blade3: enable pci3x4 nvme boot \(requires u.2 -> m.2 adapter from blade3 case kit\)
* [AR-1952](https://armbian.atlassian.net/browse/AR-1952) Update Rock CM5 I/O board config \(#5866\)
* [AR-1953](https://armbian.atlassian.net/browse/AR-1953) Add settings & updater for KDE
* [AR-1954](https://armbian.atlassian.net/browse/AR-1954) add board ArmSoM-w3; with uboot-patch and updated blobs
* [AR-1956](https://armbian.atlassian.net/browse/AR-1956) Rockchip64: Clean up archive of all EOL kernels
* [AR-1960](https://armbian.atlassian.net/browse/AR-1960) VIM1S/VIM4: Add bluetooth support
* [AR-1969](https://armbian.atlassian.net/browse/AR-1969) BPI-CM4: Add support for the waveshare cm4-io-base-b
* [AR-1970](https://armbian.atlassian.net/browse/AR-1970) BPI-CM4: Enable usb support on waveshare baseboards via overlay
* [AR-1971](https://armbian.atlassian.net/browse/AR-1971) BPI-SM1: Removed UART\_B overlay.
* [AR-1972](https://armbian.atlassian.net/browse/AR-1972) BPI-SM1: Add UART\_A "pin-ctrl: cts rts"
* [AR-1973](https://armbian.atlassian.net/browse/AR-1973)  Aligning display manager with the desktops
* [AR-1974](https://armbian.atlassian.net/browse/AR-1974) Add Ubuntu Mantic build target
* [AR-1979](https://armbian.atlassian.net/browse/AR-1979) Update kernel configs for Waydroid and Redroid support
* [AR-1980](https://armbian.atlassian.net/browse/AR-1980) xiaomi-elish: bump to kernel 6.7-rc2
* [AR-1983](https://armbian.atlassian.net/browse/AR-1983) xiaomi-elish: add typec pd support

### Solved Bugs

* [AR-1641](https://armbian.atlassian.net/browse/AR-1641) simpledrm module prevents Mali G-31 hardware acceleration
* [AR-1832](https://armbian.atlassian.net/browse/AR-1832) x13s errors with bash: line 1: add-apt-repository: command not found
* [AR-1866](https://armbian.atlassian.net/browse/AR-1866) UWE5622 driver is broken on 6.5.y
* [AR-1876](https://armbian.atlassian.net/browse/AR-1876) Shallow clones CI is getting disabled due to inactivity
* [AR-1911](https://armbian.atlassian.net/browse/AR-1911) Raspberry Pi, upgrade fails
* [AR-1923](https://armbian.atlassian.net/browse/AR-1923) Rockchip kernels compilation breaking
* [AR-1932](https://armbian.atlassian.net/browse/AR-1932) Update firmware for Orangepi R1\+ LTS
* [AR-1936](https://armbian.atlassian.net/browse/AR-1936) Khadas Vim1s: Fix display output
* [AR-1938](https://armbian.atlassian.net/browse/AR-1938) xradio: fix compilation for 6.1\+ 
* [AR-1961](https://armbian.atlassian.net/browse/AR-1961) rangepi3lts: load wifi module via systemd service otherwise it crash
* [AR-1962](https://armbian.atlassian.net/browse/AR-1962) Restore LED triggers for each ATA port indicating disk activity in mvebu-edge
* [AR-1963](https://armbian.atlassian.net/browse/AR-1963) Fix broken HDMI output on rk3328
* [AR-1964](https://armbian.atlassian.net/browse/AR-1964) Orange Pi 3 LTS: Fix ethernet broken for some users on 6.x kernel
* [AR-1965](https://armbian.atlassian.net/browse/AR-1965) Fix LicheePi 4A audio problem
* [AR-1966](https://armbian.atlassian.net/browse/AR-1966) Khadas Vim1s: Fix monitor not detected after its turned off and on again
* [AR-1967](https://armbian.atlassian.net/browse/AR-1967) xiaomi-elish: update config for 6.6, and fix one bluetooth pairing issue
* [AR-1968](https://armbian.atlassian.net/browse/AR-1968) bootscript: meson-s4t7: fix booting on ubuntu
* [AR-1976](https://armbian.atlassian.net/browse/AR-1976) VIM1S: emmc 23.8.4 install fails to boot after running upgrade using beta repository
* [AR-1977](https://armbian.atlassian.net/browse/AR-1977) Default renderer for NetPlan is not set on Debian variants
* [AR-1982](https://armbian.atlassian.net/browse/AR-1982) rockpi-s still using ifconfig to set wlan MAC address

## v23.08.5 (2023-10-11)

* Recreated images for Khadas VIM4

### Solved Bugs

* [AR-1887](https://armbian.atlassian.net/browse/AR-1887) Add fan support (fan.service) for VIM4.
* [AR-1893](https://armbian.atlassian.net/browse/AR-1893) Fix wifi not working on VIM4N.

## v23.08.4 (2023-10-09)

* Recreated images for Khadas VIM1S, Khadas VIM4

### Solved Bugs

* [AR-1894](https://armbian.atlassian.net/browse/AR-1894) HDMI not working in Armbian Image on VIM1S and VIM4. Its fixed and works on most monitor now in Debian based images, Ubuntu images will also be fixed soon.
* [AR-1895](https://armbian.atlassian.net/browse/AR-1895) Fix HDMI monitor does not work after its turned off and on again on VIM1S

## v23.08.3 (2023-09-20)

* Recreated images for NanoPi Duo, Orange Pi Zero, Orange Pi Zero 2, Orange Pi 3 LTS

### Closed Tasks

* [AR-1506](https://armbian.atlassian.net/browse/AR-1506) Reworked AC200 support for Allwinner current and edge kernels

### Solved Bugs

* [AR-1280](https://armbian.atlassian.net/browse/AR-1280) Xradio xr819 wireless driver not available in Allwinner current and edge kernels
* [AR-1833](https://armbian.atlassian.net/browse/AR-1833) Slow network speed reported by iperf3 and nuttcp on Allwinner boards with Gigabit NIC
* [AR-1866](https://armbian.atlassian.net/browse/AR-1866) Unisoc UWE5622 wireless driver not available in Allwinner legacy, current and edge kernels

## v23.08.2 (2023-09-11)

* Recreated images for Orangepi 5 Plus, Bananapi M1

## v23.08.1 (2023-09-01)

### Closed projects

* [AR-1690](https://armbian.atlassian.net/browse/AR-1690) Add Crust to Allwinner boards to enable power management functions
* [AR-1700](https://armbian.atlassian.net/browse/AR-1700) Add support for most recent memory chips on BPi M5
* [AR-1723](https://armbian.atlassian.net/browse/AR-1723) Backport Bananapi CM4 to kernel 6.1 LTS
* [AR-1744](https://armbian.atlassian.net/browse/AR-1744) Provide official distro upgrades
* [AR-1838](https://armbian.atlassian.net/browse/AR-1838) Adding armbian-gaming as extension
* [AR-1841](https://armbian.atlassian.net/browse/AR-1841) Introduce grub-with-dtb extension
* [AR-1842](https://armbian.atlassian.net/browse/AR-1842) Add Lenovo X13S as WIP board
* [AR-1843](https://armbian.atlassian.net/browse/AR-1843) Khadas VIM3/VIM3L u-boot 23.07-rc4 \+ SPI-NOR/MTD booting support
* [AR-1850](https://armbian.atlassian.net/browse/AR-1850) Odroid M1 de-infest Petitboot & use Kwiboo's 2023.10-rc2\+gmac u-boot

### Closed Tasks

* [AR-1647](https://armbian.atlassian.net/browse/AR-1647) Enable missing modules in sunxi64
* [AR-1718](https://armbian.atlassian.net/browse/AR-1718) Optimise images download build lists
* [AR-1719](https://armbian.atlassian.net/browse/AR-1719) Add and test 4G PCI modem on Bananapi CM4
* [AR-1722](https://armbian.atlassian.net/browse/AR-1722) Adjust Bananapi WiKi Pages
* [AR-1725](https://armbian.atlassian.net/browse/AR-1725) Update CM4 download pages
* [AR-1726](https://armbian.atlassian.net/browse/AR-1726) Add CM4 to auto-testing facility
* [AR-1728](https://armbian.atlassian.net/browse/AR-1728) Check if appropriate build targets has been generating
* [AR-1730](https://armbian.atlassian.net/browse/AR-1730) Make a hires photo of CM4 with modules placed on
* [AR-1780](https://armbian.atlassian.net/browse/AR-1780) Adjust u-boot patches to apply correctly
* [AR-1803](https://armbian.atlassian.net/browse/AR-1803) Enable wireless driver for MT7921U on all kernels
* [AR-1806](https://armbian.atlassian.net/browse/AR-1806) Generate all images that are declared in targets.yaml for single device
* [AR-1807](https://armbian.atlassian.net/browse/AR-1807) Test data visualisation JSON / PHP / HTML
* [AR-1824](https://armbian.atlassian.net/browse/AR-1824) Move Debian riscv64 from ports as its not 1st class citizen
* [AR-1826](https://armbian.atlassian.net/browse/AR-1826) Timezone select is too closed on status of the countries
* [AR-1834](https://armbian.atlassian.net/browse/AR-1834) Add gnome-calculator back to the default package base
* [AR-1836](https://armbian.atlassian.net/browse/AR-1836) Add SPI boot support for Rock5A
* [AR-1837](https://armbian.atlassian.net/browse/AR-1837) Add Orange Pi Plus
* [AR-1839](https://armbian.atlassian.net/browse/AR-1839) Introduce PASTE\_URL to make easy to change paste service used
* [AR-1840](https://armbian.atlassian.net/browse/AR-1840) Add pwm-fan support to Nanopi R4S
* [AR-1844](https://armbian.atlassian.net/browse/AR-1844) NanoPi Duo2: enable powerbutton and ethernet
* [AR-1845](https://armbian.atlassian.net/browse/AR-1845) Add bluetooth-hciattach extension to Orange Pi 5
* [AR-1846](https://armbian.atlassian.net/browse/AR-1846) Add Collabora rockchip-rk3588 mainline based branch
* [AR-1847](https://armbian.atlassian.net/browse/AR-1847) Add Radxa CM5 with I/O board
* [AR-1848](https://armbian.atlassian.net/browse/AR-1848) Fix thermal monitoring in 6.1 kernel
* [AR-1849](https://armbian.atlassian.net/browse/AR-1849) NanoPC-T6 Collabora: add PCIe 3
* [AR-1851](https://armbian.atlassian.net/browse/AR-1851) Add Debian Trixie host and target support

### Solved Bugs

* [AR-1539](https://armbian.atlassian.net/browse/AR-1539) XFCE image Rpi is missing from web download
* [AR-1570](https://armbian.atlassian.net/browse/AR-1570) Incomplete information in /etc/armbian-\(image\)-release
* [AR-1684](https://armbian.atlassian.net/browse/AR-1684) Synaptic search is super slow
* [AR-1707](https://armbian.atlassian.net/browse/AR-1707) Nightly images are not build with beta repository
* [AR-1724](https://armbian.atlassian.net/browse/AR-1724) CM4: Onboard WiFi and Bluetooth does not work
* [AR-1729](https://armbian.atlassian.net/browse/AR-1729) Userpatches support for series.conf seems broken
* [AR-1764](https://armbian.atlassian.net/browse/AR-1764) Some Allwinner 32bit boards hangs at boot
* [AR-1765](https://armbian.atlassian.net/browse/AR-1765) Recreate images that are missing in 23.05 release
* [AR-1771](https://armbian.atlassian.net/browse/AR-1771) Rockpi4c\+ link on download page broken
* [AR-1772](https://armbian.atlassian.net/browse/AR-1772) RockPI-S serial console drops keystrokes
* [AR-1787](https://armbian.atlassian.net/browse/AR-1787) Installing Khadas Vim3 image directly to eMMC fails
* [AR-1798](https://armbian.atlassian.net/browse/AR-1798) Orangepi 3 / LTS and Nanopi Black 5 does not boot
* [AR-1802](https://armbian.atlassian.net/browse/AR-1802) Possible bug in image assembly process
* [AR-1814](https://armbian.atlassian.net/browse/AR-1814) Installing M2PRO to eMMC fails to boot from eMMC
* [AR-1817](https://armbian.atlassian.net/browse/AR-1817) Enable wireless driver for MT7915E on all kernels
* [AR-1835](https://armbian.atlassian.net/browse/AR-1835) mkfs.vfat command is missing in minimal images

## v23.05.24 (2023-08-02)

* Recreated images for: Banana M2S, Odroid C2, Khadas VIM3

## v23.05.2 (2023-06-06)

* [AR-1765](https://armbian.atlassian.net/browse/AR-1765) Recreate images that are broken/missing in 23.05 release

## v23.05.1 (2023-05-31)

## Closed projects

* [AR-1516](https://armbian.atlassian.net/browse/AR-1516) Clean base desktops
* [AR-1536](https://armbian.atlassian.net/browse/AR-1536) Cleanup CLI packages list
* [AR-1543](https://armbian.atlassian.net/browse/AR-1543) Update RK35xx legacy kernel to 5.10
* [AR-1546](https://armbian.atlassian.net/browse/AR-1546) Merge all RK3588 under one kernel
* [AR-1549](https://armbian.atlassian.net/browse/AR-1549) Unify architecture definitions
* [AR-1557](https://armbian.atlassian.net/browse/AR-1557) Cleaning and adjusting CLI packages base
* [AR-1567](https://armbian.atlassian.net/browse/AR-1567) Generating JSON matrix
* [AR-1625](https://armbian.atlassian.net/browse/AR-1625) Extending JSON generation to support build matrix\(es\)
* [AR-1639](https://armbian.atlassian.net/browse/AR-1639) Enable armbian-config ORAS cache
* [AR-1693](https://armbian.atlassian.net/browse/AR-1693) Test as many images for upcoming 23.05 release as possible
* [AR-1700](https://armbian.atlassian.net/browse/AR-1700) Add support for most recent memory chips on BPi M5
* [AR-1748](https://armbian.atlassian.net/browse/AR-1748) Generate a sticky topic with instructions how to upgrade to Bookworm

## Closed Task

* [AR-241](https://armbian.atlassian.net/browse/AR-241) Remove NAND hacks from packaging 
* [AR-345](https://armbian.atlassian.net/browse/AR-345) Label trigger/workflow issue to jira
* [AR-773](https://armbian.atlassian.net/browse/AR-773) Add support and bug report URL to /etc/os-release
* [AR-1512](https://armbian.atlassian.net/browse/AR-1512) Switch Docker pull to armbian/cache repository
* [AR-1526](https://armbian.atlassian.net/browse/AR-1526) UWE5622 driver consolidation for rockchip64
* [AR-1542](https://armbian.atlassian.net/browse/AR-1542) Add architecture property for distributions
* [AR-1573](https://armbian.atlassian.net/browse/AR-1573) Move UEFI kernels to 6.2, move current to legacy
* [AR-1574](https://armbian.atlassian.net/browse/AR-1574) Move Rpi kernels to 6.2, move current to legacy
* [AR-1575](https://armbian.atlassian.net/browse/AR-1575) Move Odroid M1 to 6.2.y
* [AR-1577](https://armbian.atlassian.net/browse/AR-1577) Move mvebu edge kernels to 6.2, current to 6.1, current to legacy
* [AR-1590](https://armbian.atlassian.net/browse/AR-1590) Add another package to minimal images
* [AR-1591](https://armbian.atlassian.net/browse/AR-1591) Armbian buster xfce image build fails at installing package numix-icon-theme-circle
* [AR-1593](https://armbian.atlassian.net/browse/AR-1593) Add & adjust \(c\) in files
* [AR-1598](https://armbian.atlassian.net/browse/AR-1598) Minimal builds are missing apt-utils package
* [AR-1601](https://armbian.atlassian.net/browse/AR-1601) Add sudo, wget and htop to minimal packages
* [AR-1602](https://armbian.atlassian.net/browse/AR-1602) add \`fonts-noto-color-emoji\` for terminal Emoji support
* [AR-1620](https://armbian.atlassian.net/browse/AR-1620) Effectively remove Ubuntu PRO ads
* [AR-1627](https://armbian.atlassian.net/browse/AR-1627) Automatically clean docker images
* [AR-1642](https://armbian.atlassian.net/browse/AR-1642) Could not create a username containing a number 
* [AR-1645](https://armbian.atlassian.net/browse/AR-1645) Installer should handle input in the same way everywhere
* [AR-1651](https://armbian.atlassian.net/browse/AR-1651) Change Debian Bookworm into supported target
* [AR-1655](https://armbian.atlassian.net/browse/AR-1655) Enable CONFIG\_EXFAT\_FS on remaining kernels
* [AR-1656](https://armbian.atlassian.net/browse/AR-1656) Execute build train if kernel config changes
* [AR-1660](https://armbian.atlassian.net/browse/AR-1660) Enable OrangePi Zero \(LTS\) TV output
* [AR-1663](https://armbian.atlassian.net/browse/AR-1663) Add NanoPi R6S / R6C
* [AR-1664](https://armbian.atlassian.net/browse/AR-1664) Rebuild board selection for generating official images
* [AR-1669](https://armbian.atlassian.net/browse/AR-1669) Optimise PNG images we are using
* [AR-1674](https://armbian.atlassian.net/browse/AR-1674) Bump rockchip 32 bit edge to kernel 6.3
* [AR-1679](https://armbian.atlassian.net/browse/AR-1679) Drop kernel-jetson-nano-legacy
* [AR-1680](https://armbian.atlassian.net/browse/AR-1680) Drop kernel-rockchip-legacy
* [AR-1681](https://armbian.atlassian.net/browse/AR-1681) Drop kernel-rk3399-legacy
* [AR-1682](https://armbian.atlassian.net/browse/AR-1682) Drop kernel-rockchip64-legacy
* [AR-1683](https://armbian.atlassian.net/browse/AR-1683) Enable H616 CPU freq scaling
* [AR-1695](https://armbian.atlassian.net/browse/AR-1695) Bump rockchip64 current to 6.1.y
* [AR-1697](https://armbian.atlassian.net/browse/AR-1697) Add support for FriendlyElec NanoPi R4SE
* [AR-1698](https://armbian.atlassian.net/browse/AR-1698) Add NILFS2 fs support
* [AR-1699](https://armbian.atlassian.net/browse/AR-1699) Improve SD card compatibility on Radxa E25
* [AR-1706](https://armbian.atlassian.net/browse/AR-1706) Disable SKEL update mechanism from postinst
* [AR-1708](https://armbian.atlassian.net/browse/AR-1708) Improve i3-wm support
* [AR-1713](https://armbian.atlassian.net/browse/AR-1713) Introduce armbian-base-files artefact
* [AR-1717](https://armbian.atlassian.net/browse/AR-1717) Disable debug for postinst
* [AR-1747](https://armbian.atlassian.net/browse/AR-1747) Orangepi-r1plus-lts Network Interface logical names have changed and broken networking
* [AR-1760](https://armbian.atlassian.net/browse/AR-1760) Move Khadas Edge 2 to supported build targets
* [AR-1586](https://armbian.atlassian.net/browse/AR-1586) Consolidate RTL8723CS driver for all families

## Solved Bug

* [AR-1443](https://armbian.atlassian.net/browse/AR-1443) NanoPi R4S patch overwriting mainline base DTS, needs refactored
* [AR-1474](https://armbian.atlassian.net/browse/AR-1474) Emoji not shown 
* [AR-1523](https://armbian.atlassian.net/browse/AR-1523) UEFI install seems to be broken to some degree
* [AR-1528](https://armbian.atlassian.net/browse/AR-1528) Nanopi Neo stuck in boot loop
* [AR-1537](https://armbian.atlassian.net/browse/AR-1537) Missing man-db in images
* [AR-1541](https://armbian.atlassian.net/browse/AR-1541) UEFI swap problem and missing UUID for EFI partition
* [AR-1545](https://armbian.atlassian.net/browse/AR-1545) Update jethub prepackages python modules to install via apt
* [AR-1547](https://armbian.atlassian.net/browse/AR-1547) Jetson Nano legacy fails do build kernel
* [AR-1548](https://armbian.atlassian.net/browse/AR-1548) Odroid XU4 kernel compilation is failing current / edge
* [AR-1556](https://armbian.atlassian.net/browse/AR-1556) "No space left on device" while rsync root files to image
* [AR-1569](https://armbian.atlassian.net/browse/AR-1569) APT cache needs to be cleaned before closing image
* [AR-1578](https://armbian.atlassian.net/browse/AR-1578) Missing blobs for Riscv
* [AR-1588](https://armbian.atlassian.net/browse/AR-1588) Linter checking for bash shebang is incorrect
* [AR-1589](https://armbian.atlassian.net/browse/AR-1589) Kernel analysis is checking too many files
* [AR-1603](https://armbian.atlassian.net/browse/AR-1603) Broken wireless driver  8821cu-20210118 
* [AR-1611](https://armbian.atlassian.net/browse/AR-1611) Armbian install broken when installing to USB
* [AR-1615](https://armbian.atlassian.net/browse/AR-1615) Bad links Orangepizero2
* [AR-1621](https://armbian.atlassian.net/browse/AR-1621) Raspberry Pi does not build
* [AR-1623](https://armbian.atlassian.net/browse/AR-1623) Armbian install fails to start on minimal images
* [AR-1628](https://armbian.atlassian.net/browse/AR-1628) Orange Pi Zero 2 doesn't work
* [AR-1644](https://armbian.atlassian.net/browse/AR-1644) armbian-audio-config fails in minimal images; alsa-utils missing
* [AR-1648](https://armbian.atlassian.net/browse/AR-1648) Debian SID also split non-free firmware packages
* [AR-1650](https://armbian.atlassian.net/browse/AR-1650) Remote Desktop doesn't work on desktop images
* [AR-1653](https://armbian.atlassian.net/browse/AR-1653) Both Firefox and Chromium are not installing from our repo
* [AR-1658](https://armbian.atlassian.net/browse/AR-1658) Wrong artefacts creation
* [AR-1666](https://armbian.atlassian.net/browse/AR-1666) File with unexpected execution rights
* [AR-1667](https://armbian.atlassian.net/browse/AR-1667) RockPI-S audio support is gone
* [AR-1671](https://armbian.atlassian.net/browse/AR-1671) Packages are being downgraded to their repo versions
* [AR-1673](https://armbian.atlassian.net/browse/AR-1673) uboot v2018.05-sun50iw9 compile error
* [AR-1675](https://armbian.atlassian.net/browse/AR-1675) Nezha has wrong manufactur attached
* [AR-1676](https://armbian.atlassian.net/browse/AR-1676) Can't build linux-u-boot-radxa-e25-legacy and edge
* [AR-1677](https://armbian.atlassian.net/browse/AR-1677) Fix building rk322x with vendor 4.4 kernel
* [AR-1678](https://armbian.atlassian.net/browse/AR-1678) Can't build Macchiatobin-doubleshot
* [AR-1685](https://armbian.atlassian.net/browse/AR-1685) Rock 3A is missing current kernel def
* [AR-1692](https://armbian.atlassian.net/browse/AR-1692) Raspberry Pi does not boot
* [AR-1705](https://armbian.atlassian.net/browse/AR-1705) Jethome repository missing Lunar and Bookworm index
* [AR-1714](https://armbian.atlassian.net/browse/AR-1714) Our packages md hash files contains temporally path
* [AR-1715](https://armbian.atlassian.net/browse/AR-1715) Permission problem when building with GHA
* [AR-1733](https://armbian.atlassian.net/browse/AR-1733) Base files does not work for riscv64 due to anomaly
* [AR-1750](https://armbian.atlassian.net/browse/AR-1750) Missing information in BSP about repository and build FW commit
* [AR-1751](https://armbian.atlassian.net/browse/AR-1751) Ubuntu Advantage is not completely removed


## v23.02.1 (2023-02-25)

## Closed projects

* [AR-1281](https://armbian.atlassian.net/browse/AR-1281) Armbian community automated build
* [AR-1360](https://armbian.atlassian.net/browse/AR-1360) Bump Rockchip64 u-boot to 2022.07
* [AR-1408](https://armbian.atlassian.net/browse/AR-1408) Enable EDGE branch on RK3588
* [AR-1424](https://armbian.atlassian.net/browse/AR-1424) Refactor release index generation
* [AR-1432](https://armbian.atlassian.net/browse/AR-1432) Adjust 3rd party drivers for kernel 6.1
* [AR-1435](https://armbian.atlassian.net/browse/AR-1435) Generate CODEOWNER on GitHub
* [AR-1444](https://armbian.atlassian.net/browse/AR-1444) Move repo management from the build system
* [AR-1449](https://armbian.atlassian.net/browse/AR-1449) Adjust action scripts to adjusted logic
* [AR-1457](https://armbian.atlassian.net/browse/AR-1457) Create kernel config security analysis 
* [AR-1458](https://armbian.atlassian.net/browse/AR-1458) Enable AUFS on 6.1.y
* [AR-1460](https://armbian.atlassian.net/browse/AR-1460) Address corner case when looking for default route
* [AR-1461](https://armbian.atlassian.net/browse/AR-1461) Move hostapd from packages list
* [AR-1470](https://armbian.atlassian.net/browse/AR-1470) Improve new issue / request handling
* [AR-1484](https://armbian.atlassian.net/browse/AR-1484) Move meson64 CURRENT to 6.1.y
* [AR-1531](https://armbian.atlassian.net/browse/AR-1531) Add support for various HID game controllers and Waydroid
* [AR-1532](https://armbian.atlassian.net/browse/AR-1532) Split Bananapi M2PRO from M5

## Closed Task

* [AR-1313](https://armbian.atlassian.net/browse/AR-1313) Mvebu EDGE needs to be bumped to 6.1.y
* [AR-1507](https://armbian.atlassian.net/browse/AR-1507) Move UWE5622 from kernel patches to misc
* [AR-1379](https://armbian.atlassian.net/browse/AR-1379) Add support for minimal images build in CI
* [AR-1412](https://armbian.atlassian.net/browse/AR-1412) Move btrfs-progs to the minimal images
* [AR-1413](https://armbian.atlassian.net/browse/AR-1413) Port meson sm1 emmc related patches from edge to current
* [AR-1414](https://armbian.atlassian.net/browse/AR-1414) Move Bananapi M5 to the previous u-boot version
* [AR-1417](https://armbian.atlassian.net/browse/AR-1417) Add gnome-disk-utility to the desktops
* [AR-1418](https://armbian.atlassian.net/browse/AR-1418) Replace nand-sata-install with symlink to armbian-install
* [AR-1419](https://armbian.atlassian.net/browse/AR-1419) Limit automated swap creation to 16Gb
* [AR-1421](https://armbian.atlassian.net/browse/AR-1421) Add  nfs-common package too all except minimal
* [AR-1429](https://armbian.atlassian.net/browse/AR-1429) Switch to better 882xbu wireless driver
* [AR-1431](https://armbian.atlassian.net/browse/AR-1431) Improve audio config script
* [AR-1433](https://armbian.atlassian.net/browse/AR-1433) Change error reporting when linting scripts
* [AR-1434](https://armbian.atlassian.net/browse/AR-1434) Bump EDGE kernels to 6.1.y
* [AR-1448](https://armbian.atlassian.net/browse/AR-1448) Update u-boot patches for JetHub D1/D1\+
* [AR-1495](https://armbian.atlassian.net/browse/AR-1495) Change old not supported releases to EOS
* [AR-1509](https://armbian.atlassian.net/browse/AR-1509) Orange Pi R1 Plus LTS add 2 device tree overlays for rk3328 uart1 and i2C0. Network and LED's enhancements.
* [AR-1521](https://armbian.atlassian.net/browse/AR-1521) Add next Debian Bookworm
* [AR-1533](https://armbian.atlassian.net/browse/AR-1533) Disable event debugging
* [AR-1534](https://armbian.atlassian.net/browse/AR-1534) Add wpasupplicant to bookworm

## Solved Bugs

* [AR-1367](https://armbian.atlassian.net/browse/AR-1367) PCIe is stuck at Gen1 speed even tho overlay pcie-gen2 is specificed
* [AR-1416](https://armbian.atlassian.net/browse/AR-1416) Missing font in Bullseye desktop cause strange fonts in Terminator
* [AR-1437](https://armbian.atlassian.net/browse/AR-1437) Change to GitHub workflow badge routes
* [AR-1438](https://armbian.atlassian.net/browse/AR-1438) rockPi-S patchset overwriting mainline device tree
* [AR-1439](https://armbian.atlassian.net/browse/AR-1439) Rockchip64 NanoPi patches overwriting mainline DTS
* [AR-1450](https://armbian.atlassian.net/browse/AR-1450) MOTD shows error on some devices
* [AR-1463](https://armbian.atlassian.net/browse/AR-1463) Remove code was added to the sources, which creates a mess in rk3399-rock-pi-4.dts
* [AR-1467](https://armbian.atlassian.net/browse/AR-1467) Raspberry Pi 3 is unbootable, 4 boots
* [AR-1476](https://armbian.atlassian.net/browse/AR-1476) Missing firmware on Nanopi R2S
* [AR-1482](https://armbian.atlassian.net/browse/AR-1482) Do not generate swap larger the 16Gb
* [AR-1522](https://armbian.atlassian.net/browse/AR-1522) Fix SDIO port irq level bug found in 6.0\+ kernel
* [AR-1524](https://armbian.atlassian.net/browse/AR-1524) Cracklib check library must be present in all
* [AR-1527](https://armbian.atlassian.net/browse/AR-1527) Update patches for RTL8822CS

## v22.11.4 (2023-01-23)

* [Added image for Bananapi R2 PRO](https://www.armbian.com/bananapi-r2-pro/)
* kernel(s) update

## v22.11.3 (2022-12-31)

* [Added image for Orange Pi 5](https://www.armbian.com/orangepi-5/) (WIP)
* [Updated images for Bananapi M5/M2P](https://www.armbian.com/bananapi-m5/)
* [Updated images for Orangepi Zero 2](https://www.armbian.com/orange-pi-zero-2/)

## v22.11.2 (2022-12-09)

* Re-added image for Nanopi Duo
* Regenerated images Rock 5b (updated kernel)

## v22.11.1 (2022-12-03)

## Closed projects
* [AR-1278](https://armbian.atlassian.net/browse/AR-1278) Implement plymouth for kernel > 5.19.y
* [AR-1319](https://armbian.atlassian.net/browse/AR-1319) Upgrade Allwinner boot loader to 2022.08
* [AR-1335](https://armbian.atlassian.net/browse/AR-1335) Add gpiod library to armhf and arm64 server \+ desktop images
* [AR-1346](https://armbian.atlassian.net/browse/AR-1346) Grub optimisations
* [AR-1355](https://armbian.atlassian.net/browse/AR-1355) Add support for UEFI install to the nand-sata-install
* [AR-1362](https://armbian.atlassian.net/browse/AR-1362) Add Bananapi M5 to the build system
* [AR-1389](https://armbian.atlassian.net/browse/AR-1389) Refactor u-boot patches
* [AR-1390](https://armbian.atlassian.net/browse/AR-1390) Add Riscv64 support
* [AR-1399](https://armbian.atlassian.net/browse/AR-1399) Enable BASH linter at PR on changed files
* [AR-1402](https://armbian.atlassian.net/browse/AR-1402) Enable ES8316 audio properly on Radxa Rock Pi 4

## Closed Task
* [AR-668](https://armbian.atlassian.net/browse/AR-668) Using extlinux.conf instead of the legacy set of boot.scr \+ text files.
* [AR-949](https://armbian.atlassian.net/browse/AR-949) Initial board setup
* [AR-977](https://armbian.atlassian.net/browse/AR-977) Add package version number to the rootfs cache
* [AR-1034](https://armbian.atlassian.net/browse/AR-1034) Add missing Docker dependencies
* [AR-1112](https://armbian.atlassian.net/browse/AR-1112) Add ZFS repository
* [AR-1301](https://armbian.atlassian.net/browse/AR-1301) Add Rockpi 4C plus
* [AR-1312](https://armbian.atlassian.net/browse/AR-1312) Clean bootlogo patches
* [AR-1317](https://armbian.atlassian.net/browse/AR-1317) Remove nfs-kernel-server from default install
* [AR-1325](https://armbian.atlassian.net/browse/AR-1325) Deploy Chromium repo and keys to CLI images too
* [AR-1326](https://armbian.atlassian.net/browse/AR-1326) Add SKEL distribution to all existing users to the postinst script
* [AR-1336](https://armbian.atlassian.net/browse/AR-1336) Fix wallpaper not showing correct in virtual desktop
* [AR-1337](https://armbian.atlassian.net/browse/AR-1337) Re-enable Thunderbird email client for Debian Sid
* [AR-1338](https://armbian.atlassian.net/browse/AR-1338) Add Codium to Debian builds
* [AR-1342](https://armbian.atlassian.net/browse/AR-1342) Switch Codium with Code on x86
* [AR-1343](https://armbian.atlassian.net/browse/AR-1343) Update UEFI configs with latest Ubuntu desktop 22.04
* [AR-1349](https://armbian.atlassian.net/browse/AR-1349) Add Intel sound firmware to the desktops
* [AR-1350](https://armbian.atlassian.net/browse/AR-1350) Deprecating Buster and Focal
* [AR-1351](https://armbian.atlassian.net/browse/AR-1351) Adjust desktop support status
* [AR-1352](https://armbian.atlassian.net/browse/AR-1352) Add initial configuration for Terminator
* [AR-1353](https://armbian.atlassian.net/browse/AR-1353) Define panel shortcuts for Gnome x64 per appgroup
* [AR-1373](https://armbian.atlassian.net/browse/AR-1373) Port legacy kernel Rockchip Hardware Random Number Generator forward into Edge
* [AR-1376](https://armbian.atlassian.net/browse/AR-1376) Replace Ubuntu PRO advertisement
* [AR-1377](https://armbian.atlassian.net/browse/AR-1377) Add plymouth package to base images except minimal
* [AR-1388](https://armbian.atlassian.net/browse/AR-1388) Change purge releases action
* [AR-1404](https://armbian.atlassian.net/browse/AR-1404) Updated box86 and box64

## Solved Bugs
* [AR-577](https://armbian.atlassian.net/browse/AR-577) Fix USB port on Rockpi S
* [AR-1060](https://armbian.atlassian.net/browse/AR-1060) Freshly build image doesn't have BRANCH info in /etc/armbian-release
* [AR-1186](https://armbian.atlassian.net/browse/AR-1186) Screen power savings does not work
* [AR-1265](https://armbian.atlassian.net/browse/AR-1265) Rock PI-S images will not boot from internal EMMC \(SDNAND\)
* [AR-1268](https://armbian.atlassian.net/browse/AR-1268) RockPI-S WiFi throughput only 300K bytes/second
* [AR-1269](https://armbian.atlassian.net/browse/AR-1269) RockPI WiFi assigned different MAC address on each boot
* [AR-1305](https://armbian.atlassian.net/browse/AR-1305) CI build wrong images in cron
* [AR-1309](https://armbian.atlassian.net/browse/AR-1309) Some images doesn't want to be built, some are corrupted
* [AR-1310](https://armbian.atlassian.net/browse/AR-1310) Update JetHub D1 \(j100\) u-boot patchset
* [AR-1318](https://armbian.atlassian.net/browse/AR-1318) Replace expired GPG key for Github CLI
* [AR-1330](https://armbian.atlassian.net/browse/AR-1330) CLI images can ran out of space
* [AR-1332](https://armbian.atlassian.net/browse/AR-1332) Missing dependency in Docker images
* [AR-1334](https://armbian.atlassian.net/browse/AR-1334) Nanopi Neo3 does not have DT file in  EDGE
* [AR-1340](https://armbian.atlassian.net/browse/AR-1340) Disable event debugging on UEFI builds
* [AR-1341](https://armbian.atlassian.net/browse/AR-1341) Missing wallpaper in XFCE login screen Armbian Sid
* [AR-1344](https://armbian.atlassian.net/browse/AR-1344) Wrong location of package uninstall
* [AR-1345](https://armbian.atlassian.net/browse/AR-1345) Thunderbird 32b is no more, refactoring - provide it only for 64b
* [AR-1348](https://armbian.atlassian.net/browse/AR-1348) Pine64H b and NPI R1 does not build u-boot
* [AR-1363](https://armbian.atlassian.net/browse/AR-1363) Kernel freezing in armbian-kernel might not work correctly
* [AR-1374](https://armbian.atlassian.net/browse/AR-1374) Hostapd needs to be workarounded
* [AR-1381](https://armbian.atlassian.net/browse/AR-1381) XU4: On a fresh install, after moving root to f2fs eMMC, it fails to boot
* [AR-1384](https://armbian.atlassian.net/browse/AR-1384) Fix RTL8822CS driver. Update build config
* [AR-1385](https://armbian.atlassian.net/browse/AR-1385) Ambian's password rules are annoying
* [AR-1391](https://armbian.atlassian.net/browse/AR-1391) MOTD is not displaying messages correctly
* [AR-1392](https://armbian.atlassian.net/browse/AR-1392) Error triggered when changing BSP package
* [AR-1393](https://armbian.atlassian.net/browse/AR-1393) Converting to u-boot fails on riscv
* [AR-1394](https://armbian.atlassian.net/browse/AR-1394) Update kernel meson mmc driver to set phase clock from dts
* [AR-1395](https://armbian.atlassian.net/browse/AR-1395) Don't add PPA's to the CLI images
* [AR-1398](https://armbian.atlassian.net/browse/AR-1398) nand-sata-install must fail with a proper error message if the chosen mkfs.xyz is not installed
* [AR-1400](https://armbian.atlassian.net/browse/AR-1400) Raspberry Pi is unbootable
* [AR-1403](https://armbian.atlassian.net/browse/AR-1403) Wrong post install handling on install
* [AR-1405](https://armbian.atlassian.net/browse/AR-1405) When using PPA sources we need to run install\_ppa\_prerequisites

## v22.08.8 (2022-10-29)

* added test images for Odroid M1
* update rockchip64 kernels
* Regenerated images for Rockpro64, Rock64, Nanopi M4, Nanopi M4V2, Bananapi, Bananapi PRO, Bananapi M2Plus


## v22.08.7 (2022-10-20)

* Regenerated images for Rockpi S, Bananapi M1, PRO, M2+, M5, M64, UEFI, RPi4, ClockworkPi, Nanopi Neo3, Pinebook PRO, Renegade, Tinkerboard, OrangePi Zero, OrangePi Zero 2, OrangePi Zero plus
* [AR-1269](https://armbian.atlassian.net/browse/AR-1269) RockPI WiFi assigned different MAC address on each boot
* [AR-1268](https://armbian.atlassian.net/browse/AR-1268) RockPI-S WiFi throughput only 300K bytes/second
* [AR-1265](https://armbian.atlassian.net/browse/AR-1265) Rock PI-S images will not boot from internal EMMC (SDNAND)

## v22.08.5 (2022-10-14)

* Regenerated images for arm64 and x86 UEFI with improved installer

## v22.08 (2022-08-30)

### Solved Bugs

* [AR-1304](https://armbian.atlassian.net/browse/AR-1304) Boot splash is broken due to changes in kernel source
* [AR-1299](https://armbian.atlassian.net/browse/AR-1299) Debian throws out locale garbage at 1st login
* [AR-1296](https://armbian.atlassian.net/browse/AR-1296) JetHub D1 u-boot 2022.07\+ bug
* [AR-1295](https://armbian.atlassian.net/browse/AR-1295) Switch KDE plasma to Wayland
* [AR-1294](https://armbian.atlassian.net/browse/AR-1294) Remove broken packages from Debian SID
* [AR-1291](https://armbian.atlassian.net/browse/AR-1291) Several wireless drivers break down starting with 5.19.2
* [AR-1287](https://armbian.atlassian.net/browse/AR-1287) Debian SID package deprecation
* [AR-1285](https://armbian.atlassian.net/browse/AR-1285) Primary interface problem
* [AR-1282](https://armbian.atlassian.net/browse/AR-1282) Upstream wireless driver is broken
* [AR-1270](https://armbian.atlassian.net/browse/AR-1270) RockPi cannot host a desktop because it outputs no video
* [AR-1266](https://armbian.atlassian.net/browse/AR-1266) Media EDGE and media CURRENT are not compiling
* [AR-1263](https://armbian.atlassian.net/browse/AR-1263) Fix armbian-led-state-save.sh wrong behavior on boards without gpio leds.
* [AR-1235](https://armbian.atlassian.net/browse/AR-1235) Fix NanoPi \(rk3399\) boards missing correct device tree files in rk3399-legacy
* [AR-1224](https://armbian.atlassian.net/browse/AR-1224) AUFS breaks on 5.15.y
* [AR-1206](https://armbian.atlassian.net/browse/AR-1206) Firefox from Mozilla team is n/a on Focal
* [AR-1203](https://armbian.atlassian.net/browse/AR-1203) Rock3a only has one recommended target
* [AR-1202](https://armbian.atlassian.net/browse/AR-1202) Tinkerboard has only one recommended image on the download page
* [AR-1092](https://armbian.atlassian.net/browse/AR-1092) Docker is not working on some 5.15.y. / 5.16.y
* [AR-1037](https://armbian.atlassian.net/browse/AR-1037) Missing some repository install options
* [AR-1025](https://armbian.atlassian.net/browse/AR-1025) Samba timeouts and throws out error
* [AR-982](https://armbian.atlassian.net/browse/AR-982) Broken / invisible fonts on KDE plasma
* [AR-932](https://armbian.atlassian.net/browse/AR-932) HDMI rules could make troubles on some boards

### Story

* [AR-1303](https://armbian.atlassian.net/browse/AR-1303) Merging download target
* [AR-1288](https://armbian.atlassian.net/browse/AR-1288) Move DUT ip addresses to the database
* [AR-1284](https://armbian.atlassian.net/browse/AR-1284) Improve GitHub UX
* [AR-1277](https://armbian.atlassian.net/browse/AR-1277) Refactor rootfs cache system
* [AR-1248](https://armbian.atlassian.net/browse/AR-1248) Add support for month offset when creating cache
* [AR-1239](https://armbian.atlassian.net/browse/AR-1239) Wrong board status report at first login
* [AR-1238](https://armbian.atlassian.net/browse/AR-1238) Github Actions fine tuning
* [AR-1236](https://armbian.atlassian.net/browse/AR-1236) Add images integrity checking script
* [AR-1230](https://armbian.atlassian.net/browse/AR-1230) Refactor rootfs cache system
* [AR-1229](https://armbian.atlassian.net/browse/AR-1229) Enable code security analysis
* [AR-1220](https://armbian.atlassian.net/browse/AR-1220) Create nightly images directly on Github
* [AR-1130](https://armbian.atlassian.net/browse/AR-1130) Improve Pull request review culture and participation
* [AR-1081](https://armbian.atlassian.net/browse/AR-1081) Setup own mirror for kernel.org git
* [AR-580](https://armbian.atlassian.net/browse/AR-580) Generate CONTRIBUTION.md at build script repository

### Closed Sub-task

* [AR-1231](https://armbian.atlassian.net/browse/AR-1231) update meson64 edge kernel to 5.19
* [AR-686](https://armbian.atlassian.net/browse/AR-686) Migrate beta.armiban.com to redirect

### Closed Task

* [AR-1300](https://armbian.atlassian.net/browse/AR-1300) Add patches to support PiKVM
* [AR-1292](https://armbian.atlassian.net/browse/AR-1292) Conduct forum upgrade to latest version
* [AR-1279](https://armbian.atlassian.net/browse/AR-1279) Upgrade Rockchip \(32 bit\) edge kernel to v5.19
* [AR-1272](https://armbian.atlassian.net/browse/AR-1272) Move CSC targets that doesn't build to EOS
* [AR-1251](https://armbian.atlassian.net/browse/AR-1251) When generating rootfs cache also store package versions
* [AR-1249](https://armbian.atlassian.net/browse/AR-1249) Enable Debian Sid Gnome, Budgie and Cinnamon to some powerful boards
* [AR-1237](https://armbian.atlassian.net/browse/AR-1237) Add a small tool to help with unifying kernel configs
* [AR-1232](https://armbian.atlassian.net/browse/AR-1232) JetHome: add JetHub D1p support
* [AR-1223](https://armbian.atlassian.net/browse/AR-1223) Desktops are missing calculator
* [AR-1211](https://armbian.atlassian.net/browse/AR-1211) add rock-3a emmc support
* [AR-1210](https://armbian.atlassian.net/browse/AR-1210) add spi boot support for rock-3a
* [AR-1182](https://armbian.atlassian.net/browse/AR-1182) Orange Pi 4 LTS support
* [AR-1132](https://armbian.atlassian.net/browse/AR-1132) Update meson64 edge&current kernels
* [AR-1127](https://armbian.atlassian.net/browse/AR-1127) Change build train runners to use our runners
* [AR-1073](https://armbian.atlassian.net/browse/AR-1073) Remove /lib/build-all.sh
* [AR-1042](https://armbian.atlassian.net/browse/AR-1042) Sum important information in CONTRIBUTION.md
* [AR-1028](https://armbian.atlassian.net/browse/AR-1028) Add support for rootfs / toolchain bind mount
* [AR-984](https://armbian.atlassian.net/browse/AR-984) Integrate Khadas boards related fixes
* [AR-668](https://armbian.atlassian.net/browse/AR-668) Using extlinux.conf instead of the legacy set of boot.scr \+ text files.

## v22.05.4 (2022-07-14)

* Added more desktop flavors for boards which are capable (Budgie, Gnome, KDE Plasma, Xfce and Cinnamon)

## v22.05.3 (2022-06-23)

* All board images have been rebuilt due to corruption found in certain images
* Fixed Orange Pi 3 LTS bluetooth support
* [AR-1182](https://armbian.atlassian.net/browse/AR-1182) - Added board images for Orange Pi 4 LTS
* [AR-1228](https://armbian.atlassian.net/browse/AR-1228) - Upgraded bootloader to 22.04 for Rockchip family boards

## v22.05 (2022-05-28)

### Solved Bugs

* [AR-1204](https://armbian.atlassian.net/browse/AR-1204) - Orangepi R1plus-lts - USB3 Ethernet not working
* [AR-1202](https://armbian.atlassian.net/browse/AR-1202) - Tinkerboard has only one recommended image on the download page
* [AR-1199](https://armbian.atlassian.net/browse/AR-1199) - Orangepizero2 legacy images doesn't boot
* [AR-1197](https://armbian.atlassian.net/browse/AR-1197) - Support status shows unsupported even distro variant is supported \(random Focal image\)
* [AR-1196](https://armbian.atlassian.net/browse/AR-1196) - Mainline Kernel patch breaks spidev in 5.15\+
* [AR-1195](https://armbian.atlassian.net/browse/AR-1195) - Odroid N2 legacy kernel image does not build on Jammy
* [AR-1194](https://armbian.atlassian.net/browse/AR-1194) - Legacy kernels doesn't want to be added to repository
* [AR-1193](https://armbian.atlassian.net/browse/AR-1193) - Images without device tree blobs fails to build via CI
* [AR-1192](https://armbian.atlassian.net/browse/AR-1192) - Allwinner H5 boards fails on ATF compilation
* [AR-1190](https://armbian.atlassian.net/browse/AR-1190) - Docker image creation fails on Jammy host
* [AR-1189](https://armbian.atlassian.net/browse/AR-1189) - U-boot xt-q8l-v10 legacy fails to build at CI
* [AR-1185](https://armbian.atlassian.net/browse/AR-1185) - Remmina is missing RDP and VNC options
* [AR-1178](https://armbian.atlassian.net/browse/AR-1178) - Docker images creation is broken
* [AR-1173](https://armbian.atlassian.net/browse/AR-1173) - Github action for generating desktops does not start
* [AR-1172](https://armbian.atlassian.net/browse/AR-1172) - Load induced RX bug in the r8152 driver on 5.15 and 5.17
* [AR-1171](https://armbian.atlassian.net/browse/AR-1171) - Budgie desktop fails to build on Jammy
* [AR-1170](https://armbian.atlassian.net/browse/AR-1170) - Switching to beta repository at images sometimes failed
* [AR-1169](https://armbian.atlassian.net/browse/AR-1169) - Chromium does not install on Jammy desktops
* [AR-1167](https://armbian.atlassian.net/browse/AR-1167) - Update config to support Linux 5.15.36
* [AR-1160](https://armbian.atlassian.net/browse/AR-1160) - When seeking changed kernels two are always marked as changed
* [AR-1151](https://armbian.atlassian.net/browse/AR-1151) - Kernel 5.10.y need patch adjustment for boot splash
* [AR-1149](https://armbian.atlassian.net/browse/AR-1149) - Current build failure due to packages
* [AR-1148](https://armbian.atlassian.net/browse/AR-1148) - radxa zero 512MB \(no eMMC\) does not load img from SD
* [AR-1141](https://armbian.atlassian.net/browse/AR-1141) - Ubuntu Budgie on Focal Jammy / Focal fails
* [AR-1135](https://armbian.atlassian.net/browse/AR-1135) - fix armbian ramlog instability
* [AR-1129](https://armbian.atlassian.net/browse/AR-1129) - Gnome desktop on Jammy fails to start
* [AR-1115](https://armbian.atlassian.net/browse/AR-1115) - Package discrepancy in Jammy
* [AR-1102](https://armbian.atlassian.net/browse/AR-1102) - Missing wallpapers in desktop packages
* [AR-1097](https://armbian.atlassian.net/browse/AR-1097) - net: stmmac: dwmac-meson8b: interface sometimes does not come up at boot.
* [AR-1091](https://armbian.atlassian.net/browse/AR-1091) - Wireless driver for 8822bs is not compatible with 5.15.y and up
* [AR-1061](https://armbian.atlassian.net/browse/AR-1061) - udev HDMI rules are causing flickering
* [AR-1033](https://armbian.atlassian.net/browse/AR-1033) - U-boot packages doesn't want to be assembled with Docker
* [AR-1015](https://armbian.atlassian.net/browse/AR-1015) - Toolchain download only from a single source
* [AR-712](https://armbian.atlassian.net/browse/AR-712) - Broken framebuffer on A20
* [AR-583](https://armbian.atlassian.net/browse/AR-583) - RK3328 DMC driver needs small \(hopefully\) update for kernel 5.10
* [AR-191](https://armbian.atlassian.net/browse/AR-191) - SATA doesn't show up on Banana

### Story

* [AR-988](https://armbian.atlassian.net/browse/AR-988) - Add support for running x86\_64 applications
* [AR-775](https://armbian.atlassian.net/browse/AR-775) - Bring Marvell A3700-utils-marvell and mv-ddr-marvell.git to follow master
* [AR-273](https://armbian.atlassian.net/browse/AR-273) - Improve CI autotests facility

### Closed tasks

* [AR-1180](https://armbian.atlassian.net/browse/AR-1180) - Merge rk35xx-edge into rockchip64-edge
* [AR-1177](https://armbian.atlassian.net/browse/AR-1177) - Update only supported repositories
* [AR-1175](https://armbian.atlassian.net/browse/AR-1175) - Temperature monitoring for Jetson nano
* [AR-1166](https://armbian.atlassian.net/browse/AR-1166) - Add box86 package from 3rd party repository
* [AR-1165](https://armbian.atlassian.net/browse/AR-1165) - Update JetHub D1 u-boot patches
* [AR-1164](https://armbian.atlassian.net/browse/AR-1164) - Upgrade mvebu64 kernel to 5.17.y
* [AR-1159](https://armbian.atlassian.net/browse/AR-1159) - Upgrade UEFI EDGE kernels to 5.17.y
* [AR-1150](https://armbian.atlassian.net/browse/AR-1150) - Adjust hash calculating method
* [AR-1132](https://armbian.atlassian.net/browse/AR-1132) - Update meson64 edge&current kernels
* [AR-1128](https://armbian.atlassian.net/browse/AR-1128) - Add Nvidia driver to the x86 desktop images
* [AR-1126](https://armbian.atlassian.net/browse/AR-1126) - Enable desktop compilation at merge request
* [AR-1120](https://armbian.atlassian.net/browse/AR-1120) - Sync beta repository in the CI process
* [AR-1108](https://armbian.atlassian.net/browse/AR-1108) - Missing images in download section for following boards
* [AR-1076](https://armbian.atlassian.net/browse/AR-1076) - Add support for Orangepi 3 LTS
* [AR-1057](https://armbian.atlassian.net/browse/AR-1057) - Advertise recommended targets at download pages
* [AR-1008](https://armbian.atlassian.net/browse/AR-1008) - Update vars in amlogic u-boot script to match names of default u-boot vars
* [AR-959](https://armbian.atlassian.net/browse/AR-959) - Unifying TAGS as much as possible - as universal as possible
* [AR-628](https://armbian.atlassian.net/browse/AR-628) - Bump Meson64 u-boot
* [AR-296](https://armbian.atlassian.net/browse/AR-296) - Remove compressed indexes for apt?

## v22.02 (2022-02-28)

### Solved Bugs

* [AR-1101](https://armbian.atlassian.net/browse/AR-1101) - DRM patch is failing on Rockchip
* [AR-1079](https://armbian.atlassian.net/browse/AR-1079) - Ubuntu archive redirector is not providing best service
* [AR-1077](https://armbian.atlassian.net/browse/AR-1077) - Fix RPi4 userland audio
* [AR-1069](https://armbian.atlassian.net/browse/AR-1069) - First login doesn't pick up correct shell
* [AR-1065](https://armbian.atlassian.net/browse/AR-1065) - Twitter forum registration is not working
* [AR-1063](https://armbian.atlassian.net/browse/AR-1063) - X86 desktop images are not enabled in CI
* [AR-1062](https://armbian.atlassian.net/browse/AR-1062) - When selecting repository install u-boot might not be flashed
* [AR-1055](https://armbian.atlassian.net/browse/AR-1055) - Aptly repository seems to be out of business
* [AR-1048](https://armbian.atlassian.net/browse/AR-1048) - Rpi kernel image is not updated on upgrade
* [AR-1043](https://armbian.atlassian.net/browse/AR-1043) - linux-firmware repository change branch from "master"  to "main"
* [AR-973](https://armbian.atlassian.net/browse/AR-973) - boot building is failing after update to 2021.10
* [AR-871](https://armbian.atlassian.net/browse/AR-871) - Debian SID broken wallpaper

### Story

* [AR-1074](https://armbian.atlassian.net/browse/AR-1074) - Switch all CURRENT to 5.15.y and EDGE to 5.16.y
* [AR-1009](https://armbian.atlassian.net/browse/AR-1009) - Armbian Framework extensions and UEFI support

### Closed tasks

* [AR-1100](https://armbian.atlassian.net/browse/AR-1100) - Support for Orange Pi R1 Plus LTS
* [AR-1084](https://armbian.atlassian.net/browse/AR-1084) - 3D support on Debian desktop
* [AR-1078](https://armbian.atlassian.net/browse/AR-1078) - Add additional forum plugins and adjust settings
* [AR-1068](https://armbian.atlassian.net/browse/AR-1068) - Add gnome-system-monitor to Focal and Jammy
* [AR-1049](https://armbian.atlassian.net/browse/AR-1049) - Add ZFS that supports kernel 5.15.y
* [AR-1044](https://armbian.atlassian.net/browse/AR-1044) - Improve Raspberry Pi support
* [AR-1041](https://armbian.atlassian.net/browse/AR-1041) - JetHome: fix brcm \(AP6255\) firmware links
* [AR-1040](https://armbian.atlassian.net/browse/AR-1040) - Refactor armbian-bsp-cli package creation
* [AR-931](https://armbian.atlassian.net/browse/AR-931) - Using Docker image for building kernels
* [AR-893](https://armbian.atlassian.net/browse/AR-893) - Cleanup rockchip64 u-boot scenarios
* [AR-757](https://armbian.atlassian.net/browse/AR-757) - Adding Raspberry Pi
* [AR-586](https://armbian.atlassian.net/browse/AR-586) - Implement fan controller for Nanopi M4V2

## v21.08 (2021-08-31)

### Solved Bugs

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
* [AR-315](https://armbian.atlassian.net/browse/AR-315) - Add support for GPT table inside armbian-install

## v21.05.6 (2021-06-21)

Solved Bugs

Updated images for Orangepi Zero

* [AR-593](https://armbian.atlassian.net/browse/AR-593) - Rockpi S doesn't boot mainline kernel

## v21.05.3 (2021-05-24)

Solved Bugs

* [AR-780](https://armbian.atlassian.net/browse/AR-780) - Nanopi R4S USB broken
* [AR-816](https://armbian.atlassian.net/browse/AR-780) - ZRAM is missing in Jeston Nano legacy

## v21.05.2 (2021-05-24)

Solved Bugs

* [AR-748](https://armbian.atlassian.net/browse/AR-748) - Headers install broken
* [AR-740](https://armbian.atlassian.net/browse/AR-740) - Vnstat throws out garbage
* [AR-764](https://armbian.atlassian.net/browse/AR-764) - Fixing Htop security issue

Closed Tasks

ZFS updated to v2.0.4 (tested on 32bit Odroid HC1 and 64bit N2, Focal and Bionic userland)
Added Hirsute CLI images with EDGE Linux 5.12.y for most of the boards

## v21.05 (2021-05-09)

Solved Bugs

* [AR-730](https://armbian.atlassian.net/browse/AR-730) -          Duplicate packages error when updating repository

* [AR-729](https://armbian.atlassian.net/browse/AR-729) -          Fix Partition Alignment for resizes and armbian-install

* [AR-711](https://armbian.atlassian.net/browse/AR-711) -          Network troubles on Nanopi K2 / Odroids

* [AR-709](https://armbian.atlassian.net/browse/AR-709) -          Tinkerboard AP crash on client connect

* [AR-708](https://armbian.atlassian.net/browse/AR-708) -          Missing library for compiling u-boot

* [AR-707](https://armbian.atlassian.net/browse/AR-707) -          Wrong keyboard code detected

* [AR-705](https://armbian.atlassian.net/browse/AR-705) -          Compilation issues when building old u-boot

* [AR-698](https://armbian.atlassian.net/browse/AR-698) -          XU4 - current kernel oddness with docker

* [AR-697](https://armbian.atlassian.net/browse/AR-697) -          Fix Meson64 Default Governor

* [AR-688](https://armbian.atlassian.net/browse/AR-688) -          Firefly boot broken

* [AR-674](https://armbian.atlassian.net/browse/AR-674) -          Users can't change desktop wallpaper on Gnome

* [AR-666](https://armbian.atlassian.net/browse/AR-666) -          ZSH is disabled on upgrade

* [AR-662](https://armbian.atlassian.net/browse/AR-662) -          Distribution support status is not written to the /etc/armbian-release

* [AR-659](https://armbian.atlassian.net/browse/AR-659) -          Rootfs image runs out of inodes during build

* [AR-653](https://armbian.atlassian.net/browse/AR-653) -          builder issue with gnome

* [AR-647](https://armbian.atlassian.net/browse/AR-647) -          Wireless driver 8811CU is broken on 5.11.y

* [AR-646](https://armbian.atlassian.net/browse/AR-646) -          Bootsplash breaks compilation on 5.11.y

* [AR-644](https://armbian.atlassian.net/browse/AR-644) -          Wireless driver 8188 EU broken and disabled since 5.9.y

* [AR-636](https://armbian.atlassian.net/browse/AR-636) -          Odroid N2+ lost additional freq values

* [AR-585](https://armbian.atlassian.net/browse/AR-585) -          HDMI-CEC not working on rockchip64 Legacy

* [AR-88](https://armbian.atlassian.net/browse/AR-88) -          Banana Pi M3 does not boot

Finished projects

* [AR-694](https://armbian.atlassian.net/browse/AR-694) -          Create Jira-based checklist for Desktop Testing

* [AR-457](https://armbian.atlassian.net/browse/AR-457) -          Enable native arm/arm64 building

* [AR-454](https://armbian.atlassian.net/browse/AR-454) -          Additional Desktop Configurations for use with new framework

* [AR-444](https://armbian.atlassian.net/browse/AR-444) -          Improving download infrastructure Phase 2

* [AR-200](https://armbian.atlassian.net/browse/AR-200) -          Improving Desktop images

Closed Tasks

* [AR-714](https://armbian.atlassian.net/browse/AR-714) -          Adjusting support status

* [AR-710](https://armbian.atlassian.net/browse/AR-710) -          Create imx edge branch

* [AR-706](https://armbian.atlassian.net/browse/AR-706) -          Bump Allwinner u-boot to 2021.04

* [AR-704](https://armbian.atlassian.net/browse/AR-704) -          Distinguish between edge and normal image in motd

* [AR-696](https://armbian.atlassian.net/browse/AR-696) -          Improve Nvidia Jetson Nano support

* [AR-673](https://armbian.atlassian.net/browse/AR-673) -          Add few missing packages

* [AR-670](https://armbian.atlassian.net/browse/AR-670) -          Add additonal mirros for linux-firmware beside kernel source

* [AR-667](https://armbian.atlassian.net/browse/AR-667) -          Move Meson64 DEV to 5.10.y

* [AR-657](https://armbian.atlassian.net/browse/AR-657) -          Add instructions how to manual flash boot loader

* [AR-656](https://armbian.atlassian.net/browse/AR-656) -          Implement timeout on cache download

* [AR-654](https://armbian.atlassian.net/browse/AR-654) -          Fix stability issues of NanoPi M4V2 in current and dev

* [AR-651](https://armbian.atlassian.net/browse/AR-651) -          NanoPC-T4 legacy: enable USB-C DisplayPort & eDP outs

* [AR-648](https://armbian.atlassian.net/browse/AR-648) -          Resolve GPIO & PWM patches on mvebu

* [AR-645](https://armbian.atlassian.net/browse/AR-645) -          Detach rtl8812au from fixed commit ID if it builds from master

* [AR-643](https://armbian.atlassian.net/browse/AR-643) -          Bump DEV kernels to 5.11.y

* [AR-634](https://armbian.atlassian.net/browse/AR-634) -          Add Orangepi R1 Plus

* [AR-633](https://armbian.atlassian.net/browse/AR-633) -          Enable  hardware PRNG/TRNG/SHA on sun8i-ce platform

* [AR-613](https://armbian.atlassian.net/browse/AR-613) -          test/beta img auto builder

* [AR-612](https://armbian.atlassian.net/browse/AR-612) -          Update pine64 install instructions

* [AR-600](https://armbian.atlassian.net/browse/AR-600) -          RK3399's: Add multimedia and OC overlays

* [AR-599](https://armbian.atlassian.net/browse/AR-599) -          Enable HDMI-CEC and ISP1 camera support for rk3399 and rockchip64 legacy

* [AR-369](https://armbian.atlassian.net/browse/AR-369) -          Check kernel config changes

## v21.02.4 (2021-04-04)

 Added Nvidia Jetson Nano (community supported target)

Rebuild images for Odroid N2, H4, HC4

## v21.02.3 (2021-03-09)

 All kernels received upstream updates

 All images has been rebuilt

Fixed reboot troubles on meson64 family (Odroid N2, C2, H4, HC4)

ZSH upgrade fixed

Type-C DP support for the NanoPC T4

* [AR-654](https://armbian.atlassian.net/browse/AR-654) -         NanoPi M4V2 stability fix for current and dev

Allwinner a20 fail to init hdmi in many cases / fixed (all images need to be rebuilt)

* [AR-660](https://armbian.atlassian.net/browse/AR-660) -         Attempt to improve stability on Helios64

## v21.02.2 (2021-02-16)

 All kernels received upstream updates

* [AR-633](https://armbian.atlassian.net/browse/AR-633) -         Enable  hardware PRNG/TRNG/SHA on sun8i-ce platform

* [AR-636](https://armbian.atlassian.net/browse/AR-636) -         Odroid N2+ lost additional freq values

## v21.02.1 (2021-02-03)

Finished projects

* [AR-235](https://armbian.atlassian.net/browse/AR-235) -         Implement Device Tree Editor

* [AR-476](https://armbian.atlassian.net/browse/AR-476) -         Add sound to Odroid N2

* [AR-485](https://armbian.atlassian.net/browse/AR-485) -         Improve multicore compilation

* [AR-487](https://armbian.atlassian.net/browse/AR-487) -         Rework download pages

* [AR-508](https://armbian.atlassian.net/browse/AR-508) -         Add Odroid HC4

* [AR-546](https://armbian.atlassian.net/browse/AR-546) -         Added Pine64 Pinecube

* [AR-566](https://armbian.atlassian.net/browse/AR-566) -         Add Nanopi R4S

* [AR-568](https://armbian.atlassian.net/browse/AR-568) -         Add Orangepizero 2 WIP target

* [AR-571](https://armbian.atlassian.net/browse/AR-571) -         Move Meson64 DEV to 5.10.y

* [AR-589](https://armbian.atlassian.net/browse/AR-589) -         Add ZShell via armbian-zsh package

* [AR-590](https://armbian.atlassian.net/browse/AR-590) -         ZRAM Enhancements - decouple swap config from tmp

Solved bugs

* [AR-365](https://armbian.atlassian.net/browse/AR-365) -         4k not detected properly on Amlogic, Rockchip devices

* [AR-440](https://armbian.atlassian.net/browse/AR-440) -         Errors shown at 1st login under certain conditions

* [AR-512](https://armbian.atlassian.net/browse/AR-512) -         Fix Ethernet for Opi3 and other devices with phymode for kernel 5.10

* [AR-514](https://armbian.atlassian.net/browse/AR-514) -         Download and verify not fully reliable

* [AR-547](https://armbian.atlassian.net/browse/AR-547) -         First login: adding a non-existing keyboard variant

* [AR-548](https://armbian.atlassian.net/browse/AR-548) -         mvebu DFS seems to cause system hang under high I/O

* [AR-557](https://armbian.atlassian.net/browse/AR-557) -         GCC compatibility issues

* [AR-559](https://armbian.atlassian.net/browse/AR-559) -         First login script - not all locales have UTF8 encoding

* [AR-565](https://armbian.atlassian.net/browse/AR-565) -         SATA on HC4 is not recognized

* [AR-570](https://armbian.atlassian.net/browse/AR-570) -         Improper order in getty override.conf

* [AR-584](https://armbian.atlassian.net/browse/AR-584) -         Nanopi M4V2 hangs on bluetooth loading

* [AR-595](https://armbian.atlassian.net/browse/AR-595) -         Rockpi 4B 1GB not booting

* [AR-605](https://armbian.atlassian.net/browse/AR-605) -         Booting troubles on Odroid C4 / HC4

* [AR-606](https://armbian.atlassian.net/browse/AR-606) -         Force boot script update throws out some error

* [AR-608](https://armbian.atlassian.net/browse/AR-608) -         Broken building out-of-tree modules

* [AR-610](https://armbian.atlassian.net/browse/AR-610) -         Nanopi Neo2 black sometimes nic doesn&#39;t init

* [AR-615](https://armbian.atlassian.net/browse/AR-615) -         Helios64 unstable 2.5Gbps Interface on LK5.x

* [AR-616](https://armbian.atlassian.net/browse/AR-616) -         Ubuntu Bionic ZSH / BASH changing issue

* [AR-617](https://armbian.atlassian.net/browse/AR-617) -         Locales detection doesn&#39;t work properly in some cases

* [AR-627](https://armbian.atlassian.net/browse/AR-627) -         Ubuntu update is overwriting our welcome screen

* [AR-629](https://armbian.atlassian.net/browse/AR-629) -         Odroid HC4 SATA failure

* [AR-631](https://armbian.atlassian.net/browse/AR-631) -         Orangepi Zero2 broken network

* [AR-632](https://armbian.atlassian.net/browse/AR-632) -         Desktop fails to load at second run

Closed task

* [AR-163](https://armbian.atlassian.net/browse/AR-163) -         Systematically cleanup distribution defaults

* [AR-206](https://armbian.atlassian.net/browse/AR-206) -         Improve memory performance on Renegade (roc-rk3328-cc) in current

* [AR-399](https://armbian.atlassian.net/browse/AR-399) -         Improve Pinebook PRO support

* [AR-467](https://armbian.atlassian.net/browse/AR-467) -         Enable AUFS support back

* [AR-472](https://armbian.atlassian.net/browse/AR-472) -         Added support for Ubuntu 20.10 Groovy

* [AR-517](https://armbian.atlassian.net/browse/AR-517) -         Mark Bionic builds host as deprecated

* [AR-520](https://armbian.atlassian.net/browse/AR-520) -         Move Rock64 to CSC in build script

* [AR-525](https://armbian.atlassian.net/browse/AR-525) -         Bump Rockchip 32bit to 5.9.y

* [AR-526](https://armbian.atlassian.net/browse/AR-526) -         Move mvebu-dev kernel to 5.9+

* [AR-551](https://armbian.atlassian.net/browse/AR-551) -         Update fan configuration, enable network LED and enable UPS timer

* [AR-552](https://armbian.atlassian.net/browse/AR-552) -         Re-enable UHS SDR104 mode for Helios64 and roc-rk3399-pc

* [AR-553](https://armbian.atlassian.net/browse/AR-553) -         Update builder to retrieve web seeds from mirrors api

* [AR-554](https://armbian.atlassian.net/browse/AR-554) -         OdroidN2 Ethernet Failure Pt2

* [AR-556](https://armbian.atlassian.net/browse/AR-556) -         Adding vnstat and ZFS support to MOTD

* [AR-558](https://armbian.atlassian.net/browse/AR-558) -         Switch mvebu current to K5.9

* [AR-563](https://armbian.atlassian.net/browse/AR-563) -         Improve headers compilation

* [AR-576](https://armbian.atlassian.net/browse/AR-576) -         Enabled debug on RockpiS

* [AR-579](https://armbian.atlassian.net/browse/AR-579) -         Improve (oh-my)ZSH loading speed

* [AR-587](https://armbian.atlassian.net/browse/AR-587) -         Fix kernel switching for rk3399 family

* [AR-594](https://armbian.atlassian.net/browse/AR-594) -         Upgrade Meson64 u-boot to 2020.10

* [AR-598](https://armbian.atlassian.net/browse/AR-598) -         Switch rockchip64 u-boot to 2020.10

* [AR-601](https://armbian.atlassian.net/browse/AR-601) -         Move sunxi-current to 5.10.y

* [AR-603](https://armbian.atlassian.net/browse/AR-603) -         Enable SPI boot option for roc-rk3399-pc

* [AR-607](https://armbian.atlassian.net/browse/AR-607) -         Move Meson64 Current to 5.10.y

* [AR-609](https://armbian.atlassian.net/browse/AR-609) -         Move Mvebu Current to 5.10.y

* [AR-611](https://armbian.atlassian.net/browse/AR-611) -         Switch rockchip64-current to 5.10.y

* [AR-614](https://armbian.atlassian.net/browse/AR-614) -         Upgrade ZFS packages

* [AR-618](https://armbian.atlassian.net/browse/AR-618) -         Upgrade mvebu64 current to 5.10.y

* [AR-619](https://armbian.atlassian.net/browse/AR-619) -         Bump rockchip current to 5.10.y

* [AR-620](https://armbian.atlassian.net/browse/AR-620) -         Enable network link leds for NanoPi R4S by default

* [AR-622](https://armbian.atlassian.net/browse/AR-622) -         Enable DMC for Station-M1 in current and dev

* [AR-623](https://armbian.atlassian.net/browse/AR-623) -         Enable RTC (hym8563) for Station P1 in dev and current

* [AR-624](https://armbian.atlassian.net/browse/AR-624) -         Provide an option to skip autodetection at first login

* [AR-628](https://armbian.atlassian.net/browse/AR-628) -         Bump Meson64 u-boot to 2021.01

* [AR-630](https://armbian.atlassian.net/browse/AR-630) -         Bump Odroid XU4 DEV to 5.10.y

## v20.11.10 (2021-01-25)

All images rebuild due to torrent system corruption

## v20.11.9 (2021-01-23)

Broken Nanopi Neo buster image rebuild, adding Station M1 and P1 legacy images, Odroid XU4 update

## v20.11.8 (2021-01-17)

* [AR-614](https://armbian.atlassian.net/browse/AR-614) -         Upgrade ZFS on Focal and Buster (64bit only) to v2.0.1

## v20.11.7 (2021-01-06)

* [AR-605](https://armbian.atlassian.net/browse/AR-605) -         Booting troubles on Odroid C4 / HC4

all images were rebuilt - we had a few corrupted ones in previous build

## v20.11.6 (2021-01-03)

* [AR-601](https://armbian.atlassian.net/browse/AR-601) -         Move sunxi-current to 5.10.y

* [AR-235](https://armbian.atlassian.net/browse/AR-235) -         Implement Device Tree Editor in armbian-config

* [AR-589](https://armbian.atlassian.net/browse/AR-589) -         Add armbian-zsh package

* [AR-590](https://armbian.atlassian.net/browse/AR-590) -         ZRAM Enhancements - decouple swap config from tmp

* [AR-554](https://armbian.atlassian.net/browse/AR-554) -         Fix Odroid N2 Ethernet Failure

* [AR-556](https://armbian.atlassian.net/browse/AR-556) -         Adding vnstat and ZFS support to MOTD

* [AR-579](https://armbian.atlassian.net/browse/AR-579) -         Improve (oh-my)ZSH loading speed

* [AR-512](https://armbian.atlassian.net/browse/AR-512) -         Fix Ethernet for Opi3 and other devices with phymode for kernel 5.10

* [AR-547](https://armbian.atlassian.net/browse/AR-547) -         First login: adding a non-existing keyboard variant

* [AR-565](https://armbian.atlassian.net/browse/AR-565) -         Fix SATA on HC4 is not recognized

* [AR-595](https://armbian.atlassian.net/browse/AR-595) -         Fix Rockpi 4B 1GB not booting

## v20.11.5 (2020-12-31)

 [AR-566](https://armbian.atlassian.net/browse/AR-566) - Add Nanopi R4S preview images

## v20.11.4 (2020-12-15)

* [Re-adding accidentally removed network driver on Helios64](https://forum.armbian.com/topic/16476-eth1-25-vanished-upgrade-to-20113-5914-rockchip64/)
added OpenHab 3 to the armbian-config software installer

* [AR-587](https://armbian.atlassian.net/browse/AR-587) - Fix kernel switching for rk3399 family

## v20.11.3 (2020-12-12)

Bugfix release

* [AR-559](https://armbian.atlassian.net/browse/AR-559) - First login script - not all locales have UTF8 encoding
* [AR-163](https://armbian.atlassian.net/browse/AR-163) - Systematically cleanup distribution defaults
* [AR-206](https://armbian.atlassian.net/browse/AR-206) - Improve memory performance on Renegade (roc-rk3328-cc) in current
* [AR-472](https://armbian.atlassian.net/browse/AR-472) - Added support for Ubuntu 20.10 Groovy
* [AR-476](https://armbian.atlassian.net/browse/AR-476) - Add sound to Odroid N2
* [AR-485](https://armbian.atlassian.net/browse/AR-485) - Improve multicore compilation
* [AR-487](https://armbian.atlassian.net/browse/AR-487) - Rework download pages
* [AR-508](https://armbian.atlassian.net/browse/AR-508) - Add Odroid HC4
* [AR-514](https://armbian.atlassian.net/browse/AR-514) - Download and verify not fully reliable
* [AR-517](https://armbian.atlassian.net/browse/AR-517) - Mark Bionic builds host as deprecated
* [AR-525](https://armbian.atlassian.net/browse/AR-525) - Bump Rockchip 32bit to 5.9.y
* [AR-526](https://armbian.atlassian.net/browse/AR-526) - Move mvebu-dev kernel to 5.9+
* [AR-546](https://armbian.atlassian.net/browse/AR-546) - Added Pine64 Pinecube
* [AR-547](https://armbian.atlassian.net/browse/AR-547) - First login: adding a non-existing keyboard variant
* [AR-548](https://armbian.atlassian.net/browse/AR-548) - mvebu DFS seems to cause system hang under high I/O
* [AR-551](https://armbian.atlassian.net/browse/AR-551) - Update fan configuration, enable network LED and enable UPS timer
* [AR-552](https://armbian.atlassian.net/browse/AR-552) - Re-enable UHS SDR104 mode for Helios64 and roc-rk3399-pc
* [AR-553](https://armbian.atlassian.net/browse/AR-553) - Update builder to retrieve web seeds from mirrors api
* [AR-556](https://armbian.atlassian.net/browse/AR-556) - Adding vnstat and ZFS support to MOTD
* [AR-557](https://armbian.atlassian.net/browse/AR-557) - GCC compatibility issues
* [AR-558](https://armbian.atlassian.net/browse/AR-558) - Switch mvebu current to K5.9
* [AR-563](https://armbian.atlassian.net/browse/AR-563) - Improve headers compilation
* [AR-565](https://armbian.atlassian.net/browse/AR-565) - SATA on HC4 is not recognized
* [AR-568](https://armbian.atlassian.net/browse/AR-568) - Add Orangepizero 2 WIP target
* [AR-570](https://armbian.atlassian.net/browse/AR-570) - Improper order in getty override.conf
* [AR-571](https://armbian.atlassian.net/browse/AR-571) - Move Meson64 DEV to 5.10.y

## v20.11.1 (2020-12-04)

* [AR-551](https://armbian.atlassian.net/browse/AR-551) - Update fan configuration, enable network LED and enable UPS timer
* [AR-565](https://armbian.atlassian.net/browse/AR-565) - SATA on HC4 is not recognized
Updated Odroid C4/HC4, Helios64, Rockpi 4* images and rockchip64 kernels

## v20.11 (2020-11-24)

Finished projects

* [AR-2](https://armbian.atlassian.net/browse/AR-2) - Improving download infrastructure Phase 1
* [AR-151](https://armbian.atlassian.net/browse/AR-151) - Integrate JMCCs Multimedia script
* [AR-230](https://armbian.atlassian.net/browse/AR-230) - Decide what to do with TVboxes
* [AR-412](https://armbian.atlassian.net/browse/AR-412) - Update Odroid XU4 kernels
* [AR-424](https://armbian.atlassian.net/browse/AR-424) - Improve HTOP config
* [AR-456](https://armbian.atlassian.net/browse/AR-456) - Upgrading Allwinner u-boot to 2020.10
* [AR-476](https://armbian.atlassian.net/browse/AR-476) - Add sound to Odroid N2
* [AR-485](https://armbian.atlassian.net/browse/AR-485) - Improve multicore compilation
* [AR-508](https://armbian.atlassian.net/browse/AR-508) - Add Odroid HC4
* [AR-509](https://armbian.atlassian.net/browse/AR-509) - Upgrade meson64 to 5.9.y
* [AR-510](https://armbian.atlassian.net/browse/AR-510) - Move meson (Odroid C1) to 5.9.y
* [AR-532](https://armbian.atlassian.net/browse/AR-532) - Move Odroid C4 from legacy u-boot toward mainline

Solved bugs

* [AR-314](https://armbian.atlassian.net/browse/AR-314) - Links to SHA files at download pages are wrong
* [AR-372](https://armbian.atlassian.net/browse/AR-372) - Meson64 Reboot failure kernel 5.7
* [AR-373](https://armbian.atlassian.net/browse/AR-373) - Rock64 no HDMI (must be unplugged)
* [AR-382](https://armbian.atlassian.net/browse/AR-382) - Fix zram creation on bigger memory devices
* [AR-391](https://armbian.atlassian.net/browse/AR-391) - Warning a reboot is needed doesn't go away after reboot
* [AR-407](https://armbian.atlassian.net/browse/AR-407) - Bug in first login script
* [AR-417](https://armbian.atlassian.net/browse/AR-417) - HTOP in Bullseye needs higher package version
* [AR-420](https://armbian.atlassian.net/browse/AR-420) - GPIO SPI patch is failing on Rockchip64
* [AR-422](https://armbian.atlassian.net/browse/AR-422) - Improper version showing at upgrade
* [AR-425](https://armbian.atlassian.net/browse/AR-425) - Resize is finished but message doesn't disappear
* [AR-428](https://armbian.atlassian.net/browse/AR-428) - Firefox initial config has different location then ESR variant
* [AR-436](https://armbian.atlassian.net/browse/AR-436) - Rockpi S reports some error in postinst scripts
* [AR-437](https://armbian.atlassian.net/browse/AR-437) - MOTD cosmetic issue
* [AR-439](https://armbian.atlassian.net/browse/AR-439) - Automated rebuilds set image status to USER_BUILT
* [AR-441](https://armbian.atlassian.net/browse/AR-441) - Odroid C4 legacy bootscript problem
* [AR-452](https://armbian.atlassian.net/browse/AR-452) - Fix first boot locales selection and add desktop lang switching
* [AR-459](https://armbian.atlassian.net/browse/AR-459) - Missing package libreoffice-style-tango from Bullseye desktop
* [AR-471](https://armbian.atlassian.net/browse/AR-471) - Mitigate Git server failures
* [AR-482](https://armbian.atlassian.net/browse/AR-482) - Htop doesn't show CPU speed to normal user but shows properly to root
* [AR-484](https://armbian.atlassian.net/browse/AR-484) - Odroid C4 refuse to boot
* [AR-491](https://armbian.atlassian.net/browse/AR-491) - LEDs on Helios4 not working
* [AR-493](https://armbian.atlassian.net/browse/AR-493) - Patches are not creating
* [AR-494](https://armbian.atlassian.net/browse/AR-494) - Fix armbian-hardware-opitimization not being run
* [AR-505](https://armbian.atlassian.net/browse/AR-505) - armbian-hardware-optimization: eth0 tweak applied before it is appear on /proc/interrupts
* [AR-527](https://armbian.atlassian.net/browse/AR-527) - Rockchip 32bit sources were removed
* [AR-528](https://armbian.atlassian.net/browse/AR-528) - Improve creating images from repository
* [AR-529](https://armbian.atlassian.net/browse/AR-529) - Z28 PRO device tree doesn't exists in mainline

Closed tasks

* [AR-284](https://armbian.atlassian.net/browse/AR-284) - Discuss if there is a cleaner way to install Chromium
* [AR-350](https://armbian.atlassian.net/browse/AR-350) - Switch rock64 to mainline u-boot
* [AR-351](https://armbian.atlassian.net/browse/AR-351) - Switch rockpro64 to mainline u-boot
* [AR-363](https://armbian.atlassian.net/browse/AR-363) - Switch mvebu current to K5.8.y
* [AR-380](https://armbian.atlassian.net/browse/AR-380) - Revisit RTL8812AU driver
* [AR-387](https://armbian.atlassian.net/browse/AR-387) - Switch from rk3399-bluetooth service to btbcm for loading firmware/patchram in dev/current
* [AR-388](https://armbian.atlassian.net/browse/AR-388) - XU4 - Introduce new Mem freq scaling patch and re-enable
* [AR-390](https://armbian.atlassian.net/browse/AR-390) - Add Radxa Rockpi 4C
* [AR-400](https://armbian.atlassian.net/browse/AR-400) - Enable overlays in rockchip64-legacy
* [AR-401](https://armbian.atlassian.net/browse/AR-401) - Enable creation of SPI flash u-boot image for ROCK Pi 4
* [AR-403](https://armbian.atlassian.net/browse/AR-403) - Enable overlays in rk3399-legacy
* [AR-404](https://armbian.atlassian.net/browse/AR-404) - Switch renegade to mainline u-boot
* [AR-409](https://armbian.atlassian.net/browse/AR-409) - Move imx6 current kernels to 5.8.y
* [AR-413](https://armbian.atlassian.net/browse/AR-413) - Improve reliability of Helios64's eMMC module
* [AR-415](https://armbian.atlassian.net/browse/AR-415) - Improve reboot reliability for Helios64
* [AR-416](https://armbian.atlassian.net/browse/AR-416) - Move Rockchip 32bit to 5.8.y
* [AR-419](https://armbian.atlassian.net/browse/AR-419) - Add dedicated DT for Nanopi Neo3
* [AR-445](https://armbian.atlassian.net/browse/AR-445) - systemd-journal not rotated with armbian-ramlog
* [AR-458](https://armbian.atlassian.net/browse/AR-458) - Update board support statuses
* [AR-461](https://armbian.atlassian.net/browse/AR-461) - Add Armbian to Neofetch
* [AR-462](https://armbian.atlassian.net/browse/AR-462) - Adapt helios64 device tree name to match upstream Linux
* [AR-464](https://armbian.atlassian.net/browse/AR-464) - Move Libre Computer Renegade to mainline u-boot
* [AR-472](https://armbian.atlassian.net/browse/AR-472) - Added support for Ubuntu 20.10 Groovy
* [AR-473](https://armbian.atlassian.net/browse/AR-473) - Add interactive option to use precompiled packages from Armbian repository
* [AR-477](https://armbian.atlassian.net/browse/AR-477) - Advanced recovery options for rockchip64 boards
* [AR-483](https://armbian.atlassian.net/browse/AR-483) - Fix analog (3.5 jack) audio on ROCK Pi 4C
* [AR-490](https://armbian.atlassian.net/browse/AR-490) - Enable RTC on Odroid N2
* [AR-495](https://armbian.atlassian.net/browse/AR-495) - Allow building images with kernels 5.8.17+ and 5.9.2+
* [AR-499](https://armbian.atlassian.net/browse/AR-499) - Enable Watchdog for G12/Odroidn2
* [AR-504](https://armbian.atlassian.net/browse/AR-504) - Helios64: Switch fusb302 driver to mainline and enable DP over TypeC
* [AR-511](https://armbian.atlassian.net/browse/AR-511) - Switch rockchip64-current to linux 5.9.y
* [AR-513](https://armbian.atlassian.net/browse/AR-513) - Move Odroid XU4 kernels up
* [AR-515](https://armbian.atlassian.net/browse/AR-515) - Upgrade imx6 to 5.9.y
* [AR-521](https://armbian.atlassian.net/browse/AR-521) - Exchange mv with rsync
* [AR-522](https://armbian.atlassian.net/browse/AR-522) - Allow setting MTU for Rockchip64's dwmac interface
* [AR-523](https://armbian.atlassian.net/browse/AR-523) - enable CONFIG_TARGET_CORE for iSCSI target support
* [AR-524](https://armbian.atlassian.net/browse/AR-524) - Upgrade rockpis legacy kernel
* [AR-531](https://armbian.atlassian.net/browse/AR-531) - Check why disabling one update-initramfs breaks Ubuntu initrd making on update

## v20.08.22 (2020-11-8)

Added WIP images for Odroid HC4
Updated images for Odroid C4, N2, C2, Lafrite, Lepotato, KVIM1

## v20.08.13 (2020-10-19)

* [AR-363](https://armbian.atlassian.net/browse/AR-363) - Switch mvebu current to K5.8.y
* [AR-466](https://armbian.atlassian.net/browse/AR-466) - Enable Recovery button on Helios64
* [AR-416](https://armbian.atlassian.net/browse/AR-416) - Move Rockchip 32bit to 5.8.y
* [AR-476](https://armbian.atlassian.net/browse/AR-476) - Add sound to Odroid N2
update all kernels
Rebuild images for Helios4, Helios64 and Odroid N2

## v20.08.11 (2020-10-16)

* [AR-465](https://armbian.atlassian.net/browse/AR-465) - Helios64 cannot boot from eMMC
enable Ubuntu 20.10 Groovy as a CSC build option (need build parameter EXPERT="yes")
update u-boot loader to 2020.10 on Allwinner platform
update all kernels
update images for Helios 64
add option to build images from prebuild packages from repository which drastically improves build time in case you don't need to rebuild kernel

## v20.08.8 (2020-10-05)

* [AR-463](https://armbian.atlassian.net/browse/AR-463) - Improve Helios64 Stability, updated images
Adapt Helios64 devicetree name to match upstream Linux

## v20.08.4 (2020-09-23)

* [AR-399](https://armbian.atlassian.net/browse/AR-399) - Improve Pinebook PRO support, updated images
Updated Helios64 images

## v20.08.3 (2020-09-21)

* updated mainline kernel based images to Linux 5.8.10
* all other kernels updated to respective latest version
* improved htop with showing network status dynamically, GPU temp, improved CPU speed display
* fixed usbip for sharing usb over network
* fixed Odroid C4 boot script bug; adding normal and higher CPU speeds
* added many improvements for Helios64
* enabled GPU temperatures in htop for XU4, meson64 (Odroid N2/N2+) and rockchip64/32
* fixed initial configuration for Firefox
* fixed tx offloading for Rockchip64 NIC’s
* move rockchip 32bit to 5.8.y (Tinkerboard / MiQi)
* improved RK3399 stability by mingling OPP
* fixed a bunch of bugs related to encrypted root filesystem
* enabled hardware watchdog support for mvebu64 / Espressobin
* cosmetic fixes to motd
* enabling I2S and spdif on Nanopi Neo3 by default
* fixes wrong memory calculation on ZRAM display
* fixing firstlogin bug preventing running xrdp
* move Espressobin kernel to 5.8.y
* adjust / fix Kali Linux wifi injections patches

Known bugs:

* Some Rockpro64 boards have troubles with upgrade
* Bananapi M3 eMMC can’t boot from eMMC (solution is available)
* H6 stability issues on some boards
* RockpiS shows some error on upgrade but upgrade suceeds
* 4K and audio on mainline based meson64 boards

## v20.08 (2020-08-20)

Finished projects

* [AR-45](https://armbian.atlassian.net/browse/AR-45) - Make first login more user friendly
* [AR-71](https://armbian.atlassian.net/browse/AR-71) - Create a document: How we will use Jira
* [AR-182](https://armbian.atlassian.net/browse/AR-182) - Unify / merge kernel configs
* [AR-201](https://armbian.atlassian.net/browse/AR-201) - Introduce CI autotest facility
* [AR-227](https://armbian.atlassian.net/browse/AR-227) - Move Espressobin current to K5.6
* [AR-313](https://armbian.atlassian.net/browse/AR-313) - Ability to work in offline mode
* [AR-320](https://armbian.atlassian.net/browse/AR-320) - Initial support for Rockpi E
* [AR-324](https://armbian.atlassian.net/browse/AR-324) - Add Rockchip RK322X SoC support
* [AR-328](https://armbian.atlassian.net/browse/AR-328) - Meson64 move current to 5.7.y
* [AR-329](https://armbian.atlassian.net/browse/AR-329) - Switch sunxi dev target to kernel 5.7
* [AR-331](https://armbian.atlassian.net/browse/AR-331) - Enable kernel boot splash as an option
* [AR-335](https://armbian.atlassian.net/browse/AR-335) - Improve patch making
* [AR-392](https://armbian.atlassian.net/browse/AR-392) - Add Odroid N2+
* [AR-402](https://armbian.atlassian.net/browse/AR-402) - Add Helios64

Solved bugs

* [AR-282](https://armbian.atlassian.net/browse/AR-282) - Rockpi 4B 1Gb doesn't boot modern kernel / u-boot
* [AR-295](https://armbian.atlassian.net/browse/AR-295) - Odroid C2: no more USB devices after upgrade
* [AR-298](https://armbian.atlassian.net/browse/AR-298) - Missing default SElinux policy
* [AR-303](https://armbian.atlassian.net/browse/AR-303) - Create a download page for BPI M2 zero
* [AR-305](https://armbian.atlassian.net/browse/AR-305) - K-worker creates load on Allwinner devices
* [AR-319](https://armbian.atlassian.net/browse/AR-319) - Armbian config failed to switch kernels
* [AR-330](https://armbian.atlassian.net/browse/AR-330) - Shell check bugs
* [AR-332](https://armbian.atlassian.net/browse/AR-332) - When making all kernels - building sometimes fails
* [AR-337](https://armbian.atlassian.net/browse/AR-337) - Odroid XU4 Memcopy Slow on all Kernel 5.x 80MB/sec instead of 370+MB/sec
* [AR-338](https://armbian.atlassian.net/browse/AR-338) - Bananapi R2 does not boot at all
* [AR-340](https://armbian.atlassian.net/browse/AR-340) - Fix WiFi on Nanopi M4V2
* [AR-348](https://armbian.atlassian.net/browse/AR-348) - Confirm RK3399 TcpOffloading bug
* [AR-352](https://armbian.atlassian.net/browse/AR-352) - Fix Random MAC on H3 boards
* [AR-354](https://armbian.atlassian.net/browse/AR-354) - Support User Provided EDID Firmware
* [AR-355](https://armbian.atlassian.net/browse/AR-355) - backport Linux v5.8 fbtft/fb_st7789v invert colors, proper gamma
* [AR-356](https://armbian.atlassian.net/browse/AR-356) - Building multiple u-boot targets breaks
* [AR-371](https://armbian.atlassian.net/browse/AR-371) - CPU frequency scaling broken on H6
* [AR-378](https://armbian.atlassian.net/browse/AR-378) - Increase address room for initial ramdisk
* [AR-381](https://armbian.atlassian.net/browse/AR-381) - selinux-policy-default missing on Debian Bullseye
* [AR-393](https://armbian.atlassian.net/browse/AR-393) - Ask for setting locale at first run

Closed tasks

* [AR-28](https://armbian.atlassian.net/browse/AR-28) - Added new GCC compilers
* [AR-225](https://armbian.atlassian.net/browse/AR-225) - Introduce PACKAGE_LIST for BOARD and FAMILY
* [AR-300](https://armbian.atlassian.net/browse/AR-300) - Enable HDMI audio for OrangePi 4
* [AR-317](https://armbian.atlassian.net/browse/AR-317) - Move Odroid XU4 dev to mainline + patches
* [AR-318](https://armbian.atlassian.net/browse/AR-318) - Upgrade Odroid XU4 legacy kernel
* [AR-321](https://armbian.atlassian.net/browse/AR-321) - Upgrade Meson (C1) current to 5.7.y
* [AR-323](https://armbian.atlassian.net/browse/AR-323) - Allow install to SD NAND for Rockpi S
* [AR-326](https://armbian.atlassian.net/browse/AR-326) - Make USB3 support of ROCK Pi E on par with other rk3328 boards
* [AR-327](https://armbian.atlassian.net/browse/AR-327) - Bump imx6 current kernel to 5.7.y
* [AR-333](https://armbian.atlassian.net/browse/AR-333) - Update Odroid XU4 kernels
* [AR-334](https://armbian.atlassian.net/browse/AR-334) - Cleanup boot environment files
* [AR-336](https://armbian.atlassian.net/browse/AR-336) - Add support for cheap 2.5GB USB network dongles
* [AR-341](https://armbian.atlassian.net/browse/AR-341) - Follow-up N2 CPU Affinity
* [AR-349](https://armbian.atlassian.net/browse/AR-349) - Update mainline u-boot to v2020.07 for rockchip64 and rk3399
* [AR-357](https://armbian.atlassian.net/browse/AR-357) - IRQ affinity improvements for G12B
* [AR-358](https://armbian.atlassian.net/browse/AR-358) - Added initial support for Neo 3
* [AR-361](https://armbian.atlassian.net/browse/AR-361) - Update Odroid XU4 boot.ini
* [AR-362](https://armbian.atlassian.net/browse/AR-362) - HDMI sound support for Allwinner A10, A20, A31
* [AR-364](https://armbian.atlassian.net/browse/AR-364) - Change sunxi legacy to 5.4.y, current to 5.7.y
* [AR-366](https://armbian.atlassian.net/browse/AR-366) - Move rockchip/64 current to 5.7.y
* [AR-383](https://armbian.atlassian.net/browse/AR-383) - Upgrades for Tapatalk plugin
* [AR-389](https://armbian.atlassian.net/browse/AR-389) - Add PACKAGE_LIST_BOARD_REMOVE option

## v20.05.7 (2020-07-02)

* [AR-308](https://armbian.atlassian.net/browse/AR-308) - Disable HDMI in u-boot for rk3399 boards
* [AR-338](https://armbian.atlassian.net/browse/AR-338) - Bananapi R2 does not boot at all
* [AR-337](https://armbian.atlassian.net/browse/AR-337) - Odroid XU4 Memcopy Slow on all Kernel 5.x 80MB/sec instead of 370+MB/sec
Update images for: NanoPC T4, Nanopi M4,Nanopi M4v2, Nanopi Neo4, Orangepi 4, Firefly RK3399, Bananapi R2, Odroid XU4

## v20.05.6 (2020-06-19)

* [AR-324](https://armbian.atlassian.net/browse/AR-324) - Add Rockchip RK322X SoC support
* [AR-320](https://armbian.atlassian.net/browse/AR-320) - Initial support for Rockpi E
* [AR-323](https://armbian.atlassian.net/browse/AR-323) - Allow install to SD NAND for Rockpi S

## v20.05.5

never released/skipped

## v20.05.4 (2020-06-16)

* [AR-311](https://armbian.atlassian.net/browse/AR-311) - Initrd on Focal can get corrupted followup fix

## v20.05.3 (2020-06-10)

* [AR-300](https://armbian.atlassian.net/browse/AR-300) - Enable HDMI audio for OrangePi 4
* [AR-305](https://armbian.atlassian.net/browse/AR-305) - K-worker creates load on Allwinner devices
* [AR-282](https://armbian.atlassian.net/browse/AR-282) - Rockpi 4B 1Gb doesn&#39;t boot modern kernel / u-boot

## v20.05.2 (2020-06-05)

* [AR-294](https://armbian.atlassian.net/browse/AR-294) - Initrd on Focal can get corrupted

## v20.05.1 (2020-05-31)

Kagu

Finished projects

* [AR-108](https://armbian.atlassian.net/browse/AR-108) - Upgrade remaining kernels to 5.4.y
* [AR-158](https://armbian.atlassian.net/browse/AR-158) - Update 3rd party wireless drivers
* [AR-159](https://armbian.atlassian.net/browse/AR-159) - Switch fake-hwclock to hardware RTC on mvebu family
* [AR-168](https://armbian.atlassian.net/browse/AR-168) - Add NanoPi R2S board support
* [AR-180](https://armbian.atlassian.net/browse/AR-180) - Update Wireguard drivers on kernels below 5.4.y
* [AR-184](https://armbian.atlassian.net/browse/AR-184) - Improve slow booting on Rockchip RK3399 devices
* [AR-185](https://armbian.atlassian.net/browse/AR-185) - Change download images compression format
* [AR-190](https://armbian.atlassian.net/browse/AR-190) - Update wireless driver for RTL88x2BU
* [AR-196](https://armbian.atlassian.net/browse/AR-196) - Upgrade u-boot to 2020.04 where possible
* [AR-201](https://armbian.atlassian.net/browse/AR-201) - Introduce CI autotest facility
* [AR-207](https://armbian.atlassian.net/browse/AR-207) - Merge rockpis-dev into rockchip64
* [AR-208](https://armbian.atlassian.net/browse/AR-208) - Consolidate u-boot variants for mvebu family
* [AR-210](https://armbian.atlassian.net/browse/AR-210) - Add support for more HDMI resolutions on Rockchip RK3288 devices
* [AR-215](https://armbian.atlassian.net/browse/AR-215) - Move meson64 dev branch to 5.6.y
* [AR-221](https://armbian.atlassian.net/browse/AR-221) - Upgrade imx6 current to 5.6.y
* [AR-222](https://armbian.atlassian.net/browse/AR-222) - Port Docker image building to Ubuntu 20.04
* [AR-226](https://armbian.atlassian.net/browse/AR-226) - Add Hardkernel Odroid C4 mainline u-boot / kernel
* [AR-236](https://armbian.atlassian.net/browse/AR-236) - Attach Meson64 CURRENT to 5.6.y
* [AR-238](https://armbian.atlassian.net/browse/AR-238) - Updating hostapd, PSD and theme package in repository
* [AR-247](https://armbian.atlassian.net/browse/AR-247) - Revitalise Udoo board
* [AR-250](https://armbian.atlassian.net/browse/AR-250) - Improve usage of external patches
* [AR-253](https://armbian.atlassian.net/browse/AR-253) - Add prerm script for headers
* [AR-254](https://armbian.atlassian.net/browse/AR-254) - Add Banana Pi M2 Zero
* [AR-257](https://armbian.atlassian.net/browse/AR-257) - Bring Odroid C1 back from the EOL with latest upstream kernel
* [AR-260](https://armbian.atlassian.net/browse/AR-260) - Add Nanopi A64 board support
* [AR-261](https://armbian.atlassian.net/browse/AR-261) - Add Rockpi S mainline board support
* [AR-262](https://armbian.atlassian.net/browse/AR-262) - Move Allwinner development branch to 5.6.y
* [AR-278](https://armbian.atlassian.net/browse/AR-278) - Add snap free Chromium to Ubuntu Focal
* [AR-279](https://armbian.atlassian.net/browse/AR-279) - Add Hardkernel Odroid C4 stock kernel

Solved bugs

* [AR-109](https://armbian.atlassian.net/browse/AR-109) - Upgrade is not done properly on some boards
* [AR-165](https://armbian.atlassian.net/browse/AR-165) - Instability with Rock64 and Rock PRO
* [AR-177](https://armbian.atlassian.net/browse/AR-177) - No serial gadget console on Nanopi Neo2 black
* [AR-181](https://armbian.atlassian.net/browse/AR-181) - Odroid N2 crashes during USB rsync backups
* [AR-198](https://armbian.atlassian.net/browse/AR-198) - Olimex Lime 2 doesn't boot from eMMC
* [AR-204](https://armbian.atlassian.net/browse/AR-204) - CPUfreq defaults missing on update
* [AR-205](https://armbian.atlassian.net/browse/AR-205) - No sound output with OrangePi 4 in dev and current
* [AR-211](https://armbian.atlassian.net/browse/AR-211) - Chrony fails to start on Ubuntu Focal
* [AR-212](https://armbian.atlassian.net/browse/AR-212) - Random MAC on Nanopi R2S
* [AR-220](https://armbian.atlassian.net/browse/AR-220) - Disable 3D support in Bionic due to broken mesa packages
* [AR-231](https://armbian.atlassian.net/browse/AR-231) - Unstable stmmac network driver on Meson64
* [AR-237](https://armbian.atlassian.net/browse/AR-237) - Desktop install on Ubuntu Focal installs Gnome3 desktop
* [AR-239](https://armbian.atlassian.net/browse/AR-239) - Chrony fails to start on Focal
* [AR-240](https://armbian.atlassian.net/browse/AR-240) - Broken VFAT kernel upgrade
* [AR-244](https://armbian.atlassian.net/browse/AR-244) - Thermal throttling on H5 doesn't work properly
* [AR-245](https://armbian.atlassian.net/browse/AR-245) - Hostapd doesn't go up
* [AR-248](https://armbian.atlassian.net/browse/AR-248) - Odroid C4 CPU speed is limited to 1.5Ghz
* [AR-249](https://armbian.atlassian.net/browse/AR-249) - Problems with CI testings
* [AR-251](https://armbian.atlassian.net/browse/AR-251) - Fix kernel 5.7.y packages patch
* [AR-255](https://armbian.atlassian.net/browse/AR-255) - Fix Debian mirrors URL
* [AR-263](https://armbian.atlassian.net/browse/AR-263) - Fix audio on Renegade
* [AR-269](https://armbian.atlassian.net/browse/AR-269) - Add correct CPU regulator configuration for the NanoPI R1
* [AR-274](https://armbian.atlassian.net/browse/AR-274) - Add missing iozone3 package to the minimal image
* [AR-277](https://armbian.atlassian.net/browse/AR-277) - Distinguish nightly and stable images at the download pages
* [AR-286](https://armbian.atlassian.net/browse/AR-286) - Armbian-resize-filesystem fails on first run due to missing fdisk in Bullseye
* [AR-287](https://armbian.atlassian.net/browse/AR-287) - Make sure cryptsetup-initramfs is installed in any case

Closed tasks

* [AR-150](https://armbian.atlassian.net/browse/AR-150) - Disable Stretch image creation for Helios4 and Clearfog
* [AR-157](https://armbian.atlassian.net/browse/AR-157) - Add Ubuntu Focal 20.04 as a supported build host
* [AR-186](https://armbian.atlassian.net/browse/AR-186) - Blacklist 3D engine on headless images
* [AR-189](https://armbian.atlassian.net/browse/AR-189) - Move wireless driver for 8189ES from patch to git
* [AR-195](https://armbian.atlassian.net/browse/AR-195) - Adding Ubuntu 20.04 to all builds
* [AR-209](https://armbian.atlassian.net/browse/AR-209) - Disable CONFIG_VIDEO_DE2 in u-boot for Allwinner devices
* [AR-213](https://armbian.atlassian.net/browse/AR-213) - Make manual for .xz images and check their authentication
* [AR-228](https://armbian.atlassian.net/browse/AR-228) - Enable audio and USB on Nanopi A64
* [AR-229](https://armbian.atlassian.net/browse/AR-229) - Bump with AUFS for DEV kernels
* [AR-232](https://armbian.atlassian.net/browse/AR-232) - Switch Odroid XU4 DEV branch to Libreelec branch
* [AR-234](https://armbian.atlassian.net/browse/AR-234) - Disable ZSH update prompt on every two weeks
* [AR-242](https://armbian.atlassian.net/browse/AR-242) - Enable SELinux
* [AR-252](https://armbian.atlassian.net/browse/AR-252) - Improve source code cleaning
* [AR-258](https://armbian.atlassian.net/browse/AR-258) - Enables PCIE PHY with Mezzanine NVME
* [AR-259](https://armbian.atlassian.net/browse/AR-259) - Add mp8859 regulator to current for RK3399-ROC-PC
* [AR-264](https://armbian.atlassian.net/browse/AR-264) - Enable RTL8723DS WiFI driver
* [AR-265](https://armbian.atlassian.net/browse/AR-265) - Remove Xenial from supported host OS
* [AR-266](https://armbian.atlassian.net/browse/AR-266) - Fix dependency for native building on Linux Mint and Debian Buster
* [AR-267](https://armbian.atlassian.net/browse/AR-267) - Enable Cedrus video acceleration on Allwinner kernels
* [AR-268](https://armbian.atlassian.net/browse/AR-268) - Add higher clock for Allwinner H6
* [AR-270](https://armbian.atlassian.net/browse/AR-270) - Add support for alternate console UARTs in Allwinner H3 u-boot
* [AR-271](https://armbian.atlassian.net/browse/AR-271) - Lower DDR clock rate to 504MHz for H5 boards
* [AR-280](https://armbian.atlassian.net/browse/AR-280) - Update CONF, CSC and WIP statuses according to support level
* [AR-285](https://armbian.atlassian.net/browse/AR-285) - Improve thermal throttling on Allwinner H6
* [AR-288](https://armbian.atlassian.net/browse/AR-288) - Add vendor name to the board config files

## v20.02.12 (2020-04-27)

* Added preview images for Odroid C4

## v20.02.8 (2020-03-26)

* update kernels with upstream versions, synchronise and test kernel sources download

## v20.02.7 (2020-03-26)

* Updated images for Rockpi S, Odroid XU4 and FriendlyARM Nanopc T3, T3+, M3, Fire3

## v20.02.6 (2020-03-23)

* Updated images for Rockpi S and Orangepi 4
* Updated armbian-config (fixed OMV installer)

## v20.02.5 (2020-03-19)

* Updated images for Orangepi 4, Bananapi and Rockpi S

## v20.02.4 (2020-03-18)

* Added images for Nanopi R2S and Bananapi M2 Zero
* Kernel update for Odroud XU4

## v20.02.3 (2020-02-21)

* Updating images for Le potato, Khadas Vim1,La Frite, Nanopik2 S905, Odroid N2/C2 - fixing audio
* Updating images for Orangepi 4 - boot loader problem

## v20.02.2 (2020-02-18)

Chiru

Tasks

* [AR-46](https://armbian.atlassian.net/browse/AR-46) - Support for single function run
* [AR-47](https://armbian.atlassian.net/browse/AR-47) - Adding Docker shell support
* [AR-49](https://armbian.atlassian.net/browse/AR-49) - Move sunxi kernel to 5.4.y
* [AR-79](https://armbian.atlassian.net/browse/AR-79) - Check and adjust AUFS patch for 5.4.y
* [AR-80](https://armbian.atlassian.net/browse/AR-80) - Move imx6 to 5.4.y
* [AR-81](https://armbian.atlassian.net/browse/AR-81) - Enable Meson64 DEV at 5.4.y
* [AR-82](https://armbian.atlassian.net/browse/AR-82) - Move Mvebu64 / Espressobin dev kernel to 5.4.y
* [AR-84](https://armbian.atlassian.net/browse/AR-84) - Move rockchip64 current to 5.4.y
* [AR-85](https://armbian.atlassian.net/browse/AR-85) - Adjusted Sunvell R69
* [AR-90](https://armbian.atlassian.net/browse/AR-90) - Add support for Nanopi M4 v2
* [AR-92](https://armbian.atlassian.net/browse/AR-92) - Enable stable MAC address from cpuid on rk3399
* [AR-96](https://armbian.atlassian.net/browse/AR-96) - Update Xradio wireless driver
* [AR-97](https://armbian.atlassian.net/browse/AR-97) - Tag supported builds properly at download pages
* [AR-98](https://armbian.atlassian.net/browse/AR-98) - Enable missing Kuberenetes kernel dependency
* [AR-100](https://armbian.atlassian.net/browse/AR-100) - Add Debian Bullseye and Ubuntu Focal
* [AR-112](https://armbian.atlassian.net/browse/AR-112) - Enabled internal WLAN on RockPi S
* [AR-113](https://armbian.atlassian.net/browse/AR-113) - Install wireguard tools only when selected
* [AR-114](https://armbian.atlassian.net/browse/AR-114) - Enable audio codec on Orangepi Win
* [AR-115](https://armbian.atlassian.net/browse/AR-115) - Add drivers for Realtek RTL8811CU and RTL8821C chipsets
* [AR-116](https://armbian.atlassian.net/browse/AR-116) - Remove annoying debug message filling logs on 8189es
* [AR-117](https://armbian.atlassian.net/browse/AR-117) - Add Pine H64 model B
* [AR-124](https://armbian.atlassian.net/browse/AR-124) - Enable wireless on Rockpi-S
* [AR-127](https://armbian.atlassian.net/browse/AR-127) - Refactoring wifi patches
* [AR-128](https://armbian.atlassian.net/browse/AR-128) - Adding WIP support for Pinebook PRO
* [AR-129](https://armbian.atlassian.net/browse/AR-129) - Move NanopiM4 V2 and Pine H64 under supported
* [AR-134](https://armbian.atlassian.net/browse/AR-134) - Update AUFS version on Odroid XU4 and Nanopi Fire3/T3/T3+
* [AR-138](https://armbian.atlassian.net/browse/AR-138) - Update RK3399 legacy kernel (Nanopi M4, T4, Neo4) to latest upstream version
* [AR-139](https://armbian.atlassian.net/browse/AR-139) - Nanpi R1 - move primary serial console to ttyS1 which is on the chassis
* [AR-143](https://armbian.atlassian.net/browse/AR-143) - Create OpenHab installation instructions for their official documentation
* [AR-146](https://armbian.atlassian.net/browse/AR-146) - Update rockchip-legacy to most recent upstream kernel version
* [AR-147](https://armbian.atlassian.net/browse/AR-147) - Enable analogue audio on Allwinner H6
* [AR-148](https://armbian.atlassian.net/browse/AR-148) - [ mvebu-current ] Fix cpufreq (dynamic frequency scaling)
* [AR-149](https://armbian.atlassian.net/browse/AR-149) - [ mvebu-current ] Fix pcie issues
* [AR-153](https://armbian.atlassian.net/browse/AR-153) - Enable USB3 for Rock64/Renegade with RK3328 on mainline kernel
* [AR-154](https://armbian.atlassian.net/browse/AR-154) - Add analogue audio driver to Allwinner H6
* [AR-155](https://armbian.atlassian.net/browse/AR-155) - Enable Cedrus video acceleration support on Allwinner boards
* [AR-167](https://armbian.atlassian.net/browse/AR-167) - Add upstream patches for Odroid XU4
* [AR-172](https://armbian.atlassian.net/browse/AR-172) - USB3 Support for Rockchip

Bugs

* [AR-74](https://armbian.atlassian.net/browse/AR-74) - User patches directories not created
* [AR-76](https://armbian.atlassian.net/browse/AR-76) - Rockchip64 missing CPU_MIN variable
* [AR-77](https://armbian.atlassian.net/browse/AR-77) - Wrong board name variable for Orangepi RK 3399
* [AR-83](https://armbian.atlassian.net/browse/AR-83) - Packaging patch broken for kernel 5.4.y
* [AR-86](https://armbian.atlassian.net/browse/AR-86) - CPU freq scaling for H6 doesn&#39;t work in K5.4
* [AR-88](https://armbian.atlassian.net/browse/AR-88) - Banana Pi M3 does not boot
* [AR-89](https://armbian.atlassian.net/browse/AR-89) - Tinkerboard S doesn&#39;t start from eMMC
* [AR-91](https://armbian.atlassian.net/browse/AR-91) - Broken Allwinner overlays
* [AR-94](https://armbian.atlassian.net/browse/AR-94) - Espressobin v7 with 2gb of ram fail to boot
* [AR-102](https://armbian.atlassian.net/browse/AR-102) - Missing packaging patch for Rockpis legacy kernel
* [AR-103](https://armbian.atlassian.net/browse/AR-103) - PPA way of adding sources are failing on Ubuntu
* [AR-104](https://armbian.atlassian.net/browse/AR-104) - 32bit rust compiler doesn&#39;t run new kernels
* [AR-105](https://armbian.atlassian.net/browse/AR-105) - Orangepi Zero Plus 2 doesn&#39;t boot
* [AR-106](https://armbian.atlassian.net/browse/AR-106) - Wireguard breaks building on 5.4.y
* [AR-107](https://armbian.atlassian.net/browse/AR-107) - Improve compiler and rootfs download process
* [AR-110](https://armbian.atlassian.net/browse/AR-110) - Missing Bionic image for Nanopi Neo Plus2
* [AR-111](https://armbian.atlassian.net/browse/AR-111) - Some versions of Orangepi Win does not boot modern kernel
* [AR-118](https://armbian.atlassian.net/browse/AR-118) - NanoPi M4V2 ethernet partialy broken in one side
* [AR-123](https://armbian.atlassian.net/browse/AR-123) - OpenHAB2 installation is failing
* [AR-125](https://armbian.atlassian.net/browse/AR-125) - Wireless driver for 8188EUS breaks on K4.14
* [AR-126](https://armbian.atlassian.net/browse/AR-126) - Nanopi M3/Fire3/PC3 compilation breaks
* [AR-130](https://armbian.atlassian.net/browse/AR-130) - Instability with various A64 boards
* [AR-131](https://armbian.atlassian.net/browse/AR-131) - Add support for 3rd version of Pinebook A64 panel
* [AR-133](https://armbian.atlassian.net/browse/AR-133) - Odroid XU4 legacy kernel images instability
* [AR-141](https://armbian.atlassian.net/browse/AR-141) - Odroid XU4 current with kernel 5.4.y seems unstable
* [AR-142](https://armbian.atlassian.net/browse/AR-142) - Cryptsetup disk encryption build feature broken
* [AR-144](https://armbian.atlassian.net/browse/AR-144) - Tinkerboard break booting
* [AR-145](https://armbian.atlassian.net/browse/AR-145) - Missing HDMI audio on H3 boards
* [AR-152](https://armbian.atlassian.net/browse/AR-152) - Display issues with Bionic Mesa update
* [AR-164](https://armbian.atlassian.net/browse/AR-164) - Htop package does not build in qemu under Ubuntu Focal 20.04
* [AR-166](https://armbian.atlassian.net/browse/AR-166) - Rootfs cache number creates a window of 12h when users are forced to rebuild cache
* [AR-170](https://armbian.atlassian.net/browse/AR-170) - Wireless not connecting for SBCs
* [AR-171](https://armbian.atlassian.net/browse/AR-171) - Fix broken loading process on MiQi
* [AR-173](https://armbian.atlassian.net/browse/AR-173) - Fix makefile of kernel headers 4.4.210 for rk3399
* [AR-174](https://armbian.atlassian.net/browse/AR-174) - Teres Keyboard Not Working

Stories

* [AR-48](https://armbian.atlassian.net/browse/AR-48) - Bump u-boot to 2020.01 on RK3399 boards
* [AR-156](https://armbian.atlassian.net/browse/AR-156) - WIP orangepi 4 preliminary support

## v19.11.3 (2019-11-20)

Tasks

* [AR-1](https://armbian.atlassian.net/browse/AR-1) - Adding support category for distributions
* [AR-4](https://armbian.atlassian.net/browse/AR-4) - Remove Allwinner legacy
* [AR-5](https://armbian.atlassian.net/browse/AR-5) - Drop Udoo family and move Udoo board into newly created imx6 family
* [AR-9](https://armbian.atlassian.net/browse/AR-9) - Rename sunxi-next to sunxi-legacy
* [AR-10](https://armbian.atlassian.net/browse/AR-10) - Rename sunxi-dev to sunxi-current
* [AR-11](https://armbian.atlassian.net/browse/AR-11) - Adding Radxa Rockpi S support
* [AR-13](https://armbian.atlassian.net/browse/AR-13) - Rename rockchip64-default to rockchip64-legacy
* [AR-14](https://armbian.atlassian.net/browse/AR-14) - Add rockchip64-current as mainline source
* [AR-15](https://armbian.atlassian.net/browse/AR-15) - Drop Rockchip 4.19.y NEXT, current become 5.3.y
* [AR-16](https://armbian.atlassian.net/browse/AR-16) - Rename RK3399 default to legacy
* [AR-17](https://armbian.atlassian.net/browse/AR-17) - Rename Odroid XU4 next and default to legacy 4.14.y, add DEV 5.4.y
* [AR-18](https://armbian.atlassian.net/browse/AR-18) - Add Odroid N2 current mainline
* [AR-19](https://armbian.atlassian.net/browse/AR-19) - Move Odroid C1 to meson family
* [AR-20](https://armbian.atlassian.net/browse/AR-20) - Rename mvebu64-default to mvebu64-legacy
* [AR-21](https://armbian.atlassian.net/browse/AR-21) - Rename mvebu-default to mvebu-legacy
* [AR-22](https://armbian.atlassian.net/browse/AR-22) - Rename mvebu-next to mvebu-current
* [AR-23](https://armbian.atlassian.net/browse/AR-23) - Drop meson64 default and next, current becomes former DEV 5.3.y
* [AR-24](https://armbian.atlassian.net/browse/AR-24) - Drop cubox family and move Cubox/Hummingboard boards under imx6
* [AR-26](https://armbian.atlassian.net/browse/AR-26) - Adjust motd
* [AR-27](https://armbian.atlassian.net/browse/AR-27) - Enabling distribution release status
* [AR-28](https://armbian.atlassian.net/browse/AR-28) - Added new GCC compilers
* [AR-29](https://armbian.atlassian.net/browse/AR-29) - Implementing Ubuntu Eoan
* [AR-30](https://armbian.atlassian.net/browse/AR-30) - Add desktop packages per board or family
* [AR-31](https://armbian.atlassian.net/browse/AR-31) - Remove (Ubuntu/Debian) distribution name from image filename
* [AR-32](https://armbian.atlassian.net/browse/AR-32) - Move arch configs from configuration.sh to separate arm64 and armhf config files
* [AR-33](https://armbian.atlassian.net/browse/AR-33) - Revision numbers for beta builds changed to day_in_the_year
* [AR-34](https://armbian.atlassian.net/browse/AR-34) - Patches support linked patches
* [AR-35](https://armbian.atlassian.net/browse/AR-35) - Break meson64 family into gxbb and gxl
* [AR-36](https://armbian.atlassian.net/browse/AR-36) - Add Nanopineo2 Black
* [AR-38](https://armbian.atlassian.net/browse/AR-38) - Upgrade option from old branches to new one via armbian-config
* [AR-41](https://armbian.atlassian.net/browse/AR-41) - Show full timezone info
* [AR-43](https://armbian.atlassian.net/browse/AR-43) - Merge Odroid N2 to meson64
* [AR-44](https://armbian.atlassian.net/browse/AR-44) - Enable FORCE_BOOTSCRIPT_UPDATE for all builds
* [AR-57](https://armbian.atlassian.net/browse/AR-57) - New kernel feature requested CONFIG_BLK_DEV_DRBD
* [AR-60](https://armbian.atlassian.net/browse/AR-60) - Modified logrotate.service
* [AR-63](https://armbian.atlassian.net/browse/AR-63) - Docker maintenance features

Bugs

* [AR-25](https://armbian.atlassian.net/browse/AR-25) - Armbian resize stopped working in Ubuntu 19.10 or higher
* [AR-40](https://armbian.atlassian.net/browse/AR-40) - When changing console layout it does not change
* [AR-51](https://armbian.atlassian.net/browse/AR-51) - Prevent configuring locale
* [AR-52](https://armbian.atlassian.net/browse/AR-52) - Broken desktop install
* [AR-54](https://armbian.atlassian.net/browse/AR-54) - Upstream package name changed
* [AR-55](https://armbian.atlassian.net/browse/AR-55) - Wireless driver remove patch for Odroid XU4 broke down
* [AR-56](https://armbian.atlassian.net/browse/AR-56) - Missing CPU regulator
* [AR-58](https://armbian.atlassian.net/browse/AR-58) - Troubles with wireless on Nanopi DUO &amp; Opi Zero
* [AR-59](https://armbian.atlassian.net/browse/AR-59) - Compressed files are getting back to /var/log
* [AR-62](https://armbian.atlassian.net/browse/AR-62) - No HDMI sound on various meson64 boards
* [AR-64](https://armbian.atlassian.net/browse/AR-64) - Docker require root
* [AR-68](https://armbian.atlassian.net/browse/AR-68) - Broken Ethernet on Pine64+

Stories

* [AR-61](https://armbian.atlassian.net/browse/AR-61) - Adding support for LOCAL_MIRROR
* [AR-65](https://armbian.atlassian.net/browse/AR-65) - Moving configs under userpatches
* [AR-66](https://armbian.atlassian.net/browse/AR-66) - Enable build system torrent download by default
* [AR-67](https://armbian.atlassian.net/browse/AR-67) - Install Docker when we want to build under Docker
* [AR-69](https://armbian.atlassian.net/browse/AR-69) - Use kernel command line instead of a patch
* [AR-70](https://armbian.atlassian.net/browse/AR-70) - Enable Lima kernel driver on meson64
* [AR-73](https://armbian.atlassian.net/browse/AR-73) - Enable PCI on Rockpi 4 and overlay for GEN2 speed

## v5.98 (2019-10-09)

* changed ntptime with chrony
* fixed serial console on several hosts
* added FriendlyARM ZeroPi
* enabled gadgets on rockchip64
* bumped RK3399 boards to latest kernel, recreate images and repository
* merged odroidxu4 down to default since we only have one kernel
* fixed Cubox images, move them to stock kernel
* fixed low Synaptic search speed

Build script:

* script configurations were migrated to userpatches
* added option to create minimal images with around 500Mb in size BUILD_MINIMAL="yes"
* added initial support of MCIMX7SABRE board (CSC)
* updates for xt-q8l-v10 (CSC)
* Docker is installed automatically if one want use it (Debian based build host only)
* refactor build all images scripting that images can be build in full parallel mode
* added one file for storing which combinations shell be made for each board
* replaced Etcher with dd + verify for directly burning images when done
* cleaned initial config and remove confusing advanced options out

## v5.92 (2019-08-02)

* updated sunxi NEXT (4.19.63) and DEV (5.2.5) kernels
* updated htop application to show cpu speed and temperature (buster / disco)

## v5.91 (2019-07-31)

* created new images for Helios4 and Clearfog Pro/Base
* moved mvebu DEFAULT, NEXT and DEV branch to next kernel (LTS) and U-boot version
* fixed armada_thermal sensor reading, adjusted Helios4 fancontrol configuration
* fixed ODT on data signals of DDR RAM for Armada A388 SOMs
* recreated Armbian Buster images due to a bug in Network manager which in some cases failed to initiate network connection

Armbian-config:

* added Emby installation
* updated Plex install to use official repo
* added netmask-to-CIDR function for manual IP configuration

## v5.90 (2019-07-07)

* added Armbian Buster images for all boards
* added [Macchiatobin Doubleshot](https://www.armbian.com/macchiatobin-double-shot/) CSS target and images
* added images with test kernel v5.1.y for: Orangepi3, Lite2, One+, PineH64, Odroid C1, Teres, Pinebook
* added wireless [drivers for 88x2bu](https://forum.armbian.com/topic/10549-rtl88x2bu-support-in-armbian/)
* added eMMC support for Nanopi K2 (booting from doesn't work yet)
* added dual w1 overlay for meson64 family
* updated wireless [drivers for Realtek 8811, 8812, 8814 and 8821](https://github.com/aircrack-ng/rtl8812au)
* updated wireless [drivers for rtl8188eus & rtl8188eu & rtl8188etv](https://github.com/aircrack-ng/rtl8188eus)
* added latest [Wireguard driver](https://www.wireguard.com/)
* enable eMMC on Orangepi Win Plus
* enable Bluetooth on Tinkerboard, Nanopi4, Rockpi 4 CLI images
* improved ALSA config on Tinkerboard
* fixed Bluetooth on Nanopi M4/Neo4/T4 and Rockpi4
* fixed wireless drivers on OPi3 & Lite2
* fixed temperature readout on Allwinner H5 boards
* fixed SPI related bug on Allwinner 5.1.y kernel
* fixed HDMI output and bump kernel to 5.1.y on imx6 boards
* fixed eMMC install, add rootdev= to armbianEnv if missing
* fixed A10/A20 [SATA write speed](https://twitter.com/armbian/status/1127638533630459904)
* set default build target from Debian Stretch to Buster for all boards
* changed CPU clock back to 1.5/1.8Ghz defaults on boards with RK3399 to minimise thermal throttling
* changed motd console welcome text to: "Welcome to Debian Stretch with Armbian Linux 5.1.6-sunxi"
* changed display manager to lightdm by default and remove nodm completely
* changed u-boot for A64 to upstream sources
* changed RK3399 to U-boot 2019.04
* added URL to the build script and commit hash to /etc/armbian-release file
* added synaptic package manager and on-board keyboard to the desktop base
* added "logout" to the panel/menu
* added normal users to additional groups: disk tty users games
* updated all kernels with upstream
* updated ATF and bootloader on Espressobin, supporting all versions

Build script:

* added mirrors for speed-up building in China mainland
* added support for download compilers and rootfs cache via torrent network
* added new output image compression option (xz)
* enabled Debian Buster and Ubuntu Disco (unsupported) targets
* few Docker building improvements, caching image
* replace curl with aria2
* Linaro compilers update to 2019.02

Armbian-config:

* added Gimp installation
* added enable/disable Avahi
* updated OMV installer, OMV5 preparations
* enable screen resolution changer for Odroid N2
* enable CPU speed and governor adjustment

## v5.87 (2019-05-26)

* added support for [Odroid N2](https://www.armbian.com/odroid-n2/), [Nanopi R1](https://www.armbian.com/nanopi-r1/), [Nanopi Duo2](https://www.armbian.com/nanopi-duo-2/)
* enabled nightly images for Orangepi3, One+, Lite2, PineH64, Rock64pro, RockPi4b
* enabled nigtly Buster and Disco images for Le Potato
* recompiled all images and pushed update where updates are known to work (sunxi, sunxi64, meson64, ...)
* improved SATA write speed on [A20 chips for up to 300%](https://forum.armbian.com/topic/10352-a20-sata-write-speed-improvement/)
* fixed thermal throtling for H5 devices
* mainline u-boot moved 2019.04
* most development kernels moved to 5.1.y
* added separate DT for espressobinv7, updated boot loader
* enable WoL for eth0 on Helios4

Build script:

* added Debian Buster and Ubuntu Disco (WIP)
* improved building under Docker. Source code is not copied to docker image, caching image
* Linaro compilers update to 2019.02
* fixed incomplete cleaning of the source code

Armbian-config:

* fixed kernel changing
* fixed sources download
* fixed Hass.IO and TVheadend install
* added menu driven CPU frequency/governor adjustement
* improved two-factor authentication
* added meson64 and rockchip to overlay/hardware configuration
* improved hostapd management

Infrastructure:

* main download server has been hooked to 10GbE connection.
* added [web/http seeds](https://forum.armbian.com/topic/4198-seed-our-torrents) to torrent download. Torrent download could/should fully utilize your download capacity.
* major forum upgrade ([v4.4.3](https://invisioncommunity.com/release-notes/))
* added another IPV6 capable EU mirror <https://mirrors.dotsrc.org>

## v5.76 (2019-02-11)

* remove Exagear Desktop

## v5.75 (2019-02-10)

* added updated driver for Realtek 8811, 8812, 8814 and 8821 chipsets
* added Wireguard support to remaining kernels (except lower than 3.10)
* images rebuild with latest upstream sources, mainline u-boot was bumped to 2018.11

## v5.74 (2019-01-31)

* fixing systemd related [bug found](https://forum.armbian.com/topic/9289-ssh-not-working-after-upgrade-orange-pi-lite-armbian_ubuntu_xenial/) in sunxi legacy 3.4.y kernels

## v5.73 (2019-01-29)

* much faster armbian-install operations. Thanks to @dedalodaelus
* added support for @wireguard on all kernels higher than 3.10.y
* fixed drivers for popular DVB tuner S960 (all kernels)
* fixed bug in wireless drivers on Cubietruck, BananpiPRO, Bananapi+
* fixed AP mode on Orangepi PC+, Prime, One, .. when using kernel 4.19.y
* added prolific USB-to-USB bridges in mvebu-next/dev
* added nftables masquerade in mvebu64-next
* added MD raid support for SUNXI64
* upgrade bugfix for Helios4
* updated hostapd to 2.7
* fixed 1512MHz OPP on Renegade
* fixed DRM crashing for rockchip64
* mainline u-boot bumped to 2018.11 (update goes manually from armbian-install utility)
* added testing images for Orangepi RK3399 and Radxa Rockpi 4B

## v5.72 (2019-01-16)

* added additional repository mirror (updated armbian-config)
* [fixed Tinkerboard DTB](https://forum.armbian.com/topic/9312-tinkerboard-ss-bricked-after-570-upgrade/?tab=comments#comment-69964) in repository and images rebuild

## v5.71 (2019-01-16)

* updated images for Odroid C2, Lepotato and Nanopik2-S905 due to [this bug](https://github.com/armbian/build/commit/01571c0a4c6c3e7cdb1fec8c99465d8fc00c8c90)

## v5.70 (2019-01-12)

* sunxi-next and sunxi64-next were moved from 4.14.y to 4.19.y (remake of all AW images)
* better DVFS on H3/H5/A64, enabled higher cpu speed.
* added overlay support for Tinkerboard/rockchip next and kernel upped to 4.19.y
* updated next kernel for Odroid XU4 to 4.19.y
* updated next kernel for Odroid C2, Lepotato and Nanopik2-S905 to 4.19.y with overlay support
* fixed poweroff on H5
* H5/A64 lost experimental status,
* upgraded images and upstream/bugfix kernel upgrade for Rock64, Renegade,
* u-boot update is moved from automated to manual (armbian-config) to minimize boot related troubles
* added two repository mirrors: China and France (armbian-config -> Personal -> Mirror)
* changed switching to alternative kernels from armbian-config. It is possible to select a direct version and it only replaces kernel (safer)
* first official build for Olimex Teres
* mainline kernel builds for: Pine64, Pine64so, Olinuxino A64, OrangepiWin
* added more download variants for Rock64, Renegade, Tritium H3&H5
* updated images for Z28PRO, Bananapi PRO, Espressobin, Olimex Micro, Lime, Udoo, Bananapi M2, Bananapi M2U,

## v5.68 (2018-12-30)

* updated Espressobin images, kernel updated to 4.19.y

## v5.67 (2018-11-26)

* updated Helios4 images
* added experimental mainline kernel images for Pinebook and Pinebook 1080p

## v5.67 (2018-11-12)

* updated images for Bananapi R2 with eMMC install support.

## v5.66 (2018-11-08)

* added Mediatek MT7623 family.
* added images for Bananapi R2 with kernel 4.19.y without official support.

## v5.66 (2018-11-07)

* removing Odroid C2 official support, drop its default 3.16.y kernel from build engine and merge with the meson64 family.
* attach meson64 dev to 4.19.y
* drop Udoo Neo completly, drop Udoo Quad default and dev kernel.
* Odroid XU4: drop kernel 3.10.y, default branch is upgraded to offical 4.14.y, next becomes vanilla 4.19.y

## v5.65 (2018-11-06)

* Cubox-i/Hummigboard: drop kernel 3.14.y and move 4.14.y to default, next becomes 4.19.y, dev 4.19.y with a mainline u-boot

## v5.64 (2018-10-09)

* updated images and packages for Helios4.
* added images for Nanopi Neo4.

## v5.63 (2018-10-08)

* updated images for Helios4 with SPI booting support.
* updated armbian-config. Added advanced ZSH shell install with most used plugins and tmux.

## v5.62 (2018-10-01)

* updated armbian-config

## v5.61 (2018-09-26)

* updated armbian-config,
* fixed Chromium on Debian builds with a workaround. We are overwriting package with last known working one. It will show some error on startup which is safe to ignore. This workaround will fade out with Chromium upstream update.

## v5.60 (2018-09-19)

Changes overview:

General:

* Ubuntu Xenial was replaced with Bionic unless kernel was too old for the change,
* Debian Jessie becomes EOL and its building is not maintained anymore while you will still receive kernel updates,
* Emergency swap file creation is disabled by default since we use compressed memory (ZRAM) as an alternative,
* `vm.swappiness` has been changed from 0 to 100 (if you run databases on your board you might want to revert this change in `/etc/sysctl.conf`),
* RAM logging also uses ZRAM now and rotates logs automagically,
* all images were rebuilt, except boards for which support ended,
* significantly lighter - browser only - desktop images (< 1.5G),
* fixed hanging on headers installation,
* install boot script (BSP package) if not present. This fixes upgrade or kernel switching problems,
* Proper bind mount directory when installing to SATA/USB and booting from SD,
* update for wireless drivers 8812/11/14AU, 8188EU and AUFS,
* Bugfix when a temperature is not present or readings are invalid,
* Also showing bridge IP addresses in MOTD,
* storing package list compressed - saves 50-70Mb,
* enlarging automated apt-get update and purge intervals,
* smaller overhead for CLI images,
* improved alternative kernel switching,
* stop setting Google's DNS server as default for privacy reasons.

Family:

* sunxi and sunxi64, u-boot was bumped to 2018.05, NEXT branch was updated to the latest 4.14.y, DEV is attached to 4.18.y + fixed overlay support,
* mvebu64, default BSP kernel was upgraded to 4.14.y, NEXT to 4.18.y,
* odroidc1, experimental NEXT kernel branch was attached to 4.18.y,
* odroidc2 kernel was merged with meson64 on the source level,
* meson64 u-boot was pushed to 2018.05, a default was updated to the latest 4.14.y, NEXT to 4.18.y,
* rk3288, u-boot was pushed to 2018.05, legacy kernel cleaned and fixed after upstream troubles, NEXT branch was updated to the latest 4.14.y,
* rockchip64, rk3399 was split into rk3399 for Friendly ARM boards and rockchip64 for Rock64 and RockPro, Ayufan repository. Merging is postponed for the future,
* s5p6818 family support added NEXT branch was updated to the latest 4.14.y,
* mvebu, NEXT branch was updated to latest 4.14.y, DEV attached to 4.18.y,
* fixed randomly failing X server on imx6 family,

Board:

* added WIP support for Firefly RK3399, Lime A64, Renegade, Rockpro64, Olimex Teres
* added experimental images for Bananapi M3 and Cubietruck+,
* adeed support for: Tinkerboard S, Rock64, Orangepi Zero Plus, Nanopi Neo Core2, Nanopi M4,
* added NEO 1.1 regulator overlay,
* added Helios4 device tree with FAN control for modern kernel,
* enabled SPI access on Espressobin,
* updated SPI boot firmware on Espressobin (18.09.1) with many fixes and support for booting from USB, SATA, eMMC or SD,
* added Tinkerboard S DC-IN voltage to armbianmonitor,
* fixed network interface initialization,
* fixed clock drift on Bananapi boards,
* enabled concurrent AP/STA mode on Tinkerboard,
* improved support for NanoPi Fire 3 (added SPU1705, DVFS, thermal tables, etc.),
* fixed network crashing on high load. Affected: Odroid C1/C2, Le Potato kernel 4.18.y,
* fixed wireless, eMMC and Bluetooth on (unsupported) Z28 PRO and changed boot order,
* fixed eMMC install on NanoPC T3+ and Docker dependencies on Fire3, M3, NanoPC T3+,
* added eMMC and DVFS support on Espressobin mainline kernel,
* ported Tinkerboard UMS to modern u-boot,
* enabled 1392 MHz cpufreq OPP on all RK3328 devices,
* enabled 1992/1512MHz cpufreq OPP on all RK3399 devices,
* added eMMC to OlinuXino A64 kernel and u-boot,
* added Sunvell R69 CSC target,
* OrangepiWin: fixed BT,
* fixed ethernet on (unsupported) Bananapi M64.

Build script:

* changed recommended build host to Bionic, Xenial still supported for everything except building Bionic images,
* added support for burning image directly to SD card when your build is done by using Etcher for CLI,
* added support for making LUKS encrypted root images, parameters: CRYPTROOT_ENABLE=yes, CRYPTROOT_PASSPHRASE=unlockpass,
* fixed building under Docker, bumped to Bionic host,
* added building Bionic and block building it for images with too old kernels,
* added multibranch support (LIB_TAG).

Infrastructure:

* build machine main SSD and memory upgrade, switched from bare metal Ubuntu Xenial to fully optimsed Debian KVM server, free build capacity is avaliable for any armbian related activity upon request,
* download server drive capacity and download speed upgrade, IPV6,
* geo load balancing for repository and download server is under testing,
* improved repository management. Possibility to add packages via Github,
* introducing new internal parameter, example: BUILD_ALL="yes" REBUILD_IMAGES="bananapi,udoo,rock64" to specify which images need rebuilding,
* main torrent server cleanup, removed deprecated images,
* creating report <https://beta.armbian.com/buildlogs/report.html> when building all kernels. Prepared to include simple per board testing report where exists <https://github.com/armbian/testings>.

Known bugs:

* modern kernel support on A64 boards is mainly broken.

## v5.59 (2018-08-18)

* rebuilt images for Espressobin with kernel 4.18.y, Nanopc T4

## v5.58 (2018-08-13)

* rebuilt images for Bananapi, Bananapi Pro, Bananapi+, Odroid C2, Odroid XU4
* updated repository for Odroid C2/XU4, changed NEXT from 4.9.y to 4.14.y

## v5.58 (2018-08-13)

* rebuilt images for Bananapi, Bananapi Pro, Bananapi+

## v5.57 (2018-08-11)

* added Bionic desktop and Stretch CLI images for RK3399 powered Nanopc T4

## v5.56 (2018-08-10)

* rebuilt images for Pinebook. Added Bionic build

## v5.55 (2018-08-09)

* rebuilt images for Orangepi One+, Orangepi Lite 2 and Pine H64. Enabled USB3, network, THS, DVFS, higher frequencies, HDMI on 4.18.y DEV branch images.

## v5.55 (2018-08-03)

* added Stretch and Bionic mainline kernel images for Odroid C1 (testing),
* rebuilt images for Bananapi M3 (fixed ethernet)

## v5.54 (2018-07-25)

* updated images for Odroid C2, Nanopi M3, Nanopi Fire 3 and NanoPC T3+, Espressobin, Cubox-i/HB and Le potato
* added preview images without end user support for [Bananapi M3](https://www.armbian.com/bananapi-m3/),Cubietruck+ and [Bananapi M2 Berry](https://www.armbian.com/bananapi-m2u/).

## v5.53 (2018-07-23)

* Z28PRO images updated. Fixed wireless and Bluetooth
* FriendlyARM Nanopi K2 S905 images updated. Fixed ethernet problems.
* FriendlyARM Nanopi K1+ images updated. Fixed HDMI out and wireless

## v5.51 (2018-07-04)

* Helios4 Stretch and Bionic images update

## v5.50 (2018-06-28)

* Espressobin images rebuild and repository update, default 4.4.138, next 4.17.3, dev 4.18.RC, hardware crypto support in 4.17.y, zram and zswap
* Odroid C2 bugfix update

## v5.49 (2018-06-28)

* Amlogic Meson64 family (Odroid C2, Lepotato and FriendlyARM K2 S905) were merged into one kernel. Default images comes with kernel 4.14.52, next with 4.17.3 and DEV with 4.18.RC, updated boot scripts, implemented latest kernel bug fixes
* updated kernels, desktop packages and armbian config on the stable repository (apt update & upgrade)

## v5.48 (2018-06-26)

* added nightly images for Odroid C2 with 4.16.y (NEXT) and 4.18.y (DEV) and hopefully fixed ethernet driver

## v5.47 (2018-06-22)

* Odroid C2 images rebuild. Legacy kernel was upgraded to 3.16.57, next to 4.14.51, u-boot to 2018.05
* Added Tritium H5

## v5.46 (2018-06-20)

* Added Olimex Teres nightly builds
* Added FriendlyARM Nanopi K1 plus

## v5.46 (2018-06-06)

* Added Orange Pi Lite 2 and One plus nightly builds

## v5.45 (2018-05-23)

* Orangepi Zero+ images rebuild

## v5.44 (2018-05-10)

* Espressobin images were rebuilt and moved under stable. Kernel 4.14.40, Stretch, Xenial and Bionic. Fixed bootloader, ath10 wireless card support
* added initial Bionic storage to the main apt repository
* Cubox-i / Hummingboard bugfix update to 4.16.y and images rebuild
* Odroid C2 images rebuild

## v5.41 (2018-02-10)

* fixed LED driver on Helios4
* bugfix update on sunxi/sunxi64 kernel. Updated to 4.14.18
* kernel update for MVEBU next (4.14.18 and default 4.4.115) for Clearfog and Helios4. Upstream fixes,AUFS and Realtek 881yAU drivers update

## v5.40 (2018-02-05)

* fixed eMMC support on Odroid C2 NEXT, kernel 4.14.y
* updated PWM driver on Helios4
* kernel update for MVEBU next (Clearfog, Helios4)

## v5.38 (2018-01-29)

* updated all images
* added H3/H5 testing images with kernel 4.14.y
* added Nanopi M3/T3+/Fire testing image
* fixed Bluetooth on Orangepi Win
* main repository update with recent kernel on all NEXT builds

## v5.37 (2018-01-23)

* bugfix release
* armbianmonitor -u fix
* setting cronjob permissions
* replace broken u-boot packages on A20 boards
* updated utilities: hostapd, sunxi-tools, armbian-config
* updated images: Bananapi, PRO, M2, BeelinkX2, Clearfog,Cubieboard2, Cubietruck, Cubox-i/HB, Espressobin, Helios4

## v5.36 (2017-12-03)

* [bugfix release](https://forum.armbian.com/topic/5759-535-bug-questions-collection)

## v5.35 (2017-11-25)

* mainline kernel updated to 4.13.y
* mainline u-boot updated to v2017.09
* added new sunxi Device Tree overlays, fixed and improved old overlays
* Micro-USB [g_serial](https://www.kernel.org/doc/Documentation/usb/gadget_serial.txt) console is enabled by default on most small Allwiner based boards
* Olimex Lime2 and Micro: merging eMMC and normal versions
* Odroid C2: next and dev branches migrated to mainline u-boot
* Odroid XU4: added dev branch, next branch migrated to mainline u-boot
* Clearfog: added dev branch with mainline u-boot
* added supports for [7" RPi display](https://www.raspberrypi.org/products/raspberry-pi-touch-display/) to Tinkerboard with legacy kernel
* All mainline kernels: added Realtek 8811AU/8812AU/8814AU USB wireless driver with monitor mode and frame injection
* All boards: added kernel source packages to the repository (Package names `linux-source-${BRANCH}-${LINUXFAMILY}`, i.e. `linux-source-sunxi-next`)
* Kernel headers are no longer installed by default to new images
* Additional out of tree drivers and USB Redirector are no longer installed by default to new images
* Switching from emergency swap to zram on new Ubuntu Xenial images
* New hardware support (stable/supported images): NanoPi Duo, Orange Pi R1, Pinebook
* New hardware support (experimental): Le Potato, NanoPi NEO 2, Orange Pi Zero Plus, Orange Pi Zero Plus 2 (H5)
* sunxi mainline u-boot: reenabled USB keyboard support and disabled stopping the boot sequence with any key - autoboot now can be aborted with <Ctrl-C>

Desktop images:

* xterm was replaced with full featured xfce terminal,
* added memory profile caching for Chromium,
* added OpenVPN connector,
* shortcuts to armbian-config, support and donate were moved to menu,
* default icon theme was changed to lighter one (Numix),
* fixed login greeter theme,
* changed wallpaper.
* changed [CMA handling](https://github.com/armbian/build/issues/744) on Allwinner legacy kernels

armbian-config:

* was splitted from board support packages to a new package `armbian-config`
* managing board hardware configurations, hotspot, Bluetooth, SSH server
* freezing/unfreezing kernel upgrade
* switching between stable and beta builds,
* switching between alternative kernels,
* installing/uninstalling kernel headers,
* changing timezone, locales, hostname,
* running diagnostic tools,
* enabling/disabling RDP server,
* 3rd party software installer: Samba, OMV, Pi hole, Transmission, ...

Build script:

* added Debian Stretch
* most tweaks moved from inline files to separate files in board support package
* firmware blobs moved to a separate repository
* disabled distcc in extra software compilation process due to toolchain compatibility issues

* [Known problems](https://forum.armbian.com/topic/5759-535-bug-questions-collection/)

* Allwinner A20/sun7i legacy boards. Changed CMA settings prevents playing video. [You need to add cma=96M to kernel command line](https://github.com/armbian/build/issues/744)

## v5.34 (2017-10-18)

* bugfix Odroid XU4/HC1 image rebuild [due to broken USB install on kernel 4.9.x](https://forum.armbian.com/topic/5413-odroid-hc1-sata-install)
* added Le Potato and Orange Pi Zero testing image (mainline kernel)
* Tinkerboard, MiQi and Pinebook images rebuilt

## v5.33 (2017-09-24)

* Odroid XU4/HC1 images were rebuilt.

## v5.33 (2017-09-21)

* Tinkerboard and MiQi images were rebuilt. Rockchip legacy kernel was updated to 4.4.88 and mainline (NEXT) to 4.13.3.

## v5.32 (2017-06-23)

* bugfix release [due to broken crypto functions on kernel 4.11.x](https://forum.armbian.com/topic/4556-partial-bugfix-update/)

## v5.31 (2017-06-15)

* bugfix release [due to network failure](https://forum.armbian.com/topic/4498-no-boot-after-upgrade-to-530/) on some A10 / A20 boards

**End of support notice**

Following boards are no longer receiving support and updates since this version:

* Cubieboard (Allwinner A10) - not enough hardware samples to maintain support
* Lamobo R1 (Allwinner A20) - hardware design flaws, poor software support for the onboard switch
* Olimex Lime A10

## v5.30 (2017-06-14)

* mainline kernel updated to 4.11
* mainline u-boot updated to v2017.05
* Firefox was replaced with Chromium (desktop images)
* sunxi mainline configuration: added Device Tree overlays support (new images only)
* sunxi mainline configuration: added `armbian-add-overlay` helper for compiling and activating DT overlays (new images only)
* log2ram: fixed saving `/var/log` contents on shutdown
* new hardware support (stable/supported images): Xunlong Orange Pi Zero Plus 2 (H3), ASUS TinkerBoard, MiQi
* reworked package updates MOTD script to speed up the login process
* added config file `/etc/default/armbian-motd` for disabling MOTD components
* added `armbian-config` dialog-based configuration program (WIP)
* Banana Pi M2: fixed HDMI video output
* Clearfog: adjusted temperature readout
* i.MX6 mainline: enabled support for HDMI audio and PCIe bus

**End of support notice**

Following boards are no longer receiving support and updates since this version:

* Orange Pi (Allwinner A20) - no hardware samples, out of stock
* Orange Pi Mini (Allwinner A20) - no hardware samples, out of stock
* LeMaker Guitar (Actions S500)
* Roseapple Pi (Actions S500)

## v5.26, v5.27 (2017-02-24)

* security update for most kernels (packages only)
* fixes for hostapd configuration

## v5.25 (2017-02-02)

* armbian-install expanded functionality: you can partition destination and choose file-system type: ext2, ext3, ext4 and BTRFS (BTRFS requires kernel 4.4+)
* added new boards: Clearfog Base, Lime2 eMMC, Lime A33, NanoPi M1+, OrangePi Zero, OrangePi PC2 (mainline only, experimental)
* new default kernel for Clearfog(s), changed kernel family to "mvebu" to avoid conflicts
* disabled wireless power management by default to improve performance with certain drivers
* added wireless drivers to mainline kernels: OrangePi Zero, Neo Air
* implemented initrd loading support for all boards
* moved all images to single ext4 partition scheme
* changed default wallpaper, startup icon, shadows to windows on desktop builds
* Firefox web cache moved to memory
* added g_serial driver to boards without a network connector, working on both kernel (Opi Zero,Opi Lite,FA Neo Air)
* added "Software boutique" application installer on desktop builds (currently not working properly on arm64)
* added per board patching option
* added u-boot video driver and boot logo to H3 based boards
* added simplefb video driver (HDMI only) to mainline H3 kernel
* updated MALI driver on H3 platform, fixed problems on 2GB boards
* changed Ethernet switch driver on Lamobo R1 to DSA based one (mainline kernel)
* fixed soft cursor (CLI) for H3 legacy and Odroid C2
* expand and adjust multiple kernel configurations based on user requests
* adjusted sunxi boot script to support booting in SPI flash + USB storage scenario (w/o the SD card)
* dropped support for Debian Wheezy and Ubuntu Trusty releases
* sunxi mainline kernel was updated to 4.9.x, some dev kernels to 4.10
* added log2ram (Ramlog alternative) to default installation
* changed first run logic, disabled forced automatic reboot
* changed new user account creation logic, disabled forced reboot on user creation failure

## v5.24

* this version is not released, it was used for the nightly or user-built images

## v5.23 (2016-10-23)

* fixed bug in armbian-install
* fixed u-boot update bug on Allwinner platform

Known problems:

* Lamobo R1 fails to boot upon upgrade

## v5.22 (2016-10-22)

* fixed eMMC install on Odroid C2
* firmware package was splitted into minimal (default) and full versions
* patched [Dirty COW exploit](https://thehackernews.com/2016/10/linux-kernel-exploit.html) on all kernels
* added Odroid XU4 mainline kernel image
* added Olimex A33 mainline kernel image
* added Overlay FS for Cubox, Udoo and Udoo Neo
* booting problems fixed on more boards
* updated wireless driver on M2+ (dhd)
* updated driver for OV5640 on sun8i default kernel
* sunxi-next kernel version updated to 4.8.4
* BananaPi M1+ now uses upstream DTB file `sun7i-a20-bananapi-m1-plus.dtb`, boot script adjusting may be required for existing images

Desktop images:

* prebuilt mpv and FFmpeg were removed in favor of providing only configuration files
* fixed an issue with video brightness on A10/A20 based boards

Build script:

* DEBUG_MODE was renamed to CREATE_PATCHES
* GLshim was moved to a private directory, it can be activated for selected applications by changing `LD_LIBRARY_PATH`

Known problems:

* eMMC install fails (will be fixed in bugfix update)
* H3 development kernel (4.8.4) update fails to boot
* C2 upgrade hangs on compiling headers (Jessie)

## v5.20 (2016-09-16)

* added FriendlyARM Neo legacy and mainline images (experimental)
* added Orange Pi PC+ mainline kernel (experimental)
* added Pine64 / Pine64+ images with legacy kernel
* added UUID support for NAND/SATA/USB installer
* added desktop images for Cubox(s) / Hummingboard(s) with mainline kernel
* enabled MIDI sequencer and snd-rawmidi-seq in H3 legacy kernel
* added H3 consumption tool to control board consumtion level on legacy kernel
* fixed and enabled Bluetooth on Cubietruck and Cubox(s) / Hummigboard(s) desktop, both kernels
* masked p2p0 wifi direct device on Bluetooth legacy kernel
* Odroid C1/C2 upgrade fail fixed
* wireless enabled by default on Banana Pi PRO
* added new screen resolutions to H3 boards with legacy kernel
* DeviceTree Overlay ConfigFS interface for H3 mainline kernel
* update of mainline u-boot to 2016.09 should fix boot failures on H3 boards with eMMC
* disabled USB keyboard support in mainline u-boot should fix boot failures with connected USB devices

Desktop images:

* WICD was replaced with NetworkManager
* ALSA was replaced with PulseAudio
* sunxi boards: [GLshim](https://github.com/ptitSeb/gl4es) was added to desktop images with Mali support (except for Orange Pi Plus and Orange Pi Plus 2e)
* sunxi boards: prebuilt mpv now supports OSD and subtitles, activated by setting environment variable `VDPAU_OSD=1`

Build script:

* complete desktop building rework - now packages are built from sources
* added Lime 2 eMMC as build target (WIP)
* added Pine64 / Pine64+ mainline (dev) target (experimental)
* added FriendlyArm Neo as build target
* fixed MT7601 wifi driver building
* github download rework
* external toolchain rework

Added additional packages, not installed by default:

* hostapd-realtek: replacement for hostapd with support for several Realtek Wi-Fi adapters
* fswebcam-gc2035: replacement for fswebcam with support for GC2035 camera driver for H3 based boards
* guvcview: replacement for stock guvcview with support for H3-based Orange Pi CMOS cameras

Known problems:

* Mali OpenGL ES does not work on H3 boards with 2GB RAM (Orange Pi Plus 2, Orange Pi Plus 2e)
* Hardware video decoding on A10/A20 based boards produces dark video
* Some applications that depend on livav libraries (i.e. minidlna) may not work on Jessie images

## v5.17 (2016-07-07)

* bugfix release on some boards.

## v5.16 (2016-07-05)

* bugfix release. In 5.15 we accidentaly overwrote default network settings. Check /etc/network/interfaces if you use advanced network settings or fixed ip.
* small changes.

## v5.15 (2016-07-01)

* Added [improved camera driver](https://github.com/avafinger/gc2035) for Xunlong's cheap 2MP GC2035 camera
* Improved throttling/DRAM settings for the new 3 overheating H3 devices (BPi M2+, NanoPi M1, Beelink X2)
* Added official support for Beelink X2, NanoPi M1, Banana Pi M2+
* Improved console output (serial + display)
* Finally got rid of (broken) board auto detection. We do not ship any more one image for several devices that tries to detect/fix things on 1st boot but provide one dedicated image per board (Plus and Plus 2 and both NanoPi M1 variants being handled as the same device since only size of DRAM/eMMC differs)
* Tried to improve user experience with better/unified led handling (light directly after boot, communicate booting states through blinking)
* Improve partitioning and filesystem resize on 1st boot making it easier to clone every installation media afterwards
* fully support installation on eMMC on all H3 devices (`u-boot` and `armbian-install.sh` fixes)
* Improved performance/thermal/throttling behaviour on all H3 boards (especially newer Oranges)
* Prevent HDMI screen artefacts (disabling interfering TV Out by default)
* Enhanced 8189ETV driver for older Oranges
* Added support for OPi Lite, PC Plus and Plus 2E including new 8189FTV Wi-Fi (client, AP and monitoring mode, added fix for random MAC address)
* Added in-kernel corekeeper patch (bringing back killed CPU cores after heavy overheating situations when thermal situation is ok again)
* Added TV Out patch for Orange Pi PC
* Further improve driver compilation due to improved kernel headers scripts compilation
* Initrd support
* increased kernel version to 3.4.112
* Exchanged whole kernel source tree to [newer BSP variant](https://github.com/friendlyarm/h3_lichee), cleaned up sources, rebased all +100 patches (fixed display issues and kswapd bug, new and more performant GPU driver, increase Mali400MP2 clock to 600MHz)
* Added RTL2832U drivers to kernel (DVB-T)
* Fixed Docker on Odroid XU4
* Added overlay fs to Clearfog and Odroid XU4
* Many minor fixes

## v5.14 (2016-06-14)

* all images rebuilt, most of them were manually tested
* added Beelink X2 image
* Cubox / Hummingboard kernel upgrade to 3.14.72 and 4.6.2
* Trusty was replaced with Xenial

## v5.12 (2016-05-31)

* updated C1 images
* added wifi driver for new Oranges (modprobe 8189fs)
* added Orange Pi Lite, PC Plus and Plus 2E images

## v5.11 (2016-05-24)

* Various bug fixes
* new working images for Actions Semi S500 boards

## v5.10 (2016-05-01)

Images:

* all 3.10+ kernels [are Docker ready](https://forum.armbian.com/topic/490-docker-on-armbian/)
* all A10/A20/H3 comes with HW accelerated video playback in desktop build
* [fixed root exploit on H3 boards](https://github.com/armbian/build/issues/282)
* [fixed kswapd 100% bug on H3 boards](https://github.com/armbian/build/issues/219)
* fixed SPDIF / I2S audio driver in legacy kernel
* fixed Udoo Neo wireless
* fixed slow SD cards boot
* fixed Allwinner SS driver
* fixed bluetooth on Cubietruck, both kernels
* fixed wireless driver on H3 boards
* [fixed R1 switch driver](https://github.com/armbian/build/commit/94194dc06529529015bfd04767865bbd04d29d9b)
* kernel for Allwinner boards was upgraded to 3.4.112 & 4.5.2
* kernel for iMx6 boards was upgraded to 3.14.67 & 4.5.2
* kernel for Armada (Clearfog) was upgraded to 3.10.101 & 4.5.2
* kernel for Udoo boards was updated to 3.14.67 & 4.4.8
* kernel for Guitar (Lemaker) was upgraded to 3.10.101
* kernel for H3/sun8i legacy come from new Allwinner updated source (friendlyarm)
* [added support for Olimex Lime2 eMMC](https://github.com/armbian/build/issues/258)
* [increased MALI clockspeed on sun8i/legacy](https://github.com/armbian/build/issues/265)
* added [Armbianmonitor](https://forum.armbian.com/topic/881-prepare-v51-v201604/?tab=comments#comment-7095)
* added Odroid C1, C2(arm64), Nanopi M1, Banana M2+, Pcduino 2 and Pcduino 3. CLI and desktop
* added wifi radar to desktop
* added preview mainline kernel images for H3 boards (4.6.RC1)
* added initrd creation on all Allwinner images
* added Hummigboard 2 with working PCI and onboard wireless with legacy kernel 3.14.65
* added eMMC installer for H3
* added support for IFB and net scheduling for sun7i-legacy
* added ax88179_178a USB 3.0 Ethernet driver for sun7i-legacy
* hostapd comes as separate package (armbian-hostapd)
* changed first boot procedure and force user creation
* verbose / no verbose boot works almost on all boards
* enabled I2S on sun8i
* removed Debian Wheezy from auto build
* installing headers autocompile scripts
* all images come compressed with 7zip

Build script:

* GCC 5 support for mainline and allwinner legacy
* RAW images are not compressed by default
* added arm64 building support
* added docker as host
* Added Belink X2 (H3 based media player), and Roseapple (S500) as WIP target
* introducted CLI_TARGET per board
* prepared Xenial target
* fixed USB redirector building on all kernels
* support for Xenial as a build host is 95% ready.
* implemented automatic toolchain selection
* come cleanup, configurations are subfoldered
* extended_deboostrap becomes default

Known bugs:

* Udoo Neo reboots takes a while, 1min+
* headers within sun8i needs some fixing
* H3 board autodetection fail under certain conditions

## v5.06 (2016-03-18)

* increase kernel version to 3.4.111
* headers auto creation while install (eases kernel/driver compilation)
* improved SD card partitioning to help old/slow cards with wear leveling and garbage collection
* Possible to use _Ubuntu Xenial Xerus_ as target
* changed behaviour of board leds (green == power, red == warning)
* speed improvements for 1st automated reboot
* Integrates OverlayFS backport

## v5.05 (2016-03-08)

* Auto detection for the Orange Pi 2 does work now
* Mali acceleration works for all users not only root
* verbose boot logging on 1st boot and after crashes (you can toggle verbose logging using `sudo armbianmonitor -b`)
* more WiFi dongles supported due to backported firmware loader patch
* all 3 USB ports on Orange Pi One (Lite) available ([2 of them need soldering](https://forum.armbian.com/topic/755-tutorial-orange-pi-one-adding-usb-analog-audio-out-tv-out-mic-and-ir-receiver/))
* I2S possible on all Orange Pis (compare with the [mini tutorial](https://forum.armbian.com/topic/759-tutorial-i2s-on-orange-pi-h3/) since you need to tweak script.bin)
* default display resolution set to 720p60 to fix possible overscan issues on 1st boot
* HW accelerated video decoding works for most formats
* Booting from eMMC on OPi Plus now possible
* Udoo quad images upgraded to 4.4.4

## v5.04 (2016-03-01)

* HDMI/DVI works (bug in boot.cmd settings)
* Reboot issues fixed (bug in fex settings)
* 1-Wire useable (we chose to stay compatible to loboris' images so the data pin is 37 by default. You're able to change this in the [fex file](https://github.com/armbian/build/blob/6d995e31583e5361c758b401ea44634d406ac3da/config/orangepiplus.fex#L1284-L1286))
* changing display resolution and choosing between HDMI and DVI is now possible with the included _h3disp_ tool (should also work in the [stand-alone version](https://forum.armbian.com/topic/617-wip-orange-pi-one-support-for-the-upcoming-orange-pi-one/page/6/?tab=comments#comment-5480) with Debian based OS images from loboris/Xunlong). Use `sudo h3disp` in a terminal to get the idea.
* Ethernet issues fixed (combination of kernel and fex fixes)
* USB-to-SATA bridge on the Orange Pi Plus works
* stability problems on Orange Pi One fixed (due to undervoltage based on wrong fex settings)
* problems with 2 USB ports on the PC fixed (wrong kernel config)
* Mali400MP acceleration (EGL/GLES) works now
* suspend to RAM and resume by power button works now (consumption less than 0.4W without peripherals)
* Enforce user account creation before starting the GUI
* USB and Ethernet IRQs distributed nicely accross CPU cores
* Full HDMI colour-range adjustable/accessible through _h3disp_ utility
* already useable as stable headless/server board
* rebuilt Cubieboard 1 & 2 with 3.4.110 and 4.4.3
* fixed Bluetooth on Cubietruck + rebuild with 3.4.110 and 4.4.3
* all new images has no login policy: forced user generation

## v5.03 (2016-02-20)

* H3 images rebuilt

## v5.02 (2016-02-18)

* H3 images rebuilt

## v5.01 (2016-02-17)

* Bugfix update for [Allwinner boards](https://forum.armbian.com/topic/691-banana-pro-testers-wanted-sata-drive-not-working-on-some-boards/)
* Update [for H3 based boards](https://github.com/armbian/build/commit/c93d7dfb3538c36739fb8841bd314d75e7d7cbe5)

## v5.00 (2016-02-12)

* mainline kernel for Allwinner based boards upgraded to 4.4.1
* Allwinner audio driver playback and capture on kernel 4.4.1, [UAS](https://linux-sunxi.org/USB/UAS), USB OTG, battery readings,
* added Marvel Armada kernel 3.10.96, 4.4.1 and patches for changing mPCI to SATA
* added Cubox / Hummingboard kernel 4.4.1 (serial console only)
* firstrun does autoreboot only if needed: wheezy and some legacy kernels.
* [added motd](https://forum.armbian.com/topic/602-new-motd-for-ubuntudebian/?tab=comments#comment-4223) to /etc/updated.motd ... redesign, added battery info for Allwinner boards, bugfix, coloring
* fixed temperature reading on Cubox / Hummingboard legacy kernel
* fixed FB turbo building on Allwinner
* fixed NAND install on A10 boards (Legacy kernel only)
* fixed USB boot, added PWM on mainline
* fixed Banana PRO/+ onboard wireless on mainline kernel - running with normal Banana DT.
* readded USB sound
* added [A13 Olimex SOM](https://www.olimex.com/Products/SOM/A13/A13-SOM-512/)
* added [LIRC GPIO receive and send driver](https://github.com/armbian/build/issues/135) for legacy Allwinner
* added LED MMC activity to mainline kernels for Cubietruck and Cubieboard A10
* build script: option to build images with F2FS root filesystem for Allwinner boards
* build script: added alternative kernel for Lemaker Guitar (NEXT), Cubox (DEV)

## v4.81 (2015-12-28)

* complete build script rework
* new development kernel package linux-image-dev-sunxi (4.4RC6) for Allwinner boards
* added Lemaker Guitar, kernel 3.10.55
* added Odroid XU3/4, kernel 3.10.94 and mainline 4.2.8
* mainline kernel for Allwinner based boards upgraded to 4.3.3
* Udoo mainline upgraded to 4.2.8, legacy to 3.14.58
* cubox / hummingboard upgraded to 3.14.58, added mainline kernel 4.4
* fixed Jessie RTC bug, systemd default on Jessie images

## v4.70 (2015-11-30)

* Bugfix update(apt-get update && apt-get upgrade)
* small changes and fixes

## v4.6 (2015-11-24)

* Update only (apt-get update && apt-get upgrade)
* mainline kernel for Allwinner based boards upgraded to 4.2.6
* Legacy kernel for Allwinner based boards upgraded to 3.4.110
* added new board: Udoo Neo
* added USB printer, CAN, CMA, ZSWAP, USB video class, CDROM fs, sensor classs, … to Allwinner mainline kernel
* armbian-install scripts rewrite. Now it’s possible to install to any partition.
* fixed nand install for Allwinner A10 based boards: Cubieboard 1 / Lime A10
* universal upgrade script bugfix / rewrite.
* 8 channel HDMI support for legacy Allwinner kernel
* unattended upgrade fixed
* sunxi tools fixed
* added two new options to build script: keep kernel config and use_ccache
* added kernel version to motd

## v4.5 (2015-10-14)

* mainline kernel upgraded to 4.2.3 for Allwinner based boards
* legacy kernel for Allwinner compiled from new sources (linux-sunxi)
* udoo mainline upgraded to 4.2.3
* cubox / hummingboard upgraded to 3.14.54
* changed kernel naming: A10 = linux-image-sun4i, A20 = linux-image-sun7i
* new boards: Banana M2, Orange+(A31S), Cubieboard 1, Cubieboard 2 Dual SD, Lime A10
* fixed Udoo legacy wireless problems
* fixed Jessie boot problems by disabling systemd. It’s possible to re-enable within boot scripts
* added ramlog to Jessie because we don’t have systemd anymore
* changed wireless driver for Cubietruck and Banana PRO (now it’s ap6210)
* added ZRAM to mainline kernel
* fixed dvbsky modules

and a bunch of small fixes.

## v4.4 (2015-10-01)

Images:

* mainline kernel upgrade to 4.2.2 (Allwinner, Udoo Quad),
* legacy kernel upgraded to 3.4.109 (Allwinner),
* added I2C support and bunch of multimedia modules (DVB) (mainline Allwinner),
* Udoo quad images with fixed legacy kernel 3.14.28,
* Cubox and Hummingboard kernel upgrade to 3.14.53,
* brcmfmac driver fixes for mainline kernel (Banana PRO / Cubietruck)
* performance tweak: choosing a closest Debian mirror (Debian images)
* added Astrometa DVB firmware and dvb-tools
* added Nikkov SPDIF / I2S recent patch (legacy Allwinner)
* added patch for rtl8192cu: Add missing case in rtl92cu_get_hw_reg (Lamobo R1)
* bigger NAND boot partition on install
* install script bug fixes

Script:

* force apt-get update on older rootfs cache,
* image harden manipulation security,
* packages NAND/FAT/same version install faling fixed,
* image shrinking function rework,
* better packages installation install checking,
* added Debian keys to suppress warnings in debootstrap process,
* added fancy progress bars,
* added whiptail downloading prior to usage (bugfix).

## v4.3 (2015-09-17)

* kernel 4.2 for Allwinner based boards
* kernel 4.2 for Udoo Quad
* walk-around if ethernet is not detected on some boards due to RTC not set(?)
* update is done (semi) automatic if you are using Armbian 4.2. You only need to issue command: apt-get update && apt-get upgrade. If you are coming from older system, check Documentation
* U-boot on R1 is now updated to latest stable version (2015.07)
* Fixed AW SOM. Working with latest u-boot but you need to build image by yourself.
* Enabled whole USB net and HID section in kernel for Allwinner boards v4.2
* Fixed upgrade script – only some minor bugs remains.
* Fixes to build script that it’s working under Ubuntu 15.04
* Adding Bananapi Wireless driver (ap6210) back to legacy kernel
* Udoo official kernel (3.14.28) not updated due too many troubles.

## v4.2 (2015-09-01)

Images:

* Upgraded NAND / SATA installer. Possible to install to SATA/NAND boot in one step.
* Easy kernel switching between old 3.4 and 4.x
* Automatic kernel updating (to disable comment armbian repo /etc/apt/sources.list)
* Allwinner boards share one 4.x kernel and two 3.4
* All boards share the same revision number
* One minimal Ubuntu Desktop per board (Wicd, Firefox, Word)
* u-boot v2015.07 for most boards
* Aufs file system support
* kernel 4.1.6 and 3.4.108
* Added Orangepi Mini, Cubieboard 1 (4.x only), Udoo with official kernel
* Repository for Wheezy, Jessie and Trusty
* enabled USB audio in kernel 4.x
* kernel headers fixed. No need to rebuild when you update the kernel.
* fixed boot scripts that can load from FAT partition too
* removed Cubox binnary repository because of troubles
* Docker support (kernel 4.x). Already here for a while / forget to mention.
* nodm change default login

Build script:

* changed structure: sources now in folder sources, output is what we produce, deb in one folder
* expanded desktop part
* possible to build all images at once, create package repository
* SD card initial size is 4Gb, variable transfered into configuration.sh
* Avaliable board list is now created from file configuration.sh
* Fixed image shrinking problem
* Patching part rework
* Using first FAT boot partition now fixes boot scripts
* Uboot TAG moved to configuration.sh and differs for some boards
* new variables for source branches. Only too remove errors when checking out

## v4.1 (2015-08-05)

* Added desktop image
* U-Boot 2015.07 with many new features
* Added auto system update via repository apt.armbian.com
* Root password change is initialized at first boot.
* 3.4.108 kernel fixes, 4.1.4 Allwinner Security System

## v4.0 (2015-07-12)

* Fixed stability issues, temperature display in 4.x
* Kernel upgrades to 3.4.108 and 4.1.2

## v3.9 (2015-06-11)

* Bugfix release
* Kernel 4.0.5 traffic control support
* SATA / USB install fixed on kernel 4.x
* Added 256Mb emergency swap area, created automatically @first boot

## v3.8 (2015-05-21)

* Bugfix release: Cubietruck images successfully booted on Cubietruck. I waited for automatic reboot than tested remote login.
* Kernel 4.0.4 added support for power on/off button
* Both: Jessie fixed, Ethernet init fixed (uboot)
* armbian.com introduction

## v3.7 (2015-05-14)

* Kernel 4.0.3 some new functionality
* Kernel 3.4.107 added sunxi display manager to change FB on demand
* Both: Ubuntu and jessie install errors fixed, removed busybox-syslogd and changed to default logger due to problems in Jessie and Ubuntu, apt-get upgrade fixed, documentations update, Uboot fixed to 2015.4 – no more from dev branch
* Build script rework - image size shrink to actual size, possible to have fat boot partition on SD card, several script bug fixes

## v3.6 (2015-04-29)

* Kernel 3.19.6
* Kernel 3.4.107 with better BT loading solution

## v3.5 (2015-04-18)

* Kernel 3.19.4: fixed AP mode, fixed USB, added 8192CU module
* Common: apt-get upgrade ready but not enabled yet, serial console fixed, fixed hostapd under jessie, easy kernel switching, latest patched hostapd for best performance – normal and for realtek adaptors, auto IO scheduler script
* Build script: everything packed as DEB

## v3.4 (2015-03-28)

* Kernel 3.19.3: docker support, apple hid, pmp, nfsd, sata peformance fix
* Kernel 3.4.106: pmp, a20_tp - soc temp sensor
* Common: console setup fixed, headers bugfix, nand install fix
* Build script: kernel build only, custom packets install, hardware accelerated desktop build as option

## v3.3 (2015-02-28)

* Kernel 3.19.0: many new functionality and fixes.
* Bugfixes: CT wireless works in all kernels

## v3.2 (2015-01-24)

* Possible to compile external modules on both kernels
* Kernel 3.19.0 RC5
* Bugfixes: install script, headers, bashrc, spi

## v3.1 (2015-01-16)

* Kernel 3.19.0 RC4
* Added Cubieboard 1 images
* Dualboot for CB2 and CT dropped due to u-boot change. Now separate images.
* New user friendly SATA + USB installer, also on mainline

## v3.0 (2014-12-29)

* Kernel 3.18.1 for mainline image
* Added Ubuntu Trusty (14.04 LTS) image
* Bugfixes: auto packages update

## v2.9 (2014-12-03)

* Kernel 3.4.105 with new MALI driver and other fixes
* Added: Jessie image
* Major build script rewrite - much faster image building
* Fixed: failed MIN/MAX settings

## v2.8 (2014-10-17)

* Added: ondemand governor, fhandle, squashfs and btrfs
* Removed: bootsplash, lvm, version numbering in issue
* Fixed: custom scripts, Jessie upgrade
* Disabled: BT firmware loading, enable back with: insserv brcm40183-patch
* Added working driver for RT 8188C, 8192C

## v2.7 (2014-10-01)

* Kernel 3.4.104
* Automatic Debian system updates
* VGA output is now default but if HDMI is attached at first boot than it switch to HDMI for good. After first restart!
* Fixed NAND install script. /boot is mounted by default. Kernel upgrade is now the same as on SD systems.
* Cubieboard2 - disabled Cubietruck dedicated scripts (BT firmware, LED disable)
* Added network bonding and configuration for "notebook" mode (/etc/network/interfaces.bonding)
* IR receiver is preconfigured with default driver and LG remote (/etc/lirc/lircd.conf), advanced driver is present but disabled
* Added SPI and LVM functionality
* Added Debian logo boot splash image
* Added build essentials package

## v2.6 (2014-08-22)

* Kernel 3.4.103 and 3.17.0-RC1
* Added GPIO patch (only for 3.4.103)

## v2.5 (2014-08-02)

* Kernel 3.4.101 and 3.16.0-RC4
* major build script rewrite

## v2.4 (2014-07-11)

* Kernel 3.4.98
* default root password (1234) expires at first login
* build script rewrite, now 100% non-interactive process, time zone as config option
* bug fixes: removed non-existing links in /lib/modules

## v2.3 (2014-07-02)

* Kernel 3.4.96
* cpuinfo serial number added
* bug fixes: stability issues - downclocked to factory defaults, root SSH login enabled in Jessie, dedicated core for eth0 fix
* disp_vsync kernel patch

## v2.2 (2014-06-26)

* Kernel 3.4.94
* Added Jessie distro image
* Updated hostapd, bashrc, build script
* bug fixes: disabled upgrade and best mirror search @firstboot, bluetooth enabler fix
* MD5 hash image protection

## v2.1 (2014-06-13)

* Kernel 3.4.93
* Onboard Bluetooth finally works
* Small performance fix
* Allwinner Security System cryptographic accelerator

## v2.0 (2014-06-02)

* Kernel 3.4.91 with many fixes
* Cubieboard 2 stability issues fix
* eth0 interrupts are using dedicated core
* Global bashrc /etc/bash.bashrc
* Verbose output and package upgrade @ first run

## v1.9 (2014-04-27)

* Kernel headers included
* Clustering support
* Advanced IR driver with RAW RX and TX
* Bluetooth ready (working only with supported USB devices)
* Bugfixes: VLAN, login script, build script
* New packages: lirc, bluetooth

## v1.8 (2014-03-27)

* Kernel 3.4.79
* Alsa I2S patch + basic ALSA utils
* Performance tweaks: CPU O.C. to 1.2Ghz, IO scheduler NOOP for SD, CFQ for sda, journal data writeback enabled
* Avaliable memory = 2000MB
* Minimized console output at boot
* MAC address from chip ID, manual optional
* Latest (Access point) hostapd, 2.1 final release
* Login script shows current CPU temp, hard drive temp & actual free memory
* Fastest Debian mirror auto selection @first boot
* New packages: alsa-utils netselect-apt sysfsutils hddtemp bc

## v1.7 (2014-02-26)

* Flash media performance tweaks, reduced writings, tmp & logging to RAM with ramlog app – sync logs on shutdown
* SATA install script
* Dynamic MOTD: Cubieboard / Cubietruck
* Disabled Debian logo at startup
* New packages: figlet toilet screen hdparm libfuse2 ntfs-3g bash-completion

## v1.6 (2014-02-09)

* Added support for Cubieboard 2
* Build script creates separate images for VGA and HDMI
* NAND install script added support for Cubieboard 2

## v1.52 (2014-02-07)

* Various kernel tweaks, more modules enabled
* Root filesystem can be moved to USB drive
* Bugfixes: NAND install script

## v1.5 (2014-01-22)

* Hotspot Wifi Access Point / Hostapd 2.1
* Bugfixes: MAC creation script, SSH keys creation, removed double packages, …
* Graphics desktop environment upgrade ready

## v1.4 (2014-01-12)

* Patwood’s kernel 3.4.75+ with many features
* Optimized CPU frequency scaling 480-1010Mhz with interactive governor
* NAND install script included
* Cubietruck MOTD
* USB redirector – for sharing USB over TCP/IP

## v1.3 (2014-01-03)

* CPU frequency scaling 30-1000Mhz
* Patch for gpio

## v1.23 (2014-01-01)

* added HDMI version
* added sunxi-tools
* build.sh transfered to Github repository
* disabled LED blinking

## v1.2 (2013-12-26)

* changed kernel and hardware config repository
* kernel 3.4.61+
* wi-fi working
* updated manual how-to

## v1.0 (2013-12-24)

* total memory available is 2G (disabled memory for GPU by default)
* gigabit ethernet is fully operational
* sata driver enabled
* root filesystem autoresize
* MAC address fixed at first boot
* Kernel 3.4.75
* root password=1234
* Bugs: wifi and BT not working
