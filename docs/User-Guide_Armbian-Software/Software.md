---
comments: true
---

# Run/Install 3rd party applications

## Web server, LEMP, reverse proxy, Let's Encrypt SSL

### SWAG reverse proxy

**Status:** Stable

**Author:** @armbian


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


~~~ bash title="SWAG reverse proxy:"
armbian-config --cmd SWAG01
~~~

### SWAG reverse proxy .htpasswd set


~~~ bash title="SWAG reverse proxy .htpasswd set:"
armbian-config --cmd SWAG02
~~~

### SWAG remove


~~~ bash title="SWAG remove:"
armbian-config --cmd SWAG03
~~~

### SWAG purge with data folder


~~~ bash title="SWAG purge with data folder:"
armbian-config --cmd SWAG04
~~~

## Home Automation for control home appliances

### openHAB empowering the smart home

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/HAB001.png --->
[![openHAB empowering the smart home](/images/HAB001.png)](#)
<!--- section image STOP from tools/include/images/HAB001.png --->


~~~ bash title="openHAB empowering the smart home:"
armbian-config --cmd HAB001
~~~

### openHAB remove


~~~ bash title="openHAB remove:"
armbian-config --cmd HAB002
~~~

### openHAB purge with data folder


~~~ bash title="openHAB purge with data folder:"
armbian-config --cmd HAB003
~~~

### Home Assistant open source home automation


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


~~~ bash title="Home Assistant open source home automation:"
armbian-config --cmd HAS001
~~~

### Home Assistant remove


~~~ bash title="Home Assistant remove:"
armbian-config --cmd HAS002
~~~

### Home Assistant purge with data folder


~~~ bash title="Home Assistant purge with data folder:"
armbian-config --cmd HAS003
~~~

### Domoticz open source home automation


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


~~~ bash title="Domoticz open source home automation:"
armbian-config --cmd DOM001
~~~

### Domoticz remove


~~~ bash title="Domoticz remove:"
armbian-config --cmd DOM002
~~~

### Domoticz purge with data folder


~~~ bash title="Domoticz purge with data folder:"
armbian-config --cmd DOM003
~~~

### EVCC - solar charging automation


<!--- section image START from tools/include/images/EVCC01.png --->
[![EVCC - solar charging automation](/images/EVCC01.png)](#)
<!--- section image STOP from tools/include/images/EVCC01.png --->


<!--- header START from tools/include/markdown/EVCC01-header.md --->
evcc is an energy management system with a focus on electromobility. The software controls your EV charger or smart plug. It communicates with your vehicle, inverter or home storage to make intelligent charging decisions. The software is open source and community-driven.

<!--- header STOP from tools/include/markdown/EVCC01-header.md --->


~~~ bash title="EVCC - solar charging automation:"
armbian-config --cmd EVCC01
~~~

### EVCC - solar charging automation remove


~~~ bash title="EVCC - solar charging automation remove:"
armbian-config --cmd EVCC02
~~~

### EVCC purge with data folder


~~~ bash title="EVCC purge with data folder:"
armbian-config --cmd EVCC03
~~~

## Network-wide ad blockers servers

### Pi-hole DNS ad blocker

**Status:** Stable

**Author:** @armbian


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


~~~ bash title="Pi-hole DNS ad blocker:"
armbian-config --cmd DNS001
~~~

### Pi-hole remove


~~~ bash title="Pi-hole remove:"
armbian-config --cmd DNS003
~~~

### Pi-hole change web admin password


~~~ bash title="Pi-hole change web admin password:"
armbian-config --cmd DNS002
~~~

### Pi-hole purge with data folder


~~~ bash title="Pi-hole purge with data folder:"
armbian-config --cmd DNS004
~~~

### Unbound caching DNS resolver


<!--- section image START from tools/include/images/UNB001.png --->
[![Unbound caching DNS resolver](/images/UNB001.png)](#)
<!--- section image STOP from tools/include/images/UNB001.png --->


<!--- header START from tools/include/markdown/UNB001-header.md --->
Unbound is a high-performance, open-source DNS resolver. It primarily serves to resolve domain names into IP addresses for devices on a network. Unlike regular DNS servers, Unbound performs DNS lookups directly and securely, providing features like DNSSEC validation (ensuring data integrity) and privacy protections. It's often used to improve speed, security, and privacy by resolving queries locally rather than relying on external DNS services.
<!--- header STOP from tools/include/markdown/UNB001-header.md --->


~~~ bash title="Unbound caching DNS resolver:"
armbian-config --cmd UNB001
~~~

### Unbound remove


~~~ bash title="Unbound remove:"
armbian-config --cmd UNB002
~~~

### Unbound purge with data folder


~~~ bash title="Unbound purge with data folder:"
armbian-config --cmd UNB003
~~~

### AdGuardHome DNS sinkhole


<!--- section image START from tools/include/images/ADG001.png --->
[![AdGuardHome DNS sinkhole](/images/ADG001.png)](#)
<!--- section image STOP from tools/include/images/ADG001.png --->


<!--- header START from tools/include/markdown/ADG001-header.md --->
AdGuard Home is a network-wide software that functions as a DNS server and ad blocker. It blocks ads, trackers, and malicious websites at the DNS level, meaning it filters content for all devices connected to the network. It also provides additional features like parental controls, logging, and privacy protections. Essentially, it acts as a gateway between your devices and the internet, blocking unwanted content before it even reaches your devices.

<!--- header STOP from tools/include/markdown/ADG001-header.md --->


~~~ bash title="AdGuardHome DNS sinkhole:"
armbian-config --cmd ADG001
~~~

### AdGuardHome remove


~~~ bash title="AdGuardHome remove:"
armbian-config --cmd ADG002
~~~

### AdGuardHome purge with data folder


~~~ bash title="AdGuardHome purge with data folder:"
armbian-config --cmd ADG003
~~~

## Music servers and streamers

### Navidrome music server and streamer compatible with Subsonic/Airsonic

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/NAV001.png --->
[![Navidrome music server and streamer compatible with Subsonic/Airsonic](/images/NAV001.png)](#)
<!--- section image STOP from tools/include/images/NAV001.png --->


~~~ bash title="Navidrome music server and streamer compatible with Subsonic/Airsonic:"
armbian-config --cmd NAV001
~~~

### Navidrome remove


~~~ bash title="Navidrome remove:"
armbian-config --cmd NAV002
~~~

### Navidrome purge with data folder


~~~ bash title="Navidrome purge with data folder:"
armbian-config --cmd NAV003
~~~

## Download apps for movies, TV shows, music and subtitles

### qBittorrent BitTorrent client 

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/DOW001.png --->
[![qBittorrent BitTorrent client ](/images/DOW001.png)](#)
<!--- section image STOP from tools/include/images/DOW001.png --->


<!--- header START from tools/include/markdown/DOW001-header.md --->
The Qbittorrent⁠ project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

<!--- header STOP from tools/include/markdown/DOW001-header.md --->


~~~ bash title="qBittorrent BitTorrent client :"
armbian-config --cmd DOW001
~~~

### qBittorrent remove


~~~ bash title="qBittorrent remove:"
armbian-config --cmd DOW002
~~~

### qBittorrent purge with data folder


~~~ bash title="qBittorrent purge with data folder:"
armbian-config --cmd DOW003
~~~

### Deluge BitTorrent client


<!--- section image START from tools/include/images/DEL001.png --->
[![Deluge BitTorrent client](/images/DEL001.png)](#)
<!--- section image STOP from tools/include/images/DEL001.png --->


<!--- header START from tools/include/markdown/DEL001-header.md --->
Deluge⁠ is a lightweight, Free Software, cross-platform BitTorrent client.

<!--- header STOP from tools/include/markdown/DEL001-header.md --->


~~~ bash title="Deluge BitTorrent client:"
armbian-config --cmd DEL001
~~~

### Deluge remove


~~~ bash title="Deluge remove:"
armbian-config --cmd DEL002
~~~

### Deluge purge with data folder


~~~ bash title="Deluge purge with data folder:"
armbian-config --cmd DEL003
~~~

### Transmission BitTorrent client


<!--- section image START from tools/include/images/TRA001.png --->
[![Transmission BitTorrent client](/images/TRA001.png)](#)
<!--- section image STOP from tools/include/images/TRA001.png --->


<!--- header START from tools/include/markdown/TRA001-header.md --->
Transmission⁠ is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

<!--- header STOP from tools/include/markdown/TRA001-header.md --->


~~~ bash title="Transmission BitTorrent client:"
armbian-config --cmd TRA001
~~~

### Transmission remove


~~~ bash title="Transmission remove:"
armbian-config --cmd TRA002
~~~

### Transmission purge with data folder


~~~ bash title="Transmission purge with data folder:"
armbian-config --cmd TRA003
~~~

### SABnzbd newsgroup downloader


<!--- section image START from tools/include/images/SABN01.png --->
[![SABnzbd newsgroup downloader](/images/SABN01.png)](#)
<!--- section image STOP from tools/include/images/SABN01.png --->


<!--- header START from tools/include/markdown/SABN01-header.md --->
Sabnzbd⁠ makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

<!--- header STOP from tools/include/markdown/SABN01-header.md --->


~~~ bash title="SABnzbd newsgroup downloader:"
armbian-config --cmd SABN01
~~~

### SABnzbd remove


~~~ bash title="SABnzbd remove:"
armbian-config --cmd SABN02
~~~

### SABnzbd purge with data folder


~~~ bash title="SABnzbd purge with data folder:"
armbian-config --cmd SABN03
~~~

### Medusa automatic downloader for TV shows


<!--- header START from tools/include/markdown/MDS001-header.md --->
Medusa is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

<!--- header STOP from tools/include/markdown/MDS001-header.md --->


~~~ bash title="Medusa automatic downloader for TV shows:"
armbian-config --cmd MDS001
~~~

### Medusa TV shows downloader remove


~~~ bash title="Medusa TV shows downloader remove:"
armbian-config --cmd MDS002
~~~

### Medusa TV shows downloader purge


~~~ bash title="Medusa TV shows downloader purge:"
armbian-config --cmd MDS003
~~~

### Sonarr automatic downloader for TV shows


<!--- section image START from tools/include/images/SON001.png --->
[![Sonarr automatic downloader for TV shows](/images/SON001.png)](#)
<!--- section image STOP from tools/include/images/SON001.png --->


<!--- header START from tools/include/markdown/SON001-header.md --->
Sonarr (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/SON001-header.md --->


~~~ bash title="Sonarr automatic downloader for TV shows:"
armbian-config --cmd SON001
~~~

### Sonarr remove


~~~ bash title="Sonarr remove:"
armbian-config --cmd SON002
~~~

### Sonarr purge with data folder


~~~ bash title="Sonarr purge with data folder:"
armbian-config --cmd SON003
~~~

### Radarr automatic downloader for movies


<!--- section image START from tools/include/images/RAD001.png --->
[![Radarr automatic downloader for movies](/images/RAD001.png)](#)
<!--- section image STOP from tools/include/images/RAD001.png --->


<!--- header START from tools/include/markdown/RAD001-header.md --->
Radarr - A fork of Sonarr to work with movies à la Couchpotato.

<!--- header STOP from tools/include/markdown/RAD001-header.md --->


~~~ bash title="Radarr automatic downloader for movies:"
armbian-config --cmd RAD001
~~~

### Radarr remove


~~~ bash title="Radarr remove:"
armbian-config --cmd RAD002
~~~

### Radarr purge with data folder


~~~ bash title="Radarr purge with data folder:"
armbian-config --cmd RAD003
~~~

### Bazarr automatic subtitles downloader for Sonarr and Radarr


<!--- section image START from tools/include/images/BAZ001.png --->
[![Bazarr automatic subtitles downloader for Sonarr and Radarr](/images/BAZ001.png)](#)
<!--- section image STOP from tools/include/images/BAZ001.png --->


<!--- header START from tools/include/markdown/BAZ001-header.md --->
Bazarr is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

<!--- header STOP from tools/include/markdown/BAZ001-header.md --->


~~~ bash title="Bazarr automatic subtitles downloader for Sonarr and Radarr:"
armbian-config --cmd BAZ001
~~~

### Bazarr remove


~~~ bash title="Bazarr remove:"
armbian-config --cmd BAZ002
~~~

### Bazarr purge with data folder


~~~ bash title="Bazarr purge with data folder:"
armbian-config --cmd BAZ003
~~~

### Lidarr automatic music downloader


<!--- section image START from tools/include/images/LID001.png --->
[![Lidarr automatic music downloader](/images/LID001.png)](#)
<!--- section image STOP from tools/include/images/LID001.png --->


<!--- header START from tools/include/markdown/LID001-header.md --->
Lidarr is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/LID001-header.md --->


~~~ bash title="Lidarr automatic music downloader:"
armbian-config --cmd LID001
~~~

### Lidarr remove


~~~ bash title="Lidarr remove:"
armbian-config --cmd LID002
~~~

### Lidarr purge with data folder


~~~ bash title="Lidarr purge with data folder:"
armbian-config --cmd LID003
~~~

### Readarr automatic downloader for Ebooks


<!--- section image START from tools/include/images/RDR001.png --->
[![Readarr automatic downloader for Ebooks](/images/RDR001.png)](#)
<!--- section image STOP from tools/include/images/RDR001.png --->


<!--- header START from tools/include/markdown/RDR001-header.md --->
Readarr - Book Manager and Automation (Sonarr for Ebooks)

<!--- header STOP from tools/include/markdown/RDR001-header.md --->


~~~ bash title="Readarr automatic downloader for Ebooks:"
armbian-config --cmd RDR001
~~~

### Readarr remove


~~~ bash title="Readarr remove:"
armbian-config --cmd RDR002
~~~

### Readarr purge with data folder


~~~ bash title="Readarr purge with data folder:"
armbian-config --cmd RDR003
~~~

### Prowlarr index manager and proxy for PVR


<!--- section image START from tools/include/images/DOW025.png --->
[![Prowlarr index manager and proxy for PVR](/images/DOW025.png)](#)
<!--- section image STOP from tools/include/images/DOW025.png --->


<!--- header START from tools/include/markdown/DOW025-header.md --->
Prowlarr is a indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Sonarr, Radarr, Lidarr, and Readarr offering complete management of your indexers with no per app Indexer setup required (we do it all).

<!--- header STOP from tools/include/markdown/DOW025-header.md --->


~~~ bash title="Prowlarr index manager and proxy for PVR:"
armbian-config --cmd DOW025
~~~

### Prowlarr remove


~~~ bash title="Prowlarr remove:"
armbian-config --cmd DOW026
~~~

### Prowlarr purge with data folder


~~~ bash title="Prowlarr purge with data folder:"
armbian-config --cmd DOW027
~~~

### Jellyseerr Jellyfin/Emby/Plex integration install


<!--- section image START from tools/include/images/JEL001.png --->
[![Jellyseerr Jellyfin/Emby/Plex integration install](/images/JEL001.png)](#)
<!--- section image STOP from tools/include/images/JEL001.png --->


<!--- header START from tools/include/markdown/JEL001-header.md --->
Jellyseerr is a free and open source software application for managing requests for your media library. It is a fork of Overseerr built to bring support for Jellyfin & Emby media servers!

<!--- header STOP from tools/include/markdown/JEL001-header.md --->


~~~ bash title="Jellyseerr Jellyfin/Emby/Plex integration install:"
armbian-config --cmd JEL001
~~~

### Jellyseerr remove


~~~ bash title="Jellyseerr remove:"
armbian-config --cmd JEL002
~~~

### Jellyseerr purge with data folder


~~~ bash title="Jellyseerr purge with data folder:"
armbian-config --cmd JEL003
~~~

## SQL database servers and web interface managers

### Mariadb SQL database server

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/DAT001.png --->
[![Mariadb SQL database server](/images/DAT001.png)](#)
<!--- section image STOP from tools/include/images/DAT001.png --->


<!--- header START from tools/include/markdown/DAT001-header.md --->
Mariadb is one of the most popular database servers. Made by the original developers of MySQL.

<!--- header STOP from tools/include/markdown/DAT001-header.md --->


~~~ bash title="Mariadb SQL database server:"
armbian-config --cmd DAT001
~~~

### Mariadb remove


~~~ bash title="Mariadb remove:"
armbian-config --cmd DAT002
~~~

### Mariadb purge with data folder


~~~ bash title="Mariadb purge with data folder:"
armbian-config --cmd DAT003
~~~

### phpMyAdmin web interface manager


<!--- section image START from tools/include/images/DAT005.png --->
[![phpMyAdmin web interface manager](/images/DAT005.png)](#)
<!--- section image STOP from tools/include/images/DAT005.png --->


<!--- header START from tools/include/markdown/DAT005-header.md --->
Phpmyadmin is a free software tool written in PHP, intended to handle the administration of MySQL over the Web. phpMyAdmin supports a wide range of operations on MySQL and MariaDB.

<!--- header STOP from tools/include/markdown/DAT005-header.md --->


~~~ bash title="phpMyAdmin web interface manager:"
armbian-config --cmd DAT005
~~~

### phpMyAdmin remove


~~~ bash title="phpMyAdmin remove:"
armbian-config --cmd DAT006
~~~

### phpMyAdmin purge with data folder


~~~ bash title="phpMyAdmin purge with data folder:"
armbian-config --cmd DAT007
~~~

## Applications and tools for development

### Install tools for cloning and managing repositories (git)

**Status:** Stable

**Author:** @armbian


~~~ bash title="Install tools for cloning and managing repositories (git):"
armbian-config --cmd DEV001
~~~


~~~ bash title="Install tools for cloning and managing repositories (git):"
armbian-config --cmd DEV001
~~~

### Remove tools for cloning and managing repositories (git)


~~~ bash title="Remove tools for cloning and managing repositories (git):"
armbian-config --cmd DEV002
~~~


~~~ bash title="Remove tools for cloning and managing repositories (git):"
armbian-config --cmd DEV002
~~~

### Armbian router for repository mirror automation


~~~ bash title="Armbian router for repository mirror automation:"
armbian-config --cmd DEV003
~~~

### Remove Armbian router


~~~ bash title="Remove Armbian router:"
armbian-config --cmd DEV004
~~~

### Armbian rsyncd server


~~~ bash title="Armbian rsyncd server:"
armbian-config --cmd DEV010
~~~

### Remove Armbian rsyncd server


~~~ bash title="Remove Armbian rsyncd server:"
armbian-config --cmd DEV011
~~~

## Docker containerization and KVM virtual machines

### Docker minimal

**Status:** Stable

**Author:** @schwar3kat


<!--- section image START from tools/include/images/CON001.webp --->
[![Docker minimal](/images/CON001.webp)](#)
<!--- section image STOP from tools/include/images/CON001.webp --->


~~~ bash title="Docker minimal:"
armbian-config --cmd CON001
~~~

### Docker engine


~~~ bash title="Docker engine:"
armbian-config --cmd CON002
~~~

### Docker remove


~~~ bash title="Docker remove:"
armbian-config --cmd CON003
~~~

### Docker purge with all images, containers, and volumes


~~~ bash title="Docker purge with all images, containers, and volumes:"
armbian-config --cmd CON004
~~~

### Portainer container management platform


<!--- section image START from tools/include/images/CON005.webp --->
[![Portainer container management platform](/images/CON005.webp)](#)
<!--- section image STOP from tools/include/images/CON005.webp --->


<!--- header START from tools/include/markdown/CON005-header.md --->
Portainer simplifies your Docker container management via Portainer web interface. It enables faster deploy of the applications and it gives real time visibility.

<!--- header STOP from tools/include/markdown/CON005-header.md --->


~~~ bash title="Portainer container management platform:"
armbian-config --cmd CON005
~~~

### Portainer remove


~~~ bash title="Portainer remove:"
armbian-config --cmd CON006
~~~

### Portainer purge with with data folder


~~~ bash title="Portainer purge with with data folder:"
armbian-config --cmd CON007
~~~

## Media servers, organizers and editors

### Emby organizes video, music, live TV, and photos

**Status:** Stable

**Author:** @schwar3kat


<!--- section image START from tools/include/images/MED003.png --->
[![Emby organizes video, music, live TV, and photos](/images/MED003.png)](#)
<!--- section image STOP from tools/include/images/MED003.png --->


<!--- header START from tools/include/markdown/MED003-header.md --->
Emby organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

<!--- header STOP from tools/include/markdown/MED003-header.md --->


~~~ bash title="Emby organizes video, music, live TV, and photos:"
armbian-config --cmd MED003
~~~

### Emby server remove


~~~ bash title="Emby server remove:"
armbian-config --cmd MED004
~~~

### Emby server purge with data folder


~~~ bash title="Emby server purge with data folder:"
armbian-config --cmd MED005
~~~

### Stirling PDF tools for viewing and editing PDF files


<!--- section image START from tools/include/images/MED010.png --->
[![Stirling PDF tools for viewing and editing PDF files](/images/MED010.png)](#)
<!--- section image STOP from tools/include/images/MED010.png --->


<!--- header START from tools/include/markdown/MED010-header.md --->
Stirling-PDF is a robust, locally hosted web-based PDF manipulation tool using Docker. It enables you to carry out various operations on PDF files, including splitting, merging, converting, reorganizing, adding images, rotating, compressing, and more. This locally hosted web application has evolved to encompass a comprehensive set of features, addressing all your PDF requirements.

<!--- header STOP from tools/include/markdown/MED010-header.md --->


~~~ bash title="Stirling PDF tools for viewing and editing PDF files:"
armbian-config --cmd MED010
~~~

### Stirling PDF remove


~~~ bash title="Stirling PDF remove:"
armbian-config --cmd MED011
~~~

### Stirling PDF purge with data folder


~~~ bash title="Stirling PDF purge with data folder:"
armbian-config --cmd MED012
~~~

### Syncthing continuous file synchronization


<!--- section image START from tools/include/images/MED015.png --->
[![Syncthing continuous file synchronization](/images/MED015.png)](#)
<!--- section image STOP from tools/include/images/MED015.png --->


<!--- header START from tools/include/markdown/MED015-header.md --->
Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

<!--- header STOP from tools/include/markdown/MED015-header.md --->


~~~ bash title="Syncthing continuous file synchronization:"
armbian-config --cmd MED015
~~~

### Syncthing remove


~~~ bash title="Syncthing remove:"
armbian-config --cmd MED016
~~~

### Syncthing purge with data folder


~~~ bash title="Syncthing purge with data folder:"
armbian-config --cmd MED017
~~~

### Nextcloud content collaboration platform


<!--- section image START from tools/include/images/MED020.png --->
[![Nextcloud content collaboration platform](/images/MED020.png)](#)
<!--- section image STOP from tools/include/images/MED020.png --->


<!--- header START from tools/include/markdown/MED020-header.md --->
Nextcloud gives you access to all your files wherever you are.
<br>
Where are your photos and documents? With Nextcloud you pick a server of your choice, at home, in a data center or at a provider. And that is where your files will be. Nextcloud runs on that server, protecting your data and giving you access from your desktop or mobile devices. Through Nextcloud you also access, sync and share your existing data on that FTP drive at the office, a Dropbox or a NAS you have at home.

<!--- header STOP from tools/include/markdown/MED020-header.md --->


~~~ bash title="Nextcloud content collaboration platform:"
armbian-config --cmd MED020
~~~

### Nextcloud remove


~~~ bash title="Nextcloud remove:"
armbian-config --cmd MED021
~~~

### Nextcloud purge with data folder


~~~ bash title="Nextcloud purge with data folder:"
armbian-config --cmd MED022
~~~

### Owncloud share files and folders, easy and secure


~~~ bash title="Owncloud share files and folders, easy and secure:"
armbian-config --cmd MED025
~~~

### Owncloud remove


~~~ bash title="Owncloud remove:"
armbian-config --cmd MED026
~~~

### Owncloud purge with data folder


<!--- header START from tools/include/markdown/MED027-header.md --->
ownCloud is a free and open-source software project for content collaboration and sharing and syncing of files in distributed and federated enterprise scenarios.

<!--- header STOP from tools/include/markdown/MED027-header.md --->


~~~ bash title="Owncloud purge with data folder:"
armbian-config --cmd MED027
~~~

### Jellyfin Media System


<!--- section image START from tools/include/images/MED030.png --->
[![Jellyfin Media System](/images/MED030.png)](#)
<!--- section image STOP from tools/include/images/MED030.png --->


<!--- header START from tools/include/markdown/MED030-header.md --->
Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it.

<!--- header STOP from tools/include/markdown/MED030-header.md --->


~~~ bash title="Jellyfin Media System:"
armbian-config --cmd MED030
~~~

### Jellyfin remove


~~~ bash title="Jellyfin remove:"
armbian-config --cmd MED031
~~~

### Jellyfin purge with data folder


~~~ bash title="Jellyfin purge with data folder:"
armbian-config --cmd MED032
~~~

### Hastebin Paste Server


~~~ bash title="Hastebin Paste Server:"
armbian-config --cmd MED033
~~~

### Hastebin remove


~~~ bash title="Hastebin remove:"
armbian-config --cmd MED034
~~~

### Hastebin purge with data folder


~~~ bash title="Hastebin purge with data folder:"
armbian-config --cmd MED035
~~~

## Real-time monitoring, collecting metrics, up-time status

### Uptime Kuma self-hosted monitoring tool

**Status:** Stable

**Author:** @igorpecovnik


<!--- section image START from tools/include/images/MON001.webp --->
[![Uptime Kuma self-hosted monitoring tool](/images/MON001.webp)](#)
<!--- section image STOP from tools/include/images/MON001.webp --->


~~~ bash title="Uptime Kuma self-hosted monitoring tool:"
armbian-config --cmd MON001
~~~

### Uptime Kuma remove


~~~ bash title="Uptime Kuma remove:"
armbian-config --cmd MON002
~~~

### Uptime Kuma purge with data folder


~~~ bash title="Uptime Kuma purge with data folder:"
armbian-config --cmd MON003
~~~

### Netdata - monitoring real-time metrics


<!--- section image START from tools/include/images/MON005.png --->
[![Netdata - monitoring real-time metrics](/images/MON005.png)](#)
<!--- section image STOP from tools/include/images/MON005.png --->


<!--- header START from tools/include/markdown/MON005-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/MON005-header.md --->


~~~ bash title="Netdata - monitoring real-time metrics:"
armbian-config --cmd MON005
~~~

### Netdata remove


~~~ bash title="Netdata remove:"
armbian-config --cmd MON006
~~~

### Netdata purge with data folder


~~~ bash title="Netdata purge with data folder:"
armbian-config --cmd MON007
~~~

### Grafana data analytics


<!--- section image START from tools/include/images/GRA001.png --->
[![Grafana data analytics](/images/GRA001.png)](#)
<!--- section image STOP from tools/include/images/GRA001.png --->


<!--- header START from tools/include/markdown/GRA001-header.md --->
Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.
<!--- header STOP from tools/include/markdown/GRA001-header.md --->


~~~ bash title="Grafana data analytics:"
armbian-config --cmd GRA001
~~~

### Grafana remove


~~~ bash title="Grafana remove:"
armbian-config --cmd GRA002
~~~

### Grafana purge with data folder


~~~ bash title="Grafana purge with data folder:"
armbian-config --cmd GRA003
~~~

### Prometheus docker image


<!--- section image START from tools/include/images/PRO001.png --->
[![Prometheus docker image](/images/PRO001.png)](#)
<!--- section image STOP from tools/include/images/PRO001.png --->


<!--- header START from tools/include/markdown/PRO001-header.md --->
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects and stores time-series data, provides powerful query capabilities, and enables real-time alerts based on defined conditions. Commonly used in cloud and containerized environments, Prometheus integrates seamlessly with Kubernetes and other modern infrastructure.

<!--- header STOP from tools/include/markdown/PRO001-header.md --->


~~~ bash title="Prometheus docker image:"
armbian-config --cmd PRO001
~~~

### Prometheus remove


~~~ bash title="Prometheus remove:"
armbian-config --cmd PRO002
~~~

### Prometheus purge with data folder


~~~ bash title="Prometheus purge with data folder:"
armbian-config --cmd PRO003
~~~

## Remote File & Management tools

### Cockpit web-based management tool

**Status:** Stable

**Author:** @Tearran


<!--- section image START from tools/include/images/MAN001.png --->
[![Cockpit web-based management tool](/images/MAN001.png)](#)
<!--- section image STOP from tools/include/images/MAN001.png --->


~~~ bash title="Cockpit web-based management tool:"
armbian-config --cmd MAN001
~~~

### SAMBA Remote File share


~~~ bash title="SAMBA Remote File share:"
armbian-config --cmd MAN002
~~~

### Webmin web-based management tool


<!--- section image START from tools/include/images/MAN005.png --->
[![Webmin web-based management tool](/images/MAN005.png)](#)
<!--- section image STOP from tools/include/images/MAN005.png --->


~~~ bash title="Webmin web-based management tool:"
armbian-config --cmd MAN005
~~~

## Tools for printing and 3D printing

### OctoPrint web-based 3D printers management tool

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/OCT001.png --->
[![OctoPrint web-based 3D printers management tool](/images/OCT001.png)](#)
<!--- section image STOP from tools/include/images/OCT001.png --->


<!--- header START from tools/include/markdown/OCT001-header.md --->
OctoPrint is an open source 3D printer controller application, which provides a web interface for the connected printers. It displays printers status and key parameters and allows user to schedule prints and remotely control the printer.
<!--- header STOP from tools/include/markdown/OCT001-header.md --->


~~~ bash title="OctoPrint web-based 3D printers management tool:"
armbian-config --cmd OCT001
~~~

### OctoPrint remove


~~~ bash title="OctoPrint remove:"
armbian-config --cmd OCT002
~~~

### OctoPrint purge with data folder


~~~ bash title="OctoPrint purge with data folder:"
armbian-config --cmd OCT003
~~~

## Console network tools for measuring load and bandwidth

### nload -realtime console network usage monitor

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/NET001.png --->
[![nload -realtime console network usage monitor](/images/NET001.png)](#)
<!--- section image STOP from tools/include/images/NET001.png --->


~~~ bash title="nload -realtime console network usage monitor:"
armbian-config --cmd NET001
~~~

### nload - remove


~~~ bash title="nload - remove:"
armbian-config --cmd NET002
~~~

### iperf3 bandwidth measuring tool


<!--- section image START from tools/include/images/NET003.png --->
[![iperf3 bandwidth measuring tool](/images/NET003.png)](#)
<!--- section image STOP from tools/include/images/NET003.png --->


~~~ bash title="iperf3 bandwidth measuring tool:"
armbian-config --cmd NET003
~~~

### iperf3 remove


~~~ bash title="iperf3 remove:"
armbian-config --cmd NET004
~~~

### iptraf-ng IP LAN monitor


~~~ bash title="iptraf-ng IP LAN monitor:"
armbian-config --cmd NET005
~~~

### iptraf-ng remove


~~~ bash title="iptraf-ng remove:"
armbian-config --cmd NET006
~~~

### avahi-daemon hostname broadcast via mDNS


~~~ bash title="avahi-daemon hostname broadcast via mDNS:"
armbian-config --cmd NET007
~~~


~~~ bash title="avahi-daemon hostname broadcast via mDNS:"
armbian-config --cmd NET007
~~~


~~~ bash title="avahi-daemon hostname broadcast via mDNS:"
armbian-config --cmd NET007
~~~


~~~ bash title="avahi-daemon hostname broadcast via mDNS:"
armbian-config --cmd NET007
~~~

### avahi-daemon remove


~~~ bash title="avahi-daemon remove:"
armbian-config --cmd NET008
~~~


~~~ bash title="avahi-daemon remove:"
armbian-config --cmd NET008
~~~

## VPN tools

### ZeroTier connect devices over your own private network in the world.

**Status:** Stable

**Author:** @jnovos


~~~ bash title="ZeroTier connect devices over your own private network in the world.:"
armbian-config --cmd VPN001
~~~
