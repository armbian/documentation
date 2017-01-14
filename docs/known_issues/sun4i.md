**Mainline kernel** (`next`/`dev` branches)

- no MALI drivers
- [different GPIO numbering](http://linux-sunxi.org/GPIO)
- no video acceleration
- `schedutil` governor may cause clicks and pops on audio output  - change to `ondemand` to work around this issue
