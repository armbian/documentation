---
seo_title: "Armbian contributing: fork & pull requests"
description: "Contribute to Armbian on GitHub: fork the build, configng or documentation repositories, open issues and submit pull requests to the ARM Linux project."
---

# Collaborate on the project

## Overview

1. [Fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) the project.
1. Make one or more well commented and clean commits to the repository. 
1. Perform a [pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) in Github's web interface.

If it is a new feature request, do not start the coding first. Remember to [open an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) to discuss the new feature. If you want to [add code to someone else pull request](https://tighten.co/blog/adding-commits-to-a-pull-request/). Also check collection of [git tips](https://github.com/git-tips/tips) which will make your life easier.

If you are struggling, check [WEB](https://www.exchangecore.com/blog/contributing-concrete5-github) or [CLI](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github) step-by-step guide on contributing.

## Source code

- Armbian build framework: <https://github.com/armbian/build>
- Armbian configuration utility: <https://github.com/armbian/configng>
- Armbian documentation: <https://github.com/armbian/documentation>


## Adding a new board?

There are no detailed instructions on how to add a new board or even a whole new board family to the build script yet. However there are a few commits / pull requests that give clues how to achieve that like

- [https://github.com/armbian/build/pull/3176/files](https://github.com/armbian/build/pull/3176/files)
- [https://github.com/armbian/build/pull/3138/files](https://github.com/armbian/build/pull/3138/files)

## Board maintainer

Interested in keeping a board supported? See [**Become a board maintainer**](board-maintainer.md) for how to apply, the requirements, and what is expected of you — and the [Board Support Rules](board-support-rules.md).

## Release manager

This role has additional permission that allows preparation of images for release.

Release managers:
<https://github.com/orgs/armbian/teams/release-manager>
