---
title: "CDN router"
description: "Install and run CDN router on Armbian — Router for repository mirror automation. Runs on ARM64 and x86 single-board computers."
image: /images/ART001.png
category: "Armbian"
comments: true
---
# CDN router


<!--- section image START from tools/include/images/ART001.png --->
![CDN router](/images/ART001.png){ .app-logo }
<!--- section image STOP from tools/include/images/ART001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://forum.armbian.com/)


<!--- header START from tools/include/markdown/ART001-header.md --->
The Armbian Router is an intelligent redirector system that optimizes file downloads by automatically directing users to the best available mirror. It evaluates each download request based on geographic location, server health, and file availability, ensuring faster downloads, balanced load distribution, and high availability. This core service underpins Armbian's scalable mirror network, seamlessly routing traffic to improve performance and reliability for end users worldwide.

<!--- header STOP from tools/include/markdown/ART001-header.md --->


Install from **[armbian-config](/config/) → Software → Armbian → CDN router**

~~~ custombash title="CLI install"
armbian-config --cmd ART001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_armbianrouter install` |
| Remove CDN router | `armbian-config --api module_armbianrouter remove` |

---

_Part of Armbian's [Armbian infrastructure services](/User-Guide_Armbian-Software/Armbian/) software._
