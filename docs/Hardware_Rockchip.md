# Rockchip RK3399/RK3328 boards

## Graphics 3D hardware acceleration
In mainline kernel, panfrost kernel driver paired with Mesa 22.0 (or more recent) provides excellent results, capable of 3D rendering and 2D composited user interfaces.
Also Gnome and KDE compositors are perfectly usable out of the box.

There can be other issues like "unusual" screen resolutions like 1920x1200 are neither properly detected nor supported while classic *FullHD* 1920x1080 should be fine.

## USB-C
The connector is supported and is capable of switching between USB and DP modes (tested on Orange Pi 4 LTS board).

## Overclock overlay
The RK3399 can be overclocked at own risk. Use `rockchip-rk3399-opp-2ghz.dtbo` this.

# Rockchip RK322x/RK3288 boards

## Graphics 3D hardware acceleration
In mainline kernel, panfrost (RK3288) or lima (RK322x) kernel drivers, paired with Mesa 22.0 (or more recent), provides excellent results, capable of 3D rendering and 2D composited user interfaces.
Also Gnome and KDE compositors are perfectly usable out of the box.

Usually a wide range of resolutions is supported with these SoCs, due to custom HDMI timings imported in the kernel drivers through external patches from LibreELEC project. Resolution support has been reported to work up to 4k resolutions, but some unusual and uncommon setup may still have unexpected issues.

# Video Decoders for RK322x/RK3288/RK3328/RK3399 - updated March 2024

Video decoding is fully supported for these SoCs via kernel V4L2 stateless drivers like Hantro and rkvdec, though it requires userland support to be actually exploited.
Userland support is provided by gstreamer or FFmpeg frameworks, but their support varies among distributions because some bits are still missing.
For that reason, an experimental Debian/Ubuntu repository for Armbian is available at [https://forum.armbian.com/topic/32449-repository-for-v4l2request-hardware-video-decoding-rockchip-allwinner/](https://forum.armbian.com/topic/32449-repository-for-v4l2request-hardware-video-decoding-rockchip-allwinner/) to provide FFmpeg and MPV packages already compiled with the proper support for V4L2 stateless decoders.

Hardware available and Supported video decoders are:
* h.264
* h.265
* VP8
* VP9

Despite support level is getting better, at the moment of writing this documentation some bits are still moving for h.265 and VP9 and not finalized yet, though they should be usable and provide a good experience.

Also DRMPRIME support in the kernel is quite established right now and it is possible to have both full-screen and windowed hardware decoding.

Note: if you are asking about browsers, we are not there yet. Hardware video decoding and composition with existing graphics is a quite complex matter and all the actors in the pipeline should agree on the same protocols.

# Video Decoders for RK35xx series - updated March 2024

Support in the mainline kernel is not yet ready or have not been tested yet. 
These products have both rkvdec and Hantro IP (RK356x and RK3588 have Hantro G1) but there are no reports of their actual support or readiness.

# Video Encoders

All the SoCs above have Hantro IP which is capable of both decoding and encoding, but yet encoding support has not been tested and thus it is not known what is its state.
