---
seo_title: "Armbian build caching & performance switches"
description: "Speed up Armbian builds: ccache, tmpfs working dirs, parallel patch rewriting, CPU thread count and native-armhf execution on arm64 hosts."
---

# Caching & performance

Switches that trade disk, RAM or cache for faster builds.

#### CPUTHREADS

`integer`

Override `CTHREADS` if set to a valid positive integer. If not defined, defaults to 150% of the CPU threads available, to maximize compilation speed.

#### USE_CCACHE

`string`

- `yes`
- `no` (default)

Use a C compiler cache. Generally not needed thanks to git-worktree, and can slow down clean builds.

#### PRIVATE_CCACHE

`string`

- `yes`
- `no` (default)

Use `$DEST/ccache` as the ccache home directory. Setting `yes` enables `USE_CCACHE` as well.

#### CCACHE_DIR

`string` · default: `$SRC/cache/ccache` (or `$DEST/ccache` when `PRIVATE_CCACHE=yes`)

Directory for the ccache compiler cache. Point it at a persistent location to share the cache across builds.

#### USE_TMPFS

`string`

- `yes`
- `no` (default)

Use tmpfs (RAM) for build working directories. Speeds up I/O-heavy stages on hosts with plenty of RAM; needs enough memory to hold the working set.

#### PREFER_NATIVE_ARMHF

`string`

- `yes` (default)
- `no`

On arm64 build hosts whose kernel supports `CONFIG_COMPAT`, run armhf binaries (rootfs/chroot, package post-install) natively at full speed instead of through `qemu-user-static`. Native execution is roughly 10× faster than qemu emulation. On hosts without 32-bit ARM userspace support (notably Apple Silicon) the framework transparently falls back to qemu. Set `no` to force qemu even when native COMPAT is available.

To build an arm64 Armbian kernel that exposes this capability for the host that runs it, enable the [arm64-compat-vdso extension](/build-framework/extensions/list/#arm64-compat-vdso) via `ENABLE_EXTENSIONS`. The relevant kernel options are documented in the [arm64 Kconfig](https://elixir.bootlin.com/linux/latest/source/arch/arm64/Kconfig):

- `CONFIG_COMPAT=y` — required; enables 32-bit EL0 support, without which armhf binaries cannot run at all.
- `CONFIG_COMPAT_VDSO=y` — optional but recommended; provides fast `gettimeofday`/`clock_gettime` for 32-bit processes via vDSO.

To check what a given host kernel ships with:

```bash
zcat /proc/config.gz | grep -E '^CONFIG_(COMPAT|COMPAT_VDSO)='
```

A host with native armhf support will print at least `CONFIG_COMPAT=y`. If the command prints nothing, or `CONFIG_COMPAT` is unset, the host kernel cannot run armhf userspace natively and the build framework will use qemu emulation regardless of this switch.

#### PARALLEL_PATCHES

`string`

- `yes`
- `no` (default)

Speeds up `rewrite-kernel-patches` and `rewrite-uboot-patches` up to `nproc` level by spinning up overlayfs-based worktrees and processing patches in parallel. Cross-patch dependencies (e.g. a single file touched by two or more patches) are detected beforehand and grouped for sequential processing to preserve context.

!!! tip "Note"
    This feature is experimental. Check the output against a classic sequential rewrite to make sure the diff is 0.

#### PARALLEL_WORKERS

`integer`

- `1` to `32`: manually set the number of workers when `PARALLEL_PATCHES=yes`. Default is auto-calculated from `nproc`.

#### ARTIFACT_IGNORE_CACHE

`string`

- `yes`
- `no` (default)

Enforce building from source instead of using pre-built (OCI-cached) artifacts.

#### ROOT_FS_CREATE_ONLY

`string`

- `yes`
- `no` (default)

Force local rootfs cache creation only, without proceeding to a full image build.
