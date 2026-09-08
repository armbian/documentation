---
title: "HedgeDoc"
seo_title: "Install HedgeDoc on Armbian"
description: "Install and run HedgeDoc on Armbian — HedgeDoc collaborative markdown editor install. Runs on ARM64 and x86 single-board computers."
image: /images/HDOC01.png
category: "WebHosting"
comments: true
---
# HedgeDoc


<!--- section image START from tools/include/images/HDOC01.png --->
![HedgeDoc](/images/HDOC01.png){ .app-logo }
<!--- section image STOP from tools/include/images/HDOC01.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.hedgedoc.org/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:3100`


<!--- header START from tools/include/markdown/HDOC01-header.md --->
HedgeDoc is a powerful, locally hosted web-based collaborative Markdown editor. It allows you to create, edit, and share documents in real time, supporting teamwork with live collaboration, version history, and easy publishing. This self-hosted application provides a flexible and secure environment for writing notes, documentation, and knowledge bases, offering a complete solution for collaborative text editing and documentation management.

<!--- header STOP from tools/include/markdown/HDOC01-header.md --->


Install from **[armbian-config](/config/) → Software → Web Hosting → HedgeDoc**

~~~ custombash title="CLI install"
armbian-config --cmd HDOC01
~~~


<!--- footer START from tools/include/markdown/HDOC01-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3100**:

    - URL: `http://<your.IP>:3100`

=== "Directories"

    - Install directory: `/armbian/hedgedoc`

=== "View logs"

    ```sh
    docker logs -f hedgedoc
    ```

<!--- footer STOP from tools/include/markdown/HDOC01-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_hedgedoc install` |
| HedgeDoc remove | `armbian-config --api module_hedgedoc remove` |
| HedgeDoc purge with data folder | `armbian-config --api module_hedgedoc purge` |
| Status | `armbian-config --api module_hedgedoc status` |
| Help | `armbian-config --api module_hedgedoc help` |

---

_Part of Armbian's [Web server, LEMP, reverse proxy, Let's Encrypt SSL](/software/web-hosting/) software._
