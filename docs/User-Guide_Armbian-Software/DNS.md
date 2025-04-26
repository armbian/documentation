---
comments: true
---

# Network-wide ad blockers servers

## Pi-hole DNS ad blocker

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/DNS001.png --->
[![Pi-hole DNS ad blocker](/images/DNS001.png)](#)
<!--- section image STOP from tools/include/images/DNS001.png --->


<!--- header START from tools/include/markdown/DNS001-header.md --->
Pi-hole is a network-wide ad blocker that acts as a DNS (Domain Name System) sinkhole. It works by blocking requests to known ad servers, trackers, and malicious websites across all devices connected to your home network. Here's how it works:

- DNS-Based Filtering: Pi-hole intercepts DNS requests from devices on your network. When a device tries to connect to a website, Pi-hole checks if the website's domain is on a blocklist. If it is, Pi-hole prevents the connection from being made, effectively blocking ads, trackers, and potentially harmful sites.

- Customizable Blocklists: Pi-hole allows you to choose from a variety of community-maintained blocklists or even add your own. These blocklists contain domains known to serve ads, trackers, and other unwanted content.

- Device and Network-Level Protection: Once set up, Pi-hole works across your entire network. This means all devices (smartphones, tablets, computers, smart TVs, etc.) that use your Pi-hole as their DNS server automatically benefit from ad-blocking without needing individual apps or browser extensions.

- Web Interface: Pi-hole offers an intuitive web interface where you can monitor statistics, review blocked domains, and tweak settings like adding custom blocklists or whitelisting certain sites.

- Privacy and Speed: By blocking unwanted content at the DNS level, Pi-hole not only improves browsing speed (since ads are not loaded), but also enhances privacy by preventing tracking scripts from running in the background.

Pi-hole is typically installed on a Armbian minimal, but it can also run on other systems. It's a great way to have ad-blocking and privacy protection across your entire network without needing to install anything on individual devices.
<!--- header STOP from tools/include/markdown/DNS001-header.md --->


~~~ bash title="Pi-hole DNS ad blocker:"
armbian-config --cmd DNS001
~~~

## Pi-hole remove


~~~ bash title="Pi-hole remove:"
armbian-config --cmd DNS003
~~~

## Pi-hole change web admin password


~~~ bash title="Pi-hole change web admin password:"
armbian-config --cmd DNS002
~~~

## Pi-hole purge with data folder


~~~ bash title="Pi-hole purge with data folder:"
armbian-config --cmd DNS004
~~~

## Unbound caching DNS resolver


<!--- section image START from tools/include/images/UNB001.png --->
[![Unbound caching DNS resolver](/images/UNB001.png)](#)
<!--- section image STOP from tools/include/images/UNB001.png --->


<!--- header START from tools/include/markdown/UNB001-header.md --->
Unbound is a high-performance, open-source DNS resolver. It primarily serves to resolve domain names into IP addresses for devices on a network. Unlike regular DNS servers, Unbound performs DNS lookups directly and securely, providing features like DNSSEC validation (ensuring data integrity) and privacy protections. It's often used to improve speed, security, and privacy by resolving queries locally rather than relying on external DNS services.
<!--- header STOP from tools/include/markdown/UNB001-header.md --->


~~~ bash title="Unbound caching DNS resolver:"
armbian-config --cmd UNB001
~~~

## Unbound remove


~~~ bash title="Unbound remove:"
armbian-config --cmd UNB002
~~~

## Unbound purge with data folder


~~~ bash title="Unbound purge with data folder:"
armbian-config --cmd UNB003
~~~

## AdGuardHome DNS sinkhole


<!--- section image START from tools/include/images/ADG001.png --->
[![AdGuardHome DNS sinkhole](/images/ADG001.png)](#)
<!--- section image STOP from tools/include/images/ADG001.png --->


<!--- header START from tools/include/markdown/ADG001-header.md --->
AdGuard Home is a network-wide software that functions as a DNS server and ad blocker. It blocks ads, trackers, and malicious websites at the DNS level, meaning it filters content for all devices connected to the network. It also provides additional features like parental controls, logging, and privacy protections. Essentially, it acts as a gateway between your devices and the internet, blocking unwanted content before it even reaches your devices.

<!--- header STOP from tools/include/markdown/ADG001-header.md --->


~~~ bash title="AdGuardHome DNS sinkhole:"
armbian-config --cmd ADG001
~~~

## AdGuardHome remove


~~~ bash title="AdGuardHome remove:"
armbian-config --cmd ADG002
~~~

## AdGuardHome purge with data folder


~~~ bash title="AdGuardHome purge with data folder:"
armbian-config --cmd ADG003
~~~
