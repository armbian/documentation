# Armbian Software

**Lightweight, Secure, and Optimized Services for Embedded Systems**

## Overview

**Armbian Software**, accessible via the `armbian-config` utility, empowers you to quickly deploy a variety of **preconfigured applications and advanced services** — from diagnostic tools and media servers to dashboards and container orchestration platforms. Most services are offered as **Docker containers** optimized specifically for Armbian OS and supported hardware, while a subset is available as **native installations** for lightweight or performance-critical setups.

## Installation & Maintenance

Each installation is isolated and designed with **clean setup and teardown** in mind. Key features include:

- **One-command installs** with sensible defaults  
- **No leftover files or dangling containers** after uninstallation  
- **Service isolation** via Docker networks and volume mappings  
- **Support for both manual and automatic updates**, [including container image refresh](/User-Guide_Armbian-Config/System/#docker-images)
- Daily-tested [CI pipelines](https://github.com/armbian/configng/actions/workflows/unit-tests.yml) ensure that software definitions remain reliable and compatible with the latest system changes  

All configurations are streamlined to work **out of the box**, reducing the need for manual intervention or deep technical know-how.

## Security and Management

Every service runs on a **dedicated Docker network bridge**, isolating app traffic for **enhanced security** and performance. Key management benefits include:

- Optional automatic restart and image updates  
- Native logging integration with `journalctl` or Docker logs  
- Clean rollbacks and easy troubleshooting  
- Support for encrypted volumes and HTTPS reverse proxies

These features make the platform suitable for both **prototyping** and **long-term deployments**. However, a few specific services — typically those requiring low-level hardware access or advanced networking features — may still need to run directly on the host network rather than within an isolated Docker bridge.

## Hardware Support

| Architecture | Support Level | Notes |
|--------------|----------------|-------|
| x86_64       | ✅ Full         | Ideal for servers, mini PCs |
| ARM64        | ✅ Full         | Ideal for servers and SBCs |
| ARMHF        | ⚠️ Partial      | Limited by upstream container support |
| RISCV64      | ⚠️ Partial      | Experimental, growing ecosystem |

Installations may include hardware specific tuning for optimal performance.

## Why Use It

- 🚀 **One-click deployments** of popular, containerized apps  
- 🔒 **Curated, tested, and secure** software maintained by the Armbian community  
- 🔁 **Clean installs and easy removal** — no system clutter or dependency hell  
- 📦 **Optimized for Armbian-supported hardware**, with fine-tuned configurations  
- ⚙️ **Minimal overhead**, ideal for embedded, headless, or remote systems  
- 🛠️ **Easy maintenance** with integrated update and monitoring tools  
- 🌐 **Internet-ready services**, including reverse proxies and network bridges
