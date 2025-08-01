---
comments: true
---

# Remote File & Management tools

## Cockpit


Cockpit OS and VM management tool


<!--- section image START from tools/include/images/CPT001.png --->
[![Cockpit](/images/CPT001.png)](#)
<!--- section image STOP from tools/include/images/CPT001.png --->


<!--- header START from tools/include/markdown/CPT001-header.md --->
Cockpit is a web-based graphical interface for servers, intended for everyone.

Here’s a subset of tasks you can perform on each host running Cockpit

- inspect and change network settings
- configure a firewall
- manage storage (including RAID and LUKS partitions)
- create and manage virtual machines
- download and run containers
- browse and search system logs
- inspect a system’s hardware
- upgrade software
- manage user accounts
- inspect and interact with systemd-based services
- use a terminal on a remote server in your local web browser
- switch between multiple Cockpit servers

<!--- header STOP from tools/include/markdown/CPT001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/CPT001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/CPT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://cockpit-project.org/guide/latest/)  

~~~ custombash
armbian-config --cmd CPT001
~~~


<!--- footer START from tools/include/markdown/CPT001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9890**:

    - URL: `https://<your.IP>:9890`
    - Username/Password: your system login credentials

=== "Video instructions"


    <iframe width="1200" height="676" src="https://www.youtube.com/embed/L9fMWCRcqIE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!--- footer STOP from tools/include/markdown/CPT001-footer.md --->


~~~ bash title="Remove Cockpit:"
armbian-config --cmd CPT002
~~~


~~~ bash title="Purge Cockpit with virtual machines:"
armbian-config --cmd CPT003
~~~




## Homepage


Install Homepage startpage / application dashboard


<!--- section image START from tools/include/images/HPG001.png --->
[![Homepage](/images/HPG001.png)](#)
<!--- section image STOP from tools/include/images/HPG001.png --->


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

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/HPG001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/HPG001-header.md)  
__Status:__ Stable  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://gethomepage.dev/configs/)  

~~~ custombash
armbian-config --cmd HPG001
~~~


<!--- footer START from tools/include/markdown/HPG001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3021**:

    - URL: `https://<your.IP>:3021`
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


~~~ bash title="Remove Homepage:"
armbian-config --cmd HPG002
~~~


~~~ bash title="Purge Homepage with data folder:"
armbian-config --cmd HPG003
~~~




## NetBox


NetBox infrastructure resource modeling install


<!--- section image START from tools/include/images/NBOX01.png --->
[![NetBox](/images/NBOX01.png)](#)
<!--- section image STOP from tools/include/images/NBOX01.png --->


<!--- header START from tools/include/markdown/NBOX01-header.md --->
**NetBox** is an open-source infrastructure resource modeling (IRM) tool used for managing and documenting networks and data center assets.

Requirements (installed automatically)

- [Redis](/User-Guide_Armbian-Software/Database/#redis)
- [Postgres SQL](/User-Guide_Armbian-Software/Database/#postgresql)

Key Features

- **IP Address Management (IPAM)**: Track IP networks, addresses, and VRFs.
- **Data Center Infrastructure Management (DCIM)**: Model racks, devices, connections, and more.
- **Secrets Management**: Securely store credentials and other sensitive data.
- **Extensible API & Webhooks**: Integrate with external systems.
- **Custom Fields & Scripts**: Tailor NetBox to fit your organization’s needs.

Originally developed by DigitalOcean, NetBox is widely adopted by network engineers and sysadmins to maintain source-of-truth data for automation.

[Official Website](https://netbox.dev/)

<!--- header STOP from tools/include/markdown/NBOX01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/NBOX01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NBOX01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://netbox.readthedocs.io/en/stable/)  

~~~ custombash
armbian-config --cmd NBOX01
~~~


<!--- footer START from tools/include/markdown/NBOX01-footer.md --->
=== "Access to the service"

    NetBox is accessible via HTTP on port **8000**:

    - URL: `http://<your.IP>:8000`
    - API root: `http://<your.IP>:8000/api/`

=== "Default credentials"

    - Username: `admin`
    - Password: *(set during setup)*
    - API token: *Generate in the UI or via Django shell*

=== "Directories"

    - Configuration: `/armbian/netbox/config/`
    - Scripts: `/armbian/netbox/scripts/`
    - Reports: `/armbian/netbox/reports/`

=== "View logs"

    ```sh
    docker logs -f netbox
    ```

=== "Manage the service"

    ```sh
    docker exec -it netbox bash
    ```

<!--- footer STOP from tools/include/markdown/NBOX01-footer.md --->


~~~ bash title="NetBox remove:"
armbian-config --cmd NBOX02
~~~


~~~ bash title="NetBox purge with data folder:"
armbian-config --cmd NBOX03
~~~




## Samba


SAMBA Remote File share


<!--- section image START from tools/include/images/SMB001.png --->
[![Samba](/images/SMB001.png)](#)
<!--- section image STOP from tools/include/images/SMB001.png --->


<!--- header START from tools/include/markdown/SMB001-header.md --->
Samba is an open-source software suite that enables seamless file and printer sharing between Linux/Unix servers and Windows clients. It allows a Linux machine to act as a domain controller, file server, or print server within a Windows network environment, supporting cross-platform interoperability.

<!--- header STOP from tools/include/markdown/SMB001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/SMB001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/SMB001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd SMB001
~~~


## Webmin


Webmin web-based management tool


<!--- section image START from tools/include/images/WBM001.png --->
[![Webmin](/images/WBM001.png)](#)
<!--- section image STOP from tools/include/images/WBM001.png --->


<!--- header START from tools/include/markdown/WBM001-header.md --->
Webmin is a web-based system administration tool for Unix-like servers. It provides an easy-to-use browser interface to manage users, configure services, edit files, monitor system performance, and control almost every aspect of your server — without needing to touch the command line.

<!--- header STOP from tools/include/markdown/WBM001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/WBM001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/WBM001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd WBM001
~~~


<!--- footer START from tools/include/markdown/WBM001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **10000**:

    - URL: `https://<your.IP>:10000`
    - Username/Password: your system login credentials


<!--- footer STOP from tools/include/markdown/WBM001-footer.md --->

