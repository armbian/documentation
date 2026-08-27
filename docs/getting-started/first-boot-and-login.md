---
title: First boot and login
seo_title: "First boot & login on Armbian"
description: "Power the board up for the first time, log in as root, set a password, create your everyday user account and connect to a wireless network."
---
# First boot and login

## First boot

If you used an SD card insert it into a slot and power on the board. With the cheapest board, the first boot (with DHCP) can take up to two minutes with a class 10 SD card.

## First login

The first boot will log you in automatically if you have connected a display via HDMI or if you are connected to the serial console. For SSH, you need to login as **root** and use the password **1234**. If you need to find your board's IP address, you can use [this tool](https://angryip.org/).

After logging in, you will be prompted to change the default password. You will then be asked to create a normal user account that will have sudo permissions. Beware, at this stage, the keyboard is using the QWERTY layout. In case you have no wired network connection and there is a wireless adaptor detected, the system will prompt you to connect.

    Welcome to Armbian!

    Documentation: https://docs.armbian.com/ | Community support: https://forum.armbian.com/

    IP address:  Network connection timeout!

    Create root password: ********
    Repeat root password: ********

    Shell: BASH

    Creating a new user account. Press <Ctrl-C> to abort

    Please provide a username (eg. your first name): jane
    Create user (Jane) password: ********
    Repeat user (Jane) password: ********

    Please provide your real name: Jane

    Dear Jane, your account jane has been created and is sudo enabled.
    Please use this account for your daily work from now on.

    Internet connection was not detected.

    Connect via wireless? [Y/n] y

    Multiple wireless adaptors detected. Choose primary:

    1        wlx00e032cxxx94
    2        wlx60fb00yyyc4a

    Enter a number of wireles adaptor: 1

    Detected wireless networks:

    1        NETWORK
    2        MY-WIFI
    3        Caatsanddogs

    Enter a number of SSID: 3

    Enter a password for MY-WIFI: password

    Probing internet connection (9)

    Detected timezone: Europe/Ljubljana

    Set user language based on your location? [Y/n] y

    Generating locales: sl_SI.UTF-8
    root@bananapim2pro:~#

???+ tip "Automated config"
    These settings can be pre-loaded, see [Autoconfig](../user-guide/autoconfig.md)

<!-- TODO: it must be made clear that this just preps the SD card -->

---

**Previous:** [Writing the image to media](writing-the-image.md)

**Next:** [First steps after login](first-steps.md)

Back to the [Getting Started](index.md) overview.
