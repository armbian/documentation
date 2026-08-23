---
title: "Portainer"
description: "Install and run Portainer on Armbian — Portainer container management platform. Runs on ARM64 and x86 single-board computers."
image: /images/POR001.png
category: "Containers"
comments: true
---
# Portainer


<!--- section image START from tools/include/images/POR001.png --->
![Portainer](/images/POR001.png){ .app-logo }
<!--- section image STOP from tools/include/images/POR001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.portainer.io/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:9000`


<!--- header START from tools/include/markdown/POR001-header.md --->
Portainer simplifies your Docker container management via Portainer web interface. It enables faster deploy of the applications and it gives real time visibility.

<!--- header STOP from tools/include/markdown/POR001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Containers → Portainer**

~~~ custombash title="CLI install"
armbian-config --cmd POR001
~~~


<!--- footer START from tools/include/markdown/POR001-footer.md --->


<!--- footer STOP from tools/include/markdown/POR001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_portainer install` |
| Portainer purge with with data folder | `armbian-config --api module_portainer remove` |
| Purge | `armbian-config --api module_portainer purge` |
| Status | `armbian-config --api module_portainer status` |
| Help | `armbian-config --api module_portainer help` |

---

_Part of Armbian's [Docker containerization and KVM virtual machines](/User-Guide_Armbian-Software/Containers/) software._
