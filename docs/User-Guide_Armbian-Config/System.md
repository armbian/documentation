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


~~~ bash title="Install alternative kernels:"
armbian-config --cmd KER001
~~~


~~~ bash title="Install Linux headers:"
armbian-config --cmd KER002
~~~


~~~ bash title="Remove Linux headers:"
armbian-config --cmd KER003
~~~


~~~ bash title="Manage device tree overlays:"
armbian-config --cmd KER004
~~~


~~~ bash title="Select Odroid board configuration:"
armbian-config --cmd KER005
~~~


~~~ bash title="Edit the boot environment:"
armbian-config --cmd KER006
~~~

## Install to internal media, ZFS, NFS, read-only rootfs

## Install to internal storage

**Author:** @igorpecovnik

**Status:** Preview


<!--- section image START from tools/include/images/STOR001.png --->
[![Install to internal storage](/images/STOR001.png)](#)
<!--- section image STOP from tools/include/images/STOR001.png --->


~~~ bash title="Install to internal storage:"
armbian-config --cmd STOR001
~~~


~~~ bash title="ZFS filesystem - enable support:"
armbian-config --cmd STOR002
~~~


~~~ bash title="ZFS filesystem - remove support:"
armbian-config --cmd STOR003
~~~


~~~ bash title="Enable read only filesystem:"
armbian-config --cmd STOR004
~~~


~~~ bash title="Disable read only filesystem:"
armbian-config --cmd STOR005
~~~

## Enable Network filesystem (NFS) support

**Author:** @igorpecovnik

**Status:** Stable


~~~ bash title="Enable Network filesystem (NFS) support:"
armbian-config --cmd NETFS01
~~~


~~~ bash title="Disable Network filesystem (NFS) support:"
armbian-config --cmd NETFS02
~~~

## Enable network filesystem (NFS) daemon

**Author:** @igorpecovnik

**Status:** Stable


~~~ bash title="Enable network filesystem (NFS) daemon:"
armbian-config --cmd NETFS04
~~~


~~~ bash title="Configure network filesystem (NFS) daemon:"
armbian-config --cmd NETFS05
~~~


~~~ bash title="Remove network filesystem (NFS) daemon:"
armbian-config --cmd NETFS06
~~~


~~~ bash title="Show network filesystem (NFS) daemon clients:"
armbian-config --cmd NETFS07
~~~

## Find NFS servers in subnet and mount shares

**Author:** @igorpecovnik

**Status:** Stable


~~~ bash title="Find NFS servers in subnet and mount shares:"
armbian-config --cmd NETFS09
~~~


~~~ bash title="Show and manage NFS mounts:"
armbian-config --cmd NETFS10
~~~

## Manage SSH daemon options, enable 2FA

## Disable root login

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/ACC001.png --->
[![Disable root login](/images/ACC001.png)](#)
<!--- section image STOP from tools/include/images/ACC001.png --->


~~~ bash title="Disable root login:"
armbian-config --cmd ACC001
~~~


~~~ bash title="Disable root login:"
armbian-config --cmd ACC001
~~~


~~~ bash title="Enable root login:"
armbian-config --cmd ACC002
~~~


~~~ bash title="Enable root login:"
armbian-config --cmd ACC002
~~~


~~~ bash title="Disable password login:"
armbian-config --cmd ACC003
~~~


~~~ bash title="Disable password login:"
armbian-config --cmd ACC003
~~~


~~~ bash title="Enable password login:"
armbian-config --cmd ACC004
~~~


~~~ bash title="Enable password login:"
armbian-config --cmd ACC004
~~~


~~~ bash title="Disable Public key authentication login:"
armbian-config --cmd ACC005
~~~


~~~ bash title="Disable Public key authentication login:"
armbian-config --cmd ACC005
~~~


~~~ bash title="Enable Public key authentication login:"
armbian-config --cmd ACC006
~~~


~~~ bash title="Enable Public key authentication login:"
armbian-config --cmd ACC006
~~~


~~~ bash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ bash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ bash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ bash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ bash title="Disable OTP authentication:"
armbian-config --cmd ACC007
~~~


~~~ bash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ bash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ bash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ bash title="Enable OTP authentication:"
armbian-config --cmd ACC008
~~~


~~~ bash title="Enable OTP authentication:"
armbian-config --cmd ACC008
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


~~~ bash title="Disable last login banner:"
armbian-config --cmd ACC011
~~~


~~~ bash title="Enable last login banner:"
armbian-config --cmd ACC012
~~~


~~~ bash title="Enable last login banner:"
armbian-config --cmd ACC012
~~~


~~~ bash title="Sandboxed & containerised SSH server:"
armbian-config --cmd ACC013
~~~


~~~ bash title="Remove sandboxed SSH server:"
armbian-config --cmd ACC014
~~~


~~~ bash title="Purge sandboxed SSH server with data folder:"
armbian-config --cmd ACC015
~~~

## Change shell, adjust MOTD

## Change shell system wide to BASH

**Author:** @igorpecovnik

**Status:** Stable


<!--- section image START from tools/include/images/USR001.png --->
[![Change shell system wide to BASH](/images/USR001.png)](#)
<!--- section image STOP from tools/include/images/USR001.png --->


~~~ bash title="Change shell system wide to BASH:"
armbian-config --cmd USR001
~~~


~~~ bash title="Change shell system wide to ZSH:"
armbian-config --cmd USR002
~~~


~~~ bash title="Adjust welcome screen (motd):"
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


~~~ bash title="Enable Armbian firmware upgrades:"
armbian-config --cmd UPD001
~~~


~~~ bash title="Disable Armbian kernel upgrades:"
armbian-config --cmd UPD002
~~~


~~~ bash title="Switch system to rolling packages repository:"
armbian-config --cmd UPD003
~~~


~~~ bash title="Switch system to stable packages repository:"
armbian-config --cmd UPD004
~~~


~~~ bash title="Enable automating Docker container base images updating:"
armbian-config --cmd UPD007
~~~


~~~ bash title="Disable automating Docker container base images updating:"
armbian-config --cmd UPD008
~~~


~~~ bash title="Enable automatic package updates.:"
armbian-config --cmd UPD009
~~~


~~~ bash title="Configure automatic package updates:"
armbian-config --cmd UPD010
~~~


~~~ bash title="Disable automatic package updates:"
armbian-config --cmd UPD011
~~~
