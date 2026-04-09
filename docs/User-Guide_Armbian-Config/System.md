---
comments: true
---

# System wide and admin settings

## Hardware


Alternative kernels, headers, overlays, bootenv

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Kernel-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Kernel-header.md)  
#### Alternative kernels


Use alternative kernels


<!--- section image START from tools/include/images/KER001.png --->
[![Alternative kernels](/images/KER001.png)](#)
<!--- section image STOP from tools/include/images/KER001.png --->


<!--- header START from tools/include/markdown/KER001-header.md --->
Switching between different kernel versions can significantly impact the functionality of your device. A newer or older kernel may introduce changes to hardware compatibility, drivers, and system stability. Some features may stop working, while others may improve or be reintroduced.

!!! danger "Kernel changes carry inherent risks!"

    - A mismatched or incompatible kernel may result in **boot failures**, rendering the system unresponsive.
    - Certain peripherals or hardware components (e.g., Wi-Fi, GPU acceleration, or power management) may no longer function correctly.
    - Custom configurations or third-party modules might need to be recompiled or adjusted to work with the new kernel.

    Precautions Before Switching Kernels
    Before switching kernels, it is **strongly recommended** to:

    1. **Back up your system** to prevent data loss.
    2. **Verify compatibility** of your hardware and essential drivers with the target kernel version.
    3. **Keep a rescue method available**, such as a bootable SD card / USB drive or serial console access, to recover the system if necessary.

    Recovery Steps if Boot Fails
    If your device fails to boot after a kernel change, you may need to:

    - **Revert to a previous working kernel** using recovery options.
    - **Use a serial console or debug mode** to diagnose the issue.
    - **Reinstall the system** if no recovery options are available.

    **Exercise caution when switching kernels, especially on production systems or devices with limited recovery options.**

<!--- header STOP from tools/include/markdown/KER001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/KER001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/KER001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd KER001
~~~


#### Kernel Headers


Install Linux headers


<!--- section image START from tools/include/images/HEAD01.png --->
[![Kernel Headers](/images/HEAD01.png)](#)
<!--- section image STOP from tools/include/images/HEAD01.png --->


<!--- header START from tools/include/markdown/HEAD01-header.md --->
Kernel headers are files required to build modules (drivers) or software that interfaces directly with the Linux kernel. Installing headers ensures compatibility when compiling custom drivers, DKMS modules (like ZFS, WireGuard), or updating third-party software that requires access to kernel internals. The installed headers match your running kernel version and are critical for system extensions and hardware support.

<!--- header STOP from tools/include/markdown/HEAD01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/HEAD01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/HEAD01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd HEAD01
~~~


~~~ bash title="Remove Headers:"
armbian-config --cmd HEAD02
~~~



#### Device Tree Overlays


Manage device tree overlays


<!--- section image START from tools/include/images/DTO001.png --->
[![Device Tree Overlays](/images/DTO001.png)](#)
<!--- section image STOP from tools/include/images/DTO001.png --->


<!--- header START from tools/include/markdown/DTO001-header.md --->
Device Tree Overlays allow you to dynamically modify the Linux device tree at runtime, without rebuilding the kernel. They are used to enable or configure specific hardware features (like GPIO pins, I²C, SPI, sensors, displays) on single-board computers. Overlays are small snippets that can add, change, or remove parts of the hardware description, making it flexible to adapt the system for different peripherals without recompiling the full device tree.

<!--- header STOP from tools/include/markdown/DTO001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/DTO001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DTO001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd DTO001
~~~


#### Device Tree Editor


Edit device tree


<!--- section image START from tools/include/images/DTE001.png --->
[![Device Tree Editor](/images/DTE001.png)](#)
<!--- section image STOP from tools/include/images/DTE001.png --->


<!--- header START from tools/include/markdown/DTE001-header.md --->
The Device Tree Editor allows you to decompile, edit, and recompile device tree blobs (DTB) directly on your system. Device trees describe the hardware layout of your board to the Linux kernel. This tool provides a safe way to modify DTB files by decompiling them to human-readable DTS source, opening them in a text editor, validating the changes, and recompiling back to binary format.

!!! danger "Incorrect device tree changes can prevent your system from booting!"

    - Modifying the device tree can cause **hardware to stop functioning** or the system to **fail to boot entirely**.
    - Always verify your changes carefully before applying them.
    - A backup is created automatically before any modification, and can be restored from the module menu.
    - **Keep a rescue method available**, such as a bootable SD card or serial console access, to recover the system if necessary.

<!--- header STOP from tools/include/markdown/DTE001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/DTE001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/DTE001-header.md)  
__Status:__ Preview  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.kernel.org/devicetree/usage-model.html)  

~~~ custombash
armbian-config --cmd DTE001
~~~


<!--- footer START from tools/include/markdown/DTE001-footer.md --->
=== "Features"

    - **Select and edit** any DTB file from the device tree directory
    - **Edit active DTB** directly based on the `fdtfile` setting in `/boot/armbianEnv.txt`
    - **Automatic backups** before every modification with timestamped filenames
    - **Restore from backup** to revert to a previous device tree
    - **Validation** of edited DTS source before applying changes
    - **View device tree info** including model, compatible strings, and DTC version

=== "Requirements"

    - Package: `device-tree-compiler` (installed automatically if missing)
    - Device tree directory: `/boot/dtb/`

=== "Backup location"

    Backups are stored in `/boot/dtb/backup/` with the naming format:

    ```
    <original-name>.dtb.<YYYYMMDD_HHMMSS>.bak
    ```

<!--- footer STOP from tools/include/markdown/DTE001-footer.md --->


#### Odroid Boards Config


Select Odroid board configuration

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/ODR001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/ODR001-header.md)  
__Status:__ Preview  
__Architecture:__ <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  

~~~ custombash
armbian-config --cmd ODR001
~~~


#### Boot Environment


Edit the boot environment


<!--- section image START from tools/include/images/BOOT01.png --->
[![Boot Environment](/images/BOOT01.png)](#)
<!--- section image STOP from tools/include/images/BOOT01.png --->


<!--- header START from tools/include/markdown/BOOT01-header.md --->
Edit the boot environment allows you to modify critical boot settings stored in `/boot/armbianEnv.txt`. You can adjust options such as root filesystem location, kernel parameters, overlays, boot targets, or enable advanced features like early serial console. This is essential for fine-tuning hardware support, troubleshooting, or optimizing system startup behavior.

<!--- header STOP from tools/include/markdown/BOOT01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/BOOT01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/BOOT01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd BOOT01
~~~


## Desktop


Install, remove and configure desktop environments


<!--- header START from tools/include/markdown/Desktops-header.md --->
Armbian desktop installation uses upstream meta-packages from Debian and Ubuntu repositories, making it distro-agnostic and independent of pre-built Armbian desktop packages.

**How it works:**

- Installs the desktop environment meta-package (e.g., `xfce4`, `gnome-session`) along with essential extras
- Tracks all newly installed packages so uninstall cleanly removes everything added on top of CLI, including dependencies
- Applies Armbian branding: wallpapers, icons, login screen theme, and default user settings
- Configures the display manager (LightDM, GDM3, or SDDM) with auto-login (this can be disabled in menu)
- Installs [Armbian Imager](https://imager.armbian.com/) as an AppImage for writing OS images
- Sets up Profile Sync Daemon (psd) to keep browser profiles in RAM, reducing flash media wear
- Removes unnecessary bloat pulled in by meta-packages

**Networking:**

Desktop environments that require NetworkManager (e.g., GNOME) install it alongside the existing `systemd-networkd`. Wired Ethernet interfaces remain managed by `systemd-networkd`, while NetworkManager handles WiFi and VPN connections. This avoids disrupting existing network configuration.

**Supported desktops:**

| Desktop | Best for | Resources |
|---|---|---|
| XFCE | Single board computers, low-end hardware | ~300 MB RAM |
| GNOME | Modern desktops, touchscreen devices | ~800 MB RAM |
| Cinnamon | Users familiar with Windows layout | ~500 MB RAM |
| MATE | Classic GNOME 2 fans, low-resource systems | ~350 MB RAM |
| KDE Plasma | Power users, heavy customization | ~600 MB RAM |

!!! note "Switching desktops"

    Only one desktop environment should be installed at a time. Remove the current desktop before installing a different one to avoid package conflicts and mixed configurations.

<!--- header STOP from tools/include/markdown/Desktops-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Desktops-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/Desktops-header.md)  
#### Cinnamon


Cinnamon - traditional layout with modern features

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/CINMDE-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/CINMDE-header.md)  
###### Cinnamon desktop Install


<!--- section image START from tools/include/images/CINM01.png --->
[![Cinnamon desktop Install](/images/CINM01.png)](#)
<!--- section image STOP from tools/include/images/CINM01.png --->


<!--- header START from tools/include/markdown/CINM01-header.md --->
Cinnamon is a Linux desktop environment that provides advanced innovative features and a traditional user experience. The desktop layout is similar to GNOME 2 with underlying technology forked from GNOME Shell. Cinnamon makes users feel at home with an easy-to-use and comfortable desktop experience.

!!! warning "Desktop installation is resource-intensive"

    Installing a desktop environment will download and install a large number of packages. This process may take a significant amount of time depending on your internet connection and device performance. A reboot is required after installation.

<!--- header STOP from tools/include/markdown/CINM01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/CINM01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/CINM01-header.md)  
__Status:__ Stable  

~~~ custombash
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


~~~ bash title="Cinnamon desktop uninstall:"
armbian-config --cmd CINM02
~~~


~~~ bash title="Enable autologin:"
armbian-config --cmd CINM03
~~~


~~~ bash title="Disable autologin:"
armbian-config --cmd CINM04
~~~





#### GNOME


GNOME - modern, full-featured desktop

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/GNOMDE-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/GNOMDE-header.md)  
###### Gnome desktop Install


