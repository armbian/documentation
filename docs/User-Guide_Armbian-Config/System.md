---
comments: true
---

# System wide and admin settings

## Alternative kernels, headers, rolling updates, overlays

### Install alternative kernels

**Status:** Stable

**Author:** @igorpecovnik


~~~ bash title="Install alternative kernels:"
armbian-config --cmd KER001
~~~

### Install Linux headers


~~~ bash title="Install Linux headers:"
armbian-config --cmd KER002
~~~

### Remove Linux headers


~~~ bash title="Remove Linux headers:"
armbian-config --cmd KER003
~~~

### Manage device tree overlays


~~~ bash title="Manage device tree overlays:"
armbian-config --cmd KER004
~~~

### Select Odroid board configuration


~~~ bash title="Select Odroid board configuration:"
armbian-config --cmd KER005
~~~

### Edit the boot environment


~~~ bash title="Edit the boot environment:"
armbian-config --cmd KER006
~~~

## Install to internal media, ZFS, NFS, read-only rootfs

### Install to internal storage

**Status:** Preview

**Author:** @igorpecovnik


~~~ bash title="Install to internal storage:"
armbian-config --cmd STOR001
~~~

### ZFS filesystem - enable support


~~~ bash title="ZFS filesystem - enable support:"
armbian-config --cmd STOR002
~~~

### ZFS filesystem - remove support


~~~ bash title="ZFS filesystem - remove support:"
armbian-config --cmd STOR003
~~~

### Enable read only filesystem


~~~ bash title="Enable read only filesystem:"
armbian-config --cmd STOR004
~~~

### Disable read only filesystem


~~~ bash title="Disable read only filesystem:"
armbian-config --cmd STOR005
~~~

### Enable Network filesystem (NFS) support


~~~ bash title="Enable Network filesystem (NFS) support:"
armbian-config --cmd NETFS01
~~~

### Disable Network filesystem (NFS) support


~~~ bash title="Disable Network filesystem (NFS) support:"
armbian-config --cmd NETFS02
~~~

### Manage NFS Server

#### Enable network filesystem (NFS) daemon

**Status:** Stable

**Author:** @igorpecovnik


~~~ bash title="Enable network filesystem (NFS) daemon:"
armbian-config --cmd NETFS04
~~~

#### Configure network filesystem (NFS) daemon


~~~ bash title="Configure network filesystem (NFS) daemon:"
armbian-config --cmd NETFS05
~~~

#### Remove network filesystem (NFS) daemon


~~~ bash title="Remove network filesystem (NFS) daemon:"
armbian-config --cmd NETFS06
~~~

#### Show network filesystem (NFS) daemon clients


~~~ bash title="Show network filesystem (NFS) daemon clients:"
armbian-config --cmd NETFS07
~~~

### Manage NFS Client

#### Find NFS servers in subnet and mount shares

**Status:** Stable

**Author:** @igorpecovnik


~~~ bash title="Find NFS servers in subnet and mount shares:"
armbian-config --cmd NETFS09
~~~

#### Show and manage NFS mounts


~~~ bash title="Show and manage NFS mounts:"
armbian-config --cmd NETFS10
~~~

## Manage SSH daemon options, enable 2FA

### Disable root login

**Status:** Stable

**Author:** @igorpecovnik


~~~ bash title="Disable root login:"
armbian-config --cmd ACC001
~~~


~~~ bash title="Disable root login:"
armbian-config --cmd ACC001
~~~

### Enable root login


~~~ bash title="Enable root login:"
armbian-config --cmd ACC002
~~~


~~~ bash title="Enable root login:"
armbian-config --cmd ACC002
~~~

### Disable password login


~~~ bash title="Disable password login:"
armbian-config --cmd ACC003
~~~


~~~ bash title="Disable password login:"
armbian-config --cmd ACC003
~~~

### Enable password login


~~~ bash title="Enable password login:"
armbian-config --cmd ACC004
~~~


~~~ bash title="Enable password login:"
armbian-config --cmd ACC004
~~~

### Disable Public key authentication login


~~~ bash title="Disable Public key authentication login:"
armbian-config --cmd ACC005
~~~


~~~ bash title="Disable Public key authentication login:"
armbian-config --cmd ACC005
~~~

### Enable Public key authentication login


~~~ bash title="Enable Public key authentication login:"
armbian-config --cmd ACC006
~~~


~~~ bash title="Enable Public key authentication login:"
armbian-config --cmd ACC006
~~~

### Disable OTP authentication


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

### Enable OTP authentication


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

### Generate new OTP authentication QR code


~~~ bash title="Generate new OTP authentication QR code:"
armbian-config --cmd ACC009
~~~

### Show OTP authentication QR code


~~~ bash title="Show OTP authentication QR code:"
armbian-config --cmd ACC010
~~~

### Disable last login banner


~~~ bash title="Disable last login banner:"
armbian-config --cmd ACC011
~~~


~~~ bash title="Disable last login banner:"
armbian-config --cmd ACC011
~~~

### Enable last login banner


~~~ bash title="Enable last login banner:"
armbian-config --cmd ACC012
~~~


~~~ bash title="Enable last login banner:"
armbian-config --cmd ACC012
~~~

### Sandboxed & containerised SSH server


~~~ bash title="Sandboxed & containerised SSH server:"
armbian-config --cmd ACC013
~~~

### Remove sandboxed SSH server


~~~ bash title="Remove sandboxed SSH server:"
armbian-config --cmd ACC014
~~~

### Purge sandboxed SSH server with data folder


~~~ bash title="Purge sandboxed SSH server with data folder:"
armbian-config --cmd ACC015
~~~

## Change shell, adjust MOTD

### Change shell system wide to BASH

**Status:** Stable

**Author:** @igorpecovnik


~~~ bash title="Change shell system wide to BASH:"
armbian-config --cmd USR001
~~~

### Change shell system wide to ZSH


~~~ bash title="Change shell system wide to ZSH:"
armbian-config --cmd USR002
~~~

### Adjust welcome screen (motd)


~~~ bash title="Adjust welcome screen (motd):"
armbian-config --cmd USR003
~~~

## OS updates and distribution upgrades

### Enable Armbian firmware upgrades

**Status:** Stable

**Author:** @igorpecovnik


~~~ bash title="Enable Armbian firmware upgrades:"
armbian-config --cmd UPD001
~~~

### Disable Armbian kernel upgrades


~~~ bash title="Disable Armbian kernel upgrades:"
armbian-config --cmd UPD002
~~~

### Switch system to rolling packages repository


~~~ bash title="Switch system to rolling packages repository:"
armbian-config --cmd UPD003
~~~

### Switch system to stable packages repository


~~~ bash title="Switch system to stable packages repository:"
armbian-config --cmd UPD004
~~~

### Enable automating Docker container base images updating


~~~ bash title="Enable automating Docker container base images updating:"
armbian-config --cmd UPD007
~~~

### Disable automating Docker container base images updating


~~~ bash title="Disable automating Docker container base images updating:"
armbian-config --cmd UPD008
~~~

### Enable automatic package updates.


~~~ bash title="Enable automatic package updates.:"
armbian-config --cmd UPD009
~~~

### Configure automatic package updates


~~~ bash title="Configure automatic package updates:"
armbian-config --cmd UPD010
~~~

### Disable automatic package updates


~~~ bash title="Disable automatic package updates:"
armbian-config --cmd UPD011
~~~
