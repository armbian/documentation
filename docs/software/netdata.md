---
title: "Netdata"
description: "Install and run Netdata on Armbian — monitoring real-time metrics. Runs on ARM64 and x86 single-board computers."
image: /images/NTD001.png
category: "Monitoring"
comments: true
---
# Netdata


<!--- section image START from tools/include/images/NTD001.png --->
![Netdata](/images/NTD001.png){ .app-logo }
<!--- section image STOP from tools/include/images/NTD001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://learn.netdata.cloud/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:19999`


<!--- header START from tools/include/markdown/NTD001-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/NTD001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Monitoring → Netdata**

~~~ custombash title="CLI install"
armbian-config --cmd NTD001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_netdata install` |
| Netdata remove | `armbian-config --api module_netdata remove` |
| Netdata purge with data folder | `armbian-config --api module_netdata purge` |
| Status | `armbian-config --api module_netdata status` |
| Help | `armbian-config --api module_netdata help` |

---

_Part of Armbian's [Real-time monitoring, collecting metrics, up-time status](/User-Guide_Armbian-Software/Monitoring/) software._
