---
title: "EVCC"
description: "Install and run EVCC on Armbian — solar charging automation. Runs on ARM64 and x86 single-board computers."
image: /images/EVCC01.png
category: "HomeAutomation"
comments: true
---
# EVCC


<!--- section image START from tools/include/images/EVCC01.png --->
![EVCC](/images/EVCC01.png){ .app-logo }
<!--- section image STOP from tools/include/images/EVCC01.png --->


<span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.evcc.io/en) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:7070`


<!--- header START from tools/include/markdown/EVCC01-header.md --->
evcc is an energy management system with a focus on electromobility. The software controls your EV charger or smart plug. It communicates with your vehicle, inverter or home storage to make intelligent charging decisions. The software is open source and community-driven.

<!--- header STOP from tools/include/markdown/EVCC01-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Home Automation → EVCC**

~~~ custombash title="CLI install"
armbian-config --cmd EVCC01
~~~


<!--- footer START from tools/include/markdown/EVCC01-footer.md --->
=== "Access to the web interface"

    - Admin password is generated at first web interface login

=== "Directories"

    - Install directory: `/armbian/evcc`
    - Site configuration directory: `/armbian/evcc/evcc.yaml`

=== "View logs"

    ```sh
    docker logs -f evcc
    ```

<!--- footer STOP from tools/include/markdown/EVCC01-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_evcc install` |
| EVCC - solar charging automation remove | `armbian-config --api module_evcc remove` |
| EVCC purge with data folder | `armbian-config --api module_evcc purge` |
| Status | `armbian-config --api module_evcc status` |
| Help | `armbian-config --api module_evcc help` |

---

_Part of Armbian's [Home Automation for control home appliances](/User-Guide_Armbian-Software/HomeAutomation/) software._
