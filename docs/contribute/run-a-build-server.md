---
seo_title: "Donate an Armbian build server: CI runner hardware"
description: "Armbian is looking for build servers to host CI runners — 16 cores and 64 GB RAM or better, ideally 32 cores and 128 GB. How to offer one and what it will be used for."
---
# Run a build server

Every Armbian image, kernel and u-boot package is compiled on hardware donated by
the community. You can see [what that fleet looks like today](../status/build-machinery.md) —
servers, threads, memory and how many runners each one hosts.

**We are looking for more of it.** Build demand grows with every board Armbian
supports, and the queue is the limit on how quickly a fix reaches users.

## What we are looking for

| | Minimum | Ideal |
|:--|:--|:--|
| CPU | 16 cores | **32 cores** |
| Memory | 64 GB | **128 GB** |

Both `x86-64` and `arm64` are useful — a good part of the fleet is already ARM.
Fast local storage matters more than capacity: kernel builds are I/O heavy, and
the framework wants roughly 50 GB per concurrent build, so size the disk by how
many runners the machine will host.

## What it will be used for

The server joins the fleet as one or more **self-hosted GitHub runners** and
picks up jobs from the build pipeline — compiling kernels, u-boot and rootfs, and
assembling images. Nothing else runs on it.

Capacity is used **on demand**, not around the clock. Much of the fleet sits on
standby and powers up only when there is a queue, then spins back down — so a
donated machine is not a machine burning power idle.

## How to offer one

Reach out through the [contact form](https://www.armbian.com/contact/) with the
specs, the location and how you would prefer to give access. We will take it from
there and help with the setup — [armbian-config installs the runner](../software/gh-runners.md)
in a few steps on an Armbian host.

Hosting is credited on the [build machinery page](../status/build-machinery.md)
alongside the rest of the fleet.

Thanks for helping keep Armbian building.
