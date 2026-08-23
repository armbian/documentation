---
title: "Domoticz"
description: "Install and run Domoticz on Armbian — Domoticz open source home automation. Runs on ARM64 and x86 single-board computers."
image: /images/DOM001.png
category: "HomeAutomation"
comments: true
---
# Domoticz


<!--- section image START from tools/include/images/DOM001.png --->
![Domoticz](/images/DOM001.png)
<!--- section image STOP from tools/include/images/DOM001.png --->


<span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://wiki.domoticz.com) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8780`


<!--- header START from tools/include/markdown/DOM001-header.md --->
Domoticz is an open-source home automation platform that allows you to control and monitor smart devices in your home. It supports a wide range of devices, including lights, sensors, thermostats, and cameras. Through its web interface or mobile app, you can set up automation rules and schedules, providing greater convenience and energy efficiency. It’s customizable, flexible, and can be run on a variety of hardware platforms supported by Armbian.

=== "Access to the web interface"

    - Username/Password: admin / domoticz

=== "Directories"

    - Config directory: `/armbian/domoticz`

=== "Advanced setup"

    - Primary USB device passing through (`/dev/ttyUSB0`) to Docker container is enabled by default
    - For more complex setup, please follow this comprehensive guide: <https://wiki.domoticz.com/Main_Page>

<!--- header STOP from tools/include/markdown/DOM001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Home Automation → Domoticz**

~~~ custombash title="CLI install"
armbian-config --cmd DOM001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_domoticz install` |
| Domoticz remove | `armbian-config --api module_domoticz remove` |
| Domoticz purge with data folder | `armbian-config --api module_domoticz purge` |
| Status | `armbian-config --api module_domoticz status` |
| Help | `armbian-config --api module_domoticz help` |

---

_Part of Armbian's [Home Automation for control home appliances](/User-Guide_Armbian-Software/HomeAutomation/) software._
