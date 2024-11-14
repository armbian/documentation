# Armbian Build Framework Quick Start Guide

## Requirements

- x86_64 / aarch64 / riscv64 machine
- at least 4GB of memory and ~50GB of disk space for VM, container or bare metal installation
- **Armbian / Ubuntu Jammy 22.04.x** for native building or any Docker capable Linux for containerised
- **Windows 10/11 with WSL2 subsystem** running Armbian / Ubuntu Jammy 22.04.x
- Superuser rights (configured sudo or root access).
- Make sure your system is up-to-date! Outdated Docker binaries, for example, can cause trouble


## Clone repository

```bash
git clone https://github.com/armbian/build
cd build  
```
!!! note
    - Make sure that full path to the build script **does not contain spaces**
    - For stable branch use `--branch=v24.11`


## Interactive

Run framework:

```bash
./compile.sh
```

??? info "Video"
    <iframe width="939" height="529" src="https://www.youtube.com/embed/kQcEFsXEJEE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## CLI


[Comprehensive list of build Options](Developer-Guide_Build-Options.md)

Example:

```bash
./compile.sh build \
BOARD=uefi-x86 \
BRANCH=current \
BUILD_DESKTOP=yes \
BUILD_MINIMAL=no \
DESKTOP_APPGROUPS_SELECTED='browsers chat desktop_tools' \
DESKTOP_ENVIRONMENT=gnome \
DESKTOP_ENVIRONMENT_CONFIG_NAME=config_base \
KERNEL_CONFIGURE=no \
RELEASE=noble
```

!!! question "Interpretation?"

    This command will generate **Ubuntu 24.04 Noble** based **Gnome desktop** environment image for Intel based hardware (**uefi-x86**). Besides bare desktop, it will contain packages from **browsers** and **desktop_tool** sections and it will use unchanged kernel from **current kernel** branch.


## GitHub actions

If you do not own the proper equipment to build images on your own, you can use our [GitHub action](https://github.com/marketplace/actions/rebuild-armbian).