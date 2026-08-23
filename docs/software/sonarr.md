---
title: "Sonarr"
description: "Install and run Sonarr on Armbian — Sonarr automatic downloader for TV shows. Runs on ARM64 and x86 single-board computers."
image: /images/SON001.png
category: "Downloaders"
comments: true
---
# Sonarr


<!--- section image START from tools/include/images/SON001.png --->
![Sonarr](/images/SON001.png)
<!--- section image STOP from tools/include/images/SON001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://wiki.servarr.com/sonarr) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8989`


<!--- header START from tools/include/markdown/SON001-header.md --->
Sonarr (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/SON001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Downloaders → Sonarr**

~~~ custombash title="CLI install"
armbian-config --cmd SON001
~~~


<!--- footer START from tools/include/markdown/SON001-footer.md --->
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


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_sonarr install` |
| Sonarr remove | `armbian-config --api module_sonarr remove` |
| Sonarr purge with data folder | `armbian-config --api module_sonarr purge` |
| Status | `armbian-config --api module_sonarr status` |
| Help | `armbian-config --api module_sonarr help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
