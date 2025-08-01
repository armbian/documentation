---
comments: true
---

# Media servers, organizers and editors

## Emby


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

    The web interface is accessible via port **8091**:

    - URL: `https://<your.IP>:8091`

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




## Filebrowser


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




## Hastebin


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




## Immich


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




## Jellyfin


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




## Navidrome


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




## Nextcloud


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

    The web interface is accessible via port **1443**:

    - URL: `https://<your.IP>:1443`
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




## OMV


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



## Owncloud


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




## Syncthing


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




## Stirling


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

    The web interface is accessible via port **8075**:

    - URL: `https://<your.IP>:8075`

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



