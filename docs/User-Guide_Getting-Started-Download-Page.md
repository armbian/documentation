**Preparation**

Make sure you have a **good & reliable** SD card and a **proper power supply**. The XZ-compressed  should be written with an approved imaging tool capable of validating the burn.

**Approved Imaging Tools**

* [USBImager](https://gitlab.com/bztsrc/usbimager) a lightweight cross-platform imaging tool 
* [Balena Etcher](https://www.balena.io/etcher/) an electron / node.js based cross-platform imaging tool [(may contain spyware)](https://github.com/balena-io/etcher/issues?q=is%3Aissue+spyware)

**Boot**

Insert SD card into a slot and power the board. (First) boot (with DHCP) takes up to 35 seconds with a class 10 SD Card and cheapest board.

**Login**

Login as **root** on HDMI / serial console or via SSH and use password **1234**. You will be prompted to change this password at first login. Next you will be asked to create a normal user account that is sudo enabled (beware of default QWERTY keyboard settings at this stage).
