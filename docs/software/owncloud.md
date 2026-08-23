---
title: "Owncloud"
description: "Install and run Owncloud on Armbian — Owncloud share files and folders, easy and secure. Runs on ARM64 and x86 single-board computers."
image: /images/OWC001.png
category: "Media"
comments: true
---
# Owncloud


<!--- section image START from tools/include/images/OWC001.png --->
![Owncloud](/images/OWC001.png)
<!--- section image STOP from tools/include/images/OWC001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://doc.owncloud.com/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:7787`


<!--- header START from tools/include/markdown/OWC001-header.md --->
ownCloud is a free and open-source software project for content collaboration and sharing and syncing of files in distributed and federated enterprise scenarios.

<!--- header STOP from tools/include/markdown/OWC001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Media → Owncloud**

~~~ custombash title="CLI install"
armbian-config --cmd OWC001
~~~


<!--- footer START from tools/include/markdown/OWC001-footer.md --->
=== "Access to the web interface"

    - Username/Password: admin / admin

=== "Directories"

    - Install directory: `/armbian/owncloud`
    - Site configuration directory: `/armbian/owncloud/config`
    - Data directory: `/armbian/owncloud/data`

=== "View logs"

    ```sh
    docker logs -f owncloud
    ```

<!--- footer STOP from tools/include/markdown/OWC001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_owncloud install` |
| Owncloud remove | `armbian-config --api module_owncloud remove` |
| Owncloud purge with data folder | `armbian-config --api module_owncloud purge` |
| Status | `armbian-config --api module_owncloud status` |
| Help | `armbian-config --api module_owncloud help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
