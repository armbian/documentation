---
title: "phpMyAdmin"
description: "Install and run phpMyAdmin on Armbian — phpMyAdmin web interface manager. Runs on ARM64 and x86 single-board computers."
image: /images/MYA001.png
category: "Database"
comments: true
---
# phpMyAdmin


phpMyAdmin web interface manager


<!--- section image START from tools/include/images/MYA001.png --->
![phpMyAdmin](/images/MYA001.png){ .app-logo }
<!--- section image STOP from tools/include/images/MYA001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://www.phpmyadmin.net/docs/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8071`


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Database → phpMyAdmin**

~~~ custombash title="CLI install"
armbian-config --cmd MYA001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_phpmyadmin install` |
| phpMyAdmin remove | `armbian-config --api module_phpmyadmin remove` |
| phpMyAdmin purge with data folder | `armbian-config --api module_phpmyadmin purge` |
| Status | `armbian-config --api module_phpmyadmin status` |
| Help | `armbian-config --api module_phpmyadmin help` |

---

_Part of Armbian's [SQL database servers and web interface managers](/User-Guide_Armbian-Software/Database/) software._
