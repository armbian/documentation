# Frequently asked questions

## What is Armbian?

Armbian is a lightweight Linux distribution optimized for single board computers (SBCs). It provides a reliable, standardized Debian or Ubuntu-based environment tailored to work across many different ARM devices. 

In addition to prebuilt images, Armbian includes a powerful [build framework](https://github.com/armbian/build) that lets you customize kernel versions, desktop environments, and other system components to fit your needs.

## Why no universal image?

The **x86 architecture includes BIOS or UEFI**, providing a standardized interface. In contrast, **most SBCs lack such consistency**. Although the ARM ecosystem is improving via **ARM ServerReady** and **SystemReady certifications**, adoption is limited. Vendors often have **tight budgets and minimal engineering resources**, and there's little incentive to go beyond basic boot functionality.

Instead of following standards, vendors usually **fork U-Boot and apply minimal changes** needed to boot their boards.

## Why does Armbian need help?

Building and maintaining support for diverse custom hardware requires substantial **time, infrastructure, and expertise**—similar to commercial software development, but without licensing revenue. Armbian supports **a wide range of ARM-based boards**, often with **minimal or no vendor assistance** and limited user contributions. As a result, our team takes on the full responsibility for **board bring-up, patching, testing, and ongoing maintenance**, largely funded out of pocket.

In addition to the software, we maintain **forums, documentation, and user support**, all of which demand consistent effort. A dedicated group of just **10–15 volunteers** sustains the project in their spare time. While some projects repackage and redistribute our work, **the core maintenance responsibility remains with us**.

We also face **commercial entities** that leverage our work—sometimes contributing only superficial changes—adding further pressure to our limited resources. That’s why we kindly ask for **your support in helping us sustain and grow Armbian**.

## Why things stop working?

Vendors often base their software on **fixed, vendor-specific LTS kernels** and **custom U-Boot forks**, which may lack long-term upstream maintenance or open-source availability.

Armbian, by contrast, **tracks and contributes to mainline kernel development** to provide modern features and improved security. However, if **drivers are not upstreamed or properly ported**, certain hardware functions may not work or may break over time.

Our development focus is on maintaining the **CURRENT kernel branch**, which is selected for having sufficient maturity and stability for general use. **EDGE kernels**, as the name implies, are based on the latest upstream kernel versions — often including release candidates — and are **not suitable for production deployment**. These kernels are assembled for early adopters and development purposes only. Their experimental nature means **higher risk of regressions and broken functionality**.

Due to limited resources, Armbian prioritizes **basic functionality and integration testing**, not full validation of all features across all supported devices. While we do identify many issues, **some remain unresolved for extended periods — sometimes months or even years — due to a significant shortage of development capacity**.

## What do WIP, EOS, CSC mean?

These indicate [**support status**](https://docs.armbian.com/User-Guide_Board-Support-Rules):

- **.conf**: *Official Configuration*. Boards with this status are supported by the Armbian team and benefit from **Standard** or **Platinum** support levels, depending on vendor involvement, stability, and available maintenance resources.
- **WIP**: *Work In Progress*. Early development; **not ready for production**.
- **CSC**: *Community Supported Configuration*. Maintained by the **community**, not the core team.
- **EOS**: *End of Support*. **No further updates or maintenance.**

## Can I help without tech skills?

Absolutely! **Non-technical help is equally valuable**. Without community help, developers must do everything: **run infrastructure, moderate forums, answer support, manage partnerships, and fundraise**—on top of development.

<https://www.armbian.com/contact/>

You can help with **documentation, moderation, translations, outreach, fundraising, or promotion**—freeing developers to focus on what they do best.

## Why no support for old OS?

Armbian has **limited resources**, unlike larger projects. Supporting outdated OS releases like **Ubuntu Focal** or **Debian Buster**, which may lack upstream maintenance, **diverts resources from improving current versions**.

We focus only on the latest stable releases of [**Debian**](https://www.debian.org/releases/stable/) and [**Ubuntu**](https://wiki.ubuntu.com/Releases).

## Why no support for TV boxes?

A few vendors provide **schematics, upstream support, and occasional assistance**, which helps. But **most TV boxes lack documentation**, **change hardware without notice**, and use **closed-source bootloaders**.

Nearly all Armbian images for these devices are **unofficial community hacks**. Despite the large market, the **cost of support is high**, and public interest in sustaining it is low. Supporting these devices would be **unsustainable** for our small team.

## Will my board be supported?

**Maybe.** Official support depends on factors like **documentation**, **SoC vendor transparency**, **sample availability**, and—most critically—a **willing maintainer**.

When **vendors collaborate with Armbian**, the chance of support **significantly increases**.

## Which WiFi works right away?

WiFi compatibility depends on **Linux kernel driver support**. Adapters using **Intel, Atheros, or Realtek chipsets** tend to work better **out of the box**.

For performance and compatibility details, see:  
<https://docs.armbian.com/WifiPerformance/>

Note: **Results may vary by board**, due to **power limits, USB/PCI quirks**, and driver maturity.

## Why is my image not listed?

Creating and maintaining images for **all combinations** of kernel, userspace, and desktop across all boards is **technically and financially unfeasible**. We provide **[a carefully chosen set of default images](https://github.com/armbian/os/blob/main/userpatches/targets-release-standard-support.yaml)** per board.

However, using the [**Armbian build framework**](https://docs.armbian.com/Developer-Guide_Build-Preparation/), you can **easily create custom images**. It’s well-documented and accessible to moderately experienced users.

If enough users show interest in a specific configuration, we may **adjust build targets** accordingly.
