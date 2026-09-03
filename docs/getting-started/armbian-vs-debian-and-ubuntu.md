---
title: Armbian vs Debian & Ubuntu
description: "Armbian vs Debian vs Ubuntu on single-board computers: keep the Debian/Ubuntu user space you know, and gain optimized per-family kernels, ready-to-flash images, armbian-config, and hardware tested daily on real boards."
---

# Armbian vs Debian & Ubuntu

> **Armbian brings the embedded-hardware world to Debian and Ubuntu** &mdash; the boards, kernels, bootloaders and tuning they do not ship, on top of the user space you already know.

**Short version:** Armbian is not a rival to Debian or Ubuntu &mdash; it is *built on both*, and its job is to bring the embedded-hardware world to them. On a laptop, server or cloud VM you would simply run Debian or Ubuntu. On an **ARM or RISC-V single-board computer (SBC)**, Armbian gives you that same familiar Debian or Ubuntu user space **plus** the board-specific engineering &mdash; optimized kernels, bootloaders, device trees, ready-to-flash images and tuning &mdash; that generic distributions do not provide for most boards. It is a **kernel-first distribution**: the board's kernel is the heart of the project, continuously validated on real hardware.

!!! tip "The best of both worlds"
    Think of Armbian as **Debian and Ubuntu, maintained by kernel-space engineers.** You keep Debian or Ubuntu and `apt`; you add first-class hardware support, out-of-the-box optimization, and tooling made for SBCs. **You even get to choose** whether each image is Debian- or Ubuntu-based.

## At a glance

