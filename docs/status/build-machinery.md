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

**18** servers — **15** active, **3** offline · **706** CPU threads (**686** active) · **2045** GB RAM · **260** runners (**104** online).

| Server | Location | Threads | RAM | Runners | Status |
|:-------|:---------|--------:|----:|--------:|:------:|
| `insa-trixie` | Hetzner Germany | 176 | 384 GB | 40 | active |
| `ampere-1` | Armbian Datacenter | 128 | 512 GB | 64 | active |
| `kspace` | Imola | 128 | 270 GB | 32 | active |
| `github` | GitHub | 40 | 140 GB | 20 | active |
| `3950x` | Armbian Datacenter | 32 | 128 GB | 8 | active |
| `game` | Imola | 32 | 135 GB | 15 | active |
| `rack-ryzen` | Armbian Datacenter | 32 | 128 GB | 15 | active |
| `stpete` | JetHome | 24 | 66 GB | 6 | active |
| `geekom` | Mirrors | 20 | 64 GB | 8 | active |
| `cats` | Auroradev Las Vegas | 16 | 33 GB | 6 | active |
| `oregonalfa` | Oregon UNI | 16 | 32 GB | 6 | active |
| `oregonbeta` | Oregon UNI | 16 | 32 GB | 6 | active |
| `repoassembly` | Netcup Germany | 10 | 16 GB | 26 | active |
| `mt7925e` | Kspace Estonia | 8 | 16 GB | 2 | active |
| `rock5-16g-aarch64-01-04` | Rock 5 #1 | 8 | 16 GB | 0 | ⚠️ offline |
| `rock5-16g-aarch64-05-08` | Rock 5 #2 | 8 | 16 GB | 0 | ⚠️ offline |
| `werner` | Hetzner Germany | 8 | 32 GB | 4 | active |
| `big-arm` | LaneCloud | 4 | 25 GB | 2 | ⚠️ offline |

<!-- build-machinery:end -->
