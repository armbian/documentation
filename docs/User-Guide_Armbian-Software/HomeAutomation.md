# Home Automation for control home appliances


***

## openHAB empowering the smart home

<!--- section image START from tools/include/images/HAB001.png --->
[![openHAB empowering the smart home](/images/HAB001.png)](#)
<!--- section image STOP from tools/include/images/HAB001.png --->

This operation will install openHAB.

**Command:** 
~~~
armbian-config --cmd HAB001
~~~

**Author:** @armbian

**Status:** Stable



***

## openHAB remove
This operation will purge openHAB.

**Command:** 
~~~
armbian-config --cmd HAB002
~~~

**Author:** @armbian

**Status:** Stable



***

## openHAB purge with data folder
This operation will purge openHAB.

**Command:** 
~~~
armbian-config --cmd HAB003
~~~

**Author:** @armbian

**Status:** Stable



***

## Home Assistant open source home automation

<!--- section image START from tools/include/images/HAS001.png --->
[![Home Assistant open source home automation](/images/HAS001.png)](#)
<!--- section image STOP from tools/include/images/HAS001.png --->


<!--- header START from tools/include/markdown/HAS001-header.md --->
Home Assistant is an open source smart home platform that allows you to connect your smart home devices like your TV, fan, cameras, thermostats, lights, and sensors. As a user, you can build intricate automation using Home Assistant's user-friendly, unified web-based user interface.

Perfect to run on any single board computer with 4 cores and at least 512Mb of memory. Armbian installation is optimised to run from SD/eMMC media, but it is recommended to use SSD.

=== "Access to the web interface"

    The web interface is accessible via port **8123**:

    - URL: `https://<your.IP>:8123`
    - Username/Password: Are set at first web interface login

=== "Directories"

    Home Assistant on Armbian runs supervised in a Docker container. This secures same functionality as stock HAOS.

    - Config directory: `/armbian/haos`

<!--- header STOP from tools/include/markdown/HAS001-header.md --->

This operation will install Home Assistant.

**Command:** 
~~~
armbian-config --cmd HAS001
~~~

**Author:** @igorpecovnik

**Status:** Preview


<!--- footer START from tools/include/markdown/HAS001-footer.md --->
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



***

## Home Assistant remove
This operation will remove Home Assistant.

**Command:** 
~~~
armbian-config --cmd HAS002
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

## Home Assistant purge with data folder
This operation will purge Home Assistant.

**Command:** 
~~~
armbian-config --cmd HAS003
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

## Domoticz open source home automation

<!--- section image START from tools/include/images/DOM001.png --->
[![Domoticz open source home automation](/images/DOM001.png)](#)
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

This operation will install Domoticz.

**Command:** 
~~~
armbian-config --cmd DOM001
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

## Domoticz remove
This operation will remove Domoticz.

**Command:** 
~~~
armbian-config --cmd DOM002
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

## Domoticz purge with data folder
This operation will purge Domoticz.

**Command:** 
~~~
armbian-config --cmd DOM003
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

## EVCC - solar charging automation

<!--- section image START from tools/include/images/EVCC01.png --->
[![EVCC - solar charging automation](/images/EVCC01.png)](#)
<!--- section image STOP from tools/include/images/EVCC01.png --->


<!--- header START from tools/include/markdown/EVCC01-header.md --->
evcc is an energy management system with a focus on electromobility. The software controls your EV charger or smart plug. It communicates with your vehicle, inverter or home storage to make intelligent charging decisions. The software is open source and community-driven.

<!--- header STOP from tools/include/markdown/EVCC01-header.md --->

This operation will install solar charging automation.

**Command:** 
~~~
armbian-config --cmd EVCC01
~~~

**Author:** @igorpecovnik

**Status:** Preview


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



***

## EVCC - solar charging automation remove
This operation will remove solar charging automation.

**Command:** 
~~~
armbian-config --cmd EVCC02
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

## EVCC purge with data folder
This operation will purge solar charging automation with data folder.

**Command:** 
~~~
armbian-config --cmd EVCC03
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

