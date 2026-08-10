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

**73** boards (16 failed).

| Board | Status | IP address | Boot | Link | Switch | Last seen |
|:--|:--:|:--|:--|--:|:--|--:|
| Arduino UNO Q 01 | ✅ | 10.0.20.131 | local | Wi-Fi 5 | Zyxel NWA130BE | 10 Aug |
| Banana Pi CM4IO 01 | ✅ | 10.0.50.10 | local | 1 GbE | Netgear S3300-52X-PoE+ (43) | 10 Aug |
| Banana Pi M2 Ultra 01 | ✅ | 10.0.50.47 | local | 1 GbE | TP-Link TL-SG3428X (13) | 10 Aug |
| Banana Pi M2Pro 01 | ✅ | 10.0.50.43 | local | 1 GbE | Netgear S3300-52X-PoE+ (47) | 10 Aug |
| Banana Pi M5 01 | ✅ | 10.0.50.55 | local | 1 GbE | Netgear GS348 (19) | 10 Aug |
| Banana Pi Pro 01 | ✅ | 10.0.50.52 | local | 100 MbE | Netgear GS348 (8) | 10 Aug |
| BananaPi BPI-F3 01 | ✅ | 10.0.50.70 | local | 1 GbE | Netgear S3300-52X-PoE+ (46) | 10 Aug |
| BigTreeTech CB1 01 | ❌ | 10.0.50.72 | local | 100 MbE | Netgear S3300-52X-PoE+ (29) | 10 Aug |
| Clearfog Pro 01 | ✅ | 10.0.50.42 | local | 1 GbE | TP-Link TL-SG3428X (12) | 10 Aug |
| Cubietruck 01 | ✅ | 10.0.50.49 | local | 1 GbE | TP-Link TL-SG3428X (14) | 10 Aug |
| Cubox i2eX/i4 01 | ✅ | 10.0.50.63 | local | 1 GbE | Netgear GS348 (32) | 10 Aug |
| Espressobin 01 | ✅ | 10.0.50.56 | local | 1 GbE | TP-Link TL-SG3428X (11) | 10 Aug |
| Helios4 01 | ✅ | 10.0.50.58 | local | 1 GbE | Netgear GS348 (11) | 10 Aug |
| Inovato Quadra 01 | ❌ | 10.0.50.36 | local | 100 MbE | Netgear GS348 (17) | 09 Aug |
| Khadas VIM1 01 | ❌ | 10.0.50.71 | local | 100 MbE | Netgear GS348 (3) | 05 Aug |
| Khadas VIM2 01 | ❌ | 10.0.50.12 | local | 1 GbE | Netgear GS348 (13) | 09 Aug |
| Khadas VIM3 01 | ✅ | 10.0.50.38 | local | 1 GbE | Netgear GS348 (36) | 10 Aug |
| Le potato 01 | ❌ | 10.0.50.37 | local | 100 MbE | Netgear GS348 (12) | 03 Jul |
| Mekotronics R58S2 01 | ✅ | 10.0.50.19 | local | 1 GbE | Netgear GS348 (48) | 10 Aug |
| NanoPC T6 LTS 01 | ❌ | 10.0.50.30 | local | 2.5 GbE | TP-Link SG3218XP-M2 (8) | 10 Aug |
| NanoPi Duo 01 | ✅ | 10.0.50.48 | local | 100 MbE | Netgear GS348 (31) | 10 Aug |
| NanoPi K2 01 | ✅ | 10.0.50.76 | local | 1 GbE | Netgear GS348 (20) | 10 Aug |
| NanoPi M4V2 01 | ✅ | 10.0.50.97 | local | 1 GbE | Netgear S3300-52X-PoE+ (7) | 10 Aug |
| NanoPi M5 01 | ✅ | 10.0.50.35 | local | 1 GbE | Netgear S3300-52X-PoE+ (5) | 10 Aug |
| NanoPi M6 01 | ❌ | 10.0.50.18 | local | 1 GbE | Netgear S3300-52X-PoE+ (39) | 25 Jun |
| NanoPi Neo 2 Black 01 | ✅ | 10.0.50.14 | local | 1 GbE | — | 10 Aug |
| NanoPi Neo 3 01 | ✅ | 10.0.50.20 | local | 1 GbE | TP-Link TL-SG3428X (17) | 10 Aug |
| NanoPi R1 01 | ✅ | 10.0.50.59 | local | 1 GbE | Netgear GS348 (14) | 10 Aug |
| Nanopi R2S 01 | ✅ | 10.0.50.65 | local | 1 GbE | Netgear S3300-52X-PoE+ (12) | 10 Aug |
| NanoPi R6S 01 | ✅ | 10.0.50.40 | local | 1 GbE | Netgear S3300-52X-PoE+ (44) | 10 Aug |
| NanoPi R76S 01 | ✅ | 10.0.50.67 | local | 2.5 GbE | Netgear XS508M (7) | 10 Aug |
| Odroid C1 01 | ✅ | 10.0.50.27 | local | 1 GbE | Netgear GS348 (28) | 10 Aug |
| Odroid C2 01 | ✅ | 10.0.50.87 | local | 1 GbE | Netgear GS348 (7) | 10 Aug |
| Odroid C4 01 | ❌ | 10.0.50.13 | local | 1 GbE | TP-Link TL-SG3428X (10) | 08 Aug |
| Odroid C4 02 | ✅ | 10.0.50.26 | local | Wi-Fi 4 | Zyxel NWA130BE | 10 Aug |
| Odroid M1 01 | ✅ | 10.0.50.50 | local | 1 GbE | Netgear S3300-52X-PoE+ (3) | 10 Aug |
| Odroid N2 02 | ✅ | 10.0.50.66 | local | 1 GbE | TP-Link TL-SG3428X (21) | 10 Aug |
| Odroid N2 03 | ✅ | 10.0.60.10 | local | 1 GbE | — | 10 Aug |
| Odroid XU4 01 | ✅ | 10.0.50.51 | local | 1 GbE | Netgear S3300-52X-PoE+ (19) | 10 Aug |
| Orange Pi 3 01 | ✅ | 10.0.50.57 | local | 1 GbE | Netgear S3300-52X-PoE+ (31) | 10 Aug |
| Orange Pi 5 01 | ✅ | 10.0.50.39 | local | 1 GbE | TP-Link SG3218XP-M2 (5) | 10 Aug |
| Orange Pi 5 Plus 01 | ✅ | 10.0.50.33 | local | 1 GbE | Netgear S3300-52X-PoE+ (8) | 10 Aug |
| Orange Pi Lite 2 01 | ❌ | 10.0.20.125 | local | Wi-Fi 5 | Zyxel NWA130BE | 01 Jul |
| Orange Pi One+ 01 | ✅ | 10.0.50.125 | local | 1 GbE | TP-Link TL-SG3428X (18) | 10 Aug |
| Orange Pi PC + 01 | ❌ | 10.0.50.32 | local | 100 MbE | Netgear GS348 (47) | 04 Jul |
| Orange Pi PC2 01 | ✅ | 10.0.50.68 | local | 1 GbE | TP-Link TL-SG3428X (22) | 10 Aug |
| Orange Pi Prime 01 | ✅ | 10.0.50.16 | local | 1 GbE | Netgear S3300-52X-PoE+ (23) | 10 Aug |
| Orange Pi R1 01 | ✅ | 10.0.50.25 | local | Wi-Fi 4 | Zyxel NWA130BE | 10 Aug |
| Orange Pi Win 01 | ✅ | 10.0.50.24 | local | 1 GbE | Netgear S3300-52X-PoE+ (13) | 10 Aug |
| Orange Pi Zero 02 | ✅ | 10.0.50.46 | local | Wi-Fi 4 | Zyxel NWA130BE | 10 Aug |
| Orange Pi Zero Plus 01 | ❌ | 10.0.50.54 | local | 1 GbE | TP-Link TL-SG3428X (20) | 09 Aug |
| Orange Pi Zero2 01 | ✅ | 10.0.50.74 | local | 1 GbE | Netgear S3300-52X-PoE+ (45) | 10 Aug |
| OrangePi 3 LTS 01 | ✅ | 10.0.50.60 | local | 1 GbE | TP-Link TL-SG3428X (19) | 10 Aug |
| Pine H64 01 | ✅ | 10.0.50.34 | local | 1 GbE | TP-Link TL-SG3428X (9) | 10 Aug |
| Radxa ZERO 3 01 | ✅ | 10.0.20.185 | local | Wi-Fi 6 | Zyxel NWA130BE | 10 Aug |
| Raspberry Pi 01 | ✅ | 10.0.50.15 | local | 1 GbE | Netgear GS348 (1) | 10 Aug |
| Raspberry Pi 02 | ✅ | 10.0.50.22 | local | 100 MbE | Netgear GS348 (21) | 10 Aug |
| ROCK 2F 01 | ❌ | 10.0.20.164 | local | Wi-Fi 6 | Zyxel NWA130BE | 06 Jul |
| Rock 5B 01 | ✅ | 10.0.50.69 | local | 2.5 GbE | Netgear XS508M (6) | 10 Aug |
| Rock 5B 02 | ✅ | 10.0.50.17 | local | 2.5 GbE | Netgear XS508M (5) | 10 Aug |
| Rock 5B Plus 01 | ✅ | 10.0.50.41 | local | 2.5 GbE | Netgear XS508M (4) | 10 Aug |
| Rock 5T 01 | ✅ | 10.0.50.11 | local | 2.5 GbE | TP-Link SG3218XP-M2 (12) | 10 Aug |
| Rockpi 4B+ 01 | ✅ | 10.0.50.64 | local | Wi-Fi 5 | Zyxel NWA130BE | 10 Aug |
| Rockpi E 01 | ✅ | 10.0.50.61 | local | 1 GbE | TP-Link TL-SG3428X (16) | 10 Aug |
| SpacemiT K3 Pico-ITX 01 | ✅ | 10.0.50.44 | local | 10 GbE | Netgear S3300-52X-PoE+ (52) | 10 Aug |
| Tanix TX6 01 | ✅ | 10.0.50.21 | local | 100 MbE | Netgear GS348 (46) | 10 Aug |
| Tinker Board 01 | ✅ | 10.0.50.29 | local | 1 GbE | Netgear S3300-52X-PoE+ (15) | 10 Aug |
| Tinker Board 2 01 | ❌ | 10.0.50.23 | local | 1 GbE | TP-Link TL-SG3428X (15) | 09 Aug |
| Udoo 02 | ❌ | 10.0.50.161 | local | Wi-Fi 4 | Zyxel NWA130BE | 08 Aug |
| UEFI arm64 01 | ❌ | 10.0.50.45 | local | 10 GbE | Netgear XS712T (6) | 10 Aug |
| UEFI x86 01 | ✅ | 10.0.50.53 | local | 1 GbE | Netgear GS348 (9) | 10 Aug |
| UEFI x86 02 | ❌ | 10.0.20.110 | local | Wi-Fi 7 | Zyxel NWA130BE | 10 Aug |
| Z28 PRO 01 | ✅ | 10.0.50.73 | local | 1 GbE | Netgear S3300-52X-PoE+ (17) | 10 Aug |

<!-- BOARDS-STOP -->
