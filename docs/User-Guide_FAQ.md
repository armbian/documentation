# Frequently asked questions

**This information is mainly for new/inexperienced users but could be useful for others too.**

## Is Armbian an operating system?

Not per se. Armbian is a collection of scripts that allows users to create images for SBCs with working kernels in various userspace configurations. Armbian does provide prebuild images but mostly for users convenience.

## Why I cannot simply shove a random image into my board to work like on my PC?

x86 architecture always has a traditional BIOS or UEFI.   This provides a standard framework for operating systems to interact with the hardware.  Most SBCs do not.   ARM is improving the situation with *ARM Server Ready* and *ARM System Ready certificates*, but most SBC vendors are not yet incentivized to meet these standards.

Without such standards, many vendors quickly fork low-level bootloaders such as u-boot and make the bare minimum modifications needed.

[great reference here](https://bootlin.com/pub/conferences/2017/lca/petazzoni-arm-introduction/petazzoni-arm-introduction.pdf)
	
## Why is Armbian constantly asking for money? Free software should be free.

Making free licence software also require best people, expensive infrastructure, tooling. It has as much or more costs as propriatery while generating no income from the licence.

tl;dr; We are asking for help that developers and project maintainers doesn't loose their generocity and humanity which are the driving force that generates a value. For all of us! Great deal of our work represent a big pressure to our very limited private resources. We ask you to share that burden with us.

### Development Time

We are covering large area of diversed custom designed ARM hardware they way, size and under conditions nobody else does. Keeping this service up, keeping those low end hardware functional is laborious.  When releases are approaching and a lot of testing and fixing is going on, this gets up, stress intensifies. This means we have to invest let's say at least 3.000 - 4.000 EUR of our time on top of fixed costs into this service every day just to keep it up. Without developing any serious features [you wish to have](https://forum.armbian.com/forum/38-feature-requests/). Fulfilling many of these wishes would easily cost tens of thousands in development time, which we don't have and which we can't get back due to it being free software. Nobody needs to buy licence for using it, just a few people decides to [respect time and attention](https://forum.armbian.com/subscriptions/) that are receiving from developers on forums. 

### Infrastructure and Operations

We have to maintain our infrastructure where biggest costs is - once again - people's time, followed by electricity, then hardware itself. Often we get free hardware and very rare break even with electricity costs and with people that would maintain this for us. A new sponsored box usually brings us more costs then benefits. Since benefit is anyway public.

### Support Time

Each question that is directed towards our team is generating opportunity costs and taking away from development time. Some we are happy to cover, but not all. Especially when it goes for repetitive questions and demands.  

Questions associated with missing features represent another hit and miss for us. Complicated and critical upstream functions (like video acceleration withing a web browser, supporting a board that have very poor initial support and no community backing, ...) are missing. This functionality is unique to hardware and implementing is extremely labor intensive and requires unique expertise. Our team is 10-15 volunteers that maintain this project in their free time. We cannot cover the job of Google Chromium team, Collabora, ARM, Rockchip and others vendors which have not provided sufficient support for their products.

All our work is done in public and we provide all sources which we are changing in the process. All our work is patent free and released under a free licence so anyone can re-use it further. The scale of SBCs Armbian supports is hard to beat, and consequently our work is repackaged and reused by other projects and vendors. Unfortunately the burden of support is often directed to us, while they focus on revenue.

## Why does Armbian not support RaspberryPi?

Historically the Raspberry Pi has had a strong community and its own support.  Armbian's development effort is better spent focusing on other ARM-based SBCs with less support.  
There are other reasons as well. If you are interested there is a years-long conversation going on in forums: https://forum.armbian.com/topic/483-support-of-raspberry-pi/

## Why does hardware feature XY work in old kernel but not in more recent one?

Vendors tend to fork old kernel and U-Boot versions and only do minimal adjustments to make board features work. Besides the fact that those adjustments are almost never pushed to mainline they usually do not update their sources (if available at all) and kernels as well.  
Armbian moves things forward and follows mainline kernel as much as possible to provide both its features as well as security updates. The downside is that some features do not work since nobody ported specific drivers to mainline and they can also break. Armbian can only afford to do a brief testing of images and check if basic functions (boot-up, network, USB...) work due to lack of both human and financial resources.

## What does WIP/EOS/CSC mean?

- WIP: Work in progress
  - Basic functions can be tested but not ready for production yet
- CSC: Community supported configuration
  - Community contributed support. No official support from Armbian development team
- EOS: End of life
  - Support ended

## I have no technical knowledge. How can I help?

We need many different profiles of people to run this project and just about any help, help on development. Since in other case developers have to fix web pages, developers have to run projects, developers have to seek for money, developers have to maintain servers, developers have to maintain forum, developers have to moderate forums, developers have to maintain infrastructure, developers have to maintain relations with partners, developers have to waste time on repeated support question, developers have to deal with "customers", ...

## Why are old-stable distributions like Ubuntu Bionic or Debian Stretch not supported?

The Armbian project has very limited human and financial ressources so it can focus on just a few up-to-date operating systems only.

## Why does Armbian not support TV boxes? The market is huge!

Single board computer vendors are making their computers on as cheap as possible principle. There are some exceptions to be honest, which in fact produce better quality then the others. In general they provide more or less accurate schematics and they have some engineers that are available for general public and you can ask them things here and there. Most of them try to keep up with the highest standards of hardware development. With proper documentation and minimal support, costs of software development are significantly lower. This is especially important, because we waste our precious private time to secure proper hardware functioning through the time.

TV boxes lacking of any docuentation. There are frequent changes of components without any notice whatsoever, boot mechanisms are closed source and almost all Armbian builds that exist in the wild are community hacks. Market is huge but since public does not have interest in covering of support - which in this case are even bigger - our involvement to provide support is simply insane and stupid. It only eats our personal time and finances.

## There is a new board on the market. Will Armbian officially support it?

Maybe. It depends on things like available documentation from both the vendor as well as SoC manufacturer, production samples to play with, available BSP and last but not least human ressource, maintainer within the Armbian development team to say. Also if vendors decide to support Armbian there is certainly a higher chance to get it fully supported.

