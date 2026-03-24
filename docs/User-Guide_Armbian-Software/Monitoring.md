---
comments: true
---

# Real-time monitoring, collecting metrics, up-time status

## Grafana


Grafana data analytics


<!--- section image START from tools/include/images/GRA001.png --->
[![Grafana](/images/GRA001.png)](#)
<!--- section image STOP from tools/include/images/GRA001.png --->


<!--- header START from tools/include/markdown/GRA001-header.md --->
Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.
<!--- header STOP from tools/include/markdown/GRA001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/GRA001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/GRA001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://grafana.com/docs/)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd GRA001
~~~


<!--- footer START from tools/include/markdown/GRA001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3022**:

    - URL: `https://<your.IP>:3022`

=== "Directories"

    - Install directory: `/armbian/grafana`

=== "View logs"

    ```sh
    docker logs -f grafana
    ```

<!--- footer STOP from tools/include/markdown/GRA001-footer.md --->


~~~ bash title="Grafana remove:"
armbian-config --cmd GRA002
~~~


~~~ bash title="Grafana purge with data folder:"
armbian-config --cmd GRA003
~~~




## NetAlertX


NetAlertX network scanner & notification framework


<!--- section image START from tools/include/images/NAX001.png --->
[![NetAlertX](/images/NAX001.png)](#)
<!--- section image STOP from tools/include/images/NAX001.png --->


<!--- header START from tools/include/markdown/NAX001-header.md --->
NetAlertX is an open-source network monitoring and intruder detection tool designed to provide visibility into your Wi-Fi or LAN network. It scans your network for connected devices and alerts you when new or unknown devices are detected, helping you monitor unauthorized access and maintain network security.

**Key Features:**

- **Scheduled Network Scans:** Regularly scans your network to detect new devices, reconnections, disconnections, and changes in IP addresses.

- **Extensive Notification Support:** Integrates with over 80 notification services, including email, Telegram, Pushover, and NTFY, ensuring you receive timely alerts about network changes.

- **Network Visualization:** Offers a user-friendly interface to visualize your entire network, enhancing security and simplifying management.

- **Multi-Network Monitoring:** Supports synchronization of multiple network instances, providing cross-network visibility across various device manufacturers.

- **Home Assistant Integration:** Seamlessly integrates with Home Assistant, enabling advanced automation workflows and smart home integrations.

- **Customizable Plugins:** Allows users to develop custom plugins with auto-generated user interfaces and built-in notification systems, tailoring the tool to specific network monitoring needs.

NetAlertX is actively maintained and supports various installation methods, including Docker and bare-metal setups. It serves as a proactive solution for maintaining network health and preventing issues before they escalate, providing peace of mind for individuals and small businesses alike.

For more information and installation guides, visit the official [NetAlertX documentation](https://jokob-sk.github.io/NetAlertX/). 

<!--- header STOP from tools/include/markdown/NAX001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/NAX001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NAX001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://netalertx.com)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd NAX001
~~~


<!--- footer START from tools/include/markdown/NAX001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **20211**:

    - URL: `https://<your.IP>:20211`

=== "Directories"

    - Config directory: `/armbian/netalertx/config`

=== "View logs"

    ```sh
    docker logs -f netalertx
    ```

<!--- footer STOP from tools/include/markdown/NAX001-footer.md --->


~~~ bash title="NetAlertX network scanner remove:"
armbian-config --cmd NAX002
~~~


~~~ bash title="NetAlertX network scanner purge with data folder:"
armbian-config --cmd NAX003
~~~




## Netdata


Netdata - monitoring real-time metrics


<!--- section image START from tools/include/images/NTD001.png --->
[![Netdata](/images/NTD001.png)](#)
<!--- section image STOP from tools/include/images/NTD001.png --->


<!--- header START from tools/include/markdown/NTD001-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/NTD001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/NTD001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NTD001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://learn.netdata.cloud/)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd NTD001
~~~


~~~ bash title="Netdata remove:"
armbian-config --cmd NTD002
~~~


~~~ bash title="Netdata purge with data folder:"
armbian-config --cmd NTD003
~~~




## Prometheus


Prometheus monitoring and alerting toolkit


<!--- section image START from tools/include/images/PRO001.png --->
[![Prometheus](/images/PRO001.png)](#)
<!--- section image STOP from tools/include/images/PRO001.png --->


<!--- header START from tools/include/markdown/PRO001-header.md --->
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects and stores time-series data, provides powerful query capabilities, and enables real-time alerts based on defined conditions. Commonly used in cloud and containerized environments, Prometheus integrates seamlessly with Kubernetes and other modern infrastructure.

<!--- header STOP from tools/include/markdown/PRO001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/PRO001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/PRO001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @efectn  
__Documentation:__ [Link](https://prometheus.io/docs/)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd PRO001
~~~


<!--- footer START from tools/include/markdown/PRO001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9191**:

    - URL: `http://<your.IP>:9191`

=== "Directories"

    - Config directory: `/armbian/prometheus`

=== "View logs"

    ```sh
    docker logs -f prometheus
    ```

<!--- footer STOP from tools/include/markdown/PRO001-footer.md --->


~~~ bash title="Prometheus remove:"
armbian-config --cmd PRO002
~~~


~~~ bash title="Prometheus purge with data folder:"
armbian-config --cmd PRO003
~~~




## Uptime Kuma


Uptime Kuma self-hosted monitoring tool


<!--- section image START from tools/include/images/UPK001.png --->
[![Uptime Kuma](/images/UPK001.png)](#)
<!--- section image STOP from tools/include/images/UPK001.png --->


<!--- header START from tools/include/markdown/UPK001-header.md --->
[Uptime Kuma](https://github.com/louislam/uptime-kuma) is a self-hosted monitoring tool similar to \"Uptime Robot\". 
It provides a beautiful, easy-to-use web dashboard to monitor HTTP(s), TCP, Ping, and more types of services.

You can receive instant notifications when a service goes down via Telegram, Discord, Slack, email, and many other integrations.

<!--- header STOP from tools/include/markdown/UPK001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/UPK001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/UPK001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/louislam/uptime-kuma/wiki)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd UPK001
~~~


<!--- footer START from tools/include/markdown/UPK001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3001**:

    - URL: `https://<your.IP>:3001`
    - Username/Password: Are set at first web interface login

=== "Features"

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

<!--- footer STOP from tools/include/markdown/UPK001-footer.md --->


~~~ bash title="Uptime Kuma remove:"
armbian-config --cmd UPK002
~~~


~~~ bash title="Uptime Kuma purge with data folder:"
armbian-config --cmd UPK003
~~~




## Dozzle


Dozzle real-time Docker log viewer


<!--- section image START from tools/include/images/DOZ001.png --->
[![Dozzle](/images/DOZ001.png)](#)
<!--- section image STOP from tools/include/images/DOZ001.png --->


<!--- header START from tools/include/markdown/DOZ001-header.md --->
Dozzle is a lightweight, real-time Docker log viewer that provides a simple and efficient way to monitor logs from all your Docker containers. Unlike complex logging solutions, Dozzle offers a streamlined interface for viewing logs without the overhead of databases or heavy resource usage.

**Key Features:**

- **Real-time Log Streaming:** View logs from all Docker containers in real-time as they are generated, with automatic updates and scrolling.

- **Search and Filtering:** Quickly find specific log entries with built-in search functionality and filter containers by name or status.

- **Color-Coded Log Levels:** Easily identify log severity with automatic color coding for different log levels, making it simple to spot errors and warnings.

- **Multi-Container View:** Monitor multiple containers simultaneously with a split-screen view, allowing you to correlate events across different services.

- **Responsive Web Interface:** Access logs from any device with a modern, responsive web interface that works seamlessly on desktops, tablets, and mobile devices.

- **Lightweight Resource Usage:** Built with Go and designed for efficiency, Dozzle consumes minimal system resources compared to heavier logging solutions.

- **No Authentication Required:** Simple setup without complex authentication; consider securing with a reverse proxy for production environments.

Dozzle connects directly to the Docker socket to read container logs, requiring no changes to your existing containers or applications. It's an ideal solution for developers and system administrators who need quick access to container logs without the complexity of full-scale log management systems.

For more information and usage examples, visit the official [Dozzle documentation](https://dozzle.dev/).

<!--- header STOP from tools/include/markdown/DOZ001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/DOZ001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DOZ001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://dozzle.dev/)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd DOZ001
~~~


<!--- footer START from tools/include/markdown/DOZ001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8888**:

    - URL: `http://<your.IP>:8888`

=== "View logs"

    View real-time logs from the Dozzle container:

    ```sh
    docker logs -f dozzle
    ```

=== "Security considerations"

    Dozzle does not include built-in authentication. For production use, consider:

    - Running behind a reverse proxy with authentication (e.g., SWAG, Nginx)
    - Using firewall rules to restrict access to trusted networks
    - Configuring VPN access for remote log viewing

=== "Troubleshooting"

    If Dozzle cannot display logs from certain containers:

    - Ensure the Docker socket is properly mounted
    - Check that the container has logs available: `docker logs <container_name>`
    - Verify Dozzle container is running: `docker ps | grep dozzle`


<!--- footer STOP from tools/include/markdown/DOZ001-footer.md --->


~~~ bash title="Dozzle remove:"
armbian-config --cmd DOZ002
~~~


~~~ bash title="Dozzle purge:"
armbian-config --cmd DOZ003
~~~



