# Download tools


***

## Install qBittorrent

<!--- section image START from tools/include/images/DOW001.png --->
[![Install qBittorrent](/images/DOW001.png)](#)
<!--- section image STOP from tools/include/images/DOW001.png --->


<!--- header START from tools/include/markdown/DOW001-header.md --->
The Qbittorrent⁠ project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

<!--- header STOP from tools/include/markdown/DOW001-header.md --->

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

## Remove qBittorrent
**Command:** 
~~~
armbian-config --cmd DOW002
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Deluge

<!--- section image START from tools/include/images/DOW003.png --->
[![Install Deluge](/images/DOW003.png)](#)
<!--- section image STOP from tools/include/images/DOW003.png --->


<!--- header START from tools/include/markdown/DOW003-header.md --->
Deluge⁠ is a lightweight, Free Software, cross-platform BitTorrent client.

<!--- header STOP from tools/include/markdown/DOW003-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW003
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW003-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW003-footer.md --->



***

## Remove Deluge
**Command:** 
~~~
armbian-config --cmd DOW004
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Transmission

<!--- section image START from tools/include/images/DOW005.png --->
[![Install Transmission](/images/DOW005.png)](#)
<!--- section image STOP from tools/include/images/DOW005.png --->


<!--- header START from tools/include/markdown/DOW005-header.md --->
Transmission⁠ is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

<!--- header STOP from tools/include/markdown/DOW005-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW005
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW005-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW005-footer.md --->



***

## Remove Transmission
**Command:** 
~~~
armbian-config --cmd DOW006
~~~

**Author:** @armbian

**Status:** Stable



***

## Install SABnzbd

<!--- section image START from tools/include/images/DOW011.png --->
[![Install SABnzbd](/images/DOW011.png)](#)
<!--- section image STOP from tools/include/images/DOW011.png --->


<!--- header START from tools/include/markdown/DOW011-header.md --->
Sabnzbd⁠ makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

<!--- header STOP from tools/include/markdown/DOW011-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW011
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW011-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW011-footer.md --->



***

## Remove SABnzbd
**Command:** 
~~~
armbian-config --cmd DOW012
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Medusa

<!--- section image START from tools/include/images/DOW013.png --->
[![Install Medusa](/images/DOW013.png)](#)
<!--- section image STOP from tools/include/images/DOW013.png --->


<!--- header START from tools/include/markdown/DOW013-header.md --->
Medusa is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

<!--- header STOP from tools/include/markdown/DOW013-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW013
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW013-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW013-footer.md --->



***

## Remove Medusa
**Command:** 
~~~
armbian-config --cmd DOW014
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Sonarr

<!--- section image START from tools/include/images/DOW015.png --->
[![Install Sonarr](/images/DOW015.png)](#)
<!--- section image STOP from tools/include/images/DOW015.png --->


<!--- header START from tools/include/markdown/DOW015-header.md --->
Sonarr (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/DOW015-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW015
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW015-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW015-footer.md --->



***

## Remove Sonarr
**Command:** 
~~~
armbian-config --cmd DOW016
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Radarr

<!--- section image START from tools/include/images/DOW017.png --->
[![Install Radarr](/images/DOW017.png)](#)
<!--- section image STOP from tools/include/images/DOW017.png --->


<!--- header START from tools/include/markdown/DOW017-header.md --->
Radarr - A fork of Sonarr to work with movies à la Couchpotato.

<!--- header STOP from tools/include/markdown/DOW017-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW017
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW017-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW017-footer.md --->



***

## Remove Radarr
**Command:** 
~~~
armbian-config --cmd DOW018
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Bazarr

<!--- section image START from tools/include/images/DOW019.png --->
[![Install Bazarr](/images/DOW019.png)](#)
<!--- section image STOP from tools/include/images/DOW019.png --->


<!--- header START from tools/include/markdown/DOW019-header.md --->
Bazarr is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

<!--- header STOP from tools/include/markdown/DOW019-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW019
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW019-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW019-footer.md --->



***

## Remove Bazarr
**Command:** 
~~~
armbian-config --cmd DOW020
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Lidarr

<!--- section image START from tools/include/images/DOW021.png --->
[![Install Lidarr](/images/DOW021.png)](#)
<!--- section image STOP from tools/include/images/DOW021.png --->


<!--- header START from tools/include/markdown/DOW021-header.md --->
Lidarr is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/DOW021-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW021
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW021-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW021-footer.md --->



***

## Remove Lidarr
**Command:** 
~~~
armbian-config --cmd DOW022
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Readarr

<!--- section image START from tools/include/images/DOW023.png --->
[![Install Readarr](/images/DOW023.png)](#)
<!--- section image STOP from tools/include/images/DOW023.png --->


<!--- header START from tools/include/markdown/DOW023-header.md --->
Readarr - Book Manager and Automation (Sonarr for Ebooks)

<!--- header STOP from tools/include/markdown/DOW023-header.md --->

**Command:** 
~~~
armbian-config --cmd DOW023
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DOW023-footer.md --->
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

<!--- footer STOP from tools/include/markdown/DOW023-footer.md --->



***

## Remove Readarr
**Command:** 
~~~
armbian-config --cmd DOW024
~~~

**Author:** @armbian

**Status:** Stable



***

## Install Prowlarr

<!--- section image START from tools/include/images/DOW025.png --->
[![Install Prowlarr](/images/DOW025.png)](#)
<!--- section image STOP from tools/include/images/DOW025.png --->


<!--- header START from tools/include/markdown/DOW025-header.md --->
Prowlarr is a indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Sonarr, Radarr, Lidarr, and Readarr offering complete management of your indexers with no per app Indexer setup required (we do it all).

<!--- header STOP from tools/include/markdown/DOW025-header.md --->

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

## Remove Prowlarr
**Command:** 
~~~
armbian-config --cmd DOW026
~~~

**Author:** @armbian

**Status:** Stable



***

