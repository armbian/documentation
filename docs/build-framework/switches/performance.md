---
seo_title: "Armbian build caching & performance switches"
description: "Speed up Armbian builds: ccache, tmpfs working dirs, parallel patch rewriting, CPU thread count and native-armhf execution on arm64 hosts."
---

# Caching & performance

Switches that trade disk, RAM or cache for faster builds.

#### CPUTHREADS

`integer`

Sets the `make -j` parallelism used for every compilation stage — kernel, U-Boot, ATF, crust and friends. When left undefined the framework auto-picks 150% of the detected CPU count (`nproc + nproc/2`) so that cores stay busy even while some jobs stall on I/O. Set it to a valid positive integer to override that, for example to cap the load on a shared build server or to avoid the peak memory of an oversubscribed link stage. The value is also forwarded into the build container, so it applies to Docker builds as well.

#### USE_CCACHE

`string`

- `yes`
- `no` (default)

Wraps the compiler in `ccache` so unchanged translation units are served from a cache instead of recompiled, putting `/usr/lib/ccache` first on `PATH`. Off by default because the framework already caches whole kernel and U-Boot artifacts through git-worktree, which usually saves more than object-level caching would; on a cold cache the extra bookkeeping can actually make a clean build slower. Turn it on only if you repeatedly recompile the same source tree with small local changes and want ccache to short-circuit the unchanged files.

#### PRIVATE_CCACHE

`string`

- `yes`
- `no` (default)

Points ccache at a private cache directory inside the build tree rather than the shared one, which avoids the file-ownership problems that arise when the build is run under `sudo`. Because a private cache only makes sense with caching active, setting `yes` implicitly enables `USE_CCACHE` too, so you do not have to set both. Reach for it when you want ccache but are building as root and do not want to share the cache with other users on the host.

#### CCACHE_DIR

`string` · default: `$SRC/cache/ccache`

Location of the persistent ccache store, honoured by the kernel and U-Boot compile steps when ccache is active. It is distinct from `CCACHE_TEMPDIR`, which holds only transient files and lives under the working directory (often on tmpfs). Point it at a stable, roomy path — a location outside the build tree, or a shared volume in CI — so the cache survives between builds and across worktree resets instead of being thrown away.

#### USE_TMPFS

`string`

- `yes`
- `no` (default)

Mounts a RAM-backed tmpfs over the build working directories, so the churn of unpacking, patching and compiling never touches a physical disk. This can noticeably speed up I/O-heavy stages, but the mount is sized at up to 99% of RAM, so the host needs enough free memory to hold the entire working set or the build will run out of space. It is honoured only when the build runs as root on Linux and outside a Dockerfile build; in those unsupported contexts the setting is quietly skipped. Off by default; enable it on a well-provisioned host where the working directory is the bottleneck.

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

Caps how many overlayfs worktrees the parallel patch rewriter runs at once, and only takes effect when `PARALLEL_PATCHES=yes`. Leave it unset to let the framework size the pool automatically from the available cores, which is the right choice on most machines. Set an explicit count to throttle back the parallelism — for instance to reduce peak memory or disk pressure from the overlay mounts; a value that is out of range or otherwise invalid is ignored and the auto-calculation is used instead.

#### ARTIFACT_IGNORE_CACHE

`string`

- `yes`
- `no` (default)

Forces artifacts (kernel, U-Boot, rootfs and so on) to be rebuilt from source, bypassing both the local cache and the remote OCI registry that the framework would otherwise pull a ready-made artifact from. Off by default, since reusing cached artifacts is what keeps everyday builds fast. Set `yes` when you suspect a cached artifact is stale or corrupt, or when you have changed something the cache key does not capture and need to be certain the output is freshly compiled.

#### ROOT_FS_CREATE_ONLY

`string`

- `yes`
- `no` (default)

Historically this stopped the build after creating the root filesystem cache, without going on to assemble a full image. It is now deprecated: setting `yes` aborts the build with an error pointing you to the dedicated `rootfs` CLI command, which is the supported way to build just the rootfs artifact. Leave it at `no` (the default) and use `./compile.sh rootfs` instead when you only want the cached root filesystem.
