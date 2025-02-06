# System wide and admin settings


***

## Alternative kernels, headers, rolling updates, overlays


***

### Install alternative kernels
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
**Command:** 
~~~
armbian-config --cmd SY001
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

### ZFS filesystem - enable support
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
This will switch system wide shell to BASH

**Command:** 
~~~
armbian-config --cmd SY005
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Change shell system wide to ZSH
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

