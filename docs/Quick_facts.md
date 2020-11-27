# Quick Facts

## What is Armbian Linux?

Armbian Linux provides optimized Debian and Ubuntu Linux images for ARM-based SBCs. There is an incredible ecosystem of small computing platforms that are powerful alternatives to the Raspberry Pi. Armbian's mission is to provide a uniform system offering that is trustworthy to run on any of the dozens of OS-neglected ARM single board computers.

## Challenges

### Armbian is the opposite of Raspbian

Raspbian has dozens of contributors to focus on a single SBC platform. Armbian has a dozen contributors to focus on 100+ SBCs spread over 30 platforms.

### Balancing Development and Support

Given the point above, resources are thin. Armbian developers have to focus on the core mission of maintaining the [Armbian Build Platform](https://github.com/armbian/build). We heavily rely on other members of the community to support each other.  Although Armbian does provide a lot of [user friendly features](https://github.com/armbian/config), the reality is that Armbian is for more advanced users. If you are really struggling with your SBC, you may want to consider first getting more comfortable with Raspbian Linux on the Raspberry Pi.  

### More SBCs continuously coming to market

SBC and TV Box manufacturers love to design and ship new products. Unfortunately they do not like to spend time on software and instead rely on community projects such as Armbian to fill in the gaps.

## Benefits

### Simple

BASH shell, standard Debian/Ubuntu utilities. Common and specific features can be with minimalistic menu-driven utility. Login is possible via serial, HDMI/VGA or SSH. 

### Light

No bloatware or spyware. Special utilities are completely optional. Suitable for newcomers and professionals. 

### Optimized

A distributed image is compacted to real data size and starts at around of 1G. Size is optimized for SD card usage. Bigger is better. Installing applications later severely reduces the life of your SD card. They were not designed for this type of usage.

### Fast

Boards are optimized on kernel and userspace level. DVFS optimization, memory log caching, browser profile memory caching, swap usage tuning, garbage commit delay. Our system runs almost read-only and is one of the the fastest Linux for many development boards in just about every case.

### Secure

Security level is on a stock Debian/Ubuntu level and can be hardened with the configuration utility. It provides a good starting point for industrial or home usage. The system is regularly inspected by professionals within the community. Each official stable build is thoroughly tested. Images are a direct base for all 3rd party builders.

### Supported

Providing long term updates, security fixes, documentation, user support.

### Smart

Deep understanding how boards work, how operating system work and how hardware should be designed to run better. Involved in board design. Experience in Linux since early 90'. Specialized in ARM development boards since 2013. 

### Open

Open source build script and kernel development, maintenance and distribution for more than [30 different ARM and ARM64 Linux kernels](https://www.armbian.com/kernel/). Powerful build and software development tools. Can run in fully parallel mode. Can run under Docker.
