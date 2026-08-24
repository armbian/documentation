---
title: "Redis"
description: "Install and run Redis on Armbian — Redis install. Runs on ARM64 and x86 single-board computers."
image: /images/REDIS1.png
category: "Database"
comments: true
---
# Redis


<!--- section image START from tools/include/images/REDIS1.png --->
![Redis](/images/REDIS1.png){ .app-logo }
<!--- section image STOP from tools/include/images/REDIS1.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://redis.io/docs/) · :material-lan-connect:{ title="Access port" } `redis://<your.IP>:6379`


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


Install from **[armbian-config](/config/) → Software → Database → Redis**

~~~ custombash title="CLI install"
armbian-config --cmd REDIS1
~~~


<!--- footer START from tools/include/markdown/REDIS1-footer.md --->
=== "Directories"

    - Data directory: `/armbian/redis/data`

=== "View logs"

    ```sh
    docker logs -f redis
    ```

<!--- footer STOP from tools/include/markdown/REDIS1-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_redis install` |
| Redis remove | `armbian-config --api module_redis remove` |
| Redis purge with data folder | `armbian-config --api module_redis purge` |
| Status | `armbian-config --api module_redis status` |
| Help | `armbian-config --api module_redis help` |

---

_Part of Armbian's [SQL database servers and web interface managers](/User-Guide_Armbian-Software/Database/) software._
