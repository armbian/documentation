---
title: "Prowlarr"
description: "Install and run Prowlarr on Armbian — Prowlarr index manager and proxy for PVR. Runs on ARM64 and x86 single-board computers."
image: /images/PRW001.png
category: "Downloaders"
comments: true
---
# Prowlarr


<!--- section image START from tools/include/images/PRW001.png --->
![Prowlarr](/images/PRW001.png){ .app-logo }
<!--- section image STOP from tools/include/images/PRW001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://prowlarr.com/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:9696`


<!--- header START from tools/include/markdown/PRW001-header.md --->
Prowlarr is a indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Sonarr, Radarr, Lidarr, and Readarr offering complete management of your indexers with no per app Indexer setup required (we do it all).

<!--- header STOP from tools/include/markdown/PRW001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Downloaders → Prowlarr**

~~~ custombash title="CLI install"
armbian-config --cmd PRW001
~~~


<!--- footer START from tools/include/markdown/PRW001-footer.md --->
=== "Access to the web interface"

    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/prowlarr`
    - Site configuration directory: `/armbian/prowlarr/config`

=== "View logs"

    ```sh
    docker logs -f prowlarr
    ```

<!--- footer STOP from tools/include/markdown/PRW001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_prowlarr install` |
| Prowlarr remove | `armbian-config --api module_prowlarr remove` |
| Prowlarr purge with data folder | `armbian-config --api module_prowlarr purge` |
| Status | `armbian-config --api module_prowlarr status` |
| Help | `armbian-config --api module_prowlarr help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
