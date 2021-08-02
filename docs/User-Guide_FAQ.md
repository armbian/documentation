# Frequently asked questions

- **This information is mainly for new/inexperienced users but could be useful for others too.**

## Is Armbian an operating system?

Not per se. Armbian is a collection of scripts that allows users to create images for SBCs with working kernels in various userspace configurations. Armbian does provide prebuild images but mostly for users convenience.

## Why I cannot simply shove a random image into my board to work like on my PC?

Shortly explain difference between ARM and Intel architecure. Bus system, device tree....that reasons.

x86 architecture always has a traditional BIOS or UEFI.   This provides a standard framework for operating systems to interact with the hardware.  Most SBCs do not.   ARM is improving the situation with *ARM Server Ready* and *ARM System Ready certificates*, but most SBC vendors are not yet incentivized to meet these standards.

Without such standards, many vendors quickly fork low-level bootloaders such as u-boot and make the bare minimum modifications needed.

[great reference here](https://bootlin.com/pub/conferences/2017/lca/petazzoni-arm-introduction/petazzoni-arm-introduction.pdf)
	
## Why is Armbian constantly asking for money? Free software should be free.

Making free licence software also require best people, expensive infrastructure, tooling. It has as much or more costs as propriatery while generating no income from the licence.

tl;dr; We are asking for help that developers and project maintainers doesn't loose their generocity and humanity which are the driving force that generates a value. For all of us! Great deal of our work represent a big pressure to our very limited private resources. We ask you to share that burden with us.

We are covering large area of diversed custom designed ARM hardware they way, size and under conditions nobody else does. Keeping this service up, keeping those low end hardware functional, costs maintainers between 30 and 60 hours every day. When releases are approaching and a lot of testing and fixing is going on, this gets up, stress intensifies. This means we have to invest let's say at least 3.000 - 4.000 EUR of our time on top of fixed costs into this service every day just to keep it up. Without developing any serious features [you wish to have](https://forum.armbian.com/forum/38-feature-requests/). Fulfilling your wishes would costs millions, which we don't have and which we can't get back, since you expect that software is free. Nobody needs to buy licence for using it, just a few people decides to [respect time and attention](https://forum.armbian.com/subscriptions/) that are receiving from developers on forums. 

We have to maintain our infrastructure where biggest costs is - once again - people's time, followed by electricity, then hardware itself. Often we get free hardware and very rare break even with electricity costs and with people that would maintain this for us. A new sponsored box usually brings us more costs then benefits. Since benefit is anyway public.

There are more and more positions where it is nearly impossible to get a reliable volunteer, but resource such as project management, documentation editor or marketing communication is critical for project development in general. It is needed to keep up and to secure service users expect to have.

Each question that is directed towards our team is generating costs. Some we are happy to cover, but not all. Especially when it goes for repetitive questions and demands. Luxury of demanding and putting any kind of pressure is not a part of this service - it is our time and energy that helps you and money flow from your side can mitigate this tension. Especially because questions are repeating and users convenience is preventing them to invest five seconds into searching around.

Questions associated with missing features represent another hit and miss for us. Complicated and critical functions (like video acceleration withing a web browser, supporting a board that have very poor initial support and no community backing, ...) are missing with a reasons - their development can cost tens or hundredts of thousands of dollars nobody is willing to pay. Why on earth would that cost be a problem of Armbian team who is already wasting 3.000 EUR of their money per day? Our team is 10-15 volunteers that maintain this project in their free time. We cannot cover the job of Google Chromium team, Collabora, ARM, Rockchip and others vendors which failed to provide you this. And have budget for development in billions of dollars.

Those costs go sky high when someone expects personal dedication. Answering in hard technical questions can easily cost us additional 10 hours per day of totally wasted time. Private technical communication on public project is most wasted time since it is the most ineffective way to share knowledge which we would like to share as much as possible. But all have to work elsewhere to cover for family and to cover for your pleasure you have with this project. We can only afford to cover provide forums, docs, IRC/Discord.

All our work is done in public and we provide all sources which we are changing in the process. All our work is patent free and released under a free licence so anyone can re-use it further. Since we are ahead of many other projects we loose a lot more since most of projects that are repacking our work do not even try to deal with the support we do and can focus on sales only.

## Why does Armbian not support RaspberryPi?

Historically the Raspberry Pi has had a strong community and its own support.  Armbian's development effort is better spent focusing on other ARM-based SBCs with less support.  
There are other reasons as well. If you are interested there is a years-long conversation going on in forums: https://forum.armbian.com/topic/483-support-of-raspberry-pi/

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

## Add more....
