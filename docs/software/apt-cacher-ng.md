---
title: "apt-cacher-ng"
description: "Install and run apt-cacher-ng on Armbian — apt-cacher-ng caching proxy install. Runs on ARM64 and x86 single-board computers."
image: /images/APT001.png
category: "Management"
comments: true
---
# apt-cacher-ng


<!--- section image START from tools/include/images/APT001.png --->
![apt-cacher-ng](/images/APT001.png){ .app-logo }
<!--- section image STOP from tools/include/images/APT001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:3142`


<!--- header START from tools/include/markdown/APT001-header.md --->
**apt-cacher-ng** is a caching HTTP proxy for Debian and Ubuntu apt repositories. The first host on the LAN to fetch a `.deb` populates the cache; every subsequent `apt-get install` / `apt-get dist-upgrade` on any other host serves the same package from local disk — saving WAN bandwidth and turning multi-minute upgrades into seconds.

**Key Features**

- Transparent HTTP proxy in front of `deb.debian.org` / `archive.ubuntu.com` / vendor mirrors
- Single-port (`3142`), single-container deployment
- Per-package hit-rate report at `/acng-report.html`
- Survives container restart — cache lives on a host bind-mount

<!--- header STOP from tools/include/markdown/APT001-header.md --->


Install from **[armbian-config](/config/) → Software → Management → apt-cacher-ng**

~~~ custombash title="CLI install"
armbian-config --cmd APT001
~~~


<!--- footer START from tools/include/markdown/APT001-footer.md --->
=== "Client configuration"

    On each apt host on the LAN:

    ```sh
    echo 'Acquire::http::Proxy "http://<your.IP>:3142";' \
      | sudo tee /etc/apt/apt.conf.d/00aptproxy
    ```

=== "Directories"

    - Cache: `/armbian/apt-cacher-ng/cache/`

=== "View logs"

    ```sh
    docker logs -f apt-cacher-ng
    ```

<!--- footer STOP from tools/include/markdown/APT001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_aptcacherng install` |
| apt-cacher-ng remove | `armbian-config --api module_aptcacherng remove` |
| apt-cacher-ng purge with cache folder | `armbian-config --api module_aptcacherng purge` |
| Status | `armbian-config --api module_aptcacherng status` |
| Help | `armbian-config --api module_aptcacherng help` |

---

_Part of Armbian's [Remote File & Management tools](/User-Guide_Armbian-Software/Management/) software._
