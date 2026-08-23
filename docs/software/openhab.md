---
title: "openHAB"
description: "Install and run openHAB on Armbian — openHAB empowering the smart home. Runs on ARM64 and x86 single-board computers."
image: /images/HAB001.png
category: "HomeAutomation"
comments: true
---
# openHAB


openHAB empowering the smart home


<!--- section image START from tools/include/images/HAB001.png --->
![openHAB](/images/HAB001.png){ .app-logo }
<!--- section image STOP from tools/include/images/HAB001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://www.openhab.org/docs/tutorial) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:2080`


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Home Automation → openHAB**

~~~ custombash title="CLI install"
armbian-config --cmd HAB001
~~~


<!--- footer START from tools/include/markdown/HAB001-footer.md --->
=== "Access to the web interface"

    - Username/Password: Are set at first web interface login

=== "Directories"

    - Install directory: `/armbian/openhab`
    - Site configuration directory: `/armbian/openhab/conf`
    - Userdata directory: `/armbian/openhab/userdata`
    - Addons directory: `/armbian/openhab/addons`

    See also [openHAB file locations](https://www.openhab.org/docs/installation/linux.html#file-locations).

=== "View logs"

    ```sh
    docker logs -f openhab
    ```

<!--- footer STOP from tools/include/markdown/HAB001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_openhab install` |
| openHAB remove | `armbian-config --api module_openhab remove` |
| openHAB purge with data folder | `armbian-config --api module_openhab purge` |
| Status | `armbian-config --api module_openhab status` |
| Help | `armbian-config --api module_openhab help` |

---

_Part of Armbian's [Home Automation for control home appliances](/User-Guide_Armbian-Software/HomeAutomation/) software._
