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

The list below is refreshed by the reconcile action (`Inventory: scan &
reconcile` in the autotests repo): it scans the Datacenter and opens a pull
request to update this table — the same mechanism used for the
[wireless performance results](../WifiPerformance.md).

<!-- BOARDS-START -->

**71** boards (10 failed).

| Board | Status | IP address | Boot | Link | Switch | Last seen |
|:--|:--:|:--|:--|--:|:--|--:|
| Arduino UNO Q 01 | ✅ | 10.0.20.131 | local | Wi-Fi 5 | Zyxel NWA130BE | 13 Aug |
| Banana Pi CM4IO 01 | ✅ | 10.0.50.12 | local | 1 GbE | Netgear S3300-52X-PoE+ (43) | 13 Aug |
| Banana Pi M2 Ultra 01 | ✅ | 10.0.50.47 | local | 1 GbE | TP-Link TL-SG3428X (13) | 13 Aug |
| Banana Pi M2Pro 01 | ✅ | 10.0.50.43 | local | 1 GbE | Netgear S3300-52X-PoE+ (47) | 13 Aug |
| Banana Pi M5 01 | ✅ | 10.0.50.55 | local | 1 GbE | Netgear GS348 (19) | 13 Aug |
| Banana Pi Pro 01 | ✅ | 10.0.50.52 | local | 100 MbE | Netgear GS348 (8) | 13 Aug |
| BananaPi BPI-F3 01 | ✅ | 10.0.50.70 | local | 1 GbE | Netgear S3300-52X-PoE+ (46) | 13 Aug |
| BigTreeTech CB1 01 | ✅ | 10.0.50.62 | local | Wi-Fi 4 | Zyxel NWA130BE | 13 Aug |
| Clearfog Pro 01 | ✅ | 10.0.50.42 | local | 1 GbE | TP-Link TL-SG3428X (12) | 13 Aug |
| Cubie A5E 01 | ✅ | 10.0.50.10 | local | 1 GbE | Netgear S3300-52X-PoE+ (4) | 13 Aug |
| Cubietruck 01 | ✅ | 10.0.50.49 | local | 1 GbE | TP-Link TL-SG3428X (14) | 13 Aug |
| Cubox i2eX/i4 01 | ✅ | 10.0.50.63 | local | 1 GbE | Netgear GS348 (32) | 13 Aug |
| Espressobin 01 | ✅ | 10.0.50.56 | local | 1 GbE | TP-Link TL-SG3428X (11) | 13 Aug |
| Helios4 01 | ✅ | 10.0.50.58 | local | 1 GbE | Netgear GS348 (11) | 13 Aug |
| Inovato Quadra 01 | ❌ | 10.0.50.36 | local | 100 MbE | Netgear GS348 (17) | 09 Aug |
| Khadas VIM1 01 | ❌ | 10.0.50.71 | local | 100 MbE | Netgear GS348 (3) | 05 Aug |
| Khadas VIM2 01 | ✅ | 10.0.50.28 | local | 1 GbE | Netgear GS348 (13) | 13 Aug |
| Khadas VIM3 01 | ✅ | 10.0.50.38 | local | 1 GbE | Netgear GS348 (36) | 13 Aug |
| Le potato 01 | ✅ | 10.0.50.75 | local | 100 MbE | Netgear GS348 (12) | 13 Aug |
| Mekotronics R58S2 01 | ✅ | 10.0.50.19 | local | 1 GbE | Netgear GS348 (48) | 13 Aug |
| NanoPC T6 LTS 01 | ❌ | 10.0.50.30 | local | 2.5 GbE | TP-Link SG3218XP-M2 (8) | 11 Aug |
| NanoPi Duo 01 | ✅ | 10.0.50.48 | local | 100 MbE | Netgear GS348 (31) | 13 Aug |
| NanoPi K2 01 | ✅ | 10.0.50.76 | local | 1 GbE | Netgear GS348 (20) | 13 Aug |
| NanoPi M4V2 01 | ✅ | 10.0.50.97 | local | 1 GbE | Netgear S3300-52X-PoE+ (7) | 13 Aug |
| NanoPi M5 01 | ✅ | 10.0.50.35 | local | 1 GbE | Netgear S3300-52X-PoE+ (5) | 13 Aug |
| NanoPi M6 01 | ❌ | 10.0.50.18 | local | 1 GbE | Netgear S3300-52X-PoE+ (39) | 25 Jun |
| NanoPi M6 03 | ✅ | 10.0.50.165 | local | 1 GbE | — | 13 Aug |
| NanoPi Neo 2 Black 01 | ✅ | 10.0.50.14 | local | 1 GbE | — | 13 Aug |
| NanoPi Neo 3 01 | ✅ | 10.0.50.20 | local | 1 GbE | TP-Link TL-SG3428X (17) | 13 Aug |
| NanoPi R1 01 | ✅ | 10.0.50.59 | local | 1 GbE | Netgear GS348 (14) | 13 Aug |
| Nanopi R2S 01 | ✅ | 10.0.50.65 | local | 1 GbE | Netgear S3300-52X-PoE+ (12) | 13 Aug |
| NanoPi R6S 01 | ✅ | 10.0.50.40 | local | 1 GbE | Netgear S3300-52X-PoE+ (44) | 13 Aug |
| NanoPi R76S 01 | ✅ | 10.0.50.77 | local | 2.5 GbE | Netgear XS508M (7) | 13 Aug |
| Odroid C1 01 | ✅ | 10.0.50.27 | local | 1 GbE | Netgear GS348 (28) | 12 Aug |
| Odroid C2 01 | ✅ | 10.0.50.87 | local | 1 GbE | Netgear GS348 (7) | 13 Aug |
| Odroid C4 01 | ✅ | 10.0.50.26 | local | 1 GbE | TP-Link TL-SG3428X (10) | 13 Aug |
| Odroid M1 01 | ✅ | 10.0.50.50 | local | 1 GbE | Netgear S3300-52X-PoE+ (38) | 13 Aug |
| Odroid N2 01 | ✅ | 10.0.60.10 | local | 1 GbE | Netgear S3300-52X-PoE+ (14) | 13 Aug |
| Odroid XU4 01 | ✅ | 10.0.50.51 | local | 1 GbE | Netgear S3300-52X-PoE+ (19) | 13 Aug |
| Orange Pi 3 01 | ✅ | 10.0.50.57 | local | 1 GbE | Netgear S3300-52X-PoE+ (31) | 13 Aug |
| Orange Pi 5 01 | ✅ | 10.0.50.39 | local | 1 GbE | TP-Link SG3218XP-M2 (5) | 13 Aug |
| Orange Pi 5 Plus 01 | ✅ | 10.0.50.33 | local | 1 GbE | Netgear S3300-52X-PoE+ (8) | 13 Aug |
| Orange Pi Lite 2 01 | ❌ | 10.0.20.125 | local | Wi-Fi 5 | Zyxel NWA130BE | 01 Jul |
| Orange Pi One+ 01 | ✅ | 10.0.50.37 | local | 1 GbE | TP-Link TL-SG3428X (18) | 13 Aug |
| Orange Pi PC2 01 | ✅ | 10.0.50.68 | local | 1 GbE | TP-Link TL-SG3428X (22) | 13 Aug |
| Orange Pi Prime 01 | ✅ | 10.0.50.16 | local | 1 GbE | Netgear S3300-52X-PoE+ (23) | 13 Aug |
| Orange Pi R1 01 | ✅ | 10.0.50.25 | local | Wi-Fi 4 | Zyxel NWA130BE | 13 Aug |
| Orange Pi Win 01 | ✅ | 10.0.50.24 | local | 1 GbE | Netgear S3300-52X-PoE+ (13) | 13 Aug |
| Orange Pi Zero 02 | ✅ | 10.0.50.46 | local | Wi-Fi 4 | Zyxel NWA130BE | 13 Aug |
| Orange Pi Zero Plus 01 | ❌ | 10.0.50.54 | local | 1 GbE | TP-Link TL-SG3428X (20) | 11 Aug |
| Orange Pi Zero2 01 | ✅ | 10.0.50.74 | local | 1 GbE | Netgear S3300-52X-PoE+ (45) | 13 Aug |
| OrangePi 3 LTS 01 | ✅ | 10.0.50.60 | local | 1 GbE | TP-Link TL-SG3428X (19) | 13 Aug |
| Pine H64 01 | ❌ | 10.0.50.34 | local | 1 GbE | TP-Link TL-SG3428X (9) | 11 Aug |
| Radxa ZERO 3 01 | ✅ | 10.0.20.185 | local | Wi-Fi 6 | Zyxel NWA130BE | 13 Aug |
| Raspberry Pi 01 | ✅ | 10.0.50.15 | local | 1 GbE | Netgear S3300-52X-PoE+ (1) | 13 Aug |
| Raspberry Pi 02 | ✅ | 10.0.50.22 | local | 100 MbE | Netgear GS348 (21) | 13 Aug |
| ROCK 2F 01 | ✅ | 10.0.20.164 | local | Wi-Fi 6 | Zyxel NWA130BE | 13 Aug |
| Rock 5B 01 | ✅ | 10.0.50.69 | local | 2.5 GbE | Netgear XS508M (6) | 13 Aug |
| Rock 5B 02 | ✅ | 10.0.50.17 | local | 2.5 GbE | Netgear XS508M (5) | 13 Aug |
| Rock 5B Plus 01 | ✅ | 10.0.50.41 | local | 2.5 GbE | Netgear XS508M (4) | 13 Aug |
| Rock 5T 01 | ✅ | 10.0.50.66 | local | 2.5 GbE | TP-Link SG3218XP-M2 (12) | 13 Aug |
| Rockpi 4B+ 01 | ❌ | 10.0.50.64 | local | Wi-Fi 5 | Zyxel NWA130BE | 10 Aug |
| Rockpi E 01 | ✅ | 10.0.50.61 | local | 1 GbE | TP-Link TL-SG3428X (16) | 13 Aug |
| SpacemiT K3 Pico-ITX 01 | ✅ | 10.0.50.44 | local | 1 GbE | Netgear S3300-52X-PoE+ (52) | 13 Aug |
| Tanix TX6 01 | ✅ | 10.0.50.21 | local | 100 MbE | Netgear GS348 (46) | 13 Aug |
| Tinker Board 01 | ✅ | 10.0.50.29 | local | 100 MbE | Netgear S3300-52X-PoE+ (15) | 13 Aug |
| Tinker Board 2 01 | ❌ | 10.0.50.23 | local | 1 GbE | TP-Link TL-SG3428X (15) | 09 Aug |
| Udoo 01 | ✅ | 10.0.50.13 | local | 1 GbE | Netgear S3300-52X-PoE+ (37) | 13 Aug |
| UEFI arm64 01 | ✅ | 10.0.50.45 | local | 10 GbE | Netgear XS712T (6) | 13 Aug |
| UEFI x86 01 | ✅ | 10.0.50.53 | local | 1 GbE | Netgear S3300-52X-PoE+ (2) | 13 Aug |
| Z28 PRO 01 | ❌ | 10.0.50.73 | local | 1 GbE | Netgear S3300-52X-PoE+ (17) | 10 Aug |

<!-- BOARDS-STOP -->
