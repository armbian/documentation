---
title: "Nextcloud"
description: "Install and run Nextcloud on Armbian — Nextcloud content collaboration platform. Runs on ARM64 and x86 single-board computers."
image: /images/NCT001.png
category: "Media"
comments: true
---
# Nextcloud


<!--- section image START from tools/include/images/NCT001.png --->
![Nextcloud](/images/NCT001.png){ .app-logo }
<!--- section image STOP from tools/include/images/NCT001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://nextcloud.com/support/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:1443`


<!--- header START from tools/include/markdown/NCT001-header.md --->
Nextcloud gives you access to all your files wherever you are. Where are your photos and documents? With Nextcloud you pick a server of your choice, at home, in a data center or at a provider. And that is where your files will be. Nextcloud runs on that server, protecting your data and giving you access from your desktop or mobile devices. Through Nextcloud you also access, sync and share your existing data on that FTP drive at the office, a Dropbox or a NAS you have at home.

<!--- header STOP from tools/include/markdown/NCT001-header.md --->


Install from **[armbian-config](/config/) → Software → Media → Nextcloud**

~~~ custombash title="CLI install"
armbian-config --cmd NCT001
~~~


<!--- footer START from tools/include/markdown/NCT001-footer.md --->
=== "Access to the web interface"

    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/nextcloud`
    - Site configuration directory: `/armbian/nextcloud/config`
    - Data directory: `/armbian/nextcloud/data`

=== "View logs"

    ```sh
    docker logs -f nextcloud
    ```

<!--- footer STOP from tools/include/markdown/NCT001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_nextcloud install` |
| Nextcloud remove | `armbian-config --api module_nextcloud remove` |
| Nextcloud purge with data folder | `armbian-config --api module_nextcloud purge` |
| Status | `armbian-config --api module_nextcloud status` |
| Help | `armbian-config --api module_nextcloud help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
