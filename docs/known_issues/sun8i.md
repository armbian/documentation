**Legacy kernel images (all boards) ** (`default` branch)

- HDMI output (if exists) supports only limited number of predefined resolutions
- TV Out doesn't work as expected (only PAL/NTSC resolution, overscanning, no h3disp support, [notes for OPi Zero](https://forum.armbian.com/index.php?/topic/3837-psa-orange-pi-zero-expansion-board-tv-out-not-working-solution/))
- 1-Wire protocol, reading out DHT11/DHT22 sensors or [S/PDIF](https://forum.armbian.com/index.php?/topic/1891-spdif-output-on-nanopi-m1/) requires setting the minimum CPU frequency to 480MHz or higher
- Hardware accelerated video decoding supports only limited number of video formats
- 'Out of memory' (OOM) issues are possible due to a kernel bug

**Mainline kernel images (all boards) ** (`next`/`dev` branches)

- No Mali drivers
- No hardware accelerated video decoding
- `schedutil` CPU governor may cause clicks and pops on audio output - change(d) to `ondemand` to work around this issue

**Board: Orange Pi Zero **

- Onboard wireless chip (XR819) has poor software support so wireless connection issues are expected
