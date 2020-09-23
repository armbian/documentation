# Allwinner H3 boards

### Overview

The H3 SoC from Allwinner is meant for OTT boxes and therefore its reference design is _not_ accompanied by a separate PMIC (power management IC) unlike _A series_ Allwinner SoCs (like A10, A20, A64, ...). No PMIC means also that there is no battery charging/monitoring implemented so H3 is not that much suited for mobile devices. On the other hand some pretty cheap H3 boards were released that can be driven with rather low consumption and therefore combining H3 devices with a battery became a real use case with boards like [Orange Pi One/Lite](http://linux-sunxi.org/Orange_Pi_Lite), NanoPi [NEO and Neo AIR](http://linux-sunxi.org/FriendlyARM_NanoPi_NEO).

As usual [SoC](http://linux-sunxi.org/H3) and [device information](http://linux-sunxi.org/Category:H3_Devices) can be found in Linux-sunxi wiki. Same applies to status of [mainlining kernel efforts](http://linux-sunxi.org/Linux_mainlining_effort). Adding to the usual SoC feature set (I2C, SPI, PWM, UART, SDIO, GPIO and so on) H3 has one USB OTG port, 3 real USB host ports (not exposed on all devices), Fast- and Gigabit Ethernet capablities (board specific), a Mali400MP2 GPU and Allwinner's video encoding/decoding engine.

When CPU or GPU cores are fully utilized H3 tends to overheat over time like any other popular ARM SoC released within the last 2-3 years. With Armbian we provide sane dvfs (dynamic voltage frequency scaling) settings that help a lot with throttling. In case you plan to operate your H3 device constantly under high load please check Armbian forums first since boards behave differently (related to voltage regulation and PCB size and design -- some use copper layers to spread the heat away from the SoC). Also consider applying a heatsink to the SoC (a fan should not be necessary unless you want to do number crunching on your board and then you obviously chose the wrong device).

You find some [differentiation criteria regarding supported H3 devices as well as an overview/history of H3 software support in our forums](https://forum.armbian.com/topic/1351-h3-board-buyers-guide/) or use Jean-Luc's [nice comparison table](http://www.cnx-software.com/2016/06/08/allwinner-h3-boards-comparison-tables-with-orange-pi-banana-pi-m2-nanopi-p1-and-h3-olinuxino-nano-boards/#comments) (both slightly outdated since more H3 devices have been released in the meantime).

### Kernel support

Almost all features of the H3 SoC are supported on Armbian's _current_ branch. Please refer to the [Linux sunxi support sheet](https://linux-sunxi.org/Linux_mainlining_effort).

### Default settings

- CPU frequency settings are 480 MHz to 1.37 GHz on most boards (cpufreq governor is _interactive_ therefore the boards only increase CPU speed and consumption when needed). Varity might occur due to different voltage regulators and heat dissipation behaviour. Theoretically lower frequencies are possible but disabled by default due to known stability issues.
- Armbian unlike older/other H3 OS images uses the green led as 'power on' indicator (blinking means 'ready to login' or 'shutting down'), the red led (blue on NanoPis) can be used for your own purpose.

### Tips and tricks (general)

- An insufficient power supply **is the root cause of many weird symptoms/problems**. Never trust in ratings written on the PSU since they might be wrong, the PSU might be old/dying and cable/contact resistance adds to problems. In other words: Before you blame Armbian for strange behaviour please try at least one second power supply (this applies to both PSU and cable between PSU and board if this is separate -- especially USB cables really suck due to high resistance leading to severe voltage drops).
- In case you experience instabilities check your SD card using `armbianmonitor -c $HOME` and think about installing [RPi-Monitor for H3](http://www.cnx-software.com/2016/03/17/rpi-monitor-is-a-web-based-remote-monitor-for-arm-development-boards-such-as-raspberry-pi-and-orange-pi/) to get an idea whether you suffer from overheating (`sudo armbianmonitor -r` will install everything needed).
- Especially for desktop images the speed of your SD card matters. If possible try to use our _nand-sata-install_ script to move the rootfs away from SD card. The script also works with USB disks flawlessly ([some background information](https://forum.armbian.com/topic/793-moving-to-harddisk/)).

### Tips and tricks (H3 specific / lowering consumption) (outdated)

Recent research showed that H3 boards operated as wired IoT nodes need way less power compared to Raspberry Pis in the same situation (ethernet active). If you want to use your H3 device headless (server/IoT) and care about power consumption then there exist a couple of tweaks to get your board being more energy efficient when using in the meantime unsupported 3.x kernel (no tests done yet with up-to-date _legacy_/_current_ kernel):

- Disabling HDMI/GPU saves ~200mW.
- Allowing to temporarely only negotiate a Fast Ethernet connection on GbE capable boards saves +350 mW.
- Adjusting DRAM clockspeed is surprisingly another way to control consumption (on NanoPi NEO for example changing DRAM clockspeed between 132 MHz and 672 MHz results in consumption differences of 470mW).
- Limiting maximum CPU clockspeed will help with lowering maximum consumption (think about scripts running amok or something going terribly wrong), the same applies to limiting the count of active CPU cores.
- Choosing a board with Fast instead of Gigabit Ethernet or disabling GbE on the latter using `ethtool` or `ifconfig` saves at least 150 mW (board specific).

As an example: We chose default Armbian settings for NanoPi NEO to ensure this board is not able to exceed 2W consumption when running with no peripherals connected. This resulted in CPU and DRAM clockspeed of just 480/408 MHz while _booting_ (the first ~20 seconds). In normal operation we limit maximum CPU clockspeed to 912 MHz to stay below the 2W consumption barrier even in worst case scenarios.

In case you want to have a few more percent maximum CPU performance you would need to set maximum cpufreq to 1200 MHz instead of 'just' 912 MHz maximum CPU clock using our new [h3consumption tool](https://forum.armbian.com/topic/1878-testers-wanted-h3consumption-to-be-included-into-future-armbian-releases/). Be warned: This will both heavily increase consumption and SoC temperature since exceeding 912 MHz CPU clockspeed means feeding the SoC with 1.3V instead of 1.1V core voltage (most smaller H3 devices use a voltage regulator only switching between two voltages to feed the SoC based on load).

Walking this route in the other direction is more interesting: In case you want to use an H3 device as IoT node you might want to limit both idle and maximum consumption. That should involve disabling stuff not needed (eg. HDMI/GPU since this saves 200mW) or limiting ressource consumption: Lowering maximum clockspeeds for both CPU and DRAM or even disabling CPU cores (which helps _not_ with idle consumption since ARM cores enter low-power modes if not needed but can help lowering maximum consumption requirements).

Since all of this stuff is based on recent research and being still WiP please consider reading through relevant threads in Armbian forums **and** join development/research/discussions: [SBC consumption/performance comparisons](https://forum.armbian.com/topic/1748-sbc-consumptionperformance-comparisons/) and [Default settings for NanoPi NEO/Air](https://forum.armbian.com/topic/1728-rfc-default-settings-for-nanopi-neoair/).

