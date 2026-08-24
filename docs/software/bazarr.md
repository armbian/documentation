---
title: "Bazarr"
description: "Install and run Bazarr on Armbian — Bazarr automatic subtitles downloader for Sonarr and Radarr. Runs on ARM64 and x86 single-board computers."
image: /images/BAZ001.png
category: "Downloaders"
comments: true
---
# Bazarr


<!--- section image START from tools/include/images/BAZ001.png --->
![Bazarr](/images/BAZ001.png){ .app-logo }
<!--- section image STOP from tools/include/images/BAZ001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://wiki.bazarr.media/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:6767`


<!--- header START from tools/include/markdown/BAZ001-header.md --->
Bazarr is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

<!--- header STOP from tools/include/markdown/BAZ001-header.md --->


Install from **[armbian-config](/config/) → Software → Downloaders → Bazarr**

~~~ custombash title="CLI install"
armbian-config --cmd BAZ001
~~~


<!--- footer START from tools/include/markdown/BAZ001-footer.md --->
=== "Access to the web interface"

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


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_bazarr install` |
| Bazarr remove | `armbian-config --api module_bazarr remove` |
| Bazarr purge with data folder | `armbian-config --api module_bazarr purge` |
| Status | `armbian-config --api module_bazarr status` |
| Help | `armbian-config --api module_bazarr help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
