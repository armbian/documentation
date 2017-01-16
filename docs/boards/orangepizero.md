- Images with the legacy kernel provide a serial console gadget on the OTG port after the system boots up. Please make sure that board is properly powered (i.e. with microUSB Y cable or via GPIO pins) because a standard PC USB port will not provide enough current to the board

- It is possible to boot Armbian images (starting with 15.01 nightly and 5.25 release) from USB storage if a proper mainline u-boot is programmed to the onboard SPI flash
