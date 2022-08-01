# Advanced Features

## How to switch kernels?

Check [_this_](https://www.armbian.com/kernel/) for more info.

## How to troubleshoot?
## How to unbrick the system?

Both of above headings have been moved to a new page and expanded upon: [Recovery](User-Guide_Recovery.md)

## How to build a wireless driver?

Install and recreate kernel headers scripts (optional)

	armbian-config -> install kernel headers
	exit

	cd /usr/src/linux-headers-$(uname -r)
	make scripts

Go back to root directory and fetch sources (working example, use `ARCH=arm64` on 64bit system)

	cd
	git clone https://github.com/pvaret/rtl8192cu-fixes.git
	cd rtl8192cu-fixes
	make ARCH=arm

Load driver for test

	insmod 8192cu.ko

Check `dmesg` and the last entry will be:

	usbcore: registered new interface driver rtl8192cu

Plug the USB wireless adaptor and issue a command:

	iwconfig wlan0

You should see this:

	wlan0   unassociated  Nickname:"<WIFI@REALTEK>"
			Mode:Auto  Frequency=2.412 GHz  Access Point: Not-Associated
			Sensitivity:0/0
			Retry:off   RTS thr:off   Fragment thr:off
			Encryption key:off
			Power Management:off
			Link Quality=0/100  Signal level=0 dBm  Noise level=0 dBm
			Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
			Tx excessive retries:0  Invalid misc:0   Missed beacon:0

Check which wireless stations / routers are in range

	iwlist wlan0 scan | grep ESSID

## How to run Docker?

Docker works reliably with the distribution-provided builds of docker. It's as simple as `apt-get install docker.io`. If you prefer to use the latest docker builds provided directly by Docker. Please follow the guide below.

Preinstallation requirements:

- Armbian 20.08.17 or newer with Kernel 3.10 or higher
- Debian Buster (might work elsewhere with some modifications)
- root access

This method is based on Docker Debian installation [documentation](https://docs.docker.com/engine/install/debian/). Execute this as root:

```bash
apt-get remove docker docker-engine docker.io containerd runc
apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
add-apt-repository "deb [arch=arm64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
apt update
apt-get install docker-ce docker-ce-cli containerd.io
```

Test if Docker works correctly:

```bash
docker run hello-world
```

If you get that kind of output, then Docker install went fine:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

If you would like to use Docker as a non-root user, you should now consider adding your user to the `docker` group with something like:

```bash
usermod -aG docker your-user
```

You will have to log out, and log in once more in order to be able to run Docker without being root.

Let's try a last test to see if a Docker container can be seen outside of your Armbian machine:

```bash
docker run -d -p 80:80 hypriot/rpi-busybox-httpd
```

... and point the browser of any device in the same network to `http://<IP OF YOUR DEVICE>/`

[More info in this forum topic](https://forum.armbian.com/topic/490-docker-on-armbian/)

## How to set wireless access point?

There are two different HostAP daemons. One is **default** and the other one is for some **Realtek** wifi cards. Both have their own basic configurations and both are patched to gain maximum performances.

Sources: [https://github.com/igorpecovnik/hostapd](https://github.com/igorpecovnik/hostapd "https://github.com/igorpecovnik/hostapd")

Default binary and configuration location:

	/usr/sbin/hostapd
	/etc/hostapd.conf

Realtek binary and configuration location:

	/usr/sbin/hostapd-rt
	/etc/hostapd.conf-rt

Since its hard to define when to use which you always try both combinations in case of troubles. To start AP automatically:

1. Edit /etc/init.d/hostapd and add/alter location of your conf file **DAEMON_CONF=/etc/hostapd.conf** and binary **DAEMON_SBIN=/usr/sbin/hostapd**
2. Copy **/etc/network/interfaces.hostapd** to **/etc/network/interfaces**
3. Reboot
4. Predefined network name: "BOARD NAME" password: 12345678
5. To change parameters, edit /etc/hostapd.conf BTW: You can get WPAPSK the long blob from wpa_passphrase YOURNAME YOURPASS

## How to connect IR remote?

Required conditions:

- IR hardware
- loaded driver

Get your [remote configuration](http://lirc.sourceforge.net/remotes/) (lircd.conf) or [learn](https://kodi.wiki/view/HOW-TO:Setup_Lirc#Learning_Commands).

- Note: As of 2020-11-25, the above (Kodi / learn) link is broken.  However I am not sure what to replace it with.  If you know (or find out) please [submit a PR](/Process_Contribute/).  - TRS-80

You are going to need the list of all possible commands which you can map to your IR remote keys:

	irrecord --list-namespace

To start with learning process you need to delete old config:

	rm /etc/lircd.conf

Then start the process with:

	irrecord --driver=default --device=/dev/lirc0 /etc/lircd.conf

And finally start your service when done with learning:

	service lirc start

Test your remote:

	irw /dev/lircd

## Outdated

### How to freeze your filesystem? (outdated)

In certain situations it is desirable to have a virtual read-only root filesystem. This prevents any changes from occurring on the root filesystem that may alter system behavior and it allows a simple reboot to restore a system to its clean state.

You need an ODROID XU4 or Allwinner A10, A20 or H3 board with legacy kernel where we added support for overlayfs. Works only on Ubuntu Xenial. Login as root and execute:

	apt-get install overlayroot
	echo 'overlayroot="tmpfs"' >> /etc/overlayroot.conf
	reboot

After your system boots up it will always remain as is. If you want to make any permanent changes, you need to run:

	overlayroot-chroot

Changes inside this will be preserved.

