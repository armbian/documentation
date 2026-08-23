---
title: "NetAlertX"
description: "Install and run NetAlertX on Armbian — NetAlertX network scanner & notification framework. Runs on ARM64 and x86 single-board computers."
image: /images/NAX001.png
category: "Monitoring"
comments: true
---
# NetAlertX


<!--- section image START from tools/include/images/NAX001.png --->
![NetAlertX](/images/NAX001.png){ .app-logo }
<!--- section image STOP from tools/include/images/NAX001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://netalertx.com) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:20211`


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


Install from **[armbian-config](/armbian-config/) → Software → Monitoring → NetAlertX**

~~~ custombash title="CLI install"
armbian-config --cmd NAX001
~~~


<!--- footer START from tools/include/markdown/NAX001-footer.md --->
=== "Directories"

    - Config directory: `/armbian/netalertx/config`

=== "View logs"

    ```sh
    docker logs -f netalertx
    ```

<!--- footer STOP from tools/include/markdown/NAX001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_netalertx install` |
| NetAlertX network scanner remove | `armbian-config --api module_netalertx remove` |
| NetAlertX network scanner purge with data folder | `armbian-config --api module_netalertx purge` |
| Status | `armbian-config --api module_netalertx status` |
| Help | `armbian-config --api module_netalertx help` |

---

_Part of Armbian's [Real-time monitoring, collecting metrics, up-time status](/User-Guide_Armbian-Software/Monitoring/) software._
