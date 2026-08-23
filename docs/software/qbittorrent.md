---
title: "qBittorrent"
description: "Install and run qBittorrent on Armbian — qBittorrent BitTorrent client. Runs on ARM64 and x86 single-board computers."
image: /images/QBT001.png
category: "Downloaders"
comments: true
---
# qBittorrent


<!--- section image START from tools/include/images/QBT001.png --->
![qBittorrent](/images/QBT001.png){ .app-logo }
<!--- section image STOP from tools/include/images/QBT001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/qbittorrent/qBittorrent/wiki/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8090`


<!--- header START from tools/include/markdown/QBT001-header.md --->
The Qbittorrent⁠ project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

<!--- header STOP from tools/include/markdown/QBT001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Downloaders → qBittorrent**

~~~ custombash title="CLI install"
armbian-config --cmd QBT001
~~~


<!--- footer START from tools/include/markdown/QBT001-footer.md --->
=== "Access to the web interface"

    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/qbittorrent`
    - Site configuration directory: `/armbian/qbittorrent/config`
    - Download directory: `/armbian/qbittorrent/downloads`

=== "View logs"

    ```sh
    docker logs -f qbittorrent
    ```

<!--- footer STOP from tools/include/markdown/QBT001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_qbittorrent install` |
| qBittorrent remove | `armbian-config --api module_qbittorrent remove` |
| qBittorrent purge with data folder | `armbian-config --api module_qbittorrent purge` |
| Status | `armbian-config --api module_qbittorrent status` |
| Help | `armbian-config --api module_qbittorrent help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
