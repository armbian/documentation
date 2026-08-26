---
seo_title: "Armbian build proxy & mirror switches"
description: "Route the Armbian build through proxies and faster mirrors: HTTP/HTTPS proxies, kernel, U-Boot and GitHub download mirrors, a git proxy and regional presets."
---

# Mirrors

Route source downloads and package fetches through HTTP proxies, faster regional mirrors, or a git proxy — useful behind a corporate proxy or in regions where the default upstreams are slow.

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
- `gitverse`: use the GitVerse (`gitverse.ru`) mirror
- leave empty to use the official `git.kernel.org`, which may be very slow for mainland China users

#### UBOOT_MIRROR

`string`

Selects which mirror of `u-boot.git` the mainline U-Boot sources are cloned from. Leave it empty to use the official `source.denx.de`; pick one of the mirrors below when the DENX server is slow for you, as it commonly is for users in mainland China.

- `github`: use the mirror provided by GitHub, the same as `USE_GITHUB_UBOOT_MIRROR=yes`
- `gitee`: use the mirror provided by Gitee, a Chinese Git service
- leave empty to use the official `source.denx.de`, which may be very slow for mainland China users

#### GITHUB_MIRROR

`string`

Selects a mirror or proxy for the many GitHub-hosted repositories the build clones. Leave it empty to connect to GitHub directly; choose one of the options below when GitHub is slow or unreachable — again, most relevant for users in mainland China or behind a corporate git proxy.

- `fastgit`: use the fastgit.org mirror (`hub.fastgit.xyz`)
- `ghproxy`: use a GitHub proxy — defaults to `ghfast.top`; override the host with `GHPROXY_ADDRESS`
- `gitclone`: use the gitclone.com mirror
- `gitproxy`: use a pass-through git proxy whose full base URL is given in `GITPROXY_ADDRESS` (e.g. `https://gitproxy.example.com/github.com`, no trailing slash). Selected automatically when a CI runner exports `GITPROXY_ADDRESS`.
- leave empty to connect directly to GitHub, which may be very slow for mainland China users

#### GITPROXY_ADDRESS

`string`

Full base URL of the pass-through git proxy used by `GITHUB_MIRROR=gitproxy`; it replaces `https://github.com` for all source clones (for example `https://gitproxy.example.com/github.com`, no trailing slash). When a CI runner exports this variable, `GITHUB_MIRROR` is switched to `gitproxy` automatically, so self-hosted runners route their clones through the proxy without extra configuration. Set it by hand only if you run such a proxy yourself.

#### REGIONAL_MIRROR

`string`

Sets a whole group of mirrors at once from a single regional preset, so you do not have to configure each source individually. It never overrides a mirror you have already set explicitly, so you can adopt the regional defaults and still override any single one. Leave it empty for the standard upstream sources.

- `china`: MAINLINE_MIRROR=`tuna`, UBOOT_MIRROR=`gitee`, GITHUB_MIRROR=`ghproxy`, GHCR_MIRROR=`nju`, DOWNLOAD_MIRROR=`china`
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

#### NAMESERVER

`IPv4 address` · default: autodetected, else `1.0.0.1`

DNS resolver used **inside the build chroot** while packages are downloaded; it does not affect the finished image (DNS there is left to DHCP/systemd). When you leave it unset the framework autodetects a usable resolver from the host's `/etc/resolv.conf`, falling back to `1.0.0.1` (Cloudflare); set it explicitly to force a specific resolver — for example on an isolated network where the host's resolver is unreachable from the chroot.

#### GITHUB_SOURCE

`string` · default: `https://github.com`

Base GitHub URL used when the build downloads helper tools and some sources (for example `bat`, `oras` and oh-my-zsh). Defaults to `https://github.com`; override it to route those fetches through a GitHub mirror or a caching proxy. Unlike `GITHUB_MIRROR`, this substitutes the URL directly rather than selecting a named mirror preset.

#### ARMBIAN_FIRMWARE_GIT_SOURCE

`string` · default: `https://github.com/armbian/firmware`

Git repository the build clones the Armbian firmware blobs from when building the firmware packages. Defaults to `https://github.com/armbian/firmware`; point it at a fork or a local mirror to build against custom firmware or when working behind a firewall. Pair it with `ARMBIAN_FIRMWARE_GIT_BRANCH` to select the branch.

#### ARMBIAN_FIRMWARE_GIT_BRANCH

`string` · default: `master`

Branch of the Armbian firmware repository (`ARMBIAN_FIRMWARE_GIT_SOURCE`) to check out when building the firmware packages. Defaults to `master`; change it to build from a development branch or to pin firmware from a specific branch of your own fork.
