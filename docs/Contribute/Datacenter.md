# Datacenter access

Armbian runs a hardware lab — *the Datacenter* — a rack of real boards on real
networks that our CI flashes, powers, boots, tests and measures automatically.
Board maintainers can reach these boards remotely to debug problems, reproduce
issues and validate images on actual hardware.

![The Armbian Datacenter rack](../images/dc-rack.png)

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

This opens your browser to authenticate. Log in with **GitHub** and authorize the
request. Once you are verified as a `board-maintainers` member you are connected
to the Datacenter mesh. The management URL is remembered, so later you can simply
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

The list below is kept up to date automatically by the reconcile action, which
scans the Datacenter and opens a pull request to refresh it — the same mechanism
used for the [wireless performance results](../WifiPerformance.md).

<!-- BOARDS-START -->

**59** active boards.

| Board | IP address | Boot | Link | Switch | Last seen |
|:--|:--|:--|--:|:--|--:|
| Banana Pi CM4IO 01 | 10.0.50.10 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Banana Pi M2 Ultra 01 | 10.0.50.47 | local | 1GbE | TP-Link TL-SG3428X | today |
| Banana Pi M2Pro 01 | 10.0.50.43 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Banana Pi M5 01 | 10.0.50.55 | local | 1GbE | Netgear GS348 | today |
| Banana Pi Pro 01 | 10.0.50.52 | local | 100MbE | Netgear GS348 | today |
| BananaPi BPI-F3 01 | 10.0.50.70 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Clearfog Pro 01 | 10.0.50.42 | local | 1GbE | TP-Link TL-SG3428X | today |
| Cubietruck 01 | 10.0.50.49 | local | 1GbE | TP-Link TL-SG3428X | today |
| Cubox i2eX/i4 01 | 10.0.50.63 | local | 1GbE | Netgear GS348 | today |
| Espressobin 01 | 10.0.50.26 | local | 1GbE | TP-Link TL-SG3428X | today |
| Helios4 01 | 10.0.50.58 | local | 1GbE | Netgear GS348 | today |
| Inovato Quadra 01 | 10.0.50.36 | local | 100MbE | Netgear GS348 | today |
| Khadas VIM1 02 | 10.0.20.119 | local | 100MbE | — | today |
| Khadas VIM2 01 | 10.0.50.12 | local | 1GbE | Netgear GS348 | today |
| Khadas VIM3 01 | 10.0.50.38 | local | 1GbE | Netgear GS348 | today |
| NanoPC T6 LTS 01 | 10.0.50.30 | local | 2.5GbE | TP-Link SG3218XP-M2 | today |
| NanoPi Duo 01 | 10.0.50.48 | local | 100MbE | Netgear GS348 | today |
| NanoPi K2 01 | 10.0.50.76 | local | 1GbE | Netgear GS348 | today |
| NanoPi M4V2 01 | 10.0.50.97 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| NanoPi M5 01 | 10.0.50.35 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| NanoPi Neo 3 01 | 10.0.50.20 | local | 1GbE | TP-Link TL-SG3428X | today |
| Nanopi R2S 01 | 10.0.50.65 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| NanoPi R4S 01 | 10.0.50.25 | local | 1GbE | Netgear GS348 | today |
| NanoPi R6S 01 | 10.0.50.40 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| NanoPi R76S 01 | 10.0.50.67 | local | 2.5GbE | Netgear XS508M | today |
| Odroid C1 01 | 10.0.50.27 | local | 1GbE | Netgear GS348 | today |
| Odroid C2 01 | 10.0.50.87 | local | 1GbE | Netgear GS348 | today |
| Odroid C4 01 | 10.0.50.13 | local | 1GbE | TP-Link TL-SG3428X | today |
| Odroid M1 01 | 10.0.50.19 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Odroid N2 02 | 10.0.50.66 | local | 1GbE | TP-Link TL-SG3428X | today |
| Odroid XU4 01 | 10.0.50.51 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Orange Pi 3 01 | 10.0.50.57 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Orange Pi 5 01 | 10.0.50.39 | local | 1GbE | TP-Link SG3218XP-M2 | today |
| Orange Pi 5 Plus 01 | 10.0.50.33 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Orange Pi One+ 01 | 10.0.50.125 | local | 1GbE | TP-Link TL-SG3428X | today |
| Orange Pi PC2 01 | 10.0.50.68 | local | 1GbE | TP-Link TL-SG3428X | today |
| Orange Pi R1 01 | 10.0.50.50 | local | 1GbE | — | today |
| Orange Pi Win 01 | 10.0.50.24 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Orange Pi Zero 02 | 10.0.50.46 | local | 100MbE | — | today |
| Orange Pi Zero Plus 01 | 10.0.50.54 | local | 1GbE | TP-Link TL-SG3428X | today |
| Orange Pi Zero2 01 | 10.0.50.74 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| OrangePi 3 LTS 02 | 10.0.50.16 | local | 1GbE | — | today |
| Pine H64 01 | 10.0.50.34 | local | 1GbE | TP-Link TL-SG3428X | today |
| Radxa ZERO 3 01 | 10.0.20.185 | local | 1GbE | — | today |
| Raspberry Pi 01 | 10.0.50.15 | local | 1GbE | Netgear GS348 | today |
| Raspberry Pi 02 | 10.0.50.22 | local | 100MbE | Netgear GS348 | today |
| ROCK 2F 01 | 10.0.20.164 | local | — | — | today |
| Rock 5B 01 | 10.0.50.69 | local | 2.5GbE | Netgear XS508M | today |
| Rock 5B 02 | 10.0.50.17 | local | 2.5GbE | Netgear XS508M | today |
| Rock 5B Plus 01 | 10.0.50.41 | local | 2.5GbE | Netgear XS508M | today |
| Rock 5T 01 | 10.0.50.11 | local | 2.5GbE | TP-Link SG3218XP-M2 | today |
| Rockpi E 01 | 10.0.50.28 | local | 1GbE | TP-Link TL-SG3428X | today |
| SpacemiT K3 Pico-ITX 01 | 10.0.50.44 | local | 10GbE | Netgear S3300-52X-PoE+ | today |
| Tanix TX6 01 | 10.0.50.21 | local | 100MbE | Netgear GS348 | today |
| Tinker Board 01 | 10.0.50.29 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| Tinker Board 2 01 | 10.0.50.23 | local | 1GbE | TP-Link TL-SG3428X | today |
| Udoo 01 | 10.0.50.62 | local | 1GbE | Netgear S3300-52X-PoE+ | today |
| UEFI arm64 01 | 10.0.50.45 | local | 10GbE | Netgear XS712T | today |
| UEFI x86 01 | 10.0.50.53 | local | 1GbE | Netgear GS348 | today |

<!-- BOARDS-STOP -->
