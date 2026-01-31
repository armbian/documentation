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
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://learn.netdata.cloud/)  

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



