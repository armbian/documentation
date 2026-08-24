---
title: "Dozzle"
description: "Install and run Dozzle on Armbian — Dozzle real-time Docker log viewer. Runs on ARM64 and x86 single-board computers."
image: /images/DOZ001.png
category: "Monitoring"
comments: true
---
# Dozzle


<!--- section image START from tools/include/images/DOZ001.png --->
![Dozzle](/images/DOZ001.png){ .app-logo }
<!--- section image STOP from tools/include/images/DOZ001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://dozzle.dev/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8888`


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


Install from **[armbian-config](/config/) → Software → Monitoring → Dozzle**

~~~ custombash title="CLI install"
armbian-config --cmd DOZ001
~~~


<!--- footer START from tools/include/markdown/DOZ001-footer.md --->
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


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_dozzle install` |
| Dozzle remove | `armbian-config --api module_dozzle remove` |
| Dozzle purge | `armbian-config --api module_dozzle purge` |
| Status | `armbian-config --api module_dozzle status` |
| Help | `armbian-config --api module_dozzle help` |

---

_Part of Armbian's [Real-time monitoring, collecting metrics, up-time status](/User-Guide_Armbian-Software/Monitoring/) software._
