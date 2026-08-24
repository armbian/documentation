---
title: "Code-server"
description: "Install and run Code-server on Armbian — Code-server VS Code in browser. Runs on ARM64 and x86 single-board computers."
image: /images/COD001.png
category: "DevTools"
comments: true
---
# Code-server


<!--- section image START from tools/include/images/COD001.png --->
![Code-server](/images/COD001.png){ .app-logo }
<!--- section image STOP from tools/include/images/COD001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/linuxserver/docker-code-server) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8443`


<!--- header START from tools/include/markdown/COD001-header.md --->
Code-server is VS Code running on a remote server, accessible through the browser. This brings the full power of Visual Studio Code to any device with a web browser, eliminating the need for local installations while maintaining a consistent development environment across all your devices.

Built on the [VS Code](https://code.visualstudio.com/) open-source base, code-server provides enterprise-grade remote development capabilities with the familiar VS Code interface. It's maintained by [LinuxServer.io](https://www.linuxserver.io/) and optimized for containerized deployments, making it perfect for development on ARM devices, cloud servers, or homelab environments.

*Key Features*

- **Full VS Code Experience**: Complete access to the VS Code extension marketplace, themes, and settings
- **Browser-Based Access**: Development environment available from Chrome, Firefox, Safari, or Edge
- **Resource Efficiency**: Offload compilation and development tasks to more powerful servers
- **Persistent Workspaces**: All settings, extensions, and files saved across sessions
- **Multi-User Support**: Each container provides an isolated development environment
- **SSH Integration**: Built-in terminal for direct server access and command-line operations
- **Extension Marketplace**: Install thousands of VS Code extensions for any language or framework
- **Cross-Platform**: Develop from Windows, Mac, Linux, iOS, or Android devices

---

Perfect for developers working on **ARM-based SBCs**, **cloud instances**, or **homelab servers** who need a consistent, powerful development environment accessible from anywhere.

<!--- header STOP from tools/include/markdown/COD001-header.md --->


Install from **[armbian-config](/config/) → Software → Dev Tools → Code-server**

~~~ custombash title="CLI install"
armbian-config --cmd COD001
~~~


<!--- footer START from tools/include/markdown/COD001-footer.md --->
=== "Access to the web interface"

    - Default Login: No password required by default (see optional variables below)

    **Note**: Code-server uses HTTPS with a self-signed certificate by default. Your browser may show a security warning - this is normal for self-signed certificates.

=== "Directories"

    - Install directory: `/armbian/code-server`
    - Configuration directory: `/armbian/code-server/config`

=== "Optional Environment Variables"

    You can customize code-server by passing additional environment variables:

    - **PASSWORD** - Set a simple password for web UI access (not recommended for production)
    - **HASHED_PASSWORD** - Set a hashed password for enhanced security (recommended)
    - **SUDO_PASSWORD** - Set a password for sudo access within code-server terminal
    - **PROXY_DOMAIN** - Configure proxy domain for reverse proxy setups
    - **DEFAULT_WORKSPACE** - Set the default workspace directory
    - **PWA_APPNAME** - Customize the PWA (Progressive Web App) name

    To add these variables, edit the container and restart:

    ```sh
    docker stop code-server
    docker rm code-server
    # Then reinstall with modified environment variables
    ```

=== "View logs"

    ```sh
    docker logs -f code-server
    ```

=== "Password hashing"

    To generate a hashed password for the HASHED_PASSWORD variable:

    ```sh
    docker run -it --rm lscr.io/linuxserver/code-server:latest hash_password
    ```

=== "Troubleshooting"

    - **Browser shows certificate warning**: Accept the security warning to proceed (self-signed certificate)
    - **Cannot access web UI**: Check if port 8443 is open in your firewall
    - **Extensions not installing**: Check internet connectivity from the container
    - **Slow performance**: Consider increasing Docker resource limits

<!--- footer STOP from tools/include/markdown/COD001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_code-server install` |
| Code-server remove | `armbian-config --api module_code-server remove` |
| Code-server purge with data folder | `armbian-config --api module_code-server purge` |
| Status | `armbian-config --api module_code-server status` |
| Help | `armbian-config --api module_code-server help` |

---

_Part of Armbian's [Applications and tools for development](/User-Guide_Armbian-Software/DevTools/) software._
