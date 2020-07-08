# Armbian configuration utility #

![](https://raw.githubusercontent.com/armbian/config/master/images/animated-888.gif)

Is a base utility for configuring your board, divided into four main sections:

- **S**ystem - system and security settings,
- **N**etwork - wired, wireless, Bluetooth, access point,
- **P**ersonal - timezone, language, hostname,
- **S**oftware - system and 3rd party software install.

The tool needs root privileges to work and can be launched by entering ```sudo armbian-config``` at the terminal prompt or by clicking to the armbian-config menu item on desktop images.

## System ##

- **I**nstall - installs to SATA, eMMC, NAND or USB. It gives you an option to install the system to more resilient and faster internal or external media. You can also change filesystem type to ext2,3,4 or BTRFS (if supported),
- **F**reeze - freeze or unfreeze kernel and board support packages, to avoid upgrading,
- **N**ightly - switch between nightly automated beta and stable builds,
- **B**ootenv - edit boot environment and alter kernel boot parameters,
- **H**ardware - toggle board low level functions: UART, I2C, SPI, ...
- **S**witch - switch to/between alternative kernels: legacy, current, dev
- **S**SH - reconfigure SSH daemon. Permit root login, toggle ssh key and mobile phone authentication,
- **F**irmware - execute apt update and upgrade to update your system,
- **Z**shell - toogle stock BASH and ZSH with [Oh My ZSH](https://ohmyz.sh/) and [tmux](https://en.wikipedia.org/wiki/Tmux)
- **E**nable - toggle desktop on and off (on desktop images)
- **L**ightdm - change login managers from none to lightdm (on desktop images)
- **R**DP - toggle remote desktop from Windows (on desktop images)
- **O**verlayroot - toggle overlayroot (Ubuntu images)
- **M**inimal - install minimal Armbian XFCE powered desktop,
- **D**efault - install Armbian XFCE powered desktop with web browser and extras.

## Network  ##


- **I**P - choose to select dynamic or edit static IP address,
- **H**otspot - create or manage wireless access point. If your wireless adapter is recognized by a kernel, then armbian-config utility auto selects best mode on the selected device. It can detect 802.11n, 802.11a and 802.11ac. It also knows how to handle some special Realtek adapters,
- **I**PV6 - toggle IPV6 for apt and system,
- **I**perf3 - toogle network troughput tests daemon,
- **L**TE - 3G/4G LTE modem management
- **W**iFi - manage wireless networking. Connect with Wifi network. You can create multiple wireless connections at the same time. They are managed by Network Manager,
- **B**T install - pair Bluetooth devices without PIN code,
- **A**dvanced - edit network config manually,
- **F**orget - disconnets and clear all wireless connections.

## Personal settings ##

- **T**imezone - change timezone,
- **L**ocales - reconfigure language and character set,
- **K**eyboard - change console keyboaard settings,
- **H**ostname - change hostname,
- **M**irror - change to backup APT repository mirror in case of troubles,
- **W**elcome - toggle welcome screen items.

## Software ##

Software installation menu provides automated install of the following packages.

- **s**ofty
	- [TV headend](https://tvheadend.org/) *(IPTV server)*
	- [Syncthing](https://syncthing.net/) *(personal cloud)*
	- [SoftEther VPN server](https://www.softether.org/) *(VPN server)*
	- [Plex](https://www.plex.tv/) *(Plex media server)*
	- [Radarr](https://radarr.video/) *(Movie downloading server)*
	- [Sonarr](https://sonarr.tv/) *(TV shows downloading server)*
	- [Transmission](https://transmissionbt.com/) *(torrent server)*
	- [ISPConfig](https://www.ispconfig.org/) *(WEB & MAIL server)*
	- [NCP](https://nextcloudpi.com) *(Nextcloud personal cloud)*
	- [Openmediavault NAS](http://www.openmediavault.org/) *(NAS server)*
	- [PI hole](https://pi-hole.net) *(ad blocker)*
	- [UrBackup](https://www.urbackup.org/) *(client/server backup system)*
	- [Docker](https://www.docker.com) *(Docker CE engine)*
	- [Mayan EDMS](https://www.mayan-edms.com/) *(Document management system within Docker)*
	- [MiniDLNA](http://minidlna.sourceforge.net/) *(media sharing)*
- **M**onitor = simple CLI monitoring 
- **D**iagnostics = create a summary of logs and upload them to paste.bin
- **T**oggle kernel headers, RDP service, Thunderbird and Libreoffice (desktop builds)


## Sources ##

[https://github.com/armbian/config](https://github.com/armbian/config)
