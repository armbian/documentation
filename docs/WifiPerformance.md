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
**Test Date:** [2025-06-24 18:22 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15857611494)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">45.0</span> Mbits/sec | <span style="font-size: 1.5rem;">55.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.129 port 59815 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.10 MBytes  42.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.11 MBytes  42.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.13 MBytes  43.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.09 MBytes  42.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.98 MBytes  41.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.65 MBytes  39.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.31 MBytes  44.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.15 MBytes  43.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.97 MBytes  41.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.08 MBytes  42.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  53.8 MBytes  45.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  50.6 MBytes  42.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.129 port 39165 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.86 MBytes  65.9 Mbits/sec    0    400 KBytes       
    [  5]   1.00-2.00   sec  7.39 MBytes  62.0 Mbits/sec    0    673 KBytes       
    [  5]   2.00-3.00   sec  6.25 MBytes  52.4 Mbits/sec    0    764 KBytes       
    [  5]   3.00-4.00   sec  6.25 MBytes  52.4 Mbits/sec    0    826 KBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    0    888 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1007 KBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.04 MBytes       
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.11 MBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.18 MBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.28 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  66.5 MBytes  55.8 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  63.5 MBytes  53.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 138588 bytes (380 packets)
    TX: 83465 bytes (498 packets)
    signal: -27 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">107</span> Mbits/sec | <span style="font-size: 1.5rem;">96.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 36443 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.9 MBytes  99.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   2.00-3.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.7 MBytes  98.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.6 MBytes   105 Mbits/sec                  
    [  5]   6.00-7.00   sec  12.8 MBytes   108 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.4 MBytes   104 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.9 MBytes   108 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   128 MBytes   107 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   126 MBytes   105 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 40089 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  11.3 MBytes  94.4 Mbits/sec    0    467 KBytes       
    [  5]   1.00-2.00   sec  11.7 MBytes  98.5 Mbits/sec    0    518 KBytes       
    [  5]   2.00-3.00   sec  11.1 MBytes  93.3 Mbits/sec    0    518 KBytes       
    [  5]   3.00-4.00   sec  11.9 MBytes   100 Mbits/sec    0    607 KBytes       
    [  5]   4.00-5.00   sec  11.6 MBytes  97.5 Mbits/sec    0    607 KBytes       
    [  5]   5.00-6.00   sec  10.9 MBytes  91.2 Mbits/sec    0    649 KBytes       
    [  5]   6.00-7.00   sec  11.7 MBytes  98.0 Mbits/sec    0    649 KBytes       
    [  5]   7.00-8.00   sec  11.7 MBytes  98.5 Mbits/sec    0    672 KBytes       
    [  5]   8.00-9.00   sec  12.1 MBytes   101 Mbits/sec    0    730 KBytes       
    [  5]   9.00-10.00  sec  11.2 MBytes  94.3 Mbits/sec    0    730 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   115 MBytes  96.7 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   114 MBytes  95.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 105599 bytes (464 packets)
    TX: 57684 bytes (224 packets)
    signal: -35 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">90.4</span> Mbits/sec | <span style="font-size: 1.5rem;">91.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 33577 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.88 MBytes  82.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  10.9 MBytes  91.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   107 MBytes  89.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 34109 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.6 MBytes   106 Mbits/sec    0    570 KBytes       
    [  5]   1.00-2.00   sec  11.8 MBytes  98.6 Mbits/sec    0    706 KBytes       
    [  5]   2.00-3.00   sec  9.88 MBytes  82.8 Mbits/sec    0    724 KBytes       
    [  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0    724 KBytes       
    [  5]   4.00-5.00   sec  11.0 MBytes  92.3 Mbits/sec    0    812 KBytes       
    [  5]   5.00-6.00   sec  11.1 MBytes  93.3 Mbits/sec    0    860 KBytes       
    [  5]   6.00-7.00   sec  9.88 MBytes  82.9 Mbits/sec    0    860 KBytes       
    [  5]   7.00-8.00   sec  11.1 MBytes  93.3 Mbits/sec    0    860 KBytes       
    [  5]   8.00-9.00   sec  9.75 MBytes  81.8 Mbits/sec    0    860 KBytes       
    [  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0    860 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   110 MBytes  91.9 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   106 MBytes  88.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 181152 bytes (452 packets)
    TX: 91737 bytes (485 packets)
    signal: -34 dBm
    rx bitrate: 130.0 MBit/s MCS 15
    tx bitrate: 144.4 MBit/s MCS 15 short GI
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">148</span> Mbits/sec | <span style="font-size: 1.5rem;">197</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 34525 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.1 MBytes   127 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   5.00-6.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.0 MBytes   143 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   177 MBytes   148 Mbits/sec  153             sender
    [  5]   0.00-10.00  sec   174 MBytes   146 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 49055 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  26.4 MBytes   221 Mbits/sec    0    679 KBytes       
    [  5]   1.00-2.00   sec  23.8 MBytes   199 Mbits/sec    0    717 KBytes       
    [  5]   2.00-3.00   sec  23.4 MBytes   196 Mbits/sec    0    757 KBytes       
    [  5]   3.00-4.00   sec  23.6 MBytes   198 Mbits/sec    0    850 KBytes       
    [  5]   4.00-5.00   sec  22.4 MBytes   188 Mbits/sec    0    850 KBytes       
    [  5]   5.00-6.00   sec  25.0 MBytes   210 Mbits/sec    0    850 KBytes       
    [  5]   6.00-7.00   sec  22.1 MBytes   186 Mbits/sec    0    850 KBytes       
    [  5]   7.00-8.00   sec  24.9 MBytes   209 Mbits/sec    0    850 KBytes       
    [  5]   8.00-9.00   sec  22.1 MBytes   186 Mbits/sec    0    895 KBytes       
    [  5]   9.00-10.00  sec  20.8 MBytes   174 Mbits/sec    0    895 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   234 MBytes   197 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   232 MBytes   194 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -36 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">155</span> Mbits/sec | <span style="font-size: 1.5rem;">269</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 58323 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.2 MBytes   145 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.0 MBytes   151 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   185 MBytes   155 Mbits/sec    7             sender
    [  5]   0.00-10.00  sec   182 MBytes   153 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 41911 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  33.6 MBytes   282 Mbits/sec    0    929 KBytes       
    [  5]   1.00-2.00   sec  31.2 MBytes   262 Mbits/sec    0    998 KBytes       
    [  5]   2.00-3.00   sec  31.6 MBytes   265 Mbits/sec    0   1.08 MBytes       
    [  5]   3.00-4.00   sec  33.0 MBytes   277 Mbits/sec    0   1.31 MBytes       
    [  5]   4.00-5.00   sec  32.2 MBytes   271 Mbits/sec    0   1.31 MBytes       
    [  5]   5.00-6.00   sec  32.1 MBytes   269 Mbits/sec    0   1.38 MBytes       
    [  5]   6.00-7.00   sec  31.6 MBytes   265 Mbits/sec    0   1.55 MBytes       
    [  5]   7.00-8.00   sec  31.8 MBytes   266 Mbits/sec    0   1.72 MBytes       
    [  5]   8.00-9.00   sec  32.1 MBytes   269 Mbits/sec    0   1.72 MBytes       
    [  5]   9.00-10.00  sec  31.5 MBytes   264 Mbits/sec    0   1.72 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   321 MBytes   269 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   318 MBytes   267 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -39 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8821CU #1

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">133</span> Mbits/sec | <span style="font-size: 1.5rem;">208</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 34113 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.5 MBytes   138 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   5.00-6.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.1 MBytes   135 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec   159 MBytes   133 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   158 MBytes   133 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 56381 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  26.6 MBytes   223 Mbits/sec    0    587 KBytes       
    [  5]   1.00-2.00   sec  25.4 MBytes   213 Mbits/sec    0    679 KBytes       
    [  5]   2.00-3.00   sec  24.6 MBytes   207 Mbits/sec    0    713 KBytes       
    [  5]   3.00-4.00   sec  24.8 MBytes   208 Mbits/sec    0    713 KBytes       
    [  5]   4.00-5.00   sec  23.6 MBytes   198 Mbits/sec    0    713 KBytes       
    [  5]   5.00-6.00   sec  25.0 MBytes   210 Mbits/sec    0    747 KBytes       
    [  5]   6.00-7.00   sec  24.8 MBytes   208 Mbits/sec    0    785 KBytes       
    [  5]   7.00-8.00   sec  23.5 MBytes   197 Mbits/sec    0    785 KBytes       
    [  5]   8.00-9.00   sec  25.1 MBytes   211 Mbits/sec    0    785 KBytes       
    [  5]   9.00-10.00  sec  24.8 MBytes   208 Mbits/sec    0    785 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   248 MBytes   208 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   245 MBytes   205 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 167968 bytes (283 packets)
    TX: 88506 bytes (447 packets)
    signal: -45 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">274</span> Mbits/sec | <span style="font-size: 1.5rem;">258</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 59917 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  24.4 MBytes   204 Mbits/sec                  
    [  5]   1.00-2.00   sec  32.5 MBytes   273 Mbits/sec                  
    [  5]   2.00-3.00   sec  32.9 MBytes   276 Mbits/sec                  
    [  5]   3.00-4.00   sec  33.2 MBytes   279 Mbits/sec                  
    [  5]   4.00-5.00   sec  33.2 MBytes   279 Mbits/sec                  
    [  5]   5.00-6.00   sec  33.0 MBytes   277 Mbits/sec                  
    [  5]   6.00-7.00   sec  33.1 MBytes   278 Mbits/sec                  
    [  5]   7.00-8.00   sec  33.1 MBytes   278 Mbits/sec                  
    [  5]   8.00-9.00   sec  33.6 MBytes   282 Mbits/sec                  
    [  5]   9.00-10.00  sec  33.8 MBytes   283 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   326 MBytes   274 Mbits/sec   90             sender
    [  5]   0.00-10.00  sec   323 MBytes   271 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 35969 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  32.6 MBytes   273 Mbits/sec    0   1.92 MBytes       
    [  5]   1.00-2.00   sec  30.5 MBytes   256 Mbits/sec    0   1.98 MBytes       
    [  5]   2.00-3.00   sec  30.4 MBytes   255 Mbits/sec    0   2.13 MBytes       
    [  5]   3.00-4.00   sec  30.0 MBytes   252 Mbits/sec    0   2.85 MBytes       
    [  5]   4.00-5.00   sec  30.8 MBytes   258 Mbits/sec    0   2.85 MBytes       
    [  5]   5.00-6.00   sec  30.9 MBytes   259 Mbits/sec    0   2.85 MBytes       
    [  5]   6.00-7.00   sec  29.6 MBytes   249 Mbits/sec    0   2.85 MBytes       
    [  5]   7.00-8.00   sec  31.0 MBytes   260 Mbits/sec    0   2.85 MBytes       
    [  5]   8.00-9.00   sec  30.0 MBytes   252 Mbits/sec    0   2.85 MBytes       
    [  5]   9.00-10.00  sec  31.4 MBytes   263 Mbits/sec    0   2.85 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   307 MBytes   258 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   304 MBytes   254 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">333</span> Mbits/sec | <span style="font-size: 1.5rem;">611</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 50741 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  53.3 MBytes   447 Mbits/sec                  
    [  5]   1.00-2.00   sec  47.1 MBytes   395 Mbits/sec                  
    [  5]   2.00-3.00   sec  37.5 MBytes   314 Mbits/sec                  
    [  5]   3.00-4.00   sec  34.4 MBytes   288 Mbits/sec                  
    [  5]   4.00-5.00   sec  38.0 MBytes   319 Mbits/sec                  
    [  5]   5.00-6.00   sec  35.9 MBytes   301 Mbits/sec                  
    [  5]   6.00-7.00   sec  35.1 MBytes   295 Mbits/sec                  
    [  5]   7.00-8.00   sec  36.5 MBytes   306 Mbits/sec                  
    [  5]   8.00-9.00   sec  37.9 MBytes   318 Mbits/sec                  
    [  5]   9.00-10.00  sec  38.8 MBytes   326 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   398 MBytes   333 Mbits/sec  321             sender
    [  5]   0.00-10.00  sec   395 MBytes   331 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 45171 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  78.2 MBytes   656 Mbits/sec    0   7.00 MBytes       
    [  5]   1.00-2.00   sec  75.0 MBytes   627 Mbits/sec    8   3.50 MBytes       
    [  5]   2.00-3.00   sec  77.5 MBytes   653 Mbits/sec    0   3.50 MBytes       
    [  5]   3.00-4.00   sec  75.0 MBytes   629 Mbits/sec    0   3.50 MBytes       
    [  5]   4.00-5.00   sec  76.2 MBytes   640 Mbits/sec   73    916 KBytes       
    [  5]   5.00-6.00   sec  70.0 MBytes   587 Mbits/sec    0   1020 KBytes       
    [  5]   6.00-7.00   sec  70.0 MBytes   587 Mbits/sec    0   1.09 MBytes       
    [  5]   7.00-8.00   sec  71.2 MBytes   598 Mbits/sec    0   1.18 MBytes       
    [  5]   8.00-9.00   sec  72.5 MBytes   608 Mbits/sec    0   1.26 MBytes       
    [  5]   9.00-10.00  sec  62.5 MBytes   524 Mbits/sec   15    759 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   728 MBytes   611 Mbits/sec   96             sender
    [  5]   0.00-10.01  sec   726 MBytes   608 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 143821 bytes (510 packets)
    TX: 58783 bytes (214 packets)
    signal: -34 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Ampak 6275P

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AP6275P.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.149, 6.12.33-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AP6275P</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">373</span> Mbits/sec | <span style="font-size: 1.5rem;">452</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 33763 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  44.3 MBytes   372 Mbits/sec                  
    [  5]   1.00-2.00   sec  43.8 MBytes   367 Mbits/sec                  
    [  5]   2.00-3.00   sec  45.7 MBytes   383 Mbits/sec                  
    [  5]   3.00-4.00   sec  44.6 MBytes   374 Mbits/sec                  
    [  5]   4.00-5.00   sec  45.0 MBytes   377 Mbits/sec                  
    [  5]   5.00-6.00   sec  43.2 MBytes   362 Mbits/sec                  
    [  5]   6.00-7.00   sec  45.2 MBytes   379 Mbits/sec                  
    [  5]   7.00-8.00   sec  43.8 MBytes   368 Mbits/sec                  
    [  5]   8.00-9.00   sec  44.5 MBytes   373 Mbits/sec                  
    [  5]   9.00-10.00  sec  41.7 MBytes   350 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   445 MBytes   373 Mbits/sec   93             sender
    [  5]   0.00-10.00  sec   442 MBytes   371 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 55165 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  59.2 MBytes   497 Mbits/sec    0   6.44 MBytes       
    [  5]   1.00-2.00   sec  57.5 MBytes   482 Mbits/sec    0   6.44 MBytes       
    [  5]   2.00-3.00   sec  56.2 MBytes   472 Mbits/sec    0   6.44 MBytes       
    [  5]   3.00-4.00   sec  56.2 MBytes   472 Mbits/sec    0   6.44 MBytes       
    [  5]   4.00-5.00   sec  52.5 MBytes   440 Mbits/sec   51   3.22 MBytes       
    [  5]   5.00-6.00   sec  47.5 MBytes   398 Mbits/sec    0   3.22 MBytes       
    [  5]   6.00-7.00   sec  48.8 MBytes   409 Mbits/sec    0   3.22 MBytes       
    [  5]   7.00-8.00   sec  56.2 MBytes   472 Mbits/sec    0   3.22 MBytes       
    [  5]   8.00-9.00   sec  57.5 MBytes   482 Mbits/sec  132    841 KBytes       
    [  5]   9.00-10.00  sec  47.5 MBytes   398 Mbits/sec    0    921 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   539 MBytes   452 Mbits/sec  183             sender
    [  5]   0.00-10.01  sec   537 MBytes   450 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 61261 bytes (125 packets)
    TX: 54950 bytes (194 packets)
    signal: -62 dBm
    rx bitrate: 720.5 MBit/s
    tx bitrate: 720.5 MBit/s
    
    ```

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">113</span> Mbits/sec | <span style="font-size: 1.5rem;">146</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 41701 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.2 MBytes   111 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   135 MBytes   113 Mbits/sec  174             sender
    [  5]   0.00-10.00  sec   132 MBytes   111 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 50845 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.0 MBytes   151 Mbits/sec    0    519 KBytes       
    [  5]   1.00-2.00   sec  17.8 MBytes   149 Mbits/sec    0    622 KBytes       
    [  5]   2.00-3.00   sec  18.4 MBytes   154 Mbits/sec    0    789 KBytes       
    [  5]   3.00-4.00   sec  16.8 MBytes   141 Mbits/sec    0    789 KBytes       
    [  5]   4.00-5.00   sec  17.6 MBytes   148 Mbits/sec    0    830 KBytes       
    [  5]   5.00-6.00   sec  17.0 MBytes   143 Mbits/sec    0    830 KBytes       
    [  5]   6.00-7.00   sec  16.9 MBytes   142 Mbits/sec    0    871 KBytes       
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec    0    871 KBytes       
    [  5]   8.00-9.00   sec  16.9 MBytes   142 Mbits/sec    0    871 KBytes       
    [  5]   9.00-10.00  sec  17.1 MBytes   143 Mbits/sec    0    871 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   174 MBytes   146 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   171 MBytes   144 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 47270 bytes (178 packets)
    TX: 52154 bytes (217 packets)
    signal: -36 dBm
    rx bitrate: 864.8 MBit/s 80MHz HE-MCS 8 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">847</span> Mbits/sec | <span style="font-size: 1.5rem;">745</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.125 port 47403 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   106 MBytes   889 Mbits/sec                  
    [  5]   1.00-2.00   sec   109 MBytes   912 Mbits/sec                  
    [  5]   2.00-3.00   sec   106 MBytes   891 Mbits/sec                  
    [  5]   3.00-4.00   sec   106 MBytes   889 Mbits/sec                  
    [  5]   4.00-5.00   sec   102 MBytes   859 Mbits/sec                  
    [  5]   5.00-6.00   sec  97.6 MBytes   819 Mbits/sec                  
    [  5]   6.00-7.00   sec  90.2 MBytes   757 Mbits/sec                  
    [  5]   7.00-8.00   sec  93.0 MBytes   780 Mbits/sec                  
    [  5]   8.00-9.00   sec  94.8 MBytes   795 Mbits/sec                  
    [  5]   9.00-10.00  sec   103 MBytes   861 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  1010 MBytes   847 Mbits/sec  1917             sender
    [  5]   0.00-10.00  sec  1008 MBytes   845 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.125 port 42071 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  96.8 MBytes   811 Mbits/sec    0   5.21 MBytes       
    [  5]   1.00-2.00   sec   103 MBytes   863 Mbits/sec  748   1.31 MBytes       
    [  5]   2.00-3.00   sec  98.2 MBytes   824 Mbits/sec    0   1.41 MBytes       
    [  5]   3.00-4.00   sec   106 MBytes   892 Mbits/sec    0   1.51 MBytes       
    [  5]   4.00-5.00   sec   101 MBytes   844 Mbits/sec  288    830 KBytes       
    [  5]   5.00-6.00   sec  77.8 MBytes   652 Mbits/sec   57    574 KBytes       
    [  5]   6.00-7.00   sec  73.0 MBytes   612 Mbits/sec    9    464 KBytes       
    [  5]   7.00-8.00   sec  75.0 MBytes   629 Mbits/sec    0    658 KBytes       
    [  5]   8.00-9.00   sec  74.2 MBytes   623 Mbits/sec    5    465 KBytes       
    [  5]   9.00-10.00  sec  83.2 MBytes   697 Mbits/sec    0    676 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   888 MBytes   745 Mbits/sec  1107             sender
    [  5]   0.00-10.01  sec   886 MBytes   742 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 49506 bytes (203 packets)
    TX: 58050 bytes (218 packets)
    signal: -34 dBm
    rx bitrate: 1729.6 MBit/s 160MHz HE-MCS 8 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">93.1</span> Mbits/sec | <span style="font-size: 1.5rem;">65.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 46279 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.2 MBytes  85.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.1 MBytes  85.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.5 MBytes  87.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.4 MBytes  95.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.0 MBytes  92.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.2 MBytes  94.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   111 MBytes  93.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   109 MBytes  91.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 44391 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.38 MBytes  70.2 Mbits/sec    0    228 KBytes       
    [  5]   1.00-2.00   sec  7.75 MBytes  65.0 Mbits/sec    0    266 KBytes       
    [  5]   2.00-3.00   sec  7.62 MBytes  64.0 Mbits/sec    0    297 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0    297 KBytes       
    [  5]   4.00-5.00   sec  8.12 MBytes  68.2 Mbits/sec    0    314 KBytes       
    [  5]   5.00-6.00   sec  7.75 MBytes  65.0 Mbits/sec    0    337 KBytes       
    [  5]   6.00-7.00   sec  7.25 MBytes  60.8 Mbits/sec    0    354 KBytes       
    [  5]   7.00-8.00   sec  8.25 MBytes  69.2 Mbits/sec    0    380 KBytes       
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec    0    380 KBytes       
    [  5]   9.00-10.00  sec  7.62 MBytes  63.9 Mbits/sec    0    380 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  77.9 MBytes  65.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  75.8 MBytes  63.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 165022 bytes (494 packets)
    TX: 83805 bytes (490 packets)
    signal: -23 dBm
    rx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">46.5</span> Mbits/sec | <span style="font-size: 1.5rem;">33.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.124 port 37979 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.99 MBytes  41.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.86 MBytes  40.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.56 MBytes  46.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.60 MBytes  47.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.53 MBytes  46.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.13 MBytes  43.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.28 MBytes  44.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.18 MBytes  43.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.15 MBytes  43.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  55.5 MBytes  46.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  52.7 MBytes  44.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.124 port 38885 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.76 MBytes  39.9 Mbits/sec    0    206 KBytes       
    [  5]   1.00-2.00   sec  4.23 MBytes  35.4 Mbits/sec    0    216 KBytes       
    [  5]   2.00-3.00   sec  4.47 MBytes  37.5 Mbits/sec    0    229 KBytes       
    [  5]   3.00-4.00   sec  4.29 MBytes  36.0 Mbits/sec    0    229 KBytes       
    [  5]   4.00-5.00   sec  3.79 MBytes  31.8 Mbits/sec    0    229 KBytes       
    [  5]   5.00-6.00   sec  3.23 MBytes  27.1 Mbits/sec    0    229 KBytes       
    [  5]   6.00-7.00   sec  3.23 MBytes  27.1 Mbits/sec    0    229 KBytes       
    [  5]   7.00-8.00   sec  4.04 MBytes  33.9 Mbits/sec    0    229 KBytes       
    [  5]   8.00-9.00   sec  3.85 MBytes  32.3 Mbits/sec    0    229 KBytes       
    [  5]   9.00-10.00  sec  3.79 MBytes  31.8 Mbits/sec    0    229 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  39.7 MBytes  33.3 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  39.0 MBytes  32.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 71432 bytes (208 packets)
    TX: 59767 bytes (273 packets)
    signal: -55 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 65.0 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">49.4</span> Mbits/sec | <span style="font-size: 1.5rem;">52.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.123 port 50361 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.33 MBytes  53.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.73 MBytes  48.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.45 MBytes  54.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.47 MBytes  54.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.77 MBytes  48.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.80 MBytes  57.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.15 MBytes  43.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.40 MBytes  45.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.23 MBytes  43.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.79 MBytes  40.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.32  sec  60.8 MBytes  49.4 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec  58.1 MBytes  48.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.123 port 56181 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.35 MBytes  53.2 Mbits/sec    0    219 KBytes       
    [  5]   1.00-2.00   sec  7.33 MBytes  61.5 Mbits/sec    0    308 KBytes       
    [  5]   2.00-3.00   sec  5.78 MBytes  48.4 Mbits/sec    0    308 KBytes       
    [  5]   3.00-4.00   sec  7.02 MBytes  58.9 Mbits/sec    0    324 KBytes       
    [  5]   4.00-5.00   sec  6.15 MBytes  51.6 Mbits/sec    0    324 KBytes       
    [  5]   5.00-6.00   sec  5.47 MBytes  45.8 Mbits/sec    0    324 KBytes       
    [  5]   6.00-7.00   sec  6.28 MBytes  52.7 Mbits/sec    0    339 KBytes       
    [  5]   7.00-8.00   sec  5.90 MBytes  49.5 Mbits/sec    0    356 KBytes       
    [  5]   8.00-9.00   sec  6.71 MBytes  56.3 Mbits/sec    0    356 KBytes       
    [  5]   9.00-10.00  sec  5.97 MBytes  50.0 Mbits/sec    0    356 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  63.0 MBytes  52.8 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  61.0 MBytes  51.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 71929 bytes (233 packets)
    TX: 58387 bytes (272 packets)
    signal: -49 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 390.0 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">1.67</span> Mbits/sec | <span style="font-size: 1.5rem;">7.02</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 37883 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   1.00-2.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   2.00-3.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   3.00-4.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   4.00-5.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   5.00-6.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   6.00-7.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   7.00-8.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   8.00-9.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   9.00-10.00  sec   128 KBytes  1.05 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.07  sec  2.00 MBytes  1.67 Mbits/sec   70             sender
    [  5]   0.00-10.00  sec  1.62 MBytes  1.36 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 34509 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.00 MBytes  8.39 Mbits/sec    0   72.1 KBytes       
    [  5]   1.00-2.00   sec   640 KBytes  5.24 Mbits/sec    0   91.9 KBytes       
    [  5]   2.00-3.00   sec   512 KBytes  4.19 Mbits/sec    2   74.9 KBytes       
    [  5]   3.00-4.00   sec   768 KBytes  6.29 Mbits/sec    4   60.8 KBytes       
    [  5]   4.00-5.00   sec  1.00 MBytes  8.39 Mbits/sec    0   67.9 KBytes       
    [  5]   5.00-6.00   sec  1.00 MBytes  8.39 Mbits/sec    0   79.2 KBytes       
    [  5]   6.00-7.00   sec  1.00 MBytes  8.39 Mbits/sec    0   87.7 KBytes       
    [  5]   7.00-8.00   sec   768 KBytes  6.29 Mbits/sec    0   94.7 KBytes       
    [  5]   8.00-9.00   sec   768 KBytes  6.29 Mbits/sec    0   99.0 KBytes       
    [  5]   9.00-10.00  sec  1.00 MBytes  8.39 Mbits/sec    0    105 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  8.38 MBytes  7.02 Mbits/sec    6             sender
    [  5]   0.00-10.01  sec  7.88 MBytes  6.60 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 77372 bytes (326 packets)
    TX: 55018 bytes (212 packets)
    signal: -27 dBm
    rx bitrate: 19.5 MBit/s MCS 2
    tx bitrate: 43.3 MBit/s MCS 4 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">97.1</span> Mbits/sec | <span style="font-size: 1.5rem;">66.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 59789 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.6 MBytes  89.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.6 MBytes  97.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   116 MBytes  97.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   113 MBytes  95.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 35513 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.50 MBytes  71.2 Mbits/sec    0    212 KBytes       
    [  5]   1.00-2.00   sec  8.12 MBytes  68.2 Mbits/sec    0    238 KBytes       
    [  5]   2.00-3.00   sec  8.25 MBytes  69.2 Mbits/sec    0    266 KBytes       
    [  5]   3.00-4.00   sec  7.88 MBytes  66.1 Mbits/sec    0    266 KBytes       
    [  5]   4.00-5.00   sec  7.75 MBytes  65.0 Mbits/sec    0    266 KBytes       
    [  5]   5.00-6.00   sec  7.75 MBytes  65.0 Mbits/sec    0    288 KBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0    308 KBytes       
    [  5]   7.00-8.00   sec  8.00 MBytes  67.1 Mbits/sec    0    308 KBytes       
    [  5]   8.00-9.00   sec  8.12 MBytes  68.2 Mbits/sec    0    308 KBytes       
    [  5]   9.00-10.00  sec  7.62 MBytes  63.9 Mbits/sec    0    308 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  79.5 MBytes  66.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  78.1 MBytes  65.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 93032 bytes (393 packets)
    TX: 56586 bytes (251 packets)
    signal: -28 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">35.6</span> Mbits/sec | <span style="font-size: 1.5rem;">25.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 35365 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.12 MBytes  34.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.21  sec  43.4 MBytes  35.6 Mbits/sec   61             sender
    [  5]   0.00-10.00  sec  40.5 MBytes  34.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 60575 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.88 MBytes  32.5 Mbits/sec    0    182 KBytes       
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec    0    250 KBytes       
    [  5]   2.00-3.00   sec  2.88 MBytes  24.1 Mbits/sec    0    260 KBytes       
    [  5]   3.00-4.00   sec  3.00 MBytes  25.2 Mbits/sec    0    288 KBytes       
    [  5]   4.00-5.00   sec  3.12 MBytes  26.2 Mbits/sec    0    303 KBytes       
    [  5]   5.00-6.00   sec  2.62 MBytes  22.0 Mbits/sec    0    322 KBytes       
    [  5]   6.00-7.00   sec  3.38 MBytes  28.3 Mbits/sec    0    322 KBytes       
    [  5]   7.00-8.00   sec  2.75 MBytes  23.1 Mbits/sec    0    322 KBytes       
    [  5]   8.00-9.00   sec  2.75 MBytes  23.1 Mbits/sec    0    322 KBytes       
    [  5]   9.00-10.00  sec  2.75 MBytes  23.1 Mbits/sec    0    322 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  30.4 MBytes  25.5 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  28.9 MBytes  24.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 68442 bytes (219 packets)
    TX: 52950 bytes (201 packets)
    signal: -38 dBm
    rx bitrate: 52.0 MBit/s MCS 5
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">38.4</span> Mbits/sec | <span style="font-size: 1.5rem;">42.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.122 port 41427 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.39 MBytes  45.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.11 MBytes  42.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.99 MBytes  41.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.00 MBytes  25.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.24 MBytes  35.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  3.98 MBytes  33.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.61 MBytes  21.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.26 MBytes  35.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.08 MBytes  42.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.00 MBytes  42.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.12  sec  46.4 MBytes  38.4 Mbits/sec    5             sender
    [  5]   0.00-10.00  sec  43.7 MBytes  36.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.122 port 35229 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.24 MBytes  43.9 Mbits/sec    0    296 KBytes       
    [  5]   1.00-2.00   sec  5.41 MBytes  45.4 Mbits/sec    0    348 KBytes       
    [  5]   2.00-3.00   sec  5.03 MBytes  42.2 Mbits/sec    0    365 KBytes       
    [  5]   3.00-4.00   sec  5.41 MBytes  45.4 Mbits/sec    0    365 KBytes       
    [  5]   4.00-5.00   sec  5.22 MBytes  43.8 Mbits/sec    0    386 KBytes       
    [  5]   5.00-6.00   sec  4.78 MBytes  40.1 Mbits/sec    0    386 KBytes       
    [  5]   6.00-7.00   sec  4.35 MBytes  36.5 Mbits/sec    0    386 KBytes       
    [  5]   7.00-8.00   sec  4.78 MBytes  40.1 Mbits/sec    0    386 KBytes       
    [  5]   8.00-9.00   sec  5.22 MBytes  43.8 Mbits/sec    0    413 KBytes       
    [  5]   9.00-10.00  sec  5.22 MBytes  43.8 Mbits/sec    0    413 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  50.7 MBytes  42.5 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  49.8 MBytes  41.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">27.7</span> Mbits/sec | <span style="font-size: 1.5rem;">34.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 53555 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.00 MBytes  25.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.75 MBytes  23.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.62 MBytes  22.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.38 MBytes  19.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.12 MBytes  26.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.75 MBytes  23.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.62 MBytes  30.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  33.0 MBytes  27.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  29.8 MBytes  25.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 59913 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.25 MBytes  44.0 Mbits/sec    0    236 KBytes       
    [  5]   1.00-2.00   sec  4.12 MBytes  34.6 Mbits/sec    0    311 KBytes       
    [  5]   2.00-3.00   sec  4.25 MBytes  35.7 Mbits/sec    0    395 KBytes       
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec    0    419 KBytes       
    [  5]   4.00-5.00   sec  4.25 MBytes  35.7 Mbits/sec    0    419 KBytes       
    [  5]   5.00-6.00   sec  3.62 MBytes  30.4 Mbits/sec    0    443 KBytes       
    [  5]   6.00-7.00   sec  4.50 MBytes  37.7 Mbits/sec    0    443 KBytes       
    [  5]   7.00-8.00   sec  3.50 MBytes  29.4 Mbits/sec    0    443 KBytes       
    [  5]   8.00-9.00   sec  3.62 MBytes  30.4 Mbits/sec    0    443 KBytes       
    [  5]   9.00-10.00  sec  3.62 MBytes  30.4 Mbits/sec    0    443 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  41.0 MBytes  34.4 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  39.0 MBytes  32.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 74872 bytes (275 packets)
    TX: 51812 bytes (203 packets)
    signal: -34 dBm
    rx bitrate: 52.0 MBit/s MCS 5
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.154, 6.12.30-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">144</span> Mbits/sec | <span style="font-size: 1.5rem;">141</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.121 port 44349 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.3 MBytes   145 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.1 MBytes   143 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.1 MBytes   143 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   171 MBytes   144 Mbits/sec   64             sender
    [  5]   0.00-10.00  sec   169 MBytes   141 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.121 port 40027 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.2 MBytes   161 Mbits/sec    0    488 KBytes       
    [  5]   1.00-2.00   sec  16.2 MBytes   136 Mbits/sec    0    488 KBytes       
    [  5]   2.00-3.00   sec  17.0 MBytes   143 Mbits/sec    0    488 KBytes       
    [  5]   3.00-4.00   sec  16.2 MBytes   136 Mbits/sec    0    488 KBytes       
    [  5]   4.00-5.00   sec  16.0 MBytes   134 Mbits/sec    0    488 KBytes       
    [  5]   5.00-6.00   sec  17.0 MBytes   143 Mbits/sec    0    488 KBytes       
    [  5]   6.00-7.00   sec  16.2 MBytes   136 Mbits/sec    0    488 KBytes       
    [  5]   7.00-8.00   sec  17.2 MBytes   144 Mbits/sec    0    488 KBytes       
    [  5]   8.00-9.00   sec  16.0 MBytes   134 Mbits/sec    0    488 KBytes       
    [  5]   9.00-10.00  sec  17.2 MBytes   144 Mbits/sec    0    488 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   168 MBytes   141 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   166 MBytes   139 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 65759899 bytes (66226 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">18.0</span> Mbits/sec | <span style="font-size: 1.5rem;">9.53</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.117 port 49029 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.56 MBytes  13.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.91 MBytes  16.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.69 MBytes  14.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.89 MBytes  15.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.93 MBytes  16.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.98 MBytes  16.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.02 MBytes  16.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.13 MBytes  17.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.31 MBytes  19.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.21 MBytes  18.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.34  sec  22.2 MBytes  18.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  19.6 MBytes  16.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.117 port 45759 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.17 MBytes  9.81 Mbits/sec    0   97.6 KBytes       
    [  5]   1.00-2.00   sec  1.24 MBytes  10.4 Mbits/sec    0    106 KBytes       
    [  5]   2.00-3.00   sec  1.12 MBytes  9.38 Mbits/sec    0    110 KBytes       
    [  5]   3.00-4.00   sec  1.24 MBytes  10.4 Mbits/sec    0    110 KBytes       
    [  5]   4.00-5.00   sec  1.12 MBytes  9.38 Mbits/sec    0    110 KBytes       
    [  5]   5.00-6.00   sec  1.12 MBytes  9.38 Mbits/sec    0    110 KBytes       
    [  5]   6.00-7.00   sec  1018 KBytes  8.34 Mbits/sec    0    110 KBytes       
    [  5]   7.00-8.00   sec  1018 KBytes  8.34 Mbits/sec    0    110 KBytes       
    [  5]   8.00-9.00   sec  1.12 MBytes  9.38 Mbits/sec    0    110 KBytes       
    [  5]   9.00-10.00  sec  1.24 MBytes  10.4 Mbits/sec    0    110 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  11.4 MBytes  9.53 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  11.0 MBytes  9.19 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 50996 bytes (139 packets)
    TX: 60764 bytes (246 packets)
    signal: -30 dBm
    rx bitrate: 6.0 MBit/s
    tx bitrate: 65.0 MBit/s MCS 7
    
    ```

## Failed Devices

| | Commercial Name | Chip | Class |
|:---:|:-----|:--------|:------|
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AIC8800.png height=64> | AIC8800 | AIC8800 | AX |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png height=64> | Atheros AR9271 | AR9271 | N |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8852AU.png height=64> | BrosTrend 1800 | RTL8852AU | AXE3000 |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7925.png height=64> | Mediatek MT7925 | MT7925 | AX |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7925E.png height=64> | Mediatek MT7925E #1 | MT7925E | AX |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7925E.png height=64> | Mediatek MT7925E #2 | MT7925E | AX |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7601U.png height=64> | Ralink MT7601U | MT7601U |  |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png height=64> | Realtek 8188EU | RTL8192CU | N |
|<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png height=64> | Realtek 8814AU | RTL8814AU | AC |
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
