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
CRYPTROOT_MAPPER=armbian-root`                   # Default: armbian-root
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

Enforce sfdisk to align partition sector sizes.

#### UEFISIZE

`integer` (MiB) · default: `0`

Size of the UEFI/ESP partition; `0` = none.

#### BIOSSIZE

`integer` (MiB) · default: `0`

Size of the legacy BIOS boot partition on GPT; `0` = none.

#### BOOTSIZE

`integer` · default: `96`

Size in MB for a separate `/boot` filesystem. Used if `ROOTFS_TYPE` is set to non-ext4.

#### FIXED_IMAGE_SIZE

`integer`

Create an image file of this size (in megabytes) instead of minimal.

#### BOOT_FS_LABEL

`string` · default: `armbi_boot`

Filesystem label for the `/boot` partition.

#### ROOT_FS_LABEL

`string` · default: `armbi_root`

Filesystem label for the root partition.

#### UEFI_FS_LABEL

`string` · default: `armbi_efi`

Filesystem label for the EFI partition (uppercased for FAT32).

#### UEFI_MOUNT_POINT

`string` · default: `/boot/efi`

Mount point for the EFI partition.

#### UEFI_MOUNT_POINT_SKIP_FSTAB

`string` · default: `no`

Omit the EFI partition from `/etc/fstab` (comment it out instead).

#### CHECK_LOOP_FOR_SIZE

`string` · default: `yes`

Verify the loop device reports the correct size before writing the image.

#### FORCE_BOOTSCRIPT_UPDATE

`string`

- yes | no

- yes: force bootscript to get updated during bsp package upgrade

## Image compression

#### SKIP_COMPRESSING

`comma/space-separated list of file extensions`

- e.g. `iso,qcow2`: leave images of these formats uncompressed even when `COMPRESS_OUTPUTIMAGE` enables `xz`/`zstd`
- empty: (default) compress everything

Images left uncompressed are still checksummed when `COMPRESS_OUTPUTIMAGE` includes `sha`. Useful for formats consumed as-is — `qcow2` (imported into a hypervisor) or `iso` (mounted as a virtual CD) — where compression only adds an extra decompress step.

#### COMPRESS_OUTPUTIMAGE

`comma-separated list`

Create a compressed archive with an image file and GPG signature for redistribution

- sha: generate SHA256 hash for image
- gpg: sign image using gpg
- xz: compress image only using xz format
  - **IMAGE_XZ_COMPRESSION_RATIO** ( 0 - **1** - 9 ) images compression levels when using xz compressor. Beware of memory consumption when going higher
- zstd: compress image only using zstd format
  - **ZSTD_COMPRESSION_LEVEL** ( 1 - **9** - 19 ) images compression levels when using zstd compressor. Beware of memory consumption when going higher

#### IMAGE_XZ_MEMLIMIT

`string` · default: ~10GiB

`xz --memlimit-compress` ceiling for image compression.

#### ROOTFS_COMPRESSION_RATIO

`integer` · default: `5`

zstd level for rootfs compression (`15` when building the rootfs cache).

#### COMPRESS_MAX_THREADS

`integer` · default: `16`

Cap on the number of xz/zstd threads during image and rootfs compression.
