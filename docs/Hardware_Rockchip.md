# Rockchip RK3399 boards

## Graphics hardware acceleration (3D and VideoEngine)
Both only work with legacy (4.4.y) kernel using Buster userspace.  
Check [https://forum.armbian.com/topic/16516-rk3399-legacy-multimedia-framework/](https://forum.armbian.com/topic/16516-rk3399-legacy-multimedia-framework/)

3D acceleration in mainline is still in the works and is covered by Panfrost. There are still other issues like "unusual" screen resolutions like 1920x1200 are neither properly detected nor supported while classic *FullHD* 1920x1080 is fine.

## USB-C
Partially works in legacy (4.4.y). Does not work with mainline due to lack of drivers.


## Overclock overlay
The RK3399 can be overclocked at own risk. Use `rockchip-rk3399-opp-2ghz.dtbo` this.

# Rockchip RK3328 / RK 3288

A similar multimedia framework is available if using legacy 4.4.y kernel on Buster userspace.  
Check [https://forum.armbian.com/topic/16517-rk3288rk3328-legacy-multimedia-framework/](https://forum.armbian.com/topic/16517-rk3288rk3328-legacy-multimedia-framework/)
