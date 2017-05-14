- severe powering troubles due to micro USB power connector. You need extreme quality PSU and cables and even in that case you will probably suffer regular crashing and might not even boot up. [https://forum.armbian.com/index.php?/topic/3327-asus-tinkerboard](https://forum.armbian.com/index.php?/topic/3327-asus-tinkerboard) 
- known issues: ethernet driver needs some fixing
- overclocking to 2.2Ghz is possible with (patched) mainline kernel and lab power supply. Enable with:

		echo 1 > /sys/devices/system/cpu/cpufreq/boost		# enable turbo
		nano /etc/default/cpufrequtils 						# adjust new limit
		/etc/init.d/cpufrequtils restart 					# restart cpufrequtils

