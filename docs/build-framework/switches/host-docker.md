---
seo_title: "Armbian build host & Docker switches"
description: "Configure the Armbian build host and Docker container: base image, auto-pull, pruning, OCI cache, HTTP proxies, download mirrors and the apt cache."
---

# Build host & Docker

Control the build host, the Docker build container, network proxies and mirrors, and the apt package cache.

#### EXPERT

`string`

- `yes`

Unlocks development features in the interactive menus, exposing boards, kernel branches and distribution releases that are otherwise hidden because they are unsupported or still in development. Off by default so the menus only offer combinations Armbian officially supports; set `yes` when you knowingly want to build for a board or release below "supported" status. This only affects interactive mode — passing the relevant parameters on the command line already bypasses the filter.

#### CLEAN_LEVEL

`comma-separated list`

Selects which build artifacts and caches are wiped before the build runs, given as a comma-separated list of the targets below. Useful when rebuilding after source changes, or when building several images in a row and you need to force fresh compilation instead of reusing a stale tree. Include only the targets you actually need to invalidate — the `make-kernel` clean in particular is very slow, as it forces a full kernel rebuild.

- `make-atf` = make clean for ATF, if it is built.
- `make-uboot` = make clean for uboot, if it is built.
- `make-kernel` = make clean for the kernel if it is built. very slow.<br>
- `debs`, `alldebs` = delete all packages in "./output/debs"
- `images` = delete "./output/images"
- `cache` = delete "./output/cache"
- `sources` = delete `cache/sources` (all downloaded sources)
- `oldcache` = remove old cached rootfs except for the newest 8 files
- `extras` = delete additional packages for the current release in `output/debs/extra`

#### CARD_DEVICE

`string`

- `/dev/sdX`

After a successful build, writes the finished image to the named block device and verifies it by reading the data back and comparing sha256 checksums. Left empty by default, so a build only produces an image file; set it to the card's device node — check `lsblk` for the right name — to flash in the same run. Double-check the path, as the target device is overwritten completely.

#### PREFER_DOCKER

`string`

- `yes` (default)
- `no`

Armbian runs the build inside a Docker container by default, which isolates the toolchain from the host and gives reproducible results across different machines. Set to `no` to compile natively on the host instead — appropriate when Docker is unavailable, or when you have already prepared the host with all build dependencies and want to skip the container. Native builds place tighter requirements on the host OS, which is why the containerised path is preferred.

#### DOCKER_ARMBIAN_BASE_IMAGE

`string`

- `debian:trixie` (default)
- `debian:bookworm`
- `ubuntu:jammy`
- `ubuntu:noble`
- `ubuntu:resolute`

