---
comments: true
---

# Network-wide ad blockers servers

## AdGuardHome


AdGuardHome DNS sinkhole


<!--- section image START from tools/include/images/ADG001.png --->
[![AdGuardHome](/images/ADG001.png)](#)
<!--- section image STOP from tools/include/images/ADG001.png --->


<!--- header START from tools/include/markdown/ADG001-header.md --->
AdGuard Home is a network-wide software that functions as a DNS server and ad blocker. It blocks ads, trackers, and malicious websites at the DNS level, meaning it filters content for all devices connected to the network. It also provides additional features like parental controls, logging, and privacy protections. Essentially, it acts as a gateway between your devices and the internet, blocking unwanted content before it even reaches your devices.

<!--- header STOP from tools/include/markdown/ADG001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/ADG001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ADG001-header.md)  
__Status:__ Stable  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/AdguardTeam/AdGuardHome/wiki)  

~~~ custombash
armbian-config --cmd ADG001
~~~


<!--- footer START from tools/include/markdown/ADG001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3000**:

    - URL: `https://<your.IP>:3000`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/adguardhome/`
    - Configuration directory: `/armbian/adguardhome/confdir`
    - Work directory: `/armbian/adguardhome/workdir`

=== "Usage"

    - server where you are installing is automatically switched to this DNS
    - on your desktop PC set IP address of this server as DNS
    - network wide: set IP address of this server on routers DNS

=== "Black and white lists"

    There are many sites in the web giving blocklists and whitelists for AdGuard Home. They can be used when you want to have more blocking as the standard installation gives you. Here are some examples:

    - [The Big Blocklist Collection by WaLLy3K](https://firebog.net/)
    - [Phishing Army blocklist](https://phishing.army/)
    - [Whitelist collection by anudeepND](https://github.com/anudeepND/whitelist)

=== "View logs"

    ```sh
    docker logs -f adguardhome
    ```

<!--- footer STOP from tools/include/markdown/ADG001-footer.md --->


~~~ bash title="AdGuardHome remove:"
armbian-config --cmd ADG002
~~~


~~~ bash title="AdGuardHome purge with data folder:"
armbian-config --cmd ADG003
~~~




## Pi-hole


Pi-hole DNS ad blocker


<!--- section image START from tools/include/images/PIH001.png --->
[![Pi-hole](/images/PIH001.png)](#)
<!--- section image STOP from tools/include/images/PIH001.png --->


<!--- header START from tools/include/markdown/PIH001-header.md --->
Pi-hole is a network-wide ad blocker that acts as a DNS (Domain Name System) sinkhole. It works by blocking requests to known ad servers, trackers, and malicious websites across all devices connected to your home network. Here's how it works:

- DNS-Based Filtering: Pi-hole intercepts DNS requests from devices on your network. When a device tries to connect to a website, Pi-hole checks if the website's domain is on a blocklist. If it is, Pi-hole prevents the connection from being made, effectively blocking ads, trackers, and potentially harmful sites.

- Customizable Blocklists: Pi-hole allows you to choose from a variety of community-maintained blocklists or even add your own. These blocklists contain domains known to serve ads, trackers, and other unwanted content.

- Device and Network-Level Protection: Once set up, Pi-hole works across your entire network. This means all devices (smartphones, tablets, computers, smart TVs, etc.) that use your Pi-hole as their DNS server automatically benefit from ad-blocking without needing individual apps or browser extensions.

- Web Interface: Pi-hole offers an intuitive web interface where you can monitor statistics, review blocked domains, and tweak settings like adding custom blocklists or whitelisting certain sites.

- Privacy and Speed: By blocking unwanted content at the DNS level, Pi-hole not only improves browsing speed (since ads are not loaded), but also enhances privacy by preventing tracking scripts from running in the background.

Pi-hole is typically installed on a Armbian minimal, but it can also run on other systems. It's a great way to have ad-blocking and privacy protection across your entire network without needing to install anything on individual devices.
<!--- header STOP from tools/include/markdown/PIH001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/PIH001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/PIH001-header.md)  
__Status:__ Stable  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.pi-hole.net/)  

~~~ custombash
armbian-config --cmd PIH001
~~~


<!--- footer START from tools/include/markdown/PIH001-footer.md --->
=== "Access the web interface"

    The web interface of Pi-hole can be accessed via:

    - URL = `http://<your.IP>/admin`
    - Password is set and adjust from `armbian-config`

=== "Documentation"

<https://docs.pi-hole.net/>

<!--- footer STOP from tools/include/markdown/PIH001-footer.md --->


~~~ bash title="Pi-hole change web admin password:"
armbian-config --cmd PIH002
~~~


~~~ bash title="Pi-hole remove:"
armbian-config --cmd PIH003
~~~


~~~ bash title="Pi-hole purge with data folder:"
armbian-config --cmd PIH004
~~~





## Unbound


Unbound caching DNS resolver


<!--- section image START from tools/include/images/UNB001.png --->
[![Unbound](/images/UNB001.png)](#)
<!--- section image STOP from tools/include/images/UNB001.png --->


<!--- header START from tools/include/markdown/UNB001-header.md --->
Unbound is a high-performance, open-source DNS resolver. It primarily serves to resolve domain names into IP addresses for devices on a network. Unlike regular DNS servers, Unbound performs DNS lookups directly and securely, providing features like DNSSEC validation (ensuring data integrity) and privacy protections. It's often used to improve speed, security, and privacy by resolving queries locally rather than relying on external DNS services.
<!--- header STOP from tools/include/markdown/UNB001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/UNB001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/UNB001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://unbound.docs.nlnetlabs.nl/en/latest/)  

~~~ custombash
armbian-config --cmd UNB001
~~~


<!--- footer START from tools/include/markdown/UNB001-footer.md --->
=== "Default DNS port"

    - Default DNS port: 53

=== "Directories"

    - Install directory: `/armbian/unbound/`
    - Configuration directory: `/armbian/unbound/`

=== "View logs"

    ```sh
    docker logs -f unbound
    ```

<!--- footer STOP from tools/include/markdown/UNB001-footer.md --->


~~~ bash title="Unbound remove:"
armbian-config --cmd UNB002
~~~


~~~ bash title="Unbound purge with data folder:"
armbian-config --cmd UNB003
~~~