| | **Debian** | **Ubuntu** | **Armbian** |
| --- | --- | --- | --- |
| User space & package manager | Debian, `apt` | Ubuntu, `apt` | **Debian *or* Ubuntu, `apt`** &mdash; you pick |
| Primary target | Servers, desktops, x86 & official ARM ports | Cloud, desktop, x86 & certified ARM | **SBCs first** &mdash; [around 400 ARM/RISC-V boards](https://www.armbian.com/download/), server & desktop &mdash; plus cloud UEFI [x86-64](https://www.armbian.com/uefi-x86/)/[arm64](https://www.armbian.com/uefi-arm64/) |
| Kernel for your board | Generic; often unavailable or unaccelerated on SBCs | Generic; official images only for a few boards | **[Optimized kernel per board family](../status/package-repository.md#kernel-families)**, mainline based (`current` tracks the Linux LTS), with `vendor`, `legacy` and `edge` options |
| Wireless (Wi-Fi/Bluetooth) drivers | Only what the mainline kernel ships | Mainline kernel, plus a few | **Large set of extra out-of-tree drivers built into the kernel** &mdash; [work out of the box](../status/wifi-performance.md), no need for DKMS |
| Bootloader, device tree, board bring-up | Do it yourself | Do it yourself | **Provided and maintained** for supported boards (per [support level](/contribute/board-support-rules/)) |
| Image for your specific SBC | Rarely ready-made | Only for select boards | **Ready-to-flash**, compressed, [auto-expands on first boot](../index.md#key-features) |
| SBC tuning out of the box | None | None | **[zram-compressed logs, tuned I/O scheduler, DVFS, swap tuning, near read-only root](../index.md#key-features)** |
| Guided hardware & software setup | Standard tools | Standard tools | **[`armbian-config`](../config/index.md)** menu-driven utility |
| Continuous hardware validation | No per-board hardware testing | No per-board hardware testing | **[Nightly automated fleet](../status/board-tests.md)** — upgrade, reboot, performance, DVFS & network, on real boards |
| Build your own custom image | `debootstrap` / DIY | DIY | **[Full build framework](https://github.com/armbian/build)**, hybrid assembly, runs under Docker |
| Exotic / OS-neglected hardware | Unsupported | Unsupported | **Supported where nobody else is** |
| Download delivery | Community mirrors | Community mirrors | **[Global mirror network](../status/mirrors.md)** with coverage in mainland China, plus multi-mirror torrents |
| Cost | Free | Free (commercial Ubuntu Pro available) | **Free** &mdash; always, for everyone |

## Why Armbian on an SBC

### Keep the distribution you already know

Armbian images are a **lean, standard Debian or Ubuntu user space** with the well-known `apt` package manager &mdash; no proprietary base, no vendor lock-in, no relearning. Your scripts, packages and habits carry straight over. See [key features](../index.md#key-features).

### Kernel-first by design

Armbian is a **kernel-first distribution**. Where general-purpose distributions treat the kernel as one interchangeable package and ship a single generic build, Armbian puts the **board's kernel at the centre of the project**: for most SBCs there is no ready mainline image, and where a generic kernel exists it often leaves accelerators, network, video or peripherals inactive. Armbian does **independent kernel development and maintenance with long-term support** across [many kernel families](../status/package-repository.md#kernel-families), owning the bootloader, device tree and board patches, and lets you switch between **vendor, current, edge and legacy** branches per board &mdash; see [Choosing an image](choosing-an-image.md#vendor-current-edge-or-legacy). The user space is deliberately kept as **stock Debian or Ubuntu** so the part that changes for your hardware &mdash; the kernel &mdash; is exactly the part Armbian engineers.

### Wireless and networking that just work

Many SBC and USB **Wi-Fi and Bluetooth** chips are not supported by the stock Debian or Ubuntu kernel &mdash; elsewhere you would track down an out-of-tree driver and rebuild it as a DKMS module on every kernel update. Armbian **builds a large set of these wireless drivers straight into its kernels**, keeps them **ported and aligned with each new kernel release**, and **tests them on real hardware** ([Wi-Fi performance](../status/wifi-performance.md)) &mdash; so an adapter that needs manual driver-building elsewhere simply works. Armbian also makes sure its kernels carry the **full networking feature set of a desktop-class distribution** &mdash; netfilter/NAT, bridging, VLANs, IP tunnels and policy routing &mdash; which the board's vendor or minimal SBC kernels frequently strip out, so an SBC can act as a router, gateway or VPN endpoint out of the box.

### Optimized before you even log in

Armbian ships an OS that is **tuned for SBCs and flash media**: images are compacted to real size and **expand across the boot media at first boot**, `/var/log` runs on compressed zram with periodic write-back, half of RAM is available as compressed zswap, the I/O scheduler and journal are tuned, and the system runs almost read-only &mdash; **one of the fastest Linux options on many boards**. Full list in [key features](../index.md#key-features).

### Configuration made for embedded, in one tool

[`armbian-config`](../config/index.md) is a menu-driven utility for the tasks SBC users actually do &mdash; kernels, storage, network, access, localisation and one-click [software installs](../software/index.md) &mdash; and it is **unit-tested daily** ([CI](https://github.com/armbian/configng/actions/workflows/maintenance-unit-tests.yml)).

### Continuously validated on real hardware

This is where SBCs are usually left behind, and it is one of Armbian's biggest differentiators: mainstream distributions do **no per-board hardware validation** for the long tail of single-board computers. Armbian runs a **[dedicated autotest fleet](../status/board-tests.md)** where every board is put through a **nightly pipeline** — a distribution **upgrade**, a **reboot**, hardware **performance** and **DVFS** checks and a **network** throughput test — with the **[current pass/fail results published live](../status/board-tests.md)**, alongside real-hardware **[Wi-Fi performance](../status/wifi-performance.md)** measurements. It is not a promise in a wiki; it is measured on actual boards, every day.

### Backed by people and rules

Every official stable build is **thoroughly tested**, maintained by named **[per-board maintainers](https://www.armbian.com/authors)**, under clear [Board Support Rules](/contribute/board-support-rules/) that distinguish Standard Support from Community maintained. Armbian images are also a **direct base for many third-party builders**.

### Grow from user to builder

The same [build framework](https://github.com/armbian/build) that produces official images is yours to use: assemble **fully configured custom images** for your board or product, in parallel, under Docker &mdash; ideal for manufacturers, integrators and CI automation.

### Delivered everywhere

A [global network of mirrors](../status/mirrors.md) provides **perfect coverage, including mainland China**, so images and updates reach your fleet wherever it runs. Every image is also offered as a **torrent that pulls from all mirrors at once** &mdash; so instead of being throttled by a single server, downloads **saturate your own connection** and finish as fast as your line allows.

### Not just SBCs: cloud-optimized UEFI images

Armbian also builds **generic UEFI images for x86-64 and arm64** &mdash; lean, cloud-ready builds of the same Debian or Ubuntu user space. We **run our own cloud and build infrastructure on them** &mdash; including the project's x86-64 and arm64 cloud servers on **[netcup](https://www.netcup.de/)** &mdash; and they go through the [same nightly hardware test fleet](../status/board-tests.md) as the boards, so the images you would deploy are the images the project depends on itself.

## When each one is the right choice

- **Use Armbian** wherever you want its optimized kernels, tuning, [`armbian-config`](../config/index.md) and daily testing on top of a familiar Debian or Ubuntu user space:
    - **ARM or RISC-V single-board computers** &mdash; especially anything beyond the most common few boards.
    - **x86-64 and arm64 machines** &mdash; laptops, desktops, servers and cloud VMs, via Armbian's UEFI images. It is the same optimized-kernel and tuning treatment, so a fresh install often runs **leaner and faster than a stock Debian or Ubuntu** on the very same hardware &mdash; your next laptop included.
- **Use Debian or Ubuntu directly** only when you specifically want the vanilla distribution with no Armbian layer, or a distribution feature Armbian does not carry.

New here? Continue with [Getting Started](index.md) and [Choosing an image](choosing-an-image.md), or head straight to the [downloads](https://www.armbian.com/download/).
