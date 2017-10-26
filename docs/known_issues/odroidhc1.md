**Legacy kernel images**

Based on a review from @tkaiser, 

> https://forum.armbian.com/index.php?/topic/4983-odroid-hc1/

1. Use next kernel, 
1. don't think about USB3 issues any more (that's a XU4 problem), 
1. don't expect serial console problems (that was an Armbian problem), and 
1. please overthink 'rootfs on HDD' (on SSD that's great, HDDs are too slow and you prevent them from sleeping when moving the rootfs on them).

- eMMC install might be broken if you don't have recent uboot on your eMMC card - you must update it. Add `run copy_uboot_sd2emmc` to your boot.ini, boot from SD card with attached eMMC. This is one time job - remove that command from boot.ini,
- serial console is broken.

**Mainline kernel images** 
TBD

Hardkernel kept everything 100% compatible to ODROID XU4

With HC1 we're talking about Hardkernel's 4.9 or mainline

**Unverified matter**
> derived from comment chain in the review

1. Mine is not connecting at gigabit - fast ethernet only. Same cable (+few others), same PSU, same SD card, any kernel, while XU4 runs at Gigabit w/o problem
> Possibly a cable quality issue, as a cable swap caused the problem to disappear

**Notes**
1. Based on the XU4 template with exceptions

1. To avoid 'using up' write cycles on the SD media, once working, move to a RO root
filesystem, and 'chain boot' into the 2.5 in SATA drive (either SSD or spinnnig)
which do not have the same 'wear' issues

**Boot message chain**
1. Made with: 
> armbianmonitor -u output 

test run done with external RTL8153 behind internal USB3 hub on XU4

> http://sprunge.us/cOJP
