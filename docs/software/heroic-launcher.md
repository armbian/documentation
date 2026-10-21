---
title: "Heroic Launcher"
seo_title: "Install Heroic Launcher on Armbian"
description: "Install and run Heroic Launcher on Armbian — Install Heroic Launcher. Runs on ARM64 and x86 single-board computers."
image: /images/HERO01.png
category: "Gaming"
comments: true
---
# Heroic Launcher


<!--- section image START from tools/include/images/HERO01.png --->
![Heroic Launcher](/images/HERO01.png){ .app-logo }
<!--- section image STOP from tools/include/images/HERO01.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher)


<!--- header START from tools/include/markdown/HERO01-header.md --->
Heroic Games Launcher for GOG, Epic, and Amazon Games. One menu entry installs the latest release for this machine: the amd64 `.deb` on x86_64, or the arm64 `.deb` on arm64.

The package is `heroic`. Games and account data stay in the home directory when Heroic is removed.

<!--- header STOP from tools/include/markdown/HERO01-header.md --->


Install from **[armbian-config](/config/) → Software → Gaming → Heroic Launcher**

The app has no separate image. [Install an Armbian OS image first](/software/#how-to-install-an-app), then the app. For help with the app, [read its documentation](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher).

~~~ custombash title="CLI install"
armbian-config --cmd HERO01
~~~


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_heroic install` |
| Update Heroic Launcher | `armbian-config --api module_heroic update` |
| Remove Heroic Launcher | `armbian-config --api module_heroic remove` |
| Status | `armbian-config --api module_heroic status` |
| Help | `armbian-config --api module_heroic help` |

---

_Part of Armbian's [Game clients and compatibility tools](/software/gaming/) software._
