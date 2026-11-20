---
seo_title: "Test an Armbian image with QEMU"
description: "Run an Armbian image in QEMU without real hardware: a quick test of a ready-made UEFI cloud image, the QEMU board targets for images you build yourself, and how to log in over SSH."
---

# Testing with QEMU

You can try an Armbian image without a board. QEMU runs the image in a
virtual machine on your own computer, which is a quick way to check that
an image boots, has network, and accepts SSH before you flash it to real
hardware.

This page covers the two cases that come up most:

- a ready-made `uefi-x86` cloud image from the download page, run with
  UEFI firmware,
- an image you built yourself for one of the QEMU board targets, run
  with U-Boot firmware.

!!! note

    A QEMU test only proves the image itself works. It does not test
    real board hardware, board-specific drivers, or how the board boots
    from its own storage. Always test on the real board before you call
    an image good.

## What you need

- A Linux host. The commands below use Debian or Ubuntu.
- QEMU and, for the UEFI test, the OVMF firmware package.
- An Armbian image: either a downloaded `uefi-x86` cloud image, or an
  image you built for a QEMU board target.

## Quick test: a ready-made UEFI cloud image

### 1. Install QEMU and OVMF

```bash
sudo apt install ovmf qemu-system-x86
```

### 2. Download the image

Get the current `uefi-x86` cloud image from
[the UEFI x86 download page](https://www.armbian.com/uefi-x86/).
Pick the `cloud` file with the `qcow2` ending. The file names look like
this, with the version, release, and kernel changing over time:

```text
Armbian_<version>_Uefi-x86_<release>_cloud_<kernel>_minimal.img.qcow2
```

Use the file name you actually downloaded in the command below. Do not
copy a file name from an old example: names go stale with every release.

### 3. Run it

```bash
qemu-system-x86_64 \
  -bios /usr/share/ovmf/OVMF.fd \
  -m 2048 \
  -display gtk,gl=on \
  -device virtio-net,netdev=net0 \
  -netdev user,id=net0,hostfwd=tcp:127.0.0.1:5800-:22 \
  -drive if=none,id=root,file=./Armbian_<version>_Uefi-x86_<release>_cloud_<kernel>_minimal.img.qcow2,format=qcow2 \
  -device virtio-blk,drive=root
```

A QEMU window opens and the image boots, just like on real hardware.
When you are done, log in and run `poweroff`, or just close the window.

### What each switch does

- `-bios /usr/share/ovmf/OVMF.fd` boots the machine with UEFI firmware
  from the OVMF package. The cloud image needs UEFI, not the old BIOS
  boot.
- `-m 2048` gives the virtual machine 2048 MB of RAM.
- `-display gtk,gl=on` shows the guest screen in a GTK window, with
  OpenGL turned on.
- `-device virtio-net,netdev=net0` plugs in a fast virtio network card,
  connected to a network called `net0`.
- `-netdev user,id=net0,hostfwd=tcp:127.0.0.1:5800-:22` gives that network
  user-mode networking, and forwards port 5800 on your host to port 22
  (SSH) inside the guest. The `127.0.0.1` before the port binds the
  forward to your own computer only, so no other machine can reach the
  guest over SSH. That is how you reach the guest with SSH.
- `-drive if=none,id=root,file=...,format=qcow2` attaches your image
  file as a drive called `root`, and tells QEMU it is in qcow2 format.
- `-device virtio-blk,drive=root` plugs that drive into the machine as
  a fast virtio block device, so the guest can boot from it.

### Logging in

Log in on the graphical window, or over SSH from your host:

```bash
ssh -p 5800 root@127.0.0.1
```

The password is `1234`. First boot asks you to set a new root password
and create your own user account, the same as on real hardware. See
[First boot and login](/getting-started/first-boot-and-login/).

A login prompt on the graphical window only proves the image boots. The
quick test has passed only after you log in over SSH with the command
above: a successful SSH login proves the image boots, has network, and
accepts SSH.

## Test an image you built: the QEMU board targets

The build framework ships three board targets made for exactly this.
None of them are published on the download page, so build one yourself:

- `qemu-uefi-x86` boots with UEFI, like the cloud image above. Run it
  with the OVMF command from the previous section.
- `qemu-uboot-x86` boots through U-Boot on x86. The build also writes
  a `u-boot.rom` file next to the image, which QEMU uses as firmware
  with `-bios`.
- `qemu-uboot-arm64` boots through U-Boot on the ARM `virt` machine.
  The build writes a `u-boot.bin` file next to the image for the same
  purpose.

Build one like any other board, for example:

```bash
./compile.sh build BOARD=qemu-uboot-x86 BRANCH=current RELEASE=trixie ENABLE_EXTENSIONS=image-output-qcow2
```

Add `ENABLE_EXTENSIONS=image-output-qcow2` for all three targets.
Without it, the build writes only a raw `.img` file, and the `.img.qcow2`
file the QEMU commands below expect does not exist.

See [Getting started](/build-framework/getting-started/) for the full
build setup.

### U-Boot on x86

On Linux with KVM acceleration:

```bash
qemu-system-x86_64 -accel kvm -machine q35,vmport=off -smp 8 -nographic \
  -bios <version>.u-boot.rom -m 2048 \
  -nic user,model=virtio-net-pci \
  -device virtio-blk-pci,drive=drive0,bootindex=0 \
  -drive if=none,media=disk,id=drive0,file=<version>.img.qcow2,discard=unmap,detect-zeroes=unmap
```

Replace `<version>` with the version of the image you built. `-nographic`
means there is no window: the serial console runs in your terminal.
`-accel kvm` needs KVM on a Linux x86 host.

On macOS, drop `-accel kvm`. The macOS accelerator hangs U-Boot, so
plain emulation is used instead, which is slow but works:

```bash
qemu-system-x86_64 -machine q35,vmport=off -smp 8 -nographic \
  -bios <version>.u-boot.rom -m 2048 \
  -nic user,model=virtio-net-pci \
  -device virtio-blk-pci,drive=drive0,bootindex=0 \
  -drive if=none,media=disk,id=drive0,file=<version>.img.qcow2,discard=unmap,detect-zeroes=unmap
```

### U-Boot on ARM64

With virtio networking and storage:

```bash
qemu-system-aarch64 -m 2048 -machine virt -nographic -cpu cortex-a72 \
  -bios <version>.u-boot.bin \
  -nic user,model=virtio-net-pci \
  -drive if=none,media=disk,id=drive0,file=<version>.img.qcow2,discard=unmap,detect-zeroes=unmap \
  -device virtio-blk-pci,drive=drive0,bootindex=0
```

On a supported ARM64 host, try adding `-accel kvm` to the same command
for faster emulation. With an NVMe disk instead of virtio storage:

```bash
qemu-system-aarch64 -m 2048 -machine virt -nographic -cpu cortex-a57 \
  -bios <version>.u-boot.bin \
  -drive if=none,file=<version>.img.qcow2,id=armbian \
  -device nvme,drive=armbian,serial=serialnumber
```

Log in at the serial console in your terminal: `root` with password
`1234` on first boot, then set a new password when asked. These commands
forward no host port to the guest, so SSH from your host does not work
here.

## Other ways to test: Incus

Incus can also run the same qcow2 image as a virtual machine, if you
prefer it over QEMU. This page does not give an Incus recipe yet. See
the [Incus documentation](https://linuxcontainers.org/incus/docs/main/)
if you want to try it.

Producing your own qcow2 image from a build, and an automated check
that an image boots, has network, and accepts SSH, are follow-ups that
are not covered here yet.
