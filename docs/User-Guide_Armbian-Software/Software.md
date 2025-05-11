---
comments: true
---

# Run/Install 3rd party applications

## Web server, LEMP, reverse proxy, Let's Encrypt SSL

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/WebHosting-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/WebHosting-header.md)  
#### SWAG


SWAG reverse proxy


<!--- section image START from tools/include/images/SWAG01.png --->
[![SWAG](/images/SWAG01.png)](#)
<!--- section image STOP from tools/include/images/SWAG01.png --->


<!--- header START from tools/include/markdown/SWAG01-header.md --->
SWAG - Secure Web Application Gateway sets up an Nginx webserver and reverse proxy with php support and a built-in certbot client that automates free SSL server certificate generation and renewal processes (Let's Encrypt). It also contains fail2ban for intrusion prevention.

After entering required information, your server will have auto updating SSL secured website! To this website you can attach several services, for example: https://my.server.com/netdata will run [Netdata](https://www.netdata.cloud/) instance.

=== "Requirements"

    - this computer port 80 and 443 must be open to the internet
    - your domain name (myserver.mydomain.com) DNS server should point to your router WAN address
    - make sure to set additional .htpasswd username and password as you don't want to expose your services without password

=== "Directories"

    - Config directory: `/armbian/swag/config/`
    - Website root folder: `/armbian/swag/config/www/`
    - Reverse proxy configuration samples: `/armbian/swag/config/nginx/proxy-confs/`

=== "Advanced setup"

    - Please follow this comprehensive guide: <https://github.com/linuxserver/docker-swag>

<!--- header STOP from tools/include/markdown/SWAG01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/SWAG01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/SWAG01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/linuxserver/docker-swag)  

~~~ custombash
armbian-config --cmd SWAG01
~~~


~~~ bash title="SWAG reverse proxy .htpasswd set:"
armbian-config --cmd SWAG02
~~~


~~~ bash title="SWAG remove:"
armbian-config --cmd SWAG03
~~~


~~~ bash title="SWAG purge with data folder:"
armbian-config --cmd SWAG04
~~~





## Home Automation for control home appliances

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/HomeAutomation-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/HomeAutomation-header.md)  
#### openHAB


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




#### Home Assistant


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




#### Domoticz


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




#### EVCC


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




## Network-wide ad blockers servers

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/DNS-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/DNS-header.md)  
#### Pi-hole


Pi-hole DNS ad blocker


<!--- section image START from tools/include/images/PIH001.png --->
[![Pi-hole](/images/PIH001.png)](#)
<!--- section image STOP from tools/include/images/PIH001.png --->


<!--- header START from tools/include/markdown/PIH001-header.md --->
Pi-hole is a network-wide ad blocker that acts as a DNS (Domain Name System) sinkhole. It works by blocking requests to known ad servers, trackers, and malicious websites across all devices connected to your home network. Here's how it works:

- DNS-Based Filtering: Pi-hole intercepts DNS requests from devices on your network. When a device tries to connect to a website, Pi-hole checks if the website's domain is on a blocklist. If it is, Pi-hole prevents the connection from being made, effectively blocking ads, trackers, and potentially harmful sites.

- Customizable Blocklists: Pi-hole allows you to choose from a variety of community-maintained blocklists or even add your own. These blocklists contain domains known to serve ads, trackers, and other unwanted content.

- Device and Network-Level Protection: Once set up, Pi-hole works across your entire network. This means all devices (smartphones, tablets, computers, smart TVs, etc.) that use your Pi-hole as their DNS server automatically benefit from ad-blocking without needing individual apps or browser extensions.

- Web Interface: Pi-hole offers an intuitive web interface where you can monitor statistics, review blocked domains, and tweak settings like adding custom blocklists or whitelisting certain sites.

- Privacy and Speed: By blocking unwanted content at the DNS level, Pi-hole not only improves browsing speed (since ads are not loaded), but also enhances privacy by preventing tracking scripts from running in the background.

Pi-hole is typically installed on a Armbian minimal, but it can also run on other systems. It's a great way to have ad-blocking and privacy protection across your entire network without needing to install anything on individual devices.
<!--- header STOP from tools/include/markdown/PIH001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/PIH001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/PIH001-header.md)  
__Status:__ Stable  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.pi-hole.net/)  

~~~ custombash
armbian-config --cmd PIH001
~~~


<!--- footer START from tools/include/markdown/PIH001-footer.md --->
=== "Access the web interface"

    The web interface of Pi-hole can be accessed via:

    - URL = `http://<your.IP>/admin`
    - Password is set and adjust from `armbian-config`

=== "Documentation"

<https://docs.pi-hole.net/>

<!--- footer STOP from tools/include/markdown/PIH001-footer.md --->


~~~ bash title="Pi-hole remove:"
armbian-config --cmd PIH003
~~~


~~~ bash title="Pi-hole change web admin password:"
armbian-config --cmd PIH002
~~~


~~~ bash title="Pi-hole purge with data folder:"
armbian-config --cmd PIH004
~~~





#### Unbound


Unbound caching DNS resolver


<!--- section image START from tools/include/images/UNB001.png --->
[![Unbound](/images/UNB001.png)](#)
<!--- section image STOP from tools/include/images/UNB001.png --->


<!--- header START from tools/include/markdown/UNB001-header.md --->
Unbound is a high-performance, open-source DNS resolver. It primarily serves to resolve domain names into IP addresses for devices on a network. Unlike regular DNS servers, Unbound performs DNS lookups directly and securely, providing features like DNSSEC validation (ensuring data integrity) and privacy protections. It's often used to improve speed, security, and privacy by resolving queries locally rather than relying on external DNS services.
<!--- header STOP from tools/include/markdown/UNB001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/UNB001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/UNB001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://unbound.docs.nlnetlabs.nl/en/latest/)  

~~~ custombash
armbian-config --cmd UNB001
~~~


<!--- footer START from tools/include/markdown/UNB001-footer.md --->
=== "Default DNS port"

    - Default DNS port: 53

=== "Directories"

    - Install directory: `/armbian/unbound/`
    - Configuration directory: `/armbian/unbound/`

=== "View logs"

    ```sh
    docker logs -f unbound
    ```

<!--- footer STOP from tools/include/markdown/UNB001-footer.md --->


~~~ bash title="Unbound remove:"
armbian-config --cmd UNB002
~~~


~~~ bash title="Unbound purge with data folder:"
armbian-config --cmd UNB003
~~~




#### AdGuardHome


AdGuardHome DNS sinkhole


<!--- section image START from tools/include/images/ADG001.png --->
[![AdGuardHome](/images/ADG001.png)](#)
<!--- section image STOP from tools/include/images/ADG001.png --->


<!--- header START from tools/include/markdown/ADG001-header.md --->
AdGuard Home is a network-wide software that functions as a DNS server and ad blocker. It blocks ads, trackers, and malicious websites at the DNS level, meaning it filters content for all devices connected to the network. It also provides additional features like parental controls, logging, and privacy protections. Essentially, it acts as a gateway between your devices and the internet, blocking unwanted content before it even reaches your devices.

<!--- header STOP from tools/include/markdown/ADG001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/ADG001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ADG001-header.md)  
__Status:__ Stable  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/AdguardTeam/AdGuardHome/wiki)  

~~~ custombash
armbian-config --cmd ADG001
~~~


