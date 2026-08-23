---
title: "Filebrowser"
description: "Install and run Filebrowser on Armbian — Filebrowser provides a web-based file manager accessible via a browser. Runs on ARM64 and x86 single-board computers."
image: /images/FIL001.png
category: "Media"
comments: true
---
# Filebrowser


<!--- section image START from tools/include/images/FIL001.png --->
![Filebrowser](/images/FIL001.png){ .app-logo }
<!--- section image STOP from tools/include/images/FIL001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://filebrowser.org/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8095`


<!--- header START from tools/include/markdown/FIL001-header.md --->
**Filebrowser** is a lightweight, web-based file manager that gives you direct access to your files from any browser. It allows users to upload, delete, preview, rename, and organize files and folders — all through a clean, responsive interface.

**Key Features**

- Modern and intuitive web interface
- User management with role-based access
- File uploads, downloads, sharing, and previews
- Custom branding support
- Configurable directory access
- Runs as a single binary or Docker container

Official site: [https://filebrowser.org](https://filebrowser.org)

<!--- header STOP from tools/include/markdown/FIL001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Media → Filebrowser**

~~~ custombash title="CLI install"
armbian-config --cmd FIL001
~~~


<!--- footer START from tools/include/markdown/FIL001-footer.md --->
=== "Access to the web interface"

    - Username/Password: admin / admin

=== "Directories"

    - Install directory: `/armbian/filebrowser`
    - Root directory: `/armbian/filebrowser/srv`
    - Database directory: `/armbian/filebrowser/database`
    - Configuration file: `/armbian/filebrowser/filebrowser.json`
    - Branding directory: `/armbian/filebrowser/branding`

=== "View logs"

    ```sh
    docker logs -f filebrowser
    ```

<!--- footer STOP from tools/include/markdown/FIL001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_filebrowser install` |
| Filebrowser container remove | `armbian-config --api module_filebrowser remove` |
| Filebrowser container purge with data folder | `armbian-config --api module_filebrowser purge` |
| Status | `armbian-config --api module_filebrowser status` |
| Help | `armbian-config --api module_filebrowser help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
