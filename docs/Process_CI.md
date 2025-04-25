# Automation for developers and maintainers

Core automation for generating images for release are held at <https://github.com/armbian/os>


## Prepare build lists


### Recommended images

Recommended images on download pages are defined via regular expression mapping file <https://github.com/armbian/os/blob/main/exposed.map> (for changes sent PR to this file)

Example:

```
bananapim7/archive/Armbian_[0-9].*Bananapim7_noble_vendor_[0-9]*.[0-9]*.[0-9]*_gnome-kisak_desktop.img.xz
bananapim7/archive/Armbian_[0-9].*Bananapim7_bookworm_vendor_[0-9]*.[0-9]*.[0-9]*_minimal.img.xz
```

![Standard support images](images/standard-support-images.png)

### Build templates

They have definitions on what kind of images we want to build - for section or for one specific board:

``` yaml
userpatches/targets-release-apps.template
userpatches/targets-release-community-maintained.template
userpatches/targets-release-nightly.template
userpatches/targets-release-standard-support.template
```

From those templates we are [autogenerating](https://github.com/armbian/os/blob/main/.github/workflows/recreate-matrix.yml#L147-L438) YAML files, which are passed to build matrix as input. Make sure to review generated YAML files if they have wanted build targets with correct exensions enabled.

### Grouping logic

Boards are automatically divided into sections and each section is appendend to certain build scenario (minimal Debian image, Ubuntu testing with KDE, ...), which is defined in template.

Section | Condition |
|:--|:--|
| standard-support-slow-hdmi | HAS_VIDEO_OUTPUT = yes AND ARCH = armhf | 
| standard-support-fast-hdmi | HAS_VIDEO_OUTPUT = yes AND ARCH = arm64|amd64 |
| standard-support-headless | HAS_VIDEO_OUTPUT = no | 
| standard-support-riscv64 | ARCH = riscv64 | 

Example: if you want automated images without a desktop, add `HAS_VIDEO_OUTPUT=no` in board config file. Automation will only build two CLI images, Ubuntu server and Debian minimal. Which is suitable for hardware that will most likely be used headless.

### Blacklisting

Autogeneration is excluded for boards that are on blacklists:

``` yaml
userpatches/targets-automation.blacklist
userpatches/targets-automation-nightly.blacklist
```

We do this if we are not happy with the automation outcomes and want to define build targets in the template.

### Extensions

Each board variant can have additional extensions and they are defined in this file:

```
userpatches/targets-extensions.map
```

Example:

```
khadas-edge2,legacy:vendor:,ENABLE_EXTENSIONS="image-output-oowow,v4l2loopback-dkms,mesa-vpu"
```

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
- you can only generate images that are defined in [targets-release-standard-support.yaml](https://github.com/armbian/os/blob/main/userpatches/targets-release-standard-support.yaml) build lists!
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

Generates stable images defined in [targets-release-standard-support.yaml](https://github.com/armbian/os/blob/main/userpatches/targets-release-standard-support.yaml). 



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
- you can only generate images for applications that are defined in [targets-release-apps.yaml](https://github.com/armbian/os/blob/main/userpatches/targets-release-apps.yaml) build lists!
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

Generates dedicated application images defined in [targets-release-apps.yaml](https://github.com/armbian/os/blob/main/userpatches/targets-release-apps.yaml). This file is [autogenerated](https://github.com/armbian/os/blob/main/.github/workflows/recreate-matrix.yml#L147-L438) from [targets-release-apps.template](https://github.com/armbian/os/blob/main/userpatches/targets-release-apps.template). (You always edit template)

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

Generates all nighly (Rolling Release) images defined in [targets-release-nightly.yaml](https://github.com/armbian/os/blob/main/userpatches/targets-release-nightly.yaml).  This file is [autogenerated](https://github.com/armbian/os/blob/main/.github/workflows/recreate-matrix.yml#L147-L438) from [targets-release-nightly.template](https://github.com/armbian/os/blob/main/userpatches/targets-release-nightly.template). 

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
