---
title: "git_cdn"
description: "Install and run git_cdn on Armbian — git_cdn GitHub caching proxy install. Runs on ARM64 and x86 single-board computers."
image: /images/GCD001.png
category: "Management"
comments: true
---
# git_cdn


git_cdn GitHub caching proxy install


<!--- section image START from tools/include/images/GCD001.png --->
![git_cdn](/images/GCD001.png){ .app-logo }
<!--- section image STOP from tools/include/images/GCD001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://gitlab.com/grouperenault/git_cdn) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8000`


Install from **[armbian-config](/armbian-config/) → Software → Management → git_cdn**

~~~ custombash title="CLI install"
armbian-config --cmd GCD001
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_git_cdn install` |
| git_cdn remove | `armbian-config --api module_git_cdn remove` |
| git_cdn purge with cache folder | `armbian-config --api module_git_cdn purge` |
| Status | `armbian-config --api module_git_cdn status` |
| Help | `armbian-config --api module_git_cdn help` |

---

_Part of Armbian's [Remote File & Management tools](/User-Guide_Armbian-Software/Management/) software._
