---
title: "Hastebin"
description: "Install and run Hastebin on Armbian — Hastebin Paste Server. Runs on ARM64 and x86 single-board computers."
image: /images/HPS001.png
category: "Media"
comments: true
---
# Hastebin


<!--- section image START from tools/include/images/HPS001.png --->
![Hastebin](/images/HPS001.png)
<!--- section image STOP from tools/include/images/HPS001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/rpardini/ansi-hastebin) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:7777`


<!--- header START from tools/include/markdown/HPS001-header.md --->
Hastebin is a fast and simple self-hosted pastebin server. It allows users to quickly share text snippets like logs, code, or notes via a web interface or API. Hastebin is lightweight, easy to deploy with Docker, and ideal for teams needing private, temporary paste storage.

<!--- header STOP from tools/include/markdown/HPS001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Media → Hastebin**

~~~ custombash title="CLI install"
armbian-config --cmd HPS001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_hastebin install` |
| Hastebin remove | `armbian-config --api module_hastebin remove` |
| Hastebin purge with data folder | `armbian-config --api module_hastebin purge` |
| Status | `armbian-config --api module_hastebin status` |
| Help | `armbian-config --api module_hastebin help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
