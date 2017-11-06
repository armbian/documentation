# Allwinner H3 boards

**Overview**

The H3 SoC from Allwinner is meant for OTT boxes and is therefore its reference design is _not_ accompanied by a separate PMIC (power management IC) unlike A series Allwinner SoCs (A10, A20, A64, ...). No PMIC means also that there's no battery charging/monitoring implemented so H3 is not that much suited for mobile devices. On the other hand some pretty cheap H3 boards were released that can be driven with rather low consumption and therefore combining H3 devices with a battery became a real use case with boards like [Orange Pi One/Lite](http://linux-sunxi.org/Orange_Pi_Lite), NanoPi [NEO and Neo AIR](http://linux-sunxi.org/FriendlyARM_NanoPi_NEO).

As usual [SoC](http://linux-sunxi.org/H3) and [device information](http://linux-sunxi.org/Category:H3_Devices) can be found in linux-sunxi wiki. Same applies to status of [mainlining kernel efforts](http://linux-sunxi.org/Linux_mainlining_effort). Adding to the usual SoC feature set (I2C, SPI, PWM, UART, SDIO, GPIO and so on) H3 has one USB OTG port, 3 real USB host ports (not exposed on all devices), Fast and Gigabit Ethernet capablities (board specific), a Mali400MP2 GPU and Allwinner's video encoding/decoding engine.

When CPU or GPU cores are fully utilized H3 tends to overheat over time like any other popular ARM SoC released within the last 2-3 years. With Armbian we provide sane dvfs (dynamic voltage frequency scaling) settings that help a lot with throttling. In case you plan to operate your H3 device constantly under high load please check Armbian forums first since boards behave differently (related to voltage regulation and PCB size and design -- some use copper layers to spread the heat away from the SoC). Also consider applying a heatsink to the SoC (a fan should not be necessary unless you want to do number crunching on your board and then you obviously chose the wrong device).

You find some [differentiation criteria regarding supported H3 devices as well as an overview/history of H3 software support in our forums](http://forum.armbian.com/index.php/topic/1351-h3-board-buyers-guide/) or use Jean-Luc's [nice comparison table](http://www.cnx-software.com/2016/06/08/allwinner-h3-boards-comparison-tables-with-orange-pi-banana-pi-m2-nanopi-p1-and-h3-olinuxino-nano-boards/#comments) (both slightly outdated since more H3 devices have been released in the meantime).

**Kernel support**

Due to H3's overheating tendencies a working throttling implementation is important when more heavy workloads should run on the board. This is implemented in legacy kernel (settings have been improved a lot by linux-sunxi community and us compared to Allwinner's defaults), but in mainline kernel it is still Work-in-Progress which is one of the reasons that prevent us from releasing Armbian images with mainline kernel. So while you currently only get legacy images in download area you can already try to build your own images with kernel 4.x using our build system and choosing _next_ branch or use prebuilt nightly images for some boards.

Armbian legacy images for H3 devices are based on Allwinner's 3.4.39 BSP/Android kernel with +100 patches on top to fix countless security issues and to add features (we're using 3.4.113 at the time of this writing). This kernel supports nearly all SoC features and thanks to the awesome linux-sunxi community we provide also HW accelerated video decoding with desktop images (please use the included mpv player for this).

Please don't expect most of these features to be available when we provide mainline kernel images, those are more suited for headless/server operation and will shine in areas like networking or IO performance. Please have a look at what to expect again in [linux-sunxi wiki](http://linux-sunxi.org/Sunxi_devices_as_NAS#New_opportunities_with_mainline_kernel).

**Default settings**

- CPU frequency settings are 240-912 MHz on NanoPi NEO, 240-1200 MHz on BPi M2+, NanoPi M1 and Beelink X2, 480-1200 MHz on OPi One/Lite and 480-1296 MHz on the other boards (cpufreq governor is _interactive_ therefore the boards only increase CPU speed and consumption when needed). The differences are due to different voltage regulators and heat dissipation behaviour.
- Armbian unlike older/other H3 OS images uses the green led as 'power on' indicator (blinking means 'ready to login' or 'shutting down'), the red led (blue on NanoPis) can be used for your own purpose.

