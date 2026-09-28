---
seo_title: "Test an Armbian image with QEMU"
description: "Run Armbian under QEMU without hardware: the qemu-uefi-x86, qemu-uboot-x86 and qemu-uboot-arm64 board targets, and running a uefi-x86 cloud image directly."
---

# Testing an image with QEMU

`armbian/build` ships three board targets built specifically to run under QEMU. All three are
[Community maintained](/contribute/board-support-rules/#community-maintained): they get no
guaranteed support and can change or disappear. The generic x86_64 target (`uefi-x86`, Standard
support) also happens to boot under QEMU with the `ovmf` UEFI firmware package, since it's a
regular UEFI PC image.

| Board | Arch | Boot path |
|---|---|---|
| [`qemu-uefi-x86`](https://github.com/armbian/build/blob/main/config/boards/qemu-uefi-x86.csc) | x86_64 | UEFI via GRUB and OVMF firmware — same disk layout as the real `uefi-x86` target, with kernel/console output tuned for a VM |
| [`qemu-uboot-x86`](https://github.com/armbian/build/blob/main/config/boards/qemu-uboot-x86.csc) | x86_64 | U-Boot (`u-boot.rom`), no GRUB |
| [`qemu-uboot-arm64`](https://github.com/armbian/build/blob/main/config/boards/qemu-uboot-arm64.csc) | arm64 | U-Boot (`u-boot.bin`), QEMU `virt` machine |

None of these are published on the [download page](https://www.armbian.com/download/); build
one yourself, for example:

```bash
./compile.sh build BOARD=qemu-uboot-x86 BRANCH=current RELEASE=trixie
```

The image (`<version>.img.qcow2`) is written to `output/images/`. The two U-Boot boards also
export their firmware next to it — `<version>.u-boot.rom` (x86) or `<version>.u-boot.bin`
(arm64) — which QEMU needs as `-bios`.

## Running

### qemu-uboot-x86 (U-Boot, x86_64)

On Linux, with KVM:

```bash
qemu-system-x86_64 -accel kvm -machine q35,vmport=off -smp 8 -nographic \
  -bios <version>.u-boot.rom -m 2048 -nic user,model=virtio-net-pci \
  -device virtio-blk-pci,drive=drive0,bootindex=0 \
  -drive if=none,media=disk,id=drive0,file=<version>.img.qcow2,discard=unmap,detect-zeroes=unmap
```

On macOS, drop `-accel kvm` — there is none, and `-accel hvf` doesn't work here (U-Boot hangs), so this falls back to plain software emulation:

```bash
qemu-system-x86_64 -machine q35,vmport=off -smp 8 -nographic \
  -bios <version>.u-boot.rom -m 2048 -nic user,model=virtio-net-pci \
  -device virtio-blk-pci,drive=drive0,bootindex=0 \
  -drive if=none,media=disk,id=drive0,file=<version>.img.qcow2,discard=unmap,detect-zeroes=unmap
```

### qemu-uboot-arm64 (U-Boot, arm64)

```bash
qemu-system-aarch64 -m 2048 -machine virt -nographic -cpu cortex-a72 \
  -bios <version>.u-boot.bin -nic user,model=virtio-net-pci \
  -drive if=none,media=disk,id=drive0,file=<version>.img.qcow2,discard=unmap,detect-zeroes=unmap \
  -device virtio-blk-pci,drive=drive0,bootindex=0
```

Add `-accel kvm` on an arm64 host that supports it.

### uefi-x86 / qemu-uefi-x86 (UEFI, x86_64)

This is the path for a `uefi-x86` **cloud** image from the [download page](https://www.armbian.com/download/)
(filenames look like `Armbian_<version>_Uefi-x86_<release>_cloud_<kernel>_minimal.img.qcow2`) or
a `qemu-uefi-x86` build — no U-Boot export here, it boots through the standard `ovmf` UEFI
firmware package instead:

```bash
sudo apt install ovmf qemu-system-x86
```

```bash
qemu-system-x86_64 -bios /usr/share/ovmf/OVMF.fd -m 2048 \
  -display gtk,gl=on \
  -device virtio-net,netdev=net0 -netdev user,id=net0,hostfwd=tcp::5800-:22 \
  -drive if=none,id=root,file=<image>.qcow2,format=qcow2 \
  -device virtio-blk,drive=root
```

`-display gtk,gl=on` opens a local window; use `-display none` or `-nographic` on a headless
host instead. `-netdev user,...,hostfwd=tcp::5800-:22` forwards the guest's SSH port to port
5800 on the host — pick any free host port.

## Logging in

Same defaults as [first boot on real hardware](/getting-started/first-boot-and-login/): log in
on the console as **root** / **1234**, or once networking is up:

```bash
ssh -p 5800 root@localhost
```

---

Reference: [board configuration](/build-framework/board-configuration/), [board support rules](/contribute/board-support-rules/).
