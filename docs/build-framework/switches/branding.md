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

Name of the logo asset used for the login MOTD — os-release `LOGO`.

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
