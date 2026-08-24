---
seo_title: "Armbian patch & debug build switches"
description: "Developer switches for the Armbian build: round-trip kernel/U-Boot patches to git, rewrite patch files, pause to create ATF/crust patches and debug patching."
---

# Patch & debug workflow

Developer-oriented switches for round-tripping patches and debugging the build. Most are only relevant when working on the framework's patch sets — see also [User configurations](/build-framework/user-configurations/#user-provided-patches).

#### DEBUG_PATCHING

`string` · default: `no`

Emit verbose debug output while patches are applied — useful when a patch fails to apply cleanly.

#### PATCHES_TO_GIT

`string` · default: `no`

Commit the sources to git after applying patches, enabling a git-based round-trip of the patch set.

#### REWRITE_PATCHES

`string` · default: `no`

Rewrite the original patch files from the git-committed, applied state (regenerates the `.patch` files).

#### REWRITE_PATCHES_NEEDING_REBASE

`string` · default: `no`

Rewrite only the patch files that actually need a rebase, leaving the rest untouched.

#### CREATE_PATCHES_ATF

`string` · default: `no`

Pause the ARM Trusted Firmware (TF-A) build so you can create or edit ATF patches, then resume.

#### CREATE_PATCHES_CRUST

`string` · default: `no`

Pause the crust firmware build so you can create or edit crust patches, then resume.

#### FORCE_CHECK_MD5_PACKAGES

`string` · default: `no`

Force md5 verification of packages even on distributions where the check is normally skipped.

#### WRITE_EXTENSIONS_METADATA

`string` · default: `yes`

Write extension hook-point call metadata during the build (used by `show-extensions` and tooling). Set `no` to skip.

#### CREATE_PATCHES

`yes` | `no` (default)

:warning: **Deprecated** — use the `kernel-patch` / `uboot-patch` / `atf-patch` CLI commands instead.

Prompts right before compilation to make changes to the U-Boot and kernel source; the resulting diffs are written as patch files in the `output` directory. To include them in a normal run, copy them to the appropriate directories.
