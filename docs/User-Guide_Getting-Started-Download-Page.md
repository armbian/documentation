# Preparation

Make sure you have a **good & reliable** SD card and a **proper power supply**. Archives can be uncompressed with [7-Zip](http://www.7-zip.org/) on Windows, [Keka](http://www.kekaosx.com/en/) on OS X and 7z on Linux (apt-get install p7zip-full). RAW images can be written with [Etcher](https://www.etcher.io) (all OS).

# How to boot?

Insert SD card into a slot and power the board. First boot takes around 3 minutes then it might reboot and you will need to wait another one minute to login. This delay is because system creates 128Mb emergency SWAP and expand SD card to it's full capacity. Worst case scenario boot (with DHCP) takes up to 35 seconds.

# How to login? 

Login as **root** on HDMI / serial console or via SSH and use password **1234**. You will be prompted to change this password at first login. Next you will be asked to create a normal user account that is sudo enabled (beware of default QWERTY keyboard settings at this stage).

# How to connect to your router via WIFI?

Required condition: a board with onboard or supported 3rd party wireless adapter on USB

	nmtui-connect YOUR_ROUTER_SSID

![](https://www.armbian.com/wp-content/uploads/2016/12/wifi-tran.png)
