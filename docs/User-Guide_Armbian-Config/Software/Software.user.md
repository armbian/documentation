# Run/Install 3rd party applications


***

## Desktop Environments


***

### XFCE desktop


***

#### XFCE desktop Install
Install XFCE:
Xfce is a lightweight desktop environment for UNIX-like operating systems. It aims to be fast and low on system resources, while still being visually appealing and user friendly.

**Command:** 
~~~
armbian-config --cmd DE01
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Uninstall
**Command:** 
~~~
armbian-config --cmd DE02
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Enable autologin
**Command:** 
~~~
armbian-config --cmd DE03
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Disable autologin
**Command:** 
~~~
armbian-config --cmd DE04
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Gnome desktop


***

#### Gnome desktop Install
**Command:** 
~~~
armbian-config --cmd DE11
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Uninstall
**Command:** 
~~~
armbian-config --cmd DE12
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Enable autologin
**Command:** 
~~~
armbian-config --cmd DE13
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Disable autologin
**Command:** 
~~~
armbian-config --cmd DE14
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### i3-wm desktop
**Status:** Disabled



***

#### i3 desktop Install
**Command:** 
~~~
armbian-config --cmd DE21
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### i3 desktop uninstall
**Command:** 
~~~
armbian-config --cmd DE22
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Enable autologin
**Command:** 
~~~
armbian-config --cmd DE23
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Disable autologin
**Command:** 
~~~
armbian-config --cmd DE24
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Cinnamon desktop


***

#### Cinnamon desktop Install

<!--- section image START from tools/include/images/DE31.png --->
[![Cinnamon desktop Install](images/DE31.png)](#)
<!--- section image STOP from tools/include/images/DE31.png --->

**Command:** 
~~~
armbian-config --cmd DE31
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/DE31-footer.md --->
Cinnamon is a Linux desktop that provides advanced innovative features and a traditional user experience.The desktop layout is similar to Gnome 2 with underlying technology forked from Gnome Shell. Cinnamon makes users feel at home with an easy-to-use and comfortable desktop experience.
<!--- footer STOP from tools/include/markdown/DE31-header.md --->



***

#### Cinnamon desktop uninstall
**Command:** 
~~~
armbian-config --cmd DE32
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Enable autologin
**Command:** 
~~~
armbian-config --cmd DE33
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Disable autologin
**Command:** 
~~~
armbian-config --cmd DE34
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Kde-neon desktop
**Status:** Disabled



***

#### Kde-neon desktop Install
**Command:** 
~~~
armbian-config --cmd DE41
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Uninstall
**Command:** 
~~~
armbian-config --cmd DE42
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Enable autologin
**Command:** 
~~~
armbian-config --cmd DE43
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Disable autologin
**Command:** 
~~~
armbian-config --cmd DE44
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Improve application search speed
**Command:** 
~~~
armbian-config --cmd DE99
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Network tools


***

### Install realtime console network usage monitor (nload)
**Command:** 
~~~
armbian-config --cmd SW08
~~~

**Author:** 

**Status:** Preview



***

### Remove realtime console network usage monitor (nload)
**Command:** 
~~~
armbian-config --cmd SW09
~~~

**Author:** 

**Status:** Preview



***

### Install bandwidth measuring tool (iperf3)
**Command:** 
~~~
armbian-config --cmd SW10
~~~

**Author:** 

**Status:** Preview



***

### Remove bandwidth measuring tool (iperf3)
**Command:** 
~~~
armbian-config --cmd SW11
~~~

**Author:** 

**Status:** Preview



***

### Install IP LAN monitor (iptraf-ng)
**Command:** 
~~~
armbian-config --cmd SW12
~~~

**Author:** 

**Status:** Preview



***

### Remove IP LAN monitor (iptraf-ng)
**Command:** 
~~~
armbian-config --cmd SW13
~~~

**Author:** 

**Status:** Preview



***

### Install hostname broadcast via mDNS (avahi-daemon)
**Command:** 
~~~
armbian-config --cmd SW14
~~~

**Author:** 

**Status:** Preview



***

### Remove hostname broadcast via mDNS (avahi-daemon)
**Command:** 
~~~
armbian-config --cmd SW15
~~~

**Author:** 

**Status:** Preview



***

## Development


***

### Install tools for cloning and managing repositories (git)
**Command:** 
~~~
armbian-config --cmd SW17
~~~

**Author:** 

**Status:** Preview



***

### Remove tools for cloning and managing repositories (git)
**Command:** 
~~~
armbian-config --cmd SW18
~~~

**Author:** 

**Status:** Preview



***

## System benchmaking and diagnostics
**Command:** 
~~~
armbian-config --cmd Benchy
~~~

**Author:** 

**Status:** Preview



***

## Containerlization and Virtual Machines


***

### Install Docker Minimal
This operation will install Docker Minimal.

**Command:** 
~~~
armbian-config --cmd SW25
~~~

**Author:** 

**Status:** Preview



***

### Install Docker Engine
This operation will install Docker Engine.

**Command:** 
~~~
armbian-config --cmd SW26
~~~

**Author:** 

**Status:** Preview



***

### Remove Docker
This operation will purge Docker.

**Command:** 
~~~
armbian-config --cmd SW27
~~~

**Author:** 

**Status:** Preview



***

### Purge all Docker images, containers, and volumes
This operation will delete all Docker images, containers, and volumes.

**Command:** 
~~~
armbian-config --cmd SW28
~~~

**Author:** 

**Status:** Preview



***

## Media Servers and Editors


***

### Install Plex Media server
This operation will install Plex Media server.

**Command:** 
~~~
armbian-config --cmd SW21
~~~

**Author:** 

**Status:** Preview



***

### Remove Plex Media server
This operation will purge Plex Media server.

**Command:** 
~~~
armbian-config --cmd SW22
~~~

**Author:** 

**Status:** Preview



***

### Install Emby server
This operation will install Emby server.

**Command:** 
~~~
armbian-config --cmd SW23
~~~

**Author:** 

**Status:** Preview



***

### Remove Emby server
This operation will purge Emby server.

**Command:** 
~~~
armbian-config --cmd SW24
~~~

**Author:** 

**Status:** Preview



***

## Remote Management tools


***

### Install Cockpit web-based management tool
This operation will install Cockpit.
cockpit cockpit-ws cockpit-system cockpit-storaged

**Command:** 
~~~
armbian-config --cmd M00
~~~

**Author:** 

**Status:** Preview



***

### Purge Cockpit web-based management tool
This operation will purge Cockpit.

**Command:** 
~~~
armbian-config --cmd M01
~~~

**Author:** 

**Status:** Preview



***

### Start Cockpit Service
**Command:** 
~~~
armbian-config --cmd M02
~~~

**Author:** 

**Status:** Preview



***

### Stop Cockpit Service
**Command:** 
~~~
armbian-config --cmd M03
~~~

**Author:** 

**Status:** Preview



***

