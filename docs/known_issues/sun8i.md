**Legacy kernel** (`default` branch)

- HDMI output supports only predefined resolutions
- 1-Wire protocol requires setting the minimum CPU frequency to 480MHz or higher

**Mainline kernel** (`next`/`dev` branches)

- no MALI drivers
- no video acceleration
- `schedutil` governor may cause clicks and pops on audio output  - change to `ondemand` to work around this issue
