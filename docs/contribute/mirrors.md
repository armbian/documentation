---
seo_title: "Armbian mirror system & how to add a mirror"
description: "How the Armbian mirror system works: a redirector routes downloads to the fastest nearby mirror, plus mirror specs and steps to contribute a new server."
comments: true
---
# How the Armbian mirror system works

The [Armbian mirror system](https://github.com/armbian/armbian-router) distributes files efficiently, routing each user to the best available server by geographic proximity and server health. This page explains how it works, what a mirror needs to provide, and how to contribute one.

![armbian-mirror-explication](../images/armbian-mirror-explication.png)

## How it works

1. **Request** — a user starts a download (image, package, ...) from a standard URL such as `https://dl.armbian.com`.
2. **Routing** — the redirector picks the best mirror based on the user's location, each mirror's status and load, and whether it holds the requested file.
3. **Redirect** — the user is sent straight to the chosen mirror.
4. **Download** — the file is served directly from that mirror, keeping downloads fast and taking load off the core infrastructure.

The result is **load balancing** across many servers, **faster downloads** from a nearby mirror, and **redundancy** — if a mirror is unavailable, the redirector automatically routes around it.

## Contribute a mirror

If you can host a mirror for the project, here is how.

### 1. Set up an HTTP(S) host

The mirror must be reachable over HTTPS (plain HTTP is also accepted). Point a hostname at it before you start syncing.

### 2. Sync with `rsync`

Pull the content you want to serve from one of the official modules, and run it from cron every **2-4 hours**:

| Content | Command | Required space |
|---------|---------|---------------:|
| Current images | `rsync -av rsync://rsync.armbian.com/dl` | 556G |
| Packages | `rsync -av rsync://rsync.armbian.com/apt` | 84G |
| Archived images | `rsync -av rsync://rsync.armbian.com/archive` | 1.9T |
| Very old images | `rsync -av rsync://rsync.armbian.com/oldarchive` | 5.4T |

### 3. Tell us about it

Once the server is running, reach out through the [contact form](https://www.armbian.com/contact/) so we can add it to the official redirector.

Thanks for helping keep Armbian's downloads fast and reliable worldwide.


## Current Mirrors

| Site | Time Zone | Flag | Speed  | Packages | Images | Archive | Rsync |
|:-----|:----------|------|-------:|:--------:|:------:|:-------:|:-----:|
| [Atomo&nbsp;Networks](https://armbian.atomonetworks.com) | Europe/Rome | [![Italy](https://flagsapi.com/IT/shiny/32.png)](https://www.openstreetmap.org/search?lat=38.157745&lon=13.195175) | 2500&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Auroradev&nbsp;Chicago](https://armbian.chi.auroradev.org) | America/Chicago | [![United States](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=41.881832&lon=-87.623177) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Auroradev&nbsp;Las&nbsp;Vegas](https://armbian.lv.auroradev.org) | America/Los_Angeles | [![United States](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=36.18811&lon=-115.176468) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Nardol](https://armbian.nardol.ovh) | Europe/Paris | [![France](https://flagsapi.com/FR/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.8582&lon=2.3387) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Systemonachip](https://armbian.systemonachip.net) | Europe/Vienna | [![Austria](https://flagsapi.com/AT/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.3003&lon=16.3441) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [SBC&nbsp;mirror&nbsp;Australia](https://au.sbcmirror.org) | Australia/Sydney | [![Australia](https://flagsapi.com/AU/shiny/32.png)](https://www.openstreetmap.org/search?lat=-33.8715&lon=151.2006) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Distrohub](https://distrohub.kyiv.ua) | Europe/Kiev | [![Ukraine](https://flagsapi.com/UA/shiny/32.png)](https://www.openstreetmap.org/search?lat=50.458&lon=30.5303) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  | :white_check_mark: |
| [SBC&nbsp;mirror&nbsp;Spain](https://es.sbcmirror.org) | Europe/Madrid | [![Spain](https://flagsapi.com/ES/shiny/32.png)](https://www.openstreetmap.org/search?lat=40.4163&lon=-3.6934) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Hetzner&nbsp;Germany](https://fi.mirror.armbian.de) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=51.2993&lon=9.491) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Imola](https://imola.armbian.com) | Europe/Ljubljana | [![Slovenia](https://flagsapi.com/SI/shiny/32.png)](https://www.openstreetmap.org/search?lat=46.081638&lon=14.526054) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Kspace&nbsp;Estonia](https://k-space.ee.armbian.com) | Europe/Tallinn | [![Estonia](https://flagsapi.com/EE/shiny/32.png)](https://www.openstreetmap.org/search?lat=59.397987&lon=24.661898) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Albony](https://mirror.albony.in) | Asia/Kolkata | ![Cloudflare anycast](https://flagcdn.com/32x24/un.png) | 1000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Macarne&nbsp;LLC](https://mirror.ams.macarne.com/armbian) | Europe/Amsterdam | [![Netherlands](https://flagsapi.com/NL/shiny/32.png)](https://www.openstreetmap.org/search?lat=52.3785&lon=4.9) | 50000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [OSS&nbsp;Planet&nbsp;Finland](https://mirror.eu.ossplanet.net) | Europe/Helsinki | [![Taiwan](https://flagsapi.com/TW/shiny/32.png)](https://www.openstreetmap.org/search?lat=60.1699&lon=24.9384) | 10000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Hostiko](https://mirror.hostiko.network) | Europe/Kiev | [![Ukraine](https://flagsapi.com/UA/shiny/32.png)](https://www.openstreetmap.org/search?lat=50.4547&lon=30.5238) | 20000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [ISCAS](https://mirror.iscas.ac.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [OSS&nbsp;Planet&nbsp;Taipei](https://mirror.ossplanet.net) | Asia/Taipei | [![Taiwan](https://flagsapi.com/TW/shiny/32.png)](https://www.openstreetmap.org/search?lat=24.0&lon=121.0) | 1000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [SJTU](https://mirror.sjtu.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Digital&nbsp;Streaming&nbsp;Co.](https://mirror.twds.com.tw) | Asia/Taipei | [![Taiwan](https://flagsapi.com/TW/shiny/32.png)](https://www.openstreetmap.org/search?lat=25.0382&lon=121.5636) | 50000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [VineHost.NET](https://mirror.vinehost.net/armbian) | Europe/London | [![United Kingdom](https://flagsapi.com/GB/shiny/32.png)](https://www.openstreetmap.org/search?lat=54.1448&lon=-0.1555) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Yandex](https://mirror.yandex.ru/mirrors/armbian) | Europe/Moscow | [![Russia](https://flagsapi.com/RU/shiny/32.png)](https://www.openstreetmap.org/search?lat=55.7483&lon=37.6171) | 10000&nbsp;Mbps |  | :white_check_mark: | :white_check_mark: |  |
| [marcusn.net](https://mirror2.marcusn.net/armbian) | Europe/London | [![United Kingdom](https://flagsapi.com/GB/shiny/32.png)](https://www.openstreetmap.org/search?lat=51.5085&lon=-0.1257) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Alibaba&nbsp;Mirrors](https://mirrors.aliyun.com) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [BFSU](https://mirrors.bfsu.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.911&lon=116.395) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [c0urier.net](https://mirrors.c0urier.net) | Europe/Copenhagen | [![Denmark](https://flagsapi.com/DK/shiny/32.png)](https://www.openstreetmap.org/search?lat=56.0656&lon=12.2851) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [CSTCloud](https://mirrors.cstcloud.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [dotsrc.org](https://mirrors.dotsrc.org) | Europe/Copenhagen | [![Denmark](https://flagsapi.com/DK/shiny/32.png)](https://www.openstreetmap.org/search?lat=55.6802&lon=12.5892) | 20000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Jevin&nbsp;Canders&nbsp;LLC](https://mirrors.jevincanders.net) | America/New_York | [![United States](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=42.8868&lon=-78.8787) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Lahansons](https://mirrors.lahansons.com) | America/Los_Angeles | [![United States](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=37.7757&lon=-122.3952) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Nanjing&nbsp;University](https://mirrors.nju.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Qilu&nbsp;University&nbsp;of&nbsp;Technology](https://mirrors.qlu.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | 20000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Shandong&nbsp;University](https://mirrors.sdu.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=32.0617&lon=118.778) | 10000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Shanghai&nbsp;Tech&nbsp;University](https://mirrors.shanghaitech.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [SUSTech](https://mirrors.sustech.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=22.2767&lon=113.5788) | 10000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Tsinghua&nbsp;University](https://mirrors.tuna.tsinghua.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [USTC](https://mirrors.ustc.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Zhejiang&nbsp;University](https://mirrors.zju.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | 500&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Netcup&nbsp;Germany](https://netcup-01.armbian.com) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | 2500&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Netcup&nbsp;Germany](https://netcup-02.armbian.com) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | 2500&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Netcup&nbsp;Germany](https://netcup-03.armbian.com) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | 2500&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [SBC&nbsp;mirror&nbsp;Poland](https://pl.sbcmirror.org) | Europe/Warsaw | [![Poland](https://flagsapi.com/PL/shiny/32.png)](https://www.openstreetmap.org/search?lat=52.2297&lon=21.0122) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [SBC&nbsp;mirror&nbsp;Sweden](https://se.sbcmirror.org) | Europe/Stockholm | [![Sweden](https://flagsapi.com/SE/shiny/32.png)](https://www.openstreetmap.org/search?lat=59.3293&lon=18.0686) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [SBC&nbsp;mirror&nbsp;Singapore](https://sg.sbcmirror.org) | Asia/Singapore | [![Singapore](https://flagsapi.com/SG/shiny/32.png)](https://www.openstreetmap.org/search?lat=1.3673&lon=103.8014) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [JetHome](https://stpete-mirror.armbian.com) | Europe/Moscow | [![Russia](https://flagsapi.com/RU/shiny/32.png)](https://www.openstreetmap.org/search?lat=59.9417&lon=30.3096) | 2000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Xogium](https://xogium.performanceservers.nl) | Europe/Paris | [![France](https://flagsapi.com/FR/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.5144&lon=-2.768) | 500&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |

