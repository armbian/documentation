---
title: "Unbound"
description: "Install and run Unbound on Armbian — Unbound caching DNS resolver. Runs on ARM64 and x86 single-board computers."
image: /images/UNB001.png
category: "DNS"
comments: true
---
# Unbound


<!--- section image START from tools/include/images/UNB001.png --->
![Unbound](/images/UNB001.png)
<!--- section image STOP from tools/include/images/UNB001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://unbound.docs.nlnetlabs.nl/en/latest/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:5335`


<!--- header START from tools/include/markdown/UNB001-header.md --->
Unbound is a high-performance, open-source DNS resolver. It primarily serves to resolve domain names into IP addresses for devices on a network. Unlike regular DNS servers, Unbound performs DNS lookups directly and securely, providing features like DNSSEC validation (ensuring data integrity) and privacy protections. It's often used to improve speed, security, and privacy by resolving queries locally rather than relying on external DNS services.
<!--- header STOP from tools/include/markdown/UNB001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → DNS → Unbound**

~~~ custombash title="CLI install"
armbian-config --cmd UNB001
~~~


<!--- footer START from tools/include/markdown/UNB001-footer.md --->
=== "Default DNS port"

    - Default DNS port: 8053

=== "Directories"

    - Install directory: `/armbian/unbound/`
    - Configuration directory: `/armbian/unbound/`

=== "View logs"

    ```sh
    docker logs -f unbound
    ```

<!--- footer STOP from tools/include/markdown/UNB001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_unbound install` |
| Unbound remove | `armbian-config --api module_unbound remove` |
| Unbound purge with data folder | `armbian-config --api module_unbound purge` |
| Status | `armbian-config --api module_unbound status` |
| Help | `armbian-config --api module_unbound help` |

---

_Part of Armbian's [Network-wide ad blockers servers](/User-Guide_Armbian-Software/DNS/) software._
