Experimental images are based on the mainline kernel and mainline u-boot

Following features should work:

- USB ports
- Ethernet
- DVFS and THS
- GPIO sysfs interface
- SPI and I2C interfaces (activation requires DT patches or overlays)
- HDMI display output with automatic detection of the resolution based on EDID
- Analog audio output and onboard microphone input
- SPI+USB boot
- USB OTG (may require DT patches or overlays)

Features that do not work:

- Proper shutdown - switching off the power is recommended
- Additional peripherials that are not enabled in the kernel config

Features that do not work and will not be fixed anytime soon:

- Hardware accelerated video decoding
- Mali driver
- HDMI audio output
