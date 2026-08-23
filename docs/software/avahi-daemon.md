---
title: "avahi-daemon"
description: "Install and run avahi-daemon on Armbian — avahi-daemon hostname broadcast via mDNS. Runs on ARM64 and x86 single-board computers."
image: /images/AVH001.png
category: "Netconfig"
comments: true
---
# avahi-daemon


avahi-daemon hostname broadcast via mDNS


<!--- section image START from tools/include/images/AVH001.png --->
![avahi-daemon](/images/AVH001.png){ .app-logo }
<!--- section image STOP from tools/include/images/AVH001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://netbox.readthedocs.io/en/stable/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8222`


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Netconfig → avahi-daemon**

~~~ custombash title="avahi-daemon hostname broadcast via mDNS"
armbian-config --cmd AVH001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_netbox install` |
| Remove | `armbian-config --api module_netbox remove` |
| Purge | `armbian-config --api module_netbox purge` |
| Status | `armbian-config --api module_netbox status` |
| Help | `armbian-config --api module_netbox help` |

---

_Part of Armbian's [Console network tools for measuring load and bandwidth](/User-Guide_Armbian-Software/Netconfig/) software._
