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

- a **xz-compressed image file**,
- a **sha file** for download verification
- and an **asc file** for image authentication.  

For each board we usually provide:

- one CLI server image with Debian Buster userspace
- one CLI server image with Ubuntu Focal userspace
- one desktop image with Ubuntu Focal userspace **or** Debian Buster userspace

Other unsupported builds may also be available (like Debian Stretch/Bullseye or Ubuntu Disco/Eoan/Hirsute).

Some boards have different options due to their hardware specialities - router or IoT boards.

### Legacy or current?

Only _current_ kernel branch is considered fully supported and can bring up video acceleration for example. NAND support is there but is still experimental.

The level of kernel support does depend on the board family. If in your specific case something does not work well, you are always free to try an image with _legacy_ kernel included.

### What are testing images?

- made from stable branches
- not very well tested
- for end users

### What are experimental/bleeding edge images?

- made from unstable branches
- untested
- for experienced users only

Do not use testing or edge images in a productive environment. We do appreciate  your constructive [feedback to developers](https://forum.armbian.com/forum/4-development/).

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

Write the xz compressed image  with [USBImager](https://gitlab.com/bztsrc/usbimager) or [balenaEtcher](https://www.balena.io/etcher/) on all platforms since unlike other tools, either can validate burning results **saving you from corrupted SD card contents**.

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

## How to update?

	apt update
	apt upgrade

**Update process can take hours in case of using cheap SD card and/or under heavy load.**

If the kernel was upgraded during this process you will be prompted to reboot at next login.

## How to update u-boot?

First you need to update packages described in a previous "How to update" step. Then run armbian-config utility, go to system settings and proceed to:

**"Install" "Install to/update boot loader"** -> **Install/Update the bootloader on SD/eMMC**

## How to adjust hardware features?

[Use the Armbian configuration utility `armbian-config`](User-Guide_Armbian-Config.md)

## How to install to eMMC, NAND, SATA, NVME & USB?

![Installer](https://www.armbian.com/wp-content/uploads/2016/12/nandsata.png)

Required condition:

NAND:

 * kernel 3.4.x and NAND storage
 * pre-installed system on NAND (stock Android or other Linux)

eMMC/SATA/USB/NVME:

 * any kernel
 * onboard eMMC storage
 * attached SATA, NVME or USB storage

Start the install script:

	armbian-install

and follow the guide. Theose are all possible scenarios:

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

## How to connect to wireless?

Required condition: a board with onboard or supported 3rd party wireless adapter on USB

If you know what is your wireless SSID:

	nmtui-connect SSID

![](https://www.armbian.com/wp-content/uploads/2016/12/wifi-1.png)

If you do not know, you can browse and then connect

	nmtui-connect

![](https://www.armbian.com/wp-content/uploads/2016/12/wifi-2.png)

## How to set fixed IP?

By default your main network adapter's IP is assigned by your router DHCP server and all network interfaces are managed by **NetworkManager**:

	user@boardname:~$ nmcli con show
	NAME	UUID	TYPE	DEVICE 
	Wired connection 1	xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx	802-3-ethernet	eth0 

The connection can now be edited with the following:

	nmcli con mod "Wired connection 1"
	  ipv4.addresses "HOST_IP_ADDRESS"
	  ipv4.gateway "IP_GATEWAY"
	  ipv4.dns "DNS_SERVER(S)"
	  ipv4.dns-search "DOMAIN_NAME"
	  ipv4.method "manual"

The same changes can also be done with NetworkManagers text user interface:

	sudo nmtui
