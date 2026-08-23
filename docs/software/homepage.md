---
title: "Homepage"
description: "Install and run Homepage on Armbian — Install Homepage startpage / application dashboard. Runs on ARM64 and x86 single-board computers."
image: /images/HPG001.png
category: "Management"
comments: true
---
# Homepage


<!--- section image START from tools/include/images/HPG001.png --->
![Homepage](/images/HPG001.png){ .app-logo }
<!--- section image STOP from tools/include/images/HPG001.png --->


<span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://gethomepage.dev/configs/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:3021`


<!--- header START from tools/include/markdown/HPG001-header.md --->
[gethomepage](https://gethomepage.dev/) is a fast, fully static, highly customizable application dashboard built for modern self-hosted environments. With a **fully proxied** architecture and **zero runtime**, it delivers exceptional speed, security, and simplicity for organizing and accessing your services.

It supports **over 100 service integrations** and **multiple languages**, offering live status displays and dynamic resource monitoring out-of-the-box. Configuration is effortless via **YAML files** or automatic **Docker label discovery**, making setup and management seamless.

*Key Features*

- **Static Frontend**: Blazing-fast performance with no server-side runtime.
- **Secure Proxying**: Safely access internal services without direct exposure.
- **Service Integrations**: Native support for Docker, Kubernetes, Grafana, Proxmox, Home Assistant, and more.
- **Easy Configuration**: Manage layout and services with YAML or Docker labels.
- **Internationalization**: Translations available for multiple languages.
- **Flexible Theming**: Personalize with themes, layouts, and styling.
- **Simple Deployment**: Host via Docker, Kubernetes, or any static hosting platform.

---

Whether you're running a small homelab or a full server fleet, **gethomepage** offers a sleek, powerful, and secure way to stay organized.

<!--- header STOP from tools/include/markdown/HPG001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Management → Homepage**

~~~ custombash title="CLI install"
armbian-config --cmd HPG001
~~~


<!--- footer START from tools/include/markdown/HPG001-footer.md --->
=== "Access to the web interface"

    - Username/Password: none

    Configuration: Please reffer to official manual <https://gethomepage.dev/configs/>

=== "Directories"

    - Install directory: `/armbian/homepage`
    - Site configuration directory: `/armbian/homepage/config`

=== "View logs"

    ```sh
    docker logs -f homepage
    ```

<!--- footer STOP from tools/include/markdown/HPG001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_homepage install` |
| Remove Homepage | `armbian-config --api module_homepage remove` |
| Purge Homepage with data folder | `armbian-config --api module_homepage purge` |
| Status | `armbian-config --api module_homepage status` |
| Help | `armbian-config --api module_homepage help` |

---

_Part of Armbian's [Remote File & Management tools](/User-Guide_Armbian-Software/Management/) software._
