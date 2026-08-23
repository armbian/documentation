---
title: "Emby"
description: "Install and run Emby on Armbian — Emby organizes video, music, live TV, and photos. Runs on ARM64 and x86 single-board computers."
image: /images/EMB001.png
category: "Media"
comments: true
---
# Emby


<!--- section image START from tools/include/images/EMB001.png --->
![Emby](/images/EMB001.png){ .app-logo }
<!--- section image STOP from tools/include/images/EMB001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://emby.media) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8091`


<!--- header START from tools/include/markdown/EMB001-header.md --->
Emby organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

<!--- header STOP from tools/include/markdown/EMB001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Media → Emby**

~~~ custombash title="CLI install"
armbian-config --cmd EMB001
~~~


<!--- footer START from tools/include/markdown/EMB001-footer.md --->
=== "Directories"

    - Install directory: `/armbian/emby`
    - Site configuration directory: `/armbian/emby/config`
    - Data directory: `/armbian/emby/tvshows` `/armbian/emby/movies`

=== "View logs"

    ```sh
    docker logs -f emby
    ```

<!--- footer STOP from tools/include/markdown/EMB001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_embyserver install` |
| Emby server remove | `armbian-config --api module_embyserver remove` |
| Emby server purge with data folder | `armbian-config --api module_embyserver purge` |
| Status | `armbian-config --api module_embyserver status` |
| Help | `armbian-config --api module_embyserver help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
