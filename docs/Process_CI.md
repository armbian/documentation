# Automation for developers and maintainers

Core automation for generating images for release are held at <https://github.com/armbian/os>

???+ Note
    For monitoring all action scripts status and execution details, visit [https://actions.armbian.com/](https://actions.armbian.com/)


## Prepare build lists


### Recommended images

Recommended images on download pages are defined via regular expression mapping file <https://github.com/armbian/os/blob/main/exposed.map> (for changes sent PR to this file)

Example:

```
bananapim7/archive/Armbian_[0-9].*Bananapim7_noble_vendor_[0-9]*.[0-9]*.[0-9]*_gnome-kisak_desktop.img.xz
bananapim7/archive/Armbian_[0-9].*Bananapim7_bookworm_vendor_[0-9]*.[0-9]*.[0-9]*_minimal.img.xz
```

![Standard support images](images/standard-support-images.png)

### Target generation

Build target YAML files are automatically generated from `image-info.json` at <https://github.com/armbian/armbian.github.io>. The generation script classifies boards by hardware capabilities and creates appropriate build targets.

Generated files:
- `targets-release-apps.yaml` - One image per board with app-specific extensions
- `targets-release-standard-support.yaml` - Full stable/release builds
- `targets-release-nightly.yaml` - Nightly builds with hardware-based desktop selection
- `targets-release-community-maintained.yaml` - Community/CSC/TVB board builds

???+ Note
    For changes to target generation logic, submit PR to [armbian.github.io](https://github.com/armbian/armbian.github.io)

### Hardware-based board classification

Boards are automatically classified by hardware speed and architecture to determine appropriate desktop environments:

**Category** | **Condition** | **Desktop (nightly/community)**
|:--|:--|:--|
| **Fast HDMI** | ARM64/x86 with video, not in slow list | GNOME |
| **Slow HDMI** | ARM 32-bit or specific slower SoCs | XFCE |
| **Headless** | Boards without video output | CLI only |
| **RISC-V** | ARCH = riscv64 | CLI only |
| **LoongArch** | ARCH = loongarch64 | CLI only (sid only) |

**Slow hardware list** (gets XFCE):
- ARM 32-bit (arm/armhf) architecture
- Allwinner H3/H5/H6 (sun50iw*, sun55iw*)
- Amlogic S905X/S912/S905X2/S922X/A311D (meson-gxbb, meson-gxl, meson-g12a, meson-g12b, meson-sm1)
- Nuvoton MA35D1
- Rockchip RK3328/RK3399/RK3399PRO

All other ARM64 and x86 boards with video are classified as **fast** (gets GNOME).

### Automatic extensions

Fast HDMI boards automatically receive these extensions:
- `v4l2loopback-dkms` - Video4Linux loopback device support
- `mesa-vpu` - VPU driver for video acceleration

These can be supplemented with manual extensions via the extensions map.

### Manual overrides

**Blacklisting** - exclude boards from automatic generation:

``` yaml
release-targets/targets-release-nightly.blacklist
release-targets/targets-release-community-maintained.blacklist
```

**Manual targets** - add custom build targets:

``` yaml
release-targets/targets-release-nightly.manual
release-targets/targets-release-community-maintained.manual
```

**Extensions** - add board-specific extensions:

```
release-targets/targets-extensions.map
```

Format:
```
BOARD_NAME:branch1:branch2:...:ENABLE_EXTENSIONS="ext1,ext2"
```

Example:
```
khadas-edge2:legacy:vendor:,ENABLE_EXTENSIONS="image-output-oowow,v4l2loopback-dkms,mesa-vpu"
```

Wildcards apply to all branches:
```
BOARD_NAME::ENABLE_EXTENSIONS="ext1,ext2"
```

???+ Note
    Manual extensions are **merged** with automatic extensions, not replaced.
### Kernel Descriptions for Download Pages?

Each kernel branch can include an optional description, stored in [`kernel-description.json`](https://github.com/armbian/os/blob/main/kernel-description.json).

### Testing

Unfortunatelly this part does not have testing at PR stage.

## Prepare Standard Support images for release

???+ Info
    Manual executing permissions are tied to [release manager role](/Process_Contribute/#release-manager).

[![Build Standard Support Images](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-standard-support.yml/badge.svg)](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-standard-support.yml)

This build workflow is executed manually when making:

- a set of images for specific device
- a set of images for specific maintainer
- a full set of stable release images (default)

**Notes**:

- this process prepares images for release without pushing them to the download pages
- you can only generate images that are defined in [targets-release-standard-support.yaml](https://github.com/armbian/armbian.github.io/blob/main/release-targets/targets-release-standard-support.yaml) build lists!
- images generation workflows are compiled and are pretty much the same, just with different defaults

### 1. Open [workflow](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-standard-support.yml) and click

![Run Workflow](images/run-workflow.png)

### 2. Select board

![Workflow](images/complete-artifact-matrix-standard-support.png)

**Bump version**: Select if you want to trigger system wide version bump.
**Version override**: Set version under which you want to release images.

Images versions are stored in JSON files:
- https://github.com/armbian/os/blob/main/stable.json
- https://github.com/armbian/os/blob/main/nightly.json

### 3. Run workflow

![Build](images/run-worflow-button.png)

**(Workflow takes around 15 minutes to complete. In case of network issues it can also take hours)**

Generated images are uploaded to incoming folder [https://rsync.armbian.com/incoming/](https://rsync.armbian.com/incoming/) under **your GitHub username** and once they are confirmed working, please notify [@igorpecovnik](https://github.com/igorpecovnik) to move them to official download pages. Once images are moved to [main download section](https://www.armbian.com/download/), automation refreshes download pages index within 15-30 minutes.

### Aditional options

Generates stable images defined in [targets-release-standard-support.yaml](https://github.com/armbian/armbian.github.io/blob/main/release-targets/targets-release-standard-support.yaml). 



We are generating several images for each download / hardware target. They are automatically sorted by sections:

- Desktop releases
- Server and IOT releases
- Dedicated applications

Images generation can be customized:

- Framework build branch
  - main (make images from trunk)
  - vXX.X (previous stable release)
- Bump Version (system wide version bump)
- Version override (in case you don't want to use latest)
- Board (make images for one board only)
- Maintainer (make images for selected maintainer)

## Prepare application images for release (release manager)

[![Build Dedicated Application Images](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-apps.yml/badge.svg)](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-apps.yml)

This build workflow is executed manually when making:

- a set of application images for specific device
- a set of application images for specific maintainer
- a full set of application images (default)

**Notes**:

- **application images are released 10-15 minutes after build finishes succesfully**
- you can only generate images for applications that are defined in [targets-release-apps.yaml](https://github.com/armbian/armbian.github.io/blob/main/release-targets/targets-release-apps.yaml) build lists!
- images generation workflows are compiled and are pretty much the same, just with different defaults

### 1. Open [workflow](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-apps.yml) and click

![Run Workflow](images/run-workflow.png)

### 2. Select board

![Workflow](images/complete-artifact-matrix-standard-support.png)

**Version override**: Use this feature if you want to keep them under the same version, but not lower then [last released](https://docs.armbian.com/Release_Changelog/#changelog).

### 3. Run workflow

![Build](images/run-worflow-button.png)

**(Workflow takes around 15 minutes to complete. In case of network issues it can also take hours)**

Generated images are hosted at GitHub [https://github.com/armbian/distribution/releases](https://github.com/armbian/distribution/releases) and released at once. Automation refreshes download pages within 15-30 minutes after/if workflow finished succesfully.

![Dedicated Application Images](images/dedicated-applications.png)

### Aditional options

Generates dedicated application images defined in [targets-release-apps.yaml](https://github.com/armbian/armbian.github.io/blob/main/release-targets/targets-release-apps.yaml). This file is automatically generated from `image-info.json` by the [generate-targets workflow](https://github.com/armbian/armbian.github.io/blob/main/.github/workflows/generate-targets.yaml).

Images generation can be customized:

- framework build branch
  - main (make images from trunk)
  - vXX.X (previous stable release)
- Bump Version (system wide version bump)
- Version override (in case you don't want to use latest)
- board (make images only for one board)
- maintainer (make images for selected maintainer)

## Repository update (cronjob/release manager)

This pulls packages from build framework OCI cache located at GitHub and from [various 3rd party repositories](https://github.com/armbian/os/wiki/Import-3rd-party-packages) such as Chrome, Chromium, Code, Discord, (latest) ZFS, Thunderbird, Zoom, ... and pushes them to:

- `apt.armbian.com` (only new packages are added)
- `beta.armbian.com` (whole repository is recreated from scratch)

### 1. Open [workflow](https://github.com/armbian/os/actions/workflows/repository-update.yml) and click

![Run Workflow](images/run-workflow.png)

Action is executed automatically when artifact generations completes. Or manually.

### 2. Include [artifacts from generated image(s)](https://netcup.armbian.com/partial/)

When
- [ ] Add https://netcup.armbian.com/partial/ to stable repo
      
is selected.

### 3. Run workflow

![Build](images/run-worflow-button.png)

**(Workflow takes around 60 minutes to complete)**

## Build all artifacts (cronjob)

[![Build All Artifacts](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-all.yml/badge.svg)](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-all.yml)

Generates all build artifacts cache for targets defined in [targets-all-not-eos.yaml](https://github.com/armbian/os/blob/main/userpatches/targets-all-not-eos.yaml). This build job runs **every 8 hours** and can also be run manually when needed. 

This build job **needs to be successfully completed** in order to proceed generating any OS images!

## Build Rolling Release Images (cronjob)

[![Build Nightly Images](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-nightly.yml/badge.svg)](https://github.com/armbian/os/actions/workflows/complete-artifact-matrix-nightly.yml)

Generates all nightly (Rolling Release) images defined in [targets-release-nightly.yaml](https://github.com/armbian/armbian.github.io/blob/main/release-targets/targets-release-nightly.yaml). This file is automatically generated from `image-info.json` by the [generate-targets workflow](https://github.com/armbian/armbian.github.io/blob/main/.github/workflows/generate-targets.yaml). 

This build job runs every day at 9 a.m. UTC and can also be run manually when needed. Download pages are refreshed [automatically](https://github.com/armbian/os/actions/workflows/webindex-update.yml) after successful build.

![Build](images/rolling-releases.png)

## Watchdog (cronjob)

Runs every 15 minutes and re-trigger [failed builds](https://github.com/armbian/os/blob/main/.github/workflows/watchdog.yml#L26) six (6) times before finally gives out. This addresses various instabilities when building many artifacts on different hardware: 

- network timeouts
- artifact download failure
- loop devices allocation failure
- runner running low on space

## Smoke tests on hardware devices (release manager)

Smoke testing is preliminary testing to reveal simple failures severe enough to, for example, reject a prospective software release. Our test case is constructed of three steps:

![Smoke](images/smoke-tests.png)

- powering test equipment, consistent from several network switches, power supplies and dozens of hardware platforms
- running upgrade, reboot, repository switch, reboot, ... tests in parallel
- uploading a test report as build artifact followed by powering the devices off.

## Automatic Pull Requests Labeler (PR)

[![Automatic Labeler](https://github.com/armbian/build/actions/workflows/labeler.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/labeler.yml)

Automatically label new pull request based on the paths of files which are being changed. Configuration file can be found in:

        .github/labeler.yml

## Full distro test builds (cronjob/release manager)

[![Build Nightly Images](https://github.com/armbian/os/actions/workflows/full-distro-build-and-test.yml/badge.svg)](https://github.com/armbian/os/actions/workflows/full-distro-build-and-test.yml)

Generates all supported build combinations (minimal, cli, desktops) for x86 architecture to check package level changes inconsistency and dependencies.

Options:

- Framework build branch
  - **main**
  - testing_branch (string)

## Build all artifacts (admin/PR)

Generates artifacts at Pull Requests code. Build starts when label of Pull Request is set to "Build". Requires administration privileges.

## Lint on shell scripts (PR)

[![Lint On Shell Scripts](https://github.com/armbian/build/actions/workflows/pr-lint-scripts.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/pr-lint-scripts.yml)

![Lint](images/linterror.png)

Run [ShellCheck](https://github.com/koalaman/shellcheck) on changed shell scripts and report problems within. Linting runs automatically on pull requests.

## Update tools in build scripts (cronjob/admin)

[![Update Tools in Scripts](https://github.com/armbian/build/actions/workflows/update-tools.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/update-tools.yml)

Some of our scripts download tools from a repo. These cannot be bumped by Dependabot, so this workflow is a self-created Dependabot to bump versions of those tools to stay up-to-date. This workflow only creates a PR if the version was actually updated. To add a new tool, it just needs to be added to the matrix [in the script](https://github.com/armbian/build/blob/main/.github/workflows/update-tools.yml) by filling out all the variables.

## Scorecards security scan (PR)

[![Scorecards Security Scan](https://github.com/armbian/build/actions/workflows/scorecard.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/scorecard.yml)

[Scorecards](https://github.com/ossf/scorecard#what-is-scorecards) is an automated tool that assesses a number of important heuristics ("checks") associated with software security and assigns each check a score of 0-10. You can use these scores to understand specific areas to improve in order to strengthen the security posture of your project. You can also assess the risks that dependencies introduce, and make informed decisions about accepting these risks, evaluating alternative solutions, or working with the maintainers to make improvements.

## Kernel hardening analysis (PR)

[![Kernel Hardening Analysis](https://github.com/armbian/build/actions/workflows/pr-kernel-security-analysis.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/pr-kernel-security-analysis.yml)

This [analysis](https://github.com/a13xp0p0v/kconfig-hardened-check/blob/master/README.md) checks kernel configs and run if changed. There are plenty of security hardening options for the Linux kernel. A lot of them are not enabled by the major distros. We have to enable these options ourselves to make our systems more secure.
