---
seo_title: "Armbian image type switches: minimal & desktop"
description: "Choose the Armbian image type: BUILD_MINIMAL for a bare CLI image, or BUILD_DESKTOP with DESKTOP_ENVIRONMENT and DESKTOP_TIER for a desktop build."
---

# Image type

Whether to build a minimal CLI image or a desktop image, and which desktop to install.

#### BUILD_MINIMAL

`string`

- `yes`: build a bare CLI image suitable for application deployment. **Not compatible** with `BUILD_DESKTOP=yes`.
- `no` (default)

#### BUILD_DESKTOP

`string`

- `yes`: build a desktop image (pick the environment and tier below)
- `no` (default)

#### DESKTOP_ENVIRONMENT

`string`

Desktop environment to install when `BUILD_DESKTOP=yes` — e.g. `xfce`, `gnome`, `kde-plasma`, `mate`, `cinnamon`. Set manually to skip the dialog prompt; the available environments are provided by armbian-config.

#### DESKTOP_TIER

`string`

- `minimal`: bare desktop
- `mid`: desktop plus a common application set (interactive default)
- `full`: desktop plus the full bundled application set

Selects how many applications are bundled with the desktop. Replaces the removed `DESKTOP_APPGROUPS_SELECTED` and `DESKTOP_ENVIRONMENT_CONFIG_NAME` switches.