<!--- footer START from tools/include/markdown/ADG001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3000**:

    - URL: `https://<your.IP>:3000`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/adguardhome/`
    - Configuration directory: `/armbian/adguardhome/confdir`
    - Work directory: `/armbian/adguardhome/workdir`

=== "Usage"

    - server where you are installing is automatically switched to this DNS
    - on your desktop PC set IP address of this server as DNS
    - network wide: set IP address of this server on routers DNS

=== "Black and white lists"

    There are many sites in the web giving blocklists and whitelists for AdGuard Home. They can be used when you want to have more blocking as the standard installation gives you. Here are some examples:

    - [The Big Blocklist Collection by WaLLy3K](https://firebog.net/)
    - [Phishing Army blocklist](https://phishing.army/)
    - [Whitelist collection by anudeepND](https://github.com/anudeepND/whitelist)

=== "View logs"

    ```sh
    docker logs -f adguardhome
    ```

<!--- footer STOP from tools/include/markdown/ADG001-footer.md --->


~~~ bash title="AdGuardHome remove:"
armbian-config --cmd ADG002
~~~


~~~ bash title="AdGuardHome purge with data folder:"
armbian-config --cmd ADG003
~~~




## Music servers and streamers

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Music-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Music-header.md)  
#### Navidrome


Navidrome music server and streamer compatible with Subsonic/Airsonic


<!--- section image START from tools/include/images/NAV001.png --->
[![Navidrome](/images/NAV001.png)](#)
<!--- section image STOP from tools/include/images/NAV001.png --->


<!--- header START from tools/include/markdown/NAV001-header.md --->
Navidrome is a modern, lightweight, and self-hosted music server and streamer. It's designed to be compatible with the Subsonic and Airsonic APIs, making it a drop-in replacement for users of those systems. With Navidrome, you can stream your personal music collection from anywhere using any compatible Subsonic client (mobile or desktop). It supports multi-user access, real-time updates, album artwork, and is built with performance and simplicity in mind—perfect for organizing and accessing large music libraries.

<!--- header STOP from tools/include/markdown/NAV001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/NAV001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NAV001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/pynavidrome/navidrome/wiki)  

~~~ custombash
armbian-config --cmd NAV001
~~~


~~~ bash title="Navidrome remove:"
armbian-config --cmd NAV002
~~~


~~~ bash title="Navidrome purge with data folder:"
armbian-config --cmd NAV003
~~~




## Manage your finances

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Finance-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Finance-header.md)  
#### Actual Budget


Do your finances with Actual Budget


<!--- section image START from tools/include/images/ABU001.png --->
[![Actual Budget](/images/ABU001.png)](#)
<!--- section image STOP from tools/include/images/ABU001.png --->


<!--- header START from tools/include/markdown/ABU001-header.md --->
[Actual Budget](https://actualbudget.org/) is a **free, open-source personal finance app** built around the **envelope budgeting method**.

- **Privacy-focused**: Users can self-host their data or use encrypted cloud syncing.
- **Key Features**:
  - Multi-account tracking
  - Transaction importing
  - Customizable financial reports
  - Optional syncing via services like PikaPods
- **Ideal for**: Those who want a **transparent**, **self-hosted** alternative to proprietary budgeting tools.

<!--- header STOP from tools/include/markdown/ABU001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/ABU001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ABU001-header.md)  
__Status:__ Stable  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://actualbudget.org/docs)  

~~~ custombash
armbian-config --cmd ABU001
~~~


<!--- footer START from tools/include/markdown/ABU001-footer.md --->
!!! danger "Warning: HTTPS Certificate Required"

    After initially installing the Actual server, you might get stuck at the step:  
    **"Initializing the connection to the local database..."**

    The issue is due to the server not having an **HTTPS certificate**.  
    After activating an HTTPS certificate for the Actual server, everything should work fine.

    If you still encounter issues even after setting up HTTPS, we highly recommend reaching out to the [Actual Budget Discord server](https://discord.gg/actualbudget) — the developers and community there are very kind and helpful.


<!--- footer STOP from tools/include/markdown/ABU001-footer.md --->


~~~ bash title="Actual Budget remove:"
armbian-config --cmd ABU002
~~~


~~~ bash title="Actual Budget purge with data folder:"
armbian-config --cmd ABU003
~~~




## Backup solutions for your data

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Backup-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Backup-header.md)  
#### Duplicati


Duplicati install


<!--- section image START from tools/include/images/DPL001.png --->
[![Duplicati](/images/DPL001.png)](#)
<!--- section image STOP from tools/include/images/DPL001.png --->


<!--- header START from tools/include/markdown/DPL001-header.md --->
Duplicati is a versatile and secure backup tool designed for everyone, including:

- Users new to backup systems who need a simple and reliable solution.
- Experienced users who want full control over encrypted backups and storage destinations.
- System administrators who require automated, encrypted backups across multiple platforms.

Duplicati offers powerful features such as strong AES-256 encryption, backup scheduling, and flexible storage support (local folders, NAS, cloud providers like Google Drive, Dropbox, S3, and more).  
Through its web-based interface, users can easily configure, monitor, and restore backups from any browser.

Thanks to Duplicati’s smart design — working through standard protocols and containerized deployment — it fits seamlessly into any environment, from personal setups to enterprise infrastructures.

<!--- header STOP from tools/include/markdown/DPL001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/DPL001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DPL001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://prev-docs.duplicati.com/en/latest/)  

~~~ custombash
armbian-config --cmd DPL001
~~~


<!--- footer START from tools/include/markdown/DPL001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8200**:

    - URL: `http://<your.IP>:8200`

=== "Directories"

    - Install directory: `/armbian/duplicati`
    - Configuration directory: `/armbian/duplicati/config`
    - Backup target directory: `/armbian/duplicati/backups`

=== "View logs"

    ```sh
    docker logs -f duplicati
    ```

<!--- footer STOP from tools/include/markdown/DPL001-footer.md --->


~~~ bash title="Duplicati remove:"
armbian-config --cmd DPL002
~~~


~~~ bash title="Duplicati purge with data folder:"
armbian-config --cmd DPL003
~~~




## Download apps for movies, TV shows, music and subtitles

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Downloaders-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Downloaders-header.md)  
#### qBittorrent


qBittorrent BitTorrent client 


<!--- section image START from tools/include/images/DOW001.png --->
[![qBittorrent](/images/DOW001.png)](#)
<!--- section image STOP from tools/include/images/DOW001.png --->


<!--- header START from tools/include/markdown/DOW001-header.md --->
The Qbittorrent⁠ project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

<!--- header STOP from tools/include/markdown/DOW001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/DOW001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DOW001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/qbittorrent/qBittorrent/wiki/)  

~~~ custombash
armbian-config --cmd DOW001
~~~


<!--- footer START from tools/include/markdown/DOW001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8090**:

    - URL: `https://<your.IP>:8090`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/qbittorrent`
    - Site configuration directory: `/armbian/qbittorrent/config`
    - Download directory: `/armbian/qbittorrent/downloads`

=== "View logs"

    ```sh
    docker logs -f qbittorrent
    ```

<!--- footer STOP from tools/include/markdown/DOW001-footer.md --->


~~~ bash title="qBittorrent remove:"
armbian-config --cmd DOW002
~~~


~~~ bash title="qBittorrent purge with data folder:"
armbian-config --cmd DOW003
~~~


~~~ bash title="Prowlarr:"
armbian-config --cmd DOW025
~~~


<!--- footer START from tools/include/markdown/DOW025-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9696**:

    - URL: `https://<your.IP>:9696`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/prowlarr`
    - Site configuration directory: `/armbian/prowlarr/config`

=== "View logs"

    ```sh
    docker logs -f prowlarr
    ```

<!--- footer STOP from tools/include/markdown/DOW025-footer.md --->


~~~ bash title="Prowlarr remove:"
armbian-config --cmd DOW026
~~~


~~~ bash title="Prowlarr purge with data folder:"
armbian-config --cmd DOW027
~~~







#### Deluge


Deluge BitTorrent client


