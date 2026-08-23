---
title: "Navidrome"
description: "Install and run Navidrome on Armbian — Navidrome music server and streamer compatible with Subsonic/Airsonic. Runs on ARM64 and x86 single-board computers."
image: /images/NAV001.png
category: "Media"
comments: true
---
# Navidrome


<!--- section image START from tools/include/images/NAV001.png --->
![Navidrome](/images/NAV001.png){ .app-logo }
<!--- section image STOP from tools/include/images/NAV001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/pynavidrome/navidrome/wiki) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:4533`


<!--- header START from tools/include/markdown/NAV001-header.md --->
Navidrome is a modern, lightweight, and self-hosted music server and streamer. It's designed to be compatible with the Subsonic and Airsonic APIs, making it a drop-in replacement for users of those systems. With Navidrome, you can stream your personal music collection from anywhere using any compatible Subsonic client (mobile or desktop). It supports multi-user access, real-time updates, album artwork, and is built with performance and simplicity in mind—perfect for organizing and accessing large music libraries.

<!--- header STOP from tools/include/markdown/NAV001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Media → Navidrome**

~~~ custombash title="CLI install"
armbian-config --cmd NAV001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_navidrome install` |
| Navidrome remove | `armbian-config --api module_navidrome remove` |
| Navidrome purge with data folder | `armbian-config --api module_navidrome purge` |
| Status | `armbian-config --api module_navidrome status` |
| Help | `armbian-config --api module_navidrome help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
