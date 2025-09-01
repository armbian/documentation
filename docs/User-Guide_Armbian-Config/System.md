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


~~~ bash title="Remove Linux headers:"
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


## Storage


Install to internal media, ZFS, NFS, read-only rootfs

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/Storage-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/Storage-header.md)  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  
#### Install


<!--- header START from tools/include/markdown/STO001-header.md --->
This section provides an option to transfer the live running Armbian system from an SD card to internal storage devices such as eMMC, SATA, NVMe, or USB drives. It prepares the target storage, copies the active system, adjusts bootloader settings, and ensures the system can boot independently without requiring reinstallation.

<!--- header STOP from tools/include/markdown/STO001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/STO001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/STO001-header.md)  
__Status:__ Preview  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  

~~~ custombash
armbian-config --cmd STO001
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
Long-Term Support (LTS) upgrades provide a **well-tested and stable release** of the underlying Linux distribution (Debian or Ubuntu). These versions receive **security patches and critical bug fixes** for an extended period, making them the recommended choice for production systems and users who prioritize stability over new features.

!!! Note

    While LTS upgrades are considered safe, always back up your data before proceeding with a distribution upgrade.

<!--- header STOP from tools/include/markdown/STD001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/STD001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/STD001-header.md)  
__Status:__ Stable  

~~~ custombash
armbian-config --cmd STD001
~~~


#### Unstable Distro Upgrade


Distribution upgrade to rolling unstable


<!--- header START from tools/include/markdown/UNS001-header.md --->
Testing upgrades track the **latest distribution releases** that are not yet fully stabilized. They include **new features, packages, and improvements**, but may also introduce regressions or breaking changes. This option is best suited for **developers, testers, and enthusiasts** who want early access and are willing to troubleshoot issues. 

!!! Warning

    Testing upgrades may cause system instability. Avoid using this option on production devices. Always back up important data before upgrading.  



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



