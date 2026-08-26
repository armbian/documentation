---
seo_title: "Armbian build apt cache switches"
description: "Speed up repeated Armbian builds with a package cache: apt-cacher-ng, a local .deb cache, the apt proxy address and the ORAS client source."
---

# Apt

Cache Debian and Ubuntu packages between builds so they are not re-downloaded every time.

#### MANAGE_ACNG

`string` · default: `no`

Controls use of `apt-cacher-ng`, a caching proxy for Debian/Ubuntu apt repositories that speeds up repeated builds by serving already-downloaded packages from disk. Off by default. It accepts either a plain `yes`/`no` or a full URL, as described below; anything that is not `yes`, `no` or empty must be a valid `http`/`https` URL, or the build aborts.

- `yes` sets up an automatically managed `apt-cacher-ng` instance on the build host. This mode is incompatible with container builds.
- but you can provide a URL for a self-managed `apt-cacher-ng` instance, e.g. `"http://apt-cacher.example.com:3142"`

#### APT_PROXY_ADDR

`string` · default: empty

Address of an external apt caching proxy to route package downloads through during the rootfs bootstrap and chroot apt operations. **Empty by default** — no proxy is used unless you set it. When set (and `MANAGE_ACNG` is not managing its own instance), debootstrap and the chroot apt operations are pointed at this proxy. CI runners commonly export it to reuse a shared package cache. The managed `apt-cacher-ng` path (`MANAGE_ACNG=yes`) assumes the standard `localhost:3142` when this is unset.

#### APT_CACHER_NG_CACHE_DIR

`string` · default: `/var/cache/apt-cacher-ng`

Filesystem directory where the managed `apt-cacher-ng` instance (`MANAGE_ACNG=yes`) stores its cached packages. Defaults to `/var/cache/apt-cacher-ng`; point it at a larger or faster volume when the default location lacks space, or to keep the cache on persistent storage across builds.

#### USE_LOCAL_APT_DEB_CACHE

`string` · default: `yes`

Keeps a local cache of downloaded `.deb` packages under `$SRC/cache/aptcache` and reuses it across builds, so unchanged packages are not fetched again. On by default because it noticeably speeds up repeated builds; set `no` to always download fresh packages, at the cost of build time and bandwidth — the build warns that this is generally not a good idea.

#### ORAS_REPO

`string` · default: `oras-project`

GitHub organisation the build downloads the ORAS OCI client binary from, ORAS being the tool used to push and pull OCI-cached artifacts. Defaults to `oras-project`, the upstream releases; override it to pull the binary from a fork or mirror. The build already switches this automatically for architectures without an official upstream binary (such as loong64), so you rarely set it by hand.
