# Armbian Build Framework Quick Start Guide

## Requirements

- x86_64 / aarch64 / riscv64 machine
- at least 8GB (less for non-[BTF](https://docs.kernel.org/bpf/btf.html) builds) of memory and ~50GB of disk space for VM, container, or bare-metal installation
- **Armbian / Ubuntu Noble 24.04.x** for native building or any Docker capable Linux for containerised
- **Windows 10/11 with WSL2 subsystem** running Armbian / Ubuntu Noble 24.04.x
- Superuser rights (configured sudo or root access).
- Make sure your system is up-to-date! Outdated Docker binaries, for example, can cause trouble


## Clone repository

```bash
git clone https://github.com/armbian/build
cd build
```
!!! note
    - Make sure that full path to the build script **does not contain spaces**
    - For stable branch use last point release `--branch=v24.11`


    ``` mermaid
    gitGraph
       commit
       commit
       checkout main
       commit id: "v24.08" tag: "v24.08"
       branch v24.08
       commit
       commit
       commit
       commit
       checkout main
       commit id: "v24.11" tag: "v24.11"
       branch v24.11
       commit
       commit
       commit
       commit
       checkout main
       commit
       commit
       commit
       commit
       commit
       commit
       commit id: "main" type: REVERSE tag: "Trunk"
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

Comprehensive list of build [Commands](Developer-Guide_Build-Commands.md) and [Switches](Developer-Guide_Build-Switches.md)

Example:

```bash
./compile.sh build \
BOARD=uefi-x86 \
BRANCH=current \
BUILD_DESKTOP=yes \
BUILD_MINIMAL=no \
DESKTOP_APPGROUPS_SELECTED='browsers chat desktop_tools' \
DESKTOP_ENVIRONMENT=gnome \
DESKTOP_ENVIRONMENT_CONFIG_NAME=config_base \
KERNEL_CONFIGURE=no \
RELEASE=noble
```

Or, using config file `userpatches/config-myboard.conf`
that sets all these switches:

```bash
./compile.sh build \
myboard
```

!!! question "Interpretation?"

    This command will generate **Ubuntu 24.04 Noble** based **Gnome desktop** environment image for Intel based hardware (**uefi-x86**). Besides bare desktop, it will contain packages from **browsers** and **desktop_tool** sections and it will use unchanged kernel from **current kernel** branch.


## Logging


Logs are written to **output/logs**. Old logs (all but the current build)
are compressed and moved to **output/logs/archive**.

Log formats are:

- ANSI - text with ANSI escapes for color coding - \*.log.ans
- ASCII (if ansi2txt is available) - text without color coding escapes - \*.log
- Markdown summary - \*.md
- Raw (if RAW_LOG=yes) - tar file containg all the raw logs - \*.raw.tar

For much more verbose logs set switch 'DEBUG=yes'.

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
| `armbian_artifacts` | no | `build/output/images/` | Path to artifacts for upload |
| `armbian_runner_clean` | no | — | Set to any non-empty value to free disk space on GitHub-hosted runners |

### Customisation

If your repository contains a `userpatches/` directory, it will be merged into the build framework automatically. This allows you to add custom kernel configs, patches, or overlay files without forking the main build repository.
