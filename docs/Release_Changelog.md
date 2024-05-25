## v25.5.1 (2025-25-5)

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
