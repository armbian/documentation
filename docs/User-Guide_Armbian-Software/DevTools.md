---
comments: true
---

# Applications and tools for development

## Git CLI


Install tools for cloning and managing repositories (git)

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/GIT001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/GIT001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd GIT001
~~~


~~~ bash title="Remove tools for cloning and managing repositories (git):"
armbian-config --cmd GIT002
~~~



## Code-server


Code-server VS Code in browser


<!--- section image START from tools/include/images/COD001.png --->
[![Code-server](/images/COD001.png)](#)
<!--- section image STOP from tools/include/images/COD001.png --->


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

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/COD001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/COD001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/linuxserver/docker-code-server)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd COD001
~~~


<!--- footer START from tools/include/markdown/COD001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8443**:

    - URL: `https://<your.IP>:8443`
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


~~~ bash title="Code-server remove:"
armbian-config --cmd COD002
~~~


~~~ bash title="Code-server purge with data folder:"
armbian-config --cmd COD003
~~~



