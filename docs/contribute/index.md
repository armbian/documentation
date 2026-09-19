---
seo_title: "Armbian contributing: fork & pull requests"
description: "Contribute to Armbian on GitHub: fork the build, configng or documentation repositories, open issues and submit pull requests to the ARM Linux project."
---

# Get involved

## Ways to contribute

- **Fix or improve the code and documentation** — see
  [Submitting changes](#submitting-changes) below.
- [**Add software to armbian-config**](armbian-config.md) — write an install
  module and its menu entry.
- [**Add a new board or board family**](../build-framework/adding-a-board.md) to
  the build framework.
- [**Become a board maintainer**](board-maintainer.md) — keep a board supported,
  test release candidates and help its users. The
  [Board Support Rules](board-support-rules.md) define what each support tier
  requires.
- [**Run a mirror**](run-a-mirror.md) — host images and packages for the
  download network.

## Submitting changes

1. [Fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) the project.
1. Make one or more well commented and clean commits to the repository.
1. Perform a [pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) in Github's web interface.

If it is a new feature request, do not start the coding first. Remember to [open an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) to discuss the new feature. You can also [add code to someone else's pull request](https://tighten.co/blog/adding-commits-to-a-pull-request/). Also check the collection of [git tips](https://github.com/git-tips/tips) which will make your life easier.

If you are struggling, check the [WEB](https://www.exchangecore.com/blog/contributing-concrete5-github) or [CLI](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github) step-by-step guide on contributing.

## Source code

- Armbian build framework: <https://github.com/armbian/build>
- Armbian configuration utility: <https://github.com/armbian/configng>
- Armbian documentation: <https://github.com/armbian/documentation>

The [GitHub](../community/github.md) page lists the other project repositories.

## Roles and what they unlock

Contributing needs nothing but a GitHub account. Some project resources are
tied to a role:

| Role | What it unlocks |
| :--- | :-------------- |
| [Organization member](#organization-member) | [Member storage](storage.md) — public SFTP space for sharing images and packages |
| [Board maintainer](#board-maintainer) | [Datacenter access](datacenter.md) — remote access to real boards in the hardware lab |
| [Release manager](#release-manager) | Running the [release workflows](automation.md) that prepare images for release |

### Organization member

Every contributor is automatically invited to become a member of the
[Armbian organization](https://github.com/armbian) on GitHub. Contribute — for
example with a merged pull request — and accept the invitation that follows.

### Board maintainer

Board maintainers are members of the
[board-maintainers](https://github.com/orgs/armbian/teams/board-maintainers)
GitHub team. See [Become a board maintainer](board-maintainer.md) for how to
apply, the requirements, and what is expected of you.

### Release manager

This role has additional permission that allows preparation of images for release.

Release managers:
<https://github.com/orgs/armbian/teams/release-manager>
