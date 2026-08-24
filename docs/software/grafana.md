---
title: "Grafana"
seo_title: "Install Grafana on Armbian"
description: "Install and run Grafana on Armbian — Grafana data analytics. Runs on ARM64 and x86 single-board computers."
image: /images/GRA001.png
category: "Monitoring"
comments: true
---
# Grafana


<!--- section image START from tools/include/images/GRA001.png --->
![Grafana](/images/GRA001.png){ .app-logo }
<!--- section image STOP from tools/include/images/GRA001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://grafana.com/docs/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:3022`


<!--- header START from tools/include/markdown/GRA001-header.md --->
Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.
<!--- header STOP from tools/include/markdown/GRA001-header.md --->


Install from **[armbian-config](/config/) → Software → Monitoring → Grafana**

~~~ custombash title="CLI install"
armbian-config --cmd GRA001
~~~


<!--- footer START from tools/include/markdown/GRA001-footer.md --->
=== "Directories"

    - Install directory: `/armbian/grafana`

=== "View logs"

    ```sh
    docker logs -f grafana
    ```

<!--- footer STOP from tools/include/markdown/GRA001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_grafana install` |
| Grafana remove | `armbian-config --api module_grafana remove` |
| Grafana purge with data folder | `armbian-config --api module_grafana purge` |
| Status | `armbian-config --api module_grafana status` |
| Help | `armbian-config --api module_grafana help` |

---

_Part of Armbian's [Real-time monitoring, collecting metrics, up-time status](/User-Guide_Armbian-Software/Monitoring/) software._
