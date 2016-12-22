# Prerequisites for new users

Please, make sure you have:

- a proper power supply according to the board manufacturer requirements (basic usage example: 5V/2A with DC Jack barrel OR thick USB cable)
- a reliable SD card (see below "How to prepare a SD card?")

# How to prepare a SD card?

**Important note:** Make sure you use a **good & reliable** SD card. If you encounter boot or stability troubles in over 95 percent of the time it's either insufficient power supply or related to SD card (bad card, bad card reader, something went wrong when burning the image). Armbian can simply not run on unreliable hardware so checking your SD card with either [F3](http://oss.digirati.com.br/f3/) or [H2testw](http://www.heise.de/download/h2testw.html) is mandatory if you run in problems. Since [counterfeit SD cards](http://www.happybison.com/reviews/how-to-check-and-spot-fake-micro-sd-card-8/) are still an issue checking with F3/H2testw directly after purchase is **highly recommended**.

7z and zip archives can be uncompressed with [7-Zip](http://www.7-zip.org/) on Windows, [Keka](http://www.kekaosx.com/en/) on OS X and 7z on Linux (apt-get install p7zip-full). Raw images can be written with [Etcher](https://www.etcher.io) (all OS):

	# Linux example: /dev/sdx is your sd card device
	sudo dd bs=1M if=filename.img of=/dev/sdx
	sync
	# OS X example: /dev/[r]diskx is your sd card device:
	diskutil unmountDisk diskx && dd bs=1m if=filename.img of=/dev/rdiskx && diskutil eject diskx

Image writing takes up to 2 minutes on a good SD card.

Also important: SD cards are optimised for sequential reads/writes as it's common in digital cameras. This is what the *speed class* is about. And while you shouldn't buy or use any card rated less than *class 10* you should especially take care to choose one that is known to show high random I/O performance since this is way more performance relevant when used with any SBC. Even cards advertised as being 'high speed' can show horribly low random IO performance in reality.

You won't be wrong picking one of these:

[![Samsung EVO 16GB UHS-I](http://www.armbian.com/wp-content/uploads/2016/03/sdcard-samsung-1.png)](http://www.amazon.com/dp/B00IVPU7KE)
[![Transcend Ultimate 16 GB UHS-I](http://www.armbian.com/wp-content/uploads/2016/03/sdcard-transcend-1.png)](http://www.amazon.com/gp/product/B00BLHWYWS)
[![SanDisk Extreme Pro 16 GB UHS-I](http://www.armbian.com/wp-content/uploads/2016/03/sdcard-sandisk-1.png)](http://www.amazon.com/dp/B008HK1YAA)

Detailed information regarding SD card performance:

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

# How to connect to wireless?

Required condition: a board with onboard or supported 3rd party wireless adapter on USB

If you know what is your wireless SSID:

	nmtui-connect SSID

![](https://www.armbian.com/wp-content/uploads/2016/12/wifi-1.png)

If you don't know, you can browse and then connect

	nmtui-connect

![](https://www.armbian.com/wp-content/uploads/2016/12/wifi-2.png)
