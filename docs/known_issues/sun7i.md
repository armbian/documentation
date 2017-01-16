**Legacy kernel** (`default` branches)

- unstable Bluetooth stack

**Mainline kernel** (`next`/`dev` branches)

- stable Bluetooth stack
- no MALI drivers
- [different GPIO numbering](http://linux-sunxi.org/GPIO)
- no video acceleration
- `schedutil` governor may cause clicks and pops on audio output  - change to `ondemand` to work around this issue
