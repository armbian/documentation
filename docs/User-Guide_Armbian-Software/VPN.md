---
comments: true
---

# Virtual Private Network tools

## WireGuard


WireGuard VPN client / server


<!--- section image START from tools/include/images/WRG001.png --->
[![WireGuard](/images/WRG001.png)](#)
<!--- section image STOP from tools/include/images/WRG001.png --->


<!--- header START from tools/include/markdown/WRG001-header.md --->
WireGuard is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. Regarded as the most secure, easiest to use, and simplest VPN solution in the industry.
<!--- header STOP from tools/include/markdown/WRG001-header.md --->

**Author:** @armbian

**Status:** Enabled


~~~ custombash
armbian-config --cmd WRG001
~~~


<!--- footer START from tools/include/markdown/WRG001-footer.md --->
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
<!--- footer STOP from tools/include/markdown/WRG001-footer.md --->


~~~ bash title="WireGuard remove:"
armbian-config --cmd WRG002
~~~


~~~ bash title="WireGuard clients QR codes:"
armbian-config --cmd WRG003
~~~


~~~ bash title="WireGuard purge with data folder:"
armbian-config --cmd WRG004
~~~





## ZeroTier connect devices over your own private network in the world.

**Author:** @jnovos

**Status:** Stable


~~~ custombash
armbian-config --cmd ZTR001
~~~

