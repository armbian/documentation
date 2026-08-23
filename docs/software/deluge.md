---
title: "Deluge"
description: "Install and run Deluge on Armbian — Deluge BitTorrent client. Runs on ARM64 and x86 single-board computers."
image: /images/DEL001.png
category: "Downloaders"
comments: true
---
# Deluge


<!--- section image START from tools/include/images/DEL001.png --->
![Deluge](/images/DEL001.png){ .app-logo }
<!--- section image STOP from tools/include/images/DEL001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://deluge-torrent.org/userguide/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8112`


<!--- header START from tools/include/markdown/DEL001-header.md --->
Deluge⁠ is a lightweight, Free Software, cross-platform BitTorrent client.

<!--- header STOP from tools/include/markdown/DEL001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Downloaders → Deluge**

~~~ custombash title="CLI install"
armbian-config --cmd DEL001
~~~


<!--- footer START from tools/include/markdown/DEL001-footer.md --->
=== "Access to the web interface"

    - Username/Password: default user/password of admin/deluge

=== "Directories"

    - Install directory: `/armbian/deluge`
    - Site configuration directory: `/armbian/deluge/config`
    - Download directory: `/armbian/deluge/downloads`

=== "View logs"

    ```sh
    docker logs -f deluge
    ```

<!--- footer STOP from tools/include/markdown/DEL001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_deluge install` |
| Deluge remove | `armbian-config --api module_deluge remove` |
| Deluge purge with data folder | `armbian-config --api module_deluge purge` |
| Status | `armbian-config --api module_deluge status` |
| Help | `armbian-config --api module_deluge help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
