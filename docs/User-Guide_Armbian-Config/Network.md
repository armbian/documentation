---
comments: true
---

# Fixed and wireless network settings

## Basic setup


Basic network setup


<!--- section image START from tools/include/images/BNS001.png --->
[![Basic setup](/images/BNS001.png)](#)
<!--- section image STOP from tools/include/images/BNS001.png --->


<!--- header START from tools/include/markdown/BNS001-header.md --->
``` mermaid
graph LR
  A{Select interface} --> B[Configure];
  A{Select interface} --> C[Drop];
  C ---->A;
  B -->F[DHCP];
  B ---->G[Static];
  G ------>| MAC, IP, route, GW, DNS|H[Configured];
  F -->| MAC | H[Configured];
```

<!--- header STOP from tools/include/markdown/BNS001-header.md --->

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash
armbian-config --cmd BNS001
~~~


<!--- footer START from tools/include/markdown/BNS001-footer.md --->
**Select Interface:**  
Choose the desired network interface, such as:

- `eth0` for wired Ethernet
- `wlan0` for wireless connections

If selecting a **wireless interface**:

- A list of available Access Points (APs) will be displayed.
- Select your preferred AP and enter the password when prompted.
- Leave the password field empty for open networks.

**IP Address Configuration:**  
Choose between:

- **DHCP (Dynamic Host Configuration Protocol):**  
  Automatically assigns an IP address.

- **Static IP:**  
  Manually enter the following details:
  - **MAC Address (optional):** Specify if you want to spoof the MAC address.
  - **IP Address:** Use CIDR notation (e.g., `192.168.1.10/24`).
  - **Route:** Default is `0.0.0.0/0`.
  - **Gateway:** Typically the router’s IP (e.g., `192.168.1.1`).
  - **DNS:** Default is `9.9.9.9`, but you can specify another.

**Finalize Configuration:**  

- Review and confirm your settings.
- The system will apply the configurations.
- Your network connection should then be fully established.

<!--- footer STOP from tools/include/markdown/BNS001-footer.md --->


~~~ bash title="Remove Fallback DHCP Configuration:"
armbian-config --cmd BNS002
~~~



## View configuration


View Network Configuration


<!--- section image START from tools/include/images/VNS001.png --->
[![View configuration](/images/VNS001.png)](#)
<!--- section image STOP from tools/include/images/VNS001.png --->


<!--- header START from tools/include/markdown/VNS001-header.md --->
View Network Configuration allows you to display the system’s active network settings as a Netplan YAML configuration. This shows interfaces, IP addresses, gateways, DNS servers, and other networking details in a clean, human-readable format. Useful for verifying, troubleshooting, or manually editing network setup on systems that use Netplan for managing network interfaces.

<!--- header STOP from tools/include/markdown/VNS001-header.md --->

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash
armbian-config --cmd VNS001
~~~


## Advanced


Advanced bridged network configuration

#### Add or Change


Add / change interface


<!--- header START from tools/include/markdown/NEA001-header.md --->
``` mermaid
graph LR
  A[Network] --> B[Add / Change interface];
  A[Network] --> O[Revert to defaults];
  A[Network] --> P[Show configuration];
  B ---->E[Wired];
  B ---->F[Wireless];
  E -->R[DHCP];
  E -->T[Static];
  E -->S[Spoof MAC];
  F -->X[Station];
  F -->W[Access point]; 
```

<!--- header STOP from tools/include/markdown/NEA001-header.md --->

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash
armbian-config --cmd NEA001
~~~


<!--- footer START from tools/include/markdown/NEA001-footer.md --->
=== "Wired device check"

    In order to configure your network devices, they need to be supported the kernel.

    To verify, use command:

    ```sh
    ip addr
    ```

    It is usually something like eth0, enp4s3 or lan.

=== "Wireless device check"

    In order to configure your wireless network devices, they need to be supported the kernel.

    To verify, use command:

    ```sh
    iw dev | awk '$1=="Interface"{print $2}'
    ```

    It is usually something like `wlan0`, `wlo1` or `wlx12334c47dec3`. If you get blank response, it means your WiFi device / dongle is not supported by the kernel.

<!--- footer STOP from tools/include/markdown/NEA001-footer.md --->


~~~ bash title="Revert to Armbian defaults:"
armbian-config --cmd NEA002
~~~


~~~ bash title="Show configuration:"
armbian-config --cmd NEA003
~~~


~~~ bash title="Show active status:"
armbian-config --cmd NEA004
~~~





## WireGuard


WireGuard VPN client / server


<!--- section image START from tools/include/images/WG001.png --->
[![WireGuard](/images/WG001.png)](#)
<!--- section image STOP from tools/include/images/WG001.png --->


<!--- header START from tools/include/markdown/WG001-header.md --->
WireGuard is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. Regarded as the most secure, easiest to use, and simplest VPN solution in the industry.
<!--- header STOP from tools/include/markdown/WG001-header.md --->

**Author:** @armbian

**Status:** Enabled


~~~ custombash
armbian-config --cmd WG001
~~~


<!--- footer START from tools/include/markdown/WG001-footer.md --->
=== "Access to the server from internet"

    Remember to open/forward the port 51820 (UDP) through NAT on your router.
    
=== "Directories"

    - Install directory: `/armbian/wireguard`
    - Site configuration directory: `/armbian/wireguard/config`

=== "View logs"

    ```sh
    docker logs -f wireguard
    ```

# Install server and enable private network on a client

1. Install Wireguard server
2. It will asks you for peer keywords. It will make a profile for each peer
3. Download client to your PC, server or mobile phone. Scan OR code or copy credentials to the client.

Enjoy private network! Its that easy.

More informations:

<https://docs.linuxserver.io/images/docker-wireguard/>
<!--- footer STOP from tools/include/markdown/WG001-footer.md --->


~~~ bash title="WireGuard remove:"
armbian-config --cmd WG002
~~~


~~~ bash title="WireGuard clients QR codes:"
armbian-config --cmd WG003
~~~


~~~ bash title="WireGuard purge with data folder:"
armbian-config --cmd WG004
~~~




