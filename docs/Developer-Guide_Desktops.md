# Desktops

Technical reference for the desktop submodule of `armbian-config` (the [configng](https://github.com/armbian/configng) repository), under `tools/modules/desktops/`. This guide is aimed at developers who want to add a new desktop environment, modify the install/remove pipeline, or integrate the YAML-driven desktop API from another tool.

End-user instructions for installing a desktop with `armbian-config` live in the [Armbian Config](User-Guide_Armbian-Config.md) section.

## Overview

The desktop submodule replaces hand-rolled per-distro install scripts with a single YAML-driven pipeline. Each desktop environment is described by one YAML file in `tools/modules/desktops/yaml/`. A Python helper parses the YAML and emits bash-compatible variables that the rest of the module evaluates and acts on.

The submodule provides:

- **Tiered install** — every desktop ships at one of three sizes (`minimal`, `mid`, `full`), and users can move between tiers after install via `upgrade`/`downgrade`/`set-tier`.
- **Per-install manifest** — every install records exactly which packages it added so removal and downgrades only undo what they themselves did.
- **Custom APT repositories**, branding, group memberships, and skel sync.
- **Auto-login** management for `gdm3`, `sddm`, and `lightdm`, with non-destructive in-place edits of the underlying config files.
- **Per-release / per-arch package overrides** so the same YAML works across Debian bookworm/trixie/forky/sid and Ubuntu jammy/noble/resolute on amd64/arm64/armhf/riscv64/loong64 with different package availability.
- **Browser virtual token** that resolves per-release-per-arch (google-chrome-stable on amd64, chromium on Debian/Ubuntu arm arches, firefox-esr on Debian riscv64, epiphany-browser on Ubuntu riscv64, …).
- **Container/CI awareness** so the same code path can be used inside Docker without trying to start a display manager.

## Tier model

Every desktop install is run at one of three tiers, in order of inclusion: `minimal -> mid -> full`. Each tier is the union of itself plus all lower tiers, so installing `full` implies `mid` implies `minimal`. Tiers are mandatory; there is no flat "install everything from this YAML" mode.

| Tier | Contents | Approximate size |
|---|---|---|
| `minimal` | DE itself + display manager + base utilities. No browser, no office, no user-facing apps beyond a terminal and a file manager. | ~500 MB |
| `mid` | `minimal` + browser + everyday user apps (text editor, calculator, image/PDF viewer, media player, archive tool, torrent client). | ~1 GB |
| `full` | `mid` + office suite + creative tools (LibreOffice, GIMP, Inkscape, Thunderbird, Audacity). | ~2.5 GB |

The per-tier package lists for `mid` and `full` live in `common.yaml` so every DE inherits them. Per-DE YAMLs override only what they need (e.g. KDE Plasma swaps `gnome-text-editor` for `kate` at the mid tier).

The currently-installed tier is recorded in `/etc/armbian/desktop/<de>.tier`. The full set of packages installed for a given DE is recorded in `/etc/armbian/desktop/<de>.packages`.

## Component map

```text
tools/modules/desktops/
├── module_desktops.sh              # main dispatcher: install/remove/auto/manual/upgrade/downgrade/...
├── module_desktop_yamlparse.sh     # bash wrapper around the YAML parser (now takes a tier arg)
├── module_desktop_supported.sh     # arch/release support check
├── module_desktop_repo.sh          # custom APT repo + GPG keyring setup
├── module_desktop_branding.sh      # wallpapers, greeters, skel, postinst hook
├── module_desktop_getuser.sh       # detects first regular user
├── module_update_skel.sh           # propagate /etc/skel into existing $HOME (with chown -R safety net)
├── module_appimage.sh              # AppImage helper (used for armbian-imager via the CLI)
│
├── scripts/
│   └── parse_desktop_yaml.py       # YAML → bash-eval variables (or TSV/JSON listings)
│
├── yaml/
│   ├── common.yaml                 # per-tier defaults installed for every DE; browser map; tier_overrides
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
└── skel/                           # files copied into /etc/skel and propagated to existing $HOME
```

Every shell file is loaded by configng's module loader, which exposes them as bash functions in the running shell. `desktops_dir` points at the desktops directory and is used to resolve paths from any module function.

## Data flow

```text
       CLI:  armbian-config --api module_desktops install de=xfce tier=mid
              │
              ▼
   module_desktops install de=xfce tier=mid
              │
              │  1. validates tier= (mandatory; minimal|mid|full only)
              │  2. resolves user via module_desktop_getuser
              │  3. parses xfce.yaml at the requested tier via module_desktop_yamlparse
              │     → DESKTOP_PACKAGES, DESKTOP_TIER, DESKTOP_DM, DESKTOP_PRIMARY_PKG, ...
              │  4. sets up custom repo via module_desktop_repo
              │  5. apt update
              │  6. apt install $DESKTOP_PACKAGES         ← bail on failure (no state changes)
              │  7. apt install $DESKTOP_DM               ← bail on failure
              │  8. (Armbian only) install armbian-plymouth-theme if armbian repo present
              │  9. write /etc/armbian/desktop/<de>.packages and <de>.tier
              │ 10. apt remove --purge $DESKTOP_PACKAGES_UNINSTALL
              │ 11. installs branding via module_desktop_branding
              │ 12. adds user to sudo/audio/video/... groups
              │ 13. propagates /etc/skel via module_update_skel install (with recursive chown)
              │ 14. systemctl start display-manager      ← skipped in containers
              │ 15. systemctl set-default graphical.target ← only AFTER step 14 succeeds
              │ 16. enables auto-login via module_desktops auto
              ▼
         desktop ready, marker files in /etc/armbian/desktop/
```

The Python helper is the single source of truth for what packages get installed for a given (desktop, release, arch, tier) combination. The bash side never reads YAML directly.

## YAML schema

Each desktop is defined in a single YAML file under `tools/modules/desktops/yaml/`. Filename without `.yaml` is the canonical desktop name (`de_name`).

### Top-level fields

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | informational | Human-readable name. |
| `description` | string | informational | One-line summary, exposed via `DESKTOP_DESC`. |
| `display_manager` | string | yes | Greeter package: `gdm3`, `sddm`, `lightdm`, or `none`. |
| `status` | string | yes | Editorial label — one of `supported`, `community`, `unsupported`. Reported via `DESKTOP_STATUS`. Affects only labelling and catalog filtering — does not block install. `community` is used for DEs that work but are maintained on a best-effort basis; `unsupported` for DEs that are known-broken or not vetted. |
| `tiers` | mapping | yes | Per-tier package lists, keyed by `minimal`, `mid`, `full`. See [Tier blocks](#tier-blocks). |
| `tier_overrides` | mapping | optional | Per-arch and/or per-release-per-arch package removals (and additions) for tier holes. See [tier_overrides](#tier-overrides). |
| `releases` | mapping | yes | Per-release overrides keyed by release codename (`bookworm`, `trixie`, `forky`, `sid`, `jammy`, `noble`, `resolute`, ...). |
| `repo` | mapping | optional | Custom APT repository, see below. |

### Tier blocks

| Field | Type | Description |
|---|---|---|
| `packages` | list | Packages added at this tier. Combined with `common.yaml`'s same-tier packages and any earlier tiers in the walk. |
| `packages_remove` | list | Packages dropped from the accumulated list at this tier. Use this to remove a `common.yaml` entry that doesn't fit the DE (e.g. KDE Plasma drops `gnome-text-editor` and inserts `kate` at the mid tier). |
| `packages_uninstall` | list | (minimal tier only) Packages purged after install. Used for orthogonal junk that the metapackage pulls in but we want gone (e.g. `apport`, `python3-apport`). **Important**: never list a package that is a hard `Depends:` of any meta package the install ships, or apt's autoremove will cascade and yank a chunk of the desktop. |

The first DE-specific package that survives all filters becomes `DESKTOP_PRIMARY_PKG`, used by `module_desktops status` for `dpkg -l` checks. It must come from the DE's own `tiers.minimal.packages` block, not from `common.yaml`, otherwise every DE would share the same primary package.

### Per-release block

The release block is **orthogonal** to the tier walk: it applies to whatever tier is being installed. Use it for things that vary by release rather than by user choice (e.g. trixie's pulseaudio→pipewire swap, bookworm's `gnome-calculator` addition).

| Field | Type | Description |
|---|---|---|
| `architectures` | list | Architectures supported on this release. Used to compute `DESKTOP_AVAILABLE` (the "does this YAML declare the requested release+arch combo?" bool — distinct from the editorial `status` above). |
| `packages` | list | Extra packages added on top of the tier-resolved set. |
| `packages_remove` | list | Packages filtered out of the merged install list. |
| `packages_uninstall` | list | Packages purged after install on this release only. |

### tier_overrides {#tier-overrides}

`tier_overrides` is for **package availability holes**: a tier package that exists on most arches/releases but is missing on one specific combination. The schema has two layers:

```yaml
tier_overrides:
  <tier>:
    architectures:
      <arch>:
        packages_remove: [...]    # apply on this arch in any release
    releases:
      <release>:
        architectures:
          <arch>:
            packages_remove: [...]    # apply only on this release+arch combo
```

Use the per-arch layer for permanent arch-wide holes (e.g. `blender` always missing on armhf). Use the per-release-per-arch layer for transient holes (e.g. `loupe` missing on bookworm because GNOME 43 didn't have it). The parser walks tier_overrides at every tier step in its walk, so a hole declared at the mid tier is honoured for both `mid` and `full` installs.

`tier_overrides` can live in `common.yaml` (applies to every DE) or in a per-DE YAML (applies only to that DE). The parser merges common first, then per-DE.

### Custom repository block

| Field | Type | Description |
|---|---|---|
| `url` | string | Base URL for `deb [signed-by=...] <url> <suite> <components>`. |
| `key_url` | string | URL to the GPG key (ASCII-armored). |
| `keyring` | string | Path to the dearmored keyring file, e.g. `/usr/share/keyrings/neon.gpg`. |
| `suite` | string or list of strings (optional) | Suite path(s) that follow the URL. A list emits one `deb [...]` line per entry — all sharing url/keyring/components — for vendors whose archive spans multiple parallel suites (base, -security, -updates, -porting, -customization, …). Defaults to the release codename. Regex-validated to `^[A-Za-z0-9._/-]+$`. Per-release override: `releases.<release>.repo_suite`. |
| `components` | list (optional) | Components that follow the suite. Defaults to `[main]`. Each entry regex-validated to `^[A-Za-z0-9._-]+$`; invalid entries are dropped with a warning. Per-release override: `releases.<release>.repo_components`. |
| `preferences` | list (optional) | APT pin preferences written to `/etc/apt/preferences.d/<de_name>`. Each entry needs `origin`, `suite`, and `priority` (positive integer). Removed on uninstall. |

`suite` and `components` exist for vendor archives whose layout doesn't match the default `<codename> main` convention. For example, SpacemiT's K1 RISC-V archive pins a frozen snapshot per Ubuntu release (`noble/snapshots/v2.2`, `resolute/snapshots/v3.0`) and mirrors all four Ubuntu components, so `bianbu.yaml` sets `components: [main, universe, restricted, multiverse]` at the `repo:` level and overrides `repo_suite` in each release block.

`preferences` is rarely needed — only when a vendor archive must outrank the distro for a given `(origin, suite)` pair. Each list entry becomes one stanza:

```
Package: *
Pin: release o=<origin>, n=<suite>
Pin-Priority: <priority>
```

Priorities above 1000 let apt downgrade a package from the distro to the pinned archive's version; below 1000 only allows upgrades. Entries missing any required field are skipped with a warning from `parse_desktop_yaml.py`.

### Example

```yaml title="yaml/xfce.yaml"
name: xfce
description: "XFCE - lightweight and fast desktop"
display_manager: lightdm
status: supported

tiers:
  minimal:
    packages:
      - xfce4
      - xfce4-goodies
      - lightdm
      - slick-greeter
      # ...
    packages_uninstall:
      - apport
      - python3-apport
      - python3-problem-report
      - libsnapd-glib-2-1

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

```yaml title="yaml/kde-plasma.yaml — per-DE tier overrides"
name: kde-plasma
description: "KDE Plasma - feature-rich customizable desktop"
display_manager: sddm
status: supported

tiers:
  minimal:
    packages:
      - kde-plasma-desktop
      - sddm
      - konsole
      - dolphin
      - ark
      - gwenview
      - okular
      # ...
  mid:
    # KDE already ships ark / gwenview / okular at minimal — drop the
    # GTK equivalents that common.yaml's mid tier adds.
    packages_remove:
      - gnome-text-editor
      - file-roller
      - loupe
    packages:
      - kate
  full:
    # libreoffice-gtk3 vs default LibreOffice integration: KDE picks
    # up the breeze style automatically when LibreOffice is installed
    # alongside Plasma, so just drop the GTK frontend.
    packages_remove:
      - libreoffice-gtk3
```

```yaml title="yaml/kde-neon.yaml — with custom repo"
name: kde-neon
description: "KDE Neon - latest Plasma from KDE repos (Ubuntu only)"
display_manager: sddm
status: supported
repo:
  url: "http://archive.neon.kde.org/testing"
  key_url: "https://archive.neon.kde.org/public.key"
  keyring: "/usr/share/keyrings/neon.gpg"

tiers:
  minimal:
    packages:
      - neon-desktop
      - sddm
      # ...

releases:
  noble:
    architectures: [arm64, amd64]
```

### common.yaml

`common.yaml` carries the per-tier defaults that apply to every desktop, the browser substitution table, and any cross-DE `tier_overrides`. Per-DE YAMLs only declare a `tiers` block when they want to add packages on top of common or override common-tier entries.

```yaml title="yaml/common.yaml"
name: common
description: "Packages installed for every desktop, in tiers"

tiers:
  minimal:
    packages:
      - adwaita-icon-theme
      - cups
      - dconf-cli
      - profile-sync-daemon
      - terminator
      - upower
  mid:
    packages:
      - browser              # virtual — resolved per-arch from `browser:` below
      - gnome-text-editor
      - gnome-calculator
      - loupe
      - vlc
      - file-roller
      - transmission-gtk
  full:
    packages:
      - libreoffice
      - libreoffice-gtk3
      - gimp
      - inkscape
      - thunderbird
      - audacity

browser:
  bookworm:
    amd64:   google-chrome-stable
    arm64:   chromium
    armhf:   chromium
    # bookworm has no riscv64 port — no entry needed
  trixie:
    amd64:   google-chrome-stable
    arm64:   chromium
    armhf:   chromium
    riscv64: firefox-esr            # 'firefox' does not exist in Debian
  noble:
    amd64:   google-chrome-stable
    arm64:   chromium               # apt.armbian.com real .deb (Ubuntu's is snap-shim)
    armhf:   chromium
    riscv64: epiphany-browser       # firefox/chromium not built for Ubuntu riscv64
  resolute:
    amd64:   google-chrome-stable
    arm64:   chromium
    armhf:   chromium
    riscv64: epiphany-browser
  forky:
    amd64:   google-chrome-stable
    arm64:   chromium
    armhf:   chromium
    riscv64: firefox-esr
  sid:
    amd64:   google-chrome-stable
    arm64:   chromium
    armhf:   chromium
    riscv64: firefox-esr
    loong64: firefox-esr            # chromium not yet built for loong64

tier_overrides:
  mid:
    # armbian-imager ships only amd64/arm64 upstream — strip it on
    # every other arch, across every release.
    architectures:
      armhf:    { packages_remove: [armbian-imager] }
      riscv64:  { packages_remove: [armbian-imager] }
      loong64:  { packages_remove: [armbian-imager] }
    releases:
      bookworm:
        architectures:
          amd64:  { packages_remove: [loupe] }   # GNOME 43 era — no loupe
          arm64:  { packages_remove: [loupe] }
          armhf:  { packages_remove: [loupe] }
      jammy:
        architectures:
          amd64:    { packages_remove: [loupe] } # GNOME 42 — no loupe
          arm64:    { packages_remove: [loupe] }
          armhf:    { packages_remove: [loupe] }
          riscv64:  { packages_remove: [loupe] }
  full:
    # The 'code' (VSCode) .deb on apt.armbian.com links against the
    # pre-t64 library names, which don't exist on post-t64 releases
    # (trixie+, noble+). amd64/arm64 were rebuilt; armhf wasn't. No
    # riscv64 upstream build exists at all. Strip arch-wide on both
    # until/unless the armhf .deb is refreshed.
    architectures:
      armhf:    { packages_remove: [code] }
      riscv64:  { packages_remove: [code] }
    releases:
      bookworm:
        architectures:
          armhf:  { packages_remove: [thunderbird] }
      trixie:
        architectures:
          armhf:  { packages_remove: [thunderbird] }
      noble:
        # thunderbird on Ubuntu noble armhf/riscv64 is absent (no
        # upstream Ubuntu deb there), so strip on those two arches
        # only. amd64/arm64 get the real .deb from apt.armbian.com.
        architectures:
          armhf:    { packages_remove: [thunderbird] }
          riscv64:  { packages_remove: [thunderbird] }
      resolute:
        architectures:
          armhf:    { packages_remove: [thunderbird] }
          riscv64:  { packages_remove: [thunderbird] }
```

### Browser virtual token

The literal string `browser` inside any tier block resolves to a real package name from the `browser:` map at parse time. Lookup order:

1. `browser.<release>.<arch>` — most specific
2. `browser.<arch>` — per-arch fallback if no per-release entry exists
3. drop the token entirely (silent — install proceeds without a browser rather than failing on a literal `browser` apt name)

The per-release layer is needed because the same arch can resolve differently across releases:

- Debian has `firefox-esr` but **no** `firefox` package.
- Ubuntu's `chromium` / `firefox` debs are snap-shim wrappers that require `snapd`. Armbian doesn't ship snapd, so the shims are broken at runtime — apt.armbian.com hosts real `chromium` / `firefox` / `google-chrome-stable` .debs used instead.
- amd64 always gets `google-chrome-stable` (Google publishes no arm/riscv builds, so this is amd64-only).
- `chromium` isn't built for riscv64 in either Debian or Ubuntu.
- Ubuntu doesn't publish `firefox` or `firefox-esr` for riscv64 (Mozilla has no riscv64 binaries, and `firefox-esr` is a Debian-only package name). Fall back to `epiphany-browser` (GNOME Web) there — native GTK, small, and available on every Ubuntu arch.
- Debian riscv64 gets `firefox-esr` because the Debian archive does publish it for riscv64.
- `loong64` is only declared for `sid` in the inventory; `chromium` isn't built there yet either, so it uses `firefox-esr`.

## Python helper: parse_desktop_yaml.py

Single-purpose CLI that bash modules invoke via `python3`. All YAML parsing and validation happens here so the bash side stays free of YAML logic.

### Usage

```bash
# Parse one desktop at a tier and emit DESKTOP_* shell variables.
# --tier is mandatory.
parse_desktop_yaml.py <yaml_dir> <de_name> <release> <arch> --tier <minimal|mid|full>

# List all desktops as TSV (name<TAB>status<TAB>available<TAB>archs)
# The third column is "yes"/"no" for the computed DESKTOP_AVAILABLE.
parse_desktop_yaml.py <yaml_dir> --list <release> <arch> \
    [--filter <available|unavailable|all>]   \
    [--status <supported,community,unsupported>]

# Same as --list but JSON-formatted.
parse_desktop_yaml.py <yaml_dir> --list-json <release> <arch> \
    [--filter <available|unavailable|all>]   \
    [--status <supported,community,unsupported>]

# Print "<name>\t<primary_pkg>" for every desktop, used by `installed`
parse_desktop_yaml.py <yaml_dir> --primaries <release> <arch>
```

The two filter flags on `--list` / `--list-json` select on two orthogonal axes, both default to permissive (backwards-compatible with pre-filter callers):

- `--filter` selects on the **computed** `DESKTOP_AVAILABLE` axis (does the YAML declare this release+arch combo?). Values: `available` (default — hides DEs without an entry for this combo), `unavailable` (only the non-declared DEs), or `all` (no filtering on this axis).
- `--status` selects on the **editorial** `DESKTOP_STATUS` axis. Takes a comma-separated *keep-list* of status values to retain. Omit the flag to keep all statuses. Example: `--status supported,community` drops `unsupported` DEs from the output.

### Variables emitted (per-desktop mode)

All values are double-quoted and shell-escaped via `shell_escape()` (escapes `\`, `"`, `$`, and `` ` ``), so the bash caller can safely `eval` the output.

| Variable | Source | Notes |
|---|---|---|
| `DESKTOP_PACKAGES` | full tier walk: common minimal/mid/full + DE minimal/mid/full + release `packages` − every layer's `packages_remove` and `tier_overrides` removals. The `browser` virtual token is resolved here. | Space-separated, ready to feed to `apt install`. |
| `DESKTOP_PACKAGES_UNINSTALL` | minimal-tier `packages_uninstall` from common + DE + release | Space-separated. |
| `DESKTOP_PRIMARY_PKG` | first DE-specific package (not from common) that survives all filters | Used by `module_desktops status` for `dpkg -l` checks. |
| `DESKTOP_DM` | `display_manager`, default `lightdm` | |
| `DESKTOP_STATUS` | editorial `status` from the YAML, default `unsupported`. One of `supported` / `community` / `unsupported`. | Orthogonal to `DESKTOP_AVAILABLE` — a community DE may be available on a combo (its YAML declares the release+arch) or not. |
| `DESKTOP_AVAILABLE` | `yes` if `arch` is in the release's `architectures` and `release` is a key in `releases`, else `no` | Computed axis — whether the YAML declares this release+arch combo. Named `DESKTOP_SUPPORTED` before 2026-04 (the rename disambiguates this from the editorial `status` field). |
| `DESKTOP_DESC` | `description`, default `de_name` | |
| `DESKTOP_TIER` | the requested tier name | Set verbatim from the `--tier` arg. |
| `DESKTOP_REPO_URL` | `repo.url` | Only emitted when `repo:` exists. |
| `DESKTOP_REPO_KEY_URL` | `repo.key_url` | Only emitted when `repo:` exists. |
| `DESKTOP_REPO_KEYRING` | `repo.keyring` | Only emitted when `repo:` exists. |

### Resolution algorithm

For a given `(de_name, release, arch, tier)`:

1. Start with empty `packages` and `removes` lists.
2. **Walk tiers** from `minimal` up to the target tier. At each step:
    - Merge `common.tiers.<tier>.packages`, then `de.tiers.<tier>.packages`, applying each layer's `packages_remove` to filter.
    - Apply `common.tier_overrides.<tier>` for the (release, arch).
    - Apply `de.tier_overrides.<tier>` for the (release, arch).
3. **Resolve the `browser` token** to a real package via `common.browser.<release>.<arch>` (with fallback to `common.browser.<arch>`, or drop the token).
4. **Apply the release block**: filter `release.<release>.packages_remove`, then add `release.<release>.packages`.
5. **Compute `packages_uninstall`** by unioning the minimal-tier `packages_uninstall` from common, DE, and the release block.
6. **Compute `DESKTOP_PRIMARY_PKG`** as the first DE-specific tier-walk package that survived release and per-arch removals.
7. Emit all `DESKTOP_*` variables.

### Error handling and validation

The parser is strict about top-level structure but tolerant of malformed sub-nodes:

- **Mandatory `--tier` arg.** Calling without it prints usage and exits 1. Invalid tier values (`ultra`, etc.) error out with a clear message.
- **Path traversal guard** — `de_name` is resolved against `yaml_dir` via `os.path.realpath`/`commonpath`. Anything outside the directory (`../...`, absolute paths, symlink escapes) is rejected with `Error: invalid desktop name '<name>'` and exit 1.
- **Tolerant normalization** — `tiers`, `releases`, `architectures`, `tier_overrides`, `repo`, every list field passes through `_as_dict` / `_as_list` helpers. Wrong-typed nodes coerce to safe empty defaults (`{}` or `[]`) instead of raising `AttributeError` or doing surprising substring matches like `arch in "arm64"`.

### List and JSON list modes

Iterates every `*.yaml` (excluding `common.yaml`), parses each one's release block, and emits one row per DE. By default only entries with `DESKTOP_AVAILABLE=yes` for the requested `(release, arch)` are printed — pass `--filter unavailable` or `--filter all` to override. Pass `--status <csv>` to additionally narrow by the editorial `status` field. Used by `module_desktops install` to show available desktops on error and by `module_desktops supported` to expose a machine-readable catalog. These modes do not require `--tier`.

Each JSON entry has this shape (two orthogonal status axes):

```json
{
  "name": "budgie",
  "description": "Budgie - elegant desktop from Solus project",
  "display_manager": "lightdm",
  "status": "community",
  "available": true,
  "architectures": ["arm64", "amd64"]
}
```

## Bash module API

All functions are loaded by configng's module loader. They share global state (`DESKTOP_*` variables, `desktops_dir`, `DISTROID`) — call sites must follow the documented order.

### module_desktops

```text
module_desktops <command> [de=<name>] [tier=<tier>] [arch=<arch>] [release=<release>] [mode=<mode>]
```

Top-level dispatcher. The `de=`, `tier=`, `arch=`, `release=`, `mode=` arguments are parsed positionally from `$@`.

| Command | Behavior | Required args |
|---|---|---|
| `install`   | Full install pipeline (see [Lifecycle](#lifecycle-install)). Bails out cleanly on `pkg_install` failure without changing system state. With `mode=build`: skips user detection, group membership, skel propagation, and DM start/autologin — intended for image-build time when no real user exists. | `de=`, `tier=` (optional: `mode=build`) |
| `remove`    | Disables auto-login, stops the display manager, purges every package recorded in `<de>.packages`, runs `pkg_clean`, switches `default.target` back to `multi-user`, isolates to multi-user.target so the running session also drops to console. | `de=` |
| `upgrade`   | Move an installed desktop to a higher tier. Refuses if the target is the same or lower (use `downgrade`). | `de=`, `tier=` |
| `downgrade` | Move an installed desktop to a lower tier. Removable set is intersected with the install manifest so user-installed packages are never touched. | `de=`, `tier=` |
| `set-tier`  | Direction-agnostic tier change — auto-detects upgrade vs downgrade from the current marker. Same arg shape as `upgrade`/`downgrade`. Refuses with a friendly message if not installed or already at the target tier. Used by the dialog menu's "Change to <tier>" entries. | `de=`, `tier=` |
| `tier`      | Print the installed tier name (`minimal`/`mid`/`full`) on stdout, or `not installed`. Returns 0 if installed, 1 if not. Use this from the CLI when you want the actual tier value. | `de=` |
| `at-tier`   | Silent gate: exit 0 if the DE is installed AND its current tier marker matches the given target. Used by dialog menu condition gates. | `de=`, `tier=` |
| `status`    | Silent exit-code query. Returns 0 if `DESKTOP_PRIMARY_PKG` is `dpkg -l` installed, 1 if not. **Prints nothing on either path** so it can be used safely from menu condition gates that fire dozens of times per render. | `de=` |
| `disable`   | `systemctl stop && disable display-manager`. | — |
| `enable`    | `systemctl enable && start display-manager`. | — |
| `auto`      | Configures auto-login for `DESKTOP_DM` (gdm3/sddm/lightdm). Edits the gdm config in place — never overwrites the file — so user customization is preserved. | `de=` |
| `manual`    | Reverts auto-login. Idempotent. | `de=` |
| `login`     | Returns 0 if auto-login is currently configured. Anchored regex; safely ignores commented sample lines in the stock noble `custom.conf`. | `de=` |
| `supported` | With `de=`: prints `true`/`false` based on `DESKTOP_AVAILABLE` for the DE on `arch=`/`release=`. Without `de=`: prints a JSON catalog. Two optional filter knobs: `filter=available\|unavailable\|all` (computed-availability axis, default `available`) and `status=<csv>` (editorial-status keep-list — e.g. `status=supported,community` hides editorially `unsupported` DEs). | optional `de=`, `arch=`, `release=`, `filter=`, `status=` |
| `installed` | Returns 0 if any desktop is installed (uses cached `--primaries` lookup). | — |
| `help`      | Shows help and exits. | — |

#### Manifest files

Two files per installed desktop, both under `/etc/armbian/desktop/`:

| File | Format | Purpose |
|---|---|---|
| `<de>.packages` | newline-separated package names | The exact set of packages newly installed by `module_desktops install` (captured from `apt-get -s install` dry-run via `pkg_install`'s `ACTUALLY_INSTALLED` array). The `remove` path passes this to `pkg_remove`; the `downgrade` path uses it to constrain what may be removed. |
| `<de>.tier` | one line: `minimal`, `mid`, or `full` | Source of truth for the currently-installed tier. Read by `status`, `tier`, `at-tier`, `upgrade`, `downgrade`, `set-tier`. Written by `install` and the tier-change commands. |

#### Auto-login files written

| Display manager | File |
|---|---|
| `gdm3`    | `/etc/gdm3/custom.conf` on Ubuntu, `/etc/gdm3/daemon.conf` on Debian. Branched on `ID=` from `/etc/os-release` (not on release codename — both `bookworm` and `trixie` use `daemon.conf`). The file is edited in place via sed, NOT overwritten — any user customization (`WaylandEnable=false`, etc.) is preserved. |
| `sddm`    | `/etc/sddm.conf.d/autologin.conf` (drop-in, non-destructive) |
| `lightdm` | `/etc/lightdm/lightdm.conf.d/22-armbian-autologin.conf` (drop-in, non-destructive) |

### module_desktop_yamlparse

```text
module_desktop_yamlparse <de_name> [arch] [release] [tier]
```

Wraps `parse_desktop_yaml.py`. Resets all `DESKTOP_*` globals, runs the helper, and `eval`s its stdout. Returns 1 on parse failure (with the parser's stderr surfaced).

Defaults:
- `arch` → `dpkg --print-architecture`
- `release` → `$DISTROID`
- `tier` → `minimal` — passed through to the parser's `--tier` arg, so callers that only need `DESKTOP_DM` / `DESKTOP_PRIMARY_PKG` (status checks, autologin paths) don't need to know the actual installed tier.

```bash
module_desktop_yamlparse xfce
echo "$DESKTOP_PRIMARY_PKG"   # → xfce4

module_desktop_yamlparse xfce arm64 trixie full
echo "$DESKTOP_TIER"          # → full
echo "$DESKTOP_PACKAGES"      # → minimal + mid + full set, with browser resolved
```

### module_desktop_yamlparse_list

```text
module_desktop_yamlparse_list [arch] [release]
```

Calls the parser with `--list` and prints TSV to stdout. Used to assemble the "Available: ..." hint shown when `install` is invoked without `de=`.

### module_desktop_supported

```text
module_desktop_supported <de_name> [arch] [release]
```

Convenience wrapper around `module_desktop_yamlparse` that returns 0/1 based on `DESKTOP_AVAILABLE` (the computed-availability axis). Suppresses parser stderr — meant for predicates and CI gates. Note: this function does not consider the editorial `DESKTOP_STATUS` axis — a DE with `status: unsupported` can still return 0 here if its YAML declares the requested release+arch. Filter on `DESKTOP_STATUS` separately if you need to exclude unsupported DEs.

### module_desktop_repo

```text
module_desktop_repo <de_name>
```

Sets up a custom APT source. Must be called **after** `module_desktop_yamlparse` because it consumes `DESKTOP_REPO_URL`, `DESKTOP_REPO_KEY_URL`, `DESKTOP_REPO_KEYRING`.

Behavior:

1. Validates `de_name` against `^[a-zA-Z0-9._-]+$` (defense in depth — the YAML parser already blocks traversal).
2. `curl --retry 3 --connect-timeout 10 --max-time 30 ... | gpg --dearmor` writes the keyring. Pipefail is set so a curl failure is surfaced.
3. Verifies the keyring is non-empty before proceeding (catches HTML error pages dearmoring to a zero-byte file).
4. Writes `/etc/apt/sources.list.d/<de_name>.list` with `deb [signed-by=<keyring>] <url> $DISTROID main`.

A no-op if the YAML has no `repo:` block.

### module_desktop_branding

```text
module_desktop_branding <de_name>
```

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

The distributor logo for GNOME Settings → About / KDE Info Center / etc. is **not** installed from here — that file ships from `armbian-base-files` so it stays in sync with the `LOGO=` line in `/etc/os-release`.

### module_desktop_getuser

```text
module_desktop_getuser
```

Returns the first non-root, non-system user with a real login shell. Prefers `$SUDO_USER` if set and not root, otherwise scans `/etc/passwd` for the first entry with `1000 ≤ uid < 65534` and a shell that does not match `nologin|false`. Exits 1 if none is found.

### module_update_skel

```text
module_update_skel install
```

Walks `getent passwd`, and for every regular user (`1000 ≤ uid < 65534`, home directory exists, not root):

1. Walks `/etc/skel` with `find -mindepth 1`. For each entry:
    - Directory: create at the destination if missing.
    - File: copy if the destination doesn't exist; never overwrite.
2. Runs `chown -R "$uid:$gid" "$home/"` as a safety net.

The recursive `chown` is critical: other package postinst scripts (caja, nemo, gnome-keyring, …) routinely leak root-owned files into the user's `~/.config` directory on first install. Without the recursive chown, those tools refuse to start on first login because they can't write their own config dirs.

### module_appimage

```text
module_appimage <install|remove|status> app=<name>
```

Standalone AppImage helper. The internal `APPIMAGE_REPO` registry maps logical app names (e.g. `armbian-imager`) to GitHub `owner/repo` slugs and downloads the appropriate architecture-suffixed AppImage from the latest release. `module_appimage install` also installs `libfuse2`, `fuse3`, and the `libgles2`/`libegl1`/`libgl1`/`libgl1-mesa-dri` runtime so the AppImage can launch.

Not called from the desktop install path by default. The `armbian-imager` AppImage is available via `armbian-config --api module_appimage install app=armbian-imager` for users who explicitly want it.

## Lifecycle: install {#lifecycle-install}

The install pipeline in `module_desktops install` is intentionally linear and idempotent-friendly. **Every step that touches system state is gated on the previous step's success.**

Steps marked with `[R]` are **runtime-only** — skipped when `mode=build` is passed (image build time, no real user exists). Steps marked with `[B]` run in **both** modes.

```{ .text linenums="0" }
 1. [B] Validate args              de= and tier= both required; tier must be minimal|mid|full
 2. [R] Resolve target user        module_desktop_getuser (skipped in mode=build)
 3. [B] Parse YAML at target tier  module_desktop_yamlparse $de $arch $release $tier
 4. [B] Validate package list      exit if DESKTOP_PACKAGES / DESKTOP_PRIMARY_PKG empty
 5. [B] Warn on unavailable        DESKTOP_AVAILABLE != yes → stderr warning, continue
 6. [B] Suppress interactive       debconf-set-selections + DEBIAN_FRONTEND=noninteractive
 7. [B] Configure custom repo      module_desktop_repo $de  (no-op if no repo: block)
 8. [B] Write apt pin              _module_desktops_write_apt_pin  (force apt.armbian.com .debs)
 9. [B] apt update                 pkg_update
10. [B] Reset ACTUALLY_INSTALLED   array used by pkg_install to record new packages
11. [B] apt install desktop pkgs   pkg_install $DESKTOP_PACKAGES        ← bail on failure
12. [B] apt install + register DM  pkg_install $DESKTOP_DM              ← bail on failure
                                   /etc/X11/default-display-manager
13. [B] (Armbian) install plymouth if /etc/apt/sources.list.d/armbian.{list,sources} present
14. [B] Save install manifest      /etc/armbian/desktop/<de>.packages and <de>.tier
15. [B] Purge unwanted packages    apt-get remove --purge $DESKTOP_PACKAGES_UNINSTALL
16. [B] Install branding           module_desktop_branding $de (browser policies, VPU flags, etc.)
17. [R] Add user to groups         sudo netdev audio video dialout plugdev input bluetooth systemd-journal ssh
18. [R] Profile sync daemon (psd)  touch ~/.activate_psd, sudoers entry
19. [R] Sync skel to existing users module_update_skel install  (with chown -R safety net)
20. [R] Stop other DMs             gdm3/lightdm/sddm one by one
21. [R] Start display manager      systemctl start display-manager      ← container path also skips
22. [R] Switch default.target      systemctl set-default graphical.target  ONLY if step 21 succeeded
23. [R] Enable auto-login          module_desktops auto de=$de
```

**`mode=build`** is used by the Armbian build framework at image-creation time. At that point the rootfs has no regular user (armbian-firstrun creates the first user on first boot), and DM/systemd operations make no sense inside a chroot. The packages, branding, manifests, and `/etc/skel` all land correctly; the first user inherits skel at `useradd` time and armbian-firstrun manages `graphical.target`.

If step 11 or 12 fails, the function returns 1 with no further state changes — the manifest is not written, `default.target` stays at `multi-user`, no DM is started. The system is in the same state as if the install had never run.

## Lifecycle: remove

```{ .text linenums="0" }
 1. Validate args                 de= required
 2. Read installed tier marker    /etc/armbian/desktop/<de>.tier (default: minimal)
 3. Parse YAML at the installed   module_desktop_yamlparse $de $arch $release $installed_tier
    tier
 4. Disable auto-login            module_desktops manual de=$de
 5. Stop display manager          systemctl stop display-manager
 6. Switch default.target         systemctl set-default multi-user.target
 7. Isolate to multi-user         systemctl isolate multi-user.target  (drops running session
                                  to console immediately, no reboot needed)
 8. Compute removable set         from /etc/armbian/desktop/<de>.packages
                                  fallback: walk DESKTOP_PACKAGES through dpkg-query
 9. Filter out essentials         apt-get -s -y purge <list>  (simulation, stderr parsed)
                                  every package apt flags under "WARNING: The following
                                  essential packages will be removed" is dropped from
                                  the removable set — see note below
10. Purge remaining set           apt-get -y purge <filtered list>   ← bail on failure,
                                  manifest preserved for retry
11. Delete manifest files         rm /etc/armbian/desktop/<de>.{packages,tier}  (only after 10 succeeds)
12. pkg_clean                     apt-get clean — reclaim downloaded .deb cache
```

The `set-default` and `isolate` calls together ensure the user gets a console login on tty1 immediately after the uninstall, without needing to reboot. Without them, the system stays pinned to `graphical.target` with no DM behind it and the local console is blank.

**Why the essential filter (step 9).** The remove path calls `apt-get -y purge` directly — **not** `pkg_remove` (which wraps `apt-get autopurge`). `autopurge` adds an orphan-cleanup cascade on top of the removal, and on fresh post-t64 images (trixie+, noble+) several shared libs pulled in alongside `e2fsprogs` (`libext2fs2t64`, `libss2`, `logsave`) are marked auto-installed. Once the DE is gone nothing manual depends on them, autopurge proposes to orphan-remove the whole chain, and apt 2.9+ / solver 3.0 vetoes the transaction with `E: Essential packages were removed and -y was used without --allow-remove-essential` — nothing actually gets removed. A plain `apt-get purge` avoids the cascade, and the manifest is already the complete list, so no cascade is needed.

A separate case the filter catches: some base images (notably `armbian/repository-update:*-armhf` tags rebuilt from debian-slim) ship without `e2fsprogs` pre-installed. When a DE's install pulls in `dracut-install` or `gnome-disk-utility` transitively, those pull `e2fsprogs`, it lands in the manifest, and purging it would touch an Essential package. Step 9 simulates the purge, parses apt's essential-warning block (stripping `(due to X)` annotations), and drops every flagged name from the list before the real purge runs.

On failure of step 10 the function returns 1 with the manifest left in place, so the next `remove` retries against the same list rather than falling into the less-precise YAML-walk path.

## Lifecycle: upgrade and downgrade

`upgrade` and `downgrade` are the two halves of `_module_desktops_change_tier`:

```{ .text linenums="0" }
1.  Validate args                 de= and tier= required; tier must be minimal|mid|full
2.  Read current tier marker      /etc/armbian/desktop/<de>.tier (must exist)
3.  Validate direction            upgrade refuses target <= current
                                  downgrade refuses target >= current
                                  same tier → no-op message, exit 0
4.  Parse YAML twice              once at current tier, once at target tier
                                  store the package lists in two bash arrays
5.  Compute set difference        (awk on per-line printf input)
                                  upgrade:   to_install = target - current
                                  downgrade: removable  = current - target
6.  (downgrade only) intersect    removable ∩ <de>.packages — never touch
                                  packages the user installed manually
                                  outside the desktop install path
7.  Apply                         pkg_install (upgrade) or pkg_remove (downgrade)
8.  Update manifest               append new packages, or remove drained ones
9.  Update tier marker            /etc/armbian/desktop/<de>.tier
```

`set-tier` is a thin front-end over the same helper that auto-detects direction from the current tier vs the target. It's the entry point used by the dialog menu's "Change <DE> to <tier>" buttons.

## Container and CI awareness

`_desktop_in_container` returns true when any of the following holds:

- `/.dockerenv` exists
- `/run/.containerenv` exists
- `$CI` is set
- `$GITHUB_ACTIONS` is set

Inside a container the install pipeline still does packages, branding, and skel work, but **skips**:

- Stopping or starting any display manager
- The `set-default graphical.target` switch
- Restarting the display manager after auto-login changes
- The `systemctl isolate` call on remove
- Running per-desktop `postinst/<de_name>.sh` hooks

This makes the same code path usable for image preseeding inside Docker without needing parallel "container mode" branches.

## Adding a new desktop

1. **Create the YAML.** Drop a new file at `tools/modules/desktops/yaml/<de_name>.yaml` following the [schema](#yaml-schema). Minimum required fields: `display_manager`, `status`, `tiers.minimal.packages`, and at least one entry under `releases.<codename>` with an `architectures` list.
2. **(Optional) Per-DE tier overrides.** Add a `tiers.mid` and/or `tiers.full` block only if you need to override common defaults. Most DEs inherit common's mid/full unchanged.
3. **(Optional) `tier_overrides`.** Add per-arch or per-release-per-arch removals only when there's a known package availability hole specific to this DE. Cross-DE holes belong in `common.yaml`.
4. **(Optional) Custom repo.** Add a `repo:` block if the DE is not in the distro's default repositories. Pin the keyring path under `/usr/share/keyrings/`.
5. **(Optional) Postinst hook.** Drop `tools/modules/desktops/postinst/<de_name>.sh` for any per-DE configuration that has to run after `apt install`. Container/CI runs are skipped automatically.
6. **(Optional) Branding overrides.** Branding lives in shared directories, so most desktops do not need any per-DE assets — only add files when the DE needs something different.
7. **Smoke test the parser at every tier:**

    ```bash
    cd configng
    for tier in minimal mid full; do
        python3 tools/modules/desktops/scripts/parse_desktop_yaml.py \
            tools/modules/desktops/yaml <de_name> trixie arm64 --tier $tier
        echo "---"
    done
    ```

    All `DESKTOP_*` variables should print, `DESKTOP_AVAILABLE="yes"` for any (release, arch) pair you listed in the YAML, and `DESKTOP_TIER` should match the requested tier.

8. **List-mode sanity check:**

    ```bash
    python3 tools/modules/desktops/scripts/parse_desktop_yaml.py \
        tools/modules/desktops/yaml --list trixie arm64
    ```

    Your new desktop should appear in the TSV output for the (release, arch) combinations you declared.

9. **End-to-end test** in a disposable VM or container:

    ```bash
    armbian-config --api module_desktops install de=<de_name> tier=minimal
    armbian-config --api module_desktops upgrade de=<de_name> tier=mid
    armbian-config --api module_desktops upgrade de=<de_name> tier=full
    armbian-config --api module_desktops downgrade de=<de_name> tier=minimal
    armbian-config --api module_desktops remove de=<de_name>
    ```

10. **Add menu entries** in `tools/json/config.system.json` if you want the DE to appear in the dialog menu. Existing desktops use this slot allocation per DE:

    | ID slot | Action |
    |---|---|
    | `*01` | install minimal |
    | `*02` | uninstall |
    | `*03` | enable autologin |
    | `*04` | disable autologin |
    | `*05` | install mid |
    | `*06` | install full |
    | `*07` | change to minimal |
    | `*08` | change to mid |
    | `*09` | change to full |

    The `*07-*09` change-tier entries use `module_desktops set-tier` and gate visibility with `module_desktops status de=<X> && ! module_desktops at-tier de=<X> tier=<target>`.

    **`status: community` DEs** (the `[CSC]` tier) follow a shorter allocation — only `*01` (install minimal), `*02` (uninstall), `*03` (autologin), `*04` (manual-login) — matching the `kde-neon` precedent. No 3-tier install, no set-tier. Description and `short` carry a trailing `[CSC]` marker so the UI can distinguish community DEs from first-class supported ones. Do NOT add menu entries for `status: unsupported` DEs — they're intentionally kept out of the dialog so users never land on a broken install path from the menu.

## Matrix audit automation

The desktop matrix covers several DEs × several releases × several architectures, and two kinds of drift tend to accumulate silently:

1. **Missing releases** — `armbian/build` adds a new release to `config/distributions/` (e.g. Ubuntu `resolute`) but no DE YAML grows a release block for it, so the desktop can't be installed on that release at all.
2. **Package holes** — an entry in the resolved `DESKTOP_PACKAGES` set is no longer published for some `(release, arch)` pair (archive removed it, or it was never built for that arch), so `apt` fails at install time with `E: Unable to locate package`.

A weekly GitHub Actions workflow detects both, hands the findings to Claude Code to propose YAML edits, and opens a draft PR for a maintainer to review.

### Components

```text
tools/modules/desktops/github/
├── audit.py           # deterministic scanner — emits audit-report.json
├── audit_prompt.py    # renders the report into a Claude prompt
└── audit_apply.py     # legacy direct-API applier (unused by the workflow)

.github/workflows/
└── maintenance-desktop-audit.yml   # the scheduled workflow
```

Only the scanner talks to the network; the LLM never fetches package metadata itself. That keeps the "what is broken" signal reproducible and cache-friendly, and confines all non-determinism to the "how should we fix it" step.

### `audit.py`

Walks `tools/modules/desktops/yaml/` against:

- `armbian/build`'s `config/distributions/<release>.conf` (loaded from a sibling checkout passed via `--build-repo`) to get the set of releases and their support statuses (`supported`, `csc`, `eos`, …). Anything `eos` is skipped.
- `packages.debian.org` and `packages.ubuntu.com` — one `urllib` request per `(release, arch, package)` tuple, parallelised with `ThreadPoolExecutor`. Responses are cached in-process for the run.

Report shape (`audit-report.json`):

```json
{
  "scanned_releases": ["bookworm", "noble", "resolute", "trixie"],
  "build_distributions": { "<release>": { "name": "...", "support": "supported|csc|eos", "architectures": [...] } },
  "missing_releases": [ { "release": "resolute", "support_status": "csc", "architectures": [...] } ],
  "package_holes":    [ { "de": "xfce", "release": "trixie", "arch": "riscv64", "tier": "full", "missing": ["libfoo"] } ],
  "skipped_desktops": ["bianbu"],
  "stats": { "desktops": 11, "scope": 4, "holes": 0, "package_lookups": 0 }
}
```

Desktops with `status: unsupported` in their YAML are listed in `skipped_desktops` and not audited — drift in an unsupported DE isn't actionable. `status: community` DEs **are** audited (drift in a community-tier DE is still worth reporting, even if a maintainer may choose not to act on it immediately).

Flags: `--tier {minimal,mid,full}` narrows the scope; `--release <codename>` audits a single release; `--skip-network` is a dry-run that only reports `missing_releases`.

### `audit_prompt.py`

Renders the JSON report into a single text prompt (no markdown-in-markdown gymnastics; the report JSON is embedded in fenced blocks). The prompt pins Claude to:

- touch only YAML files under `tools/modules/desktops/yaml/`
- address **every** finding, not just the first
- prefer edits to `common.yaml`'s `tier_overrides` block for package holes (one place, applies to every DE) over duplicating `packages_remove` entries in per-DE YAMLs
- for missing releases, add a release block to each `status: supported` DE YAML, copying the shape from an existing block and adjusting per-release deltas only where needed
- always add an inline comment explaining **why** a hole exists, so future readers can distinguish a transient archive gap from a permanent upstream-port limitation
- preserve the existing 2-space indentation
- if the report is empty, say so and make no edits

### `maintenance-desktop-audit.yml`

Triggers:

- `schedule: '0 6 * * 1'` — Mondays 06:00 UTC. Release and package availability change slowly, so weekly is enough and cheap.
- `workflow_dispatch` — with optional `tier`, `release`, and `dry_run` inputs. `dry_run: true` stops after the deterministic audit and attaches `audit-report.json` without calling Claude or opening a PR.

Concurrency: `group: desktop-audit`, `cancel-in-progress: false` — two scheduled runs will never race, and a manual dispatch queues behind the scheduled run rather than killing it.

Job steps, in order:

1. **Checkout configng** at the workspace root (no `path:`) so `claude-code-action` finds `.git`.
2. **Checkout `armbian/build`** into `armbian-build/` with `fetch-depth: 1` — the audit only reads `config/distributions/`, so shallow is fine.
3. **Set up Python 3.12** and `pip install pyyaml`.
4. **Run `audit.py`** — writes `audit-report.json`, appends a markdown summary table to `$GITHUB_STEP_SUMMARY`, and sets `steps.audit.outputs.actionable` to `true` iff `missing_releases` or `package_holes` is non-empty.
5. **Prepare Claude prompt** (`audit_prompt.py`) — only if `actionable` and not a dry run.
6. **Upload `audit-report`** artifact (always, 30-day retention) — useful even on zero-hole runs as historical record.
7. **`anthropics/claude-code-action@v1`** with:
    - `claude_code_oauth_token: secrets.CLAUDE_CODE_OAUTH_TOKEN` (Max subscription token — no per-run API charges).
    - `claude_args: --max-turns 30 --permission-mode acceptEdits --allowed-tools Edit,Write,Read,Glob,Grep,Bash(git:*)`. `acceptEdits` plus the explicit allow-list is required: without them the action's default tool gate denies Edit/Write and the branch stays empty. `Bash(git:*)` only permits read-only git inspection; no shell execution surface.
8. **Stash Claude execution log** — copies `${RUNNER_TEMP}/claude-execution-output.json` into the workspace; uploaded as the `claude-execution-output` artifact with `if: always()` so a failed or zero-edit run is debuggable from the transcript without a re-run.
9. **Clean up temp files** — removes `armbian-build/`, `audit-report.json`, `claude-prompt.txt`, and `claude-execution-output.json` from the working tree so `peter-evans/create-pull-request` sees only Claude's YAML edits.
10. **`peter-evans/create-pull-request@v6`** — branch `bot/desktop-matrix-audit`, base `main`, `add-paths: tools/modules/desktops/yaml/*`, `delete-branch: true`, `draft: true`, labels `bot`, `desktops`, `documentation`. PR body is `steps.claude.outputs.structured_output` (Claude's own summary of what it changed and why). If Claude produced no diff, the branch is not ahead of main and no PR is opened — the workflow finishes green with only the audit artifact.

### Permissions

```yaml
permissions:
  contents: write        # push to bot/desktop-matrix-audit
  pull-requests: write   # open the PR
  id-token: write        # claude-code-action OIDC
```

### Reviewing a bot PR

Bot PRs open as **draft** on purpose. A human check before merge:

1. Read Claude's PR body — it should list every file it changed and the reason.
2. Confirm the diff is scoped to `tools/modules/desktops/yaml/`. Any out-of-scope file is a red flag (the workflow's `add-paths` should already prevent this, but verify).
3. For each missing-release addition: spot-check that the new release block is a sensible copy of an existing one (e.g. a `resolute` block for `xfce.yaml` should look like the `trixie` or `noble` block, not a half-written stub).
4. For each package-hole edit: confirm it lives in `common.yaml`'s `tier_overrides` where it belongs, not duplicated per-DE.
5. For each WHY comment: confirm it's accurate. "not yet in trixie" ages out; "no upstream riscv64 port" doesn't.
6. Mark ready for review and merge normally. `delete-branch: true` cleans up on merge.

If Claude judged the report non-actionable (e.g. the only finding is a `csc`-tier release a maintainer wants to hold off on), the run ends with the `audit-report` artifact present and no PR — inspect the artifact and the `claude-execution-output` log to confirm.

## Common pitfalls

### packages_uninstall cascade

Listing a package in `tiers.minimal.packages_uninstall` runs `apt-get remove --purge` on it after the install. If that package is a hard `Depends:` of any meta package the DE install pulled in, apt's autoremove cascade will yank the meta package along with it — and on systems with `APT::Get::AutomaticRemove "true"` (Ubuntu noble/resolute), the cascade keeps going and rips out a chunk of the desktop. Real examples that bit us:

- Listing any `xfce4-goodies` plugin (e.g. `xfce4-clipman-plugin`) yanks `xfce4-goodies` itself, then half the desktop.
- Listing `language-selector-gnome` yanks `gnome-control-center` (which has it as a hard Depends on Ubuntu), so the user loses Settings.
- Listing `kdeconnect` or `khelpcenter` yanks `neon-desktop`.

**Rule**: never put a `Depends:` of a metapackage you ship into `packages_uninstall`. Verify with `apt-cache rdepends --installed <pkg>` before adding anything.

### Gnome daemon.conf vs custom.conf

Both Debian and Ubuntu ship a `gdm3` package, but they read different config files:

- Debian (any release): `/etc/gdm3/daemon.conf`
- Ubuntu (any release): `/etc/gdm3/custom.conf`

`module_desktops auto` branches on `ID=ubuntu` from `/etc/os-release`, **not** on the release codename. Earlier versions of the code branched on codename and wrote to the wrong file on Debian bookworm.

The `auto` path also edits the file in place via sed (preserving any user customization like `WaylandEnable=false`) rather than overwriting it with a fresh `cat > $file`.

### login regex anchoring

The stock Ubuntu noble `/etc/gdm3/custom.conf` template ships with a commented sample line:

```
#  AutomaticLoginEnable = true
```

An unanchored `grep` for `AutomaticLoginEnable\s*=\s*true` matches this comment, and `module_desktops login` returns 0 (autologin enabled) on every fresh install where the user has never touched autologin. The fix is `^AutomaticLoginEnable[[:space:]]*=[[:space:]]*true` — anchored at line start so the comment doesn't match.

## Security notes

- **Path traversal**: `de_name` flows from CLI input into `os.path.join(yaml_dir, f"{de_name}.yaml")`. The Python helper resolves both sides via `os.path.realpath` and rejects anything outside `yaml_dir` (handles `..`, absolute paths, and symlink escapes). `module_desktop_repo` additionally validates `de_name` against `^[a-zA-Z0-9._-]+$` before writing `/etc/apt/sources.list.d/<de_name>.list`.
- **Shell injection**: all values emitted by the Python helper pass through `shell_escape()` (escapes `\`, `"`, `$`, `` ` ``) so the bash caller can `eval` the output safely even when YAML strings contain shell metacharacters.
- **GPG keyring fetch**: the `curl | gpg --dearmor` pipeline runs under `set -o pipefail`, with `--retry 3 --connect-timeout 10 --max-time 30`, and a non-empty file check after dearmor. A failed download or an HTML error page does not silently produce an empty keyring.
- **APT sources** are written with `[signed-by=<keyring>]`, never via `apt-key`. Each desktop's source list lives in its own file (`/etc/apt/sources.list.d/<de_name>.list`) so removal is a single `rm`.

## See also

- [Extensions](Developer-Guide_Extensions.md) — the Armbian build framework's extension system, used by board configs to inject build-time hooks.
- [Armbian Config](User-Guide_Armbian-Config.md) — end-user docs for `armbian-config`.
- [configng repository](https://github.com/armbian/configng) — source for everything described here.
