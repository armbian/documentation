---
title: Mirrors
seo_title: "Armbian mirrors: the mirror network & redirector"
description: "The Armbian mirror network: a redirector routes each download to the fastest nearby mirror. See every active mirror and how the system works."
comments: true
---
# Mirrors

The [Armbian mirror system](https://github.com/armbian/armbian-router) distributes files efficiently, routing each user to the best available server by geographic proximity and server health. Pick a nearby mirror from the list below, or read on for how the system works. Want to host a mirror? See [**Run a mirror**](/contribute/run-a-mirror/).

<!-- mirrors:start -->
## Current Mirrors

| Site | Flag | Packages | Images | Archive | Rsync |
|:-----|------|:--------:|:------:|:-------:|:-----:|
| [Atomo Networks](https://armbian.atomonetworks.com) | [![Italy](https://flagsapi.com/IT/shiny/32.png)](https://www.openstreetmap.org/search?lat=38.157745&lon=13.195175) | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Auroradev Chicago](https://armbian.chi.auroradev.org) | [![United States](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=41.881832&lon=-87.623177) | :white_check_mark: | :white_check_mark: |  |  |
| [Auroradev Las Vegas](https://armbian.lv.auroradev.org) | [![United States](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=36.18811&lon=-115.176468) | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Nardol](https://armbian.nardol.ovh) | [![France](https://flagsapi.com/FR/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.8582&lon=2.3387) | :white_check_mark: | :white_check_mark: |  |  |
| [Systemonachip](https://armbian.systemonachip.net) | [![Austria](https://flagsapi.com/AT/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.3003&lon=16.3441) | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [SBC mirror Australia](https://au.sbcmirror.org) | [![Australia](https://flagsapi.com/AU/shiny/32.png)](https://www.openstreetmap.org/search?lat=-33.8715&lon=151.2006) | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Distrohub](https://distrohub.kyiv.ua) | [![Ukraine](https://flagsapi.com/UA/shiny/32.png)](https://www.openstreetmap.org/search?lat=50.458&lon=30.5303) | :white_check_mark: | :white_check_mark: |  | :white_check_mark: |
| [SBC mirror Spain](https://es.sbcmirror.org) | [![Spain](https://flagsapi.com/ES/shiny/32.png)](https://www.openstreetmap.org/search?lat=40.4163&lon=-3.6934) | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Hetzner Germany](https://fi.mirror.armbian.de) | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=51.2993&lon=9.491) | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Imola](https://imola.armbian.com) | [![Slovenia](https://flagsapi.com/SI/shiny/32.png)](https://www.openstreetmap.org/search?lat=46.081638&lon=14.526054) | :white_check_mark: | :white_check_mark: |  |  |
| [Kspace Estonia](https://k-space.ee.armbian.com) | [![Estonia](https://flagsapi.com/EE/shiny/32.png)](https://www.openstreetmap.org/search?lat=59.397987&lon=24.661898) | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Albony](https://mirror.albony.in) | ![Cloudflare anycast](https://flagcdn.com/32x24/un.png) | :white_check_mark: |  |  |  |
| [Macarne LLC](https://mirror.ams.macarne.com/armbian) | [![Netherlands](https://flagsapi.com/NL/shiny/32.png)](https://www.openstreetmap.org/search?lat=52.3785&lon=4.9) | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [OSS Planet Finland](https://mirror.eu.ossplanet.net) | [![Taiwan](https://flagsapi.com/TW/shiny/32.png)](https://www.openstreetmap.org/search?lat=60.1699&lon=24.9384) | :white_check_mark: |  |  |  |
| [Hostiko](https://mirror.hostiko.network) | [![Ukraine](https://flagsapi.com/UA/shiny/32.png)](https://www.openstreetmap.org/search?lat=50.4547&lon=30.5238) | :white_check_mark: | :white_check_mark: |  |  |
| [ISCAS](https://mirror.iscas.ac.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | :white_check_mark: | :white_check_mark: |  |  |
| [OSS Planet Taipei](https://mirror.ossplanet.net) | [![Taiwan](https://flagsapi.com/TW/shiny/32.png)](https://www.openstreetmap.org/search?lat=24.0&lon=121.0) | :white_check_mark: |  |  |  |
| [SJTU](https://mirror.sjtu.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | :white_check_mark: |  |  |  |
| [Digital Streaming Co.](https://mirror.twds.com.tw) | [![Taiwan](https://flagsapi.com/TW/shiny/32.png)](https://www.openstreetmap.org/search?lat=25.0382&lon=121.5636) | :white_check_mark: | :white_check_mark: |  |  |
| [VineHost.NET](https://mirror.vinehost.net/armbian) | [![United Kingdom](https://flagsapi.com/GB/shiny/32.png)](https://www.openstreetmap.org/search?lat=54.1448&lon=-0.1555) | :white_check_mark: | :white_check_mark: |  |  |
| [Yandex](https://mirror.yandex.ru/mirrors/armbian) | [![Russia](https://flagsapi.com/RU/shiny/32.png)](https://www.openstreetmap.org/search?lat=55.7483&lon=37.6171) |  | :white_check_mark: | :white_check_mark: |  |
| [marcusn.net](https://mirror2.marcusn.net/armbian) | [![United Kingdom](https://flagsapi.com/GB/shiny/32.png)](https://www.openstreetmap.org/search?lat=51.5085&lon=-0.1257) | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Alibaba Mirrors](https://mirrors.aliyun.com) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | :white_check_mark: | :white_check_mark: |  |  |
| [BFSU](https://mirrors.bfsu.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.911&lon=116.395) | :white_check_mark: | :white_check_mark: |  |  |
| [c0urier.net](https://mirrors.c0urier.net) | [![Denmark](https://flagsapi.com/DK/shiny/32.png)](https://www.openstreetmap.org/search?lat=56.0656&lon=12.2851) | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [CSTCloud](https://mirrors.cstcloud.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | :white_check_mark: | :white_check_mark: |  |  |
| [dotsrc.org](https://mirrors.dotsrc.org) | [![Denmark](https://flagsapi.com/DK/shiny/32.png)](https://www.openstreetmap.org/search?lat=55.6802&lon=12.5892) | :white_check_mark: | :white_check_mark: |  |  |
| [Jevin Canders LLC](https://mirrors.jevincanders.net) | [![United States](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=42.8868&lon=-78.8787) | :white_check_mark: | :white_check_mark: |  |  |
| [Lahansons](https://mirrors.lahansons.com) | [![United States](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=37.7757&lon=-122.3952) | :white_check_mark: | :white_check_mark: |  |  |
| [Nanjing University](https://mirrors.nju.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | :white_check_mark: | :white_check_mark: |  |  |
| [Qilu University of Technology](https://mirrors.qlu.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | :white_check_mark: |  |  |  |
| [Shandong University](https://mirrors.sdu.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=32.0617&lon=118.778) | :white_check_mark: |  |  |  |
| [Shanghai Tech University](https://mirrors.shanghaitech.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | :white_check_mark: | :white_check_mark: |  |  |
| [SUSTech](https://mirrors.sustech.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=22.2767&lon=113.5788) | :white_check_mark: |  |  |  |
| [Tsinghua University](https://mirrors.tuna.tsinghua.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | :white_check_mark: | :white_check_mark: |  |  |
| [USTC](https://mirrors.ustc.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | :white_check_mark: | :white_check_mark: |  |  |
| [Zhejiang University](https://mirrors.zju.edu.cn) | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | :white_check_mark: |  |  |  |
| [Netcup Germany](https://netcup-01.armbian.com) | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | :white_check_mark: | :white_check_mark: |  |  |
| [Netcup Germany](https://netcup-02.armbian.com) | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | :white_check_mark: |  |  |  |
| [Netcup Germany](https://netcup-03.armbian.com) | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | :white_check_mark: | :white_check_mark: |  |  |
| [SBC mirror Poland](https://pl.sbcmirror.org) | [![Poland](https://flagsapi.com/PL/shiny/32.png)](https://www.openstreetmap.org/search?lat=52.2297&lon=21.0122) | :white_check_mark: | :white_check_mark: |  |  |
| [SBC mirror Sweden](https://se.sbcmirror.org) | [![Sweden](https://flagsapi.com/SE/shiny/32.png)](https://www.openstreetmap.org/search?lat=59.3293&lon=18.0686) | :white_check_mark: | :white_check_mark: |  |  |
| [SBC mirror Singapore](https://sg.sbcmirror.org) | [![Singapore](https://flagsapi.com/SG/shiny/32.png)](https://www.openstreetmap.org/search?lat=1.3673&lon=103.8014) | :white_check_mark: | :white_check_mark: |  |  |
| [JetHome](https://stpete-mirror.armbian.com) | [![Russia](https://flagsapi.com/RU/shiny/32.png)](https://www.openstreetmap.org/search?lat=59.9417&lon=30.3096) | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Xogium](https://xogium.performanceservers.nl) | [![France](https://flagsapi.com/FR/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.5144&lon=-2.768) | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
<!-- mirrors:end -->

## How it works

![Armbian mirror system](../images/armbian-mirror-system.png)

1. **Request** — a user starts a download (image, package, ...) from a standard URL such as `https://dl.armbian.com`.
2. **Routing** — the redirector picks the best mirror based on the user's location, each mirror's status and load, and whether it holds the requested file.
3. **Redirect** — the user is sent straight to the chosen mirror.
4. **Download** — the file is served directly from that mirror, keeping downloads fast and taking load off the core infrastructure.

The result is **load balancing** across many servers, **faster downloads** from a nearby mirror, and **redundancy** — if a mirror is unavailable, the redirector automatically routes around it.

## Host a mirror

Want to help serve Armbian's downloads? See [**Run a mirror**](/contribute/run-a-mirror/) for the requirements, the `rsync` sync commands and how to register your server.
