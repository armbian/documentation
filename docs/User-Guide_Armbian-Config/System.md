# System wide and admin settings


***

## Alternative kernels, headers, rolling updates, overlays


***

### Install alternative kernels

<!--- section image START from tools/include/images/SY201.png --->
[![Install alternative kernels](/images/SY201.png)](#)
<!--- section image STOP from tools/include/images/SY201.png --->


<!--- header START from tools/include/markdown/SY201-header.md --->
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

<!--- header STOP from tools/include/markdown/SY201-header.md --->

Switching between kernels might change functionality of your device. 

It might fail to boot!

**Command:** 
~~~
armbian-config --cmd SY201
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Install Linux headers

<!--- section image START from tools/include/images/SY204.png --->
[![Install Linux headers](/images/SY204.png)](#)
<!--- section image STOP from tools/include/images/SY204.png --->


<!--- header START from tools/include/markdown/SY204-header.md --->
Linux headers are essential for compiling kernel modules and ensuring compatibility with software that interacts with the kernel.

<!--- header STOP from tools/include/markdown/SY204-header.md --->

**Command:** 
~~~
armbian-config --cmd SY204
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Remove Linux headers
**Command:** 
~~~
armbian-config --cmd SY205
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Manage device tree overlays

<!--- section image START from tools/include/images/SY210.png --->
[![Manage device tree overlays](/images/SY210.png)](#)
<!--- section image STOP from tools/include/images/SY210.png --->

**Command:** 
~~~
armbian-config --cmd SY210
~~~

**Author:** @viraniac @igorpecovnik

**Status:** Stable



***

### Select Odroid board configuration
**Command:** 
~~~
armbian-config --cmd SY300
~~~

**Author:** 

**Status:** Preview



***

### Edit the boot environment

<!--- section image START from tools/include/images/SY010.png --->
[![Edit the boot environment](/images/SY010.png)](#)
<!--- section image STOP from tools/include/images/SY010.png --->

This will open /boot/armbianEnv.txt file to edit
CTRL+S to save
CTLR+X to exit
would you like to continue?

**Command:** 
~~~
armbian-config --cmd SY010
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Install to internal media, ZFS, NFS, read-only rootfs


***

### Install to internal storage

<!--- section image START from tools/include/images/SY001.png --->
[![Install to internal storage](/images/SY001.png)](#)
<!--- section image STOP from tools/include/images/SY001.png --->

**Command:** 
~~~
armbian-config --cmd SY001
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

### ZFS filesystem - enable support

<!--- header START from tools/include/markdown/SY220-header.md --->
# 📌 ZFS (Zettabyte File System)  

## 🔍 Overview  

**ZFS (Zettabyte File System)** is a high-performance, scalable, and robust file system designed to provide advanced data protection, integrity, and storage management. Developed by Sun Microsystems, ZFS is widely used in enterprise environments, NAS systems, and personal storage solutions due to its unique features.  

## 🛠️ Key Features  

### ✅ Data Integrity  
- **Copy-on-Write (CoW):** Prevents data corruption by never overwriting live data.  
- **Checksumming:** Detects and corrects silent data corruption (bit rot).  

### 📦 Storage Management  
- **Pooled Storage:** Eliminates the need for traditional partitions; all storage is managed dynamically.  
- **Snapshots & Clones:** Creates instant backups without using extra storage.  

### 🚀 Performance & Scalability  
- **Efficient Compression & Deduplication:** Reduces storage usage without performance loss.  
- **Dynamic Striping & Caching:** Distributes data across multiple disks for optimized read/write speeds.  

### 🔐 Advanced Security  
- **Native Encryption:** Supports dataset-level encryption for secure data storage.  
- **RAID-Z:** A superior RAID alternative that prevents write-hole issues.  
<!--- header STOP from tools/include/markdown/SY220-header.md --->

**Command:** 
~~~
armbian-config --cmd SY220
~~~

**Author:** @armbian

**Status:** Stable



***

### ZFS filesystem - remove support
**Command:** 
~~~
armbian-config --cmd SY221
~~~

**Author:** @armbian

**Status:** Stable



***

### Enable read only filesystem
**Command:** 
~~~
armbian-config --cmd SY007
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Disable read only filesystem
**Command:** 
~~~
armbian-config --cmd SY008
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Enable Network filesystem (NFS) support
**Command:** 
~~~
armbian-config --cmd NFS01
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Disable Network filesystem (NFS) support
**Command:** 
~~~
armbian-config --cmd NFS02
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Manage NFS Server


***

#### Enable network filesystem (NFS) daemon
**Command:** 
~~~
armbian-config --cmd NFS06
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Configure network filesystem (NFS) daemon
**Command:** 
~~~
armbian-config --cmd NFS07
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Remove network filesystem (NFS) daemon
**Command:** 
~~~
armbian-config --cmd NFS08
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Show network filesystem (NFS) daemon clients
**Command:** 
~~~
armbian-config --cmd NFS09
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Manage NFS Client


***

#### Find NFS servers in subnet and mount shares
**Command:** 
~~~
armbian-config --cmd NFS21
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

#### Show and manage NFS mounts
**Command:** 
~~~
armbian-config --cmd NFS22
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Manage SSH daemon options, enable 2FA


***

### Disable root login

<!--- section image START from tools/include/images/SY101.png --->
[![Disable root login](/images/SY101.png)](#)
<!--- section image STOP from tools/include/images/SY101.png --->

**Command:** 
~~~
armbian-config --cmd SY101
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Enable root login
**Command:** 
~~~
armbian-config --cmd SY102
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Disable password login
**Command:** 
~~~
armbian-config --cmd SY103
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Enable password login
**Command:** 
~~~
armbian-config --cmd SY104
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Disable Public key authentication login
**Command:** 
~~~
armbian-config --cmd SY105
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Enable Public key authentication login
**Command:** 
~~~
armbian-config --cmd SY106
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Disable OTP authentication
**Command:** 
~~~
armbian-config --cmd SY107
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Enable OTP authentication
**Command:** 
~~~
armbian-config --cmd SY108
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Generate new OTP authentication QR code
**Command:** 
~~~
armbian-config --cmd SY109
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Show OTP authentication QR code
**Command:** 
~~~
armbian-config --cmd SY110
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Disable last login banner
**Command:** 
~~~
armbian-config --cmd SY111
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Enable last login banner
**Command:** 
~~~
armbian-config --cmd SY112
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Sandboxed & containerised SSH server

<!--- section image START from tools/include/images/SSH200.png --->
[![Sandboxed & containerised SSH server](/images/SSH200.png)](#)
<!--- section image STOP from tools/include/images/SSH200.png --->


<!--- header START from tools/include/markdown/SSH200-header.md --->
Sandboxed & containerised SSH server allows ssh access without giving keys to the entire server. Giving ssh access via private key often means giving full access to the server. This container creates a limited and sandboxed environment that others can ssh into. The users only have access to the folders mapped and the processes running inside this container.
<!--- header STOP from tools/include/markdown/SSH200-header.md --->

This operation will install SSH server.

**Command:** 
~~~
armbian-config --cmd SSH200
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/SSH200-footer.md --->
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

<!--- footer STOP from tools/include/markdown/SSH200-footer.md --->



***

### Remove sandboxed SSH server
This operation will remove SSH server.

**Command:** 
~~~
armbian-config --cmd SSH201
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Purge sandboxed SSH server with data folder
This operation will purge SSH server with data folder.

**Command:** 
~~~
armbian-config --cmd SSH202
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Change shell, adjust MOTD


***

### Change shell system wide to BASH

<!--- section image START from tools/include/images/SY005.png --->
[![Change shell system wide to BASH](/images/SY005.png)](#)
<!--- section image STOP from tools/include/images/SY005.png --->

This will switch system wide shell to BASH

**Command:** 
~~~
armbian-config --cmd SY005
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Change shell system wide to ZSH

<!--- header START from tools/include/markdown/SY006-header.md --->
**ZSH (Z Shell)** is an extended and highly customizable Unix shell that offers powerful features beyond traditional shells like **Bash**. It is widely used for its user-friendly enhancements, scripting capabilities, and plugin support.  

## 🚀 Key Features  

- **Auto-suggestions & Syntax Highlighting** ✨  
- **Powerful Tab Completion & Globbing** 🔍  
- **Customizable Prompt (e.g., with Oh My Zsh)** 🎨  
- **Shared Command History Across Sessions** 📜  
- **Built-in Spelling Correction** 🛠️  
<!--- header STOP from tools/include/markdown/SY006-header.md --->

This will switch system wide shell to ZSH

**Command:** 
~~~
armbian-config --cmd SY006
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Adjust welcome screen (motd)
**Command:** 
~~~
armbian-config --cmd SY009
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## OS updates and distribution upgrades
**Status:** Active



***

### Enable Armbian firmware upgrades

<!--- section image START from tools/include/images/SY202.png --->
[![Enable Armbian firmware upgrades](/images/SY202.png)](#)
<!--- section image STOP from tools/include/images/SY202.png --->

This will enable Armbian kernel upgrades that are currently put on hold.

**Command:** 
~~~
armbian-config --cmd SY202
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Disable Armbian kernel upgrades
Disable Armbian kernel/firmware upgrades

**Command:** 
~~~
armbian-config --cmd SY203
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Switch system to rolling packages repository
This will switch OS to rolling releases.

**Command:** 
~~~
armbian-config --cmd SY206
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Switch system to stable packages repository
This will switch OS to stable releases

**Command:** 
~~~
armbian-config --cmd SY207
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Enable automating Docker container base images updating

<!--- section image START from tools/include/images/WTC001.png --->
[![Enable automating Docker container base images updating](/images/WTC001.png)](#)
<!--- section image STOP from tools/include/images/WTC001.png --->


<!--- header START from tools/include/markdown/WTC001-header.md --->
Watchtower is an application that will monitor your running Docker containers and watch for changes to the images that those containers were originally started from. If watchtower detects that an image has changed, it will automatically restart the container using the new image.

<!--- header STOP from tools/include/markdown/WTC001-header.md --->

**Command:** 
~~~
armbian-config --cmd WTC001
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/WTC001-footer.md --->
Every day watchtower will pull the latest images and compare it to the one that was used to run the certain container. If it sees that the image has changed it will stop/remove containers and then restart it using the new image and the same docker run options that were used to start the container initially.

<!--- footer STOP from tools/include/markdown/WTC001-footer.md --->



***

### Disable automating Docker container base images updating
**Command:** 
~~~
armbian-config --cmd WTC002
~~~

**Author:** @armbian

**Status:** Stable



***

### Enable automatic package updates.
**Command:** 
~~~
armbian-config --cmd UNAT01
~~~

**Author:** @armbian

**Status:** Stable



***

### Configure automatic package updates

<!--- section image START from tools/include/images/UNAT02.png --->
[![Configure automatic package updates](/images/UNAT02.png)](#)
<!--- section image STOP from tools/include/images/UNAT02.png --->

**Command:** 
~~~
armbian-config --cmd UNAT02
~~~

**Author:** @armbian

**Status:** Stable



***

### Disable automatic package updates
**Command:** 
~~~
armbian-config --cmd UNAT03
~~~

**Author:** @armbian

**Status:** Stable



***

