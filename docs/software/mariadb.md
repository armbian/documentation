---
title: "Mariadb"
description: "Install and run Mariadb on Armbian — Mariadb SQL database server. Runs on ARM64 and x86 single-board computers."
image: /images/DAT001.png
category: "Database"
comments: true
---
# Mariadb


<!--- section image START from tools/include/images/DAT001.png --->
![Mariadb](/images/DAT001.png){ .app-logo }
<!--- section image STOP from tools/include/images/DAT001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://mariadb.org/documentation/) · :material-lan-connect:{ title="Access port" } `mariadb://<your.IP>:3307`


<!--- header START from tools/include/markdown/DAT001-header.md --->
**MariaDB** is a fast, open-source relational database server developed by the original creators of MySQL. It is designed to be fully compatible with MySQL while offering improved performance, enhanced security, and additional features.

MariaDB supports a wide range of storage engines, advanced SQL capabilities, and both single-node and clustered deployments. It is widely used in web, cloud, and


<!--- header STOP from tools/include/markdown/DAT001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Database → Mariadb**

~~~ custombash title="CLI install"
armbian-config --cmd DAT001
~~~


<!--- footer START from tools/include/markdown/DAT001-footer.md --->
=== "Configuration"

    Database access configuration is done at first install:
    - create root password
    - create database
    - create normal user
    - create password for normal user

    - Database host: `<your.IP>:3307`

=== "Directories"

    - Install directory: `/armbian/mariadb`
    - Site configuration directory: `/armbian/mariadb/config`

=== "View logs"

    ```sh
    docker logs -f mariadb
    ```

<!--- footer STOP from tools/include/markdown/DAT001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_mariadb install` |
| Mariadb remove | `armbian-config --api module_mariadb remove` |
| Mariadb purge with data folder | `armbian-config --api module_mariadb purge` |
| Status | `armbian-config --api module_mariadb status` |
| Help | `armbian-config --api module_mariadb help` |

---

_Part of Armbian's [SQL database servers and web interface managers](/User-Guide_Armbian-Software/Database/) software._
