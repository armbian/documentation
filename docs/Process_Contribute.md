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

If you are interested in being a maintainer please review [Board Support Rules](/User-Guide_Board-Support-Rules/). Then [apply here](https://forum.armbian.com/staffapplications/application/8-single-board-computer-maintainer/) and wait for acceptance. Once accepted you will be added to our infrastructure. For this reason we need [additional information](https://www.armbian.com/maintainer-registry/) to complete your registration process.

!!! question "Requirements?"

    - You must have access to the hardware you applied to maintain
    - You must have a Github ID which should be listed in the documentation
    - You must have a forums account
    - You must have an Jira account and keep track of issues filed for your board
    - You must make sure [Armbian management](https://www.armbian.com/maintainer-registry/) has been informed of all of the above IDs for our documentation
    - You should know Armbian basics like how to get an Armbian image run on your hardware and do basic debugging, ideally via serial console
    - Knowledge in development, writing code and so on is optional but welcome

### Expectations

Maintainers must not necessarily be persons with development experience. They act as a intersection between end-users and the development team and serve the developers in best-effort manner. They are encouraged to answer basic/simple user questions (if possible, also best effort) without having to bother the development team. They are allowed to record bugs but are not allowed to escalate bugs. Team leaders do.

Take note that it is still up to development team's discretion what gets attention since Armbian has to plan carefully how to spend its very limited resources.

- You must participate in release process. Ideally you attend meetings related to releases. On that occasion you are given the chance to point out critical issues with your board.
- You must sign-off that device has been tested, is stable, and ready for release during release process. This basically means you test images that are getting prepared for release <https://rsync.armbian.com/incoming/>

!!! question "What are we looking for?"

    - does the board boot to both CLI and Desktop?
    - is the desktop usable?
    - does USB work? (at all or partially)
    - other things such as wireless, audio

If something does not work, this is fine and normal. The important part is that it is documented and we get notified about the issues. Known problems should be placed into the Jira ticket and link placed to the board download page. While not required, you should have a build environment setup so you can build images with the most recent images and test them right away. Your feedback, either positive or negative, is very welcome. You are free to add comments to every commit and pull request.

Ideally you have multiple microSD cards laying around to test regular updates on current releases and nightly without having to re-flash the same card every time to switch between branches.

Alternatively you can use auto-built images - they are placed at the ever end of each board download pages under "Rolling releases".

- You must provide "best effort" support in the forum. Do not let that wording intimidate you. This is not a complicated task. Regarding forums this can include things like answering obvious questions (for example by pointing to our documentation, ideally directly to the solution page), let the questioner know that additional information is needed for further debugging (e.g. request "armbianmonitor -u" output) or for upgrade issues, ask if they can recreate the issue with a fresh untouched image from: <https://www.armbian.com/download/>

- You must provide "best effort" support in Jira. Review submitted issues for you board made by Armbian's contributors

## Release manager

This role has additional permission that allows preparation of images for release.

Release managers:
<https://github.com/orgs/armbian/teams/release-manager>
