---
title: Choosing an Armbian image
description: "Pick the right Armbian image for your board: Debian or Ubuntu, minimal, server or desktop, and the vendor, current, edge and legacy kernel branches."
---
# Choosing an image

If your hardware is [supported](../index.md#which-hardware-is-supported), the recommended way to get started is to use **[Armbian Imager](https://imager.armbian.com/)** to select your board, download the appropriate image, and flash it in one step; alternatively, images can also be downloaded manually from [https://www.armbian.com/download/](https://www.armbian.com/download/) and flashed using Armbian Imager.

<!-- TODO: add some information about using the user interface on the site -->


## Debian or Ubuntu

If you have no special preferences or requirements, we recommend using an Ubuntu based Armbian image.


## Minimal, Server, or Desktop

For each board, we usually provide these types of images:

- **Minimal** - lightweight CLI with only a bare minimum of packages and no graphical user environment
- **Server** - server variant with preinstalled standard utilities and no graphical user environment
- **Desktop** - full featured desktop image

For some boards we provide only minimal images due to their hardware limitations.


## Vendor, Current, Edge, or Legacy

In some cases we provide images with different firmware. They differ in the level of hardware support and can be classified as follows:

- **vendor** contains a vendor-provided kernel which usually has the best hardware support while package version can be outdated, containing less general fixes <!-- TODO: phrasing -->
- **current** is following the latest [Linux mainline LTS kernel](https://www.kernel.org/category/releases.html) and is in most cases the _best choice_.

Use the following images only if these are the only ones provided, or if you want to participate in testing:

- **edge** is, as the name implies, cutting-edge fresh / development / latest stable. It is only automatically tested, it can break at any time, and it is recommended only for experienced users.
- **legacy** is the old stable current kernel. Use it if _current_ is not available or if something does not work well with it.

The level of kernel support, however, always depends on the board family. If in your specific case something does not work well, you are always free to try an image with another kernel included, or change the kernel with [armbian-config](../config/index.md).


## Rolling releases

<!-- TODO: this might be too much here; explanation could go into development docs, or appendix maybe?? -->

Rolling releases are suitable for Linux enthusiasts who want cutting edge packages and have the skills to fix the damage that a bad update might cause. If you want stability in a production environment or low headaches as a novice user, skip rolling releases. They are not at a suitable support quality level!

``` mermaid
graph LR
  A[Hardware] --> B{Armbian kernel};
  B -->|legacy| C["rolling release"];
  B -->|vendor| C["rolling release"];
  B -->|current| C["rolling release"];
  B -->|edge| C["rolling release"];
  B -->|legacy| X["point release"];
  B -->|vendor| X["point release"];
  B -->|current| X["point release"];
  B -->|edge| X["point release"];


  C ---->|minimal| E[Debian or Ubuntu];
  C ---->|server| F[Debian or Ubuntu];
  C ---->|desktop| G[Debian or Ubuntu];

  X ---->|minimal| E[Debian or Ubuntu];
  X ---->|server| F[Debian or Ubuntu];
  X ---->|desktop| G[Debian or Ubuntu];
```

!!! danger

    **Do not use** rolling release or edge images in a productive environment. Their purpose is testing and providing constructive [feedback to developers](https://forum.armbian.com/forum/4-development/).


## Download and verification

After you have determined the image you want, the download for each image consists of three separate files:

- the **.xz** compressed image file
- the **.sha file** for download verification (optional)
- the **.asc file** for image authentication (optional)

After you have downloaded these files, we recommend checking the integrity and the authenticity of the compressed image file.

!!! question "How to check the download integrity?"

    Since it might happen that your download got somehow corrupted, we publish a checksum/hash for each of our images. You can compare the image's SHA-256 hash with the one contained in the `.sha` file.

    On Windows, you can download and use the [QuickHash GUI](https://www.quickhash-gui.org/download/quickhash-v3-1-0-windows/) and follow the instructions in the gui. Linux and macOS users can simply do this in the directory with the compressed image and the checksum file:

    ```sh
    sha256sum -c Armbian_25.2.1_Bananapicm4io_bookworm_current_6.12.13_minimal.img.xz.sha
    ```

    The integrity is verified if the output looks something like this:

    ```sh
    Armbian_25.2.1_Bananapicm4io_bookworm_current_6.12.13_minimal.img.xz: OK
    ```

!!! question "How to check the download authenticity?"

    All our images are digitally signed. It is therefore possible to check their authenticity. Linux and macOS user might need to install the required tools first: for Debian/Ubuntu, this can be done via `sudo apt-get install gnupg `, and for macOS use `brew install gnupg `. Windows users can install [GnuPG from here](https://gnupg.org/download/). To check the authenticity, you will need the public key that was used to sign the images. This key can be retrieved from a keyserver or from the Debian/Ubuntu package repository (this step only needs to be done once):

    ```sh
    # download public keys either from a keyserver
    gpg --keyserver hkp://keyserver.ubuntu.com --recv-key DF00FAF1C577104B50BF1D0093D6889F9F0E78D5
    gpg --keyserver hkp://keyserver.ubuntu.com --recv-key 8CFA83D13EB2181EEF5843E41EB30FAF236099FE
    # or from the repository server
    wget -O- https://apt.armbian.com/armbian.key | gpg --import -
    ```

    To perform the verfification, run the command shown below.

    ```sh
    gpg --verify Armbian_25.2.1_Bananapicm4io_bookworm_current_6.12.13_minimal.img.xz.asc
    ```

    While the output can very depending on the GnuPG version, it should result in a response similar to the one below. It is safe to ignore the message `WARNING: This key is not certified with a trusted signature!`.

    ```sh
    gpg: Signature made Thu Feb 13 11:53:18 2025 CET
    gpg:                using RSA key DF00FAF1C577104B50BF1D0093D6889F9F0E78D5
    gpg: Good signature from "Igor Pecovnik <igor@++++++++++++.com>" [unknown]
    gpg:                 aka "Igor Pecovnik (Ljubljana, Slovenia) <igor.++++++++++++@gmail.com>" [unknown]
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: DF00 FAF1 C577 104B 50BF  1D00 93D6 889F 9F0E 78D5
    ```

    If something is wrong, the output will look something like this:

    ```sh
    gpg: Signature made Thu Feb 13 11:53:18 2025 CET
    gpg:                using RSA key DF00FAF1C577104B50BF1D0093D6889F9F0E78D5
    gpg: BAD signature from "Igor Pecovnik <igor@++++++++++++>" [unknown]
    ```

---

**Previous:** [Getting Started](index.md)

**Next:** [Writing the image to media](writing-the-image.md)

Back to the [Getting Started](index.md) overview.
