---
comments: true
---
# How the Armbian Mirror System Works  

## Introduction  
The [Armbian mirror system](https://github.com/armbian/armbian-router) is designed to efficiently distribute files, ensuring users get the best available server based on geographic proximity and server availability. This document outlines the mirroring system's operational flow, technical specifications for mirrors, and how to contribute a new server.

![armbian-mirror-explication](images/armbian-mirror-explication.png)

## Operational Flow  

1. **User Request**  
   - A user initiates a file download (system image, package, etc.) from Armbian using a standard URL (e.g., `https://dl.armbian.com`).  

2. **Redirector Server Processing**  
   - The redirector server processes the request and determines the best available mirror based on:  
     - User's geographic location  
     - Mirror server status and load  
     - Availability of the requested files  

3. **Mirror Assignment**  
   - The redirector server provides a direct URL to the most suitable mirror.  
   - The user is automatically redirected to the designated server.  

4. **Download from Assigned Mirror**  
   - The user downloads the file directly from the assigned mirror, optimizing speed and reducing load on the main infrastructure.  

## Benefits of the Mirroring System  
- **Load balancing**: Requests are distributed across multiple servers to prevent congestion.  
- **Faster downloads**: Users are served by the closest available mirror.  
- **Redundancy and reliability**: If a mirror is unavailable, the redirector automatically assigns an alternative.  

## How to Contribute a Mirror  
If you would like to contribute to the Armbian project by providing a mirror, follow these steps:  

### 1. Choose the target and set up an HTTP/HTTPS hostname  
   - The mirror must be accessible via HTTP, and HTTPS is preferred.  

### 2. Set up synchronization via `rsync`  
   - Sync files from one of the official repositories using the following commands:  

   | Content | Command | Required Space |  
   |---------|---------|---------------:|  
   | Current images | `rsync -av rsync://rsync.armbian.com/dl` | 556G |  
   | Packages | `rsync -av rsync://rsync.armbian.com/apt` | 84G |  
   | Archived images | `rsync -av rsync://rsync.armbian.com/archive` | 1.9T |  
   | Very old images | `rsync -av rsync://rsync.armbian.com/oldarchive` | 5.4T |  

   - Set up a cron job to sync every **2-4 hours**.  

### 3. Inform us about your mirror  
   - Once your server is configured, contact us via the [contact form](https://www.armbian.com/contact/) to integrate it into the official redirector system.  

Contributing a mirror helps improve Armbian’s file distribution, ensuring faster and more reliable downloads for the global community.  



## Current Mirrors

| Site | Time Zone | Flag | Speed  | Packages | Images | Archive | Rsync |
|:-----|:----------|------|-------:|:--------:|:------:|:-------:|:-----:|
| [Atomo&nbsp;Networks](https://armbian.atomonetworks.com) | Europe/Rome | [![null](https://flagsapi.com/IT/shiny/32.png)](https://www.openstreetmap.org/search?lat=38.157745&lon=13.195175) | 2500&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Auroradev&nbsp;Chicago](https://armbian.chi.auroradev.org) | America/Chicago | [![East coast](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=41.881832&lon=-87.623177) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Auroradev&nbsp;Las&nbsp;Vegas](https://armbian.lv.auroradev.org) | America/Los_Angeles | [![West coast](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=36.18811&lon=-115.176468) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Nardol](https://armbian.nardol.ovh) | Europe/Paris | [![France](https://flagsapi.com/FR/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.8582&lon=2.3387) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Systemonachip](https://armbian.systemonachip.net) | Europe/Vienna | [![Austria](https://flagsapi.com/AT/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.3003&lon=16.3441) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [TNA&nbsp;Hosting](https://armbian.tnahosting.net) | America/New_York | [![North America](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=42.112&lon=-88.0353) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Naho.moe&nbsp;Australia](https://au.mirrors.naho.moe) | Australia/Sydney | [![Australia](https://flagsapi.com/AU/shiny/32.png)](https://www.openstreetmap.org/search?lat=-33.8678&lon=151.207) | 10000&nbsp;Mbps | :x: | :x: |  |  |
| [SBC&nbsp;mirror&nbsp;Australia](https://au.sbcmirror.org) | Australia/Sydney | [![Australia](https://flagsapi.com/AU/shiny/32.png)](https://www.openstreetmap.org/search?lat=-33.8715&lon=151.2006) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Naho.moe&nbsp;Germany](https://de.mirrors.naho.moe) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4453&lon=11.0222) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [Fast&nbsp;Mirror](https://distrohub.kyiv.ua) | Europe/Kiev | [![Ukraine](https://flagsapi.com/UA/shiny/32.png)](https://www.openstreetmap.org/search?lat=50.458&lon=30.5303) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [SBC&nbsp;mirror&nbsp;Spain](https://es.sbcmirror.org) | Europe/Madrid | [![Spain](https://flagsapi.com/ES/shiny/32.png)](https://www.openstreetmap.org/search?lat=40.4163&lon=-3.6934) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Hetzner&nbsp;Germany](https://fi.mirror.armbian.de) | Europe/Berlin | [![Germany](https://flagsapi.com/FI/shiny/32.png)](https://www.openstreetmap.org/search?lat=51.2993&lon=9.491) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Imola](https://imola.armbian.com) | Europe/Ljubljana | [![Slovenia](https://flagsapi.com/SI/shiny/32.png)](https://www.openstreetmap.org/search?lat=46.081638&lon=14.526054) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Naho.noe&nbsp;India](https://in.mirrors.naho.moe) | Asia/Kolkata | [![India](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=19.0728&lon=72.8826) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [Naho.moe&nbsp;Japan](https://jp.mirrors.naho.moe) | Asia/Tokyo | [![Japan](https://flagsapi.com/JP/shiny/32.png)](https://www.openstreetmap.org/search?lat=35.6895&lon=139.6923) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Naho.moe&nbsp;Korea](https://kr.mirrors.naho.moe) | Asia/Seoul | [![Korea](https://flagsapi.com/KR/shiny/32.png)](https://www.openstreetmap.org/search?lat=37.499177&lon=126.922828) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Kspace&nbsp;Estonia](https://k-space.ee.armbian.com) | Europe/Tallinn | [![Estonia](https://flagsapi.com/EE/shiny/32.png)](https://www.openstreetmap.org/search?lat=59.397987&lon=24.661898) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [AARNet](https://mirror.aarnet.edu.au) | Australia/Sydney | [![Australia](https://flagsapi.com/AU/shiny/32.png)](https://www.openstreetmap.org/search?lat=null&lon=null) | 100000&nbsp;Mbps |  |  |  |  |
| [Albony](https://mirror.albony.in) | Asia/Kolkata | [![Dynamic](https://flagsapi.com/IN/shiny/32.png)](https://www.openstreetmap.org/search?lat=null&lon=null) | 1000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Macarne&nbsp;LLC](https://mirror.ams.macarne.com/armbian) | Europe/Amsterdam | [![Netherlands](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=52.3785&lon=4.9) | 50000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [SteeMan](https://mirror.dogmantech.com) | America/Chicago | [![Virginia](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=42.9633&lon=-85.6679) | 1000&nbsp;Mbps | :x: |  |  |  |
| [Airframes&nbsp;Europe](https://mirror-eu-de1.armbian.airframes.io) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.405&lon=11.1617) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [Hostiko](https://mirror.hostiko.network) | Europe/Kiev | [![Ukraine](https://flagsapi.com/UA/shiny/32.png)](https://www.openstreetmap.org/search?lat=50.4547&lon=30.5238) | 20000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [ISCAS](https://mirror.iscas.ac.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.9075&lon=116.3971) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [OSS&nbsp;Planet](https://mirror.ossplanet.net) | Asia/Taipei | [![Taiwan](https://flagsapi.com/TW/shiny/32.png)](https://www.openstreetmap.org/search?lat=24.0&lon=121.0) | 1000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Alibaba&nbsp;Mirrors](https://mirrors.aliyun.com) | Asia/Shanghai | [![China](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [BFSU](https://mirrors.bfsu.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=39.911&lon=116.395) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [c0urier.net](https://mirrors.c0urier.net) | Europe/Copenhagen | [![Denmark](https://flagsapi.com/DK/shiny/32.png)](https://www.openstreetmap.org/search?lat=56.0656&lon=12.2851) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [dotsrc.org](https://mirrors.dotsrc.org) | Europe/Copenhagen | [![Denmark](https://flagsapi.com/DK/shiny/32.png)](https://www.openstreetmap.org/search?lat=55.6802&lon=12.5892) | 20000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Jevin&nbsp;Canders&nbsp;LLC](https://mirrors.jevincanders.net) | America/New_York | [![East coast](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=42.8868&lon=-78.8787) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [SJTU](https://mirror.sjtu.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :x: |  |  |  |
| [Lahansons](https://mirrors.lahansons.com) | America/Los_Angeles | [![North America](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=37.7757&lon=-122.3952) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Nanjing&nbsp;University](https://mirrors.nju.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Shandong&nbsp;University](https://mirrors.sdu.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=32.0617&lon=118.778) | 10000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Shanghai&nbsp;Tech&nbsp;University](https://mirrors.shanghaitech.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [SUSTech](https://mirrors.sustech.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=22.2767&lon=113.5788) | 10000&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Tsinghua&nbsp;University](https://mirrors.tuna.tsinghua.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [USTC](https://mirrors.ustc.edu.cn) | Asia/Shanghai | [![China](https://flagsapi.com/CN/shiny/32.png)](https://www.openstreetmap.org/search?lat=34.7732&lon=113.722) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Digital&nbsp;Streaming&nbsp;Co.](https://mirror.twds.com.tw) | Asia/Taipei | [![Taiwan](https://flagsapi.com/TW/shiny/32.png)](https://www.openstreetmap.org/search?lat=25.0382&lon=121.5636) | 50000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Airframes&nbsp;Phoenix](https://mirror-us-phx1.armbian.airframes.io) | America/Phoenix | [![West coast](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=33.4413&lon=-112.0421) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [Airframes&nbsp;Seattle](https://mirror-us-sea1.armbian.airframes.io) | America/Los_Angeles | [![West coast](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=47.6034&lon=-122.3414) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [Airframes&nbsp;Seattle](https://mirror-us-sea2.armbian.airframes.io) | America/Los_Angeles | [![West coast](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=47.6034&lon=-122.3414) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [Airframes&nbsp;St&nbsp;Louis](https://mirror-us-stl1.armbian.airframes.io) | America/Chicago | [![East coast](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=38.6287&lon=-90.1988) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [VineHost.NET](https://mirror.vinehost.net/armbian) | Europe/London | [![United Kingdom](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=54.1448&lon=-0.1555) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Yandex](https://mirror.yandex.ru/mirrors/armbian) | Europe/Moscow | [![Russia](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=55.7483&lon=37.6171) | 10000&nbsp;Mbps |  | :white_check_mark: | :white_check_mark: |  |
| [Netcup&nbsp;Germany](https://netcup-01.armbian.com) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | 2500&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Netcup&nbsp;Germany](https://netcup-02.armbian.com) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | 2500&nbsp;Mbps | :white_check_mark: |  |  |  |
| [Netcup&nbsp;Germany](https://netcup-03.armbian.com) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | 2500&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Netcup&nbsp;Germany](https://repo.armbian.com) | Europe/Berlin | [![Germany](https://flagsapi.com/DE/shiny/32.png)](https://www.openstreetmap.org/search?lat=49.4478&lon=11.0683) | 2500&nbsp;Mbps |  |  |  |  |
| [Jing&nbsp;Rocks](https://repo.jing.rocks) | Asia/Tokyo | [![Japan](https://flagsapi.com/JP/shiny/32.png)](https://www.openstreetmap.org/search?lat=35.652832&lon=139.839478) | 10000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [Naho.moe&nbsp;Singapore](https://sg.mirrors.naho.moe) | Asia/Singapore | [![Singapore](https://flagsapi.com/SG/shiny/32.png)](https://www.openstreetmap.org/search?lat=1.29&lon=103.8551) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [SBC&nbsp;mirror&nbsp;Singapore](https://sg.sbcmirror.org) | Asia/Singapore | [![Singapore](https://flagsapi.com/SG/shiny/32.png)](https://www.openstreetmap.org/search?lat=1.3673&lon=103.8014) | 1000&nbsp;Mbps | :white_check_mark: | :white_check_mark: |  |  |
| [JetHome](https://stpete-mirror.armbian.com) | Europe/Moscow | [![Russia](https://flagsapi.com/RU/shiny/32.png)](https://www.openstreetmap.org/search?lat=59.9417&lon=30.3096) | 2000&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
| [Naho.moe&nbsp;UK](https://uk.mirrors.naho.moe) | Europe/London | [![United Kingdom](https://flagsapi.com/GB/shiny/32.png)](https://www.openstreetmap.org/search?lat=51.5085&lon=-0.1257) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [Naho.noe&nbsp;USA&nbsp;west](https://wa.mirrors.naho.moe) | America/New_York | [![North America](https://flagsapi.com/US/shiny/32.png)](https://www.openstreetmap.org/search?lat=47.6062&lon=-122.3321) | 1000&nbsp;Mbps | :x: | :x: |  |  |
| [Xogium](https://xogium.performanceservers.nl) | Europe/Paris | [![France](https://flagsapi.com/NL/shiny/32.png)](https://www.openstreetmap.org/search?lat=48.5144&lon=-2.768) | 500&nbsp;Mbps | :white_check_mark: | :white_check_mark: | :white_check_mark: |  |
