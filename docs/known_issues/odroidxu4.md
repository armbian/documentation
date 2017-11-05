**Legacy kernel images**

- eMMC install might be broken if you don't have recent uboot on your eMMC card - you must update it. Add `run copy_uboot_sd2emmc` to your boot.ini, boot from SD card with attached eMMC. This is one time job - remove that command from boot.ini,
- serial console is broken.
