---
comments: true
---

# Download apps for movies, TV shows, music and subtitles

## qBittorrent BitTorrent client 

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/DOW001.png --->
[![qBittorrent BitTorrent client ](/images/DOW001.png)](#)
<!--- section image STOP from tools/include/images/DOW001.png --->


<!--- header START from tools/include/markdown/DOW001-header.md --->
The Qbittorrent⁠ project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

<!--- header STOP from tools/include/markdown/DOW001-header.md --->


~~~ bash title="qBittorrent BitTorrent client :"
armbian-config --cmd DOW001
~~~


~~~ bash title="qBittorrent remove:"
armbian-config --cmd DOW002
~~~


~~~ bash title="qBittorrent purge with data folder:"
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


~~~ bash title="Deluge BitTorrent client:"
armbian-config --cmd DEL001
~~~


~~~ bash title="Deluge remove:"
armbian-config --cmd DEL002
~~~


~~~ bash title="Deluge purge with data folder:"
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


~~~ bash title="Transmission BitTorrent client:"
armbian-config --cmd TRA001
~~~


~~~ bash title="Transmission remove:"
armbian-config --cmd TRA002
~~~


~~~ bash title="Transmission purge with data folder:"
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


~~~ bash title="SABnzbd newsgroup downloader:"
armbian-config --cmd SABN01
~~~


~~~ bash title="SABnzbd remove:"
armbian-config --cmd SABN02
~~~


~~~ bash title="SABnzbd purge with data folder:"
armbian-config --cmd SABN03
~~~

## Medusa automatic downloader for TV shows

**Author:** @armbian

**Status:** Stable


<!--- header START from tools/include/markdown/MDS001-header.md --->
Medusa is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

<!--- header STOP from tools/include/markdown/MDS001-header.md --->


~~~ bash title="Medusa automatic downloader for TV shows:"
armbian-config --cmd MDS001
~~~


~~~ bash title="Medusa TV shows downloader remove:"
armbian-config --cmd MDS002
~~~


~~~ bash title="Medusa TV shows downloader purge:"
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


~~~ bash title="Sonarr automatic downloader for TV shows:"
armbian-config --cmd SON001
~~~


~~~ bash title="Sonarr remove:"
armbian-config --cmd SON002
~~~


~~~ bash title="Sonarr purge with data folder:"
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


~~~ bash title="Radarr automatic downloader for movies:"
armbian-config --cmd RAD001
~~~


~~~ bash title="Radarr remove:"
armbian-config --cmd RAD002
~~~


~~~ bash title="Radarr purge with data folder:"
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


~~~ bash title="Bazarr automatic subtitles downloader for Sonarr and Radarr:"
armbian-config --cmd BAZ001
~~~


~~~ bash title="Bazarr remove:"
armbian-config --cmd BAZ002
~~~


~~~ bash title="Bazarr purge with data folder:"
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


~~~ bash title="Lidarr automatic music downloader:"
armbian-config --cmd LID001
~~~


~~~ bash title="Lidarr remove:"
armbian-config --cmd LID002
~~~


~~~ bash title="Lidarr purge with data folder:"
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


~~~ bash title="Readarr automatic downloader for Ebooks:"
armbian-config --cmd RDR001
~~~


~~~ bash title="Readarr remove:"
armbian-config --cmd RDR002
~~~


~~~ bash title="Readarr purge with data folder:"
armbian-config --cmd RDR003
~~~


~~~ bash title="Prowlarr index manager and proxy for PVR:"
armbian-config --cmd DOW025
~~~


~~~ bash title="Prowlarr remove:"
armbian-config --cmd DOW026
~~~


~~~ bash title="Prowlarr purge with data folder:"
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


~~~ bash title="Jellyseerr Jellyfin/Emby/Plex integration install:"
armbian-config --cmd JEL001
~~~


~~~ bash title="Jellyseerr remove:"
armbian-config --cmd JEL002
~~~


~~~ bash title="Jellyseerr purge with data folder:"
armbian-config --cmd JEL003
~~~
