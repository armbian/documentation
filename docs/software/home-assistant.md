---
title: "Home Assistant"
description: "Install and run Home Assistant on Armbian — Home Assistant open source home automation. Runs on ARM64 and x86 single-board computers."
image: /images/HAS001.png
category: "HomeAutomation"
comments: true
---
# Home Assistant


<!--- section image START from tools/include/images/HAS001.png --->
![Home Assistant](/images/HAS001.png)
<!--- section image STOP from tools/include/images/HAS001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/home-assistant/supervised-installer) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8123`


<!--- header START from tools/include/markdown/HAS001-header.md --->
Home Assistant is an open source smart home platform that allows you to connect your smart home devices like your TV, fan, cameras, thermostats, lights, and sensors. As a user, you can build intricate automation using Home Assistant's user-friendly, unified web-based user interface.

Perfect to run on any single board computer with 4 cores and at least 512Mb of memory. Armbian installation is optimised to run from SD/eMMC media, but it is recommended to use SSD.

!!! danger "Limited support"

    The supervised installation method on Armbian is not officially supported by the [Home Assistant project](https://www.home-assistant.io/installation/alternative#install-home-assistant-supervised). Additionally, installation on hardware that is not officially supported is also outside the scope of support provided by the Armbian team.

    You are welcome to report high-level application issues that are reproducible on the official Home Assistant Operating System (HAOS) within the [Home Assistant Community](https://community.home-assistant.io/). For any topics related to single-board computer hardware, you may use the [Armbian Community Forums](https://forum.armbian.com); however, please be aware that official support from the Armbian team is not guaranteed.

    While the Home Assistant team [deprecated the Supervised installation method](https://community.home-assistant.io/t/feedback-requested-deprecating-core-supervised-i386-armhf-armv7/880968/312), the Armbian team will continue to provide and maintain it, as long as automated installation tests succeed and the required maintenance remains manageable.

<!--- header STOP from tools/include/markdown/HAS001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Home Automation → Home Assistant**

~~~ custombash title="CLI install"
armbian-config --cmd HAS001
~~~


<!--- footer START from tools/include/markdown/HAS001-footer.md --->
=== "Access to the web interface"

    - Username/Password: Are set at first web interface login

=== "Directories"

    Home Assistant on Armbian runs supervised in a Docker container. This secures same functionality as stock HAOS.

    - Config directory: `/armbian/haos`

=== "Armbian advantages"

    |Functionality|HAOS|Armbian with HA|
    |:--|:--:|:--:|
    |Automations|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
    |Dashboards|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
    |Integrations|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
    |Add-ons|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
    |One-click updates|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
    |Backups|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
    |General purpose server|:x:|:white_check_mark:|
    |Running on exotic hardware|:x:|:white_check_mark:|

<!--- footer STOP from tools/include/markdown/HAS001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_haos install` |
| Home Assistant remove | `armbian-config --api module_haos remove` |
| Home Assistant purge with data folder | `armbian-config --api module_haos purge` |
| Status | `armbian-config --api module_haos status` |
| Help | `armbian-config --api module_haos help` |

---

_Part of Armbian's [Home Automation for control home appliances](/User-Guide_Armbian-Software/HomeAutomation/) software._
