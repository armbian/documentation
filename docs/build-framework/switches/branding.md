---
seo_title: "Armbian image branding / vendor build switches"
description: "Rebrand Armbian images: VENDOR, VENDORURL, VENDORLOGO, MAINTAINER and related switches that write /etc/os-release, /etc/issue, the login MOTD and the .deb package signatures."
---

# Branding

Rebrand the built image's identity — the OS name, URLs, logo, MOTD colour and package maintainer. Set these to ship your own white-labelled images instead of stock Armbian. They are normally set together in a [build configuration file](/build-framework/getting-started/#cli).

These switches populate the image's identity files: `/etc/os-release`, `/etc/issue` and `/etc/issue.net`, `/etc/armbian-release`, `/etc/armbian-image-release`, the login MOTD, and the signature on the generated `.deb` packages.

!!! info "Defaults are deliberate placeholders"
    Left unset, the framework fills these with placeholder fallbacks (shown as the defaults below), so an un-branded build identifies itself as `Armbian-unofficial` rather than masquerading as an official release. A branded build overrides the whole group — see the [example](#a-full-rebrand) at the end.

#### VENDOR

`string` · default: `Armbian-unofficial`

The vendor / OS name. Written to `/etc/os-release` `PRETTY_NAME` (as `<VENDOR> <version> <release>`), `/etc/issue`, `/etc/issue.net` and `/etc/armbian-release`. When unset it becomes `Armbian-unofficial`, marking the image as not an official build.

#### VENDORPRETTYNAME

`string` · optional

A friendly vendor name recorded in `/etc/armbian-image-release` (`VENDORPRETTYNAME=`). Unset by default.

#### VENDORCOLOR

`string` (ANSI 256 / `R;G;B`) · default: `247;16;0`

Colour used for the vendor logo in the login MOTD. Written to `/etc/armbian-release`.

#### VENDORURL

`string` (URL) · default: `https://duckduckgo.com/`

Home page for the OS — os-release `HOME_URL`.

#### VENDORDOCS

`string` (URL) · default: `https://docs.armbian.com/`

Documentation URL, recorded in `/etc/armbian-release`.

#### VENDORSUPPORT

`string` (URL) · default: `https://community.armbian.com/`

Support URL — os-release `SUPPORT_URL`.

#### VENDORPRIVACY

`string` (URL) · default: `https://duckduckgo.com/`

Privacy-policy URL — os-release `PRIVACY_POLICY_URL`.

#### VENDORBUGS

`string` (URL) · default: `https://armbian.atlassian.net/`

Bug-report URL — os-release `BUG_REPORT_URL`.

#### VENDORLOGO

`string` · default: `armbian-logo`

Freedesktop icon name written to os-release `LOGO=` — the icon that tools like the desktop **About** dialog or `fastfetch` resolve from the icon theme (the asset ships as `/usr/share/pixmaps/<name>.svg`). It is **not** the boot splash; to change the Plymouth boot logo see [Boot splash (Plymouth)](#boot-splash-plymouth) below.

#### MAINTAINER

`string` · default: `John Doe`

Maintainer name used to sign the generated `.deb` packages and recorded in `/etc/armbian-release`.

#### MAINTAINERMAIL

`string` · default: `john.doe@somewhere.on.planet`

Maintainer e-mail used for the `.deb` package signatures.

## A full rebrand

Branded builds set the whole group together in a build config. For example, the values official Armbian images use:

```bash
declare -g VENDOR="Armbian"
declare -g VENDORCOLOR="247;16;0"
declare -g VENDORURL="https://www.armbian.com"
declare -g VENDORDOCS="https://docs.armbian.com"
declare -g VENDORSUPPORT="https://forum.armbian.com"
declare -g VENDORPRIVACY="https://www.armbian.com"
declare -g VENDORBUGS="https://www.armbian.com/bugs"
declare -g VENDORLOGO="armbian-logo"
declare -g MAINTAINER="Armbian Linux"
declare -g MAINTAINERMAIL="info@armbian.com"
```

!!! note "Official builds"
    When `VENDOR=Armbian`, the framework also refuses vendor branding on community / unsupported combinations (it resets several of these fields), so only genuinely official images carry the full Armbian identity.

## Boot splash (Plymouth)

The graphical boot splash is a separate asset from the branding switches above — it is **not** controlled by `VENDORLOGO`. It ships in the `armbian-plymouth-theme` package.

To use your own boot logo, replace the source image in the build framework:

- **File:** `packages/plymouth-theme-armbian/armbian-logo.png`
- **Size:** a **square PNG**, resized to **256×256** at build time — supply 256×256 (or a larger square; it is downscaled), on a transparent background (the splash background is black).

The build installs it as `/usr/share/plymouth/themes/armbian/bgrt-fallback.png`. The `bgrt-fallback` name means it is the logo used when the firmware provides no BGRT boot logo — the case on virtually all SBCs, so this is the logo you actually see.

Companion assets in the same folder: `watermark.png` (333×50, a wordmark shown centred) and `spinner.gif` (resized to a 52×52 throbber).

!!! tip "Without editing the framework tree"
    From `userpatches/customize-image.sh` you can overwrite `/usr/share/plymouth/themes/armbian/bgrt-fallback.png` (256×256) in the rootfs. Plymouth's early-boot copy lives in the initramfs, which the build regenerates after `customize-image.sh`, so dropping the file there is enough.
