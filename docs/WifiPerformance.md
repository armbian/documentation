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
**Test Date:** [2025-05-17 09:11 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15083353311)
### AC

#### BCM4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">51.9</span> Mbits/sec | <span style="font-size: 1.5rem;">59.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 52923 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.74 MBytes  48.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.94 MBytes  49.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.00 MBytes  50.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.94 MBytes  49.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.83 MBytes  48.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.00 MBytes  50.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.93 MBytes  49.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.05 MBytes  50.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.79 MBytes  48.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.87 MBytes  49.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  62.0 MBytes  51.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  59.1 MBytes  49.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 54891 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.10 MBytes  68.0 Mbits/sec    0    421 KBytes       
    [  5]   1.00-2.00   sec  8.52 MBytes  71.5 Mbits/sec    0    662 KBytes       
    [  5]   2.00-3.00   sec  6.25 MBytes  52.4 Mbits/sec    0    783 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0    885 KBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.03 MBytes       
    [  5]   5.00-6.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.08 MBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.24 MBytes       
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.24 MBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.24 MBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.34 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  70.4 MBytes  59.0 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  68.8 MBytes  57.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 161564 bytes (418 packets)
    TX: 94560 bytes (533 packets)
    signal: -26 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">116</span> Mbits/sec | <span style="font-size: 1.5rem;">108</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 33961 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.4 MBytes   113 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.4 MBytes   113 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.6 MBytes   114 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   138 MBytes   116 Mbits/sec   85             sender
    [  5]   0.00-10.00  sec   136 MBytes   114 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 35053 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  13.4 MBytes   112 Mbits/sec    0    494 KBytes       
    [  5]   1.00-2.00   sec  12.9 MBytes   108 Mbits/sec    0    635 KBytes       
    [  5]   2.00-3.00   sec  12.6 MBytes   106 Mbits/sec    0    666 KBytes       
    [  5]   3.00-4.00   sec  12.6 MBytes   105 Mbits/sec    0    699 KBytes       
    [  5]   4.00-5.00   sec  13.3 MBytes   112 Mbits/sec    0    789 KBytes       
    [  5]   5.00-6.00   sec  12.6 MBytes   105 Mbits/sec    0    789 KBytes       
    [  5]   6.00-7.00   sec  12.7 MBytes   107 Mbits/sec    0    830 KBytes       
    [  5]   7.00-8.00   sec  13.0 MBytes   109 Mbits/sec    0    830 KBytes       
    [  5]   8.00-9.00   sec  13.1 MBytes   110 Mbits/sec    0    830 KBytes       
    [  5]   9.00-10.00  sec  12.7 MBytes   106 Mbits/sec    0    881 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   129 MBytes   108 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   127 MBytes   106 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 107360 bytes (459 packets)
    TX: 55731 bytes (225 packets)
    signal: -38 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">155</span> Mbits/sec | <span style="font-size: 1.5rem;">270</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 57209 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  14.9 MBytes   125 Mbits/sec                  
    [  5]   1.00-2.00   sec  15.2 MBytes   128 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   7.00-8.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.1 MBytes   160 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.9 MBytes   158 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   184 MBytes   155 Mbits/sec   28             sender
    [  5]   0.00-10.00  sec   182 MBytes   152 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 52477 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.6 MBytes   290 Mbits/sec    0   1.11 MBytes       
    [  5]   1.00-2.00   sec  31.5 MBytes   264 Mbits/sec    0   1.25 MBytes       
    [  5]   2.00-3.00   sec  33.0 MBytes   277 Mbits/sec    0   1.32 MBytes       
    [  5]   3.00-4.00   sec  31.5 MBytes   264 Mbits/sec    0   1.32 MBytes       
    [  5]   4.00-5.00   sec  31.5 MBytes   264 Mbits/sec    0   1.32 MBytes       
    [  5]   5.00-6.00   sec  32.8 MBytes   275 Mbits/sec    0   1.32 MBytes       
    [  5]   6.00-7.00   sec  31.5 MBytes   264 Mbits/sec    0   1.32 MBytes       
    [  5]   7.00-8.00   sec  32.8 MBytes   275 Mbits/sec    0   1.32 MBytes       
    [  5]   8.00-9.00   sec  31.5 MBytes   264 Mbits/sec    0   1.32 MBytes       
    [  5]   9.00-10.00  sec  31.5 MBytes   264 Mbits/sec    0   1.39 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   322 MBytes   270 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   320 MBytes   268 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 193454 bytes (352 packets)
    TX: 103902 bytes (471 packets)
    signal: -34 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">152</span> Mbits/sec | <span style="font-size: 1.5rem;">197</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 40819 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.9 MBytes   150 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec   182 MBytes   152 Mbits/sec   58             sender
    [  5]   0.00-10.00  sec   178 MBytes   150 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 59951 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.6 MBytes   215 Mbits/sec    0    663 KBytes       
    [  5]   1.00-2.00   sec  23.5 MBytes   197 Mbits/sec    0    747 KBytes       
    [  5]   2.00-3.00   sec  22.2 MBytes   187 Mbits/sec    0    747 KBytes       
    [  5]   3.00-4.00   sec  23.6 MBytes   198 Mbits/sec    0    786 KBytes       
    [  5]   4.00-5.00   sec  23.6 MBytes   198 Mbits/sec    0    786 KBytes       
    [  5]   5.00-6.00   sec  23.5 MBytes   197 Mbits/sec    0    786 KBytes       
    [  5]   6.00-7.00   sec  23.6 MBytes   198 Mbits/sec    0    786 KBytes       
    [  5]   7.00-8.00   sec  23.6 MBytes   198 Mbits/sec    0    786 KBytes       
    [  5]   8.00-9.00   sec  22.2 MBytes   187 Mbits/sec    0    830 KBytes       
    [  5]   9.00-10.00  sec  23.8 MBytes   199 Mbits/sec    0    830 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   235 MBytes   197 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   232 MBytes   195 Mbits/sec                  receiver
    
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
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">66.2</span> Mbits/sec | <span style="font-size: 1.5rem;">99.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 57517 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.75 MBytes  56.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  7.88 MBytes  66.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  7.88 MBytes  66.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  7.12 MBytes  59.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  8.00 MBytes  67.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  7.75 MBytes  65.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  7.50 MBytes  62.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  79.0 MBytes  66.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  75.8 MBytes  63.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 60219 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  11.5 MBytes  96.4 Mbits/sec    0    510 KBytes       
    [  5]   1.00-2.00   sec  12.2 MBytes   103 Mbits/sec    0    626 KBytes       
    [  5]   2.00-3.00   sec  11.1 MBytes  93.3 Mbits/sec    0    691 KBytes       
    [  5]   3.00-4.00   sec  13.1 MBytes   110 Mbits/sec    0    817 KBytes       
    [  5]   4.00-5.00   sec  11.4 MBytes  95.4 Mbits/sec    0    861 KBytes       
    [  5]   5.00-6.00   sec  12.9 MBytes   108 Mbits/sec    0    861 KBytes       
    [  5]   6.00-7.00   sec  10.2 MBytes  86.0 Mbits/sec    0    911 KBytes       
    [  5]   7.00-8.00   sec  13.1 MBytes   110 Mbits/sec    0    976 KBytes       
    [  5]   8.00-9.00   sec  11.5 MBytes  96.5 Mbits/sec    0    976 KBytes       
    [  5]   9.00-10.00  sec  11.1 MBytes  93.3 Mbits/sec    0   1.00 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   118 MBytes  99.2 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   116 MBytes  96.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    signal: -41 dBm
    tx bitrate: 174.0 MBit/s
    ```

#### Realtek 8822CE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8822CE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.21-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">467</span> Mbits/sec | <span style="font-size: 1.5rem;">574</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 44753 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  59.0 MBytes   495 Mbits/sec                  
    [  5]   1.00-2.00   sec  66.6 MBytes   559 Mbits/sec                  
    [  5]   2.00-3.00   sec  37.5 MBytes   315 Mbits/sec                  
    [  5]   3.00-4.00   sec  34.3 MBytes   287 Mbits/sec                  
    [  5]   4.00-5.00   sec  58.0 MBytes   486 Mbits/sec                  
    [  5]   5.00-6.00   sec  65.6 MBytes   550 Mbits/sec                  
    [  5]   6.00-7.00   sec  47.1 MBytes   395 Mbits/sec                  
    [  5]   7.00-8.00   sec  47.4 MBytes   397 Mbits/sec                  
    [  5]   8.00-9.00   sec  65.8 MBytes   552 Mbits/sec                  
    [  5]   9.00-10.00  sec  73.1 MBytes   613 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   557 MBytes   467 Mbits/sec   25             sender
    [  5]   0.00-10.00  sec   554 MBytes   465 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 51477 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  74.2 MBytes   623 Mbits/sec  116   1.09 MBytes       
    [  5]   1.00-2.00   sec  72.5 MBytes   608 Mbits/sec    0   1.18 MBytes       
    [  5]   2.00-3.00   sec  65.0 MBytes   545 Mbits/sec   92    720 KBytes       
    [  5]   3.00-4.00   sec  65.0 MBytes   545 Mbits/sec    0    841 KBytes       
    [  5]   4.00-5.00   sec  70.0 MBytes   586 Mbits/sec    0    953 KBytes       
    [  5]   5.00-6.00   sec  71.2 MBytes   599 Mbits/sec    0   1.03 MBytes       
    [  5]   6.00-7.00   sec  70.0 MBytes   587 Mbits/sec   54    590 KBytes       
    [  5]   7.00-8.00   sec  62.5 MBytes   524 Mbits/sec    0    728 KBytes       
    [  5]   8.00-9.00   sec  67.5 MBytes   566 Mbits/sec    0    851 KBytes       
    [  5]   9.00-10.00  sec  66.2 MBytes   556 Mbits/sec   49    513 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   684 MBytes   574 Mbits/sec  311             sender
    [  5]   0.00-10.00  sec   681 MBytes   571 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 151417 bytes (552 packets)
    TX: 62719 bytes (237 packets)
    signal: -30 dBm
    rx bitrate: 702.0 MBit/s VHT-MCS 8 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">193</span> Mbits/sec | <span style="font-size: 1.5rem;">130</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 37731 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   1.00-2.00   sec  22.6 MBytes   190 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   3.00-4.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   4.00-5.00   sec  22.9 MBytes   192 Mbits/sec                  
    [  5]   5.00-6.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   6.00-7.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   7.00-8.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   8.00-9.00   sec  23.1 MBytes   194 Mbits/sec                  
    [  5]   9.00-10.00  sec  23.2 MBytes   195 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   230 MBytes   193 Mbits/sec  141             sender
    [  5]   0.00-10.00  sec   227 MBytes   190 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 55437 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  17.5 MBytes   147 Mbits/sec    0   2.54 MBytes       
    [  5]   1.00-2.00   sec  16.1 MBytes   135 Mbits/sec    0   3.14 MBytes       
    [  5]   2.00-3.00   sec  14.6 MBytes   123 Mbits/sec    0   3.23 MBytes       
    [  5]   3.00-4.00   sec  15.0 MBytes   126 Mbits/sec    0   3.23 MBytes       
    [  5]   4.00-5.00   sec  14.0 MBytes   117 Mbits/sec    0   3.40 MBytes       
    [  5]   5.00-6.00   sec  16.6 MBytes   139 Mbits/sec    0   3.40 MBytes       
    [  5]   6.00-7.00   sec  15.1 MBytes   127 Mbits/sec    0   3.40 MBytes       
    [  5]   7.00-8.00   sec  13.5 MBytes   113 Mbits/sec    0   3.45 MBytes       
    [  5]   8.00-9.00   sec  16.1 MBytes   135 Mbits/sec    0   3.45 MBytes       
    [  5]   9.00-10.00  sec  16.6 MBytes   139 Mbits/sec    0   3.45 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   155 MBytes   130 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec   152 MBytes   127 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 35636 bytes (144 packets)
    TX: 53094 bytes (200 packets)
    signal: -22 dBm
    rx bitrate: 172.0 MBit/s HE-MCS 7 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 58.5 MBit/s HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### BCM 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">52.4</span> Mbits/sec | <span style="font-size: 1.5rem;">53.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 49781 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.67 MBytes  55.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.70 MBytes  47.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.82 MBytes  48.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.28 MBytes  52.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.45 MBytes  54.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.07 MBytes  50.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.54 MBytes  54.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.98 MBytes  50.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.08 MBytes  42.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.61 MBytes  47.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  62.6 MBytes  52.4 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec  60.2 MBytes  50.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 40579 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.62 MBytes  72.3 Mbits/sec    0    281 KBytes       
    [  5]   1.00-2.00   sec  5.84 MBytes  49.0 Mbits/sec    0    281 KBytes       
    [  5]   2.00-3.00   sec  5.90 MBytes  49.5 Mbits/sec    0    281 KBytes       
    [  5]   3.00-4.00   sec  6.28 MBytes  52.7 Mbits/sec    0    281 KBytes       
    [  5]   4.00-5.00   sec  6.28 MBytes  52.6 Mbits/sec    0    296 KBytes       
    [  5]   5.00-6.00   sec  6.46 MBytes  54.2 Mbits/sec    0    315 KBytes       
    [  5]   6.00-7.00   sec  6.09 MBytes  51.1 Mbits/sec    0    329 KBytes       
    [  5]   7.00-8.00   sec  6.21 MBytes  52.2 Mbits/sec    0    329 KBytes       
    [  5]   8.00-9.00   sec  6.15 MBytes  51.5 Mbits/sec    0    329 KBytes       
    [  5]   9.00-10.00  sec  6.15 MBytes  51.6 Mbits/sec    0    329 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  64.0 MBytes  53.7 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  62.4 MBytes  52.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 51657 bytes (181 packets)
    TX: 57244 bytes (223 packets)
    signal: -53 dBm
    rx bitrate: 390.0 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">48.6</span> Mbits/sec | <span style="font-size: 1.5rem;">47.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 34343 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  2.22 MBytes  18.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.23 MBytes  52.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.09 MBytes  51.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.19 MBytes  52.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.27 MBytes  52.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.07 MBytes  50.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.89 MBytes  49.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.73 MBytes  48.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.24 MBytes  52.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  58.0 MBytes  48.6 Mbits/sec    4             sender
    [  5]   0.00-10.00  sec  56.4 MBytes  47.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 56485 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.48 MBytes  54.4 Mbits/sec    0    315 KBytes       
    [  5]   1.00-2.00   sec  5.59 MBytes  46.9 Mbits/sec    0    351 KBytes       
    [  5]   2.00-3.00   sec  5.59 MBytes  46.9 Mbits/sec    0    370 KBytes       
    [  5]   3.00-4.00   sec  6.09 MBytes  51.1 Mbits/sec    0    414 KBytes       
    [  5]   4.00-5.00   sec  5.28 MBytes  44.3 Mbits/sec    0    414 KBytes       
    [  5]   5.00-6.00   sec  5.65 MBytes  47.4 Mbits/sec    0    414 KBytes       
    [  5]   6.00-7.00   sec  5.22 MBytes  43.8 Mbits/sec    0    414 KBytes       
    [  5]   7.00-8.00   sec  5.72 MBytes  48.0 Mbits/sec    0    414 KBytes       
    [  5]   8.00-9.00   sec  5.78 MBytes  48.5 Mbits/sec    0    414 KBytes       
    [  5]   9.00-10.00  sec  5.65 MBytes  47.4 Mbits/sec    0    414 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  57.1 MBytes  47.9 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  56.1 MBytes  46.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">143</span> Mbits/sec | <span style="font-size: 1.5rem;">139</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 56665 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  14.7 MBytes   124 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.2 MBytes   144 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   5.00-6.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.1 MBytes   143 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.0 MBytes   142 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   171 MBytes   143 Mbits/sec  346             sender
    [  5]   0.00-10.00  sec   168 MBytes   141 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 44537 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.3 MBytes   154 Mbits/sec    0    392 KBytes       
    [  5]   1.00-2.00   sec  16.3 MBytes   137 Mbits/sec    0    392 KBytes       
    [  5]   2.00-3.00   sec  16.3 MBytes   137 Mbits/sec    0    392 KBytes       
    [  5]   3.00-4.00   sec  16.3 MBytes   137 Mbits/sec    0    392 KBytes       
    [  5]   4.00-5.00   sec  16.3 MBytes   137 Mbits/sec    0    392 KBytes       
    [  5]   5.00-6.00   sec  16.5 MBytes   139 Mbits/sec    0    392 KBytes       
    [  5]   6.00-7.00   sec  16.4 MBytes   138 Mbits/sec    0    392 KBytes       
    [  5]   7.00-8.00   sec  16.5 MBytes   138 Mbits/sec    0    392 KBytes       
    [  5]   8.00-9.00   sec  16.3 MBytes   137 Mbits/sec    0    392 KBytes       
    [  5]   9.00-10.00  sec  16.4 MBytes   138 Mbits/sec    0    392 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   166 MBytes   139 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   164 MBytes   138 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 71720394 bytes (72395 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">17.5</span> Mbits/sec | <span style="font-size: 1.5rem;">12.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 53261 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.48 MBytes  12.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.20 MBytes  10.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.38 MBytes  11.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.82 MBytes  15.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.66 MBytes  13.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.05 MBytes  17.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  1.95 MBytes  16.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.09 MBytes  17.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.53 MBytes  21.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.24 MBytes  18.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.11  sec  21.1 MBytes  17.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  18.4 MBytes  15.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 34805 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.61 MBytes  13.5 Mbits/sec    0   53.7 KBytes       
    [  5]   1.00-2.00   sec  1.55 MBytes  13.0 Mbits/sec    1   84.8 KBytes       
    [  5]   2.00-3.00   sec  1.37 MBytes  11.5 Mbits/sec    3   35.4 KBytes       
    [  5]   3.00-4.00   sec  1.55 MBytes  13.0 Mbits/sec    1   67.9 KBytes       
    [  5]   4.00-5.00   sec  1.49 MBytes  12.5 Mbits/sec    0   83.4 KBytes       
    [  5]   5.00-6.00   sec  1.37 MBytes  11.5 Mbits/sec    0   93.3 KBytes       
    [  5]   6.00-7.00   sec  1.49 MBytes  12.5 Mbits/sec    0   99.0 KBytes       
    [  5]   7.00-8.00   sec  1.18 MBytes  9.90 Mbits/sec    1   73.5 KBytes       
    [  5]   8.00-9.00   sec  1.49 MBytes  12.5 Mbits/sec    2   66.5 KBytes       
    [  5]   9.00-10.00  sec  1.49 MBytes  12.5 Mbits/sec    1   65.0 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  14.6 MBytes  12.2 Mbits/sec    9             sender
    [  5]   0.00-10.03  sec  14.2 MBytes  11.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 42040 bytes (137 packets)
    TX: 57457 bytes (241 packets)
    signal: -31 dBm
    rx bitrate: 6.0 MBit/s
    tx bitrate: 52.0 MBit/s MCS 5
    
    ```
