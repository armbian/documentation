# Changelog

* Note: If a new sub-version is released this does not necessarily mean all boards receive a new version number since most of the time these fixes are targeting a specific board or board family only.

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
* vagrant-disksize is beeing determined automatically
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
* prepared FEL boot
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
