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

_Build servers from [NetBox](https://netbox.armbian.com/), role `userlevel-runner`. The **Runners** column is the number of GitHub runner processes registered on that server (matched by its label), falling back to the value recorded in NetBox when GitHub can't be queried._

**20** servers — **16** active, **4** offline · **730** CPU threads (**690** active) · **2045** GB RAM.

| Server | Location | Threads | RAM | Runners | Status |
|:-------|:---------|--------:|----:|--------:|:------:|
| `insa-trixie` | Hetzner Germany | 176 | 375 GB | 50 | active |
| `ampere-1` | GitHub | 128 | 500 GB | 41 | active |
| `kspace` | Imola | 128 | 264 GB | 24 | active |
| `github` | GitHub | 40 | 137 GB | 20 | active |
| `3950x` | Armbian Datacenter | 32 | 125 GB | 8 | active |
| `game` | Imola | 32 | 132 GB | 15 | active |
| `rack-ryzen` | Armbian Datacenter | 32 | 125 GB | 15 | active |
| `stpete` | JetHome | 24 | 64 GB | 8 | active |
| `geekom` | Mirrors | 20 | 62 GB | 4 | active |
| `cats` | Auroradev Las Vegas | 16 | 32 GB | 6 | active |
| `mind` | GitHub | 16 | 16 GB | 2 | ⚠️ offline |
| `oregonalfa` | Oregon UNI | 16 | 31 GB | 6 | active |
| `oregonbeta` | Oregon UNI | 16 | 31 GB | 6 | active |
| `repoassembly` | Netcup Germany | 10 | 16 GB | 16 | active |
| `mt7925e` | Kspace Estonia | 8 | 16 GB | 2 | active |
| `nanopim6` | GitHub | 8 | 32 GB | 6 | ⚠️ offline |
| `rock5-16g-aarch64-01-04` | Rock 5 #1 | 8 | 16 GB | 0 | ⚠️ offline |
| `rock5-16g-aarch64-05-08` | Rock 5 #2 | 8 | 16 GB | 0 | ⚠️ offline |
| `werner` | Hetzner Germany | 8 | 31 GB | 4 | active |
| `big-arm` | LaneCloud | 4 | 24 GB | 2 | active |

<!-- build-machinery:end -->
