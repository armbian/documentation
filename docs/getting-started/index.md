---
title: Getting Started
seo_title: "Armbian getting started: flash, boot & update"
description: "Step-by-step guide to running Armbian on a single-board computer: choose an image, write it to media, first boot and login, then install and keep it updated."
---
# Armbian Getting Started Guide

Before you start, please make sure you have:

- a proper power supply according to the board manufacturer's requirements <!-- TODO: link to power issues -->
- a reliable SD card (at least 'Class 10' and 'A1'-rated is **highly** recommended)

You will also need an existing operating system and an SD card writer tool. We recommend using **[Armbian Imager](https://imager.armbian.com/)** — the official Armbian flashing tool.

![Armbian Imager workflow](../images/armbian-imager-ani.gif)

Armbian Imager is a **lightweight, native flashing tool** that supports both **selecting and downloading an Armbian image before flashing**, as well as **flashing an already downloaded image**.

!!! warning

    Make sure you use a **good, reliable and fast** SD card. If you encounter boot or stability issues, in over 95 percent of all cases these are either caused by an **insufficient** power supply, or they are related to the SD card. This can be due to a bad card, bad card reader, something went wrong when burning the image, the card turns out to be too slow to boot, etc. Armbian can simply not run on unreliable hardware.

    Checking your SD card with either [F3](https://fight-flash-fraud.readthedocs.io/en/stable/) or [H2testw](https://www.heise.de/download/product/h2testw-50539) is mandatory if you run into problems. Since [counterfeit SD cards](https://www.happybison.com/reviews/how-to-check-and-spot-fake-micro-sd-card-8/) are still an issue, we also highly recommend checking your card with these tools directly after purchase.

    Most SD cards are only optimised for sequential reads/writes as it is common with digital cameras. This is what the *speed class* is about. The SD Association defined [*Application Performance Class*](https://www.sdcard.org/developers/overview/application/index.html) as a standard for random IO performance.

    |Application Performance Class|Pictograph|Minimum Random Read|Minimum Random Write|Minimum Sustained (Seq. Write)|
    |---|---|---|---|---|
    |Class 1 (A1)|![a1-logo](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/a1-logo.png)|1500 4k IOPS|500 4k IOPS|10MBytes/sec|
    |Class 2 (A2)|![a2-logo](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/a2-logo.png)|4000 4k IOPS|2000 4k IOPS|10MBytes/sec|

    We recommend SD cards that are rated at least A1 and fulfill at least speed class C10 or higher (U1/U3, etc.). For example:

    ![a1-16gb-card](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/sandisk-ultra-a1.png) ![a1-32gb-card](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/sandisk-extremepro-a1.png) ![a2-64gb-card](https://raw.githubusercontent.com/armbian/documentation/master/docs/images/sandisk-extreme-a2.png)

    In case you chose an SD card that was already in use before, please consider resetting it back to 'factory default' performance with [SD Formatter](https://www.sdcard.org/downloads/formatter/) before burning Armbian to it ([explanation in the forum](https://forum.armbian.com/topic/3776-the-partition-is-not-resized-to-full-sd-card-size/&do=findComment&comment=27413)). Detailed information regarding ['factory default' SD card performance](https://forum.armbian.com/topic/954-sd-card-performance/page/3/&tab=comments#comment-49811).


!!! tip "New users"

    Some users might find it easier to follow this video tutorial.

    <iframe width="607" height="342" src="https://www.youtube.com/embed/hFrdyLc4g50" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    Some word of advice, though. The video has been created a few years ago. You might therefore find differences between this video and our current site. So, in doubt, also follow the sections below while watching the video.


## The steps

This guide is split into stages. Work through them in order, or jump
straight to the one you need.

1. **[Choosing an Armbian image](choosing-an-image.md)** — Debian or Ubuntu, minimal, server or desktop, and which kernel branch.
2. **[Writing the image to media](writing-the-image.md)** — Armbian Imager to an SD card, or straight to eMMC, UFS or SPI.
3. **[First boot and login](first-boot-and-login.md)** — Power up, set the root password, create your user, get on the network.
4. **[First steps after login](first-steps.md)** — `armbian-config` for the basics, then preconfigured software titles.
5. **[Installing to internal storage](install-to-internal-storage.md)** — `armbian-install` moves the system off the SD card.
6. **[Keeping Armbian up to date](updating.md)** — APT for the OS, `armbian-install` for the boot loader.
7. **[If something goes wrong](troubleshooting.md)** — When a step fails, and how to report a real bug.

Start with **[Choosing an Armbian image](choosing-an-image.md)**.
