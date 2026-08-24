---
seo_title: "Armbian build host & Docker switches"
description: "Configure the Armbian build host and Docker container: base image, auto-pull, pruning, OCI cache, HTTP proxies, download mirrors and the apt cache."
---

# Build host & Docker

Control the build host, the Docker build container, network proxies and mirrors, and the apt package cache.

## Build host & Docker

#### EXPERT

`string`

- `yes`

Show development features and boards regardless of their support status in interactive mode.

#### CLEAN_LEVEL

`comma-separated list`

Defines what should be cleaned. Changing this option can be useful when rebuilding images or building more than one image

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

After successful compilation, do a verified burn of the image to the specified storage device (flash media / SD card).

#### PREFER_DOCKER

`string`

- `yes` (default)
- `no`

Docker assisted compilation is on by default. Set to `no` if you prefer running compilation natively.

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

!!! example "Build switch example"

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

!!! example "Build switch example"

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

If enabled (`true`), the Docker build container will receive Docker credentials from the host
(`${HOME}/.docker/config.json`) and the `OCI_TARGET_BASE` environment variable.

#### OCI_TARGET_BASE

`string`

- url/to/container_registry/path
- `${GHCR_SOURCE}/armbian/*` (default; GHCR_SOURCE is defined in `lib/functions/configuration/main-config.sh`)

Select the target for pull/push OCI cached images. If not set, default is used.

#### GHCR_MIRROR_ADDRESS

`string`

The default mirror address for ghcr.io, set by `GHCR_MIRROR=dockerproxy`, is ghcr.dockerproxy.net. When this address is unavailable, an alternative address can be set with `GHCR_MIRROR_ADDRESS`.

Example:

```sh
./compile.sh GHCR_MIRROR=dockerproxy GHCR_MIRROR_ADDRESS=ghcr.libcuda.so
```

#### USERPATCHES_PATH

`string` · default: `userpatches/`

Set an alternate path for the location of the `userpatches` folder.

#### NO_HOST_RELEASE_CHECK

`string` · default: `no`

Overrides the check for a supported host system.

#### SYNC_CLOCK

`string` · default: `yes`

Sync system clock on builder before start image creation process.

#### OFFLINE_WORK

`string` · default: `no`

Skip downloading and updating sources and time and host check. Set to "yes," and you can collect packages without accessing the internet.

#### FORCE_USE_RAMDISK

`string`

Overrides autodetect for using tmpfs in new debootstrap and image creation process.

#### DISABLE_IPV6

`string` · default: `true`

The distant future, the year Two-Thousand. Set false to allow Aria2c to use a modern ip protocol.

#### DOCKER_NICE

`integer`, -20 to 19

Automatically propagated from the initial `compile.sh`'s `nice` value.

#### DOCKER_PRIVILEGED

`string` · default: `yes`

Run the build container privileged; set `no` for a narrow capability set.

#### DOCKER_SKIP_CARD_DEVICE

`string` · default: `no`

Do not pass `CARD_DEVICE` into the container.

#### FAST_DOCKER

`string` · default: `no`

Skip slow container-image refresh checks for a faster launch.

#### PRE_PREPARED_HOST

`string` · default: `no`

Assume host dependencies are already installed; skip host preparation steps.

#### ARMBIAN_DOCKER_PULL_USER

`string` · default: `$SUDO_USER`

User for the Docker image auto-pull cron.

#### NEEDS_BINFMT

`string` · default: `no`

Require binfmt_misc/qemu-static; automatically set `yes` for image and rootfs builds.

## Proxies & mirrors

#### USE_MAINLINE_GOOGLE_MIRROR

`string` · default: `no`

Use the `googlesource.com` mirror for downloading mainline kernel sources, which may be faster than `git.kernel.org` depending on your location.

#### USE_GITHUB_UBOOT_MIRROR

`string` · default: `no`

Use an unofficial GitHub mirror for downloading mainline U-Boot sources, may be faster than `git.denx.de` depending on your location.

#### DOWNLOAD_MIRROR

`string`

Select download mirror for `toolchain` and `debian/ubuntu packages`

