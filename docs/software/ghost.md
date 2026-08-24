---
title: "Ghost"
seo_title: "Install Ghost on Armbian"
description: "Install and run Ghost on Armbian — Ghost CMS install. Runs on ARM64 and x86 single-board computers."
image: /images/GHOST1.png
category: "WebHosting"
comments: true
---
# Ghost


<!--- section image START from tools/include/images/GHOST1.png --->
![Ghost](/images/GHOST1.png){ .app-logo }
<!--- section image STOP from tools/include/images/GHOST1.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://ghost.org/docs/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:9190`


<!--- header START from tools/include/markdown/GHOST1-header.md --->
Ghost is a powerful open-source publishing platform designed for professional publishing, newsletters, and modern blogs. It’s built on Node.js and provides a clean, fast, and customizable CMS experience.

<!--- header STOP from tools/include/markdown/GHOST1-header.md --->


Install from **[armbian-config](/config/) → Software → Web Hosting → Ghost**

~~~ custombash title="CLI install"
armbian-config --cmd GHOST1
~~~


<!--- footer START from tools/include/markdown/GHOST1-footer.md --->
=== "Configuration"

    Initial setup includes:

    - automatic database schema setup on first run
    - admin account created via web interface
    - Default port: `9190`
    - Admin URL: `http://<your.IP>:9190/ghost` (or behind reverse proxy like SWAG)
    - Site: `http://<your.IP>:9190`

=== "Directories"

    - Install directory: `/armbian/ghost`

=== "View logs"

    ```sh
    docker logs -f ghost
    ```

<!--- footer STOP from tools/include/markdown/GHOST1-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_ghost install` |
| Ghost CMS remove | `armbian-config --api module_ghost remove` |
| Ghost CMS purge with data folder | `armbian-config --api module_ghost purge` |
| Status | `armbian-config --api module_ghost status` |
| Help | `armbian-config --api module_ghost help` |

---

_Part of Armbian's [Web server, LEMP, reverse proxy, Let's Encrypt SSL](/User-Guide_Armbian-Software/WebHosting/) software._
