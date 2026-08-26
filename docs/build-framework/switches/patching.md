---
seo_title: "Armbian patch & debug build switches"
description: "Developer switches for the Armbian build: round-trip kernel/U-Boot patches to git, rewrite patch files, pause to create ATF/crust patches and debug patching."
---

# Patching

Developer-oriented switches for round-tripping patches and debugging the build. Most are only relevant when working on the framework's patch sets — see also [User configurations](/build-framework/user-configurations/#user-provided-patches).

#### DEBUG_PATCHING

`string` · default: `no`

Raises the log level of the Python patching tool so it prints the details of every patch it tries — which file each hunk targets, and exactly where and why one fails to apply. Off by default because the output is noisy; turn it on when a patch stops applying after a source or kernel bump and you need to see what moved. (The global `SHOW_DEBUG=yes` implies it, so you rarely set this one directly.)

#### PATCHES_TO_GIT

`string` · default: `no`

Commits the patched kernel or U-Boot tree into a working git branch, turning each applied `.patch` file into a real git commit. This is the first half of the patch round-trip: once the patch set lives in git you can reorder, edit or drop commits with normal git tooling before regenerating the files with `REWRITE_PATCHES`. You seldom set it by hand — the `kernel-patches-to-git` / `uboot-patches-to-git` CLI commands force it on — but it is the switch the whole round-trip is built around.

#### REWRITE_PATCHES

`string` · default: `no`

Completes the round-trip started by `PATCHES_TO_GIT`: after the patches have been applied and committed to git, this regenerates the on-disk `.patch` files from those commits, so any edits you made in git (rebasing onto a newer source, fixing a fuzzy hunk, splitting a patch) are written back to the patch set. Off by default because it overwrites the framework's tracked patch files in place — only enable it when you intend to update them. In practice you reach for it through the `rewrite-kernel-patches` / `rewrite-uboot-patches` CLI commands, which set it for you.

#### REWRITE_PATCHES_NEEDING_REBASE

`string` · default: `no`

Narrows `REWRITE_PATCHES` so it only rewrites the patches that no longer apply cleanly and had to be rebased, leaving every patch that still applied as-is untouched. This keeps a bulk rewrite from reformatting and re-dating the whole patch set — and producing a huge, noisy diff — when only a handful of patches actually needed fixing after a source update. Use it (via the `rewrite-*-patches-needing-rebase` CLI commands) for the common maintenance case of refreshing a patch set against newer upstream sources.

#### CREATE_PATCHES_ATF

`string` · default: `no`

Interrupts the ARM Trusted Firmware (TF-A) build right after its patches are applied, so you can edit the source tree by hand; when you continue, the framework diffs your changes and writes them out as a new ATF patch. Off by default since it only makes sense during firmware development, and it makes the build interactive. Trigger it through the `atf-patch` CLI command rather than setting it directly. Note that ATF and crust still use the older bash "userpatch" flow, not the git-based round-trip above.

#### CREATE_PATCHES_CRUST

`string` · default: `no`

The crust counterpart to `CREATE_PATCHES_ATF`: it pauses the crust (Allwinner power-management coprocessor) firmware build after patching so you can edit the source, then captures your changes as a new crust patch when you resume. Off by default for the same reasons — it is only for firmware work and turns the build interactive. Reach for it through the `crust-patch` CLI command.

#### FORCE_CHECK_MD5_PACKAGES

`string` · default: `no`

Runs `debsums` over the freshly built rootfs to verify that every installed package's files still match the md5 checksums recorded in its `.deb`, catching a corrupted download or a botched install before the image is finished. The check is skipped by default because it adds time to every rootfs build, and even when forced it only runs for distributions whose status is `supported`. Turn it on when you suspect package corruption or want the extra integrity check on a release build.

#### WRITE_EXTENSIONS_METADATA

`string` · default: `yes`

Records which extensions were called at each hook point during the build and writes that metadata out, so tooling such as `show-extensions` can report exactly what ran and where. Left on by default because the cost is negligible and the data is useful for debugging extension behaviour. Set `no` to skip it — a few info-only helper commands (for example the deb-download tooling) do this automatically, since they run the config machinery but never actually build and have no use for the metadata.