**Tips and tricks (general)**

- An insufficient power supply is the root cause of many weird symptoms/problems. Never trust in ratings written on the PSU since they might be wrong, the PSU might be old/dying and cable/contact resistance adds to problems. In other words: Before you blame Armbian for strange behaviour please try at least one second power supply (this applies to both PSU and cable between PSU and board if this is separate -- especially USB cables really suck due to high resistance leading to severe voltage drops).
- In case you experience instabilities check your SD card using `armbianmonitor -c $HOME` and think about installing [RPi-Monitor for H3](http://www.cnx-software.com/2016/03/17/rpi-monitor-is-a-web-based-remote-monitor-for-arm-development-boards-such-as-raspberry-pi-and-orange-pi/) to get an idea whether you suffer from overheating (`sudo armbianmonitor -r` will install everything needed).
- Especially for desktop images the speed of your SD card matters. If possible try to use our _nand-sata-install_ script to move the rootfs away from SD card. The script also works with USB disks flawlessly ([some background information](http://forum.armbian.com/index.php/topic/793-moving-to-harddisk/)).

**Tips and tricks (H3 specific / lowering consumption)**

Recent research showed that H3 boards operated as wired IoT nodes need way less power compared to Raspberry Pis in the same situation (Ethernet active). If you want to use your H3 device headless (server/IoT) and care about power consumption then there exist a couple of tweaks to get your board being more energy efficient when using legacy kernel (no tests done yet with mainline kernel):

- Disabling HDMI/GPU saves ~200mW.
- Allowing to temporarely only negotiate a Fast Ethernet connection on GbE capable boards saves +350 mW.
- Adjusting DRAM clockspeed is surprisingly another way to control consumption (on NanoPi NEO for example changing DRAM clockspeed between 132 MHz and 672 MHz results in consumption differences of 470mW).
- Limiting maximum CPU clockspeed will help with lowering maximum consumption (think about scripts running amok or something going terribly wrong), the same applies to limiting the count of active CPU cores.
- Choosing a board with Fast instead of Gigabit Ethernet or disabling GbE on the latter using `ethtool` or `ifconfig` saves at least 150 mW (board specific).

As an example: We chose default Armbian settings for NanoPi NEO to ensure this board is not able to exceed 2W consumption when running with no peripherals connected. This resulted in CPU and DRAM clockspeed of just 480/408 MHz while _booting_ (the first ~20 seconds). In normal operation we limit maximum CPU clockspeed to 912 MHz to stay below the 2W consumption barrier even in worst case scenarios.

In case you want to have a few more percent maximum CPU performance you would need to set maximum cpufreq to 1200 MHz instead of 'just' 912 MHz maximum CPU clock using our new [h3consumption tool](http://forum.armbian.com/index.php/topic/1878-testers-wanted-h3consumption-to-be-included-into-future-armbian-releases/). Be warned: this will both heavily increase consumption and SoC temperature since exceeding 912 MHz CPU clockspeed means feeding the SoC with 1.3V instead of 1.1V core voltage (most smaller H3 devices use a voltage regulator only switching between 2 voltages to feed the SoC based on load).

Walking this route in the other direction is more interesting: In case you want to use an H3 device as IoT node you might want to limit both idle and maximum consumption. That should involve disabling stuff not needed (eg. HDMI/GPU since this saves 200mW) or limiting ressource consumption: Lowering maximum clockspeeds for both CPU and DRAM or even disabling CPU cores (which helps _not_ with idle consumption since ARM cores enter low-power modes if not needed but can help lowering maximum consumption requirements).

Since all of this stuff is based on recent research and being still WiP please consider reading through relevant threads in Armbian forums **and** join development/research/discussions: [Running H3 boards with minimal consumption](http://forum.armbian.com/index.php/topic/1614-running-h3-boards-with-minimal-consumption/), [SBC consumption/performance comparisons](http://forum.armbian.com/index.php/topic/1748-sbc-consumptionperformance-comparisons/) and [Default settings for NanoPi NEO/Air](http://forum.armbian.com/index.php/topic/1728-rfc-default-settings-for-nanopi-neoair/).