<!--- section image START from tools/include/images/GNME01.png --->
[![Gnome desktop Install](/images/GNME01.png)](#)
<!--- section image STOP from tools/include/images/GNME01.png --->


<!--- header START from tools/include/markdown/GNME01-header.md --->
GNOME is a modern, user-friendly desktop environment for Linux, offering a clean interface, essential apps, and customization through extensions. It prioritizes simplicity, accessibility, and efficiency.

!!! warning "Desktop installation is resource-intensive"

    Installing a desktop environment will download and install a large number of packages. This process may take a significant amount of time depending on your internet connection and device performance. A reboot is required after installation.

<!--- header STOP from tools/include/markdown/GNME01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/GNME01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/GNME01-header.md)  
__Status:__ Stable  

~~~ custombash
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


~~~ bash title="Uninstall:"
armbian-config --cmd GNME02
~~~


~~~ bash title="Enable autologin:"
armbian-config --cmd GNME03
~~~


~~~ bash title="Disable autologin:"
armbian-config --cmd GNME04
~~~





#### MATE


MATE - traditional GNOME 2 desktop

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/MATEDE-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/MATEDE-header.md)  
###### MATE desktop Install


<!--- section image START from tools/include/images/MATE01.png --->
[![MATE desktop Install](/images/MATE01.png)](#)
<!--- section image STOP from tools/include/images/MATE01.png --->


<!--- header START from tools/include/markdown/MATE01-header.md --->
MATE is a continuation of GNOME 2, providing a traditional desktop experience with a classic two-panel layout. It is lightweight, stable, and fully customizable — a good choice for users who prefer a familiar desktop without the overhead of modern compositing effects.

!!! warning "Desktop installation is resource-intensive"

    Installing a desktop environment will download and install a large number of packages. This process may take a significant amount of time depending on your internet connection and device performance. A reboot is required after installation.

<!--- header STOP from tools/include/markdown/MATE01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/MATE01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/MATE01-header.md)  
__Status:__ Stable  

