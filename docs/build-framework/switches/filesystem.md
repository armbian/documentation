---
seo_title: "Armbian filesystem & image build switches"
description: "Root filesystem type, Btrfs options, LUKS encryption, partition sizes and labels, sector size and image compression for the Armbian build."
---

# Filesystem & image

Root filesystem type, encryption, partition sizes and labels, and how the finished image is compressed.

## Root filesystem

#### ROOTFS_TYPE

`string` · default: `ext4`

- `ext4` (default)
- `f2fs`
- `btrfs`
- `nilfs2`
- `xfs`
- `nfs`

Create image with different root filesystems instead of default `ext4`. Requires setting `FIXED_IMAGE_SIZE` to something smaller than the size of your SD card for `F2FS`

#### BTRFS_CHECKSUM

`string`

- `crc32c`
- `xxhash`
- `sha256`
- `blake2`

Override the default `btrfs` filesystem [checksum algorithm](https://btrfs.readthedocs.io/en/stable/Checksumming.html).  If `BTRFS_CHECKSUM` is unspecified, the checksum is chosen automatically by `mkfs.btrfs`, which currently defaults to `crc32c`.

!!! tip "Tip"

    Choose `BTRFS_CHECKSUM=blake2` for better error detection at the cost of increased CPU usage.

#### BTRFS_COMPRESSION

`string` · default: `zlib`

- `lzo`
- `none`
- `zlib` (default)
- `zstd`

When choosing `ROOTFS_TYPE=btrfs`, select `btrfs` filesystem compression method and compression level. By default, the compression is `zlib`.

!!! tip "Note"

    The script does not check the legality of the input variable (compression ratio). Input like `zlib:1234` is legal to the script but illegal to the kernel. Beware that setting this option does affect image creation only (shrinking disk size) and will not adjust `/etc/fstab`, so it is up to the user to later edit `/etc/fstab` if compression in daily operation is also wanted (beware of severe performance penalties with random IO patterns and heavy compression algorithms!).

#### BTRFS_ROOT_SUBVOLUME

`string`

When using a BTRFS image as a file system, the volume `/` is placed on
btrfs subvolume `@`. The same subvolume is set as default for mounting without
specifying the `subvol=@` option at the time the image is mounted.

Using `BTRFS_ROOT_SUBVOLUME`, you can set a different name for the
root filesystem subvolume:

```sh
./compile.sh ROOTFS_TYPE=btrfs BTRFS_ROOT_SUBVOLUME=@root
```

#### CRYPTROOT_ENABLE

`string`

- yes
- no

LUKS (Linux Unified Key Setup) is a specification for block device encryption. It establishes an on-disk format for the data, as well as a passphrase/key management policy. LUKS uses the kernel device mapper subsystem via the dm-crypt module.

```title="When enabled, you need to provide additional information:"
CRYPTROOT_PASSPHRASE="MYSECRECTPASS"             # Mandatory
CRYPTROOT_AUTOUNLOCK="yes"                       # Default: no. If set to yes you can omit CRYPTROOT_PASSPHRASE to do unattended unlocking
CRYPTROOT_SSH_UNLOCK="yes"                       # Default: yes
CRYPTROOT_SSH_UNLOCK_PORT="2222"                 # Default: 2022
CRYPTROOT_MAPPER=armbian-root                   # Default: armbian-root
CRYPTROOT_PARAMETERS="custom cryptsetup options" # Default: --pbkdf pbkdf2
```

!!! tip "Tips and warnings"

    - Private key can be placed in `$USERPATCHES_PATH/dropbear_authorized_keys` or they will be generated in `output/images/*.key` file
    - If you want to do the encryption part from scratch, check out [this](https://forum.armbian.com/topic/15618-full-root-filesystem%C2%A0encryption%C2%A0on-an-armbian-system-new-replaces-2017-tutorial-on-this-topic/) forum post.
    - This function might not work well with all distributions.
    - CRYPTROOT_MAPPER name might affect parallel image building
    - CRYPTROOT_PARAMETERS may not contain `=`; separate switches with spaces
    - CRYPTROOT_AUTOUNLOCK stores encryption key in the /etc/rootfs.key

## Partitions, sizes and labels

#### SECTOR_SIZE

`value`

- `512` (default, for SD/EMMC/...)
- `4096` (for UFS, requires util-linux >2.41. Tested on Debian Trixie host)

Logical sector size the build passes to `sfdisk --sector-size` and to `losetup -b` when partitioning and attaching the raw image, so the partition table is aligned for the target media. Leave it at `512`, which suits SD cards, eMMC and most storage; set `4096` only for UFS-based devices, which expose 4K sectors and need a host with util-linux newer than 2.41.

#### UEFISIZE

`integer` (MiB) · default: `0`

Size in MiB of the UEFI/ESP (EFI System Partition) that carries the bootloader on UEFI-booting targets such as x86 and some ARM64 boards; `0` disables it, which is the default because most Armbian boards boot from U-Boot rather than UEFI. Set a size (typically 256) for UEFI images. Do not combine `UEFISIZE>0` with `BOOTSIZE>0` — the two describe mutually exclusive boot layouts.

#### BIOSSIZE

`integer` (MiB) · default: `0`

Size in MiB of a small legacy BIOS boot partition, needed only when a GPT-partitioned image must also boot on old BIOS/CSM x86 firmware so GRUB has somewhere to embed its core. It defaults to `0` (no such partition), since most images target either UEFI or ARM boards that do not need it. A non-zero value is rejected on MBR partition tables, where it has no meaning.

#### BOOTSIZE

`integer` · default: `256` (when a separate `/boot` is required)

Size in MB of a separate `/boot` partition, created when the root filesystem cannot hold the boot files itself — typically when `ROOTFS_TYPE` is something other than `ext4` (btrfs, f2fs, nilfs2, and so on) or a board otherwise requires a dedicated boot partition. Individual board configs override it where their bootloader needs more room, and the partitioning step falls back to a 256 MB default if a boot partition is required but the value is left empty or unusably small. Leave it alone unless you know the target needs a larger `/boot`.

#### FIXED_IMAGE_SIZE

`integer`

Forces the output image to a fixed size in megabytes instead of the default behaviour, where the build makes the image just large enough to hold the root filesystem. Set it when you need a predictable image size — for example to fit a specific card, to leave free space for later growth, or because a filesystem such as f2fs requires a pre-sized image and the build will refuse to continue without it.

#### BOOT_FS_LABEL

`string` · default: `armbi_boot`

Filesystem label written to the separate `/boot` partition when one is created, used so `/etc/fstab` and boot scripts can refer to it by a stable name rather than a shifting device node. The default `armbi_boot` is fine for almost every build; override it only when a board's bootloader or an external tool expects a particular label.

#### ROOT_FS_LABEL

`string` · default: `armbi_root`

Filesystem label written to the root partition, letting the system and the kernel command line locate root by label (`root=LABEL=...`) rather than by a device path that can change between boards and adapters. The default `armbi_root` suits standard builds; change it only when something downstream keys off a specific root label.

#### UEFI_FS_LABEL

`string` · default: `armbi_efi`

Filesystem label for the FAT32 EFI System Partition. The build forces it to uppercase before running `mkfs.fat`, as FAT32 volume labels are case-insensitive and conventionally uppercase, so a value like `armbi_efi` appears as `ARMBI_EFI`. Override it when the partition should show a specific name — this is the label Windows or macOS users see if they mount the card.

#### UEFI_MOUNT_POINT

`string` · default: `/boot/efi`

Directory where the EFI System Partition is mounted inside the image, and the path written into `/etc/fstab`. The default `/boot/efi` follows the usual Linux convention; some families override it, for example Raspberry Pi mounts it at `/boot/firmware` where its bootloader and config live. Change it only to match a board's expected firmware layout.

#### UEFI_MOUNT_POINT_SKIP_FSTAB

`string` · default: `no`

Controls whether the EFI partition gets an active `/etc/fstab` entry. Left at `no`, the partition is mounted normally at boot; set `yes` and the build writes the same line commented out instead, so the EFI partition is not auto-mounted. Use it for boards or firmware that access the ESP directly and would be disturbed by it being mounted, or where you want to manage that mount yourself.

#### CHECK_LOOP_FOR_SIZE

`string` · default: `yes`

Guards against a race where the kernel has not yet reported the loop device's real size after it is attached, which can lead to a truncated or corrupt image. Left at the default `yes`, the build waits and checks the loop device reports the expected size before continuing. Set `no` only to work around a host where the check misbehaves, understanding you lose that safety net.

#### FORCE_BOOTSCRIPT_UPDATE

`string`

- yes | no

- yes: force bootscript to get updated during bsp package upgrade

Normally the boot script (`boot.cmd`/`boot.scr`) is treated as user-editable and left alone once installed, so a board-support package upgrade does not clobber local boot changes. Set `yes` to force the BSP package to overwrite it on every upgrade instead — used by boards where the boot script must always track the packaged version. Several board configs set this themselves; leave it unset unless you specifically need that behaviour.

## Image compression

#### SKIP_COMPRESSING

`comma/space-separated list of file extensions`

- e.g. `iso,qcow2`: leave images of these formats uncompressed even when `COMPRESS_OUTPUTIMAGE` enables `xz`/`zstd`
- empty: (default) compress everything

A global, comma- or space-separated list of image file extensions to leave uncompressed even when `COMPRESS_OUTPUTIMAGE` requests `xz` or `zstd`. It is empty by default, so every produced image is compressed. Images matched here are still checksummed when `COMPRESS_OUTPUTIMAGE` includes `sha`; only the compression step is skipped. Use it for formats consumed as-is — `qcow2` imported straight into a hypervisor, or `iso` mounted as a virtual CD — where compression would only add a pointless decompress step for the end user.

#### COMPRESS_OUTPUTIMAGE

`comma-separated list`

Selects the post-processing applied to the finished image for redistribution — checksums, a GPG signature and/or a compressed archive — as a comma-separated list of the tokens below. If it is left empty (or `no`), the build falls back to `sha,img`, producing a plain uncompressed image with a SHA256 checksum. Add `xz` or `zstd` to ship a compressed image, and `gpg` to sign it; the two nested ratio switches tune how hard each compressor works.

- sha: generate SHA256 hash for image
- gpg: sign image using gpg
- xz: compress image only using xz format
  - **IMAGE_XZ_COMPRESSION_RATIO** ( 0 - **1** - 9 ) images compression levels when using xz compressor. Beware of memory consumption when going higher
- zstd: compress image only using zstd format
  - **ZSTD_COMPRESSION_LEVEL** ( 1 - **9** - 19 ) images compression levels when using zstd compressor. Beware of memory consumption when going higher

#### IMAGE_XZ_MEMLIMIT

`string` · default: ~10GiB

Hard memory ceiling handed to `xz --memlimit-compress` when compressing the image, a backstop that makes the encoder scale its own thread count down rather than risk an out-of-memory kill on a busy or small host. By default the build uses about 10 GiB, automatically lowered to the memory actually available when the host has less. Set an explicit value such as `4GiB` to cap it further on constrained machines, or raise it if you have plenty of RAM and want xz to parallelise more aggressively.

#### ROOTFS_COMPRESSION_RATIO

`integer` · default: `5`

zstd compression level applied when packing the root filesystem tarball. The default `5` is a fast, light setting suited to the throwaway rootfs produced during a normal build; when the build is instead generating the shared rootfs cache artifact it raises this to `15`, trading CPU time for a smaller cached download that many later builds reuse. Raise it for smaller local rootfs archives at the cost of build time, or lower it to speed builds up.

#### COMPRESS_MAX_THREADS

`integer` · default: `16`

Upper limit on how many threads xz/zstd may use when compressing the image and rootfs. The build normally uses as many threads as the host has, capped at `16`, because past that point extra threads give little wall-time gain while consuming a lot of memory. Lower it to leave CPU and RAM for other work, or raise it on a large, well-provisioned build host. A non-numeric or zero value is ignored and falls back to the default `16`.
