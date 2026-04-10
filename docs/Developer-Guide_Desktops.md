# Desktops

Technical reference for the desktop submodule of `armbian-config` (the [configng](https://github.com/armbian/configng) repository), under `tools/modules/desktops/`. This guide is aimed at developers who want to add a new desktop environment, modify the install/remove pipeline, or integrate the YAML-driven desktop API from another tool.

End-user instructions for installing a desktop with `armbian-config` live in the [Armbian Config](User-Guide_Armbian-Config.md) section.

## Overview

The desktop submodule replaces hand-rolled per-distro install scripts with a single YAML-driven pipeline. Each desktop environment is described by one YAML file in `tools/modules/desktops/yaml/`. A Python helper parses the YAML and emits bash-compatible variables that the rest of the module evaluates and acts on.

The submodule provides:

- **Install / remove** of a desktop environment, including its display manager, custom APT repositories, branding, AppImage extras, group memberships, and skel sync.
- **Auto-login** management for `gdm3`, `sddm`, and `lightdm`.
- **Support queries** that report which desktops are available for a given (release, architecture) pair as TSV or JSON.
- **Container/CI awareness** so the same code path can be used inside Docker without trying to start a display manager.

## Component map

```text
tools/modules/desktops/
├── module_desktops.sh              # main dispatcher: install/remove/auto/manual/...
├── module_desktop_yamlparse.sh     # bash wrapper around the YAML parser
├── module_desktop_supported.sh     # arch/release support check
├── module_desktop_repo.sh          # custom APT repo + GPG keyring setup
├── module_desktop_branding.sh      # wallpapers, greeters, skel, postinst hook
├── module_desktop_getuser.sh       # detects first regular user
├── module_update_skel.sh           # propagate /etc/skel into existing $HOME
├── module_appimage.sh              # AppImage helper (used for armbian-imager)
│
├── scripts/
│   └── parse_desktop_yaml.py       # YAML → bash-eval variables (or TSV/JSON listings)
│
├── yaml/
│   ├── common.yaml                 # packages installed for every DE
│   └── <de_name>.yaml              # per-desktop definition
│
├── postinst/<de_name>.sh           # optional DE-specific post-install hook
├── greeters/{lightdm,sddm}/        # greeter configs and SDDM themes
├── branding/
│   ├── wallpapers/                 # /usr/share/backgrounds/armbian
│   ├── wallpapers-lightdm/         # /usr/share/backgrounds/armbian-lightdm
│   ├── icons/                      # /usr/share/icons/armbian
│   ├── pixmaps/                    # /usr/share/pixmaps/armbian
│   └── armbian.xml                 # GNOME background-properties
└── skel/                           # files copied into /etc/skel
```

Every shell file is loaded by configng's module loader, which exposes them as bash functions in the running shell. `script_dir` points at the configng install root and is used to resolve paths relative to the desktops directory.

## Data flow

```text
       CLI:  armbian-config desktop install de=xfce
              │
              ▼
   module_desktops install de=xfce
              │
              │  1. resolves user via module_desktop_getuser
              │  2. parses xfce.yaml via module_desktop_yamlparse → DESKTOP_* vars
              │  3. sets up custom repo  via module_desktop_repo
              │  4. apt install $DESKTOP_PACKAGES + $DESKTOP_DM
              │  5. apt remove  $DESKTOP_PACKAGES_UNINSTALL
              │  6. installs branding via module_desktop_branding
              │  7. installs Armbian Imager AppImage
              │  8. adds user to sudo/audio/video/... groups
              │  9. propagates /etc/skel via module_update_skel
              │ 10. starts display-manager (skipped in containers)
              │ 11. enables auto-login via `module_desktops auto`
              ▼
         desktop ready
```

The Python helper is the single source of truth for what packages get installed for a given (desktop, release, arch) combination. The bash side never reads YAML directly.

## YAML schema

Each desktop is defined in a single YAML file under `tools/modules/desktops/yaml/`. Filename without `.yaml` is the canonical desktop name (`de_name`).

### Top-level fields

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | informational | Human-readable name. |
| `description` | string | informational | One-line summary, exposed via `DESKTOP_DESC`. |
| `display_manager` | string | yes | Greeter package: `gdm3`, `sddm`, `lightdm`, or `none`. |
| `status` | string | yes | `supported` or `unsupported`. Reported via `DESKTOP_STATUS`. Affects only labelling — does not block install. |
| `packages` | list | yes | DE-specific packages. The first element is treated as the **primary package** and used by `module_desktops status` to detect installation. |
| `packages_uninstall` | list | optional | Packages to purge after the install (junk that the DE metapackage pulls in). |
| `releases` | mapping | yes | Per-release overrides keyed by release codename (`bookworm`, `trixie`, `noble`, `plucky`, ...). |
| `repo` | mapping | optional | Custom APT repository, see below. |

### Per-release block (`releases.<codename>`)

| Field | Type | Description |
|---|---|---|
| `architectures` | list | Architectures supported on this release. Used to compute `DESKTOP_SUPPORTED`. |
| `packages` | list | Extra packages added on top of the top-level `packages`. |
| `packages_remove` | list | Packages filtered out of the merged install list (used to drop a top-level package on a specific release). |
| `packages_uninstall` | list | Packages purged after install on this release only. |

### Custom repository block (`repo`)

| Field | Type | Description |
|---|---|---|
| `url` | string | Base URL for `deb [signed-by=...] <url> <release> main`. |
| `key_url` | string | URL to the GPG key (ASCII-armored). |
| `keyring` | string | Path to the dearmored keyring file, e.g. `/usr/share/keyrings/neon.gpg`. |

### Example

```yaml title="yaml/xfce.yaml"
name: xfce
description: "XFCE - lightweight and fast desktop"
display_manager: lightdm
status: supported

packages:
  - xfce4
  - xfce4-goodies
  - lightdm
  - slick-greeter
  # ...

packages_uninstall:
  - ristretto
  - xfburn

releases:
  trixie:
    architectures: [arm64, amd64, armhf, riscv64]
    packages:
      - pipewire-audio
      - pipewire-pulse
      - wireplumber
    packages_remove:
      - pulseaudio
      - pulseaudio-module-bluetooth
```

```yaml title="yaml/kde-neon.yaml — with custom repo"
name: kde-neon
description: "KDE Neon - latest Plasma from KDE repos (Ubuntu only)"
display_manager: sddm
status: unsupported
repo:
  url: "http://archive.neon.kde.org/testing"
  key_url: "https://archive.neon.kde.org/public.key"
  keyring: "/usr/share/keyrings/neon.gpg"

packages:
  - neon-desktop
  - sddm
  # ...

releases:
  noble:
    architectures: [arm64, amd64]
```

### `common.yaml`

Packages listed in `common.yaml` are added to every desktop install. Keep it minimal — anything desktop-specific belongs in the per-desktop file.

```yaml title="yaml/common.yaml"
name: common
description: "Common packages for all desktop environments"
packages:
  - adwaita-icon-theme
  - cups
  - dconf-cli
  - profile-sync-daemon
  - terminator
  - upower
```

## Python helper: `parse_desktop_yaml.py`

Single-purpose CLI that bash modules invoke via `python3`. All YAML parsing and validation happens here so the bash side stays free of YAML logic.

### Usage

```bash
# Parse one desktop and emit DESKTOP_* shell variables
parse_desktop_yaml.py <yaml_dir> <de_name> <release> <arch>

# List all desktops as TSV (name<TAB>status<TAB>supported<TAB>archs)
parse_desktop_yaml.py <yaml_dir> --list <release> <arch>

# Same as --list but JSON-formatted
parse_desktop_yaml.py <yaml_dir> --list-json <release> <arch>
```

### Variables emitted (per-desktop mode)

All values are double-quoted and shell-escaped via `shell_escape()` (escapes `\`, `"`, `$`, and `` ` ``), so the bash caller can safely `eval` the output.

| Variable | Source | Notes |
|---|---|---|
| `DESKTOP_PACKAGES` | merged: `common.yaml` + top-level `packages` + release `packages` − release `packages_remove` | Space-separated, ready to feed to `apt install`. |
| `DESKTOP_PACKAGES_UNINSTALL` | top-level `packages_uninstall` + release `packages_uninstall` | Space-separated. |
| `DESKTOP_PRIMARY_PKG` | first element of top-level `packages` | Used by `module_desktops status` for `dpkg -l` checks. |
| `DESKTOP_DM` | `display_manager`, default `lightdm` | |
| `DESKTOP_STATUS` | `status`, default `unsupported` | |
| `DESKTOP_SUPPORTED` | `yes` if `arch` is in the release's `architectures` and `release` is a key in `releases`, else `no` | |
| `DESKTOP_DESC` | `description`, default `de_name` | |
| `DESKTOP_REPO_URL` | `repo.url` | Only emitted when `repo:` exists. |
| `DESKTOP_REPO_KEY_URL` | `repo.key_url` | Only emitted when `repo:` exists. |
| `DESKTOP_REPO_KEYRING` | `repo.keyring` | Only emitted when `repo:` exists. |

### Error handling and validation

The parser is strict about top-level structure but tolerant of malformed sub-nodes:

- **Path traversal guard** — `de_name` is resolved against `yaml_dir` via `os.path.realpath`/`commonpath`. Anything outside the directory (`../...`, absolute paths, symlink escapes) is rejected with `Error: invalid desktop name '<name>'` and exit 1.
- **Required structural checks** — top-level YAML must be a mapping; `common.yaml` and per-desktop `packages` must be lists. Failures print a clear `Error: ...` and exit 1.
- **Tolerant normalization** — `releases`, per-release blocks, `architectures`, release-level package lists, top-level `packages_uninstall`, and `repo` all pass through `_as_dict` / `_as_list` helpers. Wrong-typed nodes coerce to safe empty defaults (`{}` or `[]`) instead of raising `AttributeError` or doing surprising substring matches like `arch in "arm64"`.

### `--list` / `--list-json` mode

Iterates every `*.yaml` (excluding `common.yaml`), parses each one, and prints **only entries supported on the requested (release, arch)**. Used by `module_desktops install` to show available desktops on error and by `module_desktops supported` to expose a machine-readable catalog.

## Bash module API

All functions are loaded by configng's module loader. They share global state (`DESKTOP_*` variables, `script_dir`, `DISTROID`) — call sites must follow the documented order.

### `module_desktops <command> [de=<name>] [arch=<arch>] [release=<release>]`

Top-level dispatcher. The `de=`, `arch=`, `release=` arguments are parsed positionally from `$@`.

| Command | Behavior | Required args |
|---|---|---|
| `install`  | Full install pipeline (see [Lifecycle](#lifecycle-install)). | `de=` |
| `remove`   | Disables auto-login, stops the display manager, purges the DM and primary package. | `de=` |
| `disable`  | `systemctl stop && disable display-manager`. | — |
| `enable`   | `systemctl enable && start display-manager`. | — |
| `status`   | Returns 0 if `DESKTOP_PRIMARY_PKG` is `dpkg -l` installed. | `de=` |
| `auto`     | Configures auto-login for `DESKTOP_DM` (gdm3/sddm/lightdm). | `de=` |
| `manual`   | Reverts auto-login. | `de=` |
| `login`    | Returns 0 if auto-login is currently configured. | `de=` |
| `supported`| With `de=`: prints `true`/`false`. Without `de=`: prints JSON catalog of supported desktops. | optional |
| `help`     | Shows help and exits. | — |

#### Auto-login files written

| Display manager | File |
|---|---|
| `gdm3`    | `/etc/gdm3/custom.conf` (or `daemon.conf` on `trixie`/`forky`) |
| `sddm`    | `/etc/sddm.conf.d/autologin.conf` |
| `lightdm` | `/etc/lightdm/lightdm.conf.d/22-armbian-autologin.conf` |

### `module_desktop_yamlparse <de_name> [arch] [release]`

Wraps `parse_desktop_yaml.py`. Resets all `DESKTOP_*` globals, runs the helper, and `eval`s its stdout. Returns 1 on parse failure (with the parser's stderr surfaced).

`arch` defaults to `dpkg --print-architecture`. `release` defaults to `$DISTROID`.

```bash
module_desktop_yamlparse xfce
echo "$DESKTOP_PRIMARY_PKG"   # → xfce4
echo "$DESKTOP_SUPPORTED"     # → yes / no
```

### `module_desktop_yamlparse_list [arch] [release]`

Calls the parser with `--list` and prints TSV to stdout. Used to assemble the "Available: ..." hint shown when `install` is invoked without `de=`.

### `module_desktop_supported <de_name> [arch] [release]`

Convenience wrapper around `module_desktop_yamlparse` that returns 0/1 based on `DESKTOP_SUPPORTED`. Suppresses parser stderr — meant for predicates and CI gates.

### `module_desktop_repo <de_name>`

Sets up a custom APT source. Must be called **after** `module_desktop_yamlparse` because it consumes `DESKTOP_REPO_URL`, `DESKTOP_REPO_KEY_URL`, `DESKTOP_REPO_KEYRING`.

Behavior:

1. Validates `de_name` against `^[a-zA-Z0-9._-]+$` (defense in depth — the YAML parser already blocks traversal).
2. `curl --retry 3 --connect-timeout 10 --max-time 30 ... | gpg --dearmor` writes the keyring. Pipefail is set so a curl failure is surfaced.
3. Verifies the keyring is non-empty before proceeding (catches HTML error pages dearmoring to a zero-byte file).
4. Writes `/etc/apt/sources.list.d/<de_name>.list` with `deb [signed-by=<keyring>] <url> $DISTROID main`.

A no-op if the YAML has no `repo:` block.

### `module_desktop_branding <de_name>`

Copies branding assets and runs the optional postinst hook. Idempotent — every step is guarded with `[[ -d ... ]]`.

| Source (under `tools/modules/desktops/`) | Destination |
|---|---|
| `greeters/lightdm/` | `/etc/armbian/lightdm/` and mirrored to `/etc/lightdm/` |
| `skel/` | `/etc/skel/` |
| `branding/wallpapers/*.jpg` | `/usr/share/backgrounds/armbian/` |
| `branding/wallpapers-lightdm/*.jpg` | `/usr/share/backgrounds/armbian-lightdm/` |
| `branding/icons/*` | `/usr/share/icons/armbian/` |
| `branding/pixmaps/*` | `/usr/share/pixmaps/armbian/` |
| `branding/armbian.xml` | `/usr/share/gnome-background-properties/` |
| `greeters/sddm/themes/*` | `/usr/share/sddm/themes/` (only when `DESKTOP_DM=sddm`) |
| `postinst/<de_name>.sh` | Executed via `bash` (skipped inside containers/CI) |

### `module_desktop_getuser`

Returns the first non-root, non-system user with a real login shell. Prefers `$SUDO_USER` if set and not root, otherwise scans `/etc/passwd` for the first entry with `1000 ≤ uid < 65534` and a shell that does not match `nologin|false`. Exits 1 if none is found.

### `module_update_skel install`

Walks `getent passwd`, and for every regular user (`1000 ≤ uid < 65534`, home directory exists, not root) copies any file present in `/etc/skel` but missing in the user's home, fixing ownership to `uid:gid`. Existing files are never overwritten.

### `module_appimage <install|remove|status> app=<name>`

Used by `module_desktops install` to install `armbian-imager`. The internal `APPIMAGE_REPO` registry maps logical app names to GitHub `owner/repo` slugs and downloads the appropriate architecture-suffixed AppImage from the latest release.

## Lifecycle: install {#lifecycle-install}

The install pipeline in `module_desktops install` is intentionally linear and idempotent-friendly.

```text
1.  Resolve target user           module_desktop_getuser
2.  Parse YAML                    module_desktop_yamlparse $de
3.  Validate package list         exit if DESKTOP_PACKAGES / DESKTOP_PRIMARY_PKG empty
4.  Warn on unsupported           DESKTOP_SUPPORTED != yes → stderr warning, continue
5.  Suppress encfs prompt         debconf-set-selections
6.  Configure custom repo         module_desktop_repo $de
7.  apt update                    pkg_update
8.  apt install desktop pkgs      pkg_install $DESKTOP_PACKAGES
9.  apt install + register DM     /etc/X11/default-display-manager
10. Purge unwanted packages       apt-get remove --purge $DESKTOP_PACKAGES_UNINSTALL
11. Install branding              module_desktop_branding $de
12. Install Armbian Imager        module_appimage install app=armbian-imager
13. Add user to groups            sudo netdev audio video dialout plugdev input bluetooth systemd-journal ssh
14. Profile sync daemon (psd)     touch ~/.activate_psd, sudoers entry
15. Sync skel to existing users   module_update_skel install
16. Start display manager         skipped if _desktop_in_container
17. Enable auto-login             module_desktops auto de=$de
```

The remove pipeline (`module_desktops remove`) reverses the user-visible parts: disables auto-login, stops the display manager, purges the DM and primary package (`apt`'s autoremove handles dependencies), and removes the Armbian Imager AppImage. It does **not** uninstall the full `DESKTOP_PACKAGES` set or undo branding — both are deliberate to avoid removing things the user may now depend on.

## Container and CI awareness

`_desktop_in_container` returns true when any of the following holds:

- `/.dockerenv` exists
- `/run/.containerenv` exists
- `$CI` is set
- `$GITHUB_ACTIONS` is set

Inside a container the install pipeline still does packages, branding, and skel work, but **skips**:

- Stopping or starting any display manager
- Restarting the display manager after auto-login changes
- Running per-desktop `postinst/<de_name>.sh` hooks

This makes the same code path usable for image preseeding inside Docker without needing parallel "container mode" branches.

## Adding a new desktop

1. **Create the YAML.** Drop a new file at `tools/modules/desktops/yaml/<de_name>.yaml` following the [schema](#yaml-schema). Minimum required fields: `display_manager`, `status`, `packages`, and at least one entry under `releases.<codename>` with an `architectures` list.
2. **(Optional) Custom repo.** Add a `repo:` block if the DE is not in the distro's default repositories. Pin the keyring path under `/usr/share/keyrings/`.
3. **(Optional) Postinst hook.** Drop `tools/modules/desktops/postinst/<de_name>.sh` for any per-DE configuration that has to run after `apt install`. Container/CI runs are skipped automatically.
4. **(Optional) Branding overrides.** Branding lives in shared directories, so most desktops do not need any per-DE assets — only add files when the DE needs something different.
5. **Smoke test the parser:**

    ```bash
    cd configng
    python3 tools/modules/desktops/scripts/parse_desktop_yaml.py \
        tools/modules/desktops/yaml <de_name> trixie arm64
    ```

    All `DESKTOP_*` variables should print, and `DESKTOP_SUPPORTED="yes"` for any (release, arch) pair you listed in the YAML.

6. **List-mode sanity check:**

    ```bash
    python3 tools/modules/desktops/scripts/parse_desktop_yaml.py \
        tools/modules/desktops/yaml --list trixie arm64
    ```

    Your new desktop should appear in the TSV output for the (release, arch) combinations you declared.

7. **End-to-end test** in a disposable VM or container with `armbian-config desktop install de=<de_name>`.

## Security notes

- **Path traversal**: `de_name` flows from CLI input into `os.path.join(yaml_dir, f"{de_name}.yaml")`. The Python helper resolves both sides via `os.path.realpath` and rejects anything outside `yaml_dir` (handles `..`, absolute paths, and symlink escapes). `module_desktop_repo` additionally validates `de_name` against `^[a-zA-Z0-9._-]+$` before writing `/etc/apt/sources.list.d/<de_name>.list`.
- **Shell injection**: all values emitted by the Python helper pass through `shell_escape()` (escapes `\`, `"`, `$`, `` ` ``) so the bash caller can `eval` the output safely even when YAML strings contain shell metacharacters.
- **GPG keyring fetch**: the `curl | gpg --dearmor` pipeline runs under `set -o pipefail`, with `--retry 3 --connect-timeout 10 --max-time 30`, and a non-empty file check after dearmor. A failed download or an HTML error page does not silently produce an empty keyring.
- **APT sources** are written with `[signed-by=<keyring>]`, never via `apt-key`. Each desktop's source list lives in its own file (`/etc/apt/sources.list.d/<de_name>.list`) so removal is a single `rm`.

## See also

- [Extensions](Developer-Guide_Extensions.md) — the Armbian build framework's extension system, used by board configs to inject build-time hooks.
- [Armbian Config](User-Guide_Armbian-Config.md) — end-user docs for `armbian-config`.
- [configng repository](https://github.com/armbian/configng) — source for everything described here.
