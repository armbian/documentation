---
title: "Pi-hole"
description: "Install and run Pi-hole on Armbian — Pi-hole DNS ad blocker with Unbound support. Runs on ARM64 and x86 single-board computers."
image: /images/PIH001.png
category: "DNS"
comments: true
---
# Pi-hole


<!--- section image START from tools/include/images/PIH001.png --->
![Pi-hole](/images/PIH001.png){ .app-logo }
<!--- section image STOP from tools/include/images/PIH001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.pi-hole.net/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8811`


<!--- header START from tools/include/markdown/PIH001-header.md --->
**Pi-hole** is a network-wide ad blocker that acts as a DNS (Domain Name System) sinkhole. It blocks connections to known ad servers, trackers, and malicious domains across all devices in your network, without requiring any browser extensions or client-side software.

### Pi-hole Explained

- **DNS-Based Filtering**
Pi-hole intercepts DNS queries made by devices on your network. When a domain is requested, Pi-hole checks it against a set of blocklists. If the domain is known to serve ads or track user activity, Pi-hole blocks the request, preventing unwanted content from loading.

- **Customizable Blocklists**
You can choose from various community-maintained blocklists or add your own. These lists contain domains associated with ads, trackers, malware, or other undesirable content.

- **Whole-Network Protection**
Once Pi-hole is configured as your network’s DNS server, all devices - smartphones, laptops, smart TVs, and IoT devices - are automatically protected. No additional configuration or software is required on the individual devices.

- **Built-in Recursive DNS with Unbound**
For added privacy and full DNS resolution control, [Unbound](#unbound) is installed and enabled by default during Pi-hole installation. Unbound functions as a local recursive DNS resolver, fetching responses directly from authoritative DNS servers rather than relying on upstream providers. This minimizes third-party exposure and can improve query performance.

- **Web Interface**
Pi-hole includes a web-based dashboard that provides real-time visibility into DNS activity. The interface allows you to view statistics, manage blocklists, whitelist domains, and configure settings with ease.

- **Privacy and Performance Benefits**
By blocking unwanted domains at the DNS level, Pi-hole reduces page load times, lowers bandwidth usage, and enhances user privacy by preventing tracking scripts and ads from reaching client devices.

- **Platform Compatibility**
Pi-hole can be installed on a variety of platforms. It runs well on lightweight systems such as **Armbian Minimal**, but is also available as a Docker container and supports deployment on most Linux-based environments.

Pi-hole offers an effective and centralized way to enhance privacy and reduce unwanted content across your entire network.

<!--- header STOP from tools/include/markdown/PIH001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → DNS → Pi-hole**

~~~ custombash title="CLI install"
armbian-config --cmd PIH001
~~~


<!--- footer START from tools/include/markdown/PIH001-footer.md --->
=== "Access the web interface"

    - Password is set on install and can be adjusted from `armbian-config`

<!--- footer STOP from tools/include/markdown/PIH001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_pi_hole install` |
| Pi-hole remove | `armbian-config --api module_pi_hole remove` |
| Pi-hole purge with data folder | `armbian-config --api module_pi_hole purge` |
| Pi-hole change web admin password | `armbian-config --api module_pi_hole password` |
| Status | `armbian-config --api module_pi_hole status` |
| Help | `armbian-config --api module_pi_hole help` |

---

_Part of Armbian's [Network-wide ad blockers servers](/User-Guide_Armbian-Software/DNS/) software._
