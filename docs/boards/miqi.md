- to boot from SD card you need to press and hold a button on the back side of the board and power on. This erases bootloader on eMMC and now you can boot from SD. In case of troubles use [this tool to restore stock bootloader](https://github.com/mqmaker/miqi-prebuilt).
- known issues: random MAC, MALI and video acceleration libraries are not installed yet
- overclocking to 2.2Ghz is possible with (patched) mainline kernel. Enable with: 
	
		echo 1 > /sys/devices/system/cpu/cpufreq/boost		# enable turbo
		nano /etc/default/cpufrequtils 						# adjust new limit
		/etc/init.d/cpufrequtils restart 					# restart cpufrequtils

- make sure you have a quality (stable) and powerful (3A) PSU if you want stable operations and overclocking. [You can also power via header](https://forum.armbian.com/index.php?/topic/1095-miqi-is-a-35-single-board-computer-with-rockchip-rk3288/#comment-8338).