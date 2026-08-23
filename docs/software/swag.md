---
title: "SWAG"
description: "Install and run SWAG on Armbian — SWAG reverse proxy. Runs on ARM64 and x86 single-board computers."
image: /images/SWAG01.png
category: "WebHosting"
comments: true
---
# SWAG


<!--- section image START from tools/include/images/SWAG01.png --->
![SWAG](/images/SWAG01.png)
<!--- section image STOP from tools/include/images/SWAG01.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/linuxserver/docker-swag) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:443`


<!--- header START from tools/include/markdown/SWAG01-header.md --->
SWAG - Secure Web Application Gateway sets up an Nginx webserver and reverse proxy with php support and a built-in certbot client that automates free SSL server certificate generation and renewal processes (Let's Encrypt). It also contains fail2ban for intrusion prevention.

After entering required information, your server will have auto updating SSL secured website! To this website you can attach several services, for example: https://my.server.com/netdata will run [Netdata](https://www.netdata.cloud/) instance.

=== "Requirements"

    - this computer port 80 and 443 must be open to the internet
    - your domain name (myserver.mydomain.com) DNS server should point to your router WAN address
    - make sure to set additional .htpasswd username and password as you don't want to expose your services without password

=== "Directories"

    - Config directory: `/armbian/swag/config/`
    - Website root folder: `/armbian/swag/config/www/`
    - Reverse proxy configuration samples: `/armbian/swag/config/nginx/proxy-confs/`

=== "Advanced setup"

    - Please follow this comprehensive guide: <https://github.com/linuxserver/docker-swag>

<!--- header STOP from tools/include/markdown/SWAG01-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Web Hosting → SWAG**

~~~ custombash title="CLI install"
armbian-config --cmd SWAG01
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_swag install` |
| SWAG remove | `armbian-config --api module_swag remove` |
| SWAG purge with data folder | `armbian-config --api module_swag purge` |
| Status | `armbian-config --api module_swag status` |
| SWAG reverse proxy .htpasswd set | `armbian-config --api module_swag password` |
| Help | `armbian-config --api module_swag help` |

---

_Part of Armbian's [Web server, LEMP, reverse proxy, Let's Encrypt SSL](/User-Guide_Armbian-Software/WebHosting/) software._
