---
title: "OMV"
seo_title: "Install OMV on Armbian"
description: "Install and run OMV on Armbian — Deploy NAS using OpenMediaVault. Runs on ARM64 and x86 single-board computers."
image: /images/OMV001.png
category: "Media"
comments: true
---
# OMV


<!--- section image START from tools/include/images/OMV001.png --->
![OMV](/images/OMV001.png){ .app-logo }
<!--- section image STOP from tools/include/images/OMV001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">amd64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">i386</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.openmediavault.org/en/stable/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:80`


<!--- header START from tools/include/markdown/OMV001-header.md --->
OpenMediaVault (OMV) is a powerful, open-source network-attached storage (NAS) operating system built on the Debian Linux distribution. It is designed to provide a simple and intuitive web-based interface for managing storage devices and network services, making it ideal for home users, small offices, and even advanced users looking for a customizable and efficient NAS solution.

OMV supports a wide range of features, including various file systems (EXT4, XFS, BTRFS, etc.), software RAID configurations, scheduled backups, and user and group management. It offers support for common network protocols such as SMB/CIFS (Windows file sharing), NFS, FTP, and SSH, enabling seamless file access across different platforms.

Through its modular design, OpenMediaVault can be easily extended with plugins, allowing users to add functionality like Docker support, media servers, cloud synchronization tools, BitTorrent clients, and more. The system is designed for stability and ease of use, with regular updates and a strong community supporting development and troubleshooting.

Whether used on a dedicated server, a Raspberry Pi, or virtualized hardware, OMV provides a flexible and reliable way to build your own custom NAS.  

**Warning**: installation works only on Debian (bookworm) based Armbian image.
<!--- header STOP from tools/include/markdown/OMV001-header.md --->


Install from **[armbian-config](/config/) → Software → Media → OMV**

~~~ custombash title="CLI install"
armbian-config --cmd OMV001
~~~


<!--- footer START from tools/include/markdown/OMV001-footer.md --->
=== "Access to the web interface"

    - Username/Password: admin / openmediavault (change after first login)

=== "Directories"

    - Default config directory: `/etc/openmediavault/`
    - Shared folders base path: `/srv/dev-disk-by-.../`
    - Plugin data directories may vary by service (e.g., Docker, SMB, etc.)

=== "Usage"

    - Use the web interface to configure storage, users, services, and plugins
    - Create shared folders and enable SMB/NFS to access files over the network
    - Monitor system status, performance, and logs from the dashboard

=== "Plugins and Add-ons"

    OpenMediaVault supports a wide range of community plugins:

    - Docker support via `openmediavault-compose` or `omv-extras`
    - Media servers (e.g., Plex, Jellyfin)
    - Backup tools (e.g., rsync, USB backup)
    - Cloud sync (e.g., Rclone)

    Install plugins through the web interface after enabling OMV-Extras.

=== "View logs"

    ```sh
    journalctl -u openmediavault-engined
    tail -f /var/log/syslog
    ```

<!--- footer STOP from tools/include/markdown/OMV001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_omv install` |
| OpenMediaVault remove | `armbian-config --api module_omv remove` |
| Status | `armbian-config --api module_omv status` |
| Help | `armbian-config --api module_omv help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