~~~ custombash
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


~~~ bash title="Uninstall:"
armbian-config --cmd MATE02
~~~


~~~ bash title="Enable autologin:"
armbian-config --cmd MATE03
~~~


~~~ bash title="Disable autologin:"
armbian-config --cmd MATE04
~~~





#### i3-wm


i3 - lightweight tiling window manager

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/I3WMDE-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/I3WMDE-header.md)  
###### i3 desktop Install


<!--- section image START from tools/include/images/I3WM01.png --->
[![i3 desktop Install](/images/I3WM01.png)](#)
<!--- section image STOP from tools/include/images/I3WM01.png --->


<!--- header START from tools/include/markdown/I3WM01-header.md --->
i3 is a tiling window manager designed for power users and developers. It is keyboard-driven, highly configurable, and extremely lightweight — making it ideal for single board computers and headless-to-desktop conversions.

!!! info "Keyboard shortcuts"

    i3 is controlled primarily via keyboard. The default modifier key is **$mod** (Super/Windows key). Press **$mod+Enter** to open a terminal, **$mod+d** to launch applications via rofi, and **$mod+Shift+e** to exit.

!!! warning "Desktop installation is resource-intensive"

    Installing a desktop environment will download and install a large number of packages. This process may take a significant amount of time depending on your internet connection and device performance. A reboot is required after installation.

<!--- header STOP from tools/include/markdown/I3WM01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/I3WM01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/I3WM01-header.md)  
__Status:__ Stable  

~~~ custombash
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


~~~ bash title="i3 desktop uninstall:"
armbian-config --cmd I3WM02
~~~


~~~ bash title="Enable autologin:"
armbian-config --cmd I3WM03
~~~


~~~ bash title="Disable autologin:"
armbian-config --cmd I3WM04
~~~





#### KDE Plasma


KDE Plasma - feature-rich customizable desktop

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/KDEPDE-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/KDEPDE-header.md)  
###### KDE Plasma Install


<!--- section image START from tools/include/images/KDEP01.png --->
[![KDE Plasma Install](/images/KDEP01.png)](#)
<!--- section image STOP from tools/include/images/KDEP01.png --->


<!--- header START from tools/include/markdown/KDEP01-header.md --->
KDE Plasma is a feature-rich desktop environment with extensive customization options. It provides a familiar taskbar and start menu layout with modern effects, widgets, and a powerful system settings application.

!!! warning "Desktop installation is resource-intensive"

    Installing a desktop environment will download and install a large number of packages. This process may take a significant amount of time depending on your internet connection and device performance. A reboot is required after installation.

<!--- header STOP from tools/include/markdown/KDEP01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/KDEP01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/KDEP01-header.md)  
__Status:__ Stable  

~~~ custombash
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


~~~ bash title="Uninstall:"
armbian-config --cmd KDEP02
~~~


~~~ bash title="Enable autologin:"
armbian-config --cmd KDEP03
~~~


~~~ bash title="Disable autologin:"
armbian-config --cmd KDEP04
~~~





#### XFCE


XFCE - lightweight and fast desktop

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/XFCEDE-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/XFCEDE-header.md)  
###### XFCE desktop Install


