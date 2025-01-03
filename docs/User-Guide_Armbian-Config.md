# Armbian Config

``` mermaid
flowchart LR
  A[armbian-config] -----> B["System"];
  A[armbian-config] -----> C["Network"];
  A[armbian-config] -----> D["Localistation"];
  A[armbian-config] -----> E["Software"];
  A[armbian-config] -----> F["Help"];
```

<img src="https://raw.githubusercontent.com/armbian/configng/main/share/icons/hicolor/scalable/configng-tux.svg">

Utility for configuring your board, adjusting services, and installing applications. It comes with Armbian by default.

To start the Armbian configuration utility, use the following command:
~~~
armbian-config
~~~

## Adding a new feature

Please check [instructions](/Contribute/Armbian-config/).

## Sources

<https://github.com/armbian/configng>

## Installation on 3rd party Linux OS

This tool is tailored to works best with Armbian Linux but it has also been automatically tested on:

- Debian Bookworm
- Ubuntu Jammy
- Ubuntu Noble

In theory it should work on any systemd APT based Linux distributions such as: Linux Mint, Elementary OS, Kali Linux, MX Linux, Parrot OS, Proxmox, Raspberry Pi OS, ...

~~~
echo "deb [signed-by=/usr/share/keyrings/armbian.gpg] \
https://github.armbian.com/configng stable main" | \
sudo tee /etc/apt/sources.list.d/armbian-development.list > /dev/null
sudo apt update
sudo apt -y install armbian-config
~~~
