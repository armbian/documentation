---
title: "PostgreSQL"
description: "Install and run PostgreSQL on Armbian — PostgreSQL install. Runs on ARM64 and x86 single-board computers."
image: /images/PGSQL1.png
category: "Database"
comments: true
---
# PostgreSQL


<!--- section image START from tools/include/images/PGSQL1.png --->
![PostgreSQL](/images/PGSQL1.png){ .app-logo }
<!--- section image STOP from tools/include/images/PGSQL1.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://www.postgresql.org/docs/) · :material-lan-connect:{ title="Access port" } `postgresql://<your.IP>:5432`


<!--- header START from tools/include/markdown/PGSQL1-header.md --->
PostgreSQL is a powerful, open-source object-relational database system known for its robustness, feature richness, and reliability.

It is designed for everyone, including:

- Developers needing advanced SQL support and extensibility.
- System administrators requiring reliable data storage for mission-critical applications.
- Enterprises seeking a high-performance, standards-compliant relational database.

PostgreSQL offers strong ACID compliance, concurrency, rich data types, full-text search, JSON support, and extensibility through stored procedures and custom functions.  
It is trusted globally in financial, government, and web-scale applications.

Thanks to its proven architecture and open-source nature, PostgreSQL fits seamlessly in projects of all sizes.

<!--- header STOP from tools/include/markdown/PGSQL1-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Database → PostgreSQL**

~~~ custombash title="CLI install"
armbian-config --cmd PGSQL1
~~~


<!--- footer START from tools/include/markdown/PGSQL1-footer.md --->
=== "Access to the database"

    - Default user: `armbian`
    - Default password: `armbian`
    - Default database: `armbian`

=== "Directories"

    - Data directory: `/armbian/postgres/data`

=== "View logs"

    ```sh
    docker logs -f postgres
    ```

<!--- footer STOP from tools/include/markdown/PGSQL1-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_postgres install` |
| PostgreSQL remove | `armbian-config --api module_postgres remove` |
| PostgreSQL purge with data folder | `armbian-config --api module_postgres purge` |
| Status | `armbian-config --api module_postgres status` |
| Help | `armbian-config --api module_postgres help` |

---

_Part of Armbian's [SQL database servers and web interface managers](/User-Guide_Armbian-Software/Database/) software._
