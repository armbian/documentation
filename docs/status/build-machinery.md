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

!!! note "Powered on demand"

    Not all of this capacity runs around the clock. A good part of the fleet
    sits on **standby and only powers up when there is build demand**, then
    spins back down once the queue is clear — keeping idle energy use and cost
    low as part of a greener build infrastructure. A server showing few or no
    online runners may simply be asleep, not broken.

<!-- build-machinery:start -->
## Build servers

**17** servers · **686** threads · **1933** GB RAM · **284** runners (**167** online).

| Server | Location | Threads | RAM | Runners | Status |
|:-------|:---------|--------:|----:|--------:|:------:|
| `insa-trixie` | Hetzner Germany | 176 | 384 GB | 40 | active |
| `ampere-1` | Armbian Datacenter | 128 | 512 GB | 64 | active |
| `kspace` | Kspace Estonia | 128 | 256 GB | 32 | active |
| `github` | GitHub | 40 | 137 GB | 20 | active |
| `rack-ryzen` | Armbian Datacenter | 32 | 125 GB | 15 | active |
| `stpete` | JetHome | 24 | 64 GB | 6 | active |
| `geekom` | Armbian Datacenter | 20 | 62 GB | 8 | active |
| `vps8000-1` | Netcup Germany | 18 | 62 GB | 9 | active |
| `vps8000-2` | Netcup Germany | 18 | 62 GB | 14 | active |
| `cats` | Auroradev Las Vegas | 16 | 32 GB | 6 | active |
| `oregon-1` | Oregon UNI | 16 | 32 GB | 8 | active |
| `oregon-2` | Oregon UNI | 16 | 32 GB | 8 | active |
| `stmir` | JetHome | 16 | 94 GB | 12 | active |
| `vps3000-1` | Netcup Germany | 12 | 24 GB | 8 | active |
| `repoassembly` | Netcup Germany | 10 | 16 GB | 26 | active |
| `werner-trixie` | Hetzner Germany | 8 | 31 GB | 4 | active |
| `xogium-ryzen` | Xogium | 8 | 8 GB | 4 | active |

<!-- build-machinery:end -->
