---
comments: true
---

# Virtual Private Network tools

## WireGuard


WireGuard VPN server


<!--- section image START from tools/include/images/WRG001.png --->
[![WireGuard](/images/WRG001.png)](#)
<!--- section image STOP from tools/include/images/WRG001.png --->


<!--- header START from tools/include/markdown/WRG001-header.md --->
WireGuard is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. Regarded as the most secure, easiest to use, and simplest VPN solution in the industry.
<!--- header STOP from tools/include/markdown/WRG001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/WRG001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/WRG001-header.md)  
__Status:__ Enabled  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.linuxserver.io/images/docker-wireguard/#server-mode)  

~~~ custombash
armbian-config --cmd WRG001
~~~


<!--- footer START from tools/include/markdown/WRG001-footer.md --->
=== "Server"

    1. Launch `armbian-config --cmd WRG001`.

    2. When prompted, enter a comma-separated list of peer names (e.g., laptop,phone,router).

    3. Peer configuration files will be created in

        ```
        /armbian/wireguard/config/wg_confs/peer_laptop.conf
        ```
    4. Scan the QR code (for mobile) or transfer .conf to your client system.

    5. Connect the client using the configuration.

=== "Client"

    1. Launch `armbian-config --cmd WRG002`.

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


~~~ bash title="WireGuard VPN client:"
armbian-config --cmd WRG002
~~~


~~~ bash title="WireGuard remove:"
armbian-config --cmd WRG003
~~~


~~~ bash title="WireGuard VPN server QR codes for clients:"
armbian-config --cmd WRG004
~~~


~~~ bash title="WireGuard purge with data folder:"
armbian-config --cmd WRG005
~~~






## ZeroTier


ZeroTier connect devices over your own private network in the world.


<!--- section image START from tools/include/images/ZTR001.png --->
[![ZeroTier](/images/ZTR001.png)](#)
<!--- section image STOP from tools/include/images/ZTR001.png --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/ZTR001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/ZTR001-header.md)  
__Status:__ Stable  

~~~ custombash
armbian-config --cmd ZTR001
~~~

