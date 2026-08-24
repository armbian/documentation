---
title: "Radarr"
seo_title: "Install Radarr on Armbian"
description: "Install and run Radarr on Armbian — Radarr automatic downloader for movies. Runs on ARM64 and x86 single-board computers."
image: /images/RAD001.png
category: "Downloaders"
comments: true
---
# Radarr


<!--- section image START from tools/include/images/RAD001.png --->
![Radarr](/images/RAD001.png){ .app-logo }
<!--- section image STOP from tools/include/images/RAD001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://wiki.servarr.com/radarr) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:7878`


<!--- header START from tools/include/markdown/RAD001-header.md --->
Radarr - A fork of Sonarr to work with movies à la Couchpotato.

<!--- header STOP from tools/include/markdown/RAD001-header.md --->


Install from **[armbian-config](/config/) → Software → Downloaders → Radarr**

~~~ custombash title="CLI install"
armbian-config --cmd RAD001
~~~


<!--- footer START from tools/include/markdown/RAD001-footer.md --->
=== "Access to the web interface"

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


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_radarr install` |
| Radarr remove | `armbian-config --api module_radarr remove` |
| Radarr purge with data folder | `armbian-config --api module_radarr purge` |
| Status | `armbian-config --api module_radarr status` |
| Help | `armbian-config --api module_radarr help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
