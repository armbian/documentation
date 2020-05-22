**Preparation**

Make sure you have a **good & reliable** SD card and a **proper power supply**. Archives can be uncompressed with [7-Zip](http://www.7-zip.org/) on Windows, [Keka](http://www.kekaosx.com/en/) on OS X and 7z on Linux (apt-get install p7zip-full). RAW images should be written with an approved imaging tool capable of validating the burn.

**Approved Imaging Tools**

* [USBImager](https://gitlab.com/bztsrc/usbimager) a lightweight cross-platform imaging tool 
* [Balena Etcher](https://www.balena.io/etcher/) an electron / node.js based cross-platform imaging tool (may contain spyware)

**Boot**

Insert SD card into a slot and power the board. (First) boot (with DHCP) takes up to 35 seconds with a class 10 SD Card and cheapest board.

**Login**

Login as **root** on HDMI / serial console or via SSH and use password **1234**. You will be prompted to change this password at first login. Next you will be asked to create a normal user account that is sudo enabled (beware of default QWERTY keyboard settings at this stage).
