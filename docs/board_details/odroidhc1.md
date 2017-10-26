-  a stripped down XU4 version dropping the internal USB hub, display and GPIO support but adding instead a great performing and UAS capable USB-to-SATA bridge (JMS578) directly to the PCB so no more cable/contact issues, no more underpowering and no more UAS hassles with some disk enclosures (that contain a broken SATA bridge or combine a working UAS capable chip with a branded/broken firmware)

from Review:
> https://forum.armbian.com/index.php?/topic/4983-odroid-hc1/

1. Software support efforts needed for HC1 (or the other variants MC1 or HC2) are zero since Hardkernel kept everything 100% compatible to ODROID XU4
1. HC1 is a very nice design addressing a few of XU3/XU4 former USB3 issues (mostly related to 'hardware' issues like cable/contact problems with USB3-A or underpowering)
1. Heat dissipation works very well (and combining this enclosure design with a huge, slow and therefore silent fan is always an option, Hardkernel evens sells a large fan suitable for 4 HC1 or MC1 units)
1. The used JMS578 bridge chip to provide SATA access is a really good choice since this IC does not only support UAS (USB Attached SCSI, way more efficient than the older MassStorage protocol and also the reason why SSDs perform twice as fast on HC1 now with 4.x kernel) but also SAT ('SCSI / ATA Translation') so you can make use of tools like hdparm/hdidle without any issues and also TRIM (though software support is lacking at least in 4.9 kernel tested with)
1. Dealing with attached SATA disks is way more reliable than on other 'USB only' platforms since connection/underpowering problems are solved
1. Only downside is the age/generation of the Exynos 5422 SoC since being an ARMv7 design it's lacking for example 'ARM crypto extensions' compared to some more recent ARM SoCs which can do stuff like AES encryption a lot more efficient/faster
