**Mainline kernel images (all boards) ** (`current` and `edge` branch)

- [Check mainlining effort status matrix](https://linux-sunxi.org/Linux_mainlining_effort#Status_Matrix)

**Board: Pine64/Pine64+ **

- Gigabit Ethernet performance: on some boards was confirmed as [hardware issue](https://forum.pine64.org/showthread.php?tid=835&pid=19773#pid19773), though the legacy kernel received a workaround that may help on some boards.
- Gigabit Ethernet performance: setting TX/RX delays manually in /boot/armbianEnv may improve performance on some boards. Refer to [this github issue](https://github.com/igorpecovnik/lib/issues/546) for the details.