Defines the build host when using a Docker container (default). The image set is
generated from [`config/distributions`](https://github.com/armbian/build/tree/main/config/distributions),
skipping releases marked `eos` plus `sid` and `forky`; see the
[published images](https://github.com/armbian/docker-armbian-build/pkgs/container/docker-armbian-build).

#### ARMBIAN_DOCKER_AUTO_PULL

`string`

- `yes`: enable automatic Docker image pulling via system cronjob (every 12 hours)
- `no`: disable and remove any existing auto-pull cronjob
- undefined (default): no automatic pulling, manual pull when needed

Enables automatic background updates of Docker build images via a system cronjob that runs every 12 hours. This prevents waiting for image pulls during builds and keeps images fresh. The feature also includes automatic cleanup of old images (keeps only the 2 most recent per tag).

```sh
# Enable auto-pull cronjob
./compile.sh docker ARMBIAN_DOCKER_AUTO_PULL=yes

# Disable and remove auto-pull cronjob
./compile.sh docker ARMBIAN_DOCKER_AUTO_PULL=no
```

!!! tip "Note"

    This is an opt-in feature. When enabled, it creates:
    - `/usr/local/bin/armbian-docker-pull` - wrapper script for cron execution
    - `/etc/cron.d/armbian-docker-pull` - cronjob (runs at 00:00 and 12:00)
    - `/var/lib/armbian/docker-pull.hash` - configuration hash for update detection

#### DOCKER_FORCE_PULL

`string`

- `yes`: force a re-pull of the Docker base image, bypassing the local pull cache
- `no` (default): reuse the local image if it is present and was pulled within the last ~24 hours

By default the build only pulls the base image when the local copy is missing or its pull marker is older than ~24 hours; otherwise it reuses the local image. Set `DOCKER_FORCE_PULL=yes` to pull the latest published image immediately — useful right after a new framework image is published, so builds pick it up without waiting for the cache to expire or removing the local image by hand.

```sh
# Force a fresh pull of the base image for this build
./compile.sh DOCKER_FORCE_PULL=yes BOARD=uefi-x86 BRANCH=current
```

#### DOCKER_PRUNE

`string`

- `yes`: prune old Armbian build images from the local Docker daemon at the start of each build
- `no` (default): leave existing images in place

Whether the build framework automatically reclaims disk space by removing old Armbian build images during setup. Off by default — safe for hosts where multiple build invocations share one Docker daemon (typical for a server running several self-hosted GitHub Actions runners on the same machine), since concurrent pruning can race with another invocation that is still committing a freshly built image and surface as `failed to get digest sha256:…: no such file or directory`, aborting the in-flight build.

Set to `yes` on single-host setups where automatic disk reclaim is desirable.

!!! warning "Behaviour change"

    Earlier releases ran the cleanup unconditionally. The default is now `no`; users who relied on the automatic reclaim need to set `DOCKER_PRUNE=yes` explicitly.

#### CI

`string`

- `true`
- `false` (default)

Marks the build as running in a continuous-integration environment. When enabled (`true`), the Docker build container receives the host's Docker credentials (`${HOME}/.docker/config.json`) and the `OCI_TARGET_BASE` environment variable, so it can authenticate to and push cached artifacts to a registry. Left `false` for ordinary local builds; Armbian's own CI runners set it, and you rarely need to set it by hand.

#### OCI_TARGET_BASE

`string`

- url/to/container_registry/path
- `${GHCR_SOURCE}/armbian/*` (default; GHCR_SOURCE is defined in `lib/functions/configuration/main-config.sh`)

Base registry path the build uses to pull and push its OCI-cached artifacts — compiled kernels, U-Boot, rootfs and similar — so that work can be shared and reused instead of rebuilt from scratch. Defaults to Armbian's GHCR namespace (`${GHCR_SOURCE}/armbian/*`); point it at your own registry path when you run a private OCI cache. It is only passed into the build container when `CI=true`.

#### GHCR_MIRROR_ADDRESS

`string`

When ghcr.io is reached through a mirror — selected with `GHCR_MIRROR=dockerproxy` — this sets the mirror's hostname. The default is `ghcr.dockerproxy.net`; override it with `GHCR_MIRROR_ADDRESS` when that host is unavailable or a different mirror is faster for you. This mainly matters in regions where ghcr.io itself is slow or unreachable.

Example:

```sh
./compile.sh GHCR_MIRROR=dockerproxy GHCR_MIRROR_ADDRESS=ghcr.libcuda.so
```

#### USERPATCHES_PATH

`string` · default: `userpatches/`

Points the build at a different location for the `userpatches` folder, which holds your custom patches, overlays, config hooks, board definitions and first-run files. Defaults to `userpatches/` inside the build tree; set an absolute path to keep your customisations in a separate repository, or to share one set of patches across several checkouts.

#### NO_HOST_RELEASE_CHECK

`string` · default: `no`

Bypasses the guard that refuses to build on host OS releases Armbian has not validated. Off by default, so an unsupported host fails early with a clear message instead of part-way through; set `yes` to force the build to proceed anyway. Useful on a newer or derivative distribution not yet on the supported list, at the risk of build failures the check would otherwise catch up front.

#### SYNC_CLOCK

`string` · default: `yes`

Synchronises the build host's clock with `ntpdate` (against `NTP_SERVER`) before image creation, since a badly skewed clock can break TLS certificate validation and produce misleading file timestamps. On by default; the build automatically skips it when `ntpd` is already running, and clock-sync failures are tolerated. Set `no` on hosts where you manage time yourself or have no network path to an NTP server.

#### OFFLINE_WORK

`string` · default: `no`

Runs the build without touching the network: it skips git fetches and updates, the host clock sync and host checks, and serves cached sources and memoized data even when they are past their normal expiry. Set `yes` to build from what is already cached — for example on an air-gapped machine, or to guarantee a repeatable build against pinned sources. Anything not already present in the cache will make the build fail rather than trigger a download.

#### FORCE_USE_RAMDISK

`string`

Overrides the automatic decision on whether to build the rootfs and image on a tmpfs ramdisk. Normally the framework weighs available memory against the expected rootfs size and enables tmpfs only when it will comfortably fit; set `yes` to force the ramdisk on — much faster, but it needs plenty of RAM — or `no` to force it off, which is safer on memory-constrained hosts. Leave it unset to keep the autodetection.

#### DISABLE_IPV6

`string` · default: `true`

Defaults to `true`, which keeps the downloader (aria2c) on IPv4 only. This avoids stalled or hanging downloads on hosts that advertise IPv6 connectivity but cannot actually route it — a surprisingly common failure. Set `false` to allow IPv6 for downloads when your network genuinely supports it.

#### DOCKER_NICE

`integer`, -20 to 19

Sets the scheduling priority (niceness) of the build process inside the Docker container. It is captured automatically from the `nice` value of the initial `compile.sh` invocation and propagated into the container, so a build you launch with `nice` stays equally polite to the rest of the host. You normally do not set this by hand; lower values mean higher priority, higher values yield CPU to other work.

#### DOCKER_PRIVILEGED

`string` · default: `yes`

Controls whether the build container runs with Docker's `--privileged` flag. On (`yes`) by default because the build needs loop devices, mounts and other host-level operations to assemble an image; set `no` to run with a narrower profile instead (loop-control device plus unconfined seccomp), which is more restrictive but may not support every build type. Leave it at the default unless you have a specific reason to tighten container privileges.

#### DOCKER_SKIP_CARD_DEVICE

`string` · default: `no`

Stops the launcher from passing `CARD_DEVICE` through to the Docker container. Off by default, so when you set `CARD_DEVICE` the target card is exposed inside the container and the image is flashed after the build; set `yes` to keep the device off the container even though `CARD_DEVICE` is set — useful when you would rather flash the resulting image manually on the host.

#### FAST_DOCKER

`string` · default: `no`

Skips the step that regenerates and rebuilds the container's Dockerfile before launch, so the build starts straight from the existing image. Off by default, which keeps the container image in step with the framework; set `yes` when you know the image is already current and want to shave the refresh time off each launch — common in CI, where the image is pulled or built once up front.

#### PRE_PREPARED_HOST

`string` · default: `no`

Tells the build that the host already has every required dependency installed, so it skips the host-preparation stage that would otherwise check and install packages. Off by default; set `yes` on a pre-provisioned image — such as a purpose-built CI runner or a container that was baked with all build tools — to save the preparation time. Enabling it on an incompletely prepared host will surface as missing-tool errors later in the build.

#### ARMBIAN_DOCKER_PULL_USER

`string` · default: `$SUDO_USER`

Chooses the user account that owns the Docker image auto-pull cronjob (see `ARMBIAN_DOCKER_AUTO_PULL`). Defaults to the invoking user — `$SUDO_USER` when running under sudo, falling back to the current user — so the scheduled pull runs as the same person who builds. Set it explicitly when the cron should run as a different, dedicated build user.

#### NEEDS_BINFMT

`string` · default: `no`

Requires that `binfmt_misc` and `qemu-user-static` are set up so the build can run foreign-architecture binaries inside the rootfs (for example running arm64 tools on an x86 host). Set to `no` by default, but the framework forces it to `yes` for any build that assembles a rootfs or image, since those must execute target-architecture code in a chroot. You rarely set it yourself; it exists so lighter operations that never enter a foreign chroot can skip the binfmt setup.

## Proxies & mirrors

#### USE_MAINLINE_GOOGLE_MIRROR

`string` · default: `no`

Fetches mainline kernel sources from the `googlesource.com` mirror instead of the official `git.kernel.org`. Off by default; enable it when `git.kernel.org` is slow or unreliable from your location, as the Google mirror is often faster. This is a shorthand for `MAINLINE_MIRROR=google`.

#### USE_GITHUB_UBOOT_MIRROR

`string` · default: `no`

Fetches mainline U-Boot sources from an unofficial GitHub mirror instead of the official `git.denx.de`. Off by default; enable it when the DENX server is slow or unreachable from your location, since GitHub is often faster and more reliable. This is a shorthand for `UBOOT_MIRROR=github`.

#### DOWNLOAD_MIRROR

`string`

Selects the download mirror used for the cross-toolchain and the Debian/Ubuntu package repositories. Leave it empty to use the official sources; choose one of the regional mirrors below when the defaults are slow, which is typically the case for users in mainland China.

- `china`: use `mirrors.tuna.tsinghua.edu.cn`; it will be very fast thanks to Tsinghua University
- `bfsu`: use `mirrors.bfsu.edu.cn`, the mirror of Beijing Foreign Studies University
- leave empty to use official source

#### LOCAL_MIRROR

`string` · default: auto

Forces a specific Armbian apt mirror, overriding the automatic mirror selection the build would otherwise make. Give it the mirror's **host and path only, without a scheme** — the build prepends `http://` when it writes the apt source, so `LOCAL_MIRROR="apt.example.com/armbian"` becomes `http://apt.example.com/armbian` (a value like `https://…` would produce an invalid `http://https://…`). Left on auto by default; set it to build against an internal or geographically closer mirror — handy on isolated networks or to reduce load on the public infrastructure.

#### MAINLINE_MIRROR

`string`

Selects which mirror of `linux-stable.git` the mainline kernel sources are cloned from. Leave it empty to use the official `git.kernel.org`; pick one of the mirrors below when that server is slow for you, as it commonly is for users in mainland China.

- `google`: use the mirror provided by Google, the same as `USE_MAINLINE_GOOGLE_MIRROR=yes`
- `tuna`: use the mirror provided by Tsinghua University
- `bfsu`: use the mirror provided by Beijing Foreign Studies University, which is similar to `tuna`
- leave empty to use the official `git.kernel.org`, which may be very slow for mainland China users

#### UBOOT_MIRROR

`string`

Selects which mirror of `u-boot.git` the mainline U-Boot sources are cloned from. Leave it empty to use the official `source.denx.de`; pick one of the mirrors below when the DENX server is slow for you, as it commonly is for users in mainland China.

- `github`: use the mirror provided by github, the same as `USE_GITHUB_UBOOT_MIRROR=yes`
- `gitee`: use the mirror provided by Gitee, a Chinese git services
- leave empty to use the official `source.denx.de`, which may be very slow for mainland China users

#### GITHUB_MIRROR

`string`

Selects a mirror or proxy for the many GitHub-hosted repositories the build clones. Leave it empty to connect to GitHub directly; choose one of the options below when GitHub is slow or unreachable — again, most relevant for users in mainland China or behind a corporate git proxy.

- `fastgit`: use the mirror provided by fastgit.org
- `gitclone`: use the mirror provided by gitclone.com
- `cnpmjs`: use the mirror provided by cnpmjs.org
- `gitproxy`: use a pass-through git proxy whose full base URL is given in `GITPROXY_ADDRESS` (e.g. `https://gitproxy.example.com/github.com`, no trailing slash). Selected automatically when a CI runner exports `GITPROXY_ADDRESS`.
- leave empty to connect directly to GitHub, which may be very slow for mainland China users

#### GITPROXY_ADDRESS

`string`

Full base URL of the pass-through git proxy used by `GITHUB_MIRROR=gitproxy`; it replaces `https://github.com` for all source clones (for example `https://gitproxy.example.com/github.com`, no trailing slash). When a CI runner exports this variable, `GITHUB_MIRROR` is switched to `gitproxy` automatically, so self-hosted runners route their clones through the proxy without extra configuration. Set it by hand only if you run such a proxy yourself.

#### REGIONAL_MIRROR

`string`

Sets a whole group of mirrors at once from a single regional preset, so you do not have to configure each source individually. It never overrides a mirror you have already set explicitly, so you can adopt the regional defaults and still override any single one. Leave it empty for the standard upstream sources.

- `china`: MAINLINE_MIRROR=`tuna`, UBOOT_MIRROR=`gitee`, GITHUB_MIRROR=`fastgit`, DOWNLOAD_MIRROR=`china`
- leave empty to use default settings

#### HTTP_PROXY

`string` · default: empty

Proxy URL for HTTP traffic, propagated into the build container and the tools it runs. Empty by default; set it when the build host reaches the internet only through an HTTP proxy.

#### HTTPS_PROXY

`string` · default: empty

Proxy URL for HTTPS traffic, propagated into the build container and the tools it runs. Empty by default; set it when the build host reaches the internet only through an HTTPS proxy.

#### FTP_PROXY

`string` · default: empty

Proxy URL for FTP traffic, propagated into the build container and the tools it runs. Empty by default; set it when the build host reaches FTP resources only through a proxy.

#### NO_PROXY

`string` · default: empty

Comma-separated list of hosts and domains that should bypass the proxies above, propagated into the build container and the tools it runs. Empty by default; set it to keep local mirrors, registries or internal hosts off the proxy.

#### GITHUB_SOURCE

`string` · default: `https://github.com`

Base GitHub URL used when the build downloads helper tools and some sources (for example `bat`, `oras` and oh-my-zsh). Defaults to `https://github.com`; override it to route those fetches through a GitHub mirror or a caching proxy. Unlike `GITHUB_MIRROR`, this substitutes the URL directly rather than selecting a named mirror preset.

#### ARMBIAN_FIRMWARE_GIT_SOURCE

`string` · default: `https://github.com/armbian/firmware`

Git repository the build clones the Armbian firmware blobs from when building the firmware packages. Defaults to `https://github.com/armbian/firmware`; point it at a fork or a local mirror to build against custom firmware or when working behind a firewall. Pair it with `ARMBIAN_FIRMWARE_GIT_BRANCH` to select the branch.

#### ARMBIAN_FIRMWARE_GIT_BRANCH

`string` · default: `master`

Branch of the Armbian firmware repository (`ARMBIAN_FIRMWARE_GIT_SOURCE`) to check out when building the firmware packages. Defaults to `master`; change it to build from a development branch or to pin firmware from a specific branch of your own fork.

## APT cache

#### MANAGE_ACNG

`string` · default: `no`

Controls use of `apt-cacher-ng`, a caching proxy for Debian/Ubuntu apt repositories that speeds up repeated builds by serving already-downloaded packages from disk. Off by default. It accepts either a plain `yes`/`no` or a full URL, as described below; anything that is not `yes`, `no` or empty must be a valid `http`/`https` URL, or the build aborts.

- `yes` sets up an automatically managed `apt-cacher-ng` instance on the build host. This mode is incompatible with container builds.
- but you can provide a URL for a self-managed `apt-cacher-ng` instance, e.g. `"http://apt-cacher.example.com:3142"`

#### APT_PROXY_ADDR

`string` · default: `localhost:3142`

Address of the apt caching proxy that package downloads are routed through during the rootfs bootstrap. Defaults to `localhost:3142`, the standard `apt-cacher-ng` port; when it is set and `MANAGE_ACNG` is not managing its own instance, the debootstrap and chroot apt operations are pointed at this proxy. CI runners commonly export it to reuse a shared cache; leave it as-is if you have no external proxy.

#### APT_CACHER_NG_CACHE_DIR

`string` · default: `/var/cache/apt-cacher-ng`

Filesystem directory where the managed `apt-cacher-ng` instance (`MANAGE_ACNG=yes`) stores its cached packages. Defaults to `/var/cache/apt-cacher-ng`; point it at a larger or faster volume when the default location lacks space, or to keep the cache on persistent storage across builds.

#### USE_LOCAL_APT_DEB_CACHE

`string` · default: `yes`

Keeps a local cache of downloaded `.deb` packages under `$SRC/cache/aptcache` and reuses it across builds, so unchanged packages are not fetched again. On by default because it noticeably speeds up repeated builds; set `no` to always download fresh packages, at the cost of build time and bandwidth — the build warns that this is generally not a good idea.

#### ORAS_REPO

`string` · default: `oras-project`

GitHub organisation the build downloads the ORAS OCI client binary from, ORAS being the tool used to push and pull OCI-cached artifacts. Defaults to `oras-project`, the upstream releases; override it to pull the binary from a fork or mirror. The build already switches this automatically for architectures without an official upstream binary (such as loong64), so you rarely set it by hand.
