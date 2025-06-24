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
**Test Date:** [2025-06-24 21:36 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15861296244)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">48.7</span> Mbits/sec | <span style="font-size: 1.5rem;">56.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.129 port 60179 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.44 MBytes  45.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.37 MBytes  45.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.61 MBytes  47.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.40 MBytes  45.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.45 MBytes  45.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.55 MBytes  46.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.45 MBytes  45.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.44 MBytes  45.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.48 MBytes  46.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.32 MBytes  44.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  58.1 MBytes  48.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  54.5 MBytes  45.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.129 port 47535 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.93 MBytes  66.5 Mbits/sec    0    400 KBytes       
    [  5]   1.00-2.00   sec  7.57 MBytes  63.5 Mbits/sec    0    701 KBytes       
    [  5]   2.00-3.00   sec  6.25 MBytes  52.4 Mbits/sec    0    945 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.11 MBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.17 MBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.17 MBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.24 MBytes       
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.32 MBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.32 MBytes       
    [  5]   9.00-10.00  sec  5.00 MBytes  41.9 Mbits/sec    0   1.42 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  66.8 MBytes  56.0 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  64.5 MBytes  54.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 153177 bytes (417 packets)
    TX: 84094 bytes (526 packets)
    signal: -27 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">111</span> Mbits/sec | <span style="font-size: 1.5rem;">99.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 50189 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.4 MBytes   104 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.7 MBytes   107 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   3.00-4.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.3 MBytes   112 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec   133 MBytes   111 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   130 MBytes   109 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 34817 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.7 MBytes   106 Mbits/sec    0    482 KBytes       
    [  5]   1.00-2.00   sec  11.7 MBytes  98.5 Mbits/sec    0    536 KBytes       
    [  5]   2.00-3.00   sec  11.6 MBytes  97.0 Mbits/sec    0    536 KBytes       
    [  5]   3.00-4.00   sec  11.2 MBytes  93.8 Mbits/sec    0    564 KBytes       
    [  5]   4.00-5.00   sec  12.1 MBytes   102 Mbits/sec    0    592 KBytes       
    [  5]   5.00-6.00   sec  12.1 MBytes   102 Mbits/sec    0    592 KBytes       
    [  5]   6.00-7.00   sec  11.7 MBytes  98.0 Mbits/sec    0    622 KBytes       
    [  5]   7.00-8.00   sec  11.7 MBytes  98.5 Mbits/sec    0    655 KBytes       
    [  5]   8.00-9.00   sec  10.9 MBytes  91.7 Mbits/sec    0    655 KBytes       
    [  5]   9.00-10.00  sec  12.6 MBytes   105 Mbits/sec    0    740 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   118 MBytes  99.2 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   116 MBytes  97.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 122276 bytes (530 packets)
    TX: 58981 bytes (233 packets)
    signal: -33 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">162</span> Mbits/sec | <span style="font-size: 1.5rem;">254</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 44113 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   1.00-2.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   5.00-6.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   9.00-10.00  sec  19.4 MBytes   163 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   193 MBytes   162 Mbits/sec   62             sender
    [  5]   0.00-10.00  sec   190 MBytes   159 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 45145 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  23.9 MBytes   200 Mbits/sec    0    597 KBytes       
    [  5]   1.00-2.00   sec  25.0 MBytes   210 Mbits/sec    0    641 KBytes       
    [  5]   2.00-3.00   sec  30.1 MBytes   253 Mbits/sec    0    731 KBytes       
    [  5]   3.00-4.00   sec  30.4 MBytes   255 Mbits/sec    0    819 KBytes       
    [  5]   4.00-5.00   sec  32.9 MBytes   276 Mbits/sec    0   1.11 MBytes       
    [  5]   5.00-6.00   sec  31.5 MBytes   264 Mbits/sec    0   1.24 MBytes       
    [  5]   6.00-7.00   sec  33.0 MBytes   277 Mbits/sec    0   1.24 MBytes       
    [  5]   7.00-8.00   sec  31.5 MBytes   264 Mbits/sec    0   1.31 MBytes       
    [  5]   8.00-9.00   sec  32.9 MBytes   276 Mbits/sec    0   1.31 MBytes       
    [  5]   9.00-10.00  sec  31.5 MBytes   264 Mbits/sec    0   1.31 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   303 MBytes   254 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   300 MBytes   251 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 192430 bytes (449 packets)
    TX: 94263 bytes (472 packets)
    signal: -36 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">154</span> Mbits/sec | <span style="font-size: 1.5rem;">187</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 42939 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.4 MBytes   146 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.04  sec   184 MBytes   154 Mbits/sec    2             sender
    [  5]   0.00-10.00  sec   181 MBytes   152 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 33483 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  24.9 MBytes   208 Mbits/sec    0    560 KBytes       
    [  5]   1.00-2.00   sec  24.4 MBytes   204 Mbits/sec    0    649 KBytes       
    [  5]   2.00-3.00   sec  23.4 MBytes   196 Mbits/sec    0    682 KBytes       
    [  5]   3.00-4.00   sec  22.4 MBytes   188 Mbits/sec    0    758 KBytes       
    [  5]   4.00-5.00   sec  19.4 MBytes   163 Mbits/sec    0    796 KBytes       
    [  5]   5.00-6.00   sec  22.2 MBytes   187 Mbits/sec    0    796 KBytes       
    [  5]   6.00-7.00   sec  20.8 MBytes   174 Mbits/sec    0    796 KBytes       
    [  5]   7.00-8.00   sec  22.4 MBytes   188 Mbits/sec    0    888 KBytes       
    [  5]   8.00-9.00   sec  20.9 MBytes   175 Mbits/sec    0    888 KBytes       
    [  5]   9.00-10.00  sec  22.2 MBytes   187 Mbits/sec    0    888 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   223 MBytes   187 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   220 MBytes   184 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -34 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">155</span> Mbits/sec | <span style="font-size: 1.5rem;">271</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 34871 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.1 MBytes   152 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec   185 MBytes   155 Mbits/sec   27             sender
    [  5]   0.00-10.00  sec   182 MBytes   152 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 38003 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.4 MBytes   288 Mbits/sec    0    827 KBytes       
    [  5]   1.00-2.00   sec  32.8 MBytes   275 Mbits/sec    0    913 KBytes       
    [  5]   2.00-3.00   sec  31.8 MBytes   266 Mbits/sec    0   1.24 MBytes       
    [  5]   3.00-4.00   sec  30.9 MBytes   259 Mbits/sec    0   1.30 MBytes       
    [  5]   4.00-5.00   sec  32.2 MBytes   271 Mbits/sec    0   1.38 MBytes       
    [  5]   5.00-6.00   sec  32.8 MBytes   275 Mbits/sec    0   1.38 MBytes       
    [  5]   6.00-7.00   sec  31.9 MBytes   267 Mbits/sec    0   1.38 MBytes       
    [  5]   7.00-8.00   sec  32.1 MBytes   269 Mbits/sec    0   1.46 MBytes       
    [  5]   8.00-9.00   sec  31.8 MBytes   266 Mbits/sec    0   1.46 MBytes       
    [  5]   9.00-10.00  sec  32.9 MBytes   276 Mbits/sec    0   1.53 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   323 MBytes   271 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   320 MBytes   268 Mbits/sec                  receiver
    
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
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">128</span> Mbits/sec | <span style="font-size: 1.5rem;">204</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 42251 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.50 MBytes  79.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.5 MBytes   138 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.2 MBytes   136 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   153 MBytes   128 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   152 MBytes   127 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 41903 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  26.6 MBytes   223 Mbits/sec    0    653 KBytes       
    [  5]   1.00-2.00   sec  24.4 MBytes   204 Mbits/sec    0    684 KBytes       
    [  5]   2.00-3.00   sec  23.4 MBytes   196 Mbits/sec    0    684 KBytes       
    [  5]   3.00-4.00   sec  24.8 MBytes   208 Mbits/sec    0    684 KBytes       
    [  5]   4.00-5.00   sec  24.8 MBytes   208 Mbits/sec    0    684 KBytes       
    [  5]   5.00-6.00   sec  23.2 MBytes   195 Mbits/sec    0    730 KBytes       
    [  5]   6.00-7.00   sec  24.9 MBytes   209 Mbits/sec    0    805 KBytes       
    [  5]   7.00-8.00   sec  23.5 MBytes   197 Mbits/sec    0    805 KBytes       
    [  5]   8.00-9.00   sec  23.5 MBytes   197 Mbits/sec    0    805 KBytes       
    [  5]   9.00-10.00  sec  23.6 MBytes   198 Mbits/sec    0    805 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   243 MBytes   204 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   240 MBytes   201 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 161315 bytes (301 packets)
    TX: 86481 bytes (434 packets)
    signal: -45 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">249</span> Mbits/sec | <span style="font-size: 1.5rem;">253</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 34501 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  24.0 MBytes   201 Mbits/sec                  
    [  5]   1.00-2.00   sec  30.2 MBytes   254 Mbits/sec                  
    [  5]   2.00-3.00   sec  29.6 MBytes   249 Mbits/sec                  
    [  5]   3.00-4.00   sec  30.1 MBytes   253 Mbits/sec                  
    [  5]   4.00-5.00   sec  29.5 MBytes   247 Mbits/sec                  
    [  5]   5.00-6.00   sec  29.9 MBytes   251 Mbits/sec                  
    [  5]   6.00-7.00   sec  29.6 MBytes   249 Mbits/sec                  
    [  5]   7.00-8.00   sec  29.8 MBytes   250 Mbits/sec                  
    [  5]   8.00-9.00   sec  29.8 MBytes   250 Mbits/sec                  
    [  5]   9.00-10.00  sec  30.6 MBytes   257 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   297 MBytes   249 Mbits/sec  367             sender
    [  5]   0.00-10.00  sec   293 MBytes   246 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 46187 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  30.0 MBytes   251 Mbits/sec    0   1.89 MBytes       
    [  5]   1.00-2.00   sec  30.8 MBytes   258 Mbits/sec    0   2.24 MBytes       
    [  5]   2.00-3.00   sec  30.2 MBytes   254 Mbits/sec    0   2.96 MBytes       
    [  5]   3.00-4.00   sec  30.2 MBytes   254 Mbits/sec    0   3.34 MBytes       
    [  5]   4.00-5.00   sec  28.4 MBytes   238 Mbits/sec    0   5.21 MBytes       
    [  5]   5.00-6.00   sec  31.2 MBytes   262 Mbits/sec    0   5.21 MBytes       
    [  5]   6.00-7.00   sec  29.9 MBytes   251 Mbits/sec    0   5.21 MBytes       
    [  5]   7.00-8.00   sec  29.9 MBytes   251 Mbits/sec    0   5.21 MBytes       
    [  5]   8.00-9.00   sec  30.5 MBytes   256 Mbits/sec    0   5.21 MBytes       
    [  5]   9.00-10.00  sec  30.4 MBytes   255 Mbits/sec    0   5.21 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   302 MBytes   253 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   299 MBytes   250 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">530</span> Mbits/sec | <span style="font-size: 1.5rem;">489</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 56217 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  68.5 MBytes   575 Mbits/sec                  
    [  5]   1.00-2.00   sec  64.3 MBytes   539 Mbits/sec                  
    [  5]   2.00-3.00   sec  65.1 MBytes   546 Mbits/sec                  
    [  5]   3.00-4.00   sec  65.4 MBytes   548 Mbits/sec                  
    [  5]   4.00-5.00   sec  67.0 MBytes   562 Mbits/sec                  
    [  5]   5.00-6.00   sec  59.9 MBytes   502 Mbits/sec                  
    [  5]   6.00-7.00   sec  59.7 MBytes   501 Mbits/sec                  
    [  5]   7.00-8.00   sec  59.9 MBytes   503 Mbits/sec                  
    [  5]   8.00-9.00   sec  59.1 MBytes   496 Mbits/sec                  
    [  5]   9.00-10.00  sec  60.5 MBytes   507 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   633 MBytes   530 Mbits/sec  504             sender
    [  5]   0.00-10.00  sec   629 MBytes   528 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 54397 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.01   sec  64.9 MBytes   539 Mbits/sec    0   5.28 MBytes       
    [  5]   1.01-2.01   sec  66.2 MBytes   556 Mbits/sec   11   2.64 MBytes       
    [  5]   2.01-3.00   sec  65.0 MBytes   550 Mbits/sec   23   1.37 MBytes       
    [  5]   3.00-4.00   sec  60.0 MBytes   503 Mbits/sec   59    766 KBytes       
    [  5]   4.00-5.00   sec  53.8 MBytes   451 Mbits/sec   36    488 KBytes       
    [  5]   5.00-6.00   sec  55.0 MBytes   461 Mbits/sec    0    631 KBytes       
    [  5]   6.00-7.00   sec  56.2 MBytes   472 Mbits/sec    0    749 KBytes       
    [  5]   7.00-8.00   sec  51.2 MBytes   430 Mbits/sec    4    481 KBytes       
    [  5]   8.00-9.00   sec  53.8 MBytes   451 Mbits/sec    0    621 KBytes       
    [  5]   9.00-10.00  sec  56.2 MBytes   472 Mbits/sec    0    740 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   582 MBytes   489 Mbits/sec  133             sender
    [  5]   0.00-10.01  sec   579 MBytes   486 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 129102 bytes (448 packets)
    TX: 56846 bytes (212 packets)
    signal: -34 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 585.1 MBit/s VHT-MCS 6 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Ampak 6275P

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AP6275P.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.149, 6.12.33-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AP6275P</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">343</span> Mbits/sec | <span style="font-size: 1.5rem;">301</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 40667 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  40.0 MBytes   336 Mbits/sec                  
    [  5]   1.00-2.00   sec  41.0 MBytes   344 Mbits/sec                  
    [  5]   2.00-3.00   sec  40.7 MBytes   341 Mbits/sec                  
    [  5]   3.00-4.00   sec  38.5 MBytes   323 Mbits/sec                  
    [  5]   4.00-5.00   sec  40.9 MBytes   343 Mbits/sec                  
    [  5]   5.00-6.00   sec  43.1 MBytes   362 Mbits/sec                  
    [  5]   6.00-7.00   sec  40.5 MBytes   340 Mbits/sec                  
    [  5]   7.00-8.00   sec  39.3 MBytes   330 Mbits/sec                  
    [  5]   8.00-9.00   sec  41.2 MBytes   345 Mbits/sec                  
    [  5]   9.00-10.00  sec  40.4 MBytes   339 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   409 MBytes   343 Mbits/sec  111             sender
    [  5]   0.00-10.00  sec   406 MBytes   340 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 45485 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  41.4 MBytes   347 Mbits/sec    0   5.21 MBytes       
    [  5]   1.00-2.00   sec  38.8 MBytes   325 Mbits/sec  116   2.60 MBytes       
    [  5]   2.00-3.00   sec  35.0 MBytes   294 Mbits/sec    0   2.60 MBytes       
    [  5]   3.00-4.00   sec  33.8 MBytes   283 Mbits/sec    0   2.60 MBytes       
    [  5]   4.00-5.00   sec  35.0 MBytes   294 Mbits/sec   48   1.30 MBytes       
    [  5]   5.00-6.00   sec  36.2 MBytes   304 Mbits/sec    0   1.34 MBytes       
    [  5]   6.00-7.00   sec  32.5 MBytes   273 Mbits/sec    0   1.35 MBytes       
    [  5]   7.00-8.00   sec  35.0 MBytes   294 Mbits/sec    0   1.35 MBytes       
    [  5]   8.00-9.00   sec  33.8 MBytes   283 Mbits/sec    0   1.37 MBytes       
    [  5]   9.00-10.00  sec  37.5 MBytes   314 Mbits/sec    0   1.41 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   359 MBytes   301 Mbits/sec  164             sender
    [  5]   0.00-10.01  sec   356 MBytes   299 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 60382 bytes (127 packets)
    TX: 54291 bytes (193 packets)
    signal: -63 dBm
    rx bitrate: 720.5 MBit/s
    tx bitrate: 544.4 MBit/s
    
    ```

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">111</span> Mbits/sec | <span style="font-size: 1.5rem;">149</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 34587 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.8 MBytes   107 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   132 MBytes   111 Mbits/sec   89             sender
    [  5]   0.00-10.00  sec   129 MBytes   108 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 56005 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.2 MBytes   161 Mbits/sec    0    612 KBytes       
    [  5]   1.00-2.00   sec  18.0 MBytes   151 Mbits/sec    0    682 KBytes       
    [  5]   2.00-3.00   sec  16.9 MBytes   141 Mbits/sec    0    755 KBytes       
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec    0    795 KBytes       
    [  5]   4.00-5.00   sec  17.8 MBytes   149 Mbits/sec    0    795 KBytes       
    [  5]   5.00-6.00   sec  18.2 MBytes   153 Mbits/sec    0    877 KBytes       
    [  5]   6.00-7.00   sec  16.8 MBytes   141 Mbits/sec    0    877 KBytes       
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec    0    922 KBytes       
    [  5]   8.00-9.00   sec  18.2 MBytes   153 Mbits/sec    0    922 KBytes       
    [  5]   9.00-10.00  sec  16.8 MBytes   140 Mbits/sec    0    922 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   178 MBytes   149 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   176 MBytes   147 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 47155 bytes (176 packets)
    TX: 51403 bytes (215 packets)
    signal: -35 dBm
    rx bitrate: 648.5 MBit/s 80MHz HE-MCS 6 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">822</span> Mbits/sec | <span style="font-size: 1.5rem;">754</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.125 port 54509 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  92.5 MBytes   775 Mbits/sec                  
    [  5]   1.00-2.00   sec   104 MBytes   868 Mbits/sec                  
    [  5]   2.00-3.00   sec   101 MBytes   844 Mbits/sec                  
    [  5]   3.00-4.00   sec   101 MBytes   846 Mbits/sec                  
    [  5]   4.00-5.00   sec   101 MBytes   844 Mbits/sec                  
    [  5]   5.00-6.00   sec  98.1 MBytes   823 Mbits/sec                  
    [  5]   6.00-7.00   sec  92.1 MBytes   773 Mbits/sec                  
    [  5]   7.00-8.00   sec  90.8 MBytes   761 Mbits/sec                  
    [  5]   8.00-9.00   sec  98.2 MBytes   824 Mbits/sec                  
    [  5]   9.00-10.00  sec  98.6 MBytes   827 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   980 MBytes   822 Mbits/sec  201             sender
    [  5]   0.00-10.00  sec   976 MBytes   819 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.125 port 55733 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  86.0 MBytes   721 Mbits/sec  403   3.11 MBytes       
    [  5]   1.00-2.00   sec   101 MBytes   848 Mbits/sec    0   3.13 MBytes       
    [  5]   2.00-3.00   sec  90.0 MBytes   755 Mbits/sec   74   1.63 MBytes       
    [  5]   3.00-4.00   sec  97.5 MBytes   818 Mbits/sec    0   1.71 MBytes       
    [  5]   4.00-5.00   sec   100 MBytes   841 Mbits/sec    0   1.79 MBytes       
    [  5]   5.00-6.00   sec  96.5 MBytes   810 Mbits/sec    0   1.86 MBytes       
    [  5]   6.00-7.00   sec  78.6 MBytes   660 Mbits/sec  259    564 KBytes       
    [  5]   7.00-8.00   sec  81.1 MBytes   681 Mbits/sec    0    742 KBytes       
    [  5]   8.00-9.00   sec  84.4 MBytes   708 Mbits/sec    0    892 KBytes       
    [  5]   9.00-10.00  sec  83.8 MBytes   702 Mbits/sec   43    809 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   899 MBytes   754 Mbits/sec  779             sender
    [  5]   0.00-10.01  sec   896 MBytes   751 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 45321 bytes (186 packets)
    TX: 55760 bytes (205 packets)
    signal: -34 dBm
    rx bitrate: 2161.3 MBit/s 160MHz HE-MCS 10 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 979.9 MBit/s 160MHz HE-MCS 5 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">91.1</span> Mbits/sec | <span style="font-size: 1.5rem;">65.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 42923 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  7.62 MBytes  63.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   109 MBytes  91.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   107 MBytes  89.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 52065 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.75 MBytes  73.3 Mbits/sec    0    222 KBytes       
    [  5]   1.00-2.00   sec  7.75 MBytes  65.0 Mbits/sec    0    288 KBytes       
    [  5]   2.00-3.00   sec  7.88 MBytes  66.0 Mbits/sec    0    288 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0    335 KBytes       
    [  5]   4.00-5.00   sec  7.75 MBytes  65.0 Mbits/sec    0    335 KBytes       
    [  5]   5.00-6.00   sec  8.38 MBytes  70.3 Mbits/sec    0    383 KBytes       
    [  5]   6.00-7.00   sec  7.12 MBytes  59.8 Mbits/sec    0    383 KBytes       
    [  5]   7.00-8.00   sec  7.75 MBytes  65.0 Mbits/sec    0    383 KBytes       
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec    0    383 KBytes       
    [  5]   9.00-10.00  sec  7.75 MBytes  65.0 Mbits/sec    0    383 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  78.2 MBytes  65.6 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  76.6 MBytes  64.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 75692 bytes (345 packets)
    TX: 51653 bytes (207 packets)
    signal: -23 dBm
    rx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">52.2</span> Mbits/sec | <span style="font-size: 1.5rem;">39.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.124 port 45389 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.86 MBytes  49.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.98 MBytes  50.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.18 MBytes  51.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.02 MBytes  50.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.87 MBytes  49.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.17 MBytes  51.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.99 MBytes  50.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.99 MBytes  50.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.93 MBytes  49.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.61 MBytes  47.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  62.4 MBytes  52.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  59.6 MBytes  50.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.124 port 38145 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.09 MBytes  42.7 Mbits/sec    0    188 KBytes       
    [  5]   1.00-2.00   sec  4.72 MBytes  39.6 Mbits/sec    0    214 KBytes       
    [  5]   2.00-3.00   sec  4.72 MBytes  39.6 Mbits/sec    0    214 KBytes       
    [  5]   3.00-4.00   sec  4.47 MBytes  37.5 Mbits/sec    0    233 KBytes       
    [  5]   4.00-5.00   sec  4.72 MBytes  39.6 Mbits/sec    0    233 KBytes       
    [  5]   5.00-6.00   sec  4.54 MBytes  38.1 Mbits/sec    0    245 KBytes       
    [  5]   6.00-7.00   sec  4.66 MBytes  39.1 Mbits/sec    0    245 KBytes       
    [  5]   7.00-8.00   sec  4.72 MBytes  39.6 Mbits/sec    0    245 KBytes       
    [  5]   8.00-9.00   sec  4.54 MBytes  38.1 Mbits/sec    0    245 KBytes       
    [  5]   9.00-10.00  sec  4.85 MBytes  40.6 Mbits/sec    0    245 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  47.0 MBytes  39.5 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  46.4 MBytes  38.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 57533 bytes (156 packets)
    TX: 52539 bytes (251 packets)
    signal: -57 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">48.8</span> Mbits/sec | <span style="font-size: 1.5rem;">54.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.123 port 47291 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.1 MBytes  85.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.59 MBytes  46.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.34 MBytes  44.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.35 MBytes  44.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.28 MBytes  44.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.26 MBytes  44.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.27 MBytes  44.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.20 MBytes  43.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.72 MBytes  39.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.81 MBytes  40.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.37  sec  60.4 MBytes  48.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  57.0 MBytes  47.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.123 port 37919 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.82 MBytes  65.5 Mbits/sec    0    252 KBytes       
    [  5]   1.00-2.00   sec  6.15 MBytes  51.6 Mbits/sec    0    276 KBytes       
    [  5]   2.00-3.00   sec  6.52 MBytes  54.7 Mbits/sec    0    296 KBytes       
    [  5]   3.00-4.00   sec  5.65 MBytes  47.4 Mbits/sec    0    311 KBytes       
    [  5]   4.00-5.00   sec  6.40 MBytes  53.7 Mbits/sec    0    311 KBytes       
    [  5]   5.00-6.00   sec  5.90 MBytes  49.5 Mbits/sec    0    311 KBytes       
    [  5]   6.00-7.00   sec  6.59 MBytes  55.3 Mbits/sec    0    332 KBytes       
    [  5]   7.00-8.00   sec  6.90 MBytes  57.9 Mbits/sec    0    332 KBytes       
    [  5]   8.00-9.00   sec  6.21 MBytes  52.1 Mbits/sec    0    332 KBytes       
    [  5]   9.00-10.00  sec  7.21 MBytes  60.4 Mbits/sec    0    502 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  65.4 MBytes  54.8 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  63.2 MBytes  53.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 53694 bytes (140 packets)
    TX: 51969 bytes (242 packets)
    signal: -50 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">11.9</span> Mbits/sec | <span style="font-size: 1.5rem;">21.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 33889 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   896 KBytes  7.33 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.12 MBytes  9.44 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.75 MBytes  14.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.62 MBytes  13.6 Mbits/sec                  
    [  5]   4.00-5.00   sec   768 KBytes  6.29 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.62 MBytes  13.6 Mbits/sec                  
    [  5]   6.00-7.00   sec   896 KBytes  7.34 Mbits/sec                  
    [  5]   7.00-8.00   sec   768 KBytes  6.29 Mbits/sec                  
    [  5]   8.00-9.00   sec   512 KBytes  4.20 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.25 MBytes  10.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  14.2 MBytes  11.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  11.1 MBytes  9.33 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 52143 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  2.50 MBytes  21.0 Mbits/sec    0    137 KBytes       
    [  5]   1.00-2.00   sec  2.00 MBytes  16.8 Mbits/sec    0    206 KBytes       
    [  5]   2.00-3.00   sec  1.62 MBytes  13.6 Mbits/sec    0    281 KBytes       
    [  5]   3.00-4.00   sec  3.88 MBytes  32.5 Mbits/sec    0    416 KBytes       
    [  5]   4.00-5.00   sec  2.75 MBytes  23.1 Mbits/sec    0    477 KBytes       
    [  5]   5.00-6.00   sec  2.12 MBytes  17.8 Mbits/sec    1    389 KBytes       
    [  5]   6.00-7.00   sec  3.25 MBytes  27.3 Mbits/sec    0    450 KBytes       
    [  5]   7.00-8.00   sec  2.12 MBytes  17.8 Mbits/sec    1    331 KBytes       
    [  5]   8.00-9.00   sec  3.12 MBytes  26.2 Mbits/sec    0    362 KBytes       
    [  5]   9.00-10.00  sec  2.25 MBytes  18.9 Mbits/sec    0    385 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  25.6 MBytes  21.5 Mbits/sec    2             sender
    [  5]   0.00-10.01  sec  23.1 MBytes  19.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 88852 bytes (371 packets)
    TX: 57757 bytes (229 packets)
    signal: -31 dBm
    rx bitrate: 39.0 MBit/s MCS 4
    tx bitrate: 65.0 MBit/s MCS 7
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">72.9</span> Mbits/sec | <span style="font-size: 1.5rem;">62.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 54661 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  7.12 MBytes  59.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.38 MBytes  70.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  8.62 MBytes  72.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  8.62 MBytes  72.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  9.12 MBytes  76.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  8.75 MBytes  73.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  87.0 MBytes  72.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  85.2 MBytes  71.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 39197 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.38 MBytes  53.4 Mbits/sec    0    232 KBytes       
    [  5]   1.00-2.00   sec  7.75 MBytes  65.0 Mbits/sec    0    288 KBytes       
    [  5]   2.00-3.00   sec  7.88 MBytes  65.9 Mbits/sec    0    344 KBytes       
    [  5]   3.00-4.00   sec  7.38 MBytes  62.0 Mbits/sec    0    362 KBytes       
    [  5]   4.00-5.00   sec  7.50 MBytes  62.9 Mbits/sec    0    380 KBytes       
    [  5]   5.00-6.00   sec  7.00 MBytes  58.8 Mbits/sec    0    404 KBytes       
    [  5]   6.00-7.00   sec  7.38 MBytes  61.9 Mbits/sec    0    404 KBytes       
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec    8    297 KBytes       
    [  5]   8.00-9.00   sec  8.25 MBytes  69.2 Mbits/sec    8    221 KBytes       
    [  5]   9.00-10.00  sec  6.88 MBytes  57.6 Mbits/sec    0    243 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  74.2 MBytes  62.3 Mbits/sec   16             sender
    [  5]   0.00-10.00  sec  72.5 MBytes  60.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 90960 bytes (375 packets)
    TX: 62336 bytes (306 packets)
    signal: -32 dBm
    rx bitrate: 240.0 MBit/s MCS 13 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">42.4</span> Mbits/sec | <span style="font-size: 1.5rem;">26.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 58269 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.50 MBytes  37.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.62 MBytes  38.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.38  sec  52.5 MBytes  42.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  49.0 MBytes  41.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 48397 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.88 MBytes  32.5 Mbits/sec    0    195 KBytes       
    [  5]   1.00-2.00   sec  3.00 MBytes  25.2 Mbits/sec    0    246 KBytes       
    [  5]   2.00-3.00   sec  2.75 MBytes  23.1 Mbits/sec    0    270 KBytes       
    [  5]   3.00-4.00   sec  3.50 MBytes  29.4 Mbits/sec    0    286 KBytes       
    [  5]   4.00-5.00   sec  3.00 MBytes  25.2 Mbits/sec    0    300 KBytes       
    [  5]   5.00-6.00   sec  3.12 MBytes  26.2 Mbits/sec    0    300 KBytes       
    [  5]   6.00-7.00   sec  3.12 MBytes  26.2 Mbits/sec    0    315 KBytes       
    [  5]   7.00-8.00   sec  2.75 MBytes  23.1 Mbits/sec    0    315 KBytes       
    [  5]   8.00-9.00   sec  3.38 MBytes  28.3 Mbits/sec    0    315 KBytes       
    [  5]   9.00-10.00  sec  2.62 MBytes  22.0 Mbits/sec    0    315 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  31.1 MBytes  26.1 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  29.6 MBytes  24.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 86250 bytes (308 packets)
    TX: 51172 bytes (208 packets)
    signal: -38 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">38.1</span> Mbits/sec | <span style="font-size: 1.5rem;">28.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.122 port 49319 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.46 MBytes  45.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.17 MBytes  35.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.70 MBytes  39.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.02 MBytes  33.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.45 MBytes  37.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.02 MBytes  42.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.41 MBytes  28.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.61 MBytes  30.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.51 MBytes  29.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.10  sec  45.9 MBytes  38.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  42.4 MBytes  35.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.122 port 44447 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.73 MBytes  48.1 Mbits/sec    0    303 KBytes       
    [  5]   1.00-2.00   sec  4.78 MBytes  40.1 Mbits/sec    0    509 KBytes       
    [  5]   2.00-3.00   sec  4.10 MBytes  34.4 Mbits/sec    0    667 KBytes       
    [  5]   3.00-4.00   sec  3.29 MBytes  27.6 Mbits/sec    0    740 KBytes       
    [  5]   4.00-5.00   sec  2.55 MBytes  21.4 Mbits/sec    0    840 KBytes       
    [  5]   5.00-6.00   sec  2.11 MBytes  17.7 Mbits/sec    0    950 KBytes       
    [  5]   6.00-7.00   sec  3.29 MBytes  27.6 Mbits/sec    0   1020 KBytes       
    [  5]   7.00-8.00   sec  2.26 MBytes  19.0 Mbits/sec    0   1.04 MBytes       
    [  5]   8.00-9.00   sec  3.75 MBytes  31.5 Mbits/sec    0   1.07 MBytes       
    [  5]   9.00-10.00  sec  2.50 MBytes  21.0 Mbits/sec    0   1.07 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  34.4 MBytes  28.8 Mbits/sec    0             sender
    [  5]   0.00-10.11  sec  32.4 MBytes  26.9 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">31.2</span> Mbits/sec | <span style="font-size: 1.5rem;">43.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 60557 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  2.38 MBytes  19.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.12 MBytes  26.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.62 MBytes  30.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.75 MBytes  31.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.08  sec  37.5 MBytes  31.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  34.4 MBytes  28.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 52903 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.88 MBytes  49.2 Mbits/sec    0    260 KBytes       
    [  5]   1.00-2.00   sec  5.50 MBytes  46.1 Mbits/sec    0    410 KBytes       
    [  5]   2.00-3.00   sec  5.00 MBytes  42.0 Mbits/sec    0    410 KBytes       
    [  5]   3.00-4.00   sec  5.38 MBytes  45.1 Mbits/sec    0    471 KBytes       
    [  5]   4.00-5.00   sec  4.88 MBytes  40.8 Mbits/sec    0    498 KBytes       
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec    0    527 KBytes       
    [  5]   6.00-7.00   sec  5.38 MBytes  45.1 Mbits/sec    0    527 KBytes       
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec    0    527 KBytes       
    [  5]   8.00-9.00   sec  4.25 MBytes  35.7 Mbits/sec    0    527 KBytes       
    [  5]   9.00-10.00  sec  5.25 MBytes  44.0 Mbits/sec    0    527 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  51.9 MBytes  43.5 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  49.8 MBytes  41.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 81030 bytes (315 packets)
    TX: 49238 bytes (197 packets)
    signal: -34 dBm
    rx bitrate: 39.0 MBit/s MCS 4
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek RT3070

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL2870.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.265, 6.12.34-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL2870</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">7.75</span> Mbits/sec | <span style="font-size: 1.5rem;">11.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 51321 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   640 KBytes  5.24 Mbits/sec                  
    [  5]   1.00-2.00   sec   512 KBytes  4.19 Mbits/sec                  
    [  5]   2.00-3.00   sec   640 KBytes  5.24 Mbits/sec                  
    [  5]   3.00-4.00   sec   768 KBytes  6.29 Mbits/sec                  
    [  5]   4.00-5.00   sec   512 KBytes  4.19 Mbits/sec                  
    [  5]   5.00-6.00   sec   768 KBytes  6.29 Mbits/sec                  
    [  5]   6.00-7.00   sec   640 KBytes  5.24 Mbits/sec                  
    [  5]   7.00-8.00   sec   768 KBytes  6.29 Mbits/sec                  
    [  5]   8.00-9.00   sec   512 KBytes  4.19 Mbits/sec                  
    [  5]   9.00-10.00  sec   768 KBytes  6.29 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  9.25 MBytes  7.75 Mbits/sec    0            sender
    [  5]   0.00-10.00  sec  6.38 MBytes  5.35 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 56799 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.75 MBytes  31.4 Mbits/sec    0    700 KBytes       
    [  5]   1.00-2.00   sec  1.38 MBytes  11.5 Mbits/sec    1   72.1 KBytes       
    [  5]   2.00-3.00   sec  1.25 MBytes  10.5 Mbits/sec    1    177 KBytes       
    [  5]   3.00-4.00   sec  0.00 Bytes  0.00 bits/sec    1   91.9 KBytes       
    [  5]   4.00-5.00   sec  1.38 MBytes  11.5 Mbits/sec    0    105 KBytes       
    [  5]   5.00-6.00   sec  1.38 MBytes  11.5 Mbits/sec    0    115 KBytes       
    [  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0    120 KBytes       
    [  5]   7.00-8.00   sec  1.50 MBytes  12.6 Mbits/sec    0    132 KBytes       
    [  5]   8.00-9.00   sec  1.38 MBytes  11.5 Mbits/sec    0    140 KBytes       
    [  5]   9.00-10.00  sec  1.38 MBytes  11.5 Mbits/sec    0    150 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  13.4 MBytes  11.2 Mbits/sec    3            sender
    [  5]   0.00-10.01  sec  9.62 MBytes  8.07 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 91401 bytes (398 packets)
    TX: 59336 bytes (213 packets)
    signal: -55 dBm
    rx bitrate: 14.4 MBit/s MCS 1 short GI
    tx bitrate: 26.0 MBit/s MCS 3
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.154, 6.12.30-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">51.3</span> Mbits/sec | <span style="font-size: 1.5rem;">55.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.121 port 58365 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.63 MBytes  47.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.72 MBytes  47.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.81 MBytes  48.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.82 MBytes  48.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.77 MBytes  48.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.82 MBytes  48.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.76 MBytes  48.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.76 MBytes  48.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.74 MBytes  48.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.72 MBytes  48.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  61.2 MBytes  51.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  57.5 MBytes  48.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.121 port 59057 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.96 MBytes  58.4 Mbits/sec    0    310 KBytes       
    [  5]   1.00-2.00   sec  8.26 MBytes  69.3 Mbits/sec    0    523 KBytes       
    [  5]   2.00-3.00   sec  5.90 MBytes  49.5 Mbits/sec    0    639 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0    742 KBytes       
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec    0    891 KBytes       
    [  5]   5.00-6.00   sec  7.50 MBytes  62.9 Mbits/sec    0    945 KBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0    981 KBytes       
    [  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0    996 KBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0    996 KBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.04 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  66.1 MBytes  55.5 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  63.6 MBytes  53.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 456459953 bytes (396688 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">17.8</span> Mbits/sec | <span style="font-size: 1.5rem;">11.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.113 port 53493 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.77 MBytes  14.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.90 MBytes  15.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.83 MBytes  15.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.52 MBytes  12.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.71 MBytes  14.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.17 MBytes  18.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.07 MBytes  17.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  1.88 MBytes  15.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.01 MBytes  16.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.38 MBytes  20.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.10  sec  21.4 MBytes  17.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  19.2 MBytes  16.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.113 port 45921 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.56 MBytes  13.1 Mbits/sec    0   87.7 KBytes       
    [  5]   1.00-2.00   sec  1.37 MBytes  11.5 Mbits/sec    0    112 KBytes       
    [  5]   2.00-3.00   sec  1.43 MBytes  12.0 Mbits/sec    0    127 KBytes       
    [  5]   3.00-4.00   sec  1.30 MBytes  10.9 Mbits/sec    0    127 KBytes       
    [  5]   4.00-5.00   sec  1.30 MBytes  10.9 Mbits/sec    0    139 KBytes       
    [  5]   5.00-6.00   sec  1.12 MBytes  9.38 Mbits/sec    6    113 KBytes       
    [  5]   6.00-7.00   sec  1.49 MBytes  12.5 Mbits/sec    0    124 KBytes       
    [  5]   7.00-8.00   sec  1.30 MBytes  10.9 Mbits/sec    0    129 KBytes       
    [  5]   8.00-9.00   sec  1.30 MBytes  10.9 Mbits/sec    0    129 KBytes       
    [  5]   9.00-10.00  sec  1.12 MBytes  9.38 Mbits/sec    7   90.5 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  13.3 MBytes  11.2 Mbits/sec   13             sender
    [  5]   0.00-10.05  sec  13.0 MBytes  10.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 52530 bytes (164 packets)
    TX: 62087 bytes (248 packets)
    signal: -30 dBm
    rx bitrate: 6.0 MBit/s
    tx bitrate: 39.0 MBit/s MCS 4
    
    ```

