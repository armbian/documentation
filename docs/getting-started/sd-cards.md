---
title: Choosing an SD card
seo_title: "Choosing an SD card for Armbian"
description: "How to pick a reliable SD card for Armbian: Application Performance Class (A1/A2), what to buy, brands, avoiding counterfeits, and verifying the card with F3 or H2testw."
---
# Choosing an SD card

In over 95% of "Armbian won't boot" or stability reports, the cause is the **SD card** or the **power supply** — not the board and not the image. Armbian cannot run reliably on unreliable storage, so the card you pick matters as much as the board itself.

## Why the card matters

A single-board computer uses the card as its **system disk**: constant small, random reads and writes, not the large sequential transfers a camera makes. The familiar *speed class* (Class 10, U1/U3, V30) only rates **sequential** throughput. What actually matters for an operating system is **random IOPS**, which the SD Association rates separately as the [**Application Performance Class**](https://www.sdcard.org/developers/overview/application/index.html) — A1 and A2.

| Application Performance Class | | Min. random read | Min. random write | Min. sustained sequential write |
|---|---|---|---|---|
| Class 1 (A1) | ![a1-logo](../images/a1-logo.png) | 1500 4K IOPS | 500 4K IOPS | 10 MB/s |
| Class 2 (A2) | ![a2-logo](../images/a2-logo.png) | 4000 4K IOPS | 2000 4K IOPS | 10 MB/s |

## What to buy

Pick a card that is:

- **A1 or A2 rated.** A2 is **not** slower or less supported than A1 on Armbian — where an A2 card's command-queuing feature isn't used it simply behaves like an A1, never worse. Either rating is fine; A2 is the safer target when buying new.
- at least **UHS-I, U3 / V30** — the faster sequential write also speeds up flashing and large writes.
- **32 GB or larger** — small cards wear out sooner, and images plus updates need the room.
- from a **reputable brand.** A1/A2 cards are **not** exclusive to any single manufacturer: Samsung, SanDisk, Lexar, Kingston and others all make suitable A1/A2 cards. Choose a well-reviewed model from a trusted seller.

For **24/7, logging-heavy, or write-heavy** use, a **high-endurance** card (the kind marketed for dashcams and CCTV) lasts far longer than a standard consumer card.

Avoid:

- **SD Express** cards — an SD Express card also carries a legacy SD/UHS-I interface, so it still works in an ordinary reader, but most SBC readers can't use its PCIe/NVMe path, so you gain nothing over a good UHS-I card. Buy one only if your board documents SD Express support.
- **No-name or suspiciously cheap** cards and unfamiliar listings — counterfeits are common (see below).

!!! tip "Further reading"
    The community-maintained [SwitchRoot SD card guide](https://wiki.switchroot.org/wiki/sd-card-guide) has current, brand-by-brand benchmarks and a list of cards to avoid. Its rankings, benchmarks and compatibility notes are measured on the Nintendo Switch (DDR200, hekate) and do not necessarily carry over to Armbian boards or readers — treat them as a starting point, not verdicts for your hardware. Its counterfeit-card advice, however, applies anywhere.

## Check the card before you trust it

Counterfeit and failing cards are the single most common cause of boot and corruption problems. **Verify every new card** — and any card you suspect — with:

- [F3](https://fight-flash-fraud.readthedocs.io/en/stable/) (Linux/macOS), or
- [H2testw](https://www.heise.de/download/product/h2testw-50539) (Windows).

Both fill the card and read it back, so **test an empty card and back up anything on it first** (H2testw's full test needs the card formatted). This detects a [fake](https://www.happybison.com/reviews/how-to-check-and-spot-fake-micro-sd-card-8/) that reports false capacity and surfaces read/write errors — do it **right after purchase** so you can refund a bad card before you rely on it. It cannot guarantee a genuine card won't fail later.

## Reusing an old card

A card that has been used before may have degraded write performance. Before writing Armbian, run the SD Association's [SD Memory Card Formatter](https://www.sdcard.org/downloads/formatter/) — it rewrites the card with the SD-optimized filesystem and alignment it expects, which can help ([background](https://forum.armbian.com/topic/954-sd-card-performance/page/3/&tab=comments#comment-49811)). If the card is still slow or reports errors afterwards, replace it.

Once you have a good card, continue with [writing the image](writing-the-image.md).
