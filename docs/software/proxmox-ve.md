---
title: "Proxmox VE"
description: "Install and run Proxmox VE on Armbian — Proxmox VE virtualization platform (keeps the Armbian kernel). Runs on ARM64 and x86 single-board computers."
image: /images/PVE001.png
category: "Management"
comments: true
---
# Proxmox VE


<!--- section image START from tools/include/images/PVE001.png --->
![Proxmox VE](/images/PVE001.png){ .app-logo }
<!--- section image STOP from tools/include/images/PVE001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://pve.proxmox.com/wiki/Install_Proxmox_VE_on_Debian_13_Trixie) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8006`


<!--- header START from tools/include/markdown/PVE001-header.md --->
[Proxmox VE](https://www.proxmox.com/en/proxmox-virtual-environment) is a complete, open-source server virtualization platform for running **KVM virtual machines** and **LXC containers** from a single, integrated web interface. It combines the tooling for compute, storage and software-defined networking so you can manage a whole host — or a cluster of them — from your browser.

This module installs Proxmox VE 9 from the official *no-subscription* repository on **Debian 13 (trixie)**, on both **amd64 and arm64**, and — unlike the upstream guide — **keeps the running Armbian kernel** instead of pulling the Proxmox one.

*Key Features*

- **KVM virtual machines**: Full hardware-accelerated VMs via the board's KVM-enabled Armbian kernel.
- **LXC containers**: Lightweight, fast system containers alongside your VMs.
- **Web management**: Manage guests, storage, backups and networking from `https://<ip>:8006`.
- **ZFS storage**: Installs ZFS (via DKMS, built against the Armbian kernel) so you can create ZFS pools and datasets for VM/container storage.
- **Keeps your kernel**: Installs `pve-manager` (no kernel dependency) rather than the `proxmox-ve` meta, so your Armbian kernel and DTBs stay in place.
- **No subscription needed**: Uses the public `pve-no-subscription` repository.

---

Ideal for turning an Armbian board into a lightweight hypervisor without giving up the board's own kernel and hardware support.

<!--- header STOP from tools/include/markdown/PVE001-header.md --->


Install from **[armbian-config](/armbian-config/) → Software → Management → Proxmox VE**

~~~ custombash title="CLI install"
armbian-config --cmd PVE001
~~~


<!--- footer START from tools/include/markdown/PVE001-footer.md --->
=== "Access to the web interface"

    - Username: `root` (your system root password)

    Official documentation: <https://pve.proxmox.com/pve-docs/>

=== "Runs on the Armbian kernel"

    This install intentionally omits the Proxmox kernel and runs on the board's
    Armbian kernel:

    - KVM virtual machines and LXC containers work provided the running kernel
      offers the needed support (KVM / `/dev/kvm` and container
      cgroups/namespaces) — which the Armbian kernels for these arches normally do.
    - This module **installs ZFS** for you (via DKMS, built against the Armbian
      kernel), so ZFS storage pools work out of the box; only ZFS-on-**root**
      (boot) is out of scope.

=== "Requirements"

    - **Armbian Trixie** (Debian 13) on **amd64** or **arm64** (enforced by the installer).
    - **Recommended:** the hostname should resolve to a non-loopback IP in
      `/etc/hosts`, e.g.:

        ```
        192.168.1.50   pve.local pve
        ```

        If it resolves only to a loopback address (`127.x` or IPv6 `::1`), the
        installer warns and lets you continue, but the web UI and clustering
        may not work until you fix `/etc/hosts`.

=== "Directories"

    - Configuration: `/etc/pve`
    - Cluster data: `/var/lib/pve-cluster`

<!--- footer STOP from tools/include/markdown/PVE001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_proxmox install` |
| Remove Proxmox VE | `armbian-config --api module_proxmox remove` |
| Purge Proxmox VE with cluster data | `armbian-config --api module_proxmox purge` |
| Status | `armbian-config --api module_proxmox status` |
| Help | `armbian-config --api module_proxmox help` |

---

_Part of Armbian's [Remote File & Management tools](/User-Guide_Armbian-Software/Management/) software._
