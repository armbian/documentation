---
comments: true
---

# Home Automation for control home appliances

## openHAB


openHAB empowering the smart home


<!--- section image START from tools/include/images/HAB001.png --->
[![openHAB](/images/HAB001.png)](#)
<!--- section image STOP from tools/include/images/HAB001.png --->

**Author:** @armbian

**Status:** Stable


~~~ custombash
armbian-config --cmd HAB001
~~~


<!--- footer START from tools/include/markdown/HAB001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8444**:

    - URL: `https://<your.IP>:8444`
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

<!--- header STOP from tools/include/markdown/HAS001-header.md --->

**Author:** @igorpecovnik

**Status:** Preview


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




## Domoticz


Domoticz open source home automation


<!--- section image START from tools/include/images/DOM001.png --->
[![Domoticz](/images/DOM001.png)](#)
<!--- section image STOP from tools/include/images/DOM001.png --->


<!--- header START from tools/include/markdown/DOM001-header.md --->
Domoticz is an open-source home automation platform that allows you to control and monitor smart devices in your home. It supports a wide range of devices, including lights, sensors, thermostats, and cameras. Through its web interface or mobile app, you can set up automation rules and schedules, providing greater convenience and energy efficiency. It’s customizable, flexible, and can be run on a variety of hardware platforms supported by Armbian.

=== "Access to the web interface"

    The web interface is accessible via port **8080**:

    - URL: `https://<your.IP>:8080`
    - Username/Password: admin / domoticz

=== "Directories"

    - Config directory: `/armbian/domoticz`

=== "Advanced setup"

    - Primary USB device passing through (`/dev/ttyUSB0`) to Docker container is enabled by default
    - For more complex setup, please follow this comprehensive guide: <https://wiki.domoticz.com/Main_Page>

<!--- header STOP from tools/include/markdown/DOM001-header.md --->

**Author:** @igorpecovnik

**Status:** Preview


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

**Author:** @igorpecovnik

**Status:** Preview


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



