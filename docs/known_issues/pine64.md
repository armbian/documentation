**Legacy kernel images (all boards) ** (`default` branch)

- Arm64 browsers (Firefox, Chromium, Iceweasel) may crash frequently. Armhf versions of these browsers should be used instead (Iceweasel and Firefox preinstalled in desktop images should be of the right architecture out of the box)
- HDMI output supports only limited number of predefined resolutions
- Hardware accelerated video decoding supports only limited number of video formats

**Mainline kernel images (all boards) ** (`next` and `dev` branch)

- [Check mainlining effort status matrix](http://linux-sunxi.org/Linux_mainlining_effort#Status_Matrix)

**Board: Pine64/Pine64+ **

- Gigabit Ethernet performance: on some boards was confirmed as [hardware issue](http://forum.pine64.org/showthread.php?tid=835&pid=19773#pid19773), though the legacy kernel received a workaround that may help on some boards.
- Gigabit Ethernet performance: setting TX/RX delays manually in /boot/armbianEnv may improve performance on some boards. Refer to [this github issue](https://github.com/igorpecovnik/lib/issues/546) for the details.
