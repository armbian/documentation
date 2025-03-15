# Real-time monitoring, collecting metrics, up-time status


***

## Uptime Kuma self-hosted monitoring tool

<!--- section image START from tools/include/images/MON001.webp --->
[![Uptime Kuma self-hosted monitoring tool](/images/MON001.webp)](#)
<!--- section image STOP from tools/include/images/MON001.webp --->

This operation will install Uptime Kuma

**Command:** 
~~~
armbian-config --cmd MON001
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/MON001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3001**:

    - URL: `https://<your.IP>:3001`
    - Username/Password: Are set at first web interface login

???+ "Uptime Kuma features"

    - Monitoring uptime for HTTP(s) / TCP / HTTP(s) Keyword / HTTP(s) Json Query / Ping / DNS Record / Push / Steam Game Server / Docker Containers
    - Fancy, Reactive, Fast UI/UX
    - Notifications via Telegram, Discord, Gotify, Slack, Pushover, Email (SMTP), and 90+ notification services, click here for the full list
    - 20-second intervals
    - Multi Languages
    - Multiple status pages
    - Map status pages to specific domains
    - Ping chart
    - Certificate info
    - Proxy support
    - 2FA support

<!--- footer STOP from tools/include/markdown/MON001-footer.md --->



***

## Uptime Kuma remove
This operation will remove Uptime Kuma

**Command:** 
~~~
armbian-config --cmd MON002
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Uptime Kuma purge with data folder
This operation will remove Uptime Kuma with data folder

**Command:** 
~~~
armbian-config --cmd MON003
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Netdata - monitoring real-time metrics

<!--- section image START from tools/include/images/MON005.png --->
[![Netdata - monitoring real-time metrics](/images/MON005.png)](#)
<!--- section image STOP from tools/include/images/MON005.png --->


<!--- header START from tools/include/markdown/MON005-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/MON005-header.md --->

This operation will install Netdata

**Command:** 
~~~
armbian-config --cmd MON005
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Netdata remove
This operation will remove Netdata

**Command:** 
~~~
armbian-config --cmd MON006
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Netdata purge with data folder
This operation will purge Netdata with data folder

**Command:** 
~~~
armbian-config --cmd MON007
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Grafana data analytics

<!--- section image START from tools/include/images/GRA001.png --->
[![Grafana data analytics](/images/GRA001.png)](#)
<!--- section image STOP from tools/include/images/GRA001.png --->


<!--- header START from tools/include/markdown/GRA001-header.md --->
Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.
<!--- header STOP from tools/include/markdown/GRA001-header.md --->

**Command:** 
~~~
armbian-config --cmd GRA001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Grafana remove
**Command:** 
~~~
armbian-config --cmd GRA002
~~~

**Author:** @armbian

**Status:** Stable



***

## Grafana purge with data folder
This operation will purge Grafana with data folder

**Command:** 
~~~
armbian-config --cmd GRA003
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Prometheus docker image

<!--- section image START from tools/include/images/PRO001.png --->
[![Prometheus docker image](/images/PRO001.png)](#)
<!--- section image STOP from tools/include/images/PRO001.png --->


<!--- header START from tools/include/markdown/PRO001-header.md --->
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects and stores time-series data, provides powerful query capabilities, and enables real-time alerts based on defined conditions. Commonly used in cloud and containerized environments, Prometheus integrates seamlessly with Kubernetes and other modern infrastructure.

<!--- header STOP from tools/include/markdown/PRO001-header.md --->

**Command:** 
~~~
armbian-config --cmd PRO001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Prometheus remove
**Command:** 
~~~
armbian-config --cmd PRO002
~~~

**Author:** @armbian

**Status:** Stable



***

## Prometheus purge with data folder
This operation will purge Prometheus with data folder

**Command:** 
~~~
armbian-config --cmd PRO003
~~~

**Author:** @armbian

**Status:** Stable



***