<!--- section image START from tools/include/images/XFCE01.png --->
[![XFCE desktop Install](/images/XFCE01.png)](#)
<!--- section image STOP from tools/include/images/XFCE01.png --->


<!--- header START from tools/include/markdown/XFCE01-header.md --->
Xfce is a lightweight, fast, and user-friendly desktop environment for Linux, offering a classic interface, essential apps, and customization. It prioritizes performance, simplicity, and efficiency, making it an excellent choice for devices with limited resources.

!!! warning "Desktop installation is resource-intensive"

    Installing a desktop environment will download and install a large number of packages. This process may take a significant amount of time depending on your internet connection and device performance. A reboot is required after installation.

<!--- header STOP from tools/include/markdown/XFCE01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/XFCE01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/XFCE01-header.md)  
__Status:__ Stable  

~~~ custombash
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


~~~ bash title="Uninstall:"
armbian-config --cmd XFCE02
~~~


~~~ bash title="Enable autologin:"
armbian-config --cmd XFCE03
~~~


~~~ bash title="Disable autologin:"
armbian-config --cmd XFCE04
~~~





## Storage


Install to internal media, ZFS, NFS, read-only rootfs

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Storage-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Storage-header.md)  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  
#### Install


Copy the running Armbian system to another device


<!--- header START from tools/include/markdown/STO001-header.md --->
- Clones your current live OS installation
- Keeps your settings, configuration, installed packages, and user data
- Essentially “transfer my existing system to internal/external storage”

Use this option to **transfer your current live Armbian system** to another storage device (eMMC, SSD, USB, etc.).  This copies your existing installation exactly as it is — including settings, installed packages, and user data.

<!--- header STOP from tools/include/markdown/STO001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/STO001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/STO001-header.md)  
__Status:__ Preview  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd STO001
~~~


#### Download and flash


Download a fresh, official Armbian OS image and write it to a device


<!--- section image START from tools/include/images/FLASH1.png --->
[![Download and flash](/images/FLASH1.png)](#)
<!--- section image STOP from tools/include/images/FLASH1.png --->


<!--- header START from tools/include/markdown/FLASH1-header.md --->
What can this tool do?

- Install Armbian onto internal **eMMC, SSD, or other storage**
- Create **bootable SD cards or USB drives** for any supported board
- Recover a system by **re-flashing a clean image**
- Switch between different **OS variants, kernel branches, or preinstalled applications**
- Accelerate development with **fast, repeatable deployments** for testing and automation

<!--- header STOP from tools/include/markdown/FLASH1-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/FLASH1-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/FLASH1-header.md)  
__Status:__ Preview  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @igorpecovnik  

~~~ custombash
armbian-config --cmd FLASH1
~~~


<!--- footer START from tools/include/markdown/FLASH1-footer.md --->

<!--- footer STOP from tools/include/markdown/FLASH1-footer.md --->


~~~ bash title="Remove cached images:"
armbian-config --cmd FLASH2
~~~



#### Read Only FS


Enable read only filesystem


<!--- header START from tools/include/markdown/ROO001-header.md --->
Read-only filesystem is enabled using overlayroot, a utility that places a temporary writable layer over the system root filesystem. Changes made during runtime are redirected into RAM or an alternative writable storage, while the underlying system remains untouched. This ensures that after a reboot, the system returns to a clean original state. It's ideal for kiosks, appliances, SD card-based systems, and scenarios where long-term filesystem durability and recovery are critical.

<!--- header STOP from tools/include/markdown/ROO001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/ROO001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ROO001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd ROO001
~~~


~~~ bash title="Disable read only filesystem:"
armbian-config --cmd ROO002
~~~



#### NFS


Enable Network filesystem (NFS) support

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/NETF01-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/NETF01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd NETF01
~~~


~~~ bash title="Disable Network filesystem (NFS) support:"
armbian-config --cmd NETF02
~~~



###### NFS server


Enable network filesystem (NFS) daemon

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/NETF04-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/NETF04-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd NETF04
~~~


~~~ bash title="Configure network filesystem (NFS) daemon:"
armbian-config --cmd NETF05
~~~


~~~ bash title="Remove network filesystem (NFS) daemon:"
armbian-config --cmd NETF06
~~~


~~~ bash title="Show network filesystem (NFS) daemon clients:"
armbian-config --cmd NETF07
~~~





###### Find NFS servers


Find NFS servers in subnet and mount shares

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/NETF09-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/NETF09-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd NETF09
~~~


~~~ bash title="Show and manage NFS mounts:"
armbian-config --cmd NETF10
~~~



#### ZFS


ZFS filesystem - enable support


