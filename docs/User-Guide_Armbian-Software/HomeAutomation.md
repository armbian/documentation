---
comments: true
---

# Home Automation for control home appliances

## Domoticz


Domoticz open source home automation


<!--- section image START from tools/include/images/DOM001.png --->
[![Domoticz](/images/DOM001.png)](#)
<!--- section image STOP from tools/include/images/DOM001.png --->


<!--- header START from tools/include/markdown/DOM001-header.md --->
Domoticz is an open-source home automation platform that allows you to control and monitor smart devices in your home. It supports a wide range of devices, including lights, sensors, thermostats, and cameras. Through its web interface or mobile app, you can set up automation rules and schedules, providing greater convenience and energy efficiency. It’s customizable, flexible, and can be run on a variety of hardware platforms supported by Armbian.

=== "Access to the web interface"

    The web interface is accessible via port **8780**:

    - URL: `https://<your.IP>:8780`
    - Username/Password: admin / domoticz

=== "Directories"

    - Config directory: `/armbian/domoticz`

=== "Advanced setup"

    - Primary USB device passing through (`/dev/ttyUSB0`) to Docker container is enabled by default
    - For more complex setup, please follow this comprehensive guide: <https://wiki.domoticz.com/Main_Page>

<!--- header STOP from tools/include/markdown/DOM001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/DOM001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DOM001-header.md)  
__Status:__ Preview  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://wiki.domoticz.com)  

~~~ custombash
armbian-config --cmd DOM001
~~~


~~~ bash title="Domoticz remove:"
armbian-config --cmd DOM002
~~~


~~~ bash title="Domoticz purge with data folder:"
armbian-config --cmd DOM003
~~~




## EVCC


EVCC - solar charging automation


<!--- section image START from tools/include/images/EVCC01.png --->
[![EVCC](/images/EVCC01.png)](#)
<!--- section image STOP from tools/include/images/EVCC01.png --->


<!--- header START from tools/include/markdown/EVCC01-header.md --->
evcc is an energy management system with a focus on electromobility. The software controls your EV charger or smart plug. It communicates with your vehicle, inverter or home storage to make intelligent charging decisions. The software is open source and community-driven.

<!--- header STOP from tools/include/markdown/EVCC01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/EVCC01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/EVCC01-header.md)  
__Status:__ Preview  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.evcc.io/en)  

~~~ custombash
armbian-config --cmd EVCC01
~~~


<!--- footer START from tools/include/markdown/EVCC01-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **7070**:

    - URL: `https://<your.IP>:7070`
    - Admin password is generated at first web interface login

=== "Directories"

    - Install directory: `/armbian/evcc`
    - Site configuration directory: `/armbian/evcc/evcc.yaml`

=== "View logs"

    ```sh
    docker logs -f evcc
    ```

<!--- footer STOP from tools/include/markdown/EVCC01-footer.md --->


~~~ bash title="EVCC - solar charging automation remove:"
armbian-config --cmd EVCC02
~~~


~~~ bash title="EVCC purge with data folder:"
armbian-config --cmd EVCC03
~~~




## openHAB


openHAB empowering the smart home


<!--- section image START from tools/include/images/HAB001.png --->
[![openHAB](/images/HAB001.png)](#)
<!--- section image STOP from tools/include/images/HAB001.png --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/HAB001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/HAB001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://www.openhab.org/docs/tutorial)  

~~~ custombash
armbian-config --cmd HAB001
~~~


<!--- footer START from tools/include/markdown/HAB001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8080**:

    - URL: `https://<your.IP>:8080`
    - Username/Password: Are set at first web interface login

=== "Directories"

    - Install directory: `/usr/share/openhab`
    - Site configuration directory: `/etc/openhab`
    - Config file: `/etc/default/openhab`
    - Data directory: `/var/lib/openhab`

    See also [openHAB file locations](https://www.openhab.org/docs/installation/linux.html#file-locations).

=== "View logs"

    ```sh
    journalctl -u openhab
    ```

<!--- footer STOP from tools/include/markdown/HAB001-footer.md --->


~~~ bash title="openHAB remove:"
armbian-config --cmd HAB002
~~~


~~~ bash title="openHAB purge with data folder:"
armbian-config --cmd HAB003
~~~




## Home Assistant


Home Assistant open source home automation


<!--- section image START from tools/include/images/HAS001.png --->
[![Home Assistant](/images/HAS001.png)](#)
<!--- section image STOP from tools/include/images/HAS001.png --->


<!--- header START from tools/include/markdown/HAS001-header.md --->
Home Assistant is an open source smart home platform that allows you to connect your smart home devices like your TV, fan, cameras, thermostats, lights, and sensors. As a user, you can build intricate automation using Home Assistant's user-friendly, unified web-based user interface.

Perfect to run on any single board computer with 4 cores and at least 512Mb of memory. Armbian installation is optimised to run from SD/eMMC media, but it is recommended to use SSD.

!!! danger "Limited support"

    The supervised installation method on Armbian is not officially supported by the [Home Assistant project](https://www.home-assistant.io/installation/alternative#install-home-assistant-supervised). Additionally, installation on hardware that is not officially supported is also outside the scope of support provided by the Armbian team.

    You are welcome to report high-level application issues that are reproducible on the official Home Assistant Operating System (HAOS) within the [Home Assistant Community](https://community.home-assistant.io/). For any topics related to single-board computer hardware, you may use the [Armbian Community Forums](https://forum.armbian.com); however, please be aware that official support from the Armbian team is not guaranteed.

    While the Home Assistant team is [planning to deprecate the Supervised installation method](https://community.home-assistant.io/t/feedback-requested-deprecating-core-supervised-i386-armhf-armv7/880968/312), the Armbian team will continue to provide and maintain the supervised installation method as long as automated installation tests remain successful and the maintenance effort remains reasonable.
<!--- header STOP from tools/include/markdown/HAS001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/HAS001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/HAS001-header.md)  
__Status:__ Preview  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/home-assistant/supervised-installer)  

~~~ custombash
armbian-config --cmd HAS001
~~~


<!--- footer START from tools/include/markdown/HAS001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8123**:

    - URL: `https://<your.IP>:8123`
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


~~~ bash title="Home Assistant remove:"
armbian-config --cmd HAS002
~~~


~~~ bash title="Home Assistant purge with data folder:"
armbian-config --cmd HAS003
~~~