<!--- section image START from tools/include/images/DEL001.png --->
[![Deluge](/images/DEL001.png)](#)
<!--- section image STOP from tools/include/images/DEL001.png --->


<!--- header START from tools/include/markdown/DEL001-header.md --->
Deluge⁠ is a lightweight, Free Software, cross-platform BitTorrent client.

<!--- header STOP from tools/include/markdown/DEL001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/DEL001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DEL001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://deluge-torrent.org/userguide/)  

~~~ custombash
armbian-config --cmd DEL001
~~~


<!--- footer START from tools/include/markdown/DEL001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8112**:

    - URL: `https://<your.IP>:8112`
    - Username/Password: default user/password of admin/deluge

=== "Directories"

    - Install directory: `/armbian/deluge`
    - Site configuration directory: `/armbian/deluge/config`
    - Download directory: `/armbian/deluge/downloads`

=== "View logs"

    ```sh
    docker logs -f deluge
    ```

<!--- footer STOP from tools/include/markdown/DEL001-footer.md --->


~~~ bash title="Deluge remove:"
armbian-config --cmd DEL002
~~~


~~~ bash title="Deluge purge with data folder:"
armbian-config --cmd DEL003
~~~




#### Transmission


Transmission BitTorrent client


<!--- section image START from tools/include/images/TRA001.png --->
[![Transmission](/images/TRA001.png)](#)
<!--- section image STOP from tools/include/images/TRA001.png --->


<!--- header START from tools/include/markdown/TRA001-header.md --->
Transmission⁠ is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

<!--- header STOP from tools/include/markdown/TRA001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/TRA001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/TRA001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://transmissionbt.com/)  

~~~ custombash
armbian-config --cmd TRA001
~~~


<!--- footer START from tools/include/markdown/TRA001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9091**:

    - URL: `https://<your.IP>:9091`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/transmission`
    - Site configuration directory: `/armbian/transmission/config`
    - Download directory: `/armbian/transmission/downloads`
    - Watch directory: `/armbian/transmission/watch`

=== "View logs"

    ```sh
    docker logs -f transmission
    ```

<!--- footer STOP from tools/include/markdown/TRA001-footer.md --->


~~~ bash title="Transmission remove:"
armbian-config --cmd TRA002
~~~


~~~ bash title="Transmission purge with data folder:"
armbian-config --cmd TRA003
~~~




#### SABnzbd


SABnzbd newsgroup downloader


<!--- section image START from tools/include/images/SABN01.png --->
[![SABnzbd](/images/SABN01.png)](#)
<!--- section image STOP from tools/include/images/SABN01.png --->


<!--- header START from tools/include/markdown/SABN01-header.md --->
Sabnzbd⁠ makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

<!--- header STOP from tools/include/markdown/SABN01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/SABN01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/SABN01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://sabnzbd.org/wiki/faq)  

~~~ custombash
armbian-config --cmd SABN01
~~~


<!--- footer START from tools/include/markdown/SABN01-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8080**:

    - URL: `https://<your.IP>:8080`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/sabnzbd`
    - Site configuration directory: `/armbian/sabnzbd/config`
    - Download directory: `/armbian/sabnzbd/downloads`
    - Incomplete downloads: `/armbian/sabnzbd/incomplete`

=== "View logs"

    ```sh
    docker logs -f sabnzbd
    ```

<!--- footer STOP from tools/include/markdown/SABN01-footer.md --->


~~~ bash title="SABnzbd remove:"
armbian-config --cmd SABN02
~~~


~~~ bash title="SABnzbd purge with data folder:"
armbian-config --cmd SABN03
~~~




#### Medusa


Medusa automatic downloader for TV shows


<!--- header START from tools/include/markdown/MDS001-header.md --->
Medusa is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

<!--- header STOP from tools/include/markdown/MDS001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/MDS001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/MDS001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/pymedusa/Medusa/wiki)  

~~~ custombash
armbian-config --cmd MDS001
~~~


<!--- footer START from tools/include/markdown/MDS001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8081**:

    - URL: `https://<your.IP>:8081`

=== "Directories"

    - Install directory: `/armbian/medusa`
    - Site configuration directory: `/armbian/medusa/config`
    - Download directory: `/armbian/medusa/downloads`
    - Download directory TV shows: `/armbian/medusa/downloads/tv`

=== "View logs"

    ```sh
    docker logs -f medusa
    ```

<!--- footer STOP from tools/include/markdown/MDS001-footer.md --->


~~~ bash title="Medusa TV shows downloader remove:"
armbian-config --cmd MDS002
~~~


~~~ bash title="Medusa TV shows downloader purge:"
armbian-config --cmd MDS003
~~~




#### Sonarr


Sonarr automatic downloader for TV shows


<!--- section image START from tools/include/images/SON001.png --->
[![Sonarr](/images/SON001.png)](#)
<!--- section image STOP from tools/include/images/SON001.png --->


<!--- header START from tools/include/markdown/SON001-header.md --->
Sonarr (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/SON001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/SON001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/SON001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://transmissionbt.com/)  

~~~ custombash
armbian-config --cmd SON001
~~~


<!--- footer START from tools/include/markdown/SON001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8989**:

    - URL: `https://<your.IP>:8989`

=== "Directories"

    - Install directory: `/armbian/sonarr`
    - Site configuration directory: `/armbian/sonarr/config`
    - Download directory: `/armbian/sonarr/tvseries`
    - Client download directory: `/armbian/sonarr/client`

=== "View logs"

    ```sh
    docker logs -f sonarr
    ```

<!--- footer STOP from tools/include/markdown/SON001-footer.md --->


~~~ bash title="Sonarr remove:"
armbian-config --cmd SON002
~~~


~~~ bash title="Sonarr purge with data folder:"
armbian-config --cmd SON003
~~~




#### Radarr


Radarr automatic downloader for movies


<!--- section image START from tools/include/images/RAD001.png --->
[![Radarr](/images/RAD001.png)](#)
<!--- section image STOP from tools/include/images/RAD001.png --->


<!--- header START from tools/include/markdown/RAD001-header.md --->
Radarr - A fork of Sonarr to work with movies à la Couchpotato.

<!--- header STOP from tools/include/markdown/RAD001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/RAD001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/RAD001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://wiki.servarr.com/radarr)  

~~~ custombash
armbian-config --cmd RAD001
~~~


<!--- footer START from tools/include/markdown/RAD001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **7878**:

    - URL: `https://<your.IP>:7878`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/radarr`
    - Site configuration directory: `/armbian/radarr/config`
    - Download directory: `/armbian/radarr/movies`
    - Client download directory: `/armbian/radarr/client`

=== "View logs"

    ```sh
    docker logs -f radarr
    ```

<!--- footer STOP from tools/include/markdown/RAD001-footer.md --->


~~~ bash title="Radarr remove:"
armbian-config --cmd RAD002
~~~


~~~ bash title="Radarr purge with data folder:"
armbian-config --cmd RAD003
~~~




#### Bazarr


Bazarr automatic subtitles downloader for Sonarr and Radarr


<!--- section image START from tools/include/images/BAZ001.png --->
[![Bazarr](/images/BAZ001.png)](#)
<!--- section image STOP from tools/include/images/BAZ001.png --->


<!--- header START from tools/include/markdown/BAZ001-header.md --->
Bazarr is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

<!--- header STOP from tools/include/markdown/BAZ001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/BAZ001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/BAZ001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://wiki.bazarr.media/)  

~~~ custombash
armbian-config --cmd BAZ001
~~~


<!--- footer START from tools/include/markdown/BAZ001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **6767**:

    - URL: `https://<your.IP>:6767`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/bazarr`
    - Site configuration directory: `/armbian/bazarr/config`
    - Download directory: `/armbian/bazarr/movies` `/armbian/bazarr/tv`

=== "View logs"

    ```sh
    docker logs -f bazarr
    ```

<!--- footer STOP from tools/include/markdown/BAZ001-footer.md --->


~~~ bash title="Bazarr remove:"
armbian-config --cmd BAZ002
~~~


~~~ bash title="Bazarr purge with data folder:"
armbian-config --cmd BAZ003
~~~




#### Lidarr


Lidarr automatic music downloader


<!--- section image START from tools/include/images/LID001.png --->
[![Lidarr](/images/LID001.png)](#)
<!--- section image STOP from tools/include/images/LID001.png --->


<!--- header START from tools/include/markdown/LID001-header.md --->
Lidarr is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/LID001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/LID001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/LID001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://wiki.servarr.com/lidarr)  

~~~ custombash
armbian-config --cmd LID001
~~~


<!--- footer START from tools/include/markdown/LID001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8686**:

    - URL: `https://<your.IP>:8686`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/lidarr`
    - Site configuration directory: `/armbian/lidarr/config`
    - Download directory: `/armbian/lidarr/downloads` `/armbian/lidarr/music`

=== "View logs"

    ```sh
    docker logs -f lidarr
    ```

<!--- footer STOP from tools/include/markdown/LID001-footer.md --->


~~~ bash title="Lidarr remove:"
armbian-config --cmd LID002
~~~


~~~ bash title="Lidarr purge with data folder:"
armbian-config --cmd LID003
~~~




#### Readarr


Readarr automatic downloader for Ebooks


<!--- section image START from tools/include/images/RDR001.png --->
[![Readarr](/images/RDR001.png)](#)
<!--- section image STOP from tools/include/images/RDR001.png --->


<!--- header START from tools/include/markdown/RDR001-header.md --->
Readarr - Book Manager and Automation (Sonarr for Ebooks)

<!--- header STOP from tools/include/markdown/RDR001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/RDR001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/RDR001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://wiki.servarr.com/readarr)  

~~~ custombash
armbian-config --cmd RDR001
~~~


<!--- footer START from tools/include/markdown/RDR001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8787**:

    - URL: `https://<your.IP>:8787`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/readarr`
    - Site configuration directory: `/armbian/readarr/config`
    - Download directory: `/armbian/readarr/books` `/armbian/readarr/client`

=== "View logs"

    ```sh
    docker logs -f readarr
    ```

<!--- footer STOP from tools/include/markdown/RDR001-footer.md --->


~~~ bash title="Readarr remove:"
armbian-config --cmd RDR002
~~~


~~~ bash title="Readarr purge with data folder:"
armbian-config --cmd RDR003
~~~




#### Jellyseerr


Jellyseerr Jellyfin/Emby/Plex integration install


<!--- section image START from tools/include/images/JEL001.png --->
[![Jellyseerr](/images/JEL001.png)](#)
<!--- section image STOP from tools/include/images/JEL001.png --->


<!--- header START from tools/include/markdown/JEL001-header.md --->
Jellyseerr is a free and open source software application for managing requests for your media library. It is a fork of Overseerr built to bring support for Jellyfin & Emby media servers!

<!--- header STOP from tools/include/markdown/JEL001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/JEL001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/JEL001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.jellyseerr.dev/)  

~~~ custombash
armbian-config --cmd JEL001
~~~


~~~ bash title="Jellyseerr remove:"
armbian-config --cmd JEL002
~~~


~~~ bash title="Jellyseerr purge with data folder:"
armbian-config --cmd JEL003
~~~




## SQL database servers and web interface managers

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Database-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Database-header.md)  
#### PostgreSQL


PostgreSQL install


<!--- section image START from tools/include/images/PGSQL1.png --->
[![PostgreSQL](/images/PGSQL1.png)](#)
<!--- section image STOP from tools/include/images/PGSQL1.png --->


<!--- header START from tools/include/markdown/PGSQL1-header.md --->
PostgreSQL is a powerful, open-source object-relational database system known for its robustness, feature richness, and reliability.

It is designed for everyone, including:

- Developers needing advanced SQL support and extensibility.
- System administrators requiring reliable data storage for mission-critical applications.
- Enterprises seeking a high-performance, standards-compliant relational database.

PostgreSQL offers strong ACID compliance, concurrency, rich data types, full-text search, JSON support, and extensibility through stored procedures and custom functions.  
It is trusted globally in financial, government, and web-scale applications.

Thanks to its proven architecture and open-source nature, PostgreSQL fits seamlessly in projects of all sizes.

<!--- header STOP from tools/include/markdown/PGSQL1-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/PGSQL1-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/PGSQL1-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://www.postgresql.org/docs/)  

~~~ custombash
armbian-config --cmd PGSQL1
~~~


<!--- footer START from tools/include/markdown/PGSQL1-footer.md --->
=== "Access to the database"

    PostgreSQL is accessible via port **5432**:

    - Host: `postgresql://<your.IP>:5432`
    - Default user: `armbian`
    - Default password: `armbian`
    - Default database: `armbian`

=== "Directories"

    - Data directory: `/armbian/postgres/data`

=== "View logs"

    ```sh
    docker logs -f postgres
    ```

<!--- footer STOP from tools/include/markdown/PGSQL1-footer.md --->


~~~ bash title="PostgreSQL remove:"
armbian-config --cmd PGSQL2
~~~


~~~ bash title="PostgreSQL purge with data folder:"
armbian-config --cmd PGSQL3
~~~




#### Mariadb


Mariadb SQL database server


<!--- section image START from tools/include/images/DAT001.png --->
[![Mariadb](/images/DAT001.png)](#)
<!--- section image STOP from tools/include/images/DAT001.png --->


<!--- header START from tools/include/markdown/DAT001-header.md --->
Mariadb is one of the most popular database servers. Made by the original developers of MySQL.

<!--- header STOP from tools/include/markdown/DAT001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/DAT001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DAT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://mariadb.org/documentation/)  

~~~ custombash
armbian-config --cmd DAT001
~~~


<!--- footer START from tools/include/markdown/DAT001-footer.md --->
=== "Configuration"

    Database access configuration is done at first install:
    - create root password
    - create database
    - create normal user
    - create password for normal user

    - Database host: `<your.IP>`

=== "Directories"

    - Install directory: `/armbian/mariadb`
    - Site configuration directory: `/armbian/mariadb/config`

=== "View logs"

    ```sh
    docker logs -f mariadb
    ```

<!--- footer STOP from tools/include/markdown/DAT001-footer.md --->


~~~ bash title="Mariadb remove:"
armbian-config --cmd DAT002
~~~


~~~ bash title="Mariadb purge with data folder:"
armbian-config --cmd DAT003
~~~




#### Redis


Redis install


<!--- section image START from tools/include/images/REDIS1.png --->
[![Redis](/images/REDIS1.png)](#)
<!--- section image STOP from tools/include/images/REDIS1.png --->


<!--- header START from tools/include/markdown/REDIS1-header.md --->
Redis is an open-source, in-memory data structure store, used as a database, cache, and message broker.  
It supports a variety of data structures such as strings, hashes, lists, sets, and sorted sets.

**Key Features:**
- Extremely fast performance with in-memory storage
- Persistence options (snapshotting and AOF)
- Pub/Sub messaging capabilities
- Built-in replication and high availability
- Simple API and wide client support

Redis is widely used for real-time applications, caching layers, session stores, and lightweight queues across industries and platforms.

<!--- header STOP from tools/include/markdown/REDIS1-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/REDIS1-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/REDIS1-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://redis.io/docs/)  

~~~ custombash
armbian-config --cmd REDIS1
~~~


<!--- footer START from tools/include/markdown/REDIS1-footer.md --->
=== "Access to the service"

    Redis server is accessible on port **6379**:

    - Host: `redis://<your.IP>:6379`

=== "Directories"

    - Data directory: `/armbian/redis/data`

=== "View logs"

    ```sh
    docker logs -f redis
    ```

<!--- footer STOP from tools/include/markdown/REDIS1-footer.md --->


~~~ bash title="Redis remove:"
armbian-config --cmd REDIS2
~~~


~~~ bash title="Redis purge with data folder:"
armbian-config --cmd REDIS3
~~~




#### phpMyAdmin


phpMyAdmin web interface manager


<!--- section image START from tools/include/images/MYA001.png --->
[![phpMyAdmin](/images/MYA001.png)](#)
<!--- section image STOP from tools/include/images/MYA001.png --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/MYA001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/MYA001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://www.phpmyadmin.net/docs/)  

~~~ custombash
armbian-config --cmd MYA001
~~~


~~~ bash title="phpMyAdmin remove:"
armbian-config --cmd MYA002
~~~


~~~ bash title="phpMyAdmin purge with data folder:"
armbian-config --cmd MYA003
~~~




## Armbian infrastructure services

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Armbian-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Armbian-header.md)  
#### CDN router


Router for repository mirror automation


<!--- section image START from tools/include/images/ART001.png --->
[![CDN router](/images/ART001.png)](#)
<!--- section image STOP from tools/include/images/ART001.png --->


<!--- header START from tools/include/markdown/ART001-header.md --->
The Armbian Router is an intelligent redirector system that optimizes file downloads by automatically directing users to the best available mirror. It evaluates each download request based on geographic location, server health, and file availability, ensuring faster downloads, balanced load distribution, and high availability. This core service underpins Armbian's scalable mirror network, seamlessly routing traffic to improve performance and reliability for end users worldwide.

<!--- header STOP from tools/include/markdown/ART001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/ART001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ART001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd ART001
~~~


~~~ bash title="Remove CDN router:"
armbian-config --cmd ART002
~~~



#### GH runners


GitHub runners for Armbian automation


<!--- section image START from tools/include/images/GHR001.png --->
[![GH runners](/images/GHR001.png)](#)
<!--- section image STOP from tools/include/images/GHR001.png --->


<!--- header START from tools/include/markdown/GHR001-header.md --->
This module automates the installation, removal, and status checking of GitHub self-hosted runners for the Armbian project. It supports batch operations and user input through dialog prompts when running interactively.

<!--- header STOP from tools/include/markdown/GHR001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/GHR001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/GHR001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd GHR001
~~~


<!--- footer START from tools/include/markdown/GHR001-footer.md --->
=== "Supported Commands"

- **`install`**  
  Installs one or more GitHub runners using the provided configuration or interactively prompted values.

- **`purge` / `remove`**  
  Removes runners based on the provided runner name series and target organization or repository.

- **`status`**  
  Quietly checks if any `actions.runner` services are currently running on the system.

=== "Available Switches"

| Switch             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `gh_token`         | GitHub token with admin rights to manage self-hosted runners.               |
| `runner_name`      | Name prefix for the runner series (default: `armbian`).                     |
| `start`            | Start index of the runner series (e.g., `01`).                              |
| `stop`             | End index of the runner series (e.g., `05`).                                |
| `label_primary`    | Labels for the first runner (default: `alfa`).                              |
| `label_secondary`  | Labels for additional runners (default: `fast,images`).                     |
| `organisation`     | GitHub organization name (default: `armbian`).                              |
| `owner`            | GitHub user or organization owner (used for repo-level runners).            |
| `repository`       | GitHub repository name (used for repo-level runners).                       |

=== "Behavior"

- Prompts the user for missing switches via `dialog` **only in interactive mode**.
- Supports bulk installation of runners using sequential numbering (`start` to `stop`).
- Calls internal `actions.runner.install` and `actions.runner.remove` helpers.
- Returns `0` if any runner services are active, `1` otherwise (for scripting use).
- Suppresses errors and outputs when checking status to remain quiet in background use.

<!--- footer STOP from tools/include/markdown/GHR001-footer.md --->


~~~ bash title="Remove GitHub runners for Armbian automation:"
armbian-config --cmd GHR002
~~~



#### Rsyncd server


<!--- section image START from tools/include/images/RSD001.png --->
[![Rsyncd server](/images/RSD001.png)](#)
<!--- section image STOP from tools/include/images/RSD001.png --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/RSD001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/RSD001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd RSD001
~~~


~~~ bash title="Remove Armbian rsyncd server:"
armbian-config --cmd RSD002
~~~



## Applications and tools for development

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/DevTools-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/DevTools-header.md)  
#### Git CLI


Install tools for cloning and managing repositories (git)

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/GIT001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/GIT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd GIT001
~~~


~~~ bash title="Remove tools for cloning and managing repositories (git):"
armbian-config --cmd GIT002
~~~



## Docker containerization and KVM virtual machines

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Containers-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Containers-header.md)  
#### Docker


Docker minimal


<!--- section image START from tools/include/images/CON001.png --->
[![Docker](/images/CON001.png)](#)
<!--- section image STOP from tools/include/images/CON001.png --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/CON001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/CON001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://wiki.bazarr.media/)  

~~~ custombash
armbian-config --cmd CON001
~~~


<!--- footer START from tools/include/markdown/CON001-footer.md --->
What is Docker? Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management.

<!--- footer STOP from tools/include/markdown/CON001-footer.md --->


~~~ bash title="Docker engine:"
armbian-config --cmd CON002
~~~


~~~ bash title="Docker remove:"
armbian-config --cmd CON003
~~~


~~~ bash title="Docker purge with all images, containers, and volumes:"
armbian-config --cmd CON004
~~~





#### Portainer


Portainer container management platform


<!--- section image START from tools/include/images/POR001.png --->
[![Portainer](/images/POR001.png)](#)
<!--- section image STOP from tools/include/images/POR001.png --->


<!--- header START from tools/include/markdown/POR001-header.md --->
Portainer simplifies your Docker container management via Portainer web interface. It enables faster deploy of the applications and it gives real time visibility.

<!--- header STOP from tools/include/markdown/POR001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/POR001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/POR001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @schwar3kat  
__Documentation:__ [Link](https://docs.portainer.io/)  

~~~ custombash
armbian-config --cmd POR001
~~~


<!--- footer START from tools/include/markdown/POR001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9002**:

    - URL = `http://<your.IP>:9002`

<!--- footer STOP from tools/include/markdown/POR001-footer.md --->


~~~ bash title="Portainer remove:"
armbian-config --cmd POR002
~~~


~~~ bash title="Portainer purge with with data folder:"
armbian-config --cmd POR003
~~~




## Media servers, organizers and editors

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Media-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Media-header.md)  
#### OMV


Deploy NAS using OpenMediaVault


<!--- section image START from tools/include/images/OMV001.png --->
[![OMV](/images/OMV001.png)](#)
<!--- section image STOP from tools/include/images/OMV001.png --->


<!--- header START from tools/include/markdown/OMV001-header.md --->
OpenMediaVault (OMV) is a powerful, open-source network-attached storage (NAS) operating system built on the Debian Linux distribution. It is designed to provide a simple and intuitive web-based interface for managing storage devices and network services, making it ideal for home users, small offices, and even advanced users looking for a customizable and efficient NAS solution.

OMV supports a wide range of features, including various file systems (EXT4, XFS, BTRFS, etc.), software RAID configurations, scheduled backups, and user and group management. It offers support for common network protocols such as SMB/CIFS (Windows file sharing), NFS, FTP, and SSH, enabling seamless file access across different platforms.

Through its modular design, OpenMediaVault can be easily extended with plugins, allowing users to add functionality like Docker support, media servers, cloud synchronization tools, BitTorrent clients, and more. The system is designed for stability and ease of use, with regular updates and a strong community supporting development and troubleshooting.

Whether used on a dedicated server, a Raspberry Pi, or virtualized hardware, OMV provides a flexible and reliable way to build your own custom NAS.  

**Warning**: installation works only on Debian (bookworm) based Armbian image.
<!--- header STOP from tools/include/markdown/OMV001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/OMV001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/OMV001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">amd64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.openmediavault.org/en/stable/)  

~~~ custombash
armbian-config --cmd OMV001
~~~


<!--- footer START from tools/include/markdown/OMV001-footer.md --->
=== "Access to the web interface"

    The OpenMediaVault web interface is accessible via the default HTTP port:

    - URL: `http://<your.IP>:80`
    - Username/Password: admin / openmediavault (change after first login)

=== "Directories"

    - Default config directory: `/etc/openmediavault/`
    - Shared folders base path: `/srv/dev-disk-by-.../`
    - Plugin data directories may vary by service (e.g., Docker, SMB, etc.)

=== "Usage"

    - Use the web interface to configure storage, users, services, and plugins
    - Create shared folders and enable SMB/NFS to access files over the network
    - Monitor system status, performance, and logs from the dashboard

=== "Plugins and Add-ons"

    OpenMediaVault supports a wide range of community plugins:

    - Docker support via `openmediavault-compose` or `omv-extras`
    - Media servers (e.g., Plex, Jellyfin)
    - Backup tools (e.g., rsync, USB backup)
    - Cloud sync (e.g., Rclone)

    Install plugins through the web interface after enabling OMV-Extras.

=== "View logs"

    ```sh
    journalctl -u openmediavault-engined
    tail -f /var/log/syslog
    ```

<!--- footer STOP from tools/include/markdown/OMV001-footer.md --->


~~~ bash title="OpenMediaVault remove:"
armbian-config --cmd OMV002
~~~



#### Filebrowser


Filebrowser provides a web-based file manager accessible via a browser


<!--- section image START from tools/include/images/FIL001.png --->
[![Filebrowser](/images/FIL001.png)](#)
<!--- section image STOP from tools/include/images/FIL001.png --->


<!--- header START from tools/include/markdown/FIL001-header.md --->
**Filebrowser** is a lightweight, web-based file manager that gives you direct access to your files from any browser. It allows users to upload, delete, preview, rename, and organize files and folders — all through a clean, responsive interface.

**Key Features**

- Modern and intuitive web interface
- User management with role-based access
- File uploads, downloads, sharing, and previews
- Custom branding support
- Configurable directory access
- Runs as a single binary or Docker container

Official site: [https://filebrowser.org](https://filebrowser.org)

<!--- header STOP from tools/include/markdown/FIL001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/FIL001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/FIL001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://filebrowser.org/)  

~~~ custombash
armbian-config --cmd FIL001
~~~


<!--- footer START from tools/include/markdown/FIL001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8095**:

    - URL: `http://<your.IP>:8095`
    - Username/Password: admin / admin

=== "Directories"

    - Install directory: `/armbian/filebrowser`
    - Root directory: `/armbian/filebrowser/srv`
    - Database directory: `/armbian/filebrowser/database`
    - Configuration file: `/armbian/filebrowser/filebrowser.json`
    - Branding directory: `/armbian/filebrowser/branding`

=== "View logs"

    ```sh
    docker logs -f filebrowser
    ```

<!--- footer STOP from tools/include/markdown/FIL001-footer.md --->


~~~ bash title="Filebrowser container remove:"
armbian-config --cmd FIL002
~~~


~~~ bash title="Filebrowser container purge with data folder:"
armbian-config --cmd FIL003
~~~




#### Emby


Emby organizes video, music, live TV, and photos


<!--- section image START from tools/include/images/EMB001.png --->
[![Emby](/images/EMB001.png)](#)
<!--- section image STOP from tools/include/images/EMB001.png --->


<!--- header START from tools/include/markdown/EMB001-header.md --->
Emby organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

<!--- header STOP from tools/include/markdown/EMB001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/EMB001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/EMB001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @schwar3kat  
__Documentation:__ [Link](https://emby.media)  

~~~ custombash
armbian-config --cmd EMB001
~~~


<!--- footer START from tools/include/markdown/EMB001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8096**:

    - URL: `https://<your.IP>:8096`

=== "Directories"

    - Install directory: `/armbian/emby`
    - Site configuration directory: `/armbian/emby/config`
    - Data directory: `/armbian/emby/tvshows` `/armbian/emby/movies`

=== "View logs"

    ```sh
    docker logs -f emby
    ```

<!--- footer STOP from tools/include/markdown/EMB001-footer.md --->


~~~ bash title="Emby server remove:"
armbian-config --cmd EMB002
~~~


~~~ bash title="Emby server purge with data folder:"
armbian-config --cmd EMB003
~~~




#### Stirling


Stirling PDF tools for viewing and editing PDF files


<!--- section image START from tools/include/images/STR001.png --->
[![Stirling](/images/STR001.png)](#)
<!--- section image STOP from tools/include/images/STR001.png --->


<!--- header START from tools/include/markdown/STR001-header.md --->
Stirling-PDF is a robust, locally hosted web-based PDF manipulation tool using Docker. It enables you to carry out various operations on PDF files, including splitting, merging, converting, reorganizing, adding images, rotating, compressing, and more. This locally hosted web application has evolved to encompass a comprehensive set of features, addressing all your PDF requirements.

<!--- header STOP from tools/include/markdown/STR001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/STR001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/STR001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.stirlingpdf.com)  

~~~ custombash
armbian-config --cmd STR001
~~~


<!--- footer START from tools/include/markdown/STR001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8077**:

    - URL: `https://<your.IP>:8077`

=== "Directories"

    - Install directory: `/armbian/stirling`

=== "View logs"

    ```sh
    docker logs -f stirling-pdf
    ```

<!--- footer STOP from tools/include/markdown/STR001-footer.md --->


~~~ bash title="Stirling PDF remove:"
armbian-config --cmd STR002
~~~


~~~ bash title="Stirling PDF purge with data folder:"
armbian-config --cmd STR003
~~~




#### Syncthing


Syncthing continuous file synchronization


<!--- section image START from tools/include/images/STC001.png --->
[![Syncthing](/images/STC001.png)](#)
<!--- section image STOP from tools/include/images/STC001.png --->


<!--- header START from tools/include/markdown/STC001-header.md --->
Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

<!--- header STOP from tools/include/markdown/STC001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/STC001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/STC001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.syncthing.net/)  

~~~ custombash
armbian-config --cmd STC001
~~~


<!--- footer START from tools/include/markdown/STC001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8884**:

    - URL: `https://<your.IP>:8884`
    - Username/Password: There is none, but it is highly suggested setting a password for this container. To do this go to Actions -> Settings -> set user/password for the webUI.

=== "Directories"

    - Install directory: `/armbian/syncthing`
    - Site configuration directory: `/armbian/syncthing/config`
    - Data directory: `/armbian/syncthing/data1` `/armbian/syncthing/data2`

=== "View logs"

    ```sh
    docker logs -f syncthing
    ```

<!--- footer STOP from tools/include/markdown/STC001-footer.md --->


~~~ bash title="Syncthing remove:"
armbian-config --cmd STC002
~~~


~~~ bash title="Syncthing purge with data folder:"
armbian-config --cmd STC003
~~~




#### Nextcloud


Nextcloud content collaboration platform


<!--- section image START from tools/include/images/NCT001.png --->
[![Nextcloud](/images/NCT001.png)](#)
<!--- section image STOP from tools/include/images/NCT001.png --->


<!--- header START from tools/include/markdown/NCT001-header.md --->
Nextcloud gives you access to all your files wherever you are. Where are your photos and documents? With Nextcloud you pick a server of your choice, at home, in a data center or at a provider. And that is where your files will be. Nextcloud runs on that server, protecting your data and giving you access from your desktop or mobile devices. Through Nextcloud you also access, sync and share your existing data on that FTP drive at the office, a Dropbox or a NAS you have at home.

<!--- header STOP from tools/include/markdown/NCT001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/NCT001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NCT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://nextcloud.com/support/)  

~~~ custombash
armbian-config --cmd NCT001
~~~


<!--- footer START from tools/include/markdown/NCT001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **443**:

    - URL: `https://<your.IP>:443`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/nextcloud`
    - Site configuration directory: `/armbian/nextcloud/config`
    - Data directory: `/armbian/nextcloud/data`

=== "View logs"

    ```sh
    docker logs -f nextcloud
    ```

<!--- footer STOP from tools/include/markdown/NCT001-footer.md --->


~~~ bash title="Nextcloud remove:"
armbian-config --cmd NCT002
~~~


~~~ bash title="Nextcloud purge with data folder:"
armbian-config --cmd NCT003
~~~




#### Owncloud


Owncloud share files and folders, easy and secure


<!--- section image START from tools/include/images/OWC001.png --->
[![Owncloud](/images/OWC001.png)](#)
<!--- section image STOP from tools/include/images/OWC001.png --->


<!--- header START from tools/include/markdown/OWC001-header.md --->
ownCloud is a free and open-source software project for content collaboration and sharing and syncing of files in distributed and federated enterprise scenarios.

<!--- header STOP from tools/include/markdown/OWC001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/OWC001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/OWC001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://doc.owncloud.com/)  

~~~ custombash
armbian-config --cmd OWC001
~~~


<!--- footer START from tools/include/markdown/OWC001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **7787**:

    - URL: `http://<your.IP>:7787`
    - Username/Password: admin / admin

=== "Directories"

    - Install directory: `/armbian/owncloud`
    - Site configuration directory: `/armbian/owncloud/config`
    - Data directory: `/armbian/owncloud/data`

=== "View logs"

    ```sh
    docker logs -f owncloud
    ```

<!--- footer STOP from tools/include/markdown/OWC001-footer.md --->


~~~ bash title="Owncloud remove:"
armbian-config --cmd OWC002
~~~


~~~ bash title="Owncloud purge with data folder:"
armbian-config --cmd OWC003
~~~




#### Jellyfin


Jellyfin Media System


<!--- section image START from tools/include/images/JMS001.png --->
[![Jellyfin](/images/JMS001.png)](#)
<!--- section image STOP from tools/include/images/JMS001.png --->


<!--- header START from tools/include/markdown/JMS001-header.md --->
Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it.

<!--- header STOP from tools/include/markdown/JMS001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/JMS001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/JMS001-header.md)  
__Status:__ Preview  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://jellyfin.org/docs/general/quick-start/)  

~~~ custombash
armbian-config --cmd JMS001
~~~


<!--- footer START from tools/include/markdown/JMS001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8096**:

    - URL: `http://<your.IP>:8096`
    - Username and password are set at first login

=== "Directories"

    - Install directory: `/armbian/jellyfin`
    - Site configuration directory: `/armbian/jellyfin/config`
    - TV shows directory: `/armbian/jellyfin/tvseries`
    - Movies directory: `/armbian/jellyfin/movies`

=== "View logs"

    ```sh
    docker logs -f jellyfin
    ```

<!--- footer STOP from tools/include/markdown/JMS001-footer.md --->


~~~ bash title="Jellyfin remove:"
armbian-config --cmd JMS002
~~~


~~~ bash title="Jellyfin purge with data folder:"
armbian-config --cmd JMS003
~~~




#### Hastebin


Hastebin Paste Server


<!--- section image START from tools/include/images/HPS001.png --->
[![Hastebin](/images/HPS001.png)](#)
<!--- section image STOP from tools/include/images/HPS001.png --->


<!--- header START from tools/include/markdown/HPS001-header.md --->
Hastebin is a fast and simple self-hosted pastebin server. It allows users to quickly share text snippets like logs, code, or notes via a web interface or API. Hastebin is lightweight, easy to deploy with Docker, and ideal for teams needing private, temporary paste storage.

<!--- header STOP from tools/include/markdown/HPS001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/HPS001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/HPS001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @efectn  
__Documentation:__ [Link](https://github.com/rpardini/ansi-hastebin)  

~~~ custombash
armbian-config --cmd HPS001
~~~


~~~ bash title="Hastebin remove:"
armbian-config --cmd HPS002
~~~


~~~ bash title="Hastebin purge with data folder:"
armbian-config --cmd HPS003
~~~




#### Immich


Immich - high-performance self-hosted photo and video backup solution


<!--- section image START from tools/include/images/IMM001.png --->
[![Immich](/images/IMM001.png)](#)
<!--- section image STOP from tools/include/images/IMM001.png --->


<!--- header START from tools/include/markdown/IMM001-header.md --->
[**Immich**](https://immich.app/) is a self-hosted photo and video backup solution, designed for individuals and families who want:

- An alternative to cloud-based services like Google Photos or iCloud  
- A private, secure place to store, browse, and share memories  
- Powerful features like automatic mobile uploads, facial recognition, and search  
- A modern, responsive web and mobile interface for easy access

Thanks to Immich being built with modern technologies like NestJS, TypeScript, and machine learning integrations, users enjoy a smooth, intelligent media experience. Whether you’re a casual user backing up phone photos or a tech-savvy person managing media across multiple devices, Immich provides the flexibility and control of a cloud solution—on your own server.

**Summary**

- **Immich** is ideal if you want full privacy, open-source flexibility, and control over your data.
- **Google Photos** is convenient and polished but comes with trade-offs in privacy and cost at scale.
- **Synology Photos** fits well in homes or small offices already using Synology NAS systems, offering good performance with integrated features.

<!--- header STOP from tools/include/markdown/IMM001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/IMM001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/IMM001-header.md)  
__Status:__ Preview  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://immich.app/docs)  

~~~ custombash
armbian-config --cmd IMM001
~~~


<!--- footer START from tools/include/markdown/IMM001-footer.md --->
=== "Access to the service"

    Immich is accessible via HTTP on port **8077**:

    - URL: `http://<your.IP>:8077`

=== "Default credentials"

    - Email: *(set during initial setup)*
    - Password: *(set during initial setup)*

=== "Directories"

    - Uploads: `/armbian/immich/photos/upload/`
    - Thumbnails: `/armbian/immich/photos/thumbs/`
    - Profile images: `/armbian/immich/photos/profile/`
    - Library: `/armbian/immich/photos/library/`
    - Encoded videos: `/armbian/immich/photos/encoded-video/`
    - Backups: `/armbian/immich/photos/backups/`

=== "View logs"

    ```sh
    docker logs -f immich
    ```

=== "Immich vs Google Photos vs Synology Photos"

    | Feature / Aspect               | **Immich**                                | **Google Photos**                           | **Synology Photos**                         |
    |-------------------------------|-------------------------------------------|---------------------------------------------|---------------------------------------------|
    | **Hosting**                   | Self-hosted                               | Cloud (Google infrastructure)               | Self-hosted (on Synology NAS)               |
    | **Privacy & Control**         | Full control, private data storage        | Data stored and analyzed by Google          | Full control within your NAS environment    |
    | **Automatic Uploads**         | Yes (via mobile app)                      | Yes (via mobile app)                        | Yes (via mobile app or Synology Drive)      |
    | **Facial Recognition**        | Yes (on-device)                           | Yes (cloud-based)                           | Yes (on-device)                             |
    | **Object & Scene Detection**  | Yes (limited but improving)               | Yes (advanced AI)                           | Yes (basic)                                 |
    | **Web Interface**             | Yes (modern and responsive)               | Yes                                         | Yes                                         |
    | **Mobile Apps**               | Yes (iOS & Android)                       | Yes (iOS & Android)                         | Yes (iOS & Android)                         |
    | **Albums & Sharing**          | Yes (with public and private sharing)     | Yes (advanced sharing options)              | Yes                                         |
    | **Multi-user Support**        | Yes                                       | Limited (mostly single user)                | Yes (multi-user, tied to NAS users)         |
    | **Backup Original Quality**   | Yes (no compression)                      | Only with paid storage                      | Yes (NAS dependent)                         |
    | **Offline Access**            | Limited (depends on app setup)            | Yes (with sync)                             | Yes                                         |
    | **Open Source**               | Yes                                       | No                                          | No                                          |
    | **Hardware Requirement**      | Any Docker-capable server or NAS          | N/A (runs on Google’s cloud)                | Synology NAS required                       |
    | **Price**                     | Free (self-hosted, you pay for hardware)  | Free (with limitations) / Paid for storage  | Included with NAS, hardware cost required   |

<!--- footer STOP from tools/include/markdown/IMM001-footer.md --->


~~~ bash title="Immich remove:"
armbian-config --cmd IMM002
~~~


~~~ bash title="Immich purge with data folder:"
armbian-config --cmd IMM003
~~~




## Real-time monitoring, collecting metrics, up-time status

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Monitoring-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Monitoring-header.md)  
#### Uptime Kuma


Uptime Kuma self-hosted monitoring tool


<!--- section image START from tools/include/images/UPK001.png --->
[![Uptime Kuma](/images/UPK001.png)](#)
<!--- section image STOP from tools/include/images/UPK001.png --->


<!--- header START from tools/include/markdown/UPK001-header.md --->
[Uptime Kuma](https://github.com/louislam/uptime-kuma) is a self-hosted monitoring tool similar to \"Uptime Robot\". 
It provides a beautiful, easy-to-use web dashboard to monitor HTTP(s), TCP, Ping, and more types of services.

You can receive instant notifications when a service goes down via Telegram, Discord, Slack, email, and many other integrations.

<!--- header STOP from tools/include/markdown/UPK001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/UPK001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/UPK001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/louislam/uptime-kuma/wiki)  

~~~ custombash
armbian-config --cmd UPK001
~~~


<!--- footer START from tools/include/markdown/UPK001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3001**:

    - URL: `https://<your.IP>:3001`
    - Username/Password: Are set at first web interface login

=== "Features"

    - Monitoring uptime for HTTP(s) / TCP / HTTP(s) Keyword / HTTP(s) Json Query / Ping / DNS Record / Push / Steam Game Server / Docker Containers
    - Fancy, Reactive, Fast UI/UX
    - Notifications via Telegram, Discord, Gotify, Slack, Pushover, Email (SMTP), and 90+ notification services, click here for the full list
    - 20-second intervals
    - Multi Languages
    - Multiple status pages
    - Map status pages to specific domains
    - Ping chart
    - Certificate info
    - Proxy support
    - 2FA support

<!--- footer STOP from tools/include/markdown/UPK001-footer.md --->


~~~ bash title="Uptime Kuma remove:"
armbian-config --cmd UPK002
~~~


~~~ bash title="Uptime Kuma purge with data folder:"
armbian-config --cmd UPK003
~~~




#### Netdata


Netdata - monitoring real-time metrics


<!--- section image START from tools/include/images/NTD001.png --->
[![Netdata](/images/NTD001.png)](#)
<!--- section image STOP from tools/include/images/NTD001.png --->


<!--- header START from tools/include/markdown/NTD001-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/NTD001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/NTD001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NTD001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://transmissionbt.com/)  

~~~ custombash
armbian-config --cmd NTD001
~~~


~~~ bash title="Netdata remove:"
armbian-config --cmd NTD002
~~~


~~~ bash title="Netdata purge with data folder:"
armbian-config --cmd NTD003
~~~




#### Grafana


Grafana data analytics


<!--- section image START from tools/include/images/GRA001.png --->
[![Grafana](/images/GRA001.png)](#)
<!--- section image STOP from tools/include/images/GRA001.png --->


<!--- header START from tools/include/markdown/GRA001-header.md --->
Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.
<!--- header STOP from tools/include/markdown/GRA001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/GRA001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/GRA001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://grafana.com/docs/)  

~~~ custombash
armbian-config --cmd GRA001
~~~


<!--- footer START from tools/include/markdown/GRA001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3000**:

    - URL: `https://<your.IP>:3000`

=== "Directories"

    - Install directory: `/armbian/grafana`

=== "View logs"

    ```sh
    docker logs -f grafana
    ```

<!--- footer STOP from tools/include/markdown/GRA001-footer.md --->


~~~ bash title="Grafana remove:"
armbian-config --cmd GRA002
~~~


~~~ bash title="Grafana purge with data folder:"
armbian-config --cmd GRA003
~~~




#### Prometheus


Prometheus docker image


<!--- section image START from tools/include/images/PRO001.png --->
[![Prometheus](/images/PRO001.png)](#)
<!--- section image STOP from tools/include/images/PRO001.png --->


<!--- header START from tools/include/markdown/PRO001-header.md --->
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects and stores time-series data, provides powerful query capabilities, and enables real-time alerts based on defined conditions. Commonly used in cloud and containerized environments, Prometheus integrates seamlessly with Kubernetes and other modern infrastructure.

<!--- header STOP from tools/include/markdown/PRO001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/PRO001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/PRO001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @efectn  
__Documentation:__ [Link](https://prometheus.io/docs/)  

~~~ custombash
armbian-config --cmd PRO001
~~~


<!--- footer START from tools/include/markdown/PRO001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9090**:

    - URL: `https://<your.IP>:9090`

=== "Directories"

    - Config directory: `/armbian/prometheus`

=== "View logs"

    ```sh
    docker logs -f prometheus
    ```

<!--- footer STOP from tools/include/markdown/PRO001-footer.md --->


~~~ bash title="Prometheus remove:"
armbian-config --cmd PRO002
~~~


~~~ bash title="Prometheus purge with data folder:"
armbian-config --cmd PRO003
~~~




#### NetAlertX


NetAlertX network scanner & notification framework


<!--- section image START from tools/include/images/NAX001.png --->
[![NetAlertX](/images/NAX001.png)](#)
<!--- section image STOP from tools/include/images/NAX001.png --->


<!--- header START from tools/include/markdown/NAX001-header.md --->
NetAlertX is an open-source network monitoring and intruder detection tool designed to provide visibility into your Wi-Fi or LAN network. It scans your network for connected devices and alerts you when new or unknown devices are detected, helping you monitor unauthorized access and maintain network security.

**Key Features:**

- **Scheduled Network Scans:** Regularly scans your network to detect new devices, reconnections, disconnections, and changes in IP addresses.

- **Extensive Notification Support:** Integrates with over 80 notification services, including email, Telegram, Pushover, and NTFY, ensuring you receive timely alerts about network changes.

- **Network Visualization:** Offers a user-friendly interface to visualize your entire network, enhancing security and simplifying management.

- **Multi-Network Monitoring:** Supports synchronization of multiple network instances, providing cross-network visibility across various device manufacturers.

- **Home Assistant Integration:** Seamlessly integrates with Home Assistant, enabling advanced automation workflows and smart home integrations.

- **Customizable Plugins:** Allows users to develop custom plugins with auto-generated user interfaces and built-in notification systems, tailoring the tool to specific network monitoring needs.

NetAlertX is actively maintained and supports various installation methods, including Docker and bare-metal setups. It serves as a proactive solution for maintaining network health and preventing issues before they escalate, providing peace of mind for individuals and small businesses alike.

For more information and installation guides, visit the official [NetAlertX documentation](https://jokob-sk.github.io/NetAlertX/). 

<!--- header STOP from tools/include/markdown/NAX001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/NAX001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NAX001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://netalertx.com)  

~~~ custombash
armbian-config --cmd NAX001
~~~


<!--- footer START from tools/include/markdown/NAX001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **20211**:

    - URL: `https://<your.IP>:20211`

=== "Directories"

    - Config directory: `/armbian/netalertx/config`

=== "View logs"

    ```sh
    docker logs -f netalertx
    ```

<!--- footer STOP from tools/include/markdown/NAX001-footer.md --->


~~~ bash title="NetAlertX network scanner remove:"
armbian-config --cmd NAX002
~~~


~~~ bash title="NetAlertX network scanner purge with data folder:"
armbian-config --cmd NAX003
~~~




## Remote File & Management tools

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Management-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Management-header.md)  
#### Cockpit


Cockpit web-based management tool


<!--- section image START from tools/include/images/CPT001.png --->
[![Cockpit](/images/CPT001.png)](#)
<!--- section image STOP from tools/include/images/CPT001.png --->


<!--- header START from tools/include/markdown/CPT001-header.md --->
Introducing Cockpit
Cockpit is a web-based graphical interface for servers, intended for everyone, especially those who are:

- new to Linux
(including Windows admins)
- familiar with Linux
and want an easy, graphical way to administer servers
- expert admins
who mainly use other tools but want an overview on individual systems

Thanks to Cockpit intentionally using system APIs and commands, a whole team of admins can manage a system in the way they prefer, including the command line and utilities right alongside Cockpit.
<!--- header STOP from tools/include/markdown/CPT001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/CPT001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/CPT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd CPT001
~~~


<!--- footer START from tools/include/markdown/CPT001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9090**:

    - URL: `https://<your.IP>:9090`
    - Username/Password: your system login credentials

=== "Video instructions"


    <iframe width="1200" height="676" src="https://www.youtube.com/embed/L9fMWCRcqIE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!--- footer STOP from tools/include/markdown/CPT001-footer.md --->


#### Samba


SAMBA Remote File share


<!--- section image START from tools/include/images/SMB001.png --->
[![Samba](/images/SMB001.png)](#)
<!--- section image STOP from tools/include/images/SMB001.png --->


<!--- header START from tools/include/markdown/SMB001-header.md --->
Samba is an open-source software suite that enables seamless file and printer sharing between Linux/Unix servers and Windows clients. It allows a Linux machine to act as a domain controller, file server, or print server within a Windows network environment, supporting cross-platform interoperability.

<!--- header STOP from tools/include/markdown/SMB001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/SMB001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/SMB001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd SMB001
~~~


#### Webmin


Webmin web-based management tool


<!--- section image START from tools/include/images/WBM001.png --->
[![Webmin](/images/WBM001.png)](#)
<!--- section image STOP from tools/include/images/WBM001.png --->


<!--- header START from tools/include/markdown/WBM001-header.md --->
Webmin is a web-based system administration tool for Unix-like servers. It provides an easy-to-use browser interface to manage users, configure services, edit files, monitor system performance, and control almost every aspect of your server — without needing to touch the command line.

<!--- header STOP from tools/include/markdown/WBM001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/WBM001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/WBM001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd WBM001
~~~


<!--- footer START from tools/include/markdown/WBM001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **10000**:

    - URL: `https://<your.IP>:10000`
    - Username/Password: your system login credentials


<!--- footer STOP from tools/include/markdown/WBM001-footer.md --->


#### Homepage


Install Homepage startpage / application dashboard


<!--- section image START from tools/include/images/HPG001.png --->
[![Homepage](/images/HPG001.png)](#)
<!--- section image STOP from tools/include/images/HPG001.png --->


<!--- header START from tools/include/markdown/HPG001-header.md --->
[gethomepage](https://gethomepage.dev/) is a fast, fully static, highly customizable application dashboard built for modern self-hosted environments. With a **fully proxied** architecture and **zero runtime**, it delivers exceptional speed, security, and simplicity for organizing and accessing your services.

It supports **over 100 service integrations** and **multiple languages**, offering live status displays and dynamic resource monitoring out-of-the-box. Configuration is effortless via **YAML files** or automatic **Docker label discovery**, making setup and management seamless.

*Key Features*

- **Static Frontend**: Blazing-fast performance with no server-side runtime.
- **Secure Proxying**: Safely access internal services without direct exposure.
- **Service Integrations**: Native support for Docker, Kubernetes, Grafana, Proxmox, Home Assistant, and more.
- **Easy Configuration**: Manage layout and services with YAML or Docker labels.
- **Internationalization**: Translations available for multiple languages.
- **Flexible Theming**: Personalize with themes, layouts, and styling.
- **Simple Deployment**: Host via Docker, Kubernetes, or any static hosting platform.

---

Whether you're running a small homelab or a full server fleet, **gethomepage** offers a sleek, powerful, and secure way to stay organized.

<!--- header STOP from tools/include/markdown/HPG001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/HPG001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/HPG001-header.md)  
__Status:__ Stable  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://gethomepage.dev/configs/)  

~~~ custombash
armbian-config --cmd HPG001
~~~


<!--- footer START from tools/include/markdown/HPG001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3000**:

    - URL: `https://<your.IP>:3000`
    - Username/Password: none

    Configuration: Please reffer to official manual <https://gethomepage.dev/configs/>

=== "Directories"

    - Install directory: `/armbian/homepage`
    - Site configuration directory: `/armbian/homepage/config`

=== "View logs"

    ```sh
    docker logs -f homepage
    ```

<!--- footer STOP from tools/include/markdown/HPG001-footer.md --->


~~~ bash title="Remove Homepage:"
armbian-config --cmd HPG002
~~~


~~~ bash title="Purge Homepage with data folder:"
armbian-config --cmd HPG003
~~~




#### NetBox


NetBox infrastructure resource modeling install


<!--- section image START from tools/include/images/NBOX01.png --->
[![NetBox](/images/NBOX01.png)](#)
<!--- section image STOP from tools/include/images/NBOX01.png --->


<!--- header START from tools/include/markdown/NBOX01-header.md --->
**NetBox** is an open-source infrastructure resource modeling (IRM) tool used for managing and documenting networks and data center assets.

Requirements (installed automatically)

- [Redis](/User-Guide_Armbian-Software/Database/#redis)
- [Postgres SQL](/User-Guide_Armbian-Software/Database/#postgresql)

Key Features

- **IP Address Management (IPAM)**: Track IP networks, addresses, and VRFs.
- **Data Center Infrastructure Management (DCIM)**: Model racks, devices, connections, and more.
- **Secrets Management**: Securely store credentials and other sensitive data.
- **Extensible API & Webhooks**: Integrate with external systems.
- **Custom Fields & Scripts**: Tailor NetBox to fit your organization’s needs.

Originally developed by DigitalOcean, NetBox is widely adopted by network engineers and sysadmins to maintain source-of-truth data for automation.

[Official Website](https://netbox.dev/)

<!--- header STOP from tools/include/markdown/NBOX01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/NBOX01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NBOX01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://netbox.readthedocs.io/en/stable/)  

~~~ custombash
armbian-config --cmd NBOX01
~~~


<!--- footer START from tools/include/markdown/NBOX01-footer.md --->
=== "Access to the service"

    NetBox is accessible via HTTP on port **8000**:

    - URL: `http://<your.IP>:8000`
    - API root: `http://<your.IP>:8000/api/`

=== "Default credentials"

    - Username: `admin`
    - Password: *(set during setup)*
    - API token: *Generate in the UI or via Django shell*

=== "Directories"

    - Configuration: `/armbian/netbox/config/`
    - Scripts: `/armbian/netbox/scripts/`
    - Reports: `/armbian/netbox/reports/`

=== "View logs"

    ```sh
    docker logs -f netbox
    ```

=== "Manage the service"

    ```sh
    docker exec -it netbox bash
    ```

<!--- footer STOP from tools/include/markdown/NBOX01-footer.md --->


~~~ bash title="NetBox remove:"
armbian-config --cmd NBOX02
~~~


~~~ bash title="NetBox purge with data folder:"
armbian-config --cmd NBOX03
~~~




## Tools for printing and 3D printing

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Printing-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Printing-header.md)  
#### OctoPrint


OctoPrint web-based 3D printers management tool


<!--- section image START from tools/include/images/OCT001.png --->
[![OctoPrint](/images/OCT001.png)](#)
<!--- section image STOP from tools/include/images/OCT001.png --->


<!--- header START from tools/include/markdown/OCT001-header.md --->
OctoPrint is an open source 3D printer controller application, which provides a web interface for the connected printers. It displays printers status and key parameters and allows user to schedule prints and remotely control the printer.
<!--- header STOP from tools/include/markdown/OCT001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/OCT001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/OCT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://transmissionbt.com/)  

~~~ custombash
armbian-config --cmd OCT001
~~~


<!--- footer START from tools/include/markdown/OCT001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **7981**:

    - URL: `https://<your.IP>:7981`

=== "Directories"

    - Install directory: `/armbian/octoprint`

=== "View logs"

    ```sh
    docker logs -f octoprint
    ```

<!--- footer STOP from tools/include/markdown/OCT001-footer.md --->


~~~ bash title="OctoPrint remove:"
armbian-config --cmd OCT002
~~~


~~~ bash title="OctoPrint purge with data folder:"
armbian-config --cmd OCT003
~~~




## Console network tools for measuring load and bandwidth

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Netconfig-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Netconfig-header.md)  
#### nload


nload - realtime console network usage monitor

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/NLD001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/NLD001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://netbox.readthedocs.io/en/stable/)  

~~~ custombash
armbian-config --cmd NLD001
~~~


~~~ bash title="nload - remove:"
armbian-config --cmd NLD002
~~~



#### iperf3


iperf3 bandwidth measuring tool

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/IPR001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/IPR001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://netbox.readthedocs.io/en/stable/)  

~~~ custombash
armbian-config --cmd IPR001
~~~


~~~ bash title="iperf3 remove:"
armbian-config --cmd IPR002
~~~



#### iptraf-ng


iptraf-ng IP LAN monitor

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/IPT001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/IPT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://netbox.readthedocs.io/en/stable/)  

~~~ custombash
armbian-config --cmd IPT001
~~~


~~~ bash title="iptraf-ng remove:"
armbian-config --cmd IPT002
~~~



#### avahi-daemon


avahi-daemon hostname broadcast via mDNS

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/AVH001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/AVH001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://netbox.readthedocs.io/en/stable/)  

~~~ custombash
armbian-config --cmd AVH001
~~~


~~~ bash title="avahi-daemon remove:"
armbian-config --cmd AVH002
~~~



## Virtual Private Network tools

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/VPN-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/VPN-header.md)  
#### WireGuard


WireGuard VPN client / server


<!--- section image START from tools/include/images/WRG001.png --->
[![WireGuard](/images/WRG001.png)](#)
<!--- section image STOP from tools/include/images/WRG001.png --->


<!--- header START from tools/include/markdown/WRG001-header.md --->
WireGuard is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. Regarded as the most secure, easiest to use, and simplest VPN solution in the industry.
<!--- header STOP from tools/include/markdown/WRG001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/WRG001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/WRG001-header.md)  
__Status:__ Enabled  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.linuxserver.io/images/docker-wireguard/#server-mode)  

~~~ custombash
armbian-config --cmd WRG001
~~~


<!--- footer START from tools/include/markdown/WRG001-footer.md --->
=== "Access to the server from internet"

    Remember to open/forward the port 51820 (UDP) through NAT on your router.
    
=== "Directories"

    - Install directory: `/armbian/wireguard`
    - Site configuration directory: `/armbian/wireguard/config`

=== "View logs"

    ```sh
    docker logs -f wireguard
    ```

# Install server and enable private network on a client

1. Install Wireguard server
2. It will asks you for peer keywords. It will make a profile for each peer
3. Download client to your PC, server or mobile phone. Scan OR code or copy credentials to the client.

Enjoy private network! Its that easy.

More informations:

<https://docs.linuxserver.io/images/docker-wireguard/>
<!--- footer STOP from tools/include/markdown/WRG001-footer.md --->


~~~ bash title="WireGuard remove:"
armbian-config --cmd WRG002
~~~


~~~ bash title="WireGuard clients QR codes:"
armbian-config --cmd WRG003
~~~


~~~ bash title="WireGuard purge with data folder:"
armbian-config --cmd WRG004
~~~





#### ZeroTier


ZeroTier connect devices over your own private network in the world.


<!--- section image START from tools/include/images/ZTR001.png --->
[![ZeroTier](/images/ZTR001.png)](#)
<!--- section image STOP from tools/include/images/ZTR001.png --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/ZTR001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/ZTR001-header.md)  
__Status:__ Stable  

~~~ custombash
armbian-config --cmd ZTR001
~~~

