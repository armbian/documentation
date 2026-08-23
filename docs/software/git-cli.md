---
title: "Git CLI"
description: "Install and run Git CLI on Armbian — Install tools for cloning and managing repositories (git). Runs on ARM64 and x86 single-board computers."
image: /images/GIT001.png
category: "DevTools"
comments: true
---
# Git CLI


Install tools for cloning and managing repositories (git)


<!--- section image START from tools/include/images/GIT001.png --->
![Git CLI](/images/GIT001.png){ .app-logo }
<!--- section image STOP from tools/include/images/GIT001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://git-scm.com/doc)


Install from **[armbian-config](/armbian-config/) → Software → Dev Tools → Git CLI**

~~~ custombash title="CLI install"
armbian-config --cmd GIT001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_git-cli install` |
| Remove tools for cloning and managing repositories (git) | `armbian-config --api module_git-cli remove` |
| Status | `armbian-config --api module_git-cli status` |
| Help | `armbian-config --api module_git-cli help` |

---

_Part of Armbian's [Applications and tools for development](/User-Guide_Armbian-Software/DevTools/) software._
