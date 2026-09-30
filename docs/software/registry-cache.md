---
title: "registry-cache"
seo_title: "Install registry-cache on Armbian"
description: "Install and run registry-cache on Armbian — OCI registry cache (ghcr.io mirror) install. Runs on ARM64 and x86 single-board computers."
image: /images/REG001.png
category: "Management"
comments: true
---
# registry-cache


<!--- section image START from tools/include/images/REG001.png --->
![registry-cache](/images/REG001.png){ .app-logo }
<!--- section image STOP from tools/include/images/REG001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://distribution.github.io/distribution/recipes/mirror/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:5000`


<!--- header START from tools/include/markdown/REG001-header.md --->
**registry-cache** is a read-only cache of one OCI registry, `ghcr.io` by default. It stores downloaded content on local disk. Tag lookups still go to the registry, so the cache needs access to the registry.

Armbian stores build artifacts and git trees on `ghcr.io`. Build hosts with many runners download each artifact once.

**Key Features**

- Read-only cache, single port (`5000`), single container ([distribution registry](https://distribution.github.io/distribution/))
- Cache expiry: 7 days
- Access: this host and its Docker containers. Set `BIND_ADDRESS` at install to serve a LAN.

!!! warning "Plain HTTP"
    The cache has no TLS and no authentication. Serve a LAN only when you trust the LAN.

<!--- header STOP from tools/include/markdown/REG001-header.md --->


Install from **[armbian-config](/config/) → Software → Management → registry-cache**

~~~ custombash title="CLI install"
armbian-config --cmd REG001
~~~


<!--- footer START from tools/include/markdown/REG001-footer.md --->
=== "Armbian builds"

    ```sh
    ./compile.sh OCI_PROXY=<address>:5000 ...
    ```

=== "Directories"

    - Cache: `/armbian/registry-cache/data/`

=== "View logs"

    ```sh
    docker logs -f registry-cache
    ```

<!--- footer STOP from tools/include/markdown/REG001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_registry_cache install` |
| OCI registry cache remove | `armbian-config --api module_registry_cache remove` |
| OCI registry cache purge with cache folder | `armbian-config --api module_registry_cache purge` |
| Status | `armbian-config --api module_registry_cache status` |
| Help | `armbian-config --api module_registry_cache help` |

---

_Part of Armbian's [Remote File & Management tools](/software/management/) software._
