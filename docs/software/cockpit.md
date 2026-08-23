---
title: "Cockpit"
description: "Install and run Cockpit on Armbian — Cockpit OS and VM management tool. Runs on ARM64 and x86 single-board computers."
image: /images/CPT001.png
category: "Management"
comments: true
---
# Cockpit


<!--- section image START from tools/include/images/CPT001.png --->
![Cockpit](/images/CPT001.png){ .app-logo }
<!--- section image STOP from tools/include/images/CPT001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://cockpit-project.org/guide/latest/) · :material-lan-connect:{ title="Access port" } `https://<your.IP>:9890`


<!--- header START from tools/include/markdown/CPT001-header.md --->
Cockpit is a web-based graphical interface for servers, intended for everyone.

Here’s a subset of tasks you can perform on each host running Cockpit

- inspect and change network settings
- configure a firewall
- manage storage (including RAID and LUKS partitions)
- create and manage virtual machines
- download and run containers
- browse and search system logs
- inspect a system’s hardware
- upgrade software
- manage user accounts
- inspect and interact with systemd-based services
- use a terminal on a remote server in your local web browser
- switch between multiple Cockpit servers

<!--- header STOP from tools/include/markdown/CPT001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Management → Cockpit**

~~~ custombash title="CLI install"
armbian-config --cmd CPT001
~~~


<!--- footer START from tools/include/markdown/CPT001-footer.md --->
=== "Access to the web interface"

    - Username/Password: your system login credentials

=== "Video instructions"

    <iframe width="1200" height="676" src="https://www.youtube.com/embed/L9fMWCRcqIE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!--- footer STOP from tools/include/markdown/CPT001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_cockpit install` |
| Remove Cockpit | `armbian-config --api module_cockpit remove` |
| Purge Cockpit with virtual machines | `armbian-config --api module_cockpit purge` |
| Status | `armbian-config --api module_cockpit status` |
| Help | `armbian-config --api module_cockpit help` |

---

_Part of Armbian's [Remote File & Management tools](/User-Guide_Armbian-Software/Management/) software._
