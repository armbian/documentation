---
title: Installing to internal storage
description: "Move Armbian off the SD card with armbian-install: boot from eMMC, NAND, SPI or UEFI disk with the system on eMMC, SATA, USB or NVMe."
---
# Installing to internal storage

At this stage, nothing has been installed onto the board's internal drive yet. Using the installer, one can now decide where to install the boot loader and the rest of the system. The installer supports various combinations depending on the availability of onboard eMMC and/or attached SATA, NVME, or USB storage.

!!! tip "Armbian Installer support those storage scenarios:"

    * boot from SD, system on SATA / USB
    * boot from eMMC / NAND, system on eMMC/NAND
    * boot from eMMC / NAND, system on SATA / USB / NVME
    * Boot from SPI - system on SATA, USB or NVMe
    * Install/Update the bootloader on SD/eMMC
    * Install/Update the bootloader on special eMMC partition
    * Install/Update the bootloader on SPI Flash
    * Install system to UEFI disk

<!-- TODO: give the user a sensible default -->

Start the install script, make your choice, and follow the instructions:

    armbian-install

![Installer](https://www.armbian.com/wp-content/uploads/2016/12/nandsata.png)

After you have decided for an option, you can choose between the following file systems: <!-- TODO: only for system? -->

* ext2,3,4
* btrfs

For novice users, a sensible default is `ext4`.

Congratulation. You have successfully installed Armbian onto your board!

---

**Previous:** [First steps after login](first-steps.md)

**Next:** [Keeping Armbian up to date](updating.md)

Back to the [Getting Started](../User-Guide_Getting-Started.md) overview.
