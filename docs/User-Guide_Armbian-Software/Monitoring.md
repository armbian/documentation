---
comments: true
---

# Real-time monitoring, collecting metrics, up-time status

## Uptime Kuma self-hosted monitoring tool

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/MON001.webp --->
[![Uptime Kuma self-hosted monitoring tool](/images/MON001.webp)](#)
<!--- section image STOP from tools/include/images/MON001.webp --->


~~~ bash title="Uptime Kuma self-hosted monitoring tool:"
armbian-config --cmd MON001
~~~


~~~ bash title="Uptime Kuma remove:"
armbian-config --cmd MON002
~~~


~~~ bash title="Uptime Kuma purge with data folder:"
armbian-config --cmd MON003
~~~


~~~ bash title="Netdata - monitoring real-time metrics:"
armbian-config --cmd MON005
~~~


~~~ bash title="Netdata remove:"
armbian-config --cmd MON006
~~~


~~~ bash title="Netdata purge with data folder:"
armbian-config --cmd MON007
~~~

## Grafana data analytics

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/GRA001.png --->
[![Grafana data analytics](/images/GRA001.png)](#)
<!--- section image STOP from tools/include/images/GRA001.png --->


<!--- header START from tools/include/markdown/GRA001-header.md --->
Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.
<!--- header STOP from tools/include/markdown/GRA001-header.md --->


~~~ bash title="Grafana data analytics:"
armbian-config --cmd GRA001
~~~


~~~ bash title="Grafana remove:"
armbian-config --cmd GRA002
~~~


~~~ bash title="Grafana purge with data folder:"
armbian-config --cmd GRA003
~~~

## Prometheus docker image

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/PRO001.png --->
[![Prometheus docker image](/images/PRO001.png)](#)
<!--- section image STOP from tools/include/images/PRO001.png --->


<!--- header START from tools/include/markdown/PRO001-header.md --->
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects and stores time-series data, provides powerful query capabilities, and enables real-time alerts based on defined conditions. Commonly used in cloud and containerized environments, Prometheus integrates seamlessly with Kubernetes and other modern infrastructure.

<!--- header STOP from tools/include/markdown/PRO001-header.md --->


~~~ bash title="Prometheus docker image:"
armbian-config --cmd PRO001
~~~


~~~ bash title="Prometheus remove:"
armbian-config --cmd PRO002
~~~


~~~ bash title="Prometheus purge with data folder:"
armbian-config --cmd PRO003
~~~
