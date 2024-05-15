# Frequently asked questions

**This information is mainly for new/inexperienced users but could be useful for others too.**

## Is Armbian an operating system?

Not per se.  Armbian is a [build](https://github.com/armbian/build) framework that allows users to create ready-to-use images with working kernels in variable userspace configurations for various single board computers (SBCs).

We do provide various prebuilt images for some boards, but mostly for users convenience.

## Why I cannot simply shove a random image into my board to work like on my PC?

x86 architecture always has a traditional BIOS or UEFI.  This provides a standard framework for operating systems to interact with the hardware.  Most SBCs do not.  ARM is improving the situation with *ARM Server Ready* and *ARM System Ready certificates*, but most SBC vendors are not yet incentivized to meet these standards.

Without such standards, many vendors quickly fork low-level bootloaders such as u-boot and make the bare minimum modifications needed.

[Great reference here](https://bootlin.com/pub/conferences/2017/lca/petazzoni-arm-introduction/petazzoni-arm-introduction.pdf)
	
## Why is Armbian constantly asking for money?  Free software should be free.

Making free licence software also requires best people, expensive infrastructure, tooling.  It has as much or more costs as proprietary while generating no income from the licence.

tl;dr: We are asking for help that developers and project maintainers do not lose their generosity and humanity which are the driving force that generates a value.  For all of us!  A great deal of our work represent a big pressure on our very limited private resources.  We ask you to share that burden with us.

### Development time

We are covering a large swath of diverse, custom designed ARM hardware in ways, extents, and under conditions nobody else does.  Keeping this service up, keeping these low end hardware functional is laborious.  When releases are approaching and a lot of testing and fixing is going on, this gets up, stress intensifies.  This means we have to invest let's say at least 3.000 - 4.000 EUR of our time on top of fixed costs into this service every day just to keep it up.  Without developing any serious features [users wish to have](https://forum.armbian.com/forum/38-feature-requests/).  Fulfilling many of these wishes would easily cost tens of thousands in development time, which we don't have and which we can't get back due to it being free software.  Nobody needs to buy licence for using it, and yet only a few people decide to [respect the time and attention](https://forum.armbian.com/subscriptions/) they are receiving from developers on forums. 

### Infrastructure and operations

We have to maintain our infrastructure where biggest costs are - once again - people's time, followed by electricity, then hardware itself.  Often we get free hardware and very rare break even with electricity costs and with people that would maintain this for us.  A new sponsored board usually brings us more costs then benefits -- since benefit is anyway public.

### Support time

The software is given, released free.  However support, development, and documentation costs time, effort, hardware and technical ability, which incurs costs.

Each question that is directed towards our team is generating opportunity costs and taking away from development time.  Some we are happy to cover, but not all.  Especially when it goes for repetitive questions and demands.

Questions associated with missing features represent another hit and miss for us.  Complicated and critical upstream functions are missing (like video acceleration within a web browser, supporting a board that had very poor initial support and no community backing, etc.).  This functionality is unique to hardware and implementing is extremely labor intensive and requires unique expertise.  Our team is 10-15 volunteers that maintain this project during their own time.  We cannot cover the job of Google Chromium team, Collabora, ARM, Rockchip and other vendors which have not provided sufficient support for their products.

All our work is done in public and we provide all sources which we are changing in the process.  All our work is patent free and released under a free licence so anyone can re-use it further.  The scale of SBCs Armbian supports is hard to beat, and consequently our work is repackaged and reused by other projects and vendors.  Unfortunately the burden of support is often directed to us, while they focus on revenue.

## Why does hardware feature XY work in old kernel but not in more recent one?

Vendors develop hardware specific support on fixed (usually old LTS) kernel and U-Boot fork and only do minimal adjustments to make board features work.  Besides the fact that those adjustments are almost never pushed back to mainline they usually do not update their sources (if available at all) and pre-made kernels/boot loaders as well.

Armbian moves things forward and follows mainline kernel as much as possible, to provide both its features as well as security updates.  The downside is that some features do not work since nobody ported specific drivers to recent mainline, and they can also break.  Armbian can only afford to do brief testing of images and check if basic functions (boot-up, network, USB, etc.) work due to lack of both human and financial resources.

## What does WIP/EOS/CSC mean?

- WIP: Work In Progress: Basic functions can be tested but not ready for production yet.
- CSC: Community Supported Configuration: Community contributed support.  No official support from Armbian development team.
- EOS: End of life: Support ended.

## I have no technical knowledge.  How can I help?

We need many different profiles of people to run this project and just about any help is appreciated, not just help on development.  Since otherwise developers have to fix web pages, developers have to run projects, developers have to seek for money, developers have to maintain servers, developers have to maintain forum, developers have to moderate forums, developers have to maintain infrastructure, developers have to maintain relations with partners, developers have to waste time on repeated support question, developers have to deal with "customers", ...

## Why are old-stable distributions like Ubuntu Focal or Debian Buster not supported?

The Armbian project has very limited human and financial resources so it can focus only on a few up-to-date operating system releases.

## I have a TV Box/tablet from <insert random vendor\>. Can I use Armbian on it?

No.

However some community members are commited to tinkering with these devices.  They discuss their findings in a dedicated space in [our forums](https://forum.armbian.com/forum/24-tv-boxes/). Take note that there is no support from the Armbian development team whatsoever.  
General advice: **Do not buy (cheap) tv boxes!**

## Why does Armbian not support TV boxes in general? The market is huge!

There are some manufacturers who produce better quality than the others.  In general they provide more or less accurate schematics and they have some engineers that are available for general public and you can ask them things here and there.  Most of them try to keep up with the highest standards of hardware development. With proper documentation and minimal support, costs of software development are significantly lower. This is especially important, because we waste our precious private time to secure proper hardware functioning through the time.

However, in vast majority of cases, TV boxes are lacking any documentation.  There are frequent changes of components without notice whatsoever, boot mechanisms are closed source and almost all Armbian builds that exist in the wild are unofficial community hacks.  Market is huge but since public does not have interest in covering of support - which in this case is even bigger - involvement in providing support is simply insane and stupid.  It only eats our personal time and finances.

## There is a new board on the market. Will Armbian officially support it?

Maybe. It depends on things like available documentation from both the vendor as well as SoC manufacturer, production samples to play with, available BSP and last but certainly not least human resources.  A Maintainer within the Armbian development team to say yes. Also if vendors decide to support Armbian there is certainly a higher chance to get it fully supported.

## How can I compile my own kernel?

Normally on Debian or Ubuntu you would do something like `sudo apt-get build-dep linux linux-image-$(uname -r)`.

However Armbian's way of building kernel images is slightly different than the standard distribution method.  The best way is to follow the procedures in the [Developer Guide](https://docs.armbian.com/Developer-Guide_Build-Preparation/).

## Why I cannot choose a specific kernel version (5.11.5 for example)?

Each kernel Armbian offers has a custom patchset on top which would be impossible to maintain compatibility to each and every kernel version out there.  Therefore the choice is usually limited to up to three branches: legacy, current and edge.  Depending on board/family the versions behind these branches may differ.  You can lookup them in the [source code](https://github.com/armbian/build/tree/master/config/sources/families).

## Can I upgrade my userspace, like Buster to Bullseye or Focal to Jammy?

Armbian does not offer a standardized way nor do we encourage users to upgrade their userspace like Focal to Jammy, Jammy to Noble, Bullseye to Bookworm, Bookworm to Trixie. We would love to do that but the reason why we cannot is simply the lack of ressources in time and devices to test such upgrades in random scenarios.

You can try to upgrade your userspace by following official ways from Debian/Ubuntu but make sure to freeze your firmware packages via `armbian-config` beforehand. Also please don't blame/complain at Armbian if something goes wrong or have other issues with the upgraded system.

## Where do I ship a board so that Armbian will add support?

Unless you have an existing arrangement with the Armbian, you will need to [contact Armbian](https://forum.armbian.com/contact/) for a paid engagement.    
You may also add support by yourself if criteria is satisfied. See [Board Support Rules](https://docs.armbian.com/User-Guide_Board-Support-Rules/) for further information.

## What WiFi adapters will most likely work out of the box?

Check [here](https://github.com/morrownr/USB-WiFi).

## I cannot find `armbian-config` on my device.

If you are using a `minimal` variant this tool is not pre-installed. However you can simply install it via `sudo apt update && sudo apt install armbian-config` which will also handle all necessary dependencies.  
If you are not using an `minimal` image and the tool is still missing [make sure your image is genuine](https://docs.armbian.com/User-Guide_Getting-Started/#how-to-check-download-authenticity).

## Why keeps one of the leds flashing twice over and over like a heartbeat? Is there something wrong?

Absolutely not. Quite the contrary. This behaviour is called `heartbeat trigger` and is controlled by the kernel. When the load increases the flashing speed will increase as well. If the flashing stops the kernel either froze or were unloaded by either reboot or shutdown.  
Unhappy? Keep reading below :-)

## Can this behaviour adjusted/disabled?

Maybe. Some boards have certain functions hard-wired to the onboard leds. Others allow to control the led functions from userspace.  
Try to find `trigger` files for the leds in `/sys`.  
Example for an _Orange Pi One_:
```
root@orangepione:~# find /sys/devices -name trigger | grep led
/sys/devices/platform/leds/leds/orangepi:red:status/trigger
/sys/devices/platform/leds/leds/orangepi:green:pwr/trigger
```
Use `cat` on the `trigger` file to both check its current behaviour, which is highlighted with [brackets], and which functions are supported. Then use `echo` to adjust the behaviour.
Example for disabling a led: 
```
root@orangepione:~# cat /sys/devices/platform/leds/leds/orangepi:red:status/trigger
none rc-feedback kbd-scrolllock kbd-numlock kbd-capslock kbd-kanalock kbd-shiftlock kbd-altgrlock kbd-ctrllock kbd-altlock kbd-shiftllock kbd-shiftrlock kbd-ctrlllock kbd-ctrlrlock usbport disk-activity disk-read disk-write ide-disk mtd nand-disk [heartbeat] cpu cpu0 cpu1 cpu2 cpu3 activity default-on panic mmc0 rfkill-any rfkill-none 0.1:01:link 0.1:01:100Mbps 0.1:01:10Mbps
root@orangepione:~# echo none > /sys/devices/platform/leds/leds/orangepi:red:status/trigger
```