## Failed Devices

| Commercial Name | Chip | Class |
|:-----|:--------|:------|
| AIC8800 | AIC8800 | AX |
| Atheros AR9271 | AR9271 | N |
| BrosTrend 1800 | RTL8852AU | AX |
| Mediatek MT7925 | MT7925 | AX |
| Mediatek MT7925E #1 | MT7925E | AX |
| Mediatek MT7925E #2 | MT7925E | AX |
| Ralink MT7601U | MT7601U | N |
| Realtek 8188EU | RTL8192CU | N |
| Realtek 8814AU | RTL8814AU | AC |
| Realtek 8852BE | RTL8852BE | AX |
| Realtek RT2870 | RTL2870 | N |
<!-- DUT-STOP -->

## Contribute

- Assist us in developing and maintaining our testing system: Your expertise can help us enhance and optimize [our test infrastructure](https://github.com/armbian/armbian.github.io/actions/workflows/usb-wireless-autotest.yml). By contributing your skills, you can play a key role in ensuring the accuracy and reliability of our test results.

- Donate hardware: Your contribution of new hardware, whether it’s a wireless adapter or any other equipment, helps us expand our testing capabilities. We’re specifically looking for [new wireless adapters](https://www.amazon.de/hz/wishlist/ls/1GA17IGQ2MF0V?ref_=wl_share) that haven’t yet been added to our system. Your donation can directly impact the scope and depth of our tests.

- Join our team: Become part of our passionate and dedicated team. We’re looking for [individuals who share our vision and are eager to contribute to the development of innovative testing solutions](https://forum.armbian.com/staffapplications/). Whether you have technical expertise or simply a willingness to learn, there’s a place for you here!


## Adding a New Device

This guide provides step-by-step instructions to add a new device (SBC SDIO, PCI or USB adapter) to the wireless testing infrastructure.

### 1. Prepare the Host Machine

- Ensure the board and wireless device is supported by Armbian.
- Flash Armbian image and configure basic settings
- Set hostname that reflects wireless test device (eg. rtl3070, wifiserver)

```bash
sudo hostnamectl set-hostname rtl3070
```

### 2. Identify Network Interfaces

- Use `ip link` or `iw dev` to list available interfaces.
- Identify MAC address and interface name (e.g., `wlan0`, `wlxMAC`, etc.).

### 3. Create a UDEV Rule

!!! warning

    This step is only necessary if your network device does not have a predictable interface name.

- Use a predictable name like `wl<MAC>` to avoid interface conflicts.
- Add rule in `/etc/udev/rules.d/70-persistent-net.rules`:
  
```bash
SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="xx:xx:xx:xx:xx:xx", NAME="wl<MAC>"
```

### 4. Get VPN access

The `TAILSCALE_AUTH_KEY` and access credentials for NetBox must be provided by the Armbian administration team. For assistance, please contact us via [https://www.armbian.com/contact/](https://www.armbian.com/contact/).

### 5. Prepare the machine

- Creates a new user (`ci`) with sudo privileges
- Configures SSH for key-based authentication only
- Installs and configures Tailscale for secure remote access
- Installs `iperf3` for network performance testing

```bash
#!/bin/bash

set -e

USERNAME="ci"
KEY_URL="https://github.armbian.com/ci.asc"
TAILSCALE_AUTH_KEY="tskey-auth-kXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

echo "[+] Creating user '$USERNAME' without password"
useradd -m -s /bin/bash "$USERNAME"
passwd -d "$USERNAME"
usermod -aG sudo "$USERNAME"

echo "[+] Setting up SSH key from $KEY_URL"
SSH_DIR="/home/$USERNAME/.ssh"
mkdir -p "$SSH_DIR"
curl -fsSL "$KEY_URL" -o "$SSH_DIR/authorized_keys"
chmod 700 "$SSH_DIR"
chmod 600 "$SSH_DIR/authorized_keys"
chown -R "$USERNAME:$USERNAME" "$SSH_DIR"

echo "[+] Disabling password authentication in SSH config"
sed -i 's/^#*\s*PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
sed -i 's/^#*\s*PermitEmptyPasswords.*/PermitEmptyPasswords no/' /etc/ssh/sshd_config
systemctl restart ssh

echo "[+] Installing Tailscale"
curl -fsSL https://tailscale.com/install.sh | sh

echo "[+] Bringing up Tailscale with provided auth key"
tailscale up --auth-key="$TAILSCALE_AUTH_KEY"

echo "[+] Installing iperf3 (non-interactive, no daemon)"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -yqq iperf3

echo "[✔] Setup complete. User '$USERNAME' added, SSH key installed, Tailscale connected."
```

### 6. Register Your Location

Access: <https://stuff.armbian.com/netbox/dcim/sites/>

- Sites in NetBox represent physical locations of wireless test equipment.
- Each site have devices such as Access Points (APs), iperf3 servers, and wireless test clients.
- Register your testing location first if it doesn't exist yet. Create a new site with a clear name (e.g., Office Berlin, Lab Maribor) and add necessary data.

!!! warning
    Make sure to check if site is not already define to not clutter database!

???+ success "Update Relevant Information"

    - Access point SSID: `Your SSID`
    - Iperf3 server IP: your local `IP address` that runs iperf3 server and can be accessible from wireless client

### 7. Register Device Type

Add [new device type](https://stuff.armbian.com/netbox/dcim/manufacturers/61/) 
 
???+ success "Relevant data"

    - Model name (CAPS): AIC8800
    - Manufacturer: Generic
    - Add image of the device in full HD (1920x1080) with exact same name as model AIC8800.png (CAPS name, lowercase extension)

!!! warning

    Skip this step if WiFi SoC already exists in database.

### 8. Register Device

???+ success "Relevant data"
 
    - Name: Compex WLE900VX (use commercial name)
    - Device role: WiFi DUT
    - Tags: USB Wireless
    - Manufacturer: Generic
    - Device type: AIC8800 (select the one you added previously)
    - Serial number: 04:f0:21:2c:75:14 (MAC address)
    - Location: where you are
    - Site: name of your office, defined in previous step
    - Custom Fields / class: AC (wifi classes: AX, AC, N)

- Add virtual interface (Add Components -> Interfaces)

???+ success "Relevant data"

    - Name: `tailscale0`
    - Type: `virtual`

Then select interface `tailscale0` and add `IP address`. Copy `IP address` from your device (example: 100.115.0.58/32) and select: Make this the primary IP for the device/VM

### 9. Run Initial Test

Run the [Wireless Performance Autotest workflow](https://github.com/armbian/armbian.github.io/actions/workflows/wireless-performance-autotest.yml) to verify whether the newly added device has been included in the test pool.

## Other resources

- [USB WiFi Adapter Information for Linux](https://github.com/morrownr/USB-WiFi)
- [Official Linux Wireless documentation](https://wireless.docs.kernel.org/en/latest/index.html)
- [Armbian forum - Advanced users - Development](https://forum.armbian.com/forum/4-advanced-users-development/)
