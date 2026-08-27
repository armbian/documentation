---
title: Build machinery
seo_title: "Armbian build machinery: build server fleet"
description: "The Armbian build machinery — the build servers that compile Armbian: CPU-thread capacity, memory and location from NetBox, and the GitHub runner processes each hosts."
---
# Build machinery

The build servers that compile Armbian — their CPU-thread capacity, memory and
location (from [NetBox](https://netbox.armbian.com/)), and how many GitHub
runner processes each server hosts (from the
[GitHub organisation](https://github.com/armbian)).

<!-- build-machinery:start -->
## Build servers

_Build servers from [NetBox](https://netbox.armbian.com/), role `userlevel-runner`. The **Runners** column is the number of GitHub runner processes registered on that server (its runners are named `<server>-NN`), falling back to the value recorded in NetBox when GitHub can't be queried._

**15** servers — **13** active, **2** offline · **658** CPU threads (**622** active) · **1846** GB RAM · **245** runners (**104** online).

| Server | Location | Threads | RAM | Runners | Status |
|:-------|:---------|--------:|----:|--------:|:------:|
| `insa-trixie` | Hetzner Germany | 176 | 384 GB | 40 | active |
| `ampere-1` | Armbian Datacenter | 128 | 512 GB | 64 | active |
| `kspace` | Kspace Estonia | 128 | 256 GB | 32 | active |
| `github` | GitHub | 40 | 137 GB | 20 | active |
| `3950x` | Armbian Datacenter | 32 | 125 GB | 8 | ⚠️ decommissioning |
| `rack-ryzen` | Armbian Datacenter | 32 | 125 GB | 15 | active |
| `stpete` | JetHome | 24 | 64 GB | 6 | active |
| `geekom` | Mirrors | 20 | 62 GB | 8 | active |
| `cats` | Auroradev Las Vegas | 16 | 32 GB | 6 | active |
| `oregonalfa` | Oregon UNI | 16 | 31 GB | 6 | active |
| `oregonbeta` | Oregon UNI | 16 | 31 GB | 6 | active |
| `repoassembly` | Netcup Germany | 10 | 16 GB | 26 | active |
| `mt7925e` | Kspace Estonia | 8 | 16 GB | 2 | active |
| `werner` | Hetzner Germany | 8 | 31 GB | 4 | active |
| `big-arm` | LaneCloud | 4 | 24 GB | 2 | ⚠️ offline |

<!-- build-machinery:end -->
