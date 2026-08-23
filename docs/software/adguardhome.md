---
title: "AdGuardHome"
description: "Install and run AdGuardHome on Armbian — AdGuardHome DNS sinkhole. Runs on ARM64 and x86 single-board computers."
image: /images/ADG001.png
category: "DNS"
comments: true
---
# AdGuardHome


<!--- section image START from tools/include/images/ADG001.png --->
![AdGuardHome](/images/ADG001.png){ .app-logo }
<!--- section image STOP from tools/include/images/ADG001.png --->


<span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/AdguardTeam/AdGuardHome/wiki) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:3000`


<!--- header START from tools/include/markdown/ADG001-header.md --->
AdGuard Home is a network-wide software that functions as a DNS server and ad blocker. It blocks ads, trackers, and malicious websites at the DNS level, meaning it filters content for all devices connected to the network. It also provides additional features like parental controls, logging, and privacy protections. Essentially, it acts as a gateway between your devices and the internet, blocking unwanted content before it even reaches your devices.

<!--- header STOP from tools/include/markdown/ADG001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → DNS → AdGuardHome**

~~~ custombash title="CLI install"
armbian-config --cmd ADG001
~~~


<!--- footer START from tools/include/markdown/ADG001-footer.md --->
=== "Access to the web interface"

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


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_adguardhome install` |
| AdGuardHome purge with data folder | `armbian-config --api module_adguardhome remove` |
| Purge | `armbian-config --api module_adguardhome purge` |
| Status | `armbian-config --api module_adguardhome status` |
| Help | `armbian-config --api module_adguardhome help` |

---

_Part of Armbian's [Network-wide ad blockers servers](/User-Guide_Armbian-Software/DNS/) software._