- `china`: use `mirrors.tuna.tsinghua.edu.cn`; it will be very fast thanks to Tsinghua University
- `bfsu`: use `mirrors.bfsu.edu.cn`, the mirror of Beijing Foreign Studies University
- leave empty to use official source

#### LOCAL_MIRROR

`string` · default: auto

Override automated mirror selection, example 'LOCAL_MIRROR="<https://yourlocalmirror.com>"'.

#### MAINLINE_MIRROR

`string`

Select mainline mirror of `linux-stable.git`

- `google`: use the mirror provided by Google, the same as `USE_MAINLINE_GOOGLE_MIRROR=yes`
- `tuna`: use the mirror provided by Tsinghua University
- `bfsu`: use the mirror provided by Beijing Foreign Studies University, which is similar to `tuna`
- leave empty to use the official `git.kernel.org`, which may be very slow for mainland China users

#### UBOOT_MIRROR

`string`

Select mainline mirror of `u-boot.git`

- `github`: use the mirror provided by github, the same as `USE_GITHUB_UBOOT_MIRROR=yes`
- `gitee`: use the mirror provided by Gitee, a Chinese git services
- leave empty to use the official `source.denx.de`, which may be very slow for mainland China users

#### GITHUB_MIRROR

`string`

Select download mirror for GitHub hosted repository

- `fastgit`: use the mirror provided by fastgit.org
- `gitclone`: use the mirror provided by gitclone.com
- `cnpmjs`: use the mirror provided by cnpmjs.org
- `gitproxy`: use a pass-through git proxy whose full base URL is given in `GITPROXY_ADDRESS` (e.g. `https://gitproxy.example.com/github.com`, no trailing slash). Selected automatically when a CI runner exports `GITPROXY_ADDRESS`.
- leave empty to connect directly to GitHub, which may be very slow for mainland China users

#### GITPROXY_ADDRESS

`string`

Full base URL of the git proxy used by `GITHUB_MIRROR=gitproxy`; it replaces `https://github.com` for all source clones. Usually provided automatically by self-hosted CI runners.

#### REGIONAL_MIRROR

`string`

Select mirrors based on regional setting, will not overwrite explicitly specified mirror option

- `china`: MAINLINE_MIRROR=`tuna`, UBOOT_MIRROR=`gitee`, GITHUB_MIRROR=`fastgit`, DOWNLOAD_MIRROR=`china`
- leave empty to use default settings

#### HTTP_PROXY

`string` · default: empty

HTTP proxy propagated into container/tool environments.

#### HTTPS_PROXY

`string` · default: empty

HTTPS proxy propagated into container/tool environments.

#### FTP_PROXY

`string` · default: empty

FTP proxy propagated into container/tool environments.

#### NO_PROXY

`string` · default: empty

Proxy-bypass list propagated into container/tool environments.

#### GITHUB_SOURCE

`string` · default: `https://github.com`

Base GitHub URL for tool/source downloads (mirror override).

#### ARMBIAN_FIRMWARE_GIT_SOURCE

`string` · default: `https://github.com/armbian/firmware`

Git source repo for Armbian firmware.

#### ARMBIAN_FIRMWARE_GIT_BRANCH

`string` · default: `master`

Git branch of the Armbian firmware repo.

## APT cache

#### MANAGE_ACNG

`string` · default: `no`

Configures use of `apt-cacher-ng`, a cache for debian/ubuntu/etc apt repositories.

- `yes` sets up an automatically managed `apt-cacher-ng` instance on the build host. This mode is incompatible with container builds.
- but you can provide a URL for a self-managed `apt-cacher-ng` instance, e.g. `"http://apt-cacher.example.com:3142"`

#### APT_PROXY_ADDR

`string` · default: `localhost:3142`

Address of the apt proxy/cacher used for package downloads.

#### APT_CACHER_NG_CACHE_DIR

`string` · default: `/var/cache/apt-cacher-ng`

Cache directory for the managed apt-cacher-ng instance.

#### USE_LOCAL_APT_DEB_CACHE

`string` · default: `yes`

Use `$SRC/cache/aptcache` as a local `.deb` apt cache.

#### ORAS_REPO

`string` · default: `oras-project`

GitHub org to download the ORAS OCI client binary from (mirror override).
