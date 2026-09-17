---
seo_title: "Armbian Datacenter access for board maintainers"
description: "Access the Armbian Datacenter hardware lab: request board-maintainers GitHub team membership and connect over VPN to debug and test boards on real hardware."
---

# Datacenter access

Armbian runs a hardware lab — *the Datacenter* — a rack of real boards on real
networks that our CI flashes, powers, boots, tests and measures automatically.
Board maintainers can reach these boards remotely to debug problems, reproduce
issues and validate images on actual hardware.

![The Armbian Datacenter rack](../images/dc-rack.png)

## What the lab can do

Boards are not simply plugged in and pinged. Each bench is wired for as much
remote control as the hardware allows, and the automated runs use all of it.

- **Remote flashing.** Boards fitted with an SD-card switcher, or reachable in
  Rockchip maskrom mode, can be re-imaged over the network with nobody touching
  the rack. This is still being brought into routine use — see the note at the
  end of this page — so most runs currently test the upgrade path on whatever
  the board already has installed.
- **NFS boot.** A board can be switched to mount its root filesystem over NFS
  from the lab's server, running a centrally prepared filesystem instead of the
  contents of its own SD card. Its kernel and initrd still come from the local
  boot medium. Boards boot locally unless deliberately switched over; the
  [Datacenter boards](/status/boards/) table records which is which.
- **Switched power.** Per-board power control through relay PDUs, APC PDUs and
  PoE switches. A power cycle is graceful by default: the OS is asked to shut
  down and confirmed down before the outlet is cut. That is what makes
  unattended re-imaging safe on hardware nobody is standing next to.
- **Power measurement.** On boards powered over PoE, consumption is sampled
  throughout the run, so the result carries idle and peak wattage alongside
  everything else.
- **Serial console server.** Cabled boards have their UART reachable over the
  network through a console server. Runs record the entire boot — U-Boot,
  kernel, and any panic — which is the only view left when a board never reaches
  the network at all. Maintainers can attach to the same console interactively.
- **Network throughput.** iperf3 against a lab-local server, in both
  directions, on *every* interface a board has rather than just the one it is
  managed through.
- **Wireless and Bluetooth.** Wi-Fi association and throughput, and Bluetooth
  controller checks, on boards carrying the radios.
- **Benchmarks and thermals.** CPU, memory and storage throughput, verification
  that CPU frequency scaling actually reaches the advertised maximum, and
  thermal-zone readings under load.

What a given board supports depends on how its bench is wired, so the coverage
differs from board to board. Results are published automatically:
[Datacenter boards](/status/boards/) for the inventory,
[Tested boards](/status/board-tests/) for per-board outcomes, and
[Wi-Fi performance](/status/wifi-performance/) for wireless throughput.

Access is over a VPN and is available to members of the
[**board-maintainers**](https://github.com/orgs/armbian/teams/board-maintainers)
GitHub team. Everything below (VPN login and board access) only works once you
are on that team.

## Requesting access

The `board-maintainers` team is a *visible* team, so organization members can
request to join it themselves:

- **If you are already an Armbian GitHub organization member** — open the
  [board-maintainers team page](https://github.com/orgs/armbian/teams/board-maintainers)
  and click **Request to join**. A team maintainer reviews and approves it.
- **If you are not an organization member yet** — every contributor is
  automatically invited to become a member of the
  [Armbian organization](https://github.com/armbian), so contribute (e.g. a
  merged pull request) and accept the invitation that follows. Once you are an
  org member, request to join the team as above.

## Connect via VPN (Netbird)

The Datacenter network is reached through [Netbird](https://netbird.io), a
WireGuard-based mesh VPN. Authentication is via **GitHub**: you sign in with your
GitHub account and are let in if you belong to the `board-maintainers` team.

### 1. Install the Netbird client

On Linux:

```bash
curl -fsSL https://pkgs.netbird.io/install.sh | sh
```

On macOS and Windows, install the client from
[netbird.io/downloads](https://netbird.io/downloads) (or via `brew`, `winget`,
etc.).

### 2. Connect to Armbian's Netbird

```bash
netbird up --management-url https://netbird.armbian.com
```

This opens your browser to authenticate:

1. On the Netbird sign-in screen, choose **Continue with Authentik**.

    ![Netbird sign-in — Continue with Authentik](../images/authentic-2.png){ width=50% }

2. On the *Armbian Auth* screen, click the **GitHub** icon (the button below
    *Log in* — not the email/username field) and authorize the request.

    ![Armbian Auth — sign in with GitHub](../images/authentic-1.png){ width=50% }

Once GitHub confirms you are a `board-maintainers` member you are connected to
the Datacenter mesh. The management URL is remembered, so next time you can just
run `netbird up`.

Check the connection and your assigned VPN address:

```bash
netbird status
```

To disconnect, run `netbird down`.

## Access boards

Once connected you are on the Datacenter network and can reach the boards
directly by their IP address.

Find the board you need — its model and IP address — in the [Boards](#boards)
list below, then SSH in as **root**:

```bash
ssh root@<board-ip>        # e.g. ssh root@10.0.50.42
```

No password is needed — every board installs the SSH public keys from your
GitHub account (`https://github.com/<your-username>.keys`) into root's
authorized keys, so make sure the matching private key is on the machine you
connect from.

If a board is unreachable it may be powered off or mid-test. For anything you
cannot resolve (missing access, a wedged board), reach out on the
[Armbian Discord](https://discord.com/invite/armbian) channels.

!!! warning "Reflashing is under testing"
    Automated board reflashing is still experimental. If you reflash a board and
    accidentally brick it or leave it unresponsive, please report it on the
    [Armbian Discord](https://discord.com/invite/armbian) so it can be recovered.

## Boards

The datacenter's board inventory — which boards are operational or broken — now lives on the [**Datacenter boards**](/status/boards/) status page.
