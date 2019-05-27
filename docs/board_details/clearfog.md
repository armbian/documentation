To boot the image from USB flash:

- Write the image to a USB flash drive
- Insert the flash drive into the USB3.0 port
- Load the modified u-boot (from the Armbian image) using the UART method
- Stop the default boot sequence
- Execute in u-boot prompt: `run usbboot`

To flash the image to eMMC:

- Boot the image from USB flash
- Write the image to eMMC using `dd` or other methods
- Mount the eMMC partition and add a line `emmc_fix=on` to `/boot/armbianEnv.txt` file - this changes the DT during boot to switch from SD with card detect switch to a non-removable eMMC.
- Unmount the eMMC partition and reboot

Please refer to [this](https://forum.armbian.com/topic/3072-clearfog-pro-emmc-requires-sd-card-to-detect-device/) forum thread for the USB boot details and [this](http://forum.solid-run.com/linux-kernel-and-bootloaders-f34/unstable-mmc-operation-with-upstream-kernel-t2986.html) thread for a discussion of known eMMC issues.
