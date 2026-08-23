---
title: "Uptime Kuma"
description: "Install and run Uptime Kuma on Armbian — Uptime Kuma self-hosted monitoring tool. Runs on ARM64 and x86 single-board computers."
image: /images/UPK001.png
category: "Monitoring"
comments: true
---
# Uptime Kuma


<!--- section image START from tools/include/images/UPK001.png --->
![Uptime Kuma](/images/UPK001.png)
<!--- section image STOP from tools/include/images/UPK001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/louislam/uptime-kuma/wiki) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:3001`


<!--- header START from tools/include/markdown/UPK001-header.md --->
[Uptime Kuma](https://github.com/louislam/uptime-kuma) is a self-hosted monitoring tool similar to \"Uptime Robot\". 
It provides a beautiful, easy-to-use web dashboard to monitor HTTP(s), TCP, Ping, and more types of services.

You can receive instant notifications when a service goes down via Telegram, Discord, Slack, email, and many other integrations.

<!--- header STOP from tools/include/markdown/UPK001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Monitoring → Uptime Kuma**

~~~ custombash title="CLI install"
armbian-config --cmd UPK001
~~~


<!--- footer START from tools/include/markdown/UPK001-footer.md --->
=== "Access to the web interface"

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


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_uptimekuma install` |
| Uptime Kuma remove | `armbian-config --api module_uptimekuma remove` |
| Uptime Kuma purge with data folder | `armbian-config --api module_uptimekuma purge` |
| Status | `armbian-config --api module_uptimekuma status` |
| Help | `armbian-config --api module_uptimekuma help` |

---

_Part of Armbian's [Real-time monitoring, collecting metrics, up-time status](/User-Guide_Armbian-Software/Monitoring/) software._
