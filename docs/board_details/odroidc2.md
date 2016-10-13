[![](http://www.armbian.com/wp-content/uploads/2016/03/odroidc2.png
)](http://www.armbian.com/odroid-c2/)

- Idle consumption with legacy image, `setenv nographics "1"` defined in `/boot/boot.ini` and only Gigabit Ethernet connected is between ~2300 mW (@500 MHz) and ~2400 mW (@1536 MHz). Hardkernel provides the possibility to [exceed 1536 MHz max cpufreq](http://odroid.com/dokuwiki/doku.php?id=en:c2_set_cpu_freq) but Armbian refrains from doing so. In case you want to change settings please keep in mind that you might have to adjust both `/boot/boot.ini` and `/etc/defaults/cpufrequtils`.
- The legacy kernel we use implements a few different cpufreq governors that show partially strange behaviour (`interactive` most of the times acting like `performance` for example). Since idle consumption differences between different cpufreq governors are negligible choosing even `performance` seems to be ok. At least `conservative` governor that switches between upper and lower clockspeeds (for details see [here](https://github.com/igorpecovnik/lib/issues/499#issuecomment-253481174)) leads to some USB performance drops while not providing significant savings.
- If you don't need GbE network transfer speeds switching to Fast Ethernet with `ethtool -s eth0 speed 100 duplex full` saves ~230 mW.
- GbE Ethernet speed should reach 935 Mbits/sec in TX direction. In RX direction with defaults you should get 800 Mbits/sec but with some tuning it should be able to exceed 900 Mbits/sec:
  - echo 32768 > /proc/sys/net/core/rps_sock_flow_entries
  - echo 32768 > /sys/class/net/eth0/queues/rx-0/rps_flow_cnt
