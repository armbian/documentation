---
description: "Install, remove and configure desktop environments such as GNOME, KDE and XFCE on Armbian single-board computers with the armbian-config utility."
comments: true
---

# Desktop


Install, remove and configure desktop environments


<!--- header START from tools/include/markdown/Desktops-header.md --->
Armbian desktop installation uses upstream meta-packages from Debian and Ubuntu repositories, making it distro-agnostic and independent of pre-built Armbian desktop packages.

**Tiered installs**

Every desktop ships at one of three sizes. You can install at any tier and switch between tiers later without uninstalling.

| Tier | Contents | Approximate size |
|---|---|---|
| **Minimal** | Desktop environment + display manager + base utilities. No browser, no office suite. | ~500 MB |
| **Mid** | Minimal plus a browser, text editor, calculator, image and PDF viewer, media player, archive manager and torrent client. | ~1 GB |
| **Full** | Mid plus LibreOffice, GIMP, Inkscape, Thunderbird and Audacity. | ~2.5 GB |

The browser shipped at mid and full tiers is chosen automatically: `chromium` on Debian, `firefox-esr` on Debian riscv64, and `epiphany-browser` on Ubuntu (Ubuntu's `chromium` and `firefox` packages are snap-shim wrappers that don't work without `snapd`, which Armbian doesn't ship).

**How it works**

- Installs the desktop meta-package (e.g. `xfce4`, `gnome-session`) plus the per-tier extras and any release-specific packages your distribution needs.
- Tracks every package the install pulls in. The list is saved to `/etc/armbian/desktop/<de>.packages`, the chosen tier to `/etc/armbian/desktop/<de>.tier`. Uninstall and downgrade use these files so they only ever remove packages the desktop install added — packages you installed manually after the fact are never touched.
- Applies Armbian branding: wallpapers, icons, login screen theme, and default user settings.
- Configures the display manager (LightDM, GDM3 or SDDM) with auto-login enabled by default. You can disable auto-login from the desktop menu without removing the desktop.
- Sets up Profile Sync Daemon (psd) to keep browser profiles in RAM, reducing flash media wear.
- Removes a small set of unwanted extras pulled in by some meta-packages (e.g. Ubuntu's `apport` crash reporter, snap-related stubs).

**Switching tiers after install**

You don't need to reinstall to add or remove tier extras. The desktop menu offers "Change *desktop* to *tier*" entries for any tier other than the one currently installed. Behind the scenes:

- Going up (minimal → mid → full) installs only the new packages introduced by the higher tier.
- Going down (full → mid → minimal) removes only the packages the install added that aren't in the lower tier. Your manually-installed packages are not touched.

**Networking**

Some desktops (notably GNOME) require NetworkManager. When installed, NetworkManager is configured to coexist with Armbian's existing `systemd-networkd`: wired Ethernet stays managed by `systemd-networkd`, while NetworkManager handles WiFi and VPN connections. This avoids disrupting your existing network configuration.

**Supported desktops**

| Desktop | Best for | Approximate RAM (minimal tier) |
|---|---|---|
| XFCE | Single board computers, low-end hardware | ~300 MB |
| GNOME | Modern desktops, touchscreen devices | ~800 MB |
| Cinnamon | Users familiar with Windows layout | ~500 MB |
| MATE | Classic GNOME 2 fans, low-resource systems | ~350 MB |
| KDE Plasma | Power users, heavy customization | ~600 MB |
| i3-wm | Developers, keyboard-driven workflows | ~150 MB |
| Xmonad | Haskell tiling window manager | ~120 MB |
| Enlightenment | EFL-based, lightweight and stylish | ~250 MB |

Mid and full tiers add roughly 500 MB and 2 GB on top of these minimum figures, depending on which tier extras your release/architecture combination ships.

!!! warning "Desktop installation is resource-intensive"

    Installing a desktop environment will download and install a large number of packages. The full tier on a fresh Ubuntu image pulls in roughly 2.5 GB and may take a significant amount of time depending on your internet connection and device performance. A reboot is required after installation.

    Running `module_desktops remove` reclaims the disk space; `apt-get clean` is run automatically as part of the remove path.

!!! note "Switching desktops"

    Only one desktop environment should be installed at a time. Remove the current desktop before installing a different one to avoid package conflicts and mixed configurations.

<!--- header STOP from tools/include/markdown/Desktops-header.md --->

## Cinnamon


Install Cinnamon (minimal)


<!--- section image START from tools/include/images/CINM01.png --->
![Cinnamon](/images/CINM01.png)
<!--- section image STOP from tools/include/images/CINM01.png --->


<!--- header START from tools/include/markdown/CINM01-header.md --->
Cinnamon is a Linux desktop environment that provides advanced innovative features and a traditional user experience. The desktop layout is similar to GNOME 2 with underlying technology forked from GNOME Shell. Cinnamon makes users feel at home with an easy-to-use and comfortable desktop experience.

<!--- header STOP from tools/include/markdown/CINM01-header.md --->


~~~ bash title="Cinnamon"
armbian-config --cmd CINM01
~~~


<!--- footer START from tools/include/markdown/CINM01-footer.md --->
=== "Display Manager"

    Cinnamon uses **LightDM** as its default display manager.

=== "Session files"

    - `/usr/share/xsessions/cinnamon.desktop`
    - `/usr/share/xsessions/cinnamon2d.desktop`

=== "Autologin"

    Autologin configuration is stored in:

    - `/etc/lightdm/lightdm.conf.d/22-armbian-autologin.conf`

<!--- footer STOP from tools/include/markdown/CINM01-footer.md --->


~~~ bash title="Cinnamon mid"
armbian-config --cmd CINM05
~~~


~~~ bash title="Cinnamon full"
armbian-config --cmd CINM06
~~~


~~~ bash title="Uninstall Cinnamon"
armbian-config --cmd CINM02
~~~


~~~ bash title="Enable autologin (Cinnamon)"
armbian-config --cmd CINM03
~~~


~~~ bash title="Disable autologin (Cinnamon)"
armbian-config --cmd CINM04
~~~


~~~ bash title="Change Cinnamon to minimal"
armbian-config --cmd CINM07
~~~


~~~ bash title="Change Cinnamon to mid"
armbian-config --cmd CINM08
~~~


~~~ bash title="Change Cinnamon to full"
armbian-config --cmd CINM09
~~~










## GNOME


Install GNOME (minimal)


<!--- section image START from tools/include/images/GNME01.png --->
![GNOME](/images/GNME01.png)
<!--- section image STOP from tools/include/images/GNME01.png --->


<!--- header START from tools/include/markdown/GNME01-header.md --->
GNOME is a modern, user-friendly desktop environment for Linux, offering a clean interface, essential apps, and customization through extensions. It prioritizes simplicity, accessibility, and efficiency.

<!--- header STOP from tools/include/markdown/GNME01-header.md --->


~~~ bash title="GNOME"
armbian-config --cmd GNME01
~~~


<!--- footer START from tools/include/markdown/GNME01-footer.md --->
=== "Display Manager"

    GNOME uses **GDM3** as its default display manager.

=== "Session files"

    - `/usr/share/xsessions/gnome.desktop`

=== "Autologin"

    Autologin configuration is stored in:

    - `/etc/gdm3/custom.conf`

<!--- footer STOP from tools/include/markdown/GNME01-footer.md --->


~~~ bash title="GNOME mid"
armbian-config --cmd GNME05
~~~


~~~ bash title="GNOME full"
armbian-config --cmd GNME06
~~~


~~~ bash title="Uninstall GNOME"
armbian-config --cmd GNME02
~~~


~~~ bash title="Enable autologin (GNOME)"
armbian-config --cmd GNME03
~~~


~~~ bash title="Disable autologin (GNOME)"
armbian-config --cmd GNME04
~~~


~~~ bash title="Change GNOME to minimal"
armbian-config --cmd GNME07
~~~


~~~ bash title="Change GNOME to mid"
armbian-config --cmd GNME08
~~~


~~~ bash title="Change GNOME to full"
armbian-config --cmd GNME09
~~~










## MATE


Install MATE (minimal)


<!--- section image START from tools/include/images/MATE01.png --->
![MATE](/images/MATE01.png)
<!--- section image STOP from tools/include/images/MATE01.png --->


<!--- header START from tools/include/markdown/MATE01-header.md --->
MATE is a continuation of GNOME 2, providing a traditional desktop experience with a classic two-panel layout. It is lightweight, stable, and fully customizable — a good choice for users who prefer a familiar desktop without the overhead of modern compositing effects.

<!--- header STOP from tools/include/markdown/MATE01-header.md --->


~~~ bash title="MATE"
armbian-config --cmd MATE01
~~~


<!--- footer START from tools/include/markdown/MATE01-footer.md --->
=== "Display Manager"

    MATE uses **LightDM** as its default display manager.

=== "Session files"

    - `/usr/share/xsessions/mate.desktop`

=== "Autologin"

    Autologin configuration is stored in:

    - `/etc/lightdm/lightdm.conf.d/22-armbian-autologin.conf`

<!--- footer STOP from tools/include/markdown/MATE01-footer.md --->


~~~ bash title="MATE mid"
armbian-config --cmd MATE05
~~~


~~~ bash title="MATE full"
armbian-config --cmd MATE06
~~~


~~~ bash title="Uninstall MATE"
armbian-config --cmd MATE02
~~~


~~~ bash title="Enable autologin (MATE)"
armbian-config --cmd MATE03
~~~


~~~ bash title="Disable autologin (MATE)"
armbian-config --cmd MATE04
~~~


~~~ bash title="Change MATE to minimal"
armbian-config --cmd MATE07
~~~


~~~ bash title="Change MATE to mid"
armbian-config --cmd MATE08
~~~


~~~ bash title="Change MATE to full"
armbian-config --cmd MATE09
~~~










## i3


Install i3 (minimal)


<!--- section image START from tools/include/images/I3WM01.png --->
![i3](/images/I3WM01.png)
<!--- section image STOP from tools/include/images/I3WM01.png --->


<!--- header START from tools/include/markdown/I3WM01-header.md --->
i3 is a tiling window manager designed for power users and developers. It is keyboard-driven, highly configurable, and extremely lightweight — making it ideal for single board computers and headless-to-desktop conversions.

!!! info "Keyboard shortcuts"

    i3 is controlled primarily via keyboard. The default modifier key is **$mod** (Super/Windows key). Press **$mod+Enter** to open a terminal, **$mod+d** to launch applications via rofi, and **$mod+Shift+e** to exit.

<!--- header STOP from tools/include/markdown/I3WM01-header.md --->


~~~ bash title="i3"
armbian-config --cmd I3WM01
~~~


<!--- footer START from tools/include/markdown/I3WM01-footer.md --->
=== "Display Manager"

    i3 uses **LightDM** as its default display manager.

=== "Session files"

    - `/usr/share/xsessions/i3.desktop`

=== "Autologin"

    Autologin configuration is stored in:

    - `/etc/lightdm/lightdm.conf.d/22-armbian-autologin.conf`

<!--- footer STOP from tools/include/markdown/I3WM01-footer.md --->


~~~ bash title="i3 mid"
armbian-config --cmd I3WM05
~~~


~~~ bash title="i3 full"
armbian-config --cmd I3WM06
~~~


~~~ bash title="Uninstall i3"
armbian-config --cmd I3WM02
~~~


~~~ bash title="Enable autologin (i3)"
armbian-config --cmd I3WM03
~~~


~~~ bash title="Disable autologin (i3)"
armbian-config --cmd I3WM04
~~~


~~~ bash title="Change i3 to minimal"
armbian-config --cmd I3WM07
~~~


~~~ bash title="Change i3 to mid"
armbian-config --cmd I3WM08
~~~


~~~ bash title="Change i3 to full"
armbian-config --cmd I3WM09
~~~










## KDE Plasma


Install KDE Plasma (minimal)


<!--- section image START from tools/include/images/KDEP01.png --->
![KDE Plasma](/images/KDEP01.png)
<!--- section image STOP from tools/include/images/KDEP01.png --->


<!--- header START from tools/include/markdown/KDEP01-header.md --->
KDE Plasma is a feature-rich desktop environment with extensive customization options. It provides a familiar taskbar and start menu layout with modern effects, widgets, and a powerful system settings application.

<!--- header STOP from tools/include/markdown/KDEP01-header.md --->


~~~ bash title="KDE Plasma"
armbian-config --cmd KDEP01
~~~


<!--- footer START from tools/include/markdown/KDEP01-footer.md --->
=== "Display Manager"

    KDE Plasma uses **SDDM** as its default display manager.

=== "Session files"

    - `/usr/share/xsessions/plasma.desktop`

=== "Autologin"

    Autologin configuration is stored in:

    - `/etc/sddm.conf.d/autologin.conf`

<!--- footer STOP from tools/include/markdown/KDEP01-footer.md --->


~~~ bash title="KDE Plasma mid"
armbian-config --cmd KDEP05
~~~


~~~ bash title="KDE Plasma full"
armbian-config --cmd KDEP06
~~~


~~~ bash title="KDE Neon"
armbian-config --cmd KDEN01
~~~


<!--- footer START from tools/include/markdown/KDEN01-footer.md --->
=== "Display Manager"

    KDE Neon uses **SDDM** as its default display manager.

=== "Session files"

    - `/usr/share/wayland-sessions/plasma.desktop`
    - `/usr/share/xsessions/plasmax11.desktop`

=== "Autologin"

    Autologin configuration is stored in:

    - `/etc/sddm.conf.d/autologin.conf`

<!--- footer STOP from tools/include/markdown/KDEN01-footer.md --->


~~~ bash title="Uninstall KDE Plasma"
armbian-config --cmd KDEP02
~~~


~~~ bash title="Uninstall KDE Neon"
armbian-config --cmd KDEN02
~~~


~~~ bash title="Enable autologin (KDE Plasma)"
armbian-config --cmd KDEP03
~~~


~~~ bash title="Enable autologin (KDE Neon)"
armbian-config --cmd KDEN03
~~~


~~~ bash title="Disable autologin (KDE Plasma)"
armbian-config --cmd KDEP04
~~~


~~~ bash title="Disable autologin (KDE Neon)"
armbian-config --cmd KDEN04
~~~


~~~ bash title="Change KDE Plasma to minimal"
armbian-config --cmd KDEP07
~~~


~~~ bash title="Change KDE Plasma to mid"
armbian-config --cmd KDEP08
~~~


~~~ bash title="Change KDE Plasma to full"
armbian-config --cmd KDEP09
~~~














## Budgie [CSC]


Install Budgie [CSC]


~~~ bash title="Budgie [CSC]"
armbian-config --cmd BDGE01
~~~


~~~ bash title="Uninstall Budgie [CSC]"
armbian-config --cmd BDGE02
~~~


~~~ bash title="Enable autologin (Budgie) [CSC]"
armbian-config --cmd BDGE03
~~~


~~~ bash title="Disable autologin (Budgie) [CSC]"
armbian-config --cmd BDGE04
~~~





## Deepin [CSC]


Install Deepin [CSC]


~~~ bash title="Deepin [CSC]"
armbian-config --cmd DEEP01
~~~


~~~ bash title="Uninstall Deepin [CSC]"
armbian-config --cmd DEEP02
~~~


~~~ bash title="Enable autologin (Deepin) [CSC]"
armbian-config --cmd DEEP03
~~~


~~~ bash title="Disable autologin (Deepin) [CSC]"
armbian-config --cmd DEEP04
~~~





## Enlightenment [CSC]


Install Enlightenment [CSC]


~~~ bash title="Enlightenment [CSC]"
armbian-config --cmd ENLT01
~~~


~~~ bash title="Uninstall Enlightenment [CSC]"
armbian-config --cmd ENLT02
~~~


~~~ bash title="Enable autologin (Enlightenment) [CSC]"
armbian-config --cmd ENLT03
~~~


~~~ bash title="Disable autologin (Enlightenment) [CSC]"
armbian-config --cmd ENLT04
~~~





## Bianbu [CSC]


Install Bianbu (minimal) [CSC]


~~~ bash title="Bianbu [CSC]"
armbian-config --cmd BIAN01
~~~


~~~ bash title="Bianbu mid [CSC]"
armbian-config --cmd BIAN05
~~~


~~~ bash title="Bianbu full [CSC]"
armbian-config --cmd BIAN06
~~~


~~~ bash title="Uninstall Bianbu"
armbian-config --cmd BIAN02
~~~


~~~ bash title="Enable autologin (Bianbu)"
armbian-config --cmd BIAN03
~~~


~~~ bash title="Disable autologin (Bianbu)"
armbian-config --cmd BIAN04
~~~


~~~ bash title="Change Bianbu to minimal"
armbian-config --cmd BIAN07
~~~


~~~ bash title="Change Bianbu to mid"
armbian-config --cmd BIAN08
~~~


~~~ bash title="Change Bianbu to full"
armbian-config --cmd BIAN09
~~~










## XFCE


Install XFCE (minimal)


<!--- section image START from tools/include/images/XFCE01.png --->
![XFCE](/images/XFCE01.png)
<!--- section image STOP from tools/include/images/XFCE01.png --->


<!--- header START from tools/include/markdown/XFCE01-header.md --->
Xfce is a lightweight, fast, and user-friendly desktop environment for Linux, offering a classic interface, essential apps, and customization. It prioritizes performance, simplicity, and efficiency, making it an excellent choice for devices with limited resources.

<!--- header STOP from tools/include/markdown/XFCE01-header.md --->


~~~ bash title="XFCE"
armbian-config --cmd XFCE01
~~~


<!--- footer START from tools/include/markdown/XFCE01-footer.md --->
=== "Display Manager"

    Xfce uses **LightDM** as its default display manager.

=== "Session files"

    - `/usr/share/xsessions/xfce.desktop`

=== "Autologin"

    Autologin configuration is stored in:

    - `/etc/lightdm/lightdm.conf.d/22-armbian-autologin.conf`

<!--- footer STOP from tools/include/markdown/XFCE01-footer.md --->


~~~ bash title="XFCE mid"
armbian-config --cmd XFCE05
~~~


~~~ bash title="XFCE full"
armbian-config --cmd XFCE06
~~~


~~~ bash title="Uninstall XFCE"
armbian-config --cmd XFCE02
~~~


~~~ bash title="Enable autologin (XFCE)"
armbian-config --cmd XFCE03
~~~


~~~ bash title="Disable autologin (XFCE)"
armbian-config --cmd XFCE04
~~~


~~~ bash title="Change XFCE to minimal"
armbian-config --cmd XFCE07
~~~


~~~ bash title="Change XFCE to mid"
armbian-config --cmd XFCE08
~~~


~~~ bash title="Change XFCE to full"
armbian-config --cmd XFCE09
~~~









