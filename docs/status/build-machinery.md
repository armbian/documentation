---
title: Build machinery
seo_title: "Armbian build machinery: self-hosted runner fleet"
description: "The Armbian build machinery — self-hosted GitHub Actions runners, their CPU-thread capacity, memory and location — from NetBox and the GitHub organisation."
---
# Build machinery

The self-hosted runners that build Armbian — their CPU-thread capacity, memory
and location (from [NetBox](https://netbox.armbian.com/)), and how they are
registered by label on the [GitHub organisation](https://github.com/armbian).

<!-- build-machinery:start -->
## Runner fleet

_Self-hosted runners from [NetBox](https://netbox.armbian.com/), role `userlevel-runner`._

**20** runners — **16** active, **4** offline · **730** CPU threads (**690** active) · **2045** GB RAM.

| Runner | Location | Threads | RAM | Status |
|:-------|:---------|--------:|----:|:------:|
| `insanisfiction.armbian.de` | Hetzner Germany | 176 | 375 GB | active |
| `ampere-1` | GitHub | 128 | 500 GB | active |
| `kspace` | Imola | 128 | 264 GB | active |
| `github.com` | GitHub | 40 | 137 GB | active |
| `3950x` | Armbian Datacenter | 32 | 125 GB | active |
| `game.imola.armbian.com` | Imola | 32 | 132 GB | active |
| `rack-ryzen` | Armbian Datacenter | 32 | 125 GB | active |
| `stpete-runner.armbian.com` | JetHome | 24 | 64 GB | active |
| `geekom` | Mirrors | 20 | 62 GB | active |
| `cats` | Auroradev Las Vegas | 16 | 32 GB | active |
| `mind` | GitHub | 16 | 16 GB | ⚠️ offline |
| `oregon-uni-1.armbian.com` | Oregon UNI | 16 | 31 GB | active |
| `oregon-uni-2.armbian.com` | Oregon UNI | 16 | 31 GB | active |
| `repo.armbian.com` | Netcup Germany | 10 | 16 GB | active |
| `mt7925e` | Kspace Estonia | 8 | 16 GB | active |
| `nanopim6` | GitHub | 8 | 32 GB | ⚠️ offline |
| `rock5-16g-aarch64-01-04` | Rock 5 #1 | 8 | 16 GB | ⚠️ offline |
| `rock5-16g-aarch64-05-08` | Rock 5 #2 | 8 | 16 GB | ⚠️ offline |
| `werner` | Hetzner Germany | 8 | 31 GB | active |
| `big-arm` | LaneCloud | 4 | 24 GB | active |

<!-- build-machinery:end -->
