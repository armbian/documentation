---
comments: true
---

# System wide and admin settings

## Alternative kernels, headers, rolling updates, overlays

## Install alternative kernels

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/KER001.png --->
[![Install alternative kernels](/images/KER001.png)](#)
<!--- section image STOP from tools/include/images/KER001.png --->


<!--- header START from tools/include/markdown/KER001-header.md --->
## Kernel Switching Warning

Switching between different kernel versions can significantly impact the functionality of your device. A newer or older kernel may introduce changes to hardware compatibility, drivers, and system stability. Some features may stop working, while others may improve or be reintroduced.  

### ⚠️ Important Warning: Kernel changes carry inherent risks!  
- A mismatched or incompatible kernel may result in **boot failures**, rendering the system unresponsive.  
- Certain peripherals or hardware components (e.g., Wi-Fi, GPU acceleration, or power management) may no longer function correctly.  
- Custom configurations or third-party modules might need to be recompiled or adjusted to work with the new kernel.  

### ✅ Precautions Before Switching Kernels  
Before switching kernels, it is **strongly recommended** to:  
1. **Back up your system** to prevent data loss.  
2. **Verify compatibility** of your hardware and essential drivers with the target kernel version.  
3. **Keep a rescue method available**, such as a bootable SD card / USB drive or serial console access, to recover the system if necessary.  

### 🛠️ Recovery Steps if Boot Fails  
If your device fails to boot after a kernel change, you may need to:  
- **Revert to a previous working kernel** using recovery options.  
- **Use a serial console or debug mode** to diagnose the issue.  
- **Reinstall the system** if no recovery options are available.  

**⚡ Exercise caution when switching kernels, especially on production systems or devices with limited recovery options.**

<!--- header STOP from tools/include/markdown/KER001-header.md --->


~~~ custombash title="Install alternative kernels:"
armbian-config --cmd KER001
~~~


~~~ custombash title="Install Linux headers:"
armbian-config --cmd KER002
~~~


~~~ custombash title="Remove Linux headers:"
armbian-config --cmd KER003
~~~


~~~ custombash title="Manage device tree overlays:"
armbian-config --cmd KER004
~~~


~~~ custombash title="Select Odroid board configuration:"
armbian-config --cmd KER005
~~~


~~~ custombash title="Edit the boot environment:"
armbian-config --cmd KER006
~~~

## Install to internal media, ZFS, NFS, read-only rootfs

## Install to internal storage

**Author:** @igorpecovnik

**Status:** Preview


<!--- section image START from tools/include/images/STOR001.png --->
[![Install to internal storage](/images/STOR001.png)](#)
<!--- section image STOP from tools/include/images/STOR001.png --->


~~~ custombash title="Install to internal storage:"
armbian-config --cmd STOR001
~~~


~~~ custombash title="ZFS filesystem - enable support:"
armbian-config --cmd STOR002
~~~


~~~ custombash title="ZFS filesystem - remove support:"
armbian-config --cmd STOR003
~~~


~~~ custombash title="Enable read only filesystem:"
armbian-config --cmd STOR004
~~~


~~~ custombash title="Disable read only filesystem:"
armbian-config --cmd STOR005
~~~

## Enable Network filesystem (NFS) support

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash title="Enable Network filesystem (NFS) support:"
armbian-config --cmd NETFS01
~~~


~~~ custombash title="Disable Network filesystem (NFS) support:"
armbian-config --cmd NETFS02
~~~

## Enable network filesystem (NFS) daemon

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash title="Enable network filesystem (NFS) daemon:"
armbian-config --cmd NETFS04
~~~


~~~ custombash title="Configure network filesystem (NFS) daemon:"
armbian-config --cmd NETFS05
~~~


~~~ custombash title="Remove network filesystem (NFS) daemon:"
armbian-config --cmd NETFS06
~~~


~~~ custombash title="Show network filesystem (NFS) daemon clients:"
armbian-config --cmd NETFS07
~~~

## Find NFS servers in subnet and mount shares

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash title="Find NFS servers in subnet and mount shares:"
armbian-config --cmd NETFS09
~~~


~~~ custombash title="Show and manage NFS mounts:"
armbian-config --cmd NETFS10
~~~

## Manage SSH daemon options, enable 2FA

## Disable root login

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/ACC001.png --->
[![Disable root login](/images/ACC001.png)](#)
<!--- section image STOP from tools/include/images/ACC001.png --->


~~~ custombash title="Disable root login:"
armbian-config --cmd ACC001
~~~


~~~ custombash title="Disable root login:"
armbian-config --cmd ACC001
~~~


~~~ custombash title="Enable root login:"
armbian-config --cmd ACC002
~~~


~~~ custombash title="Enable root login:"
armbian-config --cmd ACC002
~~~


~~~ custombash title="Disable password login:"
armbian-config --cmd ACC003
~~~


~~~ custombash title="Disable password login:"
armbian-config --cmd ACC003
~~~


~~~ custombash title="Enable password login:"
armbian-config --cmd ACC004
~~~


~~~ custombash title="Enable password login:"
armbian-config --cmd ACC004
~~~


~~~ custombash title="Disable Public key authentication login:"
armbian-config --cmd ACC005
~~~


~~~ custombash title="Disable Public key authentication login:"
armbian-config --cmd ACC005
~~~


~~~ custombash title="Enable Public key authentication login:"
armbian-config --cmd ACC006
~~~


~~~ custombash title="Enable Public key authentication login:"
armbian-config --cmd ACC006
~~~


~~~ custombash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ custombash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ custombash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ custombash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ custombash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ custombash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ custombash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ custombash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ custombash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ custombash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ custombash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ custombash title="Generate new OTP authentication QR code:"
armbian-config --cmd ACC009
~~~


~~~ custombash title="Show OTP authentication QR code:"
armbian-config --cmd ACC010
~~~


~~~ custombash title="Disable last login banner:"
armbian-config --cmd ACC011
~~~


~~~ custombash title="Disable last login banner:"
armbian-config --cmd ACC011
~~~


~~~ custombash title="Enable last login banner:"
armbian-config --cmd ACC012
~~~


~~~ custombash title="Enable last login banner:"
armbian-config --cmd ACC012
~~~


~~~ custombash title="Sandboxed & containerised SSH server:"
armbian-config --cmd ACC013
~~~


<!--- footer START from tools/include/markdown/ACC013-footer.md --->
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

<!--- footer STOP from tools/include/markdown/ACC013-footer.md --->


~~~ custombash title="Remove sandboxed SSH server:"
armbian-config --cmd ACC014
~~~


~~~ custombash title="Purge sandboxed SSH server with data folder:"
armbian-config --cmd ACC015
~~~

## Change shell, adjust MOTD

## Change shell system wide to BASH

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/USR001.png --->
[![Change shell system wide to BASH](/images/USR001.png)](#)
<!--- section image STOP from tools/include/images/USR001.png --->


~~~ custombash title="Change shell system wide to BASH:"
armbian-config --cmd USR001
~~~


~~~ custombash title="Change shell system wide to ZSH:"
armbian-config --cmd USR002
~~~


~~~ custombash title="Adjust welcome screen (motd):"
armbian-config --cmd USR003
~~~

## OS updates and distribution upgrades

**Status:** Active

## Enable Armbian firmware upgrades

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/UPD001.png --->
[![Enable Armbian firmware upgrades](/images/UPD001.png)](#)
<!--- section image STOP from tools/include/images/UPD001.png --->


~~~ custombash title="Enable Armbian firmware upgrades:"
armbian-config --cmd UPD001
~~~


~~~ custombash title="Disable Armbian kernel upgrades:"
armbian-config --cmd UPD002
~~~


~~~ custombash title="Switch system to rolling packages repository:"
armbian-config --cmd UPD003
~~~


~~~ custombash title="Switch system to stable packages repository:"
armbian-config --cmd UPD004
~~~


~~~ custombash title="Enable automating Docker container base images updating:"
armbian-config --cmd UPD007
~~~


<!--- footer START from tools/include/markdown/UPD007-footer.md --->
Every day watchtower will pull the latest images and compare it to the one that was used to run the certain container. If it sees that the image has changed it will stop/remove containers and then restart it using the new image and the same docker run options that were used to start the container initially.

<!--- footer STOP from tools/include/markdown/UPD007-footer.md --->


~~~ custombash title="Disable automating Docker container base images updating:"
armbian-config --cmd UPD008
~~~


~~~ custombash title="Enable automatic package updates.:"
armbian-config --cmd UPD009
~~~


~~~ custombash title="Configure automatic package updates:"
armbian-config --cmd UPD010
~~~


~~~ custombash title="Disable automatic package updates:"
armbian-config --cmd UPD011
~~~
