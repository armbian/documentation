---
title: Armbian — Linux for ARM single-board computers
description: "Armbian is a lean Debian and Ubuntu based Linux for ARM and RISC-V single-board computers. Docs for installing, configuring and building your own images."
image: /images/armbian-logo.png
---

# Armbian OS

## Preface

Welcome to the official documentation of Armbian Linux, a highly optimized base operating system specialized for single board computers (*SBCs*) and its extensive build framework.


### How is the documentation structured?

The table of contents in the sidebar and the links at the top of the page should let you easily access the documentation for your topic of interest.

If you are **new to Armbian**, this _Introduction_ and the [_Getting Started_](getting-started/index.md) sections provide everything you need to know about the project, where to find the resources for your board, and a tutorial for everything you need to get Armbian running and configured.

It then continues on to [_Advanced Configuration_](User-Guide_Advanced-Configuration.md) tasks and tools for **advanced users**. The topics in this section cover a wide range of tasks: configuring the system or the network without using [`armbian-config`](config/index.md), configuring your device automatically at first boot, and creating a custom image using the [`Armbian Build Framework`](/build-framework/).

If you have read through the documentation and still **need help**, check out our [_Troubleshooting_](User-Guide_Troubleshooting.md) advice.

<!-- TODO: Changelog, Relases, Model, FAQ appendixes -->


### Where to find additional help?

If you still cannot find what you need here, visit the [_Armbian forum_](https://forum.armbian.com/) where your input can also help us improving this documentation.


### How to report a problem in this documentation?

If you come across an issue in these pages, you can either report it [here](https://github.com/armbian/documentation/issues), or follow [these instructions](https://github.com/armbian/documentation/blob/main/README.md) to suggest a fix yourself.


## What is Armbian?

Armbian's goal is to provide a **highly optimized base operating system specialized for single board computers**. It embodies extremely **lightweight** hardware features with a **well-known** and supported Debian-based user-space experience, an **extensive build framework**, and it is suitable for **industrial or home use**.

Armbian is **not** a Linux distribution itself. Instead, we use Debian GNU/Linux and Ubuntu Linux as base for the images, that our users can download and deploy. We build our own set of optimized kernels for each board, and then provide an extensive and customizable framework to build, adjust, and configure these images. This framework is the heart of the project.

![What is Armbian](images/whatisarmbian.png)

### Key features

As a user, you can simply download one of our images, deploy and run it on your SBC. As an advanced user, a manufacturer or provider, you can create fully configured custom images for your board or product.

In any case, you will get these key advantages:

- you get a lean and standard **Debian** or **Ubuntu** based user space with the well known APT package manager
- we provide independent kernel development and maintenance with **long term support**
- we provide an extensive [build framework](https://github.com/armbian/build) with fast **hybrid assembly** of the whole operating system and **endless capabilities**
- we provide advanced **hardware and OS configuration** and **software installation** with the built-in [armbian-config](config/index.md) tool
- we provide exclusive support for **exotic hardware** that nobody else supports
- we provide **stabilized point** and **rolling** distribution of upgrades and OS images
- we provide a global download infrastructure with **perfect coverage, also in China mainland**
- we provide an **extensive build infrastructure** to assist in CI automation
- we do daily **automated stress and upgrade testing** on key hardware targets
- we have strong ties to embedded Linux

???+ "Other features and performance tweaks worth mentioning"

    - Images are highly compressed and automatically expand across the boot media at first boot
    - Preinstalled standard system utilities like BASH or ZSH shell
    - Login is possible via serial, HDMI/VGA or SSH
    - Custom login MOTD showing a collection of important information
    - `/var/log` is mounted as compressed device (zram, lzo) and the log2ram service saves the logs to disk daily and on shutdown
    - Half of the memory is allocated/extended for/with compressed zswap
    - `/tmp` is mounted as `tmpfs` (and can be optionally compressed)
    - Browser profile memory caching is enabled on desktop images
    - Optimized IO scheduler (check `/etc/init.d/armhwinfo`)
    - Journal data writeback is enabled (`/etc/fstab`)
    - Ethernet interrupts are using a dedicated core


### Comparison

<!-- TODO: where to??? -->

Two categories are compared alongside Armbian:

- **Downstream** &mdash; a board or SoC vendor's own OS release for its own hardware.
- **Upstream** &mdash; the mainline Linux and U-Boot trees, and distributions that ship only mainline.

Each Armbian claim links to the evidence for it. The other two columns state what
those categories are by construction, and say *varies by vendor* wherever nothing
general can be checked. They are not findings about any particular vendor or
distribution.

| | Armbian | Downstream | Upstream |
| -------- | -------- | -------- | -------- |
| Hardware maintainers | [named per board](https://armbian.com/authors) | the vendor, for its own hardware | [per subsystem](https://github.com/torvalds/linux/blob/master/MAINTAINERS), not per board |
| Build framework | [builds the whole OS](https://github.com/armbian/build) from source | the vendor's own, for its own hardware | kernel and bootloader, not an OS image |
| Maintenance | modular and reviewed; `armbian-config` is [unit tested per pull request](https://github.com/armbian/configng/actions/workflows/maintenance-unit-tests.yml) | varies by vendor | public mailing-list review |
| User-space | Debian or Ubuntu based, with Armbian packages and configuration | the vendor's own image | stock distribution user space |
| Declaring support | Standard Support requires a named maintainer; Community maintained is declared as not under active supervision &mdash; see the [Board Support Rules](User-Guide_Board-Support-Rules.md) | varies by vendor | per [`MAINTAINERS`](https://github.com/torvalds/linux/blob/master/MAINTAINERS) entry, not per board |


## Which hardware is supported?

Armbian distributes stable images for many different single board computers (SBCs). But not each model receives the same amount of support and maintenance. This might be due to lack of man-power, lack of support by the manufacturer, etc. We have therefore a system that shows the support status for each board:

[Platinum Support](https://armbian.com/boards?support=platinum){ .md-button .md-button--primary }

At least one person is providing constant maintenance and support.

[Standard Support](https://armbian.com/boards?support=standard){ .md-button }

Support is not secured, but it is still overall good.

[Community maintained](https://armbian.com/boards?support=community){ .md-button }

Most of the images for boards in this category will also work, but no warranty can be given as Armbian does not monitor their status.

*Supported / maintained* is not a guarantee, though. It merely implies that a particular SBC is at a **high level of software maturity** and has a named maintainer. Due to the complexity and lack of cooperation in the ecosystem, it is unlikely that all specialized functionalities (like 3D, VE, I²C...) are always available.

For more information see the [Board Support Guide](User-Guide_Board-Support-Rules.md)


## Where to find images and sources?

Our main website is <https://www.armbian.com/>. It is the default site for our users, and it contains the download section with all images, information about the support status for each board, links to our forum and this documentation.

The project sources are hosted on [GitHub](https://github.com/armbian) and are organized in separate Git repositories. These are the resources for developers and participants, e.g. users helping with testing.


## How can you contribute?

If you want to contribute to our project, please read the [collaboration notes](Process_Contribute.md).


???+ success "Unit testing"


    All software targets and functions are automatically tested to catch as many problems as possible.

    <a href=https://github.com/armbian/configng/actions/workflows/maintenance-unit-tests.yml><img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/armbian/configng/maintenance-unit-tests.yml?logo=githubactions&label=Unit%20tests&style=for-the-badge&branch=main"></a>
