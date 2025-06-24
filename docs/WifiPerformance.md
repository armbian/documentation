---
comments: true
---
# Testing the speed of wireless adapters

All wireless adapters were tested under consistent conditions - each positioned in close proximity (1-2m) and connected to the same wireless access point (AP). The adapters utilized various interface types, including USB, SDIO, and PCI, to evaluate performance across different hardware configurations.

<br>
[![Support Autotests](/images/support-autotest.png)](#contribute)

## Test Equipment

- **Access Point**: [Zyxel NWA130BE (Wi-Fi 7)](https://amzn.to/428dvnH)
- **Network Switches**: 
  - Netgear XS712T  
  - Netgear XS508M
- **Power Switches**: APC AP7920  
- **Client Devices**:
  - Multiple single-board computers equipped with onboard wireless modules or PCI Wi-Fi cards
  - USB wireless test server: [Geekom IT13](https://amzn.to/4crUVKP) with an [i-Tec 16-port USB 3.0 hub](https://amzn.to/42B4B29)

## Software and Infrastructure

- **Infrastructure Database**: [NetBox](https://docs.armbian.com/User-Guide_Armbian-Software/Management/#netbox) for resource modeling and inventory
- **Automation**: [GitHub Actions for workflow orchestration and test execution](https://github.com/armbian/armbian.github.io/blob/main/.github/workflows/wireless-performance-autotest.yml)
- **Networking**: [Tailscale](https://tailscale.com) for secure device connectivity across the test environment
- **Test Platform**: KVM virtual machine running the latest x86 Armbian image for USB wireless testing

## Methodology

**Overview of the WiFi performance test process:**

1. ⚡ **Power On Devices**  
   └─ Embedded WiFi-capable devices and USB wireless adapters are powered on.

2. 🌐 **Configure Wireless Connection**  
   └─ Devices are configured to connect to a predefined access point (SSID).

3. 📶 **Connect to WiFi Network**  
   └─ Network connectivity is validated to ensure the device is routable.

4. 📊 **Measure Performance (iperf3)**  
   ├─ Perform reverse (`-R`) and forward iperf3 tests  
   └─ Measure throughput and link quality.

5. 🔍 **Collect System & Network Info**  
   ├─ Extract link details (e.g. bitrate, signal strength)  
   └─ Record system version, kernel, architecture.

6. 🔁 **Restore Wired Network**  
   └─ Reapply original routes and configuration.

7. ☁️ **Upload Test Results**  
   └─ Summary, logs, and system info are uploaded as artifacts.

8. 📴 **Power Off Devices**  
   └─ All test devices are safely powered down after testing completes.

<!-- DUT-START -->

## Devices Under Tests
This section presents the performance test results, including key metrics and technical details from the test execution.  
**Test Date:** [2025-05-28 14:49 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15302170019)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">226</span> Mbits/sec | <span style="font-size: 1.5rem;">264</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 36947 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  24.9 MBytes   209 Mbits/sec                  
    [  5]   1.00-2.00   sec  26.9 MBytes   225 Mbits/sec                  
    [  5]   2.00-3.00   sec  25.1 MBytes   210 Mbits/sec                  
    [  5]   3.00-4.00   sec  28.3 MBytes   237 Mbits/sec                  
    [  5]   4.00-5.00   sec  26.8 MBytes   225 Mbits/sec                  
    [  5]   5.00-6.00   sec  27.2 MBytes   228 Mbits/sec                  
    [  5]   6.00-7.00   sec  26.9 MBytes   226 Mbits/sec                  
    [  5]   7.00-8.00   sec  27.2 MBytes   228 Mbits/sec                  
    [  5]   8.00-9.00   sec  26.9 MBytes   226 Mbits/sec                  
    [  5]   9.00-10.00  sec  26.9 MBytes   226 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   270 MBytes   226 Mbits/sec  773             sender
    [  5]   0.00-10.00  sec   267 MBytes   224 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 54545 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  33.8 MBytes   283 Mbits/sec    0    979 KBytes       
    [  5]   1.00-2.00   sec  30.0 MBytes   252 Mbits/sec    0   1.07 MBytes       
    [  5]   2.00-3.00   sec  31.2 MBytes   262 Mbits/sec    0   1.19 MBytes       
    [  5]   3.00-4.00   sec  31.2 MBytes   262 Mbits/sec    0   1.33 MBytes       
    [  5]   4.00-5.00   sec  31.2 MBytes   262 Mbits/sec    0   1.33 MBytes       
    [  5]   5.00-6.00   sec  31.2 MBytes   262 Mbits/sec    0   1.39 MBytes       
    [  5]   6.00-7.00   sec  32.5 MBytes   273 Mbits/sec    0   1.39 MBytes       
    [  5]   7.00-8.00   sec  31.2 MBytes   262 Mbits/sec    0   1.46 MBytes       
    [  5]   8.00-9.00   sec  31.2 MBytes   262 Mbits/sec    0   1.46 MBytes       
    [  5]   9.00-10.00  sec  31.2 MBytes   262 Mbits/sec    0   1.46 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   315 MBytes   264 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   312 MBytes   262 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 154671 bytes (411 packets)
    TX: 89165 bytes (523 packets)
    signal: -37 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">118</span> Mbits/sec | <span style="font-size: 1.5rem;">107</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 41633 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.3 MBytes   112 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.9 MBytes   117 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.9 MBytes   117 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.8 MBytes   115 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.9 MBytes   109 Mbits/sec                  
    [  5]   6.00-7.00   sec  14.4 MBytes   121 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   8.00-9.00   sec  14.0 MBytes   118 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.8 MBytes   116 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec   141 MBytes   118 Mbits/sec    5             sender
    [  5]   0.00-10.00  sec   137 MBytes   115 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 49285 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.6 MBytes   106 Mbits/sec    0    516 KBytes       
    [  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0    571 KBytes       
    [  5]   2.00-3.00   sec  13.0 MBytes   109 Mbits/sec    0    641 KBytes       
    [  5]   3.00-4.00   sec  12.1 MBytes   101 Mbits/sec    0    641 KBytes       
    [  5]   4.00-5.00   sec  13.5 MBytes   114 Mbits/sec    0    779 KBytes       
    [  5]   5.00-6.00   sec  12.8 MBytes   107 Mbits/sec    0    779 KBytes       
    [  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec    0    779 KBytes       
    [  5]   7.00-8.00   sec  12.5 MBytes   105 Mbits/sec    0    905 KBytes       
    [  5]   8.00-9.00   sec  13.1 MBytes   110 Mbits/sec    0    905 KBytes       
    [  5]   9.00-10.00  sec  12.7 MBytes   106 Mbits/sec    0    905 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   127 MBytes   107 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   125 MBytes   105 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 112340 bytes (497 packets)
    TX: 58510 bytes (236 packets)
    signal: -28 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">95.0</span> Mbits/sec | <span style="font-size: 1.5rem;">53.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.181 port 50439 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.2 MBytes  85.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.8 MBytes  98.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   113 MBytes  95.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   113 MBytes  94.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.181 port 48349 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.38 MBytes  61.8 Mbits/sec    0    311 KBytes       
    [  5]   1.00-2.00   sec  6.75 MBytes  56.6 Mbits/sec    0    587 KBytes       
    [  5]   2.00-3.00   sec  6.50 MBytes  54.5 Mbits/sec    0    716 KBytes       
    [  5]   3.00-4.00   sec  7.38 MBytes  61.9 Mbits/sec    0    754 KBytes       
    [  5]   4.00-5.00   sec  5.50 MBytes  46.1 Mbits/sec    0    754 KBytes       
    [  5]   5.00-6.00   sec  7.00 MBytes  58.7 Mbits/sec    0    792 KBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec    0    843 KBytes       
    [  5]   7.00-8.00   sec  7.00 MBytes  58.7 Mbits/sec    0    843 KBytes       
    [  5]   8.00-9.00   sec  5.62 MBytes  47.2 Mbits/sec    0    885 KBytes       
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec    0    885 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  64.2 MBytes  53.9 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  61.6 MBytes  51.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 188015 bytes (464 packets)
    TX: 100288 bytes (498 packets)
    signal: -40 dBm
    rx bitrate: 130.0 MBit/s MCS 15
    tx bitrate: 144.4 MBit/s MCS 15 short GI
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">198</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.182 port 48835 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  16.8 MBytes   140 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.6 MBytes   148 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   183 MBytes   153 Mbits/sec  134             sender
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.182 port 58527 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.1 MBytes   211 Mbits/sec    0    639 KBytes       
    [  5]   1.00-2.00   sec  23.6 MBytes   198 Mbits/sec    0    711 KBytes       
    [  5]   2.00-3.00   sec  22.6 MBytes   190 Mbits/sec    0    711 KBytes       
    [  5]   3.00-4.00   sec  23.8 MBytes   199 Mbits/sec    0    711 KBytes       
    [  5]   4.00-5.00   sec  23.6 MBytes   198 Mbits/sec    0    711 KBytes       
    [  5]   5.00-6.00   sec  23.5 MBytes   197 Mbits/sec    0    796 KBytes       
    [  5]   6.00-7.00   sec  23.8 MBytes   199 Mbits/sec    0    796 KBytes       
    [  5]   7.00-8.00   sec  22.2 MBytes   187 Mbits/sec    0    796 KBytes       
    [  5]   8.00-9.00   sec  23.9 MBytes   200 Mbits/sec    0    796 KBytes       
    [  5]   9.00-10.00  sec  23.6 MBytes   198 Mbits/sec    0    841 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   236 MBytes   198 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   233 MBytes   195 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -42 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">148</span> Mbits/sec | <span style="font-size: 1.5rem;">269</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.183 port 49865 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   3.00-4.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   5.00-6.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.2 MBytes   145 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.2 MBytes   145 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.8 MBytes   149 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   177 MBytes   148 Mbits/sec    8             sender
    [  5]   0.00-10.00  sec   174 MBytes   146 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.183 port 41219 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.2 MBytes   287 Mbits/sec    0    979 KBytes       
    [  5]   1.00-2.00   sec  31.5 MBytes   264 Mbits/sec    0   1.13 MBytes       
    [  5]   2.00-3.00   sec  33.1 MBytes   278 Mbits/sec    0   1.13 MBytes       
    [  5]   3.00-4.00   sec  31.5 MBytes   264 Mbits/sec    0   1.20 MBytes       
    [  5]   4.00-5.00   sec  31.4 MBytes   263 Mbits/sec    0   1.20 MBytes       
    [  5]   5.00-6.00   sec  31.6 MBytes   266 Mbits/sec    0   1.20 MBytes       
    [  5]   6.00-7.00   sec  32.2 MBytes   270 Mbits/sec    0   1.20 MBytes       
    [  5]   7.00-8.00   sec  32.6 MBytes   274 Mbits/sec    0   1.20 MBytes       
    [  5]   8.00-9.00   sec  30.9 MBytes   259 Mbits/sec    0   1.33 MBytes       
    [  5]   9.00-10.00  sec  32.0 MBytes   268 Mbits/sec    0   1.33 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   321 MBytes   269 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   319 MBytes   267 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -33 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8814AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">23.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.184 port 39333 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   5.00-6.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.0 MBytes   151 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   183 MBytes   153 Mbits/sec  120             sender
    [  5]   0.00-10.00  sec   179 MBytes   150 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.184 port 43963 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.50 MBytes  29.3 Mbits/sec    0    208 KBytes       
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec    0    331 KBytes       
    [  5]   2.00-3.00   sec  2.88 MBytes  24.1 Mbits/sec    0    358 KBytes       
    [  5]   3.00-4.00   sec  2.88 MBytes  24.1 Mbits/sec    0    376 KBytes       
    [  5]   4.00-5.00   sec  3.00 MBytes  25.2 Mbits/sec    0    376 KBytes       
    [  5]   5.00-6.00   sec  2.38 MBytes  19.9 Mbits/sec    0    376 KBytes       
    [  5]   6.00-7.00   sec  3.00 MBytes  25.2 Mbits/sec    0    376 KBytes       
    [  5]   7.00-8.00   sec  2.25 MBytes  18.9 Mbits/sec    0    376 KBytes       
    [  5]   8.00-9.00   sec  3.00 MBytes  25.2 Mbits/sec    0    376 KBytes       
    [  5]   9.00-10.00  sec  2.25 MBytes  18.9 Mbits/sec    0    376 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  28.4 MBytes  23.8 Mbits/sec    0             sender
    [  5]   0.00-10.10  sec  27.2 MBytes  22.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -38 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8821CU #1

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">123</span> Mbits/sec | <span style="font-size: 1.5rem;">211</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.185 port 57159 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.88 MBytes  57.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   4.00-5.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   5.00-6.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   7.00-8.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   8.00-9.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.0 MBytes   134 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   147 MBytes   123 Mbits/sec    2             sender
    [  5]   0.00-10.00  sec   146 MBytes   123 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.185 port 50357 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.8 MBytes   216 Mbits/sec    0    543 KBytes       
    [  5]   1.00-2.00   sec  25.6 MBytes   215 Mbits/sec    0    638 KBytes       
    [  5]   2.00-3.00   sec  26.0 MBytes   218 Mbits/sec    0    741 KBytes       
    [  5]   3.00-4.00   sec  24.8 MBytes   208 Mbits/sec    0    741 KBytes       
    [  5]   4.00-5.00   sec  25.0 MBytes   210 Mbits/sec    0    768 KBytes       
    [  5]   5.00-6.00   sec  24.9 MBytes   209 Mbits/sec    0    776 KBytes       
    [  5]   6.00-7.00   sec  24.9 MBytes   209 Mbits/sec    0    776 KBytes       
    [  5]   7.00-8.00   sec  24.9 MBytes   209 Mbits/sec    0    776 KBytes       
    [  5]   8.00-9.00   sec  24.8 MBytes   208 Mbits/sec    0    776 KBytes       
    [  5]   9.00-10.00  sec  24.8 MBytes   208 Mbits/sec    0    776 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   251 MBytes   211 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   248 MBytes   208 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 194101 bytes (390 packets)
    TX: 99340 bytes (457 packets)
    signal: -41 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">275</span> Mbits/sec | <span style="font-size: 1.5rem;">257</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.163 port 54087 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  27.2 MBytes   228 Mbits/sec                  
    [  5]   1.00-2.00   sec  33.5 MBytes   281 Mbits/sec                  
    [  5]   2.00-3.00   sec  32.8 MBytes   275 Mbits/sec                  
    [  5]   3.00-4.00   sec  33.1 MBytes   278 Mbits/sec                  
    [  5]   4.00-5.00   sec  32.5 MBytes   273 Mbits/sec                  
    [  5]   5.00-6.00   sec  32.9 MBytes   276 Mbits/sec                  
    [  5]   6.00-7.00   sec  33.5 MBytes   281 Mbits/sec                  
    [  5]   7.00-8.00   sec  33.2 MBytes   279 Mbits/sec                  
    [  5]   8.00-9.00   sec  33.1 MBytes   278 Mbits/sec                  
    [  5]   9.00-10.00  sec  33.2 MBytes   279 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   328 MBytes   275 Mbits/sec  130             sender
    [  5]   0.00-10.00  sec   325 MBytes   273 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.163 port 44557 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  33.5 MBytes   281 Mbits/sec    0   1.64 MBytes       
    [  5]   1.00-2.00   sec  30.2 MBytes   254 Mbits/sec    0   1.84 MBytes       
    [  5]   2.00-3.00   sec  29.6 MBytes   249 Mbits/sec    0   2.15 MBytes       
    [  5]   3.00-4.00   sec  31.2 MBytes   262 Mbits/sec    0   2.36 MBytes       
    [  5]   4.00-5.00   sec  30.1 MBytes   253 Mbits/sec    0   2.36 MBytes       
    [  5]   5.00-6.00   sec  30.5 MBytes   256 Mbits/sec    0   2.36 MBytes       
    [  5]   6.00-7.00   sec  30.8 MBytes   258 Mbits/sec    0   2.36 MBytes       
    [  5]   7.00-8.00   sec  30.0 MBytes   252 Mbits/sec    0   2.36 MBytes       
    [  5]   8.00-9.00   sec  29.5 MBytes   247 Mbits/sec    0   2.36 MBytes       
    [  5]   9.00-10.00  sec  30.4 MBytes   255 Mbits/sec    0   2.36 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   306 MBytes   257 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   304 MBytes   254 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### Realtek 8822CE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8822CE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.21-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">476</span> Mbits/sec | <span style="font-size: 1.5rem;">645</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 53729 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  59.9 MBytes   502 Mbits/sec                  
    [  5]   1.00-2.00   sec  59.3 MBytes   497 Mbits/sec                  
    [  5]   2.00-3.00   sec  56.7 MBytes   476 Mbits/sec                  
    [  5]   3.00-4.00   sec  57.1 MBytes   479 Mbits/sec                  
    [  5]   4.00-5.00   sec  58.3 MBytes   489 Mbits/sec                  
    [  5]   5.00-6.00   sec  57.0 MBytes   478 Mbits/sec                  
    [  5]   6.00-7.00   sec  54.5 MBytes   457 Mbits/sec                  
    [  5]   7.00-8.00   sec  54.3 MBytes   456 Mbits/sec                  
    [  5]   8.00-9.00   sec  52.9 MBytes   443 Mbits/sec                  
    [  5]   9.00-10.00  sec  54.5 MBytes   457 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   568 MBytes   476 Mbits/sec  527             sender
    [  5]   0.00-10.00  sec   564 MBytes   474 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 58093 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  77.0 MBytes   645 Mbits/sec    0   7.51 MBytes       
    [  5]   1.00-2.00   sec  77.5 MBytes   650 Mbits/sec    0   7.51 MBytes       
    [  5]   2.00-3.00   sec  77.5 MBytes   651 Mbits/sec    0   7.51 MBytes       
    [  5]   3.00-4.00   sec  75.0 MBytes   629 Mbits/sec  145   3.75 MBytes       
    [  5]   4.00-5.00   sec  77.5 MBytes   650 Mbits/sec    0   3.75 MBytes       
    [  5]   5.00-6.00   sec  78.8 MBytes   661 Mbits/sec    0   3.75 MBytes       
    [  5]   6.00-7.00   sec  77.5 MBytes   650 Mbits/sec    0   3.75 MBytes       
    [  5]   7.00-8.00   sec  77.5 MBytes   650 Mbits/sec    0   3.75 MBytes       
    [  5]   8.00-9.00   sec  75.0 MBytes   629 Mbits/sec  310   1.93 MBytes       
    [  5]   9.00-10.00  sec  76.2 MBytes   640 Mbits/sec    0   1.98 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   770 MBytes   645 Mbits/sec  455             sender
    [  5]   0.00-10.02  sec   769 MBytes   643 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 149379 bytes (548 packets)
    TX: 61579 bytes (222 packets)
    signal: -32 dBm
    rx bitrate: 585.0 MBit/s VHT-MCS 7 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Ampak 6275P

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AP6275P.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.149, 6.12.33-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AP6275P</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">273</span> Mbits/sec | <span style="font-size: 1.5rem;">262</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.137 port 56383 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  32.7 MBytes   274 Mbits/sec                  
    [  5]   1.00-2.00   sec  32.0 MBytes   268 Mbits/sec                  
    [  5]   2.00-3.00   sec  31.8 MBytes   267 Mbits/sec                  
    [  5]   3.00-4.00   sec  32.2 MBytes   270 Mbits/sec                  
    [  5]   4.00-5.00   sec  30.6 MBytes   256 Mbits/sec                  
    [  5]   5.00-6.00   sec  31.9 MBytes   267 Mbits/sec                  
    [  5]   6.00-7.00   sec  34.3 MBytes   288 Mbits/sec                  
    [  5]   7.00-8.00   sec  32.4 MBytes   272 Mbits/sec                  
    [  5]   8.00-9.00   sec  31.6 MBytes   265 Mbits/sec                  
    [  5]   9.00-10.00  sec  32.8 MBytes   275 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   325 MBytes   273 Mbits/sec  102             sender
    [  5]   0.00-10.00  sec   322 MBytes   270 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.137 port 39057 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  39.6 MBytes   332 Mbits/sec    0   7.49 MBytes       
    [  5]   1.00-2.00   sec  26.2 MBytes   220 Mbits/sec    0   7.49 MBytes       
    [  5]   2.00-3.00   sec  26.2 MBytes   220 Mbits/sec    0   7.50 MBytes       
    [  5]   3.00-4.00   sec  28.8 MBytes   241 Mbits/sec    0   7.50 MBytes       
    [  5]   4.00-5.00   sec  30.0 MBytes   252 Mbits/sec    0   7.50 MBytes       
    [  5]   5.00-6.00   sec  30.0 MBytes   252 Mbits/sec    0   7.50 MBytes       
    [  5]   6.00-7.00   sec  35.0 MBytes   294 Mbits/sec    0   7.50 MBytes       
    [  5]   7.00-8.00   sec  32.5 MBytes   273 Mbits/sec    0   7.50 MBytes       
    [  5]   8.00-9.00   sec  32.5 MBytes   273 Mbits/sec    0   7.50 MBytes       
    [  5]   9.00-10.00  sec  31.2 MBytes   262 Mbits/sec    0   7.50 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   312 MBytes   262 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   311 MBytes   260 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 65859 bytes (141 packets)
    TX: 58074 bytes (207 packets)
    signal: -70 dBm
    rx bitrate: 480.3 MBit/s
    tx bitrate: 340.2 MBit/s
    ```

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">110</span> Mbits/sec | <span style="font-size: 1.5rem;">149</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.186 port 36693 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   3.00-4.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.9 MBytes   108 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   131 MBytes   110 Mbits/sec  187             sender
    [  5]   0.00-10.00  sec   128 MBytes   108 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.186 port 49719 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.9 MBytes   158 Mbits/sec    0    554 KBytes       
    [  5]   1.00-2.00   sec  17.4 MBytes   146 Mbits/sec    0    585 KBytes       
    [  5]   2.00-3.00   sec  17.9 MBytes   150 Mbits/sec    0    617 KBytes       
    [  5]   3.00-4.00   sec  18.4 MBytes   154 Mbits/sec    0    690 KBytes       
    [  5]   4.00-5.00   sec  16.9 MBytes   142 Mbits/sec    0    725 KBytes       
    [  5]   5.00-6.00   sec  18.4 MBytes   154 Mbits/sec   24    318 KBytes       
    [  5]   6.00-7.00   sec  16.6 MBytes   139 Mbits/sec    0    598 KBytes       
    [  5]   7.00-8.00   sec  18.5 MBytes   155 Mbits/sec    0    653 KBytes       
    [  5]   8.00-9.00   sec  16.9 MBytes   142 Mbits/sec    0    690 KBytes       
    [  5]   9.00-10.00  sec  18.0 MBytes   151 Mbits/sec    0    717 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   178 MBytes   149 Mbits/sec   24             sender
    [  5]   0.00-10.01  sec   174 MBytes   146 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 41920 bytes (144 packets)
    TX: 51366 bytes (200 packets)
    signal: -39 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">816</span> Mbits/sec | <span style="font-size: 1.5rem;">571</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 35841 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  98.8 MBytes   828 Mbits/sec                  
    [  5]   1.00-2.00   sec  91.4 MBytes   767 Mbits/sec                  
    [  5]   2.00-3.00   sec  96.0 MBytes   805 Mbits/sec                  
    [  5]   3.00-4.00   sec  88.0 MBytes   738 Mbits/sec                  
    [  5]   4.00-5.00   sec  90.1 MBytes   756 Mbits/sec                  
    [  5]   5.00-6.00   sec  99.6 MBytes   836 Mbits/sec                  
    [  5]   6.00-7.00   sec  98.6 MBytes   827 Mbits/sec                  
    [  5]   7.00-8.00   sec   102 MBytes   860 Mbits/sec                  
    [  5]   8.00-9.00   sec   101 MBytes   848 Mbits/sec                  
    [  5]   9.00-10.00  sec   104 MBytes   872 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   973 MBytes   816 Mbits/sec  255             sender
    [  5]   0.00-10.00  sec   970 MBytes   814 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 60461 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  92.1 MBytes   772 Mbits/sec  557    737 KBytes       
    [  5]   1.00-2.00   sec  89.8 MBytes   753 Mbits/sec  328    479 KBytes       
    [  5]   2.00-3.00   sec  75.6 MBytes   634 Mbits/sec  156    351 KBytes       
    [  5]   3.00-4.00   sec  76.8 MBytes   644 Mbits/sec  102    294 KBytes       
    [  5]   4.00-5.00   sec  39.9 MBytes   334 Mbits/sec    0    450 KBytes       
    [  5]   5.00-6.00   sec  41.9 MBytes   351 Mbits/sec    0    564 KBytes       
    [  5]   6.00-7.00   sec  61.6 MBytes   517 Mbits/sec   23    489 KBytes       
    [  5]   7.00-8.00   sec  75.1 MBytes   630 Mbits/sec   77    469 KBytes       
    [  5]   8.00-9.00   sec  69.1 MBytes   580 Mbits/sec  100    215 KBytes       
    [  5]   9.00-10.00  sec  59.2 MBytes   497 Mbits/sec    0    468 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   681 MBytes   571 Mbits/sec  1343             sender
    [  5]   0.00-10.00  sec   678 MBytes   569 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 66879 bytes (227 packets)
    TX: 82439 bytes (295 packets)
    signal: -30 dBm
    rx bitrate: 2401.9 MBit/s 160MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 2041.6 MBit/s 160MHz HE-MCS 11 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">96.6</span> Mbits/sec | <span style="font-size: 1.5rem;">66.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.188 port 37161 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.12 MBytes  76.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.6 MBytes  97.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.6 MBytes  97.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   115 MBytes  96.6 Mbits/sec   33             sender
    [  5]   0.00-10.00  sec   112 MBytes  93.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.188 port 41073 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.50 MBytes  71.2 Mbits/sec    0    229 KBytes       
    [  5]   1.00-2.00   sec  8.12 MBytes  68.2 Mbits/sec    0    270 KBytes       
    [  5]   2.00-3.00   sec  7.62 MBytes  64.0 Mbits/sec    0    300 KBytes       
    [  5]   3.00-4.00   sec  8.12 MBytes  68.2 Mbits/sec    0    315 KBytes       
    [  5]   4.00-5.00   sec  7.62 MBytes  64.0 Mbits/sec    0    315 KBytes       
    [  5]   5.00-6.00   sec  7.62 MBytes  63.9 Mbits/sec    0    315 KBytes       
    [  5]   6.00-7.00   sec  7.88 MBytes  66.1 Mbits/sec    0    315 KBytes       
    [  5]   7.00-8.00   sec  7.75 MBytes  65.0 Mbits/sec    0    354 KBytes       
    [  5]   8.00-9.00   sec  8.00 MBytes  67.1 Mbits/sec    0    421 KBytes       
    [  5]   9.00-10.00  sec  7.88 MBytes  65.9 Mbits/sec    0    421 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  79.1 MBytes  66.4 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  76.9 MBytes  64.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 111511 bytes (465 packets)
    TX: 66801 bytes (266 packets)
    signal: -17 dBm
    rx bitrate: 240.0 MBit/s MCS 13 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">44.7</span> Mbits/sec | <span style="font-size: 1.5rem;">42.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.164 port 41125 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.13 MBytes  34.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.69 MBytes  39.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.46 MBytes  37.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.98 MBytes  41.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.41 MBytes  45.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.33 MBytes  44.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.35 MBytes  44.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.13 MBytes  43.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.24 MBytes  44.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  53.4 MBytes  44.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  50.0 MBytes  41.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.164 port 40661 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.52 MBytes  46.3 Mbits/sec    0    232 KBytes       
    [  5]   1.00-2.00   sec  4.97 MBytes  41.7 Mbits/sec    0    273 KBytes       
    [  5]   2.00-3.00   sec  5.22 MBytes  43.8 Mbits/sec    0    290 KBytes       
    [  5]   3.00-4.00   sec  5.03 MBytes  42.2 Mbits/sec    0    290 KBytes       
    [  5]   4.00-5.00   sec  5.03 MBytes  42.2 Mbits/sec    0    307 KBytes       
    [  5]   5.00-6.00   sec  4.91 MBytes  41.2 Mbits/sec    0    307 KBytes       
    [  5]   6.00-7.00   sec  5.03 MBytes  42.2 Mbits/sec    0    307 KBytes       
    [  5]   7.00-8.00   sec  5.10 MBytes  42.7 Mbits/sec    0    307 KBytes       
    [  5]   8.00-9.00   sec  4.91 MBytes  41.2 Mbits/sec    0    307 KBytes       
    [  5]   9.00-10.00  sec  4.85 MBytes  40.7 Mbits/sec    0    307 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  50.6 MBytes  42.4 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  50.0 MBytes  41.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 63428 bytes (165 packets)
    TX: 57268 bytes (286 packets)
    signal: -52 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 65.0 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">54.9</span> Mbits/sec | <span style="font-size: 1.5rem;">54.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 47067 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.35 MBytes  44.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.04 MBytes  50.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.42 MBytes  53.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.72 MBytes  56.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.06 MBytes  50.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  7.27 MBytes  60.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  7.31 MBytes  61.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.61 MBytes  55.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.68 MBytes  47.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.35 MBytes  53.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.05  sec  65.8 MBytes  54.9 Mbits/sec    9             sender
    [  5]   0.00-10.00  sec  63.8 MBytes  53.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 45433 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.85 MBytes  57.4 Mbits/sec    0    216 KBytes       
    [  5]   1.00-2.00   sec  5.59 MBytes  46.9 Mbits/sec    0    249 KBytes       
    [  5]   2.00-3.00   sec  6.90 MBytes  57.9 Mbits/sec    0    290 KBytes       
    [  5]   3.00-4.00   sec  7.46 MBytes  62.6 Mbits/sec    0    339 KBytes       
    [  5]   4.00-5.00   sec  5.78 MBytes  48.5 Mbits/sec    0    339 KBytes       
    [  5]   5.00-6.00   sec  7.08 MBytes  59.4 Mbits/sec    0    443 KBytes       
    [  5]   6.00-7.00   sec  6.40 MBytes  53.7 Mbits/sec    0    443 KBytes       
    [  5]   7.00-8.00   sec  6.46 MBytes  54.2 Mbits/sec    0    443 KBytes       
    [  5]   8.00-9.00   sec  6.34 MBytes  53.2 Mbits/sec    0    443 KBytes       
    [  5]   9.00-10.00  sec  5.47 MBytes  45.9 Mbits/sec   35    310 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  64.3 MBytes  54.0 Mbits/sec   35             sender
    [  5]   0.00-10.01  sec  62.4 MBytes  52.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 63956 bytes (209 packets)
    TX: 56508 bytes (251 packets)
    signal: -54 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">46.8</span> Mbits/sec | <span style="font-size: 1.5rem;">50.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.189 port 52827 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.00 MBytes  33.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.38 MBytes  45.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.25 MBytes  44.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  55.9 MBytes  46.8 Mbits/sec    8             sender
    [  5]   0.00-10.00  sec  52.6 MBytes  44.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.189 port 43877 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.50 MBytes  46.1 Mbits/sec    0    320 KBytes       
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec    0    550 KBytes       
    [  5]   2.00-3.00   sec  6.88 MBytes  57.6 Mbits/sec    5    506 KBytes       
    [  5]   3.00-4.00   sec  5.62 MBytes  47.2 Mbits/sec    0    576 KBytes       
    [  5]   4.00-5.00   sec  5.62 MBytes  47.2 Mbits/sec    0    636 KBytes       
    [  5]   5.00-6.00   sec  5.62 MBytes  47.2 Mbits/sec    0    673 KBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.2 Mbits/sec    0    701 KBytes       
    [  5]   7.00-8.00   sec  7.00 MBytes  58.7 Mbits/sec    0    717 KBytes       
    [  5]   8.00-9.00   sec  5.50 MBytes  46.2 Mbits/sec    0    724 KBytes       
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec    0    724 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  60.2 MBytes  50.5 Mbits/sec    5             sender
    [  5]   0.00-10.00  sec  57.8 MBytes  48.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 104301 bytes (445 packets)
    TX: 55932 bytes (216 packets)
    signal: -27 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">85.0</span> Mbits/sec | <span style="font-size: 1.5rem;">67.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.190 port 58389 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.12 MBytes  76.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  9.75 MBytes  81.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.0 MBytes  84.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.0 MBytes  83.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  9.88 MBytes  82.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.1 MBytes  85.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.0 MBytes  83.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.1 MBytes  85.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   101 MBytes  85.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  99.0 MBytes  83.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.190 port 54813 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.88 MBytes  74.1 Mbits/sec    0    291 KBytes       
    [  5]   1.00-2.00   sec  8.75 MBytes  73.7 Mbits/sec    0    365 KBytes       
    [  5]   2.00-3.00   sec  8.00 MBytes  67.1 Mbits/sec    0    426 KBytes       
    [  5]   3.00-4.00   sec  7.00 MBytes  58.7 Mbits/sec    0    426 KBytes       
    [  5]   4.00-5.00   sec  7.88 MBytes  66.1 Mbits/sec    0    426 KBytes       
    [  5]   5.00-6.00   sec  7.75 MBytes  65.0 Mbits/sec    0    426 KBytes       
    [  5]   6.00-7.00   sec  7.88 MBytes  66.0 Mbits/sec    0    426 KBytes       
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec    0    426 KBytes       
    [  5]   8.00-9.00   sec  8.00 MBytes  67.1 Mbits/sec    0    426 KBytes       
    [  5]   9.00-10.00  sec  7.88 MBytes  66.0 Mbits/sec    0    426 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  79.9 MBytes  67.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  77.9 MBytes  65.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 231320 bytes (725 packets)
    TX: 121316 bytes (597 packets)
    signal: -34 dBm
    rx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">45.5</span> Mbits/sec | <span style="font-size: 1.5rem;">30.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.191 port 44361 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.12 MBytes  42.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.25 MBytes  44.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  54.2 MBytes  45.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  51.8 MBytes  43.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.191 port 58915 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.25 MBytes  35.6 Mbits/sec    0    214 KBytes       
    [  5]   1.00-2.00   sec  3.75 MBytes  31.5 Mbits/sec    0    286 KBytes       
    [  5]   2.00-3.00   sec  4.12 MBytes  34.6 Mbits/sec    0    365 KBytes       
    [  5]   3.00-4.00   sec  3.12 MBytes  26.2 Mbits/sec    0    382 KBytes       
    [  5]   4.00-5.00   sec  3.88 MBytes  32.5 Mbits/sec    0    382 KBytes       
    [  5]   5.00-6.00   sec  3.12 MBytes  26.2 Mbits/sec    0    382 KBytes       
    [  5]   6.00-7.00   sec  3.25 MBytes  27.3 Mbits/sec    0    382 KBytes       
    [  5]   7.00-8.00   sec  4.00 MBytes  33.6 Mbits/sec    0    382 KBytes       
    [  5]   8.00-9.00   sec  3.25 MBytes  27.3 Mbits/sec    0    382 KBytes       
    [  5]   9.00-10.00  sec  3.12 MBytes  26.2 Mbits/sec    0    382 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  35.9 MBytes  30.1 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  34.2 MBytes  28.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 101086 bytes (372 packets)
    TX: 61142 bytes (227 packets)
    signal: -36 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">35.5</span> Mbits/sec | <span style="font-size: 1.5rem;">48.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 53759 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.29 MBytes  44.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.20 MBytes  35.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.22 MBytes  27.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.58 MBytes  30.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.96 MBytes  41.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.70 MBytes  39.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.04 MBytes  25.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.96 MBytes  33.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.35 MBytes  11.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  42.4 MBytes  35.5 Mbits/sec    7             sender
    [  5]   0.00-10.00  sec  38.7 MBytes  32.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 48721 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.19 MBytes  51.9 Mbits/sec    0    376 KBytes       
    [  5]   1.00-2.00   sec  5.65 MBytes  47.4 Mbits/sec    0    417 KBytes       
    [  5]   2.00-3.00   sec  5.90 MBytes  49.5 Mbits/sec    0    440 KBytes       
    [  5]   3.00-4.00   sec  5.47 MBytes  45.9 Mbits/sec    0    467 KBytes       
    [  5]   4.00-5.00   sec  5.65 MBytes  47.4 Mbits/sec    0    467 KBytes       
    [  5]   5.00-6.00   sec  5.59 MBytes  46.9 Mbits/sec    0    496 KBytes       
    [  5]   6.00-7.00   sec  5.65 MBytes  47.4 Mbits/sec    0    535 KBytes       
    [  5]   7.00-8.00   sec  5.78 MBytes  48.5 Mbits/sec    0    535 KBytes       
    [  5]   8.00-9.00   sec  5.28 MBytes  44.3 Mbits/sec    0    535 KBytes       
    [  5]   9.00-10.00  sec  6.15 MBytes  51.6 Mbits/sec    0    566 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  57.3 MBytes  48.1 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  55.9 MBytes  46.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">1.67</span> Mbits/sec | <span style="font-size: 1.5rem;">17.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.192 port 48165 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   256 KBytes  2.09 Mbits/sec                  
    [  5]   1.00-2.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   2.00-3.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   3.00-4.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   4.00-5.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   5.00-6.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   6.00-7.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   7.00-8.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   8.00-9.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   9.00-10.00  sec   128 KBytes  1.05 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.07  sec  2.00 MBytes  1.67 Mbits/sec   75             sender
    [  5]   0.00-10.00  sec  1.75 MBytes  1.47 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.192 port 33845 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  2.00 MBytes  16.8 Mbits/sec    0    115 KBytes       
    [  5]   1.00-2.00   sec  2.38 MBytes  19.9 Mbits/sec    0    202 KBytes       
    [  5]   2.00-3.00   sec  2.00 MBytes  16.8 Mbits/sec    0    260 KBytes       
    [  5]   3.00-4.00   sec  1.88 MBytes  15.7 Mbits/sec    0    346 KBytes       
    [  5]   4.00-5.00   sec  2.25 MBytes  18.9 Mbits/sec    0    437 KBytes       
    [  5]   5.00-6.00   sec  2.88 MBytes  24.1 Mbits/sec    0    549 KBytes       
    [  5]   6.00-7.00   sec  2.38 MBytes  19.9 Mbits/sec    0    632 KBytes       
    [  5]   7.00-8.00   sec  1.25 MBytes  10.5 Mbits/sec    0    714 KBytes       
    [  5]   8.00-9.00   sec  2.75 MBytes  23.1 Mbits/sec    0    810 KBytes       
    [  5]   9.00-10.00  sec  1.38 MBytes  11.5 Mbits/sec    0    844 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  21.1 MBytes  17.7 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  18.4 MBytes  15.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 85181 bytes (369 packets)
    TX: 56055 bytes (199 packets)
    signal: -44 dBm
    rx bitrate: 52.0 MBit/s MCS 5
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">141</span> Mbits/sec | <span style="font-size: 1.5rem;">140</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 39925 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.7 MBytes   132 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.6 MBytes   140 Mbits/sec                  
    [  5]   4.00-5.00   sec  14.7 MBytes   123 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.4 MBytes   155 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.9 MBytes   142 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   169 MBytes   141 Mbits/sec  350             sender
    [  5]   0.00-10.00  sec   166 MBytes   139 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 32803 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.7 MBytes   157 Mbits/sec    0    421 KBytes       
    [  5]   1.00-2.00   sec  16.0 MBytes   134 Mbits/sec    0    421 KBytes       
    [  5]   2.00-3.00   sec  16.7 MBytes   140 Mbits/sec    0    421 KBytes       
    [  5]   3.00-4.00   sec  16.8 MBytes   141 Mbits/sec    0    421 KBytes       
    [  5]   4.00-5.00   sec  16.8 MBytes   141 Mbits/sec    0    421 KBytes       
    [  5]   5.00-6.00   sec  15.9 MBytes   133 Mbits/sec    0    421 KBytes       
    [  5]   6.00-7.00   sec  16.7 MBytes   140 Mbits/sec    0    421 KBytes       
    [  5]   7.00-8.00   sec  16.7 MBytes   140 Mbits/sec    0    421 KBytes       
    [  5]   8.00-9.00   sec  16.7 MBytes   140 Mbits/sec    0    421 KBytes       
    [  5]   9.00-10.00  sec  15.9 MBytes   133 Mbits/sec    0    421 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   167 MBytes   140 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   165 MBytes   138 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 3143165524 bytes (2598523 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">19.3</span> Mbits/sec | <span style="font-size: 1.5rem;">12.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.196 port 50459 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.91 MBytes  16.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.60 MBytes  13.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.90 MBytes  16.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.04 MBytes  17.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.99 MBytes  16.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.07 MBytes  17.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.33 MBytes  19.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.41 MBytes  20.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.18 MBytes  18.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.45 MBytes  20.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.10  sec  23.2 MBytes  19.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  20.9 MBytes  17.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.196 port 46033 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.31 MBytes  11.0 Mbits/sec    5   36.8 KBytes       
    [  5]   1.00-2.00   sec  1.40 MBytes  11.8 Mbits/sec    1   42.4 KBytes       
    [  5]   2.00-3.00   sec  1.51 MBytes  12.6 Mbits/sec    0   65.0 KBytes       
    [  5]   3.00-4.00   sec  1.62 MBytes  13.6 Mbits/sec    0   80.6 KBytes       
    [  5]   4.00-5.00   sec  1.24 MBytes  10.4 Mbits/sec    3   56.6 KBytes       
    [  5]   5.00-6.00   sec  1.49 MBytes  12.5 Mbits/sec    0   74.9 KBytes       
    [  5]   6.00-7.00   sec  1.49 MBytes  12.5 Mbits/sec    0   84.8 KBytes       
    [  5]   7.00-8.00   sec  1.49 MBytes  12.5 Mbits/sec    0   91.9 KBytes       
    [  5]   8.00-9.00   sec  1.37 MBytes  11.5 Mbits/sec    0   97.6 KBytes       
    [  5]   9.00-10.00  sec  1.49 MBytes  12.5 Mbits/sec    0    102 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  14.4 MBytes  12.1 Mbits/sec    9             sender
    [  5]   0.00-10.04  sec  14.1 MBytes  11.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 60150 bytes (180 packets)
    TX: 62764 bytes (257 packets)
    signal: -30 dBm
    rx bitrate: 6.0 MBit/s
    tx bitrate: 52.0 MBit/s MCS 5
    
    ```
## Failed Devices

| | Name | Model | Class |
|:---:|:-----|:--------|:------|
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AIC8800.png height=64> | AIC8800 | AIC8800 | AX |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png height=64> | Atheros AR9271 | AR9271 | N |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8852AU.png height=64> | BrosTrend 1800 | RTL8852AU | AXE3000 |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7601U.png height=64> | Ralink MT7601U | MT7601U |  |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png height=64> | Realtek 8188EU | RTL8192CU | N |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8852BE.png height=64> | Realtek 8852BE | RTL8852BE | AX |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL2870.png height=64> | Realtek RT2870 | RTL2870 | N |


<!-- DUT-STOP -->

## Contribute

- Assist us in developing and maintaining our testing system: Your expertise can help us enhance and optimize [our test infrastructure](https://github.com/armbian/armbian.github.io/actions/workflows/usb-wireless-autotest.yml). By contributing your skills, you can play a key role in ensuring the accuracy and reliability of our test results.

- Donate hardware: Your contribution of new hardware, whether it’s a wireless adapter or any other equipment, helps us expand our testing capabilities. We’re specifically looking for [new wireless adapters](https://www.amazon.de/hz/wishlist/ls/1GA17IGQ2MF0V?ref_=wl_share) that haven’t yet been added to our system. Your donation can directly impact the scope and depth of our tests.

- Join our team: Become part of our passionate and dedicated team. We’re looking for [individuals who share our vision and are eager to contribute to the development of innovative testing solutions](https://forum.armbian.com/staffapplications/). Whether you have technical expertise or simply a willingness to learn, there’s a place for you here!

## Other resources

- [USB WiFi Adapter Information for Linux](https://github.com/morrownr/USB-WiFi)
- [Official Linux Wireless documentation](https://wireless.docs.kernel.org/en/latest/index.html)
- [Armbian forum - Advanced users - Development](https://forum.armbian.com/forum/4-advanced-users-development/)
