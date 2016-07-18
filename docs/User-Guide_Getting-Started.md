# Prerequisites for NEW users

Please, make sure you have:
- a proper power supply according to the board manufacturer requirements
- a reliable SD card (see below "How to prepare a SD card?")

# What to download?

Each board is fully supported with up to **four basic system** options: 
	
- Debian Wheezy, Jessie, Ubuntu Trusty, Xenial

Some boards also have a desktop version Debian Jessie.

# Legacy or Vanilla?

Both kernels, where exists, are stable and production ready, but you should use them for different purpuses since their basic support differ:

 - legacy: video acceleration, NAND support, connecting displays 
 - vanilla: headless server, light desktop operations 
 
# How to check download authenticity?

All our images are digitally signed and therefore it's possible to check theirs authentication. You need to unzip the download package and issue those commands (Linux):

	# download my public key from the database
	gpg --keyserver pgp.mit.edu --recv-key 9F0E78D5
	gpg --verify Armbian_4.83_Armada_Debian_jessie_3.10.94.raw.asc
	
	# proper respond
	gpg: Signature made sob 09 jan 2016 15:01:03 CET using RSA key ID 9F0E78D5
	gpg: Good signature from "Igor Pecovnik (Ljubljana, Slovenia) <igor.++++++++++++@gmail.com>"	
	
	# wrong repond. Not genuine Armbian image!
	gpg: Signature made Sun 03 Jan 2016 11:46:25 AM CET using RSA key ID 9F0E78D5
	gpg: BAD signature from "Igor Pecovnik (Ljubljana, Slovenia) <igor.++++++++++++@gmail.com>"

It is safe to ignore WARNING: This key is not certified with a trusted signature!

# How to prepare a SD card?

**Important note:** Make sure you use a **good & reliable** SD card. If you encounter boot troubles in 95 percent it's either insufficient power supply or a bad SD card or a bad card reader. Armbian can simply not run on unreliable hardware so checking your SD card with either [F3](http://oss.digirati.com.br/f3/) or [H2testw](http://www.heise.de/download/h2testw.html) is a must if you run in boot problems.

7z and zip archives can be uncompressed with [7-Zip](http://www.7-zip.org/) on Windows, [Keka](http://www.kekaosx.com/en/) on Mac and 7z on Linux (apt-get install p7zip-full). RAW images can be written with [Rufus](https://rufus.akeo.ie/) (Win) or DD in Linux/Mac:

	# Linux example: /dev/sdx is your sd card device
	dd bs=1M if=filename.raw of=/dev/sdx
	# OS X example: /dev/[r]diskx is your sd card device:
	diskutil unmountDisk diskx && dd bs=1m if=filename.raw of=/dev/rdiskx && diskutil eject diskx

Image writing takes around 3 minutes on a slow, class 6 SD card.

Also important: SD cards are optimised for sequential reads/writes as it's common in digital cameras. This is what the *speed class* is about. And while you shouldn't buy any card rated less than *class 10* today you should especially take care to choose one that is known to show high random I/O performance since this is way more performance relevant when used with any SBC. Even cards advertised as being 'high speed' show horribly low random IO performance in reality.

You won't be wrong picking one of these:

[![Samsung EVO 16GB UHS-I](http://www.armbian.com/wp-content/uploads/2016/03/sdcard-samsung-1.png)](http://www.amazon.com/dp/B00IVPU7KE)
[![Transcend Ultimate 16 GB UHS-I](http://www.armbian.com/wp-content/uploads/2016/03/sdcard-transcend-1.png)](http://www.amazon.com/gp/product/B00BLHWYWS)
[![SanDisk Extreme Pro 16 GB UHS-I](http://www.armbian.com/wp-content/uploads/2016/03/sdcard-sandisk-1.png)](http://www.amazon.com/dp/B008HK1YAA)

Detailed informations regarding SD cards performance:

- [SD card performance with Armbian - Thomas Kaiser](http://forum.armbian.com/index.php/topic/954-sd-card-performance/)
- [Raspberry Pi microSD card performance comparison - Jeff Geerling](http://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-microsd-card)
- [The Best microSD Card - Kimber Streams](http://thewirecutter.com/reviews/best-microsd-card/)

# How to boot?

Insert SD card into a slot and power the board. First boot takes around 3 minutes then it reboots and you will need to wait another one minute to login. This delay is because system updates package list and creates 128Mb emergency SWAP on the SD card.

Normal boot (with DHCP) takes up to 35 seconds with a class 6 SD CARD and cheapest board.

# How to login? 

Login as **root** on console or via SSH and use password **1234**. You will be prompted to change this password at first login. You will then be asked to create a normal user account that is sudo enabled (beware of default QWERTY keyboard settings at this stage).

Desktop images starts into desktop without asking for password. To change this add some display manager:

	apt-get install lightdm

... or edit the contents of file:

	/etc/default/nodm

and change the autologin user.

# How to update?

	apt-get update
	apt-get upgrade

**Update process can take hours in case of using cheap SD card and/or under heavy load.**

This will not only update distribution packages (Debian/Ubuntu) but also updates Armbian kernel, u-boot and board support package if available. So if you've seen in the list of updated packages the names _u-boot_ or _linux_ the following command is required for changes to take effect:

	reboot

# How to add users?

To create a normal user do this:

	adduser MyNewUsername

Put user to sudo group:

	usermod -aG sudo MyNewUsername

# How to install to eMMC, NAND, SATA & USB?

[su_youtube_advanced url="https:\/\/youtu.be\/6So8MA-qru8" controls="yes" showinfo="no" loop="yes" rel="no" modestbranding="yes"]

Required condition:

NAND:

 * kernel 3.4.x and NAND storage
 * pre-installed system on NAND (stock Android or other Linux)

eMMC/SATA/USB:

 * any kernel
 * onboard eMMC storage or permanently attached SATA or USB storage

Start the install script: 

	nand-sata-install

and follow the guide. You can create up to three scenarios:

 * boot from SD, system on SATA / USB
 * boot from eMMC / NAND, system on eMMC/NAND
 * boot from eMMC / NAND, system on SATA / USB

# How to set fixed IP?

By default your main network adapter's IP is assigned by your router DHCP server.

	iface eth0 inet dhcp 

change to - for example:

	iface eth0 inet static
	 	address 192.168.1.100
        netmask 255.255.255.0
		gateway 192.168.1.1