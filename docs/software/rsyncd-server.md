---
title: "Rsyncd server"
description: "Install and run Rsyncd server on Armbian — Rsyncd server. Runs on ARM64 and x86 single-board computers."
image: /images/RSD001.png
category: "Armbian"
comments: true
---
# Rsyncd server


<!--- section image START from tools/include/images/RSD001.png --->
![Rsyncd server](/images/RSD001.png){ .app-logo }
<!--- section image STOP from tools/include/images/RSD001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://forum.armbian.com/)


Install from **[armbian-config](/config/) → Software → Armbian → Rsyncd server**

~~~ custombash title="CLI install"
armbian-config --cmd RSD001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_armbian_rsyncd install` |
| Remove Armbian rsyncd server | `armbian-config --api module_armbian_rsyncd remove` |

---

_Part of Armbian's [Armbian infrastructure services](/User-Guide_Armbian-Software/Armbian/) software._
