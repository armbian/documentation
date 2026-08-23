---
title: "NetBox"
description: "Install and run NetBox on Armbian — NetBox infrastructure resource modeling install. Runs on ARM64 and x86 single-board computers."
image: /images/NBOX01.png
category: "Management"
comments: true
---
# NetBox


<!--- section image START from tools/include/images/NBOX01.png --->
![NetBox](/images/NBOX01.png){ .app-logo }
<!--- section image STOP from tools/include/images/NBOX01.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://netbox.readthedocs.io/en/stable/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8222`


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


Install from **[armbian-config](/armbian-config/) → Software → Management → NetBox**

~~~ custombash title="CLI install"
armbian-config --cmd NBOX01
~~~


<!--- footer START from tools/include/markdown/NBOX01-footer.md --->
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


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_netbox install` |
| NetBox remove | `armbian-config --api module_netbox remove` |
| NetBox purge with data folder | `armbian-config --api module_netbox purge` |
| Status | `armbian-config --api module_netbox status` |
| Help | `armbian-config --api module_netbox help` |

---

_Part of Armbian's [Remote File & Management tools](/User-Guide_Armbian-Software/Management/) software._
