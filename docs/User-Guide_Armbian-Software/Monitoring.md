---
comments: true
---

# Real-time monitoring, collecting metrics, up-time status

## Uptime Kuma self-hosted monitoring tool

**Status:** Stable

**Author:** @igorpecovnik


<!--- section image START from tools/include/images/MON001.webp --->
[![Uptime Kuma self-hosted monitoring tool](/images/MON001.webp)](#)
<!--- section image STOP from tools/include/images/MON001.webp --->


~~~ bash title="Uptime Kuma self-hosted monitoring tool:"
armbian-config --cmd MON001
~~~

## Uptime Kuma remove


~~~ bash title="Uptime Kuma remove:"
armbian-config --cmd MON002
~~~

## Uptime Kuma purge with data folder


~~~ bash title="Uptime Kuma purge with data folder:"
armbian-config --cmd MON003
~~~

## Netdata - monitoring real-time metrics


<!--- section image START from tools/include/images/MON005.png --->
[![Netdata - monitoring real-time metrics](/images/MON005.png)](#)
<!--- section image STOP from tools/include/images/MON005.png --->


<!--- header START from tools/include/markdown/MON005-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/MON005-header.md --->


~~~ bash title="Netdata - monitoring real-time metrics:"
armbian-config --cmd MON005
~~~

## Netdata remove


~~~ bash title="Netdata remove:"
armbian-config --cmd MON006
~~~

## Netdata purge with data folder


~~~ bash title="Netdata purge with data folder:"
armbian-config --cmd MON007
~~~

## Grafana data analytics


<!--- section image START from tools/include/images/GRA001.png --->
[![Grafana data analytics](/images/GRA001.png)](#)
<!--- section image STOP from tools/include/images/GRA001.png --->


<!--- header START from tools/include/markdown/GRA001-header.md --->
Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.
<!--- header STOP from tools/include/markdown/GRA001-header.md --->


~~~ bash title="Grafana data analytics:"
armbian-config --cmd GRA001
~~~

## Grafana remove


~~~ bash title="Grafana remove:"
armbian-config --cmd GRA002
~~~

## Grafana purge with data folder


~~~ bash title="Grafana purge with data folder:"
armbian-config --cmd GRA003
~~~

## Prometheus docker image


<!--- section image START from tools/include/images/PRO001.png --->
[![Prometheus docker image](/images/PRO001.png)](#)
<!--- section image STOP from tools/include/images/PRO001.png --->


<!--- header START from tools/include/markdown/PRO001-header.md --->
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects and stores time-series data, provides powerful query capabilities, and enables real-time alerts based on defined conditions. Commonly used in cloud and containerized environments, Prometheus integrates seamlessly with Kubernetes and other modern infrastructure.

<!--- header STOP from tools/include/markdown/PRO001-header.md --->


~~~ bash title="Prometheus docker image:"
armbian-config --cmd PRO001
~~~

## Prometheus remove


~~~ bash title="Prometheus remove:"
armbian-config --cmd PRO002
~~~

## Prometheus purge with data folder


~~~ bash title="Prometheus purge with data folder:"
armbian-config --cmd PRO003
~~~
