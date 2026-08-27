---
seo_title: "Become an Armbian board maintainer"
description: "Become an Armbian board maintainer: application steps, requirements and release responsibilities for testing and signing off single-board computer images."
---

# Board Maintainers

## How to become a maintainer?

If you are interested in being a maintainer please review [Board Support Rules](/contribute/board-support-rules/). Then [apply here](https://forum.armbian.com/staffapplications/application/8-single-board-computer-maintainer/) and wait for acceptance. Once accepted you will be added to our infrastruture. For this reason we need [additional information](https://www.armbian.com/maintainer-registry/) to complete your registration process.

!!! question "Requirements?"

    - You must have access to the hardware you applied to maintain
    - You must have a Github ID which should be listed in the documentation
    - You must have a forums account
    - You must keep track of the [GitHub issues](https://github.com/armbian) filed for your board
    - You must make sure [Armbian management](https://www.armbian.com/maintainer-registry/) has been informed of all of the above IDs for our documentation
    - You should know Armbian basics like how to get an Armbian image run on your hardware and do basic debugging, ideally via serial console
    - Knowledge in development, writing code and so on is optional but welcome

## Expectations

Maintainers must not necessarily be persons with development experience. They act as a intersection between end-users and the development team and serve the developers in best-effort manner. They are encouraged to answer basic/simple user questions (if possible, also best effort) without having to bother the development team. They are allowed to record bugs but are not allowed to escalate bugs. Team leaders do.

Take note that it is still up to development team's discretion what gets attention since Armbian has to plan carefully how to spend its very limited resources.

- You must participate in release process. Ideally you attend meetings related to releases. On that occasion you are given the chance to point out critical issues with your board.
- You must sign-off that device has been tested, is stable, and ready for release during release process. This basically means you test images that are getting prepared for release <https://rsync.armbian.com/incoming/>

!!! question "What are we looking for?"

    - does the board boot to both CLI and Desktop?
    - is the desktop usable?
    - does USB work? (at all or partially)
    - other things such as wireless, audio

If something does not work, this is fine and normal. The important part is that it is documented and we get notified about the issues. Known problems should be filed as a GitHub issue and linked from the board download page. While not required, you should have a build environment setup so you can build images with the most recent images and test them right away. Your feedback, either positive or negative, is very welcome. You are free to add comments to every commit and pull request.

Ideally you have multiple microSD cards laying around to test regular updates on current releases and nightly without having to re-flash the same card every time to switch between branches.

Alternatively you can use auto-built images - they are placed at the ever end of each board download pages under "Rolling releases".

- You must provide "best effort" support in the forum. Do not let that wording intimidate you. This is not a complicated task. Regarding forums this can include things like answering obvious questions (for example by pointing to our documentation, ideally directly to the solution page), let the questioner know that additional information is needed for further debugging (e.g. request "armbianmonitor -u" output) or for upgrade issues, ask if they can recreate the issue with a fresh untouched image from: <https://www.armbian.com/download/>

- You must provide "best effort" support on GitHub — review the issues submitted for your board by Armbian's contributors.

## During a release

Release meetings happen about four times a year, roughly a month before each release (end of February, May, August, November) — see the [release model](/releases/release-model/). Attending is optional, but you **must** sign off that your board has been tested and is ready, by filling in the [Release Testing Form](https://www.armbian.com/rc-testing/) for each release candidate.

## Issue priority

A rough guide when triaging issues filed for your board:

**Low priority** — usually picked up by the community over time:

- Wi-Fi (missing modules, AP mode, …)
- Bluetooth
- GPIO, I²C
- hardware accelerators (crypto, VPU / video)
- device-tree overlays

**High priority** — worth flagging to the team promptly:

- the image does not boot
- the image or its packages are corrupt
- SD card or eMMC is not working as expected

Collect as much detail as you can (logs, `armbianmonitor -u`, the exact image) before filing, and ask the reporter for anything still missing.

## Losing support status

As noted in the [Board Support Rules](board-support-rules.md), a board's support status is revoked for at least the current **and** upcoming release cycle(s) if a **"must"** from the responsibilities above is not fulfilled.