---
title: "WireGuard"
description: "Install and run WireGuard on Armbian — WireGuard VPN server. Runs on ARM64 and x86 single-board computers."
image: /images/WRG001.png
category: "VPN"
comments: true
---
# WireGuard


<!--- section image START from tools/include/images/WRG001.png --->
![WireGuard](/images/WRG001.png)
<!--- section image STOP from tools/include/images/WRG001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.linuxserver.io/images/docker-wireguard/#server-mode) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:51820`


<!--- header START from tools/include/markdown/WRG001-header.md --->
WireGuard is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. Regarded as the most secure, easiest to use, and simplest VPN solution in the industry.
<!--- header STOP from tools/include/markdown/WRG001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → VPN → WireGuard**

~~~ custombash title="WireGuard VPN server"
armbian-config --cmd WRG001
~~~


<!--- footer START from tools/include/markdown/WRG001-footer.md --->
=== "Server"

    1. Launch `armbian-config --api module_wireguard server`.

    2. When prompted, enter a comma-separated list of peer names (e.g., laptop,phone,router).

    3. Peer configuration files will be created in

        ```
        /armbian/wireguard/config/wg_confs/peer_laptop.conf
        ```
    4. Scan the QR code (for mobile) or transfer .conf to your client system.

    5. Connect the client using the configuration.

=== "Client"

    1. Launch `armbian-config --api module_wireguard client`.

    2. You will be asked to edit or paste a valid WireGuard configuration.

    3. Provide the client configuration in this format:

    ```sh
    [Interface]
    Address = 10.13.13.2/32
    PrivateKey = <your-private-key>
    DNS = 1.1.1.1

    [Peer]
    PublicKey = <server-public-key>
    Endpoint = your.server.com:51820
    AllowedIPs = 0.0.0.0/0
    PersistentKeepalive = 25
    ```

    4. The configuration will be saved to:

        ```
        /armbian/wireguard/config/wg_confs/client.conf
        ```

    5. When prompted, enter the local LAN subnets you wish to route via VPN (e.g., `10.0.10.0/24,192.168.0.0/16`).

    6. The VPN container will be started and routing rules will be generated accordingly.

    7. Routing will be restored automatically on boot via systemd service.

=== "Access to the server from internet"

    Remember to open/forward the port 51820 (UDP) through NAT on your router.
    
=== "Directories"

    - Install directory: `/armbian/wireguard`
    - Site configuration directory: `/armbian/wireguard/config`

=== "View logs"

    ```sh
    docker logs -f wireguard
    ```
<!--- footer STOP from tools/include/markdown/WRG001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_wireguard install` |
| WireGuard VPN client | `armbian-config --api module_wireguard client` |
| WireGuard VPN server | `armbian-config --api module_wireguard server` |
| WireGuard remove | `armbian-config --api module_wireguard remove` |
| WireGuard purge with data folder | `armbian-config --api module_wireguard purge` |
| WireGuard VPN server QR codes for clients | `armbian-config --api module_wireguard qrcode` |
| Status | `armbian-config --api module_wireguard status` |
| Help | `armbian-config --api module_wireguard help` |

---

_Part of Armbian's [Virtual Private Network tools](/User-Guide_Armbian-Software/VPN/) software._
