---
title: "Transmission"
description: "Install and run Transmission on Armbian — Transmission BitTorrent client. Runs on ARM64 and x86 single-board computers."
image: /images/TRA001.png
category: "Downloaders"
comments: true
---
# Transmission


<!--- section image START from tools/include/images/TRA001.png --->
![Transmission](/images/TRA001.png){ .app-logo }
<!--- section image STOP from tools/include/images/TRA001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://transmissionbt.com/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:9091`


<!--- header START from tools/include/markdown/TRA001-header.md --->
Transmission⁠ is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

<!--- header STOP from tools/include/markdown/TRA001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Downloaders → Transmission**

~~~ custombash title="CLI install"
armbian-config --cmd TRA001
~~~


<!--- footer START from tools/include/markdown/TRA001-footer.md --->
=== "Access to the web interface"

    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/transmission`
    - Site configuration directory: `/armbian/transmission/config`
    - Download directory: `/armbian/transmission/downloads`
    - Watch directory: `/armbian/transmission/watch`

=== "View logs"

    ```sh
    docker logs -f transmission
    ```

<!--- footer STOP from tools/include/markdown/TRA001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_transmission install` |
| Transmission remove | `armbian-config --api module_transmission remove` |
| Transmission purge with data folder | `armbian-config --api module_transmission purge` |
| Status | `armbian-config --api module_transmission status` |
| Help | `armbian-config --api module_transmission help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
