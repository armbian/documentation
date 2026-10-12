---
title: "SolidPing"
seo_title: "Install SolidPing on Armbian"
description: "Install and run SolidPing on Armbian — SolidPing uptime and synthetic monitoring. Runs on ARM64 and x86 single-board computers."
image: /images/SPG001.png
category: "Monitoring"
comments: true
---
# SolidPing


<!--- section image START from tools/include/images/SPG001.png --->
![SolidPing](/images/SPG001.png){ .app-logo }
<!--- section image STOP from tools/include/images/SPG001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.solidping.io) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:4000`


<!--- header START from tools/include/markdown/SPG001-header.md --->
[SolidPing](https://github.com/fclairamb/solidping) is a self-hosted uptime and synthetic monitoring tool, written in Go and stored in SQLite by default.
It checks HTTP, DNS, TCP, ICMP, TLS certificates, databases, message queues, cron job heartbeats and more, with status pages, incidents and alerting.

<!--- header STOP from tools/include/markdown/SPG001-header.md --->


Install from **[armbian-config](/config/) → Software → Monitoring → SolidPing**

The app has no separate image. [Install an Armbian OS image first](/software/#how-to-install-an-app), then the app. For help with the app, [read its documentation](https://docs.solidping.io).

~~~ custombash title="CLI install"
armbian-config --cmd SPG001
~~~


<!--- footer START from tools/include/markdown/SPG001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **4000**:

    - URL: `http://<your.IP>:4000`
    - Email: `admin@solidping.io`
    - Password: `solidpass` (you are asked to change it at first login)

=== "Directories"

    - Data: `/armbian/solidping/`

=== "View logs"

    ```sh
    docker logs -f solidping
    ```

<!--- footer STOP from tools/include/markdown/SPG001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_solidping install` |
| SolidPing remove | `armbian-config --api module_solidping remove` |
| SolidPing purge with data folder | `armbian-config --api module_solidping purge` |
| Status | `armbian-config --api module_solidping status` |
| Help | `armbian-config --api module_solidping help` |

---

_Part of Armbian's [Real-time monitoring, collecting metrics, up-time status](/software/monitoring/) software._
