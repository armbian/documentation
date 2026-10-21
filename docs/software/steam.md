---
title: "Steam"
seo_title: "Install Steam on Armbian"
description: "Install and run Steam on Armbian — Install Steam. Runs on ARM64 and x86 single-board computers."
image: /images/STM001.png
category: "Gaming"
comments: true
---
# Steam


<!--- section image START from tools/include/images/STM001.png --->
![Steam](/images/STM001.png){ .app-logo }
<!--- section image STOP from tools/include/images/STM001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/armbian/configng/issues/941)


<!--- header START from tools/include/markdown/STM001-header.md --->
Steam for **arm64** and **amd64**.

On arm64, the installer downloads Valve's public-beta linuxarm64 client into the desktop user's home. Native x86_64 Linux games use the FEX tool shipped with Steam. The installer extracts FEX's official Arch rootfs to `~/.local/share/fex-emu/RootFS/ArchLinux` and links it to `/usr/share/guestos/fex-mesa`, which is the path Steam's FEX tool uses. It does not install a separate FEX package. Windows games use the FEX build shipped inside a Proton tree. Proton-CachyOS and Proton-GE are optional menu entries. Each installs the latest arm64 release into `compatibilitytools.d`. Because the FEX guest path is system-wide, only one user per system can run x86_64 games through this setup.

On amd64, the installer adds Valve's signed apt repository and installs the official `steam-launcher` package, plus the `steam-libs-amd64` and `steam-libs-i386` metapackages. The repository key is accepted only when its fingerprints match the keys Valve publishes. Apt then checks the `.deb` against that signed index. The client downloads the rest of Steam on first launch. Enabling the i386 architecture is required for 32-bit libraries and is left in place after removal. Proton-CachyOS and Proton-GE use the same menu entries as on arm64, with the x86_64 release archive.

<!--- header STOP from tools/include/markdown/STM001-header.md --->


Install from **[armbian-config](/config/) → Software → Gaming → Steam**

The app has no separate image. [Install an Armbian OS image first](/software/#how-to-install-an-app), then the app. For help with the app, [read its documentation](https://github.com/armbian/configng/issues/941).

~~~ custombash title="CLI install"
armbian-config --cmd STM001
~~~


<!--- footer START from tools/include/markdown/STM001-footer.md --->
=== "What gets installed"

    **arm64**

    - Steam client from the `linuxarm64` public-beta manifest, into `~/.local/share/Steam`
    - A desktop launcher that starts `steamrtarm64/steam`
    - FEX's official Arch rootfs, extracted to `~/.local/share/fex-emu/RootFS/ArchLinux` and linked from `/usr/share/guestos/fex-mesa` so x86_64 Linux games can start
    - Proton-CachyOS and Proton-GE only when you choose those menu entries. Each installs the latest arm64 release and replaces an older copy of the same tool

    Host packages supply `libibus` and `libva`. The installer does not download the steamrt3 tarball. **Update Steam** refreshes the FEX rootfs when FEX publishes a new image, and updates a Proton tool only when that tool is already installed.

    **amd64**

    - Valve's `steam-launcher` package from `https://repo.steampowered.com/steam/`
    - `steam-libs-amd64` and `steam-libs-i386`
    - The i386 dpkg architecture, when it is not already enabled
    - Proton-CachyOS and Proton-GE only when you choose those menu entries. Each installs the latest generic x86_64 release into `compatibilitytools.d` and replaces an older copy of the same tool

    **Update Steam** upgrades the launcher packages and updates a Proton tool only when that tool is already installed. The Steam client still updates itself after you launch it.

=== "First launch"

    On arm64, when the desktop user already has a graphical session, install runs `steam -deckard -exitsteam` once so the client can bootstrap, then quits. The menu entry itself does not use `-deckard`. Over SSH, with no display, that pass is skipped. Launch Steam from the menu and sign in. The first game launch lets Steam download Steam Linux Runtime 4.0 for arm64.

    On amd64, launch Steam from the menu and sign in. The official package downloads the client on that first launch.

=== "Remove and purge"

    - **Remove Proton-CachyOS** or **Remove Proton-GE** deletes that compatibility tool for this machine. Games and the Steam client stay. Each entry is shown only when that tool is installed.
    - **Remove** on arm64 deletes the client and any Proton-CachyOS or Proton-GE trees. Games, userdata, and the FEX rootfs stay. On amd64 it removes the `steam-launcher` package, the library metapackages, and any Proton-CachyOS or Proton-GE trees. Games and userdata stay, and Valve's apt repository stays so a later install can use it.
    - **Purge** deletes `~/.local/share/Steam`, `~/.steam`, and, when this module created them, the extracted FEX rootfs and a `libvpx.so.6` compatibility link. On amd64 it also removes the launcher packages, Valve's apt source, and the repository key. The i386 architecture is not turned back off.

<!--- footer STOP from tools/include/markdown/STM001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_steam install` |
| Update | `armbian-config --api module_steam update` |
| Remove Steam client | `armbian-config --api module_steam remove` |
| Purge Steam with games and userdata | `armbian-config --api module_steam purge` |
| Status | `armbian-config --api module_steam status` |
| Help | `armbian-config --api module_steam help` |
| Install or update Proton-CachyOS | `armbian-config --api module_steam proton-cachyos` |
| Install or update Proton-GE | `armbian-config --api module_steam proton-ge` |
| Proton-cachyos-remove | `armbian-config --api module_steam proton-cachyos-remove` |
| Proton-ge-remove | `armbian-config --api module_steam proton-ge-remove` |
| Proton-cachyos-status | `armbian-config --api module_steam proton-cachyos-status` |
| Proton-ge-status | `armbian-config --api module_steam proton-ge-status` |

---

_Part of Armbian's [Game clients and compatibility tools](/software/gaming/) software._
