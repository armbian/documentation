---
title: "Jellyseerr"
description: "Install and run Jellyseerr on Armbian — Jellyseerr Jellyfin/Emby/Plex integration install. Runs on ARM64 and x86 single-board computers."
image: /images/JEL001.png
category: "Downloaders"
comments: true
---
# Jellyseerr


<!--- section image START from tools/include/images/JEL001.png --->
![Jellyseerr](/images/JEL001.png){ .app-logo }
<!--- section image STOP from tools/include/images/JEL001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.jellyseerr.dev/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:5055`


<!--- header START from tools/include/markdown/JEL001-header.md --->
Jellyseerr is a free and open source software application for managing requests for your media library. It is a fork of Overseerr built to bring support for Jellyfin & Emby media servers!

<!--- header STOP from tools/include/markdown/JEL001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Downloaders → Jellyseerr**

~~~ custombash title="CLI install"
armbian-config --cmd JEL001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_jellyseerr install` |
| Jellyseerr remove | `armbian-config --api module_jellyseerr remove` |
| Jellyseerr purge with data folder | `armbian-config --api module_jellyseerr purge` |
| Status | `armbian-config --api module_jellyseerr status` |
| Help | `armbian-config --api module_jellyseerr help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
