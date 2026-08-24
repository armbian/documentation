---
title: "Lidarr"
description: "Install and run Lidarr on Armbian — Lidarr automatic music downloader. Runs on ARM64 and x86 single-board computers."
image: /images/LID001.png
category: "Downloaders"
comments: true
---
# Lidarr


<!--- section image START from tools/include/images/LID001.png --->
![Lidarr](/images/LID001.png){ .app-logo }
<!--- section image STOP from tools/include/images/LID001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://wiki.servarr.com/lidarr) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8686`


<!--- header START from tools/include/markdown/LID001-header.md --->
Lidarr is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

<!--- header STOP from tools/include/markdown/LID001-header.md --->


Install from **[armbian-config](/config/) → Software → Downloaders → Lidarr**

~~~ custombash title="CLI install"
armbian-config --cmd LID001
~~~


<!--- footer START from tools/include/markdown/LID001-footer.md --->
=== "Access to the web interface"

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


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_lidarr install` |
| Lidarr remove | `armbian-config --api module_lidarr remove` |
| Lidarr purge with data folder | `armbian-config --api module_lidarr purge` |
| Status | `armbian-config --api module_lidarr status` |
| Help | `armbian-config --api module_lidarr help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
