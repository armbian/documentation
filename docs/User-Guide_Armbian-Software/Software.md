---
comments: true
---

# Run/Install 3rd party applications

## Web server, LEMP, reverse proxy, Let's Encrypt SSL

**Status:** Stable

## SWAG reverse proxy

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/SWAG01.png --->
[![SWAG reverse proxy](/images/SWAG01.png)](#)
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


~~~ custombash title="SWAG reverse proxy:"
armbian-config --cmd SWAG01
~~~


~~~ custombash title="SWAG reverse proxy .htpasswd set:"
armbian-config --cmd SWAG02
~~~


~~~ custombash title="SWAG remove:"
armbian-config --cmd SWAG03
~~~


~~~ custombash title="SWAG purge with data folder:"
armbian-config --cmd SWAG04
~~~

## Home Automation for control home appliances

## openHAB empowering the smart home

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/HAB001.png --->
[![openHAB empowering the smart home](/images/HAB001.png)](#)
<!--- section image STOP from tools/include/images/HAB001.png --->


~~~ custombash title="openHAB empowering the smart home:"
armbian-config --cmd HAB001
~~~


~~~ custombash title="openHAB remove:"
armbian-config --cmd HAB002
~~~


~~~ custombash title="openHAB purge with data folder:"
armbian-config --cmd HAB003
~~~

## Home Assistant open source home automation

**Author:** @igorpecovnik

**Status:** Preview


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


~~~ custombash title="Home Assistant open source home automation:"
armbian-config --cmd HAS001
~~~


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


~~~ custombash title="Home Assistant remove:"
armbian-config --cmd HAS002
~~~


~~~ custombash title="Home Assistant purge with data folder:"
armbian-config --cmd HAS003
~~~

## Domoticz open source home automation

**Author:** @igorpecovnik

**Status:** Preview


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


~~~ custombash title="Domoticz open source home automation:"
armbian-config --cmd DOM001
~~~


~~~ custombash title="Domoticz remove:"
armbian-config --cmd DOM002
~~~


~~~ custombash title="Domoticz purge with data folder:"
armbian-config --cmd DOM003
~~~

## EVCC - solar charging automation

**Author:** @igorpecovnik

**Status:** Preview


<!--- section image START from tools/include/images/EVCC01.png --->
[![EVCC - solar charging automation](/images/EVCC01.png)](#)
<!--- section image STOP from tools/include/images/EVCC01.png --->


<!--- header START from tools/include/markdown/EVCC01-header.md --->
evcc is an energy management system with a focus on electromobility. The software controls your EV charger or smart plug. It communicates with your vehicle, inverter or home storage to make intelligent charging decisions. The software is open source and community-driven.

<!--- header STOP from tools/include/markdown/EVCC01-header.md --->


~~~ custombash title="EVCC - solar charging automation:"
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


~~~ custombash title="EVCC - solar charging automation remove:"
armbian-config --cmd EVCC02
~~~


~~~ custombash title="EVCC purge with data folder:"
armbian-config --cmd EVCC03
~~~

## Network-wide ad blockers servers

## Pi-hole DNS ad blocker

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/DNS001.png --->
[![Pi-hole DNS ad blocker](/images/DNS001.png)](#)
<!--- section image STOP from tools/include/images/DNS001.png --->


<!--- header START from tools/include/markdown/DNS001-header.md --->
Pi-hole is a network-wide ad blocker that acts as a DNS (Domain Name System) sinkhole. It works by blocking requests to known ad servers, trackers, and malicious websites across all devices connected to your home network. Here's how it works:

- DNS-Based Filtering: Pi-hole intercepts DNS requests from devices on your network. When a device tries to connect to a website, Pi-hole checks if the website's domain is on a blocklist. If it is, Pi-hole prevents the connection from being made, effectively blocking ads, trackers, and potentially harmful sites.

- Customizable Blocklists: Pi-hole allows you to choose from a variety of community-maintained blocklists or even add your own. These blocklists contain domains known to serve ads, trackers, and other unwanted content.

- Device and Network-Level Protection: Once set up, Pi-hole works across your entire network. This means all devices (smartphones, tablets, computers, smart TVs, etc.) that use your Pi-hole as their DNS server automatically benefit from ad-blocking without needing individual apps or browser extensions.

- Web Interface: Pi-hole offers an intuitive web interface where you can monitor statistics, review blocked domains, and tweak settings like adding custom blocklists or whitelisting certain sites.

- Privacy and Speed: By blocking unwanted content at the DNS level, Pi-hole not only improves browsing speed (since ads are not loaded), but also enhances privacy by preventing tracking scripts from running in the background.

Pi-hole is typically installed on a Armbian minimal, but it can also run on other systems. It's a great way to have ad-blocking and privacy protection across your entire network without needing to install anything on individual devices.
<!--- header STOP from tools/include/markdown/DNS001-header.md --->


~~~ custombash title="Pi-hole DNS ad blocker:"
armbian-config --cmd DNS001
~~~


<!--- footer START from tools/include/markdown/DNS001-footer.md --->
=== "Access the web interface"

    The web interface of Pi-hole can be accessed via:

    - URL = `http://<your.IP>/admin`
    - Password is set and adjust from `armbian-config`

=== "Documentation"

<https://docs.pi-hole.net/>

<!--- footer STOP from tools/include/markdown/DNS001-footer.md --->


~~~ custombash title="Pi-hole remove:"
armbian-config --cmd DNS003
~~~


~~~ custombash title="Pi-hole change web admin password:"
armbian-config --cmd DNS002
~~~


~~~ custombash title="Pi-hole purge with data folder:"
armbian-config --cmd DNS004
~~~

## Unbound caching DNS resolver

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/UNB001.png --->
[![Unbound caching DNS resolver](/images/UNB001.png)](#)
<!--- section image STOP from tools/include/images/UNB001.png --->


<!--- header START from tools/include/markdown/UNB001-header.md --->
Unbound is a high-performance, open-source DNS resolver. It primarily serves to resolve domain names into IP addresses for devices on a network. Unlike regular DNS servers, Unbound performs DNS lookups directly and securely, providing features like DNSSEC validation (ensuring data integrity) and privacy protections. It's often used to improve speed, security, and privacy by resolving queries locally rather than relying on external DNS services.
<!--- header STOP from tools/include/markdown/UNB001-header.md --->


~~~ custombash title="Unbound caching DNS resolver:"
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


~~~ custombash title="Unbound remove:"
armbian-config --cmd UNB002
~~~


~~~ custombash title="Unbound purge with data folder:"
armbian-config --cmd UNB003
~~~

## AdGuardHome DNS sinkhole

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/ADG001.png --->
[![AdGuardHome DNS sinkhole](/images/ADG001.png)](#)
<!--- section image STOP from tools/include/images/ADG001.png --->


<!--- header START from tools/include/markdown/ADG001-header.md --->
AdGuard Home is a network-wide software that functions as a DNS server and ad blocker. It blocks ads, trackers, and malicious websites at the DNS level, meaning it filters content for all devices connected to the network. It also provides additional features like parental controls, logging, and privacy protections. Essentially, it acts as a gateway between your devices and the internet, blocking unwanted content before it even reaches your devices.

<!--- header STOP from tools/include/markdown/ADG001-header.md --->


~~~ custombash title="AdGuardHome DNS sinkhole:"
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


~~~ custombash title="AdGuardHome remove:"
armbian-config --cmd ADG002
~~~


~~~ custombash title="AdGuardHome purge with data folder:"
armbian-config --cmd ADG003
~~~

## Music servers and streamers

## Navidrome music server and streamer compatible with Subsonic/Airsonic

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/NAV001.png --->
[![Navidrome music server and streamer compatible with Subsonic/Airsonic](/images/NAV001.png)](#)
<!--- section image STOP from tools/include/images/NAV001.png --->


~~~ custombash title="Navidrome music server and streamer compatible with Subsonic/Airsonic:"
armbian-config --cmd NAV001
~~~


~~~ custombash title="Navidrome remove:"
armbian-config --cmd NAV002
~~~


~~~ custombash title="Navidrome purge with data folder:"
armbian-config --cmd NAV003
~~~

## Download apps for movies, TV shows, music and subtitles

## qBittorrent BitTorrent client 

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/DOW001.png --->
[![qBittorrent BitTorrent client ](/images/DOW001.png)](#)
<!--- section image STOP from tools/include/images/DOW001.png --->


<!--- header START from tools/include/markdown/DOW001-header.md --->
The Qbittorrent⁠ project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

<!--- header STOP from tools/include/markdown/DOW001-header.md --->


~~~ custombash title="qBittorrent BitTorrent client :"
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


~~~ custombash title="qBittorrent remove:"
armbian-config --cmd DOW002
~~~


~~~ custombash title="qBittorrent purge with data folder:"
armbian-config --cmd DOW003
~~~

## Deluge BitTorrent client

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/DEL001.png --->
[![Deluge BitTorrent client](/images/DEL001.png)](#)
<!--- section image STOP from tools/include/images/DEL001.png --->


<!--- header START from tools/include/markdown/DEL001-header.md --->
Deluge⁠ is a lightweight, Free Software, cross-platform BitTorrent client.

<!--- header STOP from tools/include/markdown/DEL001-header.md --->


~~~ custombash title="Deluge BitTorrent client:"
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


~~~ custombash title="Deluge remove:"
armbian-config --cmd DEL002
~~~


~~~ custombash title="Deluge purge with data folder:"
armbian-config --cmd DEL003
~~~

## Transmission BitTorrent client

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/TRA001.png --->
[![Transmission BitTorrent client](/images/TRA001.png)](#)
<!--- section image STOP from tools/include/images/TRA001.png --->


<!--- header START from tools/include/markdown/TRA001-header.md --->
Transmission⁠ is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

<!--- header STOP from tools/include/markdown/TRA001-header.md --->


~~~ custombash title="Transmission BitTorrent client:"
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


~~~ custombash title="Transmission remove:"
armbian-config --cmd TRA002
~~~


~~~ custombash title="Transmission purge with data folder:"
armbian-config --cmd TRA003
~~~

## SABnzbd newsgroup downloader

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/SABN01.png --->
[![SABnzbd newsgroup downloader](/images/SABN01.png)](#)
<!--- section image STOP from tools/include/images/SABN01.png --->


<!--- header START from tools/include/markdown/SABN01-header.md --->
Sabnzbd⁠ makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

<!--- header STOP from tools/include/markdown/SABN01-header.md --->


~~~ custombash title="SABnzbd newsgroup downloader:"
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


~~~ custombash title="SABnzbd remove:"
armbian-config --cmd SABN02
~~~


~~~ custombash title="SABnzbd purge with data folder:"
armbian-config --cmd SABN03
~~~

## Medusa automatic downloader for TV shows

**Author:** @armbian

**Status:** Stable


<!--- header START from tools/include/markdown/MDS001-header.md --->
Medusa is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

<!--- header STOP from tools/include/markdown/MDS001-header.md --->


~~~ custombash title="Medusa automatic downloader for TV shows:"
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


~~~ custombash title="Medusa TV shows downloader remove:"
armbian-config --cmd MDS002
~~~


~~~ custombash title="Medusa TV shows downloader purge:"
armbian-config --cmd MDS003
~~~

## Sonarr automatic downloader for TV shows

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/SON001.png --->
[![Sonarr automatic downloader for TV shows](/images/SON001.png)](#)
<!--- section image STOP from tools/include/images/SON001.png --->


<!--- header START from tools/include/markdown/SON001-header.md --->
Sonarr (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/SON001-header.md --->


~~~ custombash title="Sonarr automatic downloader for TV shows:"
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


~~~ custombash title="Sonarr remove:"
armbian-config --cmd SON002
~~~


~~~ custombash title="Sonarr purge with data folder:"
armbian-config --cmd SON003
~~~

## Radarr automatic downloader for movies

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/RAD001.png --->
[![Radarr automatic downloader for movies](/images/RAD001.png)](#)
<!--- section image STOP from tools/include/images/RAD001.png --->


<!--- header START from tools/include/markdown/RAD001-header.md --->
Radarr - A fork of Sonarr to work with movies à la Couchpotato.

<!--- header STOP from tools/include/markdown/RAD001-header.md --->


~~~ custombash title="Radarr automatic downloader for movies:"
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


~~~ custombash title="Radarr remove:"
armbian-config --cmd RAD002
~~~


~~~ custombash title="Radarr purge with data folder:"
armbian-config --cmd RAD003
~~~

## Bazarr automatic subtitles downloader for Sonarr and Radarr

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/BAZ001.png --->
[![Bazarr automatic subtitles downloader for Sonarr and Radarr](/images/BAZ001.png)](#)
<!--- section image STOP from tools/include/images/BAZ001.png --->


<!--- header START from tools/include/markdown/BAZ001-header.md --->
Bazarr is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

<!--- header STOP from tools/include/markdown/BAZ001-header.md --->


~~~ custombash title="Bazarr automatic subtitles downloader for Sonarr and Radarr:"
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


~~~ custombash title="Bazarr remove:"
armbian-config --cmd BAZ002
~~~


~~~ custombash title="Bazarr purge with data folder:"
armbian-config --cmd BAZ003
~~~

## Lidarr automatic music downloader

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/LID001.png --->
[![Lidarr automatic music downloader](/images/LID001.png)](#)
<!--- section image STOP from tools/include/images/LID001.png --->


<!--- header START from tools/include/markdown/LID001-header.md --->
Lidarr is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/LID001-header.md --->


~~~ custombash title="Lidarr automatic music downloader:"
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


~~~ custombash title="Lidarr remove:"
armbian-config --cmd LID002
~~~


~~~ custombash title="Lidarr purge with data folder:"
armbian-config --cmd LID003
~~~

## Readarr automatic downloader for Ebooks

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/RDR001.png --->
[![Readarr automatic downloader for Ebooks](/images/RDR001.png)](#)
<!--- section image STOP from tools/include/images/RDR001.png --->


<!--- header START from tools/include/markdown/RDR001-header.md --->
Readarr - Book Manager and Automation (Sonarr for Ebooks)

<!--- header STOP from tools/include/markdown/RDR001-header.md --->


~~~ custombash title="Readarr automatic downloader for Ebooks:"
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


~~~ custombash title="Readarr remove:"
armbian-config --cmd RDR002
~~~


~~~ custombash title="Readarr purge with data folder:"
armbian-config --cmd RDR003
~~~


~~~ custombash title="Prowlarr index manager and proxy for PVR:"
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


~~~ custombash title="Prowlarr remove:"
armbian-config --cmd DOW026
~~~


~~~ custombash title="Prowlarr purge with data folder:"
armbian-config --cmd DOW027
~~~

## Jellyseerr Jellyfin/Emby/Plex integration install

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/JEL001.png --->
[![Jellyseerr Jellyfin/Emby/Plex integration install](/images/JEL001.png)](#)
<!--- section image STOP from tools/include/images/JEL001.png --->


<!--- header START from tools/include/markdown/JEL001-header.md --->
Jellyseerr is a free and open source software application for managing requests for your media library. It is a fork of Overseerr built to bring support for Jellyfin & Emby media servers!

<!--- header STOP from tools/include/markdown/JEL001-header.md --->


~~~ custombash title="Jellyseerr Jellyfin/Emby/Plex integration install:"
armbian-config --cmd JEL001
~~~


~~~ custombash title="Jellyseerr remove:"
armbian-config --cmd JEL002
~~~


~~~ custombash title="Jellyseerr purge with data folder:"
armbian-config --cmd JEL003
~~~

## SQL database servers and web interface managers

## Mariadb SQL database server

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/DAT001.png --->
[![Mariadb SQL database server](/images/DAT001.png)](#)
<!--- section image STOP from tools/include/images/DAT001.png --->


<!--- header START from tools/include/markdown/DAT001-header.md --->
Mariadb is one of the most popular database servers. Made by the original developers of MySQL.

<!--- header STOP from tools/include/markdown/DAT001-header.md --->


~~~ custombash title="Mariadb SQL database server:"
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


~~~ custombash title="Mariadb remove:"
armbian-config --cmd DAT002
~~~


~~~ custombash title="Mariadb purge with data folder:"
armbian-config --cmd DAT003
~~~


~~~ custombash title="phpMyAdmin web interface manager:"
armbian-config --cmd DAT005
~~~


<!--- footer START from tools/include/markdown/DAT005-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8071**:

    - URL: `https://<your.IP>:8071`
    - Server: IP from server you are connecting to. If you have installed MariaDB via this tool, then this is `<your.IP>`
    - Username: defined at SQL server install (MariaDb)
    - Password: defined at SQL server install (MariaDb)

=== "Directories"

    - Install directory: `/armbian/phpmyadmin`
    - Site configuration directory: `/armbian/phpmyadmin/config`

=== "View logs"

    ```sh
    docker logs -f phpmyadmin
    ```

<!--- footer STOP from tools/include/markdown/DAT005-footer.md --->


~~~ custombash title="phpMyAdmin remove:"
armbian-config --cmd DAT006
~~~


~~~ custombash title="phpMyAdmin purge with data folder:"
armbian-config --cmd DAT007
~~~

## Applications and tools for development

## Install tools for cloning and managing repositories (git)

**Author:** @armbian

**Status:** Stable


~~~ custombash title="Install tools for cloning and managing repositories (git):"
armbian-config --cmd DEV001
~~~


~~~ custombash title="Install tools for cloning and managing repositories (git):"
armbian-config --cmd DEV001
~~~


~~~ custombash title="Remove tools for cloning and managing repositories (git):"
armbian-config --cmd DEV002
~~~


~~~ custombash title="Remove tools for cloning and managing repositories (git):"
armbian-config --cmd DEV002
~~~


~~~ custombash title="Armbian router for repository mirror automation:"
armbian-config --cmd DEV003
~~~


~~~ custombash title="Remove Armbian router:"
armbian-config --cmd DEV004
~~~


~~~ custombash title="Armbian rsyncd server:"
armbian-config --cmd DEV010
~~~


~~~ custombash title="Remove Armbian rsyncd server:"
armbian-config --cmd DEV011
~~~

## Docker containerization and KVM virtual machines

## Docker minimal

**Author:** @schwar3kat

**Status:** Stable


<!--- section image START from tools/include/images/CON001.webp --->
[![Docker minimal](/images/CON001.webp)](#)
<!--- section image STOP from tools/include/images/CON001.webp --->


~~~ custombash title="Docker minimal:"
armbian-config --cmd CON001
~~~


<!--- footer START from tools/include/markdown/CON001-footer.md --->
What is Docker? Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management.

<!--- footer STOP from tools/include/markdown/CON001-footer.md --->


~~~ custombash title="Docker engine:"
armbian-config --cmd CON002
~~~


~~~ custombash title="Docker remove:"
armbian-config --cmd CON003
~~~


~~~ custombash title="Docker purge with all images, containers, and volumes:"
armbian-config --cmd CON004
~~~


~~~ custombash title="Portainer container management platform:"
armbian-config --cmd CON005
~~~


<!--- footer START from tools/include/markdown/CON005-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9002**:

    - URL = `http://<your.IP>:9002`

<!--- footer STOP from tools/include/markdown/CON005-footer.md --->


~~~ custombash title="Portainer remove:"
armbian-config --cmd CON006
~~~


~~~ custombash title="Portainer purge with with data folder:"
armbian-config --cmd CON007
~~~

## Media servers, organizers and editors

## Emby organizes video, music, live TV, and photos

**Author:** @schwar3kat

**Status:** Stable


<!--- section image START from tools/include/images/MED003.png --->
[![Emby organizes video, music, live TV, and photos](/images/MED003.png)](#)
<!--- section image STOP from tools/include/images/MED003.png --->


<!--- header START from tools/include/markdown/MED003-header.md --->
Emby organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

<!--- header STOP from tools/include/markdown/MED003-header.md --->


~~~ custombash title="Emby organizes video, music, live TV, and photos:"
armbian-config --cmd MED003
~~~


<!--- footer START from tools/include/markdown/MED003-footer.md --->
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

<!--- footer STOP from tools/include/markdown/MED003-footer.md --->


~~~ custombash title="Emby server remove:"
armbian-config --cmd MED004
~~~


~~~ custombash title="Emby server purge with data folder:"
armbian-config --cmd MED005
~~~


~~~ custombash title="Stirling PDF tools for viewing and editing PDF files:"
armbian-config --cmd MED010
~~~


<!--- footer START from tools/include/markdown/MED010-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8077**:

    - URL: `https://<your.IP>:8077`

=== "Directories"

    - Install directory: `/armbian/stirling`

=== "View logs"

    ```sh
    docker logs -f stirling-pdf
    ```

<!--- footer STOP from tools/include/markdown/MED010-footer.md --->


~~~ custombash title="Stirling PDF remove:"
armbian-config --cmd MED011
~~~


~~~ custombash title="Stirling PDF purge with data folder:"
armbian-config --cmd MED012
~~~


~~~ custombash title="Syncthing continuous file synchronization:"
armbian-config --cmd MED015
~~~


<!--- footer START from tools/include/markdown/MED015-footer.md --->
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

<!--- footer STOP from tools/include/markdown/MED015-footer.md --->


~~~ custombash title="Syncthing remove:"
armbian-config --cmd MED016
~~~


~~~ custombash title="Syncthing purge with data folder:"
armbian-config --cmd MED017
~~~


~~~ custombash title="Nextcloud content collaboration platform:"
armbian-config --cmd MED020
~~~


<!--- footer START from tools/include/markdown/MED020-footer.md --->
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

<!--- footer STOP from tools/include/markdown/MED020-footer.md --->


~~~ custombash title="Nextcloud remove:"
armbian-config --cmd MED021
~~~


~~~ custombash title="Nextcloud purge with data folder:"
armbian-config --cmd MED022
~~~


~~~ custombash title="Owncloud share files and folders, easy and secure:"
armbian-config --cmd MED025
~~~


~~~ custombash title="Owncloud remove:"
armbian-config --cmd MED026
~~~


~~~ custombash title="Owncloud purge with data folder:"
armbian-config --cmd MED027
~~~


<!--- footer START from tools/include/markdown/MED027-footer.md --->
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

<!--- footer STOP from tools/include/markdown/MED027-footer.md --->


~~~ custombash title="Jellyfin Media System:"
armbian-config --cmd MED030
~~~


<!--- footer START from tools/include/markdown/MED030-footer.md --->
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

<!--- footer STOP from tools/include/markdown/MED030-footer.md --->


~~~ custombash title="Jellyfin remove:"
armbian-config --cmd MED031
~~~


~~~ custombash title="Jellyfin purge with data folder:"
armbian-config --cmd MED032
~~~


~~~ custombash title="Hastebin Paste Server:"
armbian-config --cmd MED033
~~~


~~~ custombash title="Hastebin remove:"
armbian-config --cmd MED034
~~~


~~~ custombash title="Hastebin purge with data folder:"
armbian-config --cmd MED035
~~~

## Real-time monitoring, collecting metrics, up-time status

## Uptime Kuma self-hosted monitoring tool

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/UPK001.webp --->
[![Uptime Kuma self-hosted monitoring tool](/images/UPK001.webp)](#)
<!--- section image STOP from tools/include/images/UPK001.webp --->


<!--- header START from tools/include/markdown/UPK001-header.md --->
[Uptime Kuma](https://github.com/louislam/uptime-kuma) is a self-hosted monitoring tool similar to \"Uptime Robot\". 
It provides a beautiful, easy-to-use web dashboard to monitor HTTP(s), TCP, Ping, and more types of services.

You can receive instant notifications when a service goes down via Telegram, Discord, Slack, email, and many other integrations.

<!--- header STOP from tools/include/markdown/UPK001-header.md --->


~~~ custombash title="Uptime Kuma self-hosted monitoring tool:"
armbian-config --cmd UPK001
~~~


<!--- footer START from tools/include/markdown/UPK001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3001**:

    - URL: `https://<your.IP>:3001`
    - Username/Password: Are set at first web interface login

=== "Features"

    - Monitor uptime and response time of any service
    - Beautiful graphs and charts for history
    - Supports HTTP, HTTPS, TCP, ICMP Ping, DNS queries, and more
    - Multiple notification integrations
    - Docker-ready and lightweight

=== "Requirements"

    - Ports open on firewall if accessed externally

=== "Official Documentation"

    - <https://github.com/louislam/uptime-kuma>

<!--- footer STOP from tools/include/markdown/UPK001-footer.md --->


~~~ custombash title="Uptime Kuma remove:"
armbian-config --cmd UPK002
~~~


~~~ custombash title="Uptime Kuma purge with data folder:"
armbian-config --cmd UPK003
~~~

## Netdata - monitoring real-time metrics

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/MON005.png --->
[![Netdata - monitoring real-time metrics](/images/MON005.png)](#)
<!--- section image STOP from tools/include/images/MON005.png --->


<!--- header START from tools/include/markdown/MON005-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/MON005-header.md --->


~~~ custombash title="Netdata - monitoring real-time metrics:"
armbian-config --cmd MON005
~~~


~~~ custombash title="Netdata remove:"
armbian-config --cmd MON006
~~~


~~~ custombash title="Netdata purge with data folder:"
armbian-config --cmd MON007
~~~

## Grafana data analytics

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/GRA001.png --->
[![Grafana data analytics](/images/GRA001.png)](#)
<!--- section image STOP from tools/include/images/GRA001.png --->


<!--- header START from tools/include/markdown/GRA001-header.md --->
Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.
<!--- header STOP from tools/include/markdown/GRA001-header.md --->


~~~ custombash title="Grafana data analytics:"
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


~~~ custombash title="Grafana remove:"
armbian-config --cmd GRA002
~~~


~~~ custombash title="Grafana purge with data folder:"
armbian-config --cmd GRA003
~~~

## Prometheus docker image

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/PRO001.png --->
[![Prometheus docker image](/images/PRO001.png)](#)
<!--- section image STOP from tools/include/images/PRO001.png --->


<!--- header START from tools/include/markdown/PRO001-header.md --->
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects and stores time-series data, provides powerful query capabilities, and enables real-time alerts based on defined conditions. Commonly used in cloud and containerized environments, Prometheus integrates seamlessly with Kubernetes and other modern infrastructure.

<!--- header STOP from tools/include/markdown/PRO001-header.md --->


~~~ custombash title="Prometheus docker image:"
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


~~~ custombash title="Prometheus remove:"
armbian-config --cmd PRO002
~~~


~~~ custombash title="Prometheus purge with data folder:"
armbian-config --cmd PRO003
~~~

## Remote File & Management tools

## Cockpit web-based management tool

**Author:** @Tearran

**Status:** Stable


<!--- section image START from tools/include/images/MAN001.png --->
[![Cockpit web-based management tool](/images/MAN001.png)](#)
<!--- section image STOP from tools/include/images/MAN001.png --->


~~~ custombash title="Cockpit web-based management tool:"
armbian-config --cmd MAN001
~~~


<!--- footer START from tools/include/markdown/MAN001-footer.md --->
Introducing Cockpit
Cockpit is a web-based graphical interface for servers, intended for everyone, especially those who are:

- new to Linux
(including Windows admins)
- familiar with Linux
and want an easy, graphical way to administer servers
- expert admins
who mainly use other tools but want an overview on individual systems

Thanks to Cockpit intentionally using system APIs and commands, a whole team of admins can manage a system in the way they prefer, including the command line and utilities right alongside Cockpit.
<!--- footer STOP from tools/include/markdown/MAN001-footer.md --->


~~~ custombash title="SAMBA Remote File share:"
armbian-config --cmd MAN002
~~~


~~~ custombash title="Webmin web-based management tool:"
armbian-config --cmd MAN005
~~~


<!--- footer START from tools/include/markdown/MAN005-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **10000**:

    - URL: `https://<your.IP>:10000`
    - Username/Password: your system login credentials


<!--- footer STOP from tools/include/markdown/MAN005-footer.md --->

## Tools for printing and 3D printing

## OctoPrint web-based 3D printers management tool

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/OCT001.png --->
[![OctoPrint web-based 3D printers management tool](/images/OCT001.png)](#)
<!--- section image STOP from tools/include/images/OCT001.png --->


<!--- header START from tools/include/markdown/OCT001-header.md --->
OctoPrint is an open source 3D printer controller application, which provides a web interface for the connected printers. It displays printers status and key parameters and allows user to schedule prints and remotely control the printer.
<!--- header STOP from tools/include/markdown/OCT001-header.md --->


~~~ custombash title="OctoPrint web-based 3D printers management tool:"
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


~~~ custombash title="OctoPrint remove:"
armbian-config --cmd OCT002
~~~


~~~ custombash title="OctoPrint purge with data folder:"
armbian-config --cmd OCT003
~~~

## Console network tools for measuring load and bandwidth

## nload -realtime console network usage monitor

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/NET001.png --->
[![nload -realtime console network usage monitor](/images/NET001.png)](#)
<!--- section image STOP from tools/include/images/NET001.png --->


<!--- header START from tools/include/markdown/NET001-header.md --->
``` mermaid
graph LR
  A{Select interface} --> B[Configure];
  A{Select interface} --> C[Drop];
  C ---->A;
  B -->F[DHCP];
  B ---->G[Static];
  G ------>| MAC, IP, route, GW, DNS|H[Configured];
  F -->| MAC | H[Configured];
```

<!--- header STOP from tools/include/markdown/NET001-header.md --->


~~~ custombash title="nload -realtime console network usage monitor:"
armbian-config --cmd NET001
~~~


<!--- footer START from tools/include/markdown/NET001-footer.md --->
1. **Select Interface:**
   - Launch the `armbian-config` utility:
     ```bash
     sudo armbian-config
     ```
   - Navigate to `Network` and choose the desired network interface (e.g., `eth0` for wired or `wlan0` for wireless).

2. **Wireless Interface Configuration:**
   - If configuring a wireless interface:
     - A list of available Access Points (APs) will be displayed.
     - Select your preferred AP and enter the password when prompted. Leave the password field empty for open networks.

3. **IP Address Configuration:**
   - Choose between:
     - **DHCP (Dynamic Host Configuration Protocol):** Automatically assigns an IP address.
     - **Static IP:** Manually enter details:
       - **MAC Address (optional):** Specify if you want spoofing MAC address.
       - **IP Address:** Use CIDR notation (e.g., `192.168.1.10/24`).
       - **Route:** Default is `0.0.0.0/0`.
       - **Gateway:** Typically the router's IP, e.g., `192.168.1.1`.
       - **DNS:** Default is `9.9.9.9`, but can be changed.

4. **Finalize Configuration:**
   - Review and confirm your settings.
   - The system applies the configurations, and your network should be set up.
<!--- footer STOP from tools/include/markdown/NET001-footer.md --->


~~~ custombash title="nload - remove:"
armbian-config --cmd NET002
~~~


~~~ custombash title="iperf3 bandwidth measuring tool:"
armbian-config --cmd NET003
~~~


~~~ custombash title="iperf3 remove:"
armbian-config --cmd NET004
~~~


~~~ custombash title="iptraf-ng IP LAN monitor:"
armbian-config --cmd NET005
~~~


~~~ custombash title="iptraf-ng remove:"
armbian-config --cmd NET006
~~~


~~~ custombash title="avahi-daemon hostname broadcast via mDNS:"
armbian-config --cmd NET007
~~~


~~~ custombash title="avahi-daemon hostname broadcast via mDNS:"
armbian-config --cmd NET007
~~~


~~~ custombash title="avahi-daemon hostname broadcast via mDNS:"
armbian-config --cmd NET007
~~~


~~~ custombash title="avahi-daemon hostname broadcast via mDNS:"
armbian-config --cmd NET007
~~~


~~~ custombash title="avahi-daemon remove:"
armbian-config --cmd NET008
~~~


~~~ custombash title="avahi-daemon remove:"
armbian-config --cmd NET008
~~~

## VPN tools

## ZeroTier connect devices over your own private network in the world.

**Author:** @jnovos

**Status:** Stable


~~~ custombash title="ZeroTier connect devices over your own private network in the world.:"
armbian-config --cmd VPN001
~~~
