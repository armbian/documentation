---
title: How a build runs
seo_title: "How the Armbian build framework runs a build"
description: "A high-level walkthrough of what the Armbian build framework does on a vanilla run: configuration aggregation, the artifact and remote-cache model, rootfs creation, and image assembly."
---
# How a build runs

This is a high-level tour of what `./compile.sh` does on a vanilla image build. It is a mental model, not a line-by-line reference — the exact steps live in `lib/functions/` in the [build repository](https://github.com/armbian/build).

## Order of operations

1. **Entry and argument parsing.** `compile.sh` reads the command (e.g. `build`, `kernel-config`) and every `KEY=value` argument, turning each into the configuration variable used later.

2. **Host preparation.** The framework runs inside a **Docker container by default** (`PREFER_DOCKER=yes`); it builds or pulls the build image, then installs host dependencies into it — including the **cross-toolchains, which are ordinary distribution packages** (gcc/binutils for the target architecture), not a collection Armbian ships itself. You can also build natively on a supported host.

3. **Configuration aggregation.** Configuration is layered and inherited: **board → family → architecture → release**, merged with your `userpatches/` overrides and any enabled [extensions](extensions/index.md). The result is the complete set of variables — kernel source and branch, u-boot source, patch directories, package lists, and so on — that drives the rest of the build.

4. **Artifacts (build-or-pull).** Each major component — **u-boot, kernel, firmware, `armbian-bsp-cli`, and the rootfs** — is an *artifact*. The framework computes a **content hash** from that artifact's inputs (git revision, patches, `.config`, framework code, variables), then:
    - looks the hash up in the local cache and in the **remote OCI registry** (`ghcr.io/armbian/os`);
    - if a matching build already exists, it is **downloaded** — no compilation;
    - otherwise the artifact is **built** (checkout source, apply the framework's patches then your `userpatches/` patches, compile to `.deb` / tarball) and **pushed** to the cache so the next build reuses it.

5. **Root filesystem.** The rootfs is itself an artifact: pulled from cache when available, otherwise created with **`debootstrap`** for the target release (Debian or Ubuntu), then customized — Armbian packages, board support (`armbian-bsp-cli`), and the kernel/u-boot `.deb`s installed inside the chroot.

6. **Image assembly.** A raw image file is created on a **loop device**, partitioned and formatted, and the finished rootfs is copied in. Board- and family-specific **post-processing** then runs — for example writing u-boot to the right offset and assembling secondary program loaders.

7. **Finalization.** The image is watermarked in **`/etc/armbian-release`**, checksums are generated, and the image is compressed.

## Notes

- **Kernel branches** are `legacy`, `current`, `edge`, and (for some boards) `vendor` — set with `BRANCH=`.
- **Releases** are current Debian/Ubuntu codenames (for example `trixie`, `noble`), set with `RELEASE=`.
- Individual stages can be run on their own — `kernel-config`, `kernel-patch`, `rewrite-kernel-config`, `artifact`, and others — which is how maintainers iterate without a full image build. See the [command reference](commands/index.md).

*This page grew out of [documentation issue #190](https://github.com/armbian/documentation/issues/190), updated for the current (post-"armbian-next") framework.*
