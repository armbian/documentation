# Home Automation


***

## Install openHAB

<!--- section image START from tools/include/images/HA001.png --->
[![Install openHAB](/images/HA001.png)](#)
<!--- section image STOP from tools/include/images/HA001.png --->

**Command:** 
~~~
armbian-config --cmd HA001
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/HA001-footer.md --->
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

<!--- footer STOP from tools/include/markdown/HA001-footer.md --->



***

## Remove openHAB
**Command:** 
~~~
armbian-config --cmd HA002
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Home Assistant

<!--- section image START from tools/include/images/HA003.png --->
[![Install Home Assistant](/images/HA003.png)](#)
<!--- section image STOP from tools/include/images/HA003.png --->


<!--- header START from tools/include/markdown/HA003-header.md --->
Home Assistant is an open source smart home platform that allows you to connect your smart home devices like your TV, fan, cameras, thermostats, lights, and sensors. As a user, you can build intricate automation using Home Assistant's user-friendly, unified web-based user interface.

Perfect to run on any single board computer with 4 cores and at least 512Mb of memory. Armbian installation is optimised to run from SD/eMMC media, but it is recommended to use SSD.

=== "Access to the web interface"

    The web interface is accessible via port **8123**:

    - URL: `https://<your.IP>:8123`
    - Username/Password: Are set at first web interface login

=== "Directories"

    Home Assistant on Armbian runs supervised in a Docker container. This secures same functionality as stock HAOS.

    - Config directory: `/usr/share/haos`

<!--- header STOP from tools/include/markdown/HA003-header.md --->

**Command:** 
~~~
armbian-config --cmd HA003
~~~

**Author:** @igorpecovnik

**Status:** Preview


<!--- footer START from tools/include/markdown/HA003-footer.md --->
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
<!--- footer STOP from tools/include/markdown/HA003-footer.md --->



***

## Remove Home Assistant
**Command:** 
~~~
armbian-config --cmd HA004
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

