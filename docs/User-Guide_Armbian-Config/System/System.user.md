# System wide and admin settings


***

## Enable Armbian kernel/firmware upgrades
This will enable Armbian kernel upgrades.

**Command:** 
~~~
armbian-config --cmd S01
~~~

**Author:** 

**Status:** Preview



***

## Disable Armbian kernel upgrades
Disable Armbian kernel/firmware upgrades

**Command:** 
~~~
armbian-config --cmd S02
~~~

**Author:** 

**Status:** Preview



***

## Edit the boot environment
This will open /boot/armbianEnv.txt file to edit
CTRL+S to save
CTLR+X to exit
would you like to continue?

**Command:** 
~~~
armbian-config --cmd S03
~~~

**Author:** 

**Status:** Preview



***

## Install Linux headers
**Command:** 
~~~
armbian-config --cmd S04
~~~

**Author:** @Tearran

**Status:** Preview



***

## Remove Linux headers
**Command:** 
~~~
armbian-config --cmd S05
~~~

**Author:** @Tearran

**Status:** Preview



***

## Install to internal storage
**Command:** 
~~~
armbian-config --cmd S06
~~~

**Author:** https://github.com/igorpecovnik

**Status:** Preview



***

## Manage SSH login options


***

### Disable root login
**Command:** 
~~~
armbian-config --cmd S07
~~~

**Author:** 

**Status:** Preview



***

### Enable root login
**Command:** 
~~~
armbian-config --cmd S08
~~~

**Author:** 

**Status:** Preview



***

### Disable password login
**Command:** 
~~~
armbian-config --cmd S09
~~~

**Author:** 

**Status:** Preview



***

### Enable password login
**Command:** 
~~~
armbian-config --cmd S10
~~~

**Author:** 

**Status:** Preview



***

### Disable Public key authentication login
**Command:** 
~~~
armbian-config --cmd S11
~~~

**Author:** 

**Status:** Preview



***

### Enable Public key authentication login
**Command:** 
~~~
armbian-config --cmd S12
~~~

**Author:** 

**Status:** Preview



***

### Disable OTP authentication
**Command:** 
~~~
armbian-config --cmd S13
~~~

**Author:** 

**Status:** Preview



***

### Enable OTP authentication
**Command:** 
~~~
armbian-config --cmd S14
~~~

**Author:** 

**Status:** Preview



***

### Generate new OTP authentication QR code
**Command:** 
~~~
armbian-config --cmd S15
~~~

**Author:** 

**Status:** Preview



***

### Show OTP authentication QR code
**Command:** 
~~~
armbian-config --cmd S16
~~~

**Author:** Igor Pecovnik

**Status:** Preview



***

### Disable last login banner
**Command:** 
~~~
armbian-config --cmd S30
~~~

**Author:** 

**Status:** Preview



***

### Enable last login banner
**Command:** 
~~~
armbian-config --cmd S31
~~~

**Author:** 

**Status:** Preview



***

## Change shell system wide to BASH
**Command:** 
~~~
armbian-config --cmd S17
~~~

**Author:** https://github.com/igorpecovnik

**Status:** Preview



***

## Change shell system wide to ZSH
**Command:** 
~~~
armbian-config --cmd S18
~~~

**Author:** https://github.com/igorpecovnik

**Status:** Preview



***

## Switch to rolling release
This will switch to rolling releases

would you like to continue?

**Command:** 
~~~
armbian-config --cmd S19
~~~

**Author:** Igor Pecovnik

**Status:** Preview



***

## Switch to stable release
This will switch to stable releases

would you like to continue?

**Command:** 
~~~
armbian-config --cmd S20
~~~

**Author:** Igor Pecovnik

**Status:** Preview



***

## Enable read only filesystem
This will enable Armbian read-only filesystem. Reboot is mandatory?


**Command:** 
~~~
armbian-config --cmd S21
~~~

**Author:** Igor Pecovnik

**Status:** Preview



***

## Disable read only filesystem
This will disable Armbian read-only filesystem. Reboot is mandatory?


**Command:** 
~~~
armbian-config --cmd S22
~~~

**Author:** Igor Pecovnik

**Status:** Preview



***

## Adjust welcome screen (motd)
**Command:** 
~~~
armbian-config --cmd S23
~~~

**Author:** 

**Status:** Preview



***

## Install alternative kernels
Switching between kernels might change functionality of your device. 

It might fail to boot!

**Command:** 
~~~
armbian-config --cmd S24
~~~

**Author:** Igor Pecovnik

**Status:** Preview



***

## Distribution upgrades


***

### Upgrade to latest stable / LTS
Release upgrade is irriversible operation which upgrades all packages. 

Resoulted upgrade might break your build beyond repair!

**Command:** 
~~~
armbian-config --cmd S26
~~~

**Author:** Igor Pecovnik

**Status:** Active



***

### Upgrade to rolling unstable
Release upgrade is irriversible operation which upgrades all packages. 

Resoulted upgrade might break your build beyond repair!

**Command:** 
~~~
armbian-config --cmd S27
~~~

**Author:** Igor Pecovnik

**Status:** Active



***

## Manage device tree overlays
**Command:** 
~~~
armbian-config --cmd S28
~~~

**Author:** Gunjan Gupta

**Status:** Active



***

