# Automatic or Manual Firmware Compilation

[![Build train](https://github.com/armbian/build/actions/workflows/build-train.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/build-train.yml)

Generates kernels at code push if their code, patches or config was changed in any way. It is also triggered via cron in the middle of CET night.

![Build](images/build-train.png)

Build train is executed only if there are changed kernels. When this happens, it also generates armbian-firmware, desktop and u-boot packages. If build succeeds it pushes packages to the package repository and increments trunk build version.

- generates all changed kernels,
- generate all boot loaders for all supported hardware,
- generate desktop pacakages,
- generates armbian-firmware, armbian-zsh, armbian-config.

You can change source repository and you can change destination package repository to https://beta.armbian.com (default) or https://apt.armbian.com

Manual Executing rights: [Armbian project member](https://github.com/orgs/armbian/people)

# Automatic or Manual Images Compilation

[![Build Images](https://github.com/armbian/build/actions/workflows/build-images.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/build-images.yml)

![Build](images/build-all-images.png)

Automatically generates all beta images after firmware compilation was succesfull. It only rebuild images if changes were made.

- can build release candidate or stable images,
- can select build source repository,
- can choose packages source repository apt.armbian.com or beta.armbian.com,
- can build images for one or more boards with targets defined in [this configuration](https://github.com/armbian/build/blob/master/config/targets.conf).

Manual executing rights: [Armbian release manager](https://forum.armbian.com/staffapplications/application/11-release-manager/)

# Automatic Pull Requests Labeler

[![Automatic Labeler](https://github.com/armbian/build/actions/workflows/labeler.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/labeler.yml)

Automatically label new pull request based on the paths of files which are being changed. Configuration file can be found in:

        .github/labeler.yml

# Manual Pull Requests rebase

[![Automatic Rebase](https://github.com/armbian/build/actions/workflows/rebase.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/rebase.yml)

Pull most recent code from master branch and put your work on top of your pull request.

How to use it? Simply comment 

       /rebase

to trigger the action.

- [Advantages of Git Rebase](https://itnext.io/advantages-of-git-rebase-af3b5f5448c6),
- [Automatic Rebase Action origin](https://github.com/marketplace/actions/automatic-rebase).

# Automatic or Manual Desktops Test Builds

[![Build All Desktops](https://github.com/armbian/build/actions/workflows/build-all-desktops.yml/badge.svg)](https://github.com/armbian/build/actions/workflows/build-all-desktops.yml)

Generates all desktops for arm64 and x86 arhitecture to verify if they build correctly. Build is triggered every day, manually (by [any member of Armbian project](https://github.com/orgs/armbian/people)) or in pull requests if label "Desktop" is set. Aim of this test case is to find out if there are troubles in packages relations.

- releases: bullseye, sid, jammy, focal,
- desktop environments: xfce, gnome, mate, cinnamon, budgie, kde-plasma,
- builds are not using cached rootfs to force packages assembly,
- included applications paths are "3dsupport browsers",
- builds are done with [Docker image](https://github.com/orgs/armbian/packages?repo_name=build) on public runners.

# Automatic Kernel Build at Pull Requests

Generates kernels at Pull Requests if their code, patches or config was changed. Build starts when label of Pull Request is set to "Ready"

# Integrity testings

This action tests package integrity from all stable images at download section.

Manual Executing rights: [Armbian project member](https://github.com/orgs/armbian/people)

# Forked Helper

- Run repository dispatch to default fork branch
- Dispatch event on forked repostitory

# Lint On Scripts

Run [ShellCheck](https://github.com/koalaman/shellcheck) on all scripts and generates report as a build artefact. Since our scripts are full of shellcheck problems we don't stop this action on errors. Not yet. For now, a report is generated. One has to download artefacts to see where the problems are.

Linting is run automatically on every push, including pull requests.

# Scorecards Security Scan

Scorecards is an automated tool that assesses a number of important heuristics ("checks") associated with software security and assigns each check a score of 0-10. You can use these scores to understand specific areas to improve in order to strengthen the security posture of your project. You can also assess the risks that dependencies introduce, and make informed decisions about accepting these risks, evaluating alternative solutions, or working with the maintainers to make improvements.

https://github.com/ossf/scorecard#what-is-scorecards

# Smoke tests on hardware devices

Smoke testing is preliminary testing to reveal simple failures severe enough to, for example, reject a prospective software release. Our test case is conducted of three steps:

![Smoke](images/smoke-tests.png)

- powering test equipment, consistent from several network switches, power supplies and dosents of hardware
- running upgrade, reboot, repository switch, reboot, ... tests in parallel
- uploading a test report as build artefact following by powering the devices off.

Executing rights: [Any member of Armbian project](https://github.com/orgs/armbian/people)
