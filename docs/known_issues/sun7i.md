**Legacy kernel** (`default` branches)

- unstable Bluetooth stack

**Mainline kernel** (`next`/`dev` branches)

- No Mali drivers
- No hardware accelerated video decoding
- [Different GPIO numbering](http://linux-sunxi.org/GPIO) compared to the legacy kernel
- `schedutil` CPU governor may cause clicks and pops on audio output  - change to `ondemand` to work around this issue

**Board: Lamobo R1 **

- b53 switch driver in mainline kernel uses DSA interface for configuration instead of `swconfig` tool. Please check [this](https://github.com/igorpecovnik/lib/issues/511) issue for details

