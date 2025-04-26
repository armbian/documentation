---
comments: true
---

# Download apps for movies, TV shows, music and subtitles

## qBittorrent BitTorrent client 

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

## qBittorrent remove


~~~ bash title="qBittorrent remove:"
armbian-config --cmd DOW002
~~~

## qBittorrent purge with data folder


~~~ bash title="qBittorrent purge with data folder:"
armbian-config --cmd DOW003
~~~

## Deluge BitTorrent client


<!--- section image START from tools/include/images/DEL001.png --->
[![Deluge BitTorrent client](/images/DEL001.png)](#)
<!--- section image STOP from tools/include/images/DEL001.png --->


<!--- header START from tools/include/markdown/DEL001-header.md --->
Deluge⁠ is a lightweight, Free Software, cross-platform BitTorrent client.

<!--- header STOP from tools/include/markdown/DEL001-header.md --->


~~~ bash title="Deluge BitTorrent client:"
armbian-config --cmd DEL001
~~~

## Deluge remove


~~~ bash title="Deluge remove:"
armbian-config --cmd DEL002
~~~

## Deluge purge with data folder


~~~ bash title="Deluge purge with data folder:"
armbian-config --cmd DEL003
~~~

## Transmission BitTorrent client


<!--- section image START from tools/include/images/TRA001.png --->
[![Transmission BitTorrent client](/images/TRA001.png)](#)
<!--- section image STOP from tools/include/images/TRA001.png --->


<!--- header START from tools/include/markdown/TRA001-header.md --->
Transmission⁠ is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

<!--- header STOP from tools/include/markdown/TRA001-header.md --->


~~~ bash title="Transmission BitTorrent client:"
armbian-config --cmd TRA001
~~~

## Transmission remove


~~~ bash title="Transmission remove:"
armbian-config --cmd TRA002
~~~

## Transmission purge with data folder


~~~ bash title="Transmission purge with data folder:"
armbian-config --cmd TRA003
~~~

## SABnzbd newsgroup downloader


<!--- section image START from tools/include/images/SABN01.png --->
[![SABnzbd newsgroup downloader](/images/SABN01.png)](#)
<!--- section image STOP from tools/include/images/SABN01.png --->


<!--- header START from tools/include/markdown/SABN01-header.md --->
Sabnzbd⁠ makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

<!--- header STOP from tools/include/markdown/SABN01-header.md --->


~~~ bash title="SABnzbd newsgroup downloader:"
armbian-config --cmd SABN01
~~~

## SABnzbd remove


~~~ bash title="SABnzbd remove:"
armbian-config --cmd SABN02
~~~

## SABnzbd purge with data folder


~~~ bash title="SABnzbd purge with data folder:"
armbian-config --cmd SABN03
~~~

## Medusa automatic downloader for TV shows


<!--- header START from tools/include/markdown/MDS001-header.md --->
Medusa is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

<!--- header STOP from tools/include/markdown/MDS001-header.md --->


~~~ bash title="Medusa automatic downloader for TV shows:"
armbian-config --cmd MDS001
~~~

## Medusa TV shows downloader remove


~~~ bash title="Medusa TV shows downloader remove:"
armbian-config --cmd MDS002
~~~

## Medusa TV shows downloader purge


~~~ bash title="Medusa TV shows downloader purge:"
armbian-config --cmd MDS003
~~~

## Sonarr automatic downloader for TV shows


<!--- section image START from tools/include/images/SON001.png --->
[![Sonarr automatic downloader for TV shows](/images/SON001.png)](#)
<!--- section image STOP from tools/include/images/SON001.png --->


<!--- header START from tools/include/markdown/SON001-header.md --->
Sonarr (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/SON001-header.md --->


~~~ bash title="Sonarr automatic downloader for TV shows:"
armbian-config --cmd SON001
~~~

## Sonarr remove


~~~ bash title="Sonarr remove:"
armbian-config --cmd SON002
~~~

## Sonarr purge with data folder


~~~ bash title="Sonarr purge with data folder:"
armbian-config --cmd SON003
~~~

## Radarr automatic downloader for movies


<!--- section image START from tools/include/images/RAD001.png --->
[![Radarr automatic downloader for movies](/images/RAD001.png)](#)
<!--- section image STOP from tools/include/images/RAD001.png --->


<!--- header START from tools/include/markdown/RAD001-header.md --->
Radarr - A fork of Sonarr to work with movies à la Couchpotato.

<!--- header STOP from tools/include/markdown/RAD001-header.md --->


~~~ bash title="Radarr automatic downloader for movies:"
armbian-config --cmd RAD001
~~~

## Radarr remove


~~~ bash title="Radarr remove:"
armbian-config --cmd RAD002
~~~

## Radarr purge with data folder


~~~ bash title="Radarr purge with data folder:"
armbian-config --cmd RAD003
~~~

## Bazarr automatic subtitles downloader for Sonarr and Radarr


<!--- section image START from tools/include/images/BAZ001.png --->
[![Bazarr automatic subtitles downloader for Sonarr and Radarr](/images/BAZ001.png)](#)
<!--- section image STOP from tools/include/images/BAZ001.png --->


<!--- header START from tools/include/markdown/BAZ001-header.md --->
Bazarr is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

<!--- header STOP from tools/include/markdown/BAZ001-header.md --->


~~~ bash title="Bazarr automatic subtitles downloader for Sonarr and Radarr:"
armbian-config --cmd BAZ001
~~~

## Bazarr remove


~~~ bash title="Bazarr remove:"
armbian-config --cmd BAZ002
~~~

## Bazarr purge with data folder


~~~ bash title="Bazarr purge with data folder:"
armbian-config --cmd BAZ003
~~~

## Lidarr automatic music downloader


<!--- section image START from tools/include/images/LID001.png --->
[![Lidarr automatic music downloader](/images/LID001.png)](#)
<!--- section image STOP from tools/include/images/LID001.png --->


<!--- header START from tools/include/markdown/LID001-header.md --->
Lidarr is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/LID001-header.md --->


~~~ bash title="Lidarr automatic music downloader:"
armbian-config --cmd LID001
~~~

## Lidarr remove


~~~ bash title="Lidarr remove:"
armbian-config --cmd LID002
~~~

## Lidarr purge with data folder


~~~ bash title="Lidarr purge with data folder:"
armbian-config --cmd LID003
~~~

## Readarr automatic downloader for Ebooks


<!--- section image START from tools/include/images/RDR001.png --->
[![Readarr automatic downloader for Ebooks](/images/RDR001.png)](#)
<!--- section image STOP from tools/include/images/RDR001.png --->


<!--- header START from tools/include/markdown/RDR001-header.md --->
Readarr - Book Manager and Automation (Sonarr for Ebooks)

<!--- header STOP from tools/include/markdown/RDR001-header.md --->


~~~ bash title="Readarr automatic downloader for Ebooks:"
armbian-config --cmd RDR001
~~~

## Readarr remove


~~~ bash title="Readarr remove:"
armbian-config --cmd RDR002
~~~

## Readarr purge with data folder


~~~ bash title="Readarr purge with data folder:"
armbian-config --cmd RDR003
~~~

## Prowlarr index manager and proxy for PVR


<!--- section image START from tools/include/images/DOW025.png --->
[![Prowlarr index manager and proxy for PVR](/images/DOW025.png)](#)
<!--- section image STOP from tools/include/images/DOW025.png --->


<!--- header START from tools/include/markdown/DOW025-header.md --->
Prowlarr is a indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Sonarr, Radarr, Lidarr, and Readarr offering complete management of your indexers with no per app Indexer setup required (we do it all).

<!--- header STOP from tools/include/markdown/DOW025-header.md --->


~~~ bash title="Prowlarr index manager and proxy for PVR:"
armbian-config --cmd DOW025
~~~

## Prowlarr remove


~~~ bash title="Prowlarr remove:"
armbian-config --cmd DOW026
~~~

## Prowlarr purge with data folder


~~~ bash title="Prowlarr purge with data folder:"
armbian-config --cmd DOW027
~~~

## Jellyseerr Jellyfin/Emby/Plex integration install


<!--- section image START from tools/include/images/JEL001.png --->
[![Jellyseerr Jellyfin/Emby/Plex integration install](/images/JEL001.png)](#)
<!--- section image STOP from tools/include/images/JEL001.png --->


<!--- header START from tools/include/markdown/JEL001-header.md --->
Jellyseerr is a free and open source software application for managing requests for your media library. It is a fork of Overseerr built to bring support for Jellyfin & Emby media servers!

<!--- header STOP from tools/include/markdown/JEL001-header.md --->


~~~ bash title="Jellyseerr Jellyfin/Emby/Plex integration install:"
armbian-config --cmd JEL001
~~~

## Jellyseerr remove


~~~ bash title="Jellyseerr remove:"
armbian-config --cmd JEL002
~~~

## Jellyseerr purge with data folder


~~~ bash title="Jellyseerr purge with data folder:"
armbian-config --cmd JEL003
~~~