<!-- DUT-STOP -->

## Contribute

- Assist us in developing and maintaining our testing system: Your expertise can help us enhance and optimize [our test infrastructure](https://github.com/armbian/armbian.github.io/actions/workflows/usb-wireless-autotest.yml). By contributing your skills, you can play a key role in ensuring the accuracy and reliability of our test results.

- Donate hardware: Your contribution of new hardware, whether it’s a wireless adapter or any other equipment, helps us expand our testing capabilities. We’re specifically looking for [new wireless adapters](https://www.amazon.de/hz/wishlist/ls/1GA17IGQ2MF0V?ref_=wl_share) that haven’t yet been added to our system. Your donation can directly impact the scope and depth of our tests.

- Join our team: Become part of our passionate and dedicated team. We’re looking for [individuals who share our vision and are eager to contribute to the development of innovative testing solutions](https://forum.armbian.com/staffapplications/). Whether you have technical expertise or simply a willingness to learn, there’s a place for you here!

## Other resources

- [USB WiFi Adapter Information for Linux](https://github.com/morrownr/USB-WiFi)
- [Official Linux Wireless documentation](https://wireless.docs.kernel.org/en/latest/index.html)
- [Armbian forum - Advanced users - Development](https://forum.armbian.com/forum/4-advanced-users-development/)
