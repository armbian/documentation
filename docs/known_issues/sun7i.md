**Mainline kernel** (`current`/`edge` branches)

- No hardware accelerated video decoding
- [Different GPIO numbering](https://linux-sunxi.org/GPIO) compared to old legacy 3.x kernel
- `schedutil` CPU governor may cause clicks and pops on audio output  - change to `ondemand` to work around this issue

**Board: Lamobo R1 **

- b53 switch driver in mainline kernel uses DSA interface for configuration instead of `swconfig` tool. Please check [this](https://github.com/igorpecovnik/lib/issues/511) issue for details
- underpower issues are possible when using hard drive, HDMI and wireless together. Connecting a battery may help
- Gigabit Ethernet transfer rate is around 300Mbit
