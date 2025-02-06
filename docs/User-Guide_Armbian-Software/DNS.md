# Network-wide ad blockers servers


***

## Pi-hole DNS ad blocker

<!--- section image START from tools/include/images/DNS001.png --->
[![Pi-hole DNS ad blocker](/images/DNS001.png)](#)
<!--- section image STOP from tools/include/images/DNS001.png --->


<!--- header START from tools/include/markdown/DNS001-header.md --->
Pi-hole is a DNS sinkhole with web interface that will block ads for any device on your network.


<!--- header STOP from tools/include/markdown/DNS001-header.md --->

**Command:** 
~~~
armbian-config --cmd DNS001
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DNS001-footer.md --->
=== "Access the web interface"

    The web interface of Pi-hole can be accessed via:

    - URL = `http://<your.IP>/admin`
    - Password = 'Set / adjust from armbian-config'

=== "Documentation"

<https://docs.pi-hole.net/>

<!--- footer STOP from tools/include/markdown/DNS001-footer.md --->



***

## Pi-hole remove
**Command:** 
~~~
armbian-config --cmd DNS003
~~~

**Author:** @armbian

**Status:** Stable



***

## Pi-hole change web admin password
**Command:** 
~~~
armbian-config --cmd DNS002
~~~

**Author:** @armbian

**Status:** Stable



***

## Pi-hole purge with data folder
**Command:** 
~~~
armbian-config --cmd DNS004
~~~

**Author:** @armbian

**Status:** Stable



***

## Unbound caching DNS resolver

<!--- section image START from tools/include/images/UNB001.png --->
[![Unbound caching DNS resolver](/images/UNB001.png)](#)
<!--- section image STOP from tools/include/images/UNB001.png --->


<!--- header START from tools/include/markdown/UNB001-header.md --->
Unbound is a high-performance, open-source DNS resolver. It primarily serves to resolve domain names into IP addresses for devices on a network. Unlike regular DNS servers, Unbound performs DNS lookups directly and securely, providing features like DNSSEC validation (ensuring data integrity) and privacy protections. It's often used to improve speed, security, and privacy by resolving queries locally rather than relying on external DNS services.
<!--- header STOP from tools/include/markdown/UNB001-header.md --->

**Command:** 
~~~
armbian-config --cmd UNB001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Unbound remove
**Command:** 
~~~
armbian-config --cmd UNB002
~~~

**Author:** @armbian

**Status:** Stable



***

## Unbound purge with data folder
**Command:** 
~~~
armbian-config --cmd UNB003
~~~

**Author:** @armbian

**Status:** Stable



***

## AdGuardHome DNS sinkhole

<!--- section image START from tools/include/images/ADG001.png --->
[![AdGuardHome DNS sinkhole](/images/ADG001.png)](#)
<!--- section image STOP from tools/include/images/ADG001.png --->


<!--- header START from tools/include/markdown/ADG001-header.md --->
AdGuard Home is a network-wide software that functions as a DNS server and ad blocker. It blocks ads, trackers, and malicious websites at the DNS level, meaning it filters content for all devices connected to the network. It also provides additional features like parental controls, logging, and privacy protections. Essentially, it acts as a gateway between your devices and the internet, blocking unwanted content before it even reaches your devices.

<!--- header STOP from tools/include/markdown/ADG001-header.md --->

**Command:** 
~~~
armbian-config --cmd ADG001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## AdGuardHome remove
**Command:** 
~~~
armbian-config --cmd ADG002
~~~

**Author:** @armbian

**Status:** Stable



***

## AdGuardHome purge with data folder
**Command:** 
~~~
armbian-config --cmd ADG003
~~~

**Author:** @armbian

**Status:** Stable



***