<!--- section image START from tools/include/images/ZFS001.png --->
[![ZFS](/images/ZFS001.png)](#)
<!--- section image STOP from tools/include/images/ZFS001.png --->


<!--- header START from tools/include/markdown/ZFS001-header.md --->
ZFS is an advanced, high-performance file system and volume manager designed for data integrity, scalability, and ease of use. It offers features like copy-on-write snapshots, native compression, data deduplication, automatic repair, and efficient storage pooling. Originally developed by Sun Microsystems, ZFS is ideal for handling large amounts of data reliably with minimal maintenance.

When enabling ZFS support, Armbian checks if the running kernel can support ZFS, installs matching kernel headers if necessary, and builds the ZFS DKMS (Dynamic Kernel Module Support) module automatically.

=== "ARC Cache Tuning"

    The **ARC (Adaptive Replacement Cache)** is ZFS's intelligent caching system.

    **Recommended Settings:**
    
    - **ARC Min:** 1/8 of RAM (minimum cache size)
    - **ARC Max:** 1/2 of RAM (maximum cache size)

    For memory-constrained ARM devices (1-2 GB RAM):
    
    - Consider limiting ARC to 256-512 MB to leave memory for applications
    - ARC Max = 0 means "use all available RAM" (may not be ideal for small systems)

    **Impact:**
    
    - Higher ARC = better read performance for frequently accessed data
    - Too high ARC can cause system swapping and degraded performance

=== "Dirty Data Tuning"

    **Dirty data** is modified data waiting to be written to disk.

    **Recommended Setting:**
    
    - **4% of RAM** (or 4% of ARC size, whichever is smaller)

    **Impact:**
    
    - Higher values = better write performance, more data loss risk on power failure
    - Lower values = safer data, more frequent disk writes

=== "TXG Timeout Tuning"

    **TXG (Transaction Group)** controls how often ZFS writes changes to disk.

    **Recommended Setting:**
    
    - **5 seconds** (default)

    **Range:** 1-30 seconds

    **Impact:**
    
    - Lower (1-3s): Better data safety, more disk writes, lower performance
    - Higher (10-30s): Better performance, more data loss risk on power failure

=== "Compression"

    ZFS compression is transparent and can actually **improve performance** by reducing I/O.

    **Options:**
    
    - **lz4**: Fast, good compression (recommended for most)
    - **zstd**: Better compression ratio, slightly slower CPU usage
    - **gzip**: Maximum compression, slowest
    - **off**: Disable compression

    **Note:** Compression setting only affects **new** datasets. Existing datasets keep their compression setting.

=== "Applying Configuration"

    Configuration is saved to `/etc/modprobe.d/zfs.conf` and requires reloading the ZFS module:

    ```bash
    # Option 1: Reboot (simplest)
    reboot

    # Option 2: Reload module (requires exporting all ZFS pools)
    zpool export -a
    rmmod zfs
    modprobe zfs
    ```

=== "Reset to Defaults"

    The tuning interface includes a "Reset to Defaults" option that:

    - Removes custom configuration from `/etc/modprobe.d/zfs.conf`
    - Resets all parameters to ZFS defaults
    - Requires module reload to take effect

=== "Pool Import"

    ZFS pools can be imported when they are not currently mounted. This is useful when:

    - Moving pools between systems
    - Booting from a different system with ZFS pools present
    - Pools were exported and need to be re-imported

    **Import Options:**

    - **Scan:** Lists all available pools that can be imported
    - **Import with original mount points:** Pool datasets mount at their configured locations
    - **Import with alternate mount point:** Pool datasets mount under a custom root directory

    **Force Import:**

    The import function uses `-f` flag to force import, which handles:

    - HostID mismatches between systems
    - Pool state issues
    - Active pools on other systems (use with caution)

    **Alternate Mount Point:**

    When importing with an alternate root (`altroot`):

    - Datasets mount under the specified path (e.g., `/mnt/pool`)
    - Original mount point configuration is preserved
    - Useful for temporary access or recovery scenarios

    **Note:** Default behavior is to use the pool's original mount points for maximum compatibility.

<!--- header STOP from tools/include/markdown/ZFS001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/ZFS001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ZFS001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd ZFS001
~~~


<!--- footer START from tools/include/markdown/ZFS001-footer.md --->
##### Key Features

###### Data Integrity
- **Copy-on-Write (CoW):** Prevents data corruption by never overwriting live data.
- **Checksumming:** Detects and corrects silent data corruption (bit rot).

###### Storage Management
- **Pooled Storage:** Eliminates the need for traditional partitions; all storage is managed dynamically.
- **Snapshots & Clones:** Creates instant backups without using extra storage.

###### Performance & Scalability
- **Efficient Compression & Deduplication:** Reduces storage usage without performance loss.
- **Dynamic Striping & Caching:** Distributes data across multiple disks for optimized read/write speeds.

###### Advanced Security
- **Native Encryption:** Supports dataset-level encryption for secure data storage.
- **RAID-Z:** A superior RAID alternative that prevents write-hole issues.


<!--- footer STOP from tools/include/markdown/ZFS001-footer.md --->


~~~ bash title="ZFS filesystem - remove support:"
armbian-config --cmd ZFS002
~~~


~~~ bash title="Tune ZFS:"
armbian-config --cmd ZFS003
~~~


~~~ bash title="Import ZFS Pool:"
armbian-config --cmd ZFS004
~~~





#### Memory


Memory management - enable features


<!--- section image START from tools/include/images/MEM001.png --->
[![Memory](/images/MEM001.png)](#)
<!--- section image STOP from tools/include/images/MEM001.png --->


<!--- header START from tools/include/markdown/MEM001-header.md --->
ZRAM is a Linux kernel module that creates compressed RAM-based block devices. It extends available memory by compressing pages and storing them in RAM, giving you more usable memory at the cost of some CPU overhead. On devices with limited RAM, ZRAM can significantly improve system responsiveness and prevent out-of-memory conditions.

When enabling memory management, Armbian installs the `zram-config` package if not already present, enables the `armbian-zram-config` service, and configures optimal swappiness settings for ZRAM-based swapping.

*Key Features*

- **Memory Compression**: Transparent ZRAM-based swap that extends available memory without application changes
- **Parallel Compression**: Multiple ZRAM devices utilize all CPU cores for maximum throughput
- **Algorithm Choice**: Select optimal compression for your hardware (lzo, lz4, zstd, lzo-rle)
- **Adaptive Swapping**: Swappiness tuned for ZRAM's in-RAM characteristics
- **Memory Overcommitment**: Support for swap sizes larger than physical RAM
- **Safe Defaults**: Sensible defaults based on your system's memory size

---

Perfect for **ARM-based SBCs**, **small form-factor PCs**, and **servers** where physical RAM is limited and disk-based swap would cause excessive I/O.

<!--- header STOP from tools/include/markdown/MEM001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/MEM001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/MEM001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd MEM001
~~~


<!--- footer START from tools/include/markdown/MEM001-footer.md --->
=== "Recommended Settings"

    Settings are automatically selected based on system memory:

    | System | ZRAM Size | Memory Limit | Swappiness |
    |--------|-----------|--------------|------------|
    | < 4 GB RAM | 50% | 50% | 100 |
    | 4+ GB RAM | 25% | 25% | 80 |

    - **Max Devices**: Set to CPU core count (capped at 8)
    - **Algorithm**: lzo (best for ARM), lz4 (fast on x86), zstd (best ratio, slower)

=== "Tuning Parameters"

    - **ZRAM Percentage** (10-300%): Swap space relative to physical RAM. With 50% on a 2GB system you get 1GB of swap, but compression (2:1 to 3:1) effectively holds 2-3GB
    - **Memory Limit** (10-100%): Prevents ZRAM from consuming too much physical RAM. Should generally match ZRAM percentage
    - **Swappiness** (1-100): How aggressively the kernel swaps to ZRAM. Use 80-100 for ZRAM (unlike disk swap where 60 is default)
    - **Max Devices** (1-8): Number of ZRAM devices, usually one per CPU core for parallel compression

=== "Troubleshooting"

    - **ZRAM not working**: Check `systemctl status armbian-zram-config` and `swapon --show`
    - **High CPU usage**: Normal during memory pressure. Reduce `ZRAM_PERCENTAGE` or switch to `lzo` algorithm
    - **Still out of memory**: Increase `ZRAM_PERCENTAGE` (up to 200-300% for read-heavy workloads)
    - **Algorithm not supported**: Run `cat /sys/block/zram0/comp_algorithm` to see available options
    - **Changes not applying**: Run `systemctl restart armbian-zram-config` or reboot

=== "Advanced Configuration"

    Edit `/etc/default/armbian-zram-config` directly for advanced options:

    ```sh
    # Backup first
    cp /etc/default/armbian-zram-config /etc/default/armbian-zram-config.bak

    # Edit configuration
    nano /etc/default/armbian-zram-config

    # Restart to apply
    systemctl restart armbian-zram-config
    ```

    **ZRAM backing device** - for systems with fast NVMe storage:

    ```sh
    # Add to /etc/default/armbian-zram-config
    ZRAM_BACKING_DEV=/dev/nvme0n1p4
    ```

    **Monitoring**:

    ```sh
    # Check compression ratio
    echo "scale=2; $(cat /sys/block/zram0/orig_data_size) / $(cat /sys/block/zram0/compr_data_size)" | bc

    # Monitor swap usage
    watch -n 1 'swapon --show && free -h'
    ```

=== "Configuration Files"

    - **`/etc/default/armbian-zram-config`**: Main ZRAM configuration
    - **`/etc/sysctl.d/99-armbian-memory.conf`**: Swappiness and VM parameters
    - **`zramctl`**: Show detailed ZRAM device statistics
    - **`swapon --show`**: Display active swap devices including ZRAM

<!--- footer STOP from tools/include/markdown/MEM001-footer.md --->


~~~ bash title="Memory:"
armbian-config --cmd MEM002
~~~


~~~ bash title="Tune Memory:"
armbian-config --cmd MEM003
~~~




## SSH daemon


Manage SSH daemon options, enable 2FA

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Access-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Access-header.md)  
#### Native


Disable root login


<!--- section image START from tools/include/images/ACC001.png --->
[![Native](/images/ACC001.png)](#)
<!--- section image STOP from tools/include/images/ACC001.png --->


<!--- header START from tools/include/markdown/ACC001-header.md --->
Manage native SSH daemon allows you to configure SSH server settings such as login security, authentication methods, and connection restrictions. It also enables setting up Two-Factor Authentication (2FA) to further secure SSH access using time-based codes (TOTP), adding an extra layer of protection beyond passwords.

<!--- header STOP from tools/include/markdown/ACC001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/ACC001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ACC001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd ACC001
~~~


~~~ bash title="Enable root login:"
armbian-config --cmd ACC002
~~~


~~~ bash title="Disable password login:"
armbian-config --cmd ACC003
~~~


~~~ bash title="Enable password login:"
armbian-config --cmd ACC004
~~~


~~~ bash title="Disable Public key authentication login:"
armbian-config --cmd ACC005
~~~


~~~ bash title="Enable Public key authentication login:"
armbian-config --cmd ACC006
~~~


~~~ bash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ bash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ bash title="Generate new OTP authentication QR code:"
armbian-config --cmd ACC009
~~~


~~~ bash title="Show OTP authentication QR code:"
armbian-config --cmd ACC010
~~~


~~~ bash title="Disable last login banner:"
armbian-config --cmd ACC011
~~~


~~~ bash title="Enable last login banner:"
armbian-config --cmd ACC012
~~~













#### Containerised


Sandboxed & containerised SSH server


<!--- section image START from tools/include/images/SSH001.png --->
[![Containerised](/images/SSH001.png)](#)
<!--- section image STOP from tools/include/images/SSH001.png --->


<!--- header START from tools/include/markdown/SSH001-header.md --->
Sandboxed & containerised SSH server allows ssh access without giving keys to the entire server. Giving ssh access via private key often means giving full access to the server. This container creates a limited and sandboxed environment that others can ssh into. The users only have access to the folders mapped and the processes running inside this container.
<!--- header STOP from tools/include/markdown/SSH001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/SSH001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/SSH001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.linuxserver.io/images/docker-openssh-server/#server-mode)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd SSH001
~~~


<!--- footer START from tools/include/markdown/SSH001-footer.md --->
=== "Access to SSH server"

    - `ssh username@<your.IP> -p 2222`

=== "Directories"

    - Install directory: `/armbian/openssh-server`
    - Configuration directory: `/armbian/openssh-server/config`
    - Shared storage directory: `USER_DEFINED`

=== "View logs"

    ```sh
    docker logs -f openssh-server
    ```

<!--- footer STOP from tools/include/markdown/SSH001-footer.md --->


~~~ bash title="Remove sandboxed SSH server:"
armbian-config --cmd SSH002
~~~


~~~ bash title="Purge sandboxed SSH server with data folder:"
armbian-config --cmd SSH003
~~~




## Shell and MOTD


Change shell, adjust MOTD

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/User-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/User-header.md)  
#### Change shell


Change shell system wide to ZSH


<!--- section image START from tools/include/images/SHELL1.png --->
[![Change shell](/images/SHELL1.png)](#)
<!--- section image STOP from tools/include/images/SHELL1.png --->


<!--- header START from tools/include/markdown/SHELL1-header.md --->
ZSH is a powerful and customizable shell designed to be an enhanced replacement for BASH. When combined with Oh My Zsh, which is integrated in `armbian-zsh`, it offers an extensive plugin system, beautiful themes, and productivity features like autosuggestions, syntax highlighting, and easier navigation.

<!--- header STOP from tools/include/markdown/SHELL1-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/SHELL1-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/SHELL1-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd SHELL1
~~~


~~~ bash title="Change shell system wide to BASH:"
armbian-config --cmd SHELL2
~~~



#### Adjust MOTD


Adjust welcome screen (motd)

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/MOTD01-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/MOTD01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd MOTD01
~~~


## OS Updates


OS updates and distribution upgrades

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Updates-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Updates-header.md)  
__Status:__ Active  
#### Firmware


Enable Armbian firmware upgrades


<!--- section image START from tools/include/images/UPD001.png --->
[![Firmware](/images/UPD001.png)](#)
<!--- section image STOP from tools/include/images/UPD001.png --->


<!--- header START from tools/include/markdown/UPD001-header.md --->
**Enable Armbian firmware upgrades** manages whether the Armbian firmware (kernel + u-boot + firmware) packages are held or unheld in the package manager. By removing or setting the hold, it controls if firmware updates are applied automatically through regular `apt update` and `apt upgrade` processes. This allows users to either freeze the firmware version for stability or enable updates for improved hardware support.

<!--- header STOP from tools/include/markdown/UPD001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/UPD001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/UPD001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd UPD001
~~~


~~~ bash title="Disable Armbian firmware upgrades:"
armbian-config --cmd UPD002
~~~



#### Rolling


Switch system to rolling packages repository


<!--- header START from tools/include/markdown/ROLLIN-header.md --->
The daily rolling repository offers frequently updated packages directly from development branches. It provides access to the latest features, bug fixes, and hardware support improvements but may introduce instability or regressions. This channel is intended for testing, development, and users who need the newest updates at the cost of reduced stability.

<!--- header STOP from tools/include/markdown/ROLLIN-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/ROLLIN-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ROLLIN-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd ROLLIN
~~~


#### Stable


Switch system to stable packages repository


<!--- header START from tools/include/markdown/STABLE-header.md --->
The stable repository provides thoroughly tested packages intended for production use. Updates from this channel prioritize stability, long-term reliability, and minimal risk, ensuring systems remain secure and operational without unexpected changes. Only critical bug fixes and essential improvements are introduced after extensive testing.

<!--- header STOP from tools/include/markdown/STABLE-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/STABLE-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/STABLE-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd STABLE
~~~


#### Stable Distro Upgrade


Distribution upgrade to latest stable / LTS


<!--- header START from tools/include/markdown/STD001-header.md --->
Stable / LTS upgrades move your system to a newer release of Debian or Ubuntu, bringing updated system packages along with long-term security fixes and bug patches. This makes them the safest choice for reliable, everyday use.

!!! Warning "Risks of Stable Upgrades"

    Distribution upgrades are experimental and **not supported by Armbian**. Use at your own risk.

    Even LTS → LTS upgrades (e.g., **Debian Bookworm → Trixie**, **Ubuntu Jammy → Noble**) carry some risks:

    - **Broken dependencies** – some packages may fail to upgrade or be removed.  
    - **Configuration overrides** – local changes may be replaced by defaults.  
    - **Downtime** – failed upgrades may require console access, manual recovery, or a full reinstall.  

    Because Armbian integrates upstream Debian/Ubuntu with custom board support packages, upgrades may still trigger **unexpected breakage** on some devices.  

<!--- header STOP from tools/include/markdown/STD001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/STD001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/STD001-header.md)  
__Status:__ Stable  

~~~ custombash
armbian-config --cmd STD001
~~~


<!--- footer START from tools/include/markdown/STD001-footer.md --->
Best Practices

1. **Back up your data** (system and configuration).  
2. **Test on a spare device or SD card** before upgrading production systems.  
3. **Read the official release notes** of your target distribution:  
- [Armbian FAQ: Can I upgrade my userspace flavor?](/User-Guide_FAQ/#can-i-upgrade-my-userspace-flavor-like-bullseye-to-bookworm-or-jammy-to-noble)  
- [Debian upgrade notes](https://www.debian.org/releases/trixie/release-notes/upgrading.en.html)  
- [Ubuntu release upgrade guide](https://documentation.ubuntu.com/server/how-to/software/upgrade-your-release/)  
4. **Ensure you have console access** (serial, HDMI + keyboard, SSH).  
5. **Consider fresh installs** if uptime and stability matter more than keeping the old environment.  

<!--- footer STOP from tools/include/markdown/STD001-footer.md --->


#### Unstable Distro Upgrade


Distribution upgrade to rolling unstable


<!--- header START from tools/include/markdown/UNS001-header.md --->
Non-LTS releases are intended for **developers, testers, and enthusiasts** who want the latest features — **not for production systems**.  

!!! Warning "Risks of Unstable Upgrades"

    Distribution upgrades are experimental and **not supported by Armbian**. Use at your own risk.

    - **High chance of breakage** – dependencies, bootloader, or kernel may fail.  
    - **Short lifecycle** – requires frequent re-upgrades (every ~6–9 months).  
    - **Unfinished features** – packages may be experimental or not fully supported.  
    - **Armbian compatibility** – integration with board support packages is less tested.  

<!--- header STOP from tools/include/markdown/UNS001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/UNS001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/UNS001-header.md)  
__Status:__ Stable  

~~~ custombash
armbian-config --cmd UNS001
~~~


#### Docker images


Enable automating Docker container base images updating


<!--- section image START from tools/include/images/WTC001.png --->
[![Docker images](/images/WTC001.png)](#)
<!--- section image STOP from tools/include/images/WTC001.png --->


<!--- header START from tools/include/markdown/WTC001-header.md --->
Watchtower is a lightweight tool that automatically monitors and updates running Docker containers whenever a new image version becomes available.
It checks remote registries for updated images, pulls them, stops the old containers, and restarts them using the updated versions — all without manual intervention.
Watchtower is fully configurable, allowing you to control update frequency, select specific containers, and manage notification settings.

<!--- header STOP from tools/include/markdown/WTC001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/WTC001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/WTC001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://containrrr.dev/watchtower/)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd WTC001
~~~


~~~ bash title="Disable automating Docker container base images updating:"
armbian-config --cmd WTC002
~~~



#### Packages


Enable automatic package updates.


<!--- section image START from tools/include/images/UNAT01.png --->
[![Packages](/images/UNAT01.png)](#)
<!--- section image STOP from tools/include/images/UNAT01.png --->


<!--- header START from tools/include/markdown/UNAT01-header.md --->
Unattended upgrades automatically install security updates and important package updates on your system without requiring manual intervention. It helps keep your system secure, stable, and up-to-date by silently applying patches. The behavior is fully configurable — you can control which packages are upgraded, set reboot options, and customize notifications or logging.

<!--- header STOP from tools/include/markdown/UNAT01-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/UNAT01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/UNAT01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd UNAT01
~~~


~~~ bash title="Configure automatic package updates:"
armbian-config --cmd UNAT02
~~~


~~~ bash title="Disable automatic package updates:"
armbian-config --cmd UNAT03
~~~



