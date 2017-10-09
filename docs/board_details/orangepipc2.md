Following features that arent't present in the mainline kernel should work:

- Ethernet
- DVFS
- THS
- DRM/KMS HDMI display driver with audio (2ch / stereo only) and CEC support

Refer to the [status matrix](https://linux-sunxi.org/Linux_mainlining_effort#Status_Matrix) for mainline kernel support status

Features that do not work:

- CVBS (composite video) output
- Proper shutdown - switching off the power is recommended
- Suspend/resume

Features that do not work and will not be added anytime soon:

- Hardware accelerated video decoding (Cedrus)
- Mali driver
- CSI camera input
