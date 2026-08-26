---
seo_title: "Armbian build target switches: BOARD, BRANCH, RELEASE"
description: "Select what the Armbian build framework builds: BOARD, kernel BRANCH (vendor, legacy, current, edge) and the Debian or Ubuntu RELEASE."
---

# Target

Which board, kernel branch and userspace release to build. Set these to skip the interactive dialog.

#### BOARD

`string`

Set the board manually to skip the dialog prompt. The value is [a board config filename without its extension](https://github.com/armbian/build/tree/main/config/boards) — e.g. `BOARD=bananapim5` loads `config/boards/bananapim5.conf`. See [Board configuration](/build-framework/board-configuration/) for what a board file defines.

#### BRANCH

`string`

- `vendor`
- `legacy`
- `current` (recommended)
- `edge`

Set the kernel and U-Boot branch manually to skip the dialog prompt.

!!! tip "Note"
    Some branches may not be available for all devices.

#### RELEASE

`string`

Supported:

- `trixie` (Debian 13)
- `noble` (Ubuntu 24.04)
- `resolute` (Ubuntu 26.04)

Community supported:

- `bookworm` (Debian 12)
- `forky` (Debian 14)
- `sid` (Debian unstable)
- `jammy` (Ubuntu 22.04)

Set the userspace release base manually to skip the dialog prompt. Each release carries its own support status in [`config/distributions/<release>/support`](https://github.com/armbian/build/tree/main/config/distributions); releases marked `eos` there are end of service and are not listed here.

!!! tip "Note"
    Only stable and/or LTS upstream Debian or Ubuntu releases are officially supported. Others might work or not.
