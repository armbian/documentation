---
seo_title: "Armbian image type switches: minimal & desktop"
description: "Choose the Armbian image type: BUILD_MINIMAL for a bare CLI image, or BUILD_DESKTOP with DESKTOP_ENVIRONMENT and DESKTOP_TIER for a desktop build."
---

# Image type

Armbian builds three image flavours, chosen with the two switches below: a **minimal** bare-CLI image, the **standard** CLI/server image (the default when neither switch is set), and a **desktop** image. For desktop builds you then pick which environment to install and how many applications come with it.

#### BUILD_MINIMAL

`string`

- `yes`: build a bare command-line image with only the essential packages
- `no` (default)

Produces the smallest possible image — no desktop and none of the extra server utilities that ship in the standard CLI image — so it boots fast and leaves the most room for your own workload. It suits headless appliances and single-application deployments where you install exactly what you need on top. **Not compatible** with `BUILD_DESKTOP=yes`; leaving both switches at `no` builds the standard CLI/server image instead.

#### BUILD_DESKTOP

`string`

- `yes`: build a graphical desktop image
- `no` (default)

Adds a full graphical desktop on top of the base system. When set, choose the desktop with [`DESKTOP_ENVIRONMENT`](#desktop_environment) and how much software it bundles with [`DESKTOP_TIER`](#desktop_tier); in interactive mode the build prompts for both. Mutually exclusive with `BUILD_MINIMAL=yes`.

#### DESKTOP_ENVIRONMENT

`string`

Which desktop environment to install when `BUILD_DESKTOP=yes` — for example `xfce`, `gnome`, `kde-plasma`, `mate` or `cinnamon`. Setting it on the command line skips the interactive prompt. The list of available environments is defined per release by [armbian-config](/config/desktops/), so not every desktop is offered on every board and release combination.

#### DESKTOP_TIER

`string`

- `minimal`: the desktop environment on its own, with almost no extra applications
- `mid`: the desktop plus a common everyday application set — browser, file manager, media and utilities (the interactive default)
- `full`: the desktop plus the complete bundled application set, including the heavier office and productivity apps

Controls how much software is preinstalled alongside the desktop, letting you trade image size against out-of-the-box convenience.
