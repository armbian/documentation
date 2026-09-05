---
seo_title: "Update & upgrade Armbian"
description: "Apply OS updates and run Debian and Ubuntu distribution upgrades on Armbian single-board computers with the armbian-config utility."
comments: true
---

# OS Updates


OS updates and distribution upgrades

## Firmware


Enable Armbian firmware upgrades


<!--- section image START from tools/include/images/UPD001.png --->
![Firmware](/images/UPD001.png)
<!--- section image STOP from tools/include/images/UPD001.png --->


<!--- header START from tools/include/markdown/UPD001-header.md --->
**Enable Armbian firmware upgrades** manages whether the Armbian firmware (kernel + u-boot + firmware) packages are held or unheld in the package manager. By removing or setting the hold, it controls if firmware updates are applied automatically through regular `apt update` and `apt upgrade` processes. This allows users to either freeze the firmware version for stability or enable updates for improved hardware support.

<!--- header STOP from tools/include/markdown/UPD001-header.md --->


~~~ bash title="Firmware"
armbian-config --cmd UPD001
~~~


~~~ bash title="Disable Armbian firmware upgrades"
armbian-config --cmd UPD002
~~~



## Rolling


Switch system to rolling packages repository


<!--- header START from tools/include/markdown/ROLLIN-header.md --->
The daily rolling repository offers frequently updated packages directly from development branches. It provides access to the latest features, bug fixes, and hardware support improvements but may introduce instability or regressions. This channel is intended for testing, development, and users who need the newest updates at the cost of reduced stability.

<!--- header STOP from tools/include/markdown/ROLLIN-header.md --->


~~~ bash title="Rolling"
armbian-config --cmd ROLLIN
~~~


## Stable


Switch system to stable packages repository


<!--- header START from tools/include/markdown/STABLE-header.md --->
The stable repository provides thoroughly tested packages intended for production use. Updates from this channel prioritize stability, long-term reliability, and minimal risk, ensuring systems remain secure and operational without unexpected changes. Only critical bug fixes and essential improvements are introduced after extensive testing.

<!--- header STOP from tools/include/markdown/STABLE-header.md --->


~~~ bash title="Stable"
armbian-config --cmd STABLE
~~~


## Stable Distro Upgrade


Distribution upgrade to latest stable / LTS


<!--- header START from tools/include/markdown/STD001-header.md --->
Stable / LTS upgrades move your system to a newer release of Debian or Ubuntu, bringing updated system packages along with long-term security fixes and bug patches. This makes them the safest choice for reliable, everyday use.

!!! Warning "Risks of Stable Upgrades"

    Distribution upgrades are experimental and **not supported by Armbian**. Use at your own risk.

    Even LTS → LTS upgrades (e.g., **Debian Bookworm → Trixie**, **Ubuntu Jammy → Noble**) carry some risks:

    - **Broken dependencies** – some packages may fail to upgrade or be removed.  
    - **Configuration overrides** – local changes may be replaced by defaults.  
    - **Downtime** – failed upgrades may require console access, manual recovery, or a full reinstall.  

    Because Armbian integrates upstream Debian/Ubuntu with custom board support packages, upgrades may still trigger **unexpected breakage** on some devices.  

<!--- header STOP from tools/include/markdown/STD001-header.md --->


~~~ bash title="Stable Distro Upgrade"
armbian-config --cmd STD001
~~~


<!--- footer START from tools/include/markdown/STD001-footer.md --->
Best Practices

1. **Back up your data** (system and configuration).  
2. **Test on a spare device or SD card** before upgrading production systems.  
3. **Read the official release notes** of your target distribution:  
- [Armbian FAQ: Can I upgrade my userspace flavor?](/User-Guide_FAQ/#can-i-upgrade-my-userspace-flavor-like-bullseye-to-bookworm-or-jammy-to-noble)  
- [Debian upgrade notes](https://www.debian.org/releases/trixie/release-notes/upgrading.en.html)  
- [Ubuntu release upgrade guide](https://documentation.ubuntu.com/server/how-to/software/upgrade-your-release/)  
4. **Ensure you have console access** (serial, HDMI + keyboard, SSH).  
5. **Consider fresh installs** if uptime and stability matter more than keeping the old environment.  

<!--- footer STOP from tools/include/markdown/STD001-footer.md --->


## Unstable Distro Upgrade


Distribution upgrade to rolling unstable


<!--- header START from tools/include/markdown/UNS001-header.md --->
Non-LTS releases are intended for **developers, testers, and enthusiasts** who want the latest features — **not for production systems**.  

!!! Warning "Risks of Unstable Upgrades"

    Distribution upgrades are experimental and **not supported by Armbian**. Use at your own risk.

    - **High chance of breakage** – dependencies, bootloader, or kernel may fail.  
    - **Short lifecycle** – requires frequent re-upgrades (every ~6–9 months).  
    - **Unfinished features** – packages may be experimental or not fully supported.  
    - **Armbian compatibility** – integration with board support packages is less tested.  

<!--- header STOP from tools/include/markdown/UNS001-header.md --->


~~~ bash title="Unstable Distro Upgrade"
armbian-config --cmd UNS001
~~~


## Docker images


Enable automating Docker container base images updating


<!--- section image START from tools/include/images/WTC001.png --->
![Docker images](/images/WTC001.png)
<!--- section image STOP from tools/include/images/WTC001.png --->


<!--- header START from tools/include/markdown/WTC001-header.md --->
Watchtower is a lightweight tool that automatically monitors and updates running Docker containers whenever a new image version becomes available.
It checks remote registries for updated images, pulls them, stops the old containers, and restarts them using the updated versions — all without manual intervention.
Watchtower is fully configurable, allowing you to control update frequency, select specific containers, and manage notification settings.

<!--- header STOP from tools/include/markdown/WTC001-header.md --->


~~~ bash title="Docker images"
armbian-config --cmd WTC001
~~~


~~~ bash title="Disable automating Docker container base images updating"
armbian-config --cmd WTC002
~~~



## Packages


Enable automatic package updates.


<!--- section image START from tools/include/images/UNAT01.png --->
![Packages](/images/UNAT01.png)
<!--- section image STOP from tools/include/images/UNAT01.png --->


<!--- header START from tools/include/markdown/UNAT01-header.md --->
Unattended upgrades automatically install security updates and important package updates on your system without requiring manual intervention. It helps keep your system secure, stable, and up-to-date by silently applying patches. The behavior is fully configurable — you can control which packages are upgraded, set reboot options, and customize notifications or logging.

<!--- header STOP from tools/include/markdown/UNAT01-header.md --->


~~~ bash title="Packages"
armbian-config --cmd UNAT01
~~~


~~~ bash title="Configure automatic package updates"
armbian-config --cmd UNAT02
~~~


~~~ bash title="Disable automatic package updates"
armbian-config --cmd UNAT03
~~~



