# P2P download managers for movies, TV shows, music and subtitles


***

## qBittorrent BitTorrent server 

<!--- section image START from tools/include/images/DOW001.png --->
[![qBittorrent BitTorrent server ](/images/DOW001.png)](#)
<!--- section image STOP from tools/include/images/DOW001.png --->


<!--- header START from tools/include/markdown/DOW001-header.md --->
The Qbittorrent⁠ project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

<!--- header STOP from tools/include/markdown/DOW001-header.md --->

This operation will install qBittorrent BitTorrent server

**Command:** 
~~~
armbian-config --cmd DOW001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## qBittorrent remove
This operation will remove qBittorrent BitTorrent server

**Command:** 
~~~
armbian-config --cmd DOW002
~~~

**Author:** @armbian

**Status:** Stable



***

## qBittorrent purge with data folder
This operation will remove qBittorrent BitTorrent data folder

**Command:** 
~~~
armbian-config --cmd DOW003
~~~

**Author:** @armbian

**Status:** Stable



***

## Deluge BitTorrent server

<!--- section image START from tools/include/images/DEL001.png --->
[![Deluge BitTorrent server](/images/DEL001.png)](#)
<!--- section image STOP from tools/include/images/DEL001.png --->


<!--- header START from tools/include/markdown/DEL001-header.md --->
Deluge⁠ is a lightweight, Free Software, cross-platform BitTorrent client.

<!--- header STOP from tools/include/markdown/DEL001-header.md --->

This operation will install BitTorrent server

**Command:** 
~~~
armbian-config --cmd DEL001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Deluge remove
This operation will remove Deluge BitTorrent server

**Command:** 
~~~
armbian-config --cmd DEL002
~~~

**Author:** @armbian

**Status:** Stable



***

## Deluge purge with data folder
This operation will remove Deluge BitTorrent server data folder

**Command:** 
~~~
armbian-config --cmd DEL003
~~~

**Author:** @armbian

**Status:** Stable



***

## Transmission BitTorrent server

<!--- section image START from tools/include/images/TRA001.png --->
[![Transmission BitTorrent server](/images/TRA001.png)](#)
<!--- section image STOP from tools/include/images/TRA001.png --->


<!--- header START from tools/include/markdown/TRA001-header.md --->
Transmission⁠ is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

<!--- header STOP from tools/include/markdown/TRA001-header.md --->

This operation will install Transmission BitTorrent server

**Command:** 
~~~
armbian-config --cmd TRA001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Transmission remove
This operation will remove Transmission BitTorrent server

**Command:** 
~~~
armbian-config --cmd TRA002
~~~

**Author:** @armbian

**Status:** Stable



***

## Transmission purge with data folder
This operation will remove Transmission BitTorrent server data folder

**Command:** 
~~~
armbian-config --cmd TRA003
~~~

**Author:** @armbian

**Status:** Stable



***

## SABnzbd newsgroup downloader

<!--- section image START from tools/include/images/SABN01.png --->
[![SABnzbd newsgroup downloader](/images/SABN01.png)](#)
<!--- section image STOP from tools/include/images/SABN01.png --->


<!--- header START from tools/include/markdown/SABN01-header.md --->
Sabnzbd⁠ makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

<!--- header STOP from tools/include/markdown/SABN01-header.md --->

This operation will install SABnzbd newsgroup downloader

**Command:** 
~~~
armbian-config --cmd SABN01
~~~

**Author:** @armbian

**Status:** Stable


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



***

## SABnzbd remove
This operation will remove SABnzbd newsgroup downloader

**Command:** 
~~~
armbian-config --cmd SABN02
~~~

**Author:** @armbian

**Status:** Stable



***

## SABnzbd purge with data folder
This operation will purge SABnzbd newsgroup data folder

**Command:** 
~~~
armbian-config --cmd SABN03
~~~

**Author:** @armbian

**Status:** Stable



***

## Medusa automatic downloader for TV shows

<!--- header START from tools/include/markdown/MDS001-header.md --->
Medusa is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

<!--- header STOP from tools/include/markdown/MDS001-header.md --->

This operation will install Medusa TV shows downloader

**Command:** 
~~~
armbian-config --cmd MDS001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Medusa TV shows downloader remove
This operation will remove Medusa TV shows downloader

**Command:** 
~~~
armbian-config --cmd MDS002
~~~

**Author:** @armbian

**Status:** Stable



***

## Medusa TV shows downloader purge
This operation will purge Medusa TV shows data folder

**Command:** 
~~~
armbian-config --cmd MDS003
~~~

**Author:** @armbian

**Status:** Stable



***

## Sonarr automatic downloader for TV shows

<!--- section image START from tools/include/images/SON001.png --->
[![Sonarr automatic downloader for TV shows](/images/SON001.png)](#)
<!--- section image STOP from tools/include/images/SON001.png --->


<!--- header START from tools/include/markdown/SON001-header.md --->
Sonarr (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/SON001-header.md --->

This operation will install Sonarr PVR for Usenet and BitTorrent

**Command:** 
~~~
armbian-config --cmd SON001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Sonarr remove
This operation will remove Sonarr PVR for Usenet and BitTorrent

**Command:** 
~~~
armbian-config --cmd SON002
~~~

**Author:** @armbian

**Status:** Stable



***

## Sonarr purge with data folder
This operation will purge Sonarr PVR for Usenet and BitTorrent purge data folder

**Command:** 
~~~
armbian-config --cmd SON003
~~~

**Author:** @armbian

**Status:** Stable



***

## Radarr automatic downloader for movies

<!--- section image START from tools/include/images/RAD001.png --->
[![Radarr automatic downloader for movies](/images/RAD001.png)](#)
<!--- section image STOP from tools/include/images/RAD001.png --->


<!--- header START from tools/include/markdown/RAD001-header.md --->
Radarr - A fork of Sonarr to work with movies à la Couchpotato.

<!--- header STOP from tools/include/markdown/RAD001-header.md --->

This operation will install Radarr movie collection manager

**Command:** 
~~~
armbian-config --cmd RAD001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Radarr remove
This operation will remove Radarr movie collection manager

**Command:** 
~~~
armbian-config --cmd RAD002
~~~

**Author:** @armbian

**Status:** Stable



***

## Radarr purge with data folder
This operation will purge Radarr movie collection manager data folder

**Command:** 
~~~
armbian-config --cmd RAD003
~~~

**Author:** @armbian

**Status:** Stable



***

## Bazarr automatic subtitles downloader for Sonarr and Radarr

<!--- section image START from tools/include/images/BAZ001.png --->
[![Bazarr automatic subtitles downloader for Sonarr and Radarr](/images/BAZ001.png)](#)
<!--- section image STOP from tools/include/images/BAZ001.png --->


<!--- header START from tools/include/markdown/BAZ001-header.md --->
Bazarr is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

<!--- header STOP from tools/include/markdown/BAZ001-header.md --->

This operation will install Bazarr subtitles manager for Sonarr and Radarr

**Command:** 
~~~
armbian-config --cmd BAZ001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Bazarr remove
This operation will remove Bazarr subtitles manager for Sonarr and Radarr

**Command:** 
~~~
armbian-config --cmd BAZ002
~~~

**Author:** @armbian

**Status:** Stable



***

## Bazarr purge with data folder
This operation will purge Bazarr subtitles manager with data folder

**Command:** 
~~~
armbian-config --cmd BAZ003
~~~

**Author:** @armbian

**Status:** Stable



***

## Lidarr automatic music downloader

<!--- section image START from tools/include/images/LID001.png --->
[![Lidarr automatic music downloader](/images/LID001.png)](#)
<!--- section image STOP from tools/include/images/LID001.png --->


<!--- header START from tools/include/markdown/LID001-header.md --->
Lidarr is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/LID001-header.md --->

This operation will install Lidarr music collection manager for Usenet and BitTorrent users

**Command:** 
~~~
armbian-config --cmd LID001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Lidarr remove
This operation will remove Lidarr

**Command:** 
~~~
armbian-config --cmd LID002
~~~

**Author:** @armbian

**Status:** Stable



***

## Lidarr purge with data folder
This operation will purge Lidarr with data folder

**Command:** 
~~~
armbian-config --cmd LID003
~~~

**Author:** @armbian

**Status:** Stable



***

## Readarr automatic downloader for Ebooks

<!--- section image START from tools/include/images/RDR001.png --->
[![Readarr automatic downloader for Ebooks](/images/RDR001.png)](#)
<!--- section image STOP from tools/include/images/RDR001.png --->


<!--- header START from tools/include/markdown/RDR001-header.md --->
Readarr - Book Manager and Automation (Sonarr for Ebooks)

<!--- header STOP from tools/include/markdown/RDR001-header.md --->

This operation will install Readarr

**Command:** 
~~~
armbian-config --cmd RDR001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Readarr remove
This operation will remove Readarr

**Command:** 
~~~
armbian-config --cmd RDR002
~~~

**Author:** @armbian

**Status:** Stable



***

## Readarr purge with data folder
This operation will purge Readarr with data folder

**Command:** 
~~~
armbian-config --cmd RDR003
~~~

**Author:** @armbian

**Status:** Stable



***

## Prowlarr index manager and proxy for PVR

<!--- section image START from tools/include/images/DOW025.png --->
[![Prowlarr index manager and proxy for PVR](/images/DOW025.png)](#)
<!--- section image STOP from tools/include/images/DOW025.png --->


<!--- header START from tools/include/markdown/DOW025-header.md --->
Prowlarr is a indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Sonarr, Radarr, Lidarr, and Readarr offering complete management of your indexers with no per app Indexer setup required (we do it all).

<!--- header STOP from tools/include/markdown/DOW025-header.md --->

This operation will install Prowlarr

**Command:** 
~~~
armbian-config --cmd DOW025
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Prowlarr remove
This operation will remove Prowlarr

**Command:** 
~~~
armbian-config --cmd DOW026
~~~

**Author:** @armbian

**Status:** Stable



***

## Prowlarr purge with data folder
This operation will purge Prowlarr with data folder

**Command:** 
~~~
armbian-config --cmd DOW027
~~~

**Author:** @armbian

**Status:** Stable



***

## Jellyseerr Jellyfin/Emby/Plex integration install

<!--- section image START from tools/include/images/JEL001.png --->
[![Jellyseerr Jellyfin/Emby/Plex integration install](/images/JEL001.png)](#)
<!--- section image STOP from tools/include/images/JEL001.png --->


<!--- header START from tools/include/markdown/JEL001-header.md --->
Jellyseerr is a free and open source software application for managing requests for your media library. It is a fork of Overseerr built to bring support for Jellyfin & Emby media servers!

<!--- header STOP from tools/include/markdown/JEL001-header.md --->

This operation will install Jellyseerr

**Command:** 
~~~
armbian-config --cmd JEL001
~~~

**Author:** @armbian

**Status:** Stable



***

## Jellyseerr remove
This operation will remove Jellyseerr

**Command:** 
~~~
armbian-config --cmd JEL002
~~~

**Author:** @armbian

**Status:** Stable



***

## Jellyseerr purge with data folder
This operation will purge Jellyseerr with data folder

**Command:** 
~~~
armbian-config --cmd JEL003
~~~

**Author:** @armbian

**Status:** Stable



***

