---
comments: true
---

# Real-time monitoring, collecting metrics, up-time status

## Uptime Kuma self-hosted monitoring tool

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/UPK001.webp --->
[![Uptime Kuma self-hosted monitoring tool](/images/UPK001.webp)](#)
<!--- section image STOP from tools/include/images/UPK001.webp --->


<!--- header START from tools/include/markdown/UPK001-header.md --->
[Uptime Kuma](https://github.com/louislam/uptime-kuma) is a self-hosted monitoring tool similar to \"Uptime Robot\". 
It provides a beautiful, easy-to-use web dashboard to monitor HTTP(s), TCP, Ping, and more types of services.

You can receive instant notifications when a service goes down via Telegram, Discord, Slack, email, and many other integrations.

<!--- header STOP from tools/include/markdown/UPK001-header.md --->


~~~ custombash title="Uptime Kuma self-hosted monitoring tool:"
armbian-config --cmd UPK001
~~~


<!--- footer START from tools/include/markdown/UPK001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3001**:

    - URL: `https://<your.IP>:3001`
    - Username/Password: Are set at first web interface login

=== "Features"

    - Monitor uptime and response time of any service
    - Beautiful graphs and charts for history
    - Supports HTTP, HTTPS, TCP, ICMP Ping, DNS queries, and more
    - Multiple notification integrations
    - Docker-ready and lightweight

=== "Requirements"

    - Ports open on firewall if accessed externally

=== "Official Documentation"

    - <https://github.com/louislam/uptime-kuma>

<!--- footer STOP from tools/include/markdown/UPK001-footer.md --->


~~~ custombash title="Uptime Kuma remove:"
armbian-config --cmd UPK002
~~~


~~~ custombash title="Uptime Kuma purge with data folder:"
armbian-config --cmd UPK003
~~~

## Netdata - monitoring real-time metrics

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/MON005.png --->
[![Netdata - monitoring real-time metrics](/images/MON005.png)](#)
<!--- section image STOP from tools/include/images/MON005.png --->


<!--- header START from tools/include/markdown/MON005-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/MON005-header.md --->


~~~ custombash title="Netdata - monitoring real-time metrics:"
armbian-config --cmd MON005
~~~


~~~ custombash title="Netdata remove:"
armbian-config --cmd MON006
~~~


~~~ custombash title="Netdata purge with data folder:"
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


~~~ custombash title="Grafana data analytics:"
armbian-config --cmd GRA001
~~~


<!--- footer START from tools/include/markdown/GRA001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3000**:

    - URL: `https://<your.IP>:3000`

=== "Directories"

    - Install directory: `/armbian/grafana`

=== "View logs"

    ```sh
    docker logs -f grafana
    ```

<!--- footer STOP from tools/include/markdown/GRA001-footer.md --->


~~~ custombash title="Grafana remove:"
armbian-config --cmd GRA002
~~~


~~~ custombash title="Grafana purge with data folder:"
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


~~~ custombash title="Prometheus docker image:"
armbian-config --cmd PRO001
~~~


<!--- footer START from tools/include/markdown/PRO001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9090**:

    - URL: `https://<your.IP>:9090`

=== "Directories"

    - Config directory: `/armbian/prometheus`

=== "View logs"

    ```sh
    docker logs -f prometheus
    ```

<!--- footer STOP from tools/include/markdown/PRO001-footer.md --->


~~~ custombash title="Prometheus remove:"
armbian-config --cmd PRO002
~~~


~~~ custombash title="Prometheus purge with data folder:"
armbian-config --cmd PRO003
~~~
