---
comments: true
---

# SQL database servers and web interface managers

## MySQL


MySQL SQL database server


<!--- section image START from tools/include/images/MYSQL1.png --->
[![MySQL](/images/MYSQL1.png)](#)
<!--- section image STOP from tools/include/images/MYSQL1.png --->


<!--- header START from tools/include/markdown/MYSQL1-header.md --->
MySQL is one of the world’s most widely used open-source database servers. Trusted for decades in web, cloud, and enterprise applications.

<!--- header STOP from tools/include/markdown/MYSQL1-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/MYSQL1-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/MYSQL1-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://hub.docker.com/_/mysql)  

~~~ custombash
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


~~~ bash title="MySQL remove:"
armbian-config --cmd MYSQL2
~~~


~~~ bash title="MySQL purge with data folder:"
armbian-config --cmd MYSQL3
~~~




## Mariadb


Mariadb SQL database server


<!--- section image START from tools/include/images/DAT001.png --->
[![Mariadb](/images/DAT001.png)](#)
<!--- section image STOP from tools/include/images/DAT001.png --->


<!--- header START from tools/include/markdown/DAT001-header.md --->
**MariaDB** is a fast, open-source relational database server developed by the original creators of MySQL. It is designed to be fully compatible with MySQL while offering improved performance, enhanced security, and additional features.

MariaDB supports a wide range of storage engines, advanced SQL capabilities, and both single-node and clustered deployments. It is widely used in web, cloud, and


<!--- header STOP from tools/include/markdown/DAT001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/DAT001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DAT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://mariadb.org/documentation/)  

~~~ custombash
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


~~~ bash title="Mariadb remove:"
armbian-config --cmd DAT002
~~~


~~~ bash title="Mariadb purge with data folder:"
armbian-config --cmd DAT003
~~~




## phpMyAdmin


phpMyAdmin web interface manager


<!--- section image START from tools/include/images/MYA001.png --->
[![phpMyAdmin](/images/MYA001.png)](#)
<!--- section image STOP from tools/include/images/MYA001.png --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/MYA001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/MYA001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://www.phpmyadmin.net/docs/)  

~~~ custombash
armbian-config --cmd MYA001
~~~


~~~ bash title="phpMyAdmin remove:"
armbian-config --cmd MYA002
~~~


~~~ bash title="phpMyAdmin purge with data folder:"
armbian-config --cmd MYA003
~~~




## PostgreSQL


PostgreSQL install


<!--- section image START from tools/include/images/PGSQL1.png --->
[![PostgreSQL](/images/PGSQL1.png)](#)
<!--- section image STOP from tools/include/images/PGSQL1.png --->


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

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/PGSQL1-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/PGSQL1-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://www.postgresql.org/docs/)  

~~~ custombash
armbian-config --cmd PGSQL1
~~~


<!--- footer START from tools/include/markdown/PGSQL1-footer.md --->
=== "Access to the database"

    PostgreSQL is accessible via port **5432**:

    - Host: `postgresql://<your.IP>:5432`
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


~~~ bash title="PostgreSQL remove:"
armbian-config --cmd PGSQL2
~~~


~~~ bash title="PostgreSQL purge with data folder:"
armbian-config --cmd PGSQL3
~~~




## Redis


Redis install


<!--- section image START from tools/include/images/REDIS1.png --->
[![Redis](/images/REDIS1.png)](#)
<!--- section image STOP from tools/include/images/REDIS1.png --->


<!--- header START from tools/include/markdown/REDIS1-header.md --->
Redis is an open-source, in-memory data structure store, used as a database, cache, and message broker.  
It supports a variety of data structures such as strings, hashes, lists, sets, and sorted sets.

**Key Features:**
- Extremely fast performance with in-memory storage
- Persistence options (snapshotting and AOF)
- Pub/Sub messaging capabilities
- Built-in replication and high availability
- Simple API and wide client support

Redis is widely used for real-time applications, caching layers, session stores, and lightweight queues across industries and platforms.

<!--- header STOP from tools/include/markdown/REDIS1-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/REDIS1-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/REDIS1-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://redis.io/docs/)  

~~~ custombash
armbian-config --cmd REDIS1
~~~


<!--- footer START from tools/include/markdown/REDIS1-footer.md --->
=== "Access to the service"

    Redis server is accessible on port **6379**:

    - Host: `redis://<your.IP>:6379`

=== "Directories"

    - Data directory: `/armbian/redis/data`

=== "View logs"

    ```sh
    docker logs -f redis
    ```

<!--- footer STOP from tools/include/markdown/REDIS1-footer.md --->


~~~ bash title="Redis remove:"
armbian-config --cmd REDIS2
~~~


~~~ bash title="Redis purge with data folder:"
armbian-config --cmd REDIS3
~~~



