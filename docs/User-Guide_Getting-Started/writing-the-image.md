---
title: Writing the image to media
description: "Write an Armbian image to an SD card with Armbian Imager, or flash it straight to a board's internal eMMC, UFS or SPI storage over USB."
---
# Writing the image to your media

There are multiple ways to deploy the image to your board. The easiest and most common option is to write the Armbian Image to your SD-Card. 

## Flash to SD Card

Use **[Armbian Imager](https://github.com/armbian/imager/releases)** to flash the image.

Armbian Imager can:

- download official Armbian images
- flash **already downloaded `.img`, `.img.xz`, or custom images**
- automatically verify written data
- protect your system disks from accidental overwrite

Steps:

1. Install and open **Armbian Imager**
2. Select your board or choose a local/custom image
3. Select your SD card or USB drive
4. Flash and wait for verification to finish

!!! warning "Other tools"

    We are aware that many programs can be used for this step. However, tools without proper verification and safe target selection can hide problems such as bad cards, faulty readers, partial writes, or accidentally selecting the wrong drive. These issues have caused too many avoidable error reports.

    For this reason, **Armbian Imager is the recommended tool**.

    Due to reports of image corruption caused by decompression issues, [balenaEtcher](https://www.balena.io/etcher/) is not recommended.

## Flash to Internal Memory

Flash to Internal Memory allows you to write Armbian image directly to the device’s built‑in storage. This process completely replaces the existing system and erases all current data on the target drive. Use with caution, as once started, the operation cannot be undone.

### Rockchip

When a Rockchip device is placed into **Maskrom mode**, you can use `rkdeveloptool` to flash an image directly to its internal storage (**eMMC**, **UFS**, or **SPI**) over USB.

=== "Debian"

    Install requirements for `rkdeveloptool`

    ``` bash
    sudo apt-get update
    sudo apt-get install -y build-essential git wget
    sudo apt-get install -y libudev-dev libusb-1.0-0-dev dh-autoreconf pkg-config libusb-1.0
    ```

    Download & Compile `rkdeveloptool`

    ``` bash
    git clone https://github.com/rockchip-linux/rkdeveloptool
    cd rkdeveloptool
    autoreconf -i
    ./configure
    make -j $(nproc)
    ```

    Optionally install `rkdeveloptool` systemwide:

    ``` bash
    sudo cp rkdeveloptool /usr/local/sbin/
    ```

=== "MacOS"

    First make sure you have [brew](https://brew.sh) installed. Then you can run the following commands to install rkdeveloptool:

    Install requirements

    ``` bash
    brew install automake autoconf libusb pkg-config git wget
    ```

    Download & Compile `rkdeveloptool`

    ``` bash
    git clone https://github.com/rockchip-linux/rkdeveloptool
    cd rkdeveloptool
    autoreconf -i
    ./configure
    make -j $(nproc)
    ```

    Optionally install `rkdeveloptool` systemwide:

    ``` bash
    cp rkdeveloptool /opt/homebrew/bin/
    ```

1. Connect & Boot your Board into Maskrom mode. Usually there is a button to hold for 5 seconds during boot else check your manufactures website.
2. Run `rkdeveloptool ld` to list all connected devices
3. Extract your image `unxz Armbian-YourBoard.img.xz`
4. Flash the RK3XXX_loader.bin (check your SoC) via `rkdeveloptool db RK3XXX_loader.bin` which stands for download boot
5. Erase the current storage medium (usually EMMC) via `rkdeveloptool ef` which stands for erase flash
6. Now you can flash the extracted image with `sudo rkdeveloptool wl 0 Armbian-YourBoard.img` (make sure the file ends with **.img**)
7. Reboot your board with `sudo rkdeveloptool rd` which stands for (power) reset device

---

**Previous:** [Choosing an Armbian image](choosing-an-image.md)

**Next:** [First boot and login](first-boot-and-login.md)

Back to the [Getting Started](../User-Guide_Getting-Started.md) overview.
