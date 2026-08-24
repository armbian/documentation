---
title: "MySQL"
description: "Install and run MySQL on Armbian — MySQL SQL database server. Runs on ARM64 and x86 single-board computers."
image: /images/MYSQL1.png
category: "Database"
comments: true
---
# MySQL


<!--- section image START from tools/include/images/MYSQL1.png --->
![MySQL](/images/MYSQL1.png){ .app-logo }
<!--- section image STOP from tools/include/images/MYSQL1.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://hub.docker.com/_/mysql) · :material-lan-connect:{ title="Access port" } `mysql://<your.IP>:3306`


<!--- header START from tools/include/markdown/MYSQL1-header.md --->
MySQL is one of the world’s most widely used open-source database servers. Trusted for decades in web, cloud, and enterprise applications.

<!--- header STOP from tools/include/markdown/MYSQL1-header.md --->


Install from **[armbian-config](/config/) → Software → Database → MySQL**

~~~ custombash title="CLI install"
armbian-config --cmd MYSQL1
~~~


<!--- footer START from tools/include/markdown/MYSQL1-footer.md --->
=== "Configuration"

    Database access configuration is done at first install:

    - create root password
    - create database
    - create normal user
    - create password for normal user

    - Database host: `<your.IP>`

=== "Directories"

    - Install directory: `/armbian/mysql`
    - Data volume mounted to: `/armbian/mysql/data`

=== "View logs"

    ```sh
    docker logs -f mysql
    ```

<!--- footer STOP from tools/include/markdown/MYSQL1-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_mysql install` |
| MySQL remove | `armbian-config --api module_mysql remove` |
| MySQL purge with data folder | `armbian-config --api module_mysql purge` |
| Status | `armbian-config --api module_mysql status` |
| Help | `armbian-config --api module_mysql help` |

---

_Part of Armbian's [SQL database servers and web interface managers](/User-Guide_Armbian-Software/Database/) software._
