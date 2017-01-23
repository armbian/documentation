**Legacy kernel images (all boards) ** (`default` branch)

- HDMI output supports only limited number of predefined resolutions
- TV Out doesn't work as expected (only PAL/NTSC resolution, overscanning, no h3disp support)
- 1-Wire protocol requires setting the minimum CPU frequency to 480MHz or higher
- Hardware accelerated video decoding supports only limited number of video formats
- OOM issues are possible due to a kernel bug

**Mainline kernel images (all boards) ** (`next`/`dev` branches)

- No Mali drivers
- No hardware accelerated video decoding
- `schedutil` CPU governor may cause clicks and pops on audio output - change to `ondemand` to work around this issue

**Board: Orange Pi Zero **

- Onboard wireless chip (XR819) has poor software support so wireless connection issues are expected
