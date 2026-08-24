---
title: "GH runners"
description: "Install and run GH runners on Armbian — GitHub runners for Armbian automation. Runs on ARM64 and x86 single-board computers."
image: /images/GHR001.png
category: "Armbian"
comments: true
---
# GH runners


<!--- section image START from tools/include/images/GHR001.png --->
![GH runners](/images/GHR001.png){ .app-logo }
<!--- section image STOP from tools/include/images/GHR001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://forum.armbian.com/)


<!--- header START from tools/include/markdown/GHR001-header.md --->
This module automates the installation, removal, and status checking of GitHub self-hosted runners for the Armbian project. It supports batch operations and user input through dialog prompts when running interactively.

<!--- header STOP from tools/include/markdown/GHR001-header.md --->


Install from **[armbian-config](/config/) → Software → Armbian → GH runners**

~~~ custombash title="CLI install"
armbian-config --cmd GHR001
~~~


<!--- footer START from tools/include/markdown/GHR001-footer.md --->
=== "Supported Commands"

- **`install`**  
  Installs one or more GitHub runners using the provided configuration or interactively prompted values.

- **`purge` / `remove`**  
  Removes runners based on the provided runner name series and target organization or repository.

- **`status`**  
  Quietly checks if any `actions.runner` services are currently running on the system.

=== "Available Switches"

| Switch             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `gh_token`         | GitHub token with admin rights to manage self-hosted runners.               |
| `runner_name`      | Name prefix for the runner series (default: `armbian`).                     |
| `start`            | Start index of the runner series (e.g., `01`).                              |
| `stop`             | End index of the runner series (e.g., `05`).                                |
| `label_primary`    | Labels for the first runner (default: `alfa`).                              |
| `label_secondary`  | Labels for additional runners (default: `fast,images`).                     |
| `organisation`     | GitHub organization name (default: `armbian`).                              |
| `owner`            | GitHub user or organization owner (used for repo-level runners).            |
| `repository`       | GitHub repository name (used for repo-level runners).                       |

=== "Behavior"

- Prompts the user for missing switches via `dialog` **only in interactive mode**.
- Supports bulk installation of runners using sequential numbering (`start` to `stop`).
- Calls internal `actions.runner.install` and `actions.runner.remove` helpers.
- Returns `0` if any runner services are active, `1` otherwise (for scripting use).
- Suppresses errors and outputs when checking status to remain quiet in background use.

<!--- footer STOP from tools/include/markdown/GHR001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_armbian_runners install` |
| Remove GitHub runners for Armbian automation | `armbian-config --api module_armbian_runners remove` |

---

_Part of Armbian's [Armbian infrastructure services](/User-Guide_Armbian-Software/Armbian/) software._
