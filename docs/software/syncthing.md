---
title: "Syncthing"
seo_title: "Install Syncthing on Armbian"
description: "Install and run Syncthing on Armbian — Syncthing continuous file synchronization. Runs on ARM64 and x86 single-board computers."
image: /images/STC001.png
category: "Media"
comments: true
---
# Syncthing


<!--- section image START from tools/include/images/STC001.png --->
![Syncthing](/images/STC001.png){ .app-logo }
<!--- section image STOP from tools/include/images/STC001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.syncthing.net/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8884`


<!--- header START from tools/include/markdown/STC001-header.md --->
Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

<!--- header STOP from tools/include/markdown/STC001-header.md --->


Install from **[armbian-config](/config/) → Software → Media → Syncthing**

~~~ custombash title="CLI install"
armbian-config --cmd STC001
~~~


<!--- footer START from tools/include/markdown/STC001-footer.md --->
=== "Access to the web interface"

    - Username/Password: There is none, but it is highly suggested setting a password for this container. To do this go to Actions -> Settings -> set user/password for the webUI.

=== "Directories"

    - Install directory: `/armbian/syncthing`
    - Site configuration directory: `/armbian/syncthing/config`
    - Data directory: `/armbian/syncthing/data1` `/armbian/syncthing/data2`

=== "View logs"

    ```sh
    docker logs -f syncthing
    ```

<!--- footer STOP from tools/include/markdown/STC001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_syncthing install` |
| Syncthing remove | `armbian-config --api module_syncthing remove` |
| Syncthing purge with data folder | `armbian-config --api module_syncthing purge` |
| Status | `armbian-config --api module_syncthing status` |
| Help | `armbian-config --api module_syncthing help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
