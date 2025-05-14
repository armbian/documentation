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
**Test Date:** [2025-05-14 21:49 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15031336398)
### AC

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">193</span> Mbits/sec | <span style="font-size: 1.5rem;">153</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 46847 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  22.4 MBytes   188 Mbits/sec                  
    [  5]   1.00-2.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.8 MBytes   200 Mbits/sec                  
    [  5]   3.00-4.00   sec  23.6 MBytes   198 Mbits/sec                  
    [  5]   4.00-5.00   sec  23.1 MBytes   194 Mbits/sec                  
    [  5]   5.00-6.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   6.00-7.00   sec  22.6 MBytes   190 Mbits/sec                  
    [  5]   7.00-8.00   sec  20.9 MBytes   175 Mbits/sec                  
    [  5]   8.00-9.00   sec  22.1 MBytes   185 Mbits/sec                  
    [  5]   9.00-10.00  sec  22.5 MBytes   189 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   231 MBytes   193 Mbits/sec   65             sender
    [  5]   0.00-10.00  sec   227 MBytes   191 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 35739 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.1 MBytes   152 Mbits/sec    0    666 KBytes       
    [  5]   1.00-2.00   sec  18.6 MBytes   156 Mbits/sec    0    861 KBytes       
    [  5]   2.00-3.00   sec  19.1 MBytes   160 Mbits/sec    0   1.12 MBytes       
    [  5]   3.00-4.00   sec  17.8 MBytes   149 Mbits/sec    0   1.12 MBytes       
    [  5]   4.00-5.00   sec  17.1 MBytes   144 Mbits/sec    0   1.12 MBytes       
    [  5]   5.00-6.00   sec  19.4 MBytes   163 Mbits/sec    0   1.25 MBytes       
    [  5]   6.00-7.00   sec  17.5 MBytes   147 Mbits/sec    0   1.25 MBytes       
    [  5]   7.00-8.00   sec  18.8 MBytes   157 Mbits/sec    0   1.25 MBytes       
    [  5]   8.00-9.00   sec  17.5 MBytes   147 Mbits/sec    0   1.25 MBytes       
    [  5]   9.00-10.00  sec  18.8 MBytes   157 Mbits/sec    0   1.32 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   183 MBytes   153 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   179 MBytes   150 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 128707 bytes (556 packets)
    TX: 59660 bytes (240 packets)
    signal: -35 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">79.3</span> Mbits/sec | <span style="font-size: 1.5rem;">117</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 47441 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  7.75 MBytes  64.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.88 MBytes  82.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  9.88 MBytes  82.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  9.75 MBytes  81.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.00 MBytes  75.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  94.6 MBytes  79.3 Mbits/sec    5             sender
    [  5]   0.00-10.00  sec  94.0 MBytes  78.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 59041 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  14.5 MBytes   122 Mbits/sec    0    604 KBytes       
    [  5]   1.00-2.00   sec  13.2 MBytes   111 Mbits/sec    0    790 KBytes       
    [  5]   2.00-3.00   sec  14.4 MBytes   121 Mbits/sec    0   1012 KBytes       
    [  5]   3.00-4.00   sec  14.0 MBytes   118 Mbits/sec    0   1.06 MBytes       
    [  5]   4.00-5.00   sec  15.5 MBytes   130 Mbits/sec    0   1.11 MBytes       
    [  5]   5.00-6.00   sec  14.6 MBytes   123 Mbits/sec    0   1.16 MBytes       
    [  5]   6.00-7.00   sec  14.1 MBytes   119 Mbits/sec    0   1.16 MBytes       
    [  5]   7.00-8.00   sec  14.0 MBytes   117 Mbits/sec    0   1.23 MBytes       
    [  5]   8.00-9.00   sec  12.8 MBytes   107 Mbits/sec    0   1.23 MBytes       
    [  5]   9.00-10.00  sec  12.9 MBytes   108 Mbits/sec    0   1.29 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   140 MBytes   117 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   138 MBytes   115 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 197004 bytes (485 packets)
    TX: 102632 bytes (499 packets)
    signal: -39 dBm
    rx bitrate: 243.0 MBit/s MCS 14 40MHz
    tx bitrate: 243.0 MBit/s MCS 14 40MHz
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">156</span> Mbits/sec | <span style="font-size: 1.5rem;">198</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 59855 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.0 MBytes   151 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   186 MBytes   156 Mbits/sec  267             sender
    [  5]   0.00-10.00  sec   183 MBytes   154 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 60777 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.9 MBytes   217 Mbits/sec    0    590 KBytes       
    [  5]   1.00-2.00   sec  23.2 MBytes   195 Mbits/sec    0    701 KBytes       
    [  5]   2.00-3.00   sec  23.5 MBytes   197 Mbits/sec    0    701 KBytes       
    [  5]   3.00-4.00   sec  23.8 MBytes   199 Mbits/sec    2    369 KBytes       
    [  5]   4.00-5.00   sec  23.5 MBytes   197 Mbits/sec    0    404 KBytes       
    [  5]   5.00-6.00   sec  22.9 MBytes   192 Mbits/sec    0    427 KBytes       
    [  5]   6.00-7.00   sec  24.1 MBytes   202 Mbits/sec    3    348 KBytes       
    [  5]   7.00-8.00   sec  22.2 MBytes   187 Mbits/sec    0    375 KBytes       
    [  5]   8.00-9.00   sec  22.8 MBytes   191 Mbits/sec    0    404 KBytes       
    [  5]   9.00-10.00  sec  23.6 MBytes   198 Mbits/sec    0    420 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   236 MBytes   198 Mbits/sec    5             sender
    [  5]   0.00-10.01  sec   233 MBytes   195 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -37 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">272</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 58545 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.2 MBytes   153 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   182 MBytes   153 Mbits/sec    5             sender
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 49649 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.6 MBytes   290 Mbits/sec    0    775 KBytes       
    [  5]   1.00-2.00   sec  31.9 MBytes   267 Mbits/sec    0    915 KBytes       
    [  5]   2.00-3.00   sec  32.9 MBytes   276 Mbits/sec    6    527 KBytes       
    [  5]   3.00-4.00   sec  31.6 MBytes   265 Mbits/sec    0    571 KBytes       
    [  5]   4.00-5.00   sec  31.8 MBytes   266 Mbits/sec    0    600 KBytes       
    [  5]   5.00-6.00   sec  32.9 MBytes   276 Mbits/sec    0    614 KBytes       
    [  5]   6.00-7.00   sec  31.6 MBytes   265 Mbits/sec    0    621 KBytes       
    [  5]   7.00-8.00   sec  31.6 MBytes   265 Mbits/sec    0    624 KBytes       
    [  5]   8.00-9.00   sec  33.4 MBytes   280 Mbits/sec    0    624 KBytes       
    [  5]   9.00-10.00  sec  31.5 MBytes   264 Mbits/sec    0    625 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   324 MBytes   272 Mbits/sec    6             sender
    [  5]   0.00-10.01  sec   320 MBytes   269 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -35 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8814AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">152</span> Mbits/sec | <span style="font-size: 1.5rem;">23.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.106 port 48913 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   5.00-6.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.1 MBytes   152 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   181 MBytes   152 Mbits/sec  182             sender
    [  5]   0.00-10.00  sec   178 MBytes   149 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.106 port 54221 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.50 MBytes  29.3 Mbits/sec    0    256 KBytes       
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec    0    337 KBytes       
    [  5]   2.00-3.00   sec  2.75 MBytes  23.1 Mbits/sec    0    337 KBytes       
    [  5]   3.00-4.00   sec  2.75 MBytes  23.1 Mbits/sec    0    337 KBytes       
    [  5]   4.00-5.00   sec  2.88 MBytes  24.1 Mbits/sec    0    354 KBytes       
    [  5]   5.00-6.00   sec  2.25 MBytes  18.9 Mbits/sec    0    354 KBytes       
    [  5]   6.00-7.00   sec  3.00 MBytes  25.2 Mbits/sec    0    354 KBytes       
    [  5]   7.00-8.00   sec  3.00 MBytes  25.2 Mbits/sec    0    354 KBytes       
    [  5]   8.00-9.00   sec  2.12 MBytes  17.8 Mbits/sec    0    354 KBytes       
    [  5]   9.00-10.00  sec  3.00 MBytes  25.2 Mbits/sec    0    354 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  28.5 MBytes  23.9 Mbits/sec    0             sender
    [  5]   0.00-10.09  sec  26.9 MBytes  22.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -37 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8822CE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8822CE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.21-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">581</span> Mbits/sec | <span style="font-size: 1.5rem;">567</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 37067 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  77.7 MBytes   652 Mbits/sec                  
    [  5]   1.00-2.00   sec  75.7 MBytes   635 Mbits/sec                  
    [  5]   2.00-3.00   sec  71.0 MBytes   595 Mbits/sec                  
    [  5]   3.00-4.00   sec  63.2 MBytes   530 Mbits/sec                  
    [  5]   4.00-5.00   sec  65.0 MBytes   545 Mbits/sec                  
    [  5]   5.00-6.00   sec  66.5 MBytes   558 Mbits/sec                  
    [  5]   6.00-7.00   sec  68.8 MBytes   577 Mbits/sec                  
    [  5]   7.00-8.00   sec  68.3 MBytes   573 Mbits/sec                  
    [  5]   8.00-9.00   sec  68.1 MBytes   571 Mbits/sec                  
    [  5]   9.00-10.00  sec  65.3 MBytes   548 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   692 MBytes   581 Mbits/sec  1119             sender
    [  5]   0.00-10.00  sec   690 MBytes   578 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 37065 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  75.5 MBytes   633 Mbits/sec  316   1.62 MBytes       
    [  5]   1.00-2.00   sec  73.8 MBytes   619 Mbits/sec    0   1.68 MBytes       
    [  5]   2.00-3.00   sec  75.0 MBytes   629 Mbits/sec    0   1.74 MBytes       
    [  5]   3.00-4.00   sec  63.8 MBytes   533 Mbits/sec  100    535 KBytes       
    [  5]   4.00-5.00   sec  60.0 MBytes   505 Mbits/sec    0    679 KBytes       
    [  5]   5.00-6.00   sec  63.8 MBytes   535 Mbits/sec    0    805 KBytes       
    [  5]   6.00-7.00   sec  67.5 MBytes   566 Mbits/sec    0    916 KBytes       
    [  5]   7.00-8.00   sec  67.5 MBytes   566 Mbits/sec    0   1018 KBytes       
    [  5]   8.00-9.00   sec  67.5 MBytes   566 Mbits/sec    0   1.08 MBytes       
    [  5]   9.00-10.00  sec  61.2 MBytes   514 Mbits/sec   62    693 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   676 MBytes   567 Mbits/sec  478             sender
    [  5]   0.00-10.01  sec   673 MBytes   564 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 110819 bytes (397 packets)
    TX: 58888 bytes (213 packets)
    signal: -33 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">111</span> Mbits/sec | <span style="font-size: 1.5rem;">151</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.117 port 44687 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.0 MBytes   109 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   132 MBytes   111 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   130 MBytes   109 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.117 port 53111 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.8 MBytes   166 Mbits/sec    0    598 KBytes       
    [  5]   1.00-2.00   sec  17.8 MBytes   149 Mbits/sec    0    631 KBytes       
    [  5]   2.00-3.00   sec  19.1 MBytes   160 Mbits/sec    0    706 KBytes       
    [  5]   3.00-4.00   sec  17.2 MBytes   145 Mbits/sec    0    861 KBytes       
    [  5]   4.00-5.00   sec  18.4 MBytes   154 Mbits/sec    0    912 KBytes       
    [  5]   5.00-6.00   sec  16.8 MBytes   141 Mbits/sec    0    957 KBytes       
    [  5]   6.00-7.00   sec  18.1 MBytes   152 Mbits/sec    0   1005 KBytes       
    [  5]   7.00-8.00   sec  17.1 MBytes   144 Mbits/sec    0   1005 KBytes       
    [  5]   8.00-9.00   sec  18.6 MBytes   156 Mbits/sec    0   1005 KBytes       
    [  5]   9.00-10.00  sec  17.1 MBytes   143 Mbits/sec    0   1005 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   177 MBytes   149 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 66451 bytes (214 packets)
    TX: 48111 bytes (208 packets)
    signal: -40 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">617</span> Mbits/sec | <span style="font-size: 1.5rem;">456</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 41085 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  95.8 MBytes   802 Mbits/sec                  
    [  5]   1.00-2.00   sec   100 MBytes   841 Mbits/sec                  
    [  5]   2.00-3.00   sec  72.6 MBytes   609 Mbits/sec                  
    [  5]   3.00-4.00   sec  63.8 MBytes   535 Mbits/sec                  
    [  5]   4.00-5.00   sec  62.6 MBytes   525 Mbits/sec                  
    [  5]   5.00-6.00   sec  71.5 MBytes   600 Mbits/sec                  
    [  5]   6.00-7.00   sec  73.4 MBytes   616 Mbits/sec                  
    [  5]   7.00-8.00   sec  65.8 MBytes   552 Mbits/sec                  
    [  5]   8.00-9.00   sec  61.1 MBytes   513 Mbits/sec                  
    [  5]   9.00-10.00  sec  64.9 MBytes   544 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   736 MBytes   617 Mbits/sec  1160             sender
    [  5]   0.00-10.00  sec   732 MBytes   614 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 54827 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  50.6 MBytes   424 Mbits/sec  197    622 KBytes       
    [  5]   1.00-2.00   sec  47.0 MBytes   394 Mbits/sec    0    723 KBytes       
    [  5]   2.00-3.00   sec  59.0 MBytes   495 Mbits/sec    0    833 KBytes       
    [  5]   3.00-4.00   sec  55.0 MBytes   461 Mbits/sec   42    549 KBytes       
    [  5]   4.00-5.00   sec  53.8 MBytes   451 Mbits/sec    0    676 KBytes       
    [  5]   5.00-6.00   sec  52.8 MBytes   443 Mbits/sec    0    781 KBytes       
    [  5]   6.00-7.00   sec  51.9 MBytes   435 Mbits/sec   10    542 KBytes       
    [  5]   7.00-8.00   sec  49.8 MBytes   417 Mbits/sec    0    660 KBytes       
    [  5]   8.00-9.00   sec  59.2 MBytes   497 Mbits/sec    0    781 KBytes       
    [  5]   9.00-10.00  sec  65.2 MBytes   547 Mbits/sec    0    892 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   544 MBytes   456 Mbits/sec  249             sender
    [  5]   0.00-10.01  sec   541 MBytes   454 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 43261 bytes (153 packets)
    TX: 52241 bytes (221 packets)
    signal: -30 dBm
    rx bitrate: 1441.3 MBit/s 160MHz HE-MCS 7 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">91.8</span> Mbits/sec | <span style="font-size: 1.5rem;">66.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.114 port 37453 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.0 MBytes  83.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.1 MBytes  93.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   110 MBytes  91.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.114 port 36415 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.62 MBytes  72.3 Mbits/sec    0    209 KBytes       
    [  5]   1.00-2.00   sec  7.62 MBytes  64.0 Mbits/sec    0    219 KBytes       
    [  5]   2.00-3.00   sec  7.88 MBytes  66.1 Mbits/sec    0    269 KBytes       
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec    0    318 KBytes       
    [  5]   4.00-5.00   sec  8.00 MBytes  67.1 Mbits/sec    0    368 KBytes       
    [  5]   5.00-6.00   sec  7.62 MBytes  64.0 Mbits/sec    0    368 KBytes       
    [  5]   6.00-7.00   sec  7.75 MBytes  65.0 Mbits/sec    0    368 KBytes       
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0    368 KBytes       
    [  5]   8.00-9.00   sec  8.25 MBytes  69.2 Mbits/sec    0    368 KBytes       
    [  5]   9.00-10.00  sec  7.62 MBytes  63.9 Mbits/sec    0    368 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  79.2 MBytes  66.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  77.2 MBytes  64.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 207895 bytes (624 packets)
    TX: 99830 bytes (537 packets)
    signal: -17 dBm
    rx bitrate: 180.0 MBit/s MCS 12 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Atheros AR9271

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">108</span> Mbits/sec | <span style="font-size: 1.5rem;">86.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.113 port 39067 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.9 MBytes  99.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   2.00-3.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   3.00-4.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   6.00-7.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.6 MBytes   106 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.04  sec   130 MBytes   108 Mbits/sec  107             sender
    [  5]   0.00-10.00  sec   126 MBytes   106 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.113 port 58143 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  11.0 MBytes  92.2 Mbits/sec    0    273 KBytes       
    [  5]   1.00-2.00   sec  10.1 MBytes  84.9 Mbits/sec    0    273 KBytes       
    [  5]   2.00-3.00   sec  10.1 MBytes  84.9 Mbits/sec    0    273 KBytes       
    [  5]   3.00-4.00   sec  10.1 MBytes  84.9 Mbits/sec    0    273 KBytes       
    [  5]   4.00-5.00   sec  9.62 MBytes  80.7 Mbits/sec    0    273 KBytes       
    [  5]   5.00-6.00   sec  10.6 MBytes  89.1 Mbits/sec    0    273 KBytes       
    [  5]   6.00-7.00   sec  10.1 MBytes  84.9 Mbits/sec    0    273 KBytes       
    [  5]   7.00-8.00   sec  9.75 MBytes  81.8 Mbits/sec    0    273 KBytes       
    [  5]   8.00-9.00   sec  10.1 MBytes  84.9 Mbits/sec    0    273 KBytes       
    [  5]   9.00-10.00  sec  11.1 MBytes  93.3 Mbits/sec    0    474 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   103 MBytes  86.2 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   100 MBytes  84.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 97402 bytes (347 packets)
    TX: 50805 bytes (200 packets)
    signal: -49 dBm
    rx bitrate: 150.0 MBit/s MCS 7 40MHz short GI
    tx bitrate: 150.0 MBit/s MCS 7 40MHz short GI
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">60.4</span> Mbits/sec | <span style="font-size: 1.5rem;">43.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.112 port 42931 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.62 MBytes  47.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  7.00 MBytes  58.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.12 MBytes  59.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  7.00 MBytes  58.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  7.00 MBytes  58.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  7.00 MBytes  58.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.88 MBytes  57.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  72.0 MBytes  60.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  69.6 MBytes  58.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.112 port 45035 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.62 MBytes  47.1 Mbits/sec    0    189 KBytes       
    [  5]   1.00-2.00   sec  5.00 MBytes  42.0 Mbits/sec    0    208 KBytes       
    [  5]   2.00-3.00   sec  4.25 MBytes  35.6 Mbits/sec    0    215 KBytes       
    [  5]   3.00-4.00   sec  6.38 MBytes  53.5 Mbits/sec    0    468 KBytes       
    [  5]   4.00-5.00   sec  5.75 MBytes  48.2 Mbits/sec    0    615 KBytes       
    [  5]   5.00-6.00   sec  5.50 MBytes  46.1 Mbits/sec    0    819 KBytes       
    [  5]   6.00-7.00   sec  4.12 MBytes  34.6 Mbits/sec    0    915 KBytes       
    [  5]   7.00-8.00   sec  4.12 MBytes  34.6 Mbits/sec    0   1.00 MBytes       
    [  5]   8.00-9.00   sec  5.50 MBytes  46.1 Mbits/sec    0   1.19 MBytes       
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec    0   1.30 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  51.9 MBytes  43.5 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  48.0 MBytes  40.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 79770 bytes (313 packets)
    TX: 49164 bytes (204 packets)
    signal: -23 dBm
    rx bitrate: 120.0 MBit/s MCS 5 40MHz short GI
    tx bitrate: 135.0 MBit/s MCS 6 40MHz short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">81.1</span> Mbits/sec | <span style="font-size: 1.5rem;">54.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.111 port 50739 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  8.00 MBytes  67.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  9.88 MBytes  82.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  9.88 MBytes  82.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  9.00 MBytes  75.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  9.25 MBytes  77.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  8.12 MBytes  68.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.50 MBytes  79.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  96.8 MBytes  81.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  94.0 MBytes  78.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.111 port 59629 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.75 MBytes  65.0 Mbits/sec   15    119 KBytes       
    [  5]   1.00-2.00   sec  5.62 MBytes  47.1 Mbits/sec    0    151 KBytes       
    [  5]   2.00-3.00   sec  6.75 MBytes  56.6 Mbits/sec   13   91.9 KBytes       
    [  5]   3.00-4.00   sec  6.12 MBytes  51.4 Mbits/sec    0    134 KBytes       
    [  5]   4.00-5.00   sec  6.12 MBytes  51.4 Mbits/sec    7    120 KBytes       
    [  5]   5.00-6.00   sec  6.88 MBytes  57.7 Mbits/sec    0    154 KBytes       
    [  5]   6.00-7.00   sec  7.38 MBytes  61.9 Mbits/sec    6    137 KBytes       
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec    0    156 KBytes       
    [  5]   8.00-9.00   sec  6.62 MBytes  55.6 Mbits/sec   16   96.2 KBytes       
    [  5]   9.00-10.00  sec  6.62 MBytes  55.6 Mbits/sec    0    140 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  65.1 MBytes  54.6 Mbits/sec   57             sender
    [  5]   0.00-10.00  sec  64.2 MBytes  53.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 191504 bytes (570 packets)
    TX: 107355 bytes (539 packets)
    signal: -32 dBm
    rx bitrate: 240.0 MBit/s MCS 13 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">75.7</span> Mbits/sec | <span style="font-size: 1.5rem;">86.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.110 port 46957 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  8.88 MBytes  74.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.88 MBytes  74.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.00 MBytes  75.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.25 MBytes  69.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  8.88 MBytes  74.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  8.62 MBytes  72.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  90.5 MBytes  75.7 Mbits/sec   91             sender
    [  5]   0.00-10.00  sec  87.5 MBytes  73.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.110 port 39599 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  10.8 MBytes  90.1 Mbits/sec    0    400 KBytes       
    [  5]   1.00-2.00   sec  10.8 MBytes  90.1 Mbits/sec    0    486 KBytes       
    [  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0    568 KBytes       
    [  5]   3.00-4.00   sec  11.6 MBytes  97.5 Mbits/sec    0    636 KBytes       
    [  5]   4.00-5.00   sec  10.2 MBytes  86.0 Mbits/sec    0    636 KBytes       
    [  5]   5.00-6.00   sec  9.50 MBytes  79.7 Mbits/sec    0    679 KBytes       
    [  5]   6.00-7.00   sec  11.0 MBytes  92.3 Mbits/sec    0    711 KBytes       
    [  5]   7.00-8.00   sec  9.88 MBytes  82.8 Mbits/sec    0    711 KBytes       
    [  5]   8.00-9.00   sec  8.62 MBytes  72.4 Mbits/sec    0    711 KBytes       
    [  5]   9.00-10.00  sec  10.1 MBytes  84.8 Mbits/sec    0    749 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   102 MBytes  86.0 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  99.1 MBytes  83.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 81811 bytes (289 packets)
    TX: 51544 bytes (212 packets)
    signal: -34 dBm
    rx bitrate: 121.5 MBit/s MCS 6 40MHz
    tx bitrate: 150.0 MBit/s MCS 7 40MHz short GI
    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">41.5</span> Mbits/sec | <span style="font-size: 1.5rem;">34.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.109 port 52805 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.50 MBytes  37.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.00 MBytes  41.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.09  sec  50.0 MBytes  41.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  48.0 MBytes  40.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.109 port 60887 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.25 MBytes  35.6 Mbits/sec    0    211 KBytes       
    [  5]   1.00-2.00   sec  4.00 MBytes  33.6 Mbits/sec    0    277 KBytes       
    [  5]   2.00-3.00   sec  3.62 MBytes  30.4 Mbits/sec    0    320 KBytes       
    [  5]   3.00-4.00   sec  2.62 MBytes  22.0 Mbits/sec    0    320 KBytes       
    [  5]   4.00-5.00   sec  3.25 MBytes  27.3 Mbits/sec    0    320 KBytes       
    [  5]   5.00-6.00   sec  3.38 MBytes  28.3 Mbits/sec    0    320 KBytes       
    [  5]   6.00-7.00   sec  4.88 MBytes  40.9 Mbits/sec    0    337 KBytes       
    [  5]   7.00-8.00   sec  4.88 MBytes  40.9 Mbits/sec    0    337 KBytes       
    [  5]   8.00-9.00   sec  4.75 MBytes  39.8 Mbits/sec    0    337 KBytes       
    [  5]   9.00-10.00  sec  6.00 MBytes  50.3 Mbits/sec    0    533 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  41.6 MBytes  34.9 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  39.0 MBytes  32.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 100098 bytes (361 packets)
    TX: 51838 bytes (203 packets)
    signal: 0 dBm
    rx bitrate: 58.5 MBit/s MCS 6
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">140</span> Mbits/sec | <span style="font-size: 1.5rem;">139</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 45391 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.3 MBytes   128 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.3 MBytes   137 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.0 MBytes   135 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   9.00-10.00  sec  15.6 MBytes   131 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   167 MBytes   140 Mbits/sec  452             sender
    [  5]   0.00-10.00  sec   163 MBytes   137 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 39661 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.0 MBytes   151 Mbits/sec    0    403 KBytes       
    [  5]   1.00-2.00   sec  16.9 MBytes   142 Mbits/sec    0    403 KBytes       
    [  5]   2.00-3.00   sec  16.3 MBytes   137 Mbits/sec    0    423 KBytes       
    [  5]   3.00-4.00   sec  16.0 MBytes   134 Mbits/sec    0    423 KBytes       
    [  5]   4.00-5.00   sec  16.8 MBytes   141 Mbits/sec    0    423 KBytes       
    [  5]   5.00-6.00   sec  15.7 MBytes   132 Mbits/sec    0    423 KBytes       
    [  5]   6.00-7.00   sec  16.0 MBytes   134 Mbits/sec    0    423 KBytes       
    [  5]   7.00-8.00   sec  16.7 MBytes   140 Mbits/sec    0    423 KBytes       
    [  5]   8.00-9.00   sec  16.0 MBytes   134 Mbits/sec    0    423 KBytes       
    [  5]   9.00-10.00  sec  16.7 MBytes   140 Mbits/sec    0    423 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   165 MBytes   139 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   163 MBytes   137 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 309243875 bytes (254697 packets)
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
