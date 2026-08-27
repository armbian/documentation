---
seo_title: "Armbian build switches reference"
description: "Reference for every optional compile.sh build switch in the Armbian build framework, grouped by what it controls: target, image, kernel, filesystem, host and more."
---

# Build switches

Switches are optional parameters passed to `./compile.sh` (or set in a [build configuration file](/build-framework/getting-started/#cli)) that control **what** and **how** a build produces. They are all optional; defaults are noted per entry.

```bash
./compile.sh PARAM=value OTHER_PARAM=value [<configfile> ...] [<command>]
```

!!! info "Switches vs. board configuration"
    Switches are **per-build** parameters. Variables that describe a specific **board** — its name, family, bootloader, kernel targets — live in the board's own `.conf` file; see [Board configuration](/build-framework/board-configuration/). `BOARD` is the bridge: `BOARD=bananapim5` tells the build to load `config/boards/bananapim5.conf`.

The reference is split by what each switch controls:

| Page | Covers |
|---|---|
| [Target](target.md) | Which board, kernel branch and release to build |
| [Image](image-type.md) | Minimal / desktop image and desktop selection |
| [Contents](image-contents.md) | Packages, firmware, networking and first-run behaviour inside the image |
| [Branding](branding.md) | Vendor / OS identity: name, URLs, logo, MOTD colour, maintainer |
| [Kernel](kernel-uboot.md) | Kernel source, config, compiler and bootloader options |
| [Filesystem](filesystem.md) | Root filesystem, partitions, labels, sizes and compression |
| [Host](host-docker.md) | The build host and the Docker build container |
| [Mirrors](proxies-mirrors.md) | HTTP proxies, download mirrors and a git proxy |
| [Apt](apt-cache.md) | apt-cacher-ng and local `.deb` package caching |
| [Performance](performance.md) | ccache, tmpfs, parallelism and native-armhf acceleration |
| [Patching](patching.md) | Round-tripping patches and build-debug switches |
| [Diagnostics](diagnostics.md) | Build logs and debug output |
