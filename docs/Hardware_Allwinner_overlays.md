# Device Tree overlays

Most in-circuit and GPIO based interfaces (SPI, I2C, I2S, UART, ...) don't have a mechanism for detecting and identifying devices connected to the bus,
so Linux kernel has to be told explicitly about the device and its configuration details.

While Device Tree is a way of describing hardware configuration to the kernel, Device Tree overlays are a way for modifying the DT
in order to provide the kernel and kernel drivers with details about external devices or to activate interfaces disabled by default.

From mainline Linux kernel perspective all unused in-circuit type interfaces should be disabled by default
and all pins muxed with those interfaces should be available as standard GPIOs.

### Armbian specific notes

- DT overlays are a Work-in-Progress (WIP) feature, present only in the nightly and user made images
- DT overlay parameters are even more experimental and require extensive testing
- Currently implemented only for sunxi based devices that use mainline u-boot and kernel
- Latest versions of the u-boot and the boot script is required

Please note that different SoCs will have different sets of available overlays.

### Quick start

1. Check the README.<soc-id>-overlays in `/boot/dtb/overlay/` (32-bit SoCs) or `/boot/dtb/allwinner/overlay/` (64-bit SoCs) for a list of provided overlays, their required and optional parameters
2. Add names of overlays you want to activate to `overlays=` line in `/boot/armbianEnv.txt`, separated with spaces
3. Add required parameters with their values to `/boot/armbianEnv.txt`, one per line
4. Add optional parameters with their values to `/boot/armbianEnv.txt` if you want to change the default value, one per line
5. If you didn't find the required overlay or want to change one of provided overlays, place your compiled overlays in `/boot/overlay-user/` directory and list their names to `user_overlays=` line in `/boot/armbianEnv.txt`
6. Reboot

### armbianEnv.txt entries reference

- `overlay_prefix` - prefix for the DT and overlay file names, set at OS image creation time
- `overlays` - list of overlays to activate from kernel directory
- `user_overlays` - list of overlays to activate from `/boot/overlay-user/` directory
- `param_*` - overlay parameters

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
- No more than one `overlays` line and one `user_overlays` line can be present in the environment file
- Multiple names should be separated by space
- If activated overlays have parameters marked as "Required", those parameters have to be set to proper values
- Reboot is required for any changes to take effect

### Overlay parameters

Some overlays have additional parameters that can be set.

Parameters marked as "Required" have to be set if overlay with these parameters is activated, other parameters are not mandatory if default value is suitable.

Parameters are set by adding their name and value to `/boot/armbianEnv.txt`, each parameter should be added on a new line.

Please refer to `README.<SoC_prefix>-overlays` files in `/boot/dtb/overlay/` (`/boot/dtb/allwinner/overlay/` for 64-bit SoCs) directory for supported parameters, i.e. `README.sun8i-h3-overlays` for H3 based boards.

Parameters of type `pin` require special format:

- Value consists of a letter `P`, a letter that signifies the pin bank and a number of the pin in the bank
- Letters should be upper case
- Numbers should not contain leading zeros
- Examples: good - `PA9`, `PG12`; bad - `pa2`, `PG08`

### Overlay bus selection

SoCs may contain multiple bus controllers of the same type, i.e. Allwinner H3 contains 2 SPI controllers and Allwinner A20 contains 4 SPI controllers.

Please refer to your board documentation and schematic to determine what pins are wired to the pin headers and thus what bus number should be used in each case.

### Overlay pinmux conflicts

Some controllers may share the SoC pins in some configurations. For example on Allwinner H3 UART 3 and SPI 1 use the same pins - `PA13`, `PA14`, `PA15`, `PA16`.
In this case activating both UART 3 and SPI 1 would result in a conflict, and on practice only one interface (either SPI or UART) will be accessible on these pins.

Please check the SoC specific README, board schematic, SoC datasheet or other documentation if you are unsure about possible conflicts if activating multiple overlays for the controllers that use shared (muxed) pins.

### Overlay device endpoint conflicts

Overlays for devices that use addresses or similar mechanisms (i.e. SPI chip selects) can't be activated simultaneously if addresses (chip selects) are identical.

For example H3 SPI comtrollers have only one hardware chip select, so `spi-spidev` and `spi-jedec-nor` overlays cannot be activated both if they would use the same bus number and chip select.

### Overlay compatibility

Device Tree overlays for differnet platforms and SoCs are not directly compatible.
This, for example, means that overlays for H3 may need some changes to work on A20, and that Raspberry Pi overlays will need adjustments in order to be used on Allwinner based boards.

Rework may include changing labels, references (phandles) and pinconf bindings.

### Debugging

As overlays and overlay parameters are applied by the u-boot, it is impossible to get any debugging information (such as error messages) from the OS.

Serial console on UART 0 is required to debug DT overlay related problems.

### Example `/boot/armbianEnv.txt` contents:

	verbosity=1
	console=serial
	overlay_prefix=sun8i-h3
	rootdev=UUID=bd0ded76-1188-4b52-a20a-64f326c1f193
	rootfstype=ext4
	overlays=w1-gpio uart1 i2c0 spi-spidev
	param_w1_pin=PA20
	param_w1_pin_int_pullup=1
	param_uart1_rtscts=1
	param_spidev_spi_bus=0

##### Example of serial console log when using several overlays:

	## Executing script at 43100000
	U-boot loaded from SD
	Boot script loaded from mmc
	265 bytes read in 182 ms (1000 Bytes/s)
	5074230 bytes read in 532 ms (9.1 MiB/s)
	5702664 bytes read in 579 ms (9.4 MiB/s)
	Found mainline kernel configuration
	32724 bytes read in 269 ms (118.2 KiB/s)
	882 bytes read in 277 ms (2.9 KiB/s)
	Applying kernel provided DT overlay sun8i-h3-w1-gpio.dtbo
	506 bytes read in 326 ms (1000 Bytes/s)
	Applying kernel provided DT overlay sun8i-h3-uart1.dtbo
	374 bytes read in 377 ms (0 Bytes/s)
	Applying kernel provided DT overlay sun8i-h3-i2c0.dtbo
	788 bytes read in 347 ms (2 KiB/s)
	Applying kernel provided DT overlay sun8i-h3-spi-spidev.dtbo
	4327 bytes read in 268 ms (15.6 KiB/s)
	Applying kernel provided DT fixup script (sun8i-h3-fixup.scr)
	## Executing script at 44000000
	tmp_bank=A
	tmp_pin=20
	## Loading init Ramdisk from Legacy Image at 43300000 ...
	   Image Name:   uInitrd
	   Image Type:   ARM Linux RAMDisk Image (gzip compressed)
	   Data Size:    5074166 Bytes = 4.8 MiB
	   Load Address: 00000000
	   Entry Point:  00000000
	   Verifying Checksum ... OK
	## Flattened Device Tree blob at 43000000
	   Booting using the fdt blob at 0x43000000
	   reserving fdt memory region: addr=43000000 size=9000
	   Loading Ramdisk to 49b29000, end 49fffcf6 ... OK
	   Loading Device Tree to 49b1d000, end 49b28fff ... OK

	Starting kernel ...

