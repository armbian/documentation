# Armbian Quick Start Guide

<iframe width="607" height="342" src="https://www.youtube.com/embed/hFrdyLc4g50" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Mentioned links:

- [https://gitlab.com/bztsrc/usbimager/](https://gitlab.com/bztsrc/usbimager/)  
- [https://forum.armbian.com/topic/4767-powering-through-micro-usb/](https://forum.armbian.com/topic/4767-powering-through-micro-usb/)  
- [https://docs.armbian.com/](https://docs.armbian.com/)  
- [https://forum.armbian.com/profile/9032-werner/](https://forum.armbian.com/profile/9032-werner/)  
- [https://forum.armbian.com/topic/12803-armbian-irc-chat/](https://forum.armbian.com/topic/12803-armbian-irc-chat/)  

## Prerequisites for new users

Please, make sure you have:

- a proper power supply according to the board manufacturer requirements (basic usage example: 5V/2A with DC Jack barrel or **thick** USB cable)
- a reliable SD card (see below "How to prepare a SD card?")

## What to download?

The download for each image consists of three separate files:

- **.xz**-compressed image file
- **.sha file** for download verification
- **.asc file** for image authentication  

For each board we usually provide various image types:

- **CLI** - server variant without desktop environment
- **minimal** - very lightweight server variant with just the bare minimum, not even includes `armbian-config`. Everything can be installed via `apt`.
- **Desktop** full featured desktop image with either Ubuntu Jammy userspace **or** Debian Bookworm userspace

Other (unsupported) builds may also be available (like Debian Bullseye/Sid or Ubuntu Lunar/Mantic).
Some boards have different options due to their hardware specialities - router or IoT boards.

### Legacy, current or edge?

- **legacy** is either a vendor provided kernel or an old LTS mainline kernel. Use if either _current_ is not available or something does not work well.
- **current** is usually following current mainline LTS kernel and considered fully supported and can bring up features video acceleration for example
- **edge** is as the name implies cutting-edge and usually following the latest mainline kernel or 3rd party development branch. Untested, unstable, can break at any time, for experienced users only.

The level of kernel support however always depends on the board family. 
If in your specific case something does not work well, you are always free to try an image with an other kernel included.

### What are testing images *(WIP)*?

- made from stable branches
- not very well tested
- for end users

**Do not use** testing or edge images in a productive environment. We do appreciate your constructive [feedback to developers](https://forum.armbian.com/forum/4-development/).

### How to check download authenticity?

All our images are digitally signed and therefore it is possible to check their authenticity.  You need to  issue these commands (Linux/macOS, you might need to install dependencies first, eg. `apt-get install gnupg ` on Debian/Ubuntu or `brew install gnupg ` on macOS. on windows install the current simple gnupg [Gnupg](https://gnupg.org/download/):
	
	# download public key from the database
	gpg --keyserver hkp://keyserver.ubuntu.com --recv-key DF00FAF1C577104B50BF1D0093D6889F9F0E78D5
	
	# perform verification 
	gpg --verify Armbian_5.18_Armada_Debian_jessie_3.10.94.img.xz.asc

	# proper response
	gpg: Signature made sob 09 jan 2016 15:01:03 CET using RSA key ID 9F0E78D5
	gpg: Good signature from "Igor Pecovnik (Ljubljana, Slovenia) <igor.++++++++++++@gmail.com>"

	# wrong reponse. Not genuine Armbian image!
	gpg: Signature made Sun 03 Jan 2016 11:46:25 AM CET using RSA key ID 9F0E78D5
	gpg: BAD signature from "Igor Pecovnik (Ljubljana, Slovenia) <igor.++++++++++++@gmail.com>"

It is safe to ignore the message `WARNING: This key is not certified with a trusted signature!`.

### How to check download integrity?

Since it might happen that your download got somehow corrupted we integrate a checksum/hash for the image.  You can compare the image's SHA-256 hash with the one contained in the `sha256sum.sha` file. 

On Windows, you can download and use the [QuickHash GUI](https://www.quickhash-gui.org/download/quickhash-v3-1-0-windows/) and follow the instructions in the gui.

while on Linux/macOS, in the directory in which you have downloaded the files ,you would do this

	shasum -a 256 -c Armbian_*.img.sha
	#good response
	Armbian_5.35_Clearfogpro_Debian_stretch_next_4.13.16.img: OK

## How to prepare a SD card?

**Important note:** Make sure you use a **good, reliable and fast** SD card. If you encounter boot or stability troubles in over 95 percent of the time it is either insufficient power supply or related to SD card (bad card, bad card reader, something went wrong when burning the image, card too slow to boot -- 'Class 10' highly recommended!). Armbian can simply not run on unreliable hardware so checking your SD card with either [F3](https://fight-flash-fraud.readthedocs.io/en/stable/) or [H2testw](https://www.heise.de/download/product/h2testw-50539) is mandatory if you run in problems. Since [counterfeit SD cards](https://www.happybison.com/reviews/how-to-check-and-spot-fake-micro-sd-card-8/) are still an issue checking with F3/H2testw directly after purchase is **highly recommended**.

Write the **.xz compressed image** with a tool [USBImager](https://gitlab.com/bztsrc/usbimager) or [balenaEtcher](https://www.balena.io/etcher/) on all platforms since, unlike other tools, either can validate written data **saving you from corrupted SD card contents**.

Also important: Most SD cards are only optimised for sequential reads/writes as it is common with digital cameras. This is what the *speed class* is about. The SD Association defined [*Application Performance Class*](https://www.sdcard.org/developers/overview/application/index.html) as a standard for random IO performance.

|Application Performance Class|Pictograph|Miniumum Random Read|Minimum Random Write|Minimum Sustained (Seq. Write)|
|---|---|---|---|---|
|Class 1 (A1)|![a1-logo](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/a1-logo.png)|1500 4k IOPS|500 4k IOPS|10MBytes/sec|
|Class 2 (A2)|![a2-logo](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/a2-logo.png)|4000 4k IOPS|2000 4k IOPS|10MBytes/sec|

At the time of this writing A1 and A2 cards are only widely available from SanDisk. Armbian recommends A1 rated SD-Cards **only** now ([A2 rated cards need yet lacking driver support and therefore show lower overall and especially random IO performance](https://github.com/ThomasKaiser/Knowledge/blob/master/articles/A1_and_A2_rated_SD_cards.md)). For example:

![a1-16gb-card](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/sandisk-ultra-a1.png) ![a1-32gb-card](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/sandisk-extremepro-a1.png) ![a2-64gb-card](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/sandisk-extreme-a2.png)

In case you chose an SD card that was already in use before please consider resetting it back to 'factory default' performance with [SD Formatter](https://www.sdcard.org/downloads/formatter/) before burning Armbian to it ([explanation in the forum](https://forum.armbian.com/topic/3776-the-partition-is-not-resized-to-full-sd-card-size/&do=findComment&comment=27413)). Detailed information regarding ['factory default' SD card performance](https://forum.armbian.com/topic/954-sd-card-performance/page/3/&tab=comments#comment-49811).

## How to boot?

Insert SD card into a slot and power the board. (First) boot (with DHCP) takes up to two minutes with a class 10 SD card and cheapest board.

## How to login?

First boot will log you automatically on HDMI or serial console while for SSH login you need to login as **root** and use password **1234**. You will be prompted to change this password. You will then be asked to create a normal user account that is sudo enabled (beware of default QWERTY keyboard settings at this stage). Please use [this tool](https://angryip.org/), to find your board IP address.


	odroidxu4 login: root (automatic login)

	  ___      _           _     _  __  ___   _ _  _
	 / _ \  __| |_ __ ___ (_) __| | \ \/ / | | | || |
	| | | |/ _` | '__/ _ \| |/ _` |  \  /| | | | || |_
	| |_| | (_| | | | (_) | | (_| |  /  \| |_| |__   _|
	 \___/ \__,_|_|  \___/|_|\__,_| /_/\_\\___/   |_|

	Welcome to Armbian 21.11 Jammy with Linux 5.4.160-odroidxu4

	No end-user support: built from trunk

	System load:   13%              Up time:       0 min
	Memory usage:  7% of 1.94G      IP:            10.0.10.112
	CPU temp:      48°C             Usage of /:    6% of 29G

	[ 0 security updates available, 45 updates total: apt upgrade ]
	Last check: 2021-11-21 10:32

	[ General system configuration (beta): armbian-config ]

	Last login: Sun Nov 21 10:32:42 UTC 2021 on tty1

	Waiting for system to finish booting ...

	New to Armbian? Documentation: https://docs.armbian.com Support: https://forum.armbian.com

	New root password: ********
	Repeat password: ********

	Choose default system command shell:

	1) bash
	2) zsh

	Shell: ZSH

	Creating a new user account. Press <Ctrl-C> to abort

	Please provide a username (eg. your forename): igorp
	Create password: ********
	Repeat password: ********

	Please provide your real name: Igor

	Dear Igor, your account igorp has been created and is sudo enabled.
	Please use this account for your daily work from now on.

	Detected timezone: Europe/Ljubljana

	Set user language based on your location? [Y/n] 

	Generating locales: sl_SI.UTF-8

	You selected ZSH as your default shell. 
	If you want to use it right away, please logout and login! 

	root@odroidxu4:~# 

## How to update firmware and packages?

	apt update
	apt upgrade

**Update process can take hours in case of using cheap SD card and/or under heavy load.**

If the kernel was upgraded during this process you will be prompted to reboot at next login.

## How to update u-boot?

First you need to update packages described in a previous "How to update" step. Then run armbian-config utility, go to system settings and proceed to:

**"Install" "Install to/update boot loader"** -> **Install/Update the bootloader on SD/eMMC**

## How to upgrade distribution (like Focal to Jammy or Bullseye to Bookworm)?

Fire up `armbian-config` to freeze your firmware packages (if not frozen already, select `System` and `Freeze`).  
Then follow generic upgrade instructions specific to your userspace:  

- Like for Debian: [https://www.debian.org/releases/bookworm/arm64/release-notes/ch-upgrading.en.html](https://www.debian.org/releases/bookworm/arm64/release-notes/ch-upgrading.en.html)  
- Or Ubuntu: launch `do-release-upgrade`

__Attention:__ Userspaces distribution upgrades are neither tested nor supported. Therefore Armbian cannot provide support if something goes wrong.  

## How to adjust hardware features?

[Use the Armbian configuration utility `armbian-config`](User-Guide_Armbian-Config.md)

## How to install to eMMC, SATA, NVME & USB?

![Installer](https://www.armbian.com/wp-content/uploads/2016/12/nandsata.png)

Required condition for eMMC/SATA/USB/NVME:

 * onboard eMMC storage
 * attached SATA, NVME or USB storage

Start the install script:

	armbian-install

and follow the guide. Those are all possible scenarios:

 * boot from SD, system on SATA / USB
 * boot from eMMC / NAND, system on eMMC/NAND
 * boot from eMMC / NAND, system on SATA / USB / NVME
 * Boot from SPI - system on SATA, USB or NVMe
 * Install/Update the bootloader on SD/eMMC
 * Install/Update the bootloader on special eMMC partition
 * Install/Update the bootloader on SPI Flash
 * Install system to UEFI disk

and you can choose the following file system options:

 * ext2,3,4
 * btrfs

On Allwinner devices after switching to boot from NAND or eMMC clearing the boot loader signature on the SD card is recommended: `dd if=/dev/zero of=/dev/mmcblkN bs=1024 seek=8 count=1` (replace `/dev/mmcblkN` with the correct device node -- in case you run this directly after `armbian-install` without a reboot in between then it's `/dev/mmcblk0`). When booting from eMMC to get SD cards auto-detected on Allwinner legacy images please consider changing `mmc0`'s `sdc_detmode` from 3 to 1 in the board's fex file (see [here](https://forum.armbian.com/topic/1702-orange-pi-plus-2e-where-is-16ghz-and-sd/?tab=comments#comment-13163) for details).  

## How to install to NAND?

While in theory writing to NAND should still be possible using `armbian-installer`, this requires running a very old 3.4.y kernel which Armbian as dropped support for several years ago. Therefore this feature is to be considered as deprecated and no support for either 3.4.y systems or NAND installations will be provided.
