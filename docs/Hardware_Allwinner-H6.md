# Allwinner H6

### CPU frequency

[See the generic Allwinner page](https://docs.armbian.com/Hardware_Allwinner/)

~~The H6 CPU frequency has ben soft-capped at 1,48 GHz to avoid thermal throttling too fast. This limit can be lifted by editing
`/etc/default/cpufrequtils` and set `MAX_SPEED` to `1810000`.~~
With the release of Armbian 20.05 "Kagu" new thermal zones have been added making this limitation obsolete and therefore has been removed. All H6 boards now clocking at the highest possible value OOB.

**Warning**
Adding proper cooling is highly recommended.


### PCIe (un-)supported

Some H6 SoC based boards (like Pine H64 Model a, discontinued) are shipped with a PCIe slot. This slot can and will **not be supported** by Armbian as it has to be considered as broken by design. [Linux-Sunxi](https://linux-sunxi.org/H6#Errata) writes about this: 

> Allwinner H6 has a quirky PCIe controller that doesn't map the PCIe address space properly (only 64k accessible at one time) to CPU, and accessing the PCIe config space, I/O space or memory space will need to be wrapped. As Linux doesn't wrap PCIe memory space access, it's not possible to do a proper PCIe controller driver for H6. The BSP kernel modifies the driver to wrap the access, so it's also not generic, and only devices with modified driver will work. 
