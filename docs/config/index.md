---
description: "armbian-config is the interactive, scriptable setup tool preinstalled on every Armbian image: configure networking, kernels, storage, users and software on your SBC."
---

# Armbian Config

**Armbian Config** (`armbian-config`) is a lightweight, **interactive and scriptable** configuration utility that automates the common tasks of setting up and maintaining an Armbian system. It ships **preinstalled** on every Armbian image and is especially handy on single-board computers (SBCs) — it gets you to a ready-to-use system without editing config files by hand.

## What it can do

- **Initial setup & personalization** — hostname, timezone, locales, keyboard, users, MOTD
- **Networking** — Wi-Fi, VPN, static IP, and advanced/bridged configurations
- **Kernel & firmware** — select, switch and manage kernels, headers, device-tree overlays and firmware
- **Hardware features** — enable and manage board-specific options
- **Storage** — install to internal media, ZFS, NFS, read-only root, and more
- **Software** — sandboxed installation of third-party applications and services, plus system and distribution updates
- **Desktop environments** — install and tier-manage XFCE, GNOME, KDE Plasma, MATE, Cinnamon and others

## Quick start

Open a terminal (locally or over SSH) and run:

~~~ bash
armbian-config
~~~

Every menu action can also be driven **non-interactively** for scripting and automation:

~~~ bash
armbian-config --cmd <ID>        # run a menu command
armbian-config --api <helper>    # call a module helper directly
~~~

## Compatibility

Armbian Config is optimized for **[Armbian Linux](https://www.armbian.com)**, but in theory it works on any systemd-based, APT-compatible distribution — Linux Mint, Elementary OS, Kali Linux, MX Linux, Parrot OS, Proxmox, Raspberry Pi OS, and others. It is continuously and automatically tested on current versions of Debian and Ubuntu.

<details><summary>Install on a non-Armbian distribution</summary>

~~~ bash
wget -qO - https://apt.armbian.com/armbian.key | gpg --dearmor | \
sudo tee /usr/share/keyrings/armbian.gpg > /dev/null
cat << EOF | sudo tee /etc/apt/sources.list.d/armbian-config.sources > /dev/null
Types: deb
URIs: https://github.armbian.com/configng
Suites: stable
Components: main
Signed-By: /usr/share/keyrings/armbian.gpg
EOF
sudo apt update
sudo apt -y install armbian-config
~~~
</details>

## Contribute

Want to expand Armbian Config with a new feature, software title, or configuration module? Contributions are welcome — see the [contribution guide](/Contribute/Armbian-config/). Keep changes modular and easy to maintain, so they are quick to review and merge.

## Sources

<https://github.com/armbian/configng>
