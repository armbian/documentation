# Device Tree overlays

### Armbian specific notes

- DT overlays are a Work-in-Progress (WIP) feature, present only in the nightly and user made images
- DT overlay parameters are even more experimental and require extensive testing
- Currently implemented only for sunxi based devices that use mainline u-boot and kernel
- Latest versions of the u-boot and the boot script is required

### Kernel provided vs user provided overlays

Overlays can be loaded from 2 locations:

- `/boot/dtb/overlay/` (`/boot/dtb/allwinner/overlay/` for 64-bit SoCs) - kernel provided overlays
- `/boot/overlay-user/` - user provided overlays

Main differences between these locations:

- Kernel provided overlays are updated with the kernel packages, any changes to this directory (including new files) will be lost on kernel upgrade
- Kernel provided directory may contain overlays for different SoCs, so overlay file name pattern will be `<prefix>-<name>`, for example `sun8i-h3-i2c0.dtbo`, where `sun8i-h3` is the prefix and `i2c0` is the name
- Kernel provided overlays are activated by the overlay name (i.e. `i2c0`), and the prefix is set at OS image creation time
- User provided overlays directory is empty by default and is meant for storing and using user created overlays that are not present in the kernel packages or modified stock overlays
- User provided overlays are activated by the file name (excluding the extension), i.e. for file `adafruit13m.dtbo` overlay name would be `adafruit13m`

### Activation

DT overlays are activated by editing u-boot environment file `/boot/armbianEnv.txt`

- Kernel provided overlays are activated by adding a name to the `overlays` variable
- User provided overlays are activated by adding a name to the `user_overlays` variable
- No more than one `overlays` line and no more than one `user_overlays` line can be present in the environment file
- Multiple names should be separated by space
- Reboot is required for any changes to take effect

### Overlay parameters

Some overlays have additional parameters that can be set. None of the parameters are mandatory to set if default value is suitable.

Parameters are set by adding their name and value to `/boot/armbianEnv.txt`, each parameter should be added on a new line.

Please refer to `README.<SoC_prefix>-overlays` files in `/boot/dtb/overlay/` (`/boot/dtb/allwinner/overlay/` for 64-bit SoCs) directory for supported parameters, i.e. `README.sun8i-h3-overlays` for H3 based boards.

Parameters of type `pin` require special format:

- Value consists of a letter `P`, a letter that signifies the pin bank and a number of the pin in the bank
- Letters should be upper case
- Numbers should not contain leading zeros
- Examples: good - `PA9`, `PG12`; bad - `pa2`, `PG08`

### Example `/boot/armbianEnv.txt` contents:

	verbosity=1
	console=serial
	overlay_prefix=sun8i-h3
	rootdev=UUID=bd0ded76-1188-4b52-a20a-64f326c1f193
	rootfstype=ext4
	overlays=w1-gpio uart1 i2c0
	param_w1_pin=PA20
	param_uart1_rtscts=1

