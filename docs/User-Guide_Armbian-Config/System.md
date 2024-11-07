# System wide and admin settings


***

## Enable Armbian firmware upgrades
This will enable Armbian kernel upgrades that are currently put on hold.

**Command:** 
~~~
armbian-config --cmd SY001
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Disable Armbian kernel upgrades
Disable Armbian kernel/firmware upgrades

**Command:** 
~~~
armbian-config --cmd SY002
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Edit the boot environment
This will open /boot/armbianEnv.txt file to edit
CTRL+S to save
CTLR+X to exit
would you like to continue?

**Command:** 
~~~
armbian-config --cmd SY003
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Install Linux headers
**Command:** 
~~~
armbian-config --cmd SY004
~~~

**Author:** @Tearran

**Status:** Preview



***

## Remove Linux headers
**Command:** 
~~~
armbian-config --cmd SY005
~~~

**Author:** @Tearran

**Status:** Preview



***

## Install to internal storage
**Command:** 
~~~
armbian-config --cmd SY006
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

## Manage SSH login options


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

## Change shell system wide to BASH
This will switch system wide shell to BASH

**Command:** 
~~~
armbian-config --cmd SY008
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Change shell system wide to ZSH
This will switch system wide shell to ZSH

**Command:** 
~~~
armbian-config --cmd SY009
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Switch to rolling release
This will switch OS to rolling releases.

**Command:** 
~~~
armbian-config --cmd SY010
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Switch to stable release
This will switch OS to stable releases

**Command:** 
~~~
armbian-config --cmd SY011
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Enable read only filesystem
This will enable Armbian read-only filesystem. Reboot is mandatory?


**Command:** 
~~~
armbian-config --cmd SY012
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Disable read only filesystem
This will disable Armbian read-only filesystem. Reboot is mandatory?


**Command:** 
~~~
armbian-config --cmd SY013
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Adjust welcome screen (motd)
**Command:** 
~~~
armbian-config --cmd SY014
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Install alternative kernels
Switching between kernels might change functionality of your device. 

It might fail to boot!

**Command:** 
~~~
armbian-config --cmd SY015
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Manage device tree overlays
**Command:** 
~~~
armbian-config --cmd SY017
~~~

**Author:** @viraniac @igorpecovnik

**Status:** Stable



***

