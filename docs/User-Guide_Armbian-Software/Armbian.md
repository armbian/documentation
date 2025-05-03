---
comments: true
---

# Armbian infrastructure services

## CDN router


Router for repository mirror automation


<!--- section image START from tools/include/images/ART001.png --->
[![CDN router](/images/ART001.png)](#)
<!--- section image STOP from tools/include/images/ART001.png --->


<!--- header START from tools/include/markdown/ART001-header.md --->
The Armbian Router is an intelligent redirector system that optimizes file downloads by automatically directing users to the best available mirror. It evaluates each download request based on geographic location, server health, and file availability, ensuring faster downloads, balanced load distribution, and high availability. This core service underpins Armbian's scalable mirror network, seamlessly routing traffic to improve performance and reliability for end users worldwide.

<!--- header STOP from tools/include/markdown/ART001-header.md --->

**Author:** @efectn

**Status:** Stable


~~~ custombash
armbian-config --cmd ART001
~~~


~~~ bash title="Remove CDN router:"
armbian-config --cmd ART002
~~~



## GH runners


GitHub runners for Armbian automation


<!--- section image START from tools/include/images/GHR001.png --->
[![GH runners](/images/GHR001.png)](#)
<!--- section image STOP from tools/include/images/GHR001.png --->


<!--- header START from tools/include/markdown/GHR001-header.md --->
This module automates the installation, removal, and status checking of GitHub self-hosted runners for the Armbian project. It supports batch operations and user input through dialog prompts when running interactively.

<!--- header STOP from tools/include/markdown/GHR001-header.md --->

**Author:** @efectn

**Status:** Stable


~~~ custombash
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


~~~ bash title="Remove GitHub runners for Armbian automation:"
armbian-config --cmd GHR002
~~~



## Rsyncd server

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash
armbian-config --cmd RSD001
~~~


~~~ bash title="Remove Armbian rsyncd server:"
armbian-config --cmd RSD002
~~~


