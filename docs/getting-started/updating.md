---
title: Keeping Armbian up to date
description: "Update an Armbian system: APT for the base operating system, armbian-install for the boot loader, and how the firmware package freeze protects you."
---
# Keeping the system up to date

The operating system consists of two parts that must be updated separately.


## Update the Armbian OS

For the base operating system, use the APT package manager to keep the packages up to date.

    apt update
    apt upgrade

**The Update process can take quite some time in case you are using an old or a cheap SD card and/or experience heavy load.**

Users with a desktop will find graphical tools that allow one to update the system packages without using the command line.

Armbian provides a firmware package freeze feature to provide you with the possibility to upgrade all packages **but** the firmware. This prevents unpleasant surprises on functionality regressions that can come with kernel upgrades. To enable or disable this feature, look for

    Enable Armbian kernel/firmware upgrades / Disable Armbian kernel upgrades

within [armbian-config](../config/index.md).

If the kernel was upgraded during this process, you will be prompted to reboot at the next login.

<!-- TODO: maybe move this to advanced? Definitely not for novice users -->

!!! danger "Upgrade the Armbian OS"

    When a new major release of Debian or Ubuntu is out, we recommend to start with a fresh image. While it is possible to do what is called a _"dist-upgrade"_, the process is largerly in the domain of the underlaying Debian or Ubuntu user space. We provide only an experimental `Distribution upgrades` feature for [armbian-config](../config/index.md).

    Userspaces distribution upgrades are neither tested nor supported. Therefore Armbian cannot provide any support if something goes wrong.


## Update the boot loader

The second part that can be updated is the boot loader.

First, update all packages as described in the previous section. Then run:

```bash
sudo armbian-install
```

and select:

    Install/Update the bootloader on SD/eMMC

---

**Previous:** [Installing to internal storage](install-to-internal-storage.md)

**Next:** [If something goes wrong](troubleshooting.md)

Back to the [Getting Started](index.md) overview.
