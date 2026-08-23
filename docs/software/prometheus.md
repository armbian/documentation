---
title: "Prometheus"
description: "Install and run Prometheus on Armbian — Prometheus monitoring and alerting toolkit. Runs on ARM64 and x86 single-board computers."
image: /images/PRO001.png
category: "Monitoring"
comments: true
---
# Prometheus


<!--- section image START from tools/include/images/PRO001.png --->
![Prometheus](/images/PRO001.png){ .app-logo }
<!--- section image STOP from tools/include/images/PRO001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://prometheus.io/docs/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:9191`


<!--- header START from tools/include/markdown/PRO001-header.md --->
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects and stores time-series data, provides powerful query capabilities, and enables real-time alerts based on defined conditions. Commonly used in cloud and containerized environments, Prometheus integrates seamlessly with Kubernetes and other modern infrastructure.

<!--- header STOP from tools/include/markdown/PRO001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Monitoring → Prometheus**

~~~ custombash title="CLI install"
armbian-config --cmd PRO001
~~~


<!--- footer START from tools/include/markdown/PRO001-footer.md --->
=== "Directories"

    - Config directory: `/armbian/prometheus`

=== "View logs"

    ```sh
    docker logs -f prometheus
    ```

<!--- footer STOP from tools/include/markdown/PRO001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_prometheus install` |
| Prometheus remove | `armbian-config --api module_prometheus remove` |
| Prometheus purge with data folder | `armbian-config --api module_prometheus purge` |
| Status | `armbian-config --api module_prometheus status` |
| Help | `armbian-config --api module_prometheus help` |

---

_Part of Armbian's [Real-time monitoring, collecting metrics, up-time status](/User-Guide_Armbian-Software/Monitoring/) software._
