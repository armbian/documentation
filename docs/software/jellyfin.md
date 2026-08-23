---
title: "Jellyfin"
description: "Install and run Jellyfin on Armbian — Jellyfin Media System. Runs on ARM64 and x86 single-board computers."
image: /images/JMS001.png
category: "Media"
comments: true
---
# Jellyfin


<!--- section image START from tools/include/images/JMS001.png --->
![Jellyfin](/images/JMS001.png){ .app-logo }
<!--- section image STOP from tools/include/images/JMS001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://jellyfin.org/docs/general/quick-start/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8096`


<!--- header START from tools/include/markdown/JMS001-header.md --->
Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it.

<!--- header STOP from tools/include/markdown/JMS001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Media → Jellyfin**

~~~ custombash title="CLI install"
armbian-config --cmd JMS001
~~~


<!--- footer START from tools/include/markdown/JMS001-footer.md --->
=== "Access to the web interface"

    - Username and password are set at first login

=== "Directories"

    - Install directory: `/armbian/jellyfin`
    - Site configuration directory: `/armbian/jellyfin/config`
    - TV shows directory: `/armbian/jellyfin/tvseries`
    - Movies directory: `/armbian/jellyfin/movies`

=== "View logs"

    ```sh
    docker logs -f jellyfin
    ```

<!--- footer STOP from tools/include/markdown/JMS001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_jellyfin install` |
| Jellyfin remove | `armbian-config --api module_jellyfin remove` |
| Jellyfin purge with data folder | `armbian-config --api module_jellyfin purge` |
| Status | `armbian-config --api module_jellyfin status` |
| Help | `armbian-config --api module_jellyfin help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
