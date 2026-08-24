---
seo_title: "Armbian build host setup & requirements"
description: "Armbian build framework quick start: hardware requirements, Debian 13 Trixie or Docker host setup and cloning the repository to build ARM Linux images."
---

# Armbian Build Framework Quick Start Guide

## Requirements

- x86_64 / aarch64 / riscv64 machine
- at least 8GB (less for non-[BTF](https://docs.kernel.org/bpf/btf.html) builds) of memory and ~50GB of disk space for VM, container, or bare-metal installation
- **Armbian/Debian 13 (Trixie)** for native building or any Docker capable Linux for containerised
- **Windows 10/11 with WSL2 subsystem** running Armbian/Debian 13 (Trixie)
- Superuser rights (configured sudo or root access).
- Make sure your system is up-to-date! Outdated Docker binaries, for example, can cause trouble


## Install Docker

The build runs inside a Docker container by default (`./compile.sh` relaunches itself in one), so the host needs a working Docker install.

On an **Armbian** host, install it with `armbian-config` → **Software → Containers → Docker** (see [Docker](/software/docker/)).

On other Debian/Ubuntu hosts (including WSL2):

```bash
sudo apt install -y docker.io docker-buildx
```

Or follow the [official Docker install guide](https://docs.docker.com/engine/install/).


## Clone repository

```bash
git clone https://github.com/armbian/build
cd build
```
!!! note
    - Make sure that full path to the build script **does not contain spaces**
    - For stable branch use last point release `--branch=v24.11`


## Install host requirements

Install the build host prerequisites. You only need to run this once:

```bash
./compile.sh requirements
```


## Interactive

Run framework:

```bash
./compile.sh
```

??? info "Video"
    <iframe width="939" height="529" src="https://www.youtube.com/embed/kQcEFsXEJEE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## CLI

```bash
./compile.sh [command] [switch...] [config...]
```

!!! tip "Troubleshooting: 'unknown terminal type' error"
    When running the script, especially from modern terminal emulators (like Ghostty, Kitty, WezTerm), you might encounter an error like

    'xterm-ghostty': unknown terminal type

    **Quick workaround:** you can force a more common terminal type before running the script:
    ```bash
    env TERM=xterm-256color ./compile.sh
    ```

Only one command can be specified.

Switches are parameter settings that are used by the build framework itself
(e.g. `DEBUG=yes`) or the specific command.

Config files are bash shell scripts that are sourced in the order
specified. They are primarily used to set switches but might also set hook
functions. They must be located in the `userpatches` directory and must
be named `config-${arg}.conf` or `config-${arg}.conf.sh` (where `${arg}` is
the argument from the command line): one or the other, but not both.

Switches set on the commandline override settings from the config files,
regardless of the order they appear on the comandline.

Comprehensive list of build [Commands](/build-framework/commands/) and [Switches](/build-framework/switches/)

Example:

```bash
./compile.sh build \
BOARD=uefi-x86 \
BRANCH=current \
BUILD_DESKTOP=yes \
BUILD_MINIMAL=no \
DESKTOP_ENVIRONMENT=gnome \
DESKTOP_TIER=full \
KERNEL_CONFIGURE=no \
RELEASE=resolute
```

Or, using config file `userpatches/config-myboard.conf`
that sets all these switches:

```bash
./compile.sh build \
myboard
```

!!! question "Interpretation?"

    This command will generate an **Ubuntu 26.04 Resolute** based **GNOME desktop** image for Intel based hardware (**uefi-x86**), using the **full** desktop tier (the bare desktop plus its bundled application set) and an unchanged kernel from the **current** branch.


## Logging


Logs are written to **output/logs**. Old logs (all but the current build)
are compressed and moved to **output/logs/archive**.

Log formats are:

- ANSI - text with ANSI escapes for color coding - \*.log.ans
- ASCII (if ansi2txt is available) - text without color coding escapes - \*.log
- Markdown summary - \*.md
- Raw (if RAW_LOG=yes) - tar file containg all the raw logs - \*.raw.tar

For much more verbose logs set switch 'DEBUG=yes'.

To share a build log when asking for help, set `SHARE_LOG=yes`. The build uploads the log to Armbian's paste service (`paste.armbian.com`) and prints a URL you can post in the forum or a bug report:

```bash
./compile.sh build BOARD=uefi-x86 BRANCH=current SHARE_LOG=yes
```

## GitHub Actions

If you do not have the proper equipment to build images on your own, you can use our [GitHub Action](https://github.com/marketplace/actions/rebuild-armbian).

### Minimal workflow example

Create `.github/workflows/build.yml` in your repository:

```yaml
name: Build Armbian Image
on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest # ubuntu-24.04-arm, ubuntu-24.04-riscv
    steps:
      - uses: armbian/build@main
        with:
          armbian_token: ${{ secrets.GITHUB_TOKEN }}
          armbian_board: "uefi-x86" # orangepi5 bananapif3
          armbian_release: "noble" # trixie
          armbian_target: "build"
          armbian_ui: "minimal" # server xfce
          armbian_runner_clean: "yes" # recommended for Github runners
```

The action will build the image, create a GitHub Release in your repository and upload the artifacts.

### Inputs reference

| Input | Required | Default | Description |
|---|---|---|---|
| `armbian_token` | **yes** | — | GitHub access token (`GITHUB_TOKEN` or a PAT) |
| `armbian_board` | no | `uefi-x86` | Hardware platform (e.g. `orangepi5`, `rock-5b`) |
| `armbian_target` | no | `kernel` | Build target: `kernel` or `build` (full image) |
| `armbian_branch` | no | `main` | Armbian framework branch |
| `armbian_kernel_branch` | no | `current` | Kernel branch: `current`, `edge`, etc. |
| `armbian_release` | no | `noble` | Userspace release (e.g. `noble`, `bookworm`, `trixie`) |
| `armbian_ui` | no | `minimal` | `minimal`, `server`, or a desktop environment name (e.g. `xfce`, `gnome`) |
| `armbian_version` | no | *auto* | Override version; patch level is auto-incremented from `stable.json` if not set |
| `armbian_compress` | no | `sha,img,xz` | Output compression method |
| `armbian_extensions` | no | — | Comma-separated list of build extensions to enable |
| `armbian_pgp_key` | no | — | GPG private key for image signing (store as a secret) |
| `armbian_pgp_password` | no | — | GPG passphrase (store as a secret) |
| `armbian_release_title` | no | `Armbian image` | GitHub Release title |
| `armbian_release_body` | no | *(link to build tools)* | GitHub Release body text |
| `armbian_release_tag` | no | *auto* | GitHub Release tag; defaults to the computed version |
| `armbian_release_prerelease` | no | `false` | Publish the release as a pre-release (useful for matrix builds; promote later) |
| `armbian_download_base_url` | no | `https://dl.armbian.com` | Base URL where published images live (used to build the assets manifest URLs) |
| `armbian_download_repository` | no | `archive` | Repository segment under `<base>/<board>/<repo>/`; empty string gives a flat URL shape |
| `armbian_index_url` | no | `https://github.armbian.com/armbian-images.json` | Canonical `armbian-images.json` used to enrich entries; empty string skips enrichment |
| `armbian_artifacts` | no | `build/output/images/` | Path to artifacts for upload |
| `armbian_runner_clean` | no | — | Set to any non-empty value to free disk space on GitHub-hosted runners |

### Customisation

If your repository contains a `userpatches/` directory, it will be merged into the build framework automatically. This allows you to add custom kernel configs, patches, or overlay files without forking the main build repository.

---

**Previous:** [Overview](index.md)

**Next:** [Build commands](commands.md)

Reference: [build commands](commands.md), [build switches](switches/index.md), [user configurations](user-configurations.md), [board configuration](board-configuration.md), [extensions](extensions/index.md).
