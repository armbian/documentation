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
**Test Date:** [2025-05-13 11:54 UTC](https://github.com/armbian/armbian.github.io/actions/runs/14995513446)
### AC

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">272</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 46735 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.4 MBytes   154 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   183 MBytes   153 Mbits/sec  102             sender
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 34829 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.4 MBytes   288 Mbits/sec    0   1.74 MBytes       
    [  5]   1.00-2.00   sec  32.1 MBytes   270 Mbits/sec    0   2.29 MBytes       
    [  5]   2.00-3.00   sec  33.1 MBytes   278 Mbits/sec    0   2.29 MBytes       
    [  5]   3.00-4.00   sec  30.9 MBytes   259 Mbits/sec   26   1.60 MBytes       
    [  5]   4.00-5.00   sec  33.0 MBytes   277 Mbits/sec    0   1.60 MBytes       
    [  5]   5.00-6.00   sec  31.5 MBytes   264 Mbits/sec    0   1.60 MBytes       
    [  5]   6.00-7.00   sec  32.9 MBytes   276 Mbits/sec    0   1.60 MBytes       
    [  5]   7.00-8.00   sec  31.6 MBytes   265 Mbits/sec    0   1.60 MBytes       
    [  5]   8.00-9.00   sec  32.9 MBytes   276 Mbits/sec    0   1.60 MBytes       
    [  5]   9.00-10.00  sec  31.5 MBytes   264 Mbits/sec    0   1.60 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   324 MBytes   272 Mbits/sec   26             sender
    [  5]   0.00-10.03  sec   322 MBytes   269 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 206623 bytes (393 packets)
    TX: 108788 bytes (497 packets)
    signal: 0 dBm
    rx bitrate: 173.4 MBit/s VHT-MCS 9 VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">200</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 48381 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  14.9 MBytes   125 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.5 MBytes   155 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   183 MBytes   153 Mbits/sec   28             sender
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 38943 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  26.0 MBytes   218 Mbits/sec    0    669 KBytes       
    [  5]   1.00-2.00   sec  23.2 MBytes   195 Mbits/sec    0    669 KBytes       
    [  5]   2.00-3.00   sec  23.6 MBytes   198 Mbits/sec    0    751 KBytes       
    [  5]   3.00-4.00   sec  23.6 MBytes   198 Mbits/sec    0    751 KBytes       
    [  5]   4.00-5.00   sec  23.9 MBytes   200 Mbits/sec    0    793 KBytes       
    [  5]   5.00-6.00   sec  23.4 MBytes   196 Mbits/sec    0    793 KBytes       
    [  5]   6.00-7.00   sec  23.5 MBytes   197 Mbits/sec    0    793 KBytes       
    [  5]   7.00-8.00   sec  23.6 MBytes   198 Mbits/sec    0    793 KBytes       
    [  5]   8.00-9.00   sec  23.8 MBytes   199 Mbits/sec    0    916 KBytes       
    [  5]   9.00-10.00  sec  23.6 MBytes   198 Mbits/sec    0    916 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   238 MBytes   200 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   235 MBytes   197 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -29 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">150</span> Mbits/sec | <span style="font-size: 1.5rem;">273</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 51571 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.4 MBytes   129 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.9 MBytes   150 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   179 MBytes   150 Mbits/sec    3             sender
    [  5]   0.00-10.00  sec   177 MBytes   149 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 51879 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  33.8 MBytes   283 Mbits/sec    0    969 KBytes       
    [  5]   1.00-2.00   sec  33.8 MBytes   283 Mbits/sec    0   1.06 MBytes       
    [  5]   2.00-3.00   sec  30.6 MBytes   257 Mbits/sec    0   1.19 MBytes       
    [  5]   3.00-4.00   sec  32.5 MBytes   273 Mbits/sec    0   1.27 MBytes       
    [  5]   4.00-5.00   sec  32.9 MBytes   276 Mbits/sec    0   1.41 MBytes       
    [  5]   5.00-6.00   sec  32.9 MBytes   276 Mbits/sec    0   1.41 MBytes       
    [  5]   6.00-7.00   sec  31.9 MBytes   267 Mbits/sec    0   1.50 MBytes       
    [  5]   7.00-8.00   sec  32.9 MBytes   276 Mbits/sec    0   1.50 MBytes       
    [  5]   8.00-9.00   sec  31.6 MBytes   265 Mbits/sec    0   1.50 MBytes       
    [  5]   9.00-10.00  sec  32.5 MBytes   273 Mbits/sec    0   1.59 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   325 MBytes   273 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   323 MBytes   270 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -34 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8814AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">74.5</span> Mbits/sec | <span style="font-size: 1.5rem;">5.66</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.106 port 40123 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.9 MBytes  91.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  7.88 MBytes  66.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  7.88 MBytes  66.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  8.00 MBytes  67.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  8.12 MBytes  68.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  8.62 MBytes  72.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  9.00 MBytes  75.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  8.25 MBytes  69.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.32  sec  91.6 MBytes  74.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  87.6 MBytes  73.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.106 port 38443 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec   640 KBytes  5.24 Mbits/sec    0   65.0 KBytes       
    [  5]   1.00-2.00   sec   768 KBytes  6.29 Mbits/sec    0   90.5 KBytes       
    [  5]   2.00-3.00   sec   512 KBytes  4.19 Mbits/sec    0    113 KBytes       
    [  5]   3.00-4.00   sec  1.00 MBytes  8.39 Mbits/sec    0    147 KBytes       
    [  5]   4.00-5.00   sec   640 KBytes  5.24 Mbits/sec    0    177 KBytes       
    [  5]   5.00-6.00   sec   384 KBytes  3.15 Mbits/sec    0    205 KBytes       
    [  5]   6.00-7.00   sec  1.00 MBytes  8.39 Mbits/sec    0    235 KBytes       
    [  5]   7.00-8.00   sec   512 KBytes  4.19 Mbits/sec    0    283 KBytes       
    [  5]   8.00-9.00   sec  1.38 MBytes  11.5 Mbits/sec    0    345 KBytes       
    [  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0    345 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  6.75 MBytes  5.66 Mbits/sec    0             sender
    [  5]   0.00-10.42  sec  5.62 MBytes  4.53 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    signal: -35 dBm
    tx bitrate: 174.0 MBit/s
    ```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">112</span> Mbits/sec | <span style="font-size: 1.5rem;">149</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.117 port 45429 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.2 MBytes   111 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   134 MBytes   112 Mbits/sec   30             sender
    [  5]   0.00-10.00  sec   132 MBytes   110 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.117 port 56851 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.6 MBytes   165 Mbits/sec    0    574 KBytes       
    [  5]   1.00-2.00   sec  17.0 MBytes   143 Mbits/sec    0    789 KBytes       
    [  5]   2.00-3.00   sec  17.0 MBytes   143 Mbits/sec    0    830 KBytes       
    [  5]   3.00-4.00   sec  18.6 MBytes   156 Mbits/sec    0   1018 KBytes       
    [  5]   4.00-5.00   sec  17.9 MBytes   150 Mbits/sec    0   1.07 MBytes       
    [  5]   5.00-6.00   sec  17.2 MBytes   145 Mbits/sec    0   1.13 MBytes       
    [  5]   6.00-7.00   sec  17.8 MBytes   149 Mbits/sec    0   1.13 MBytes       
    [  5]   7.00-8.00   sec  17.0 MBytes   143 Mbits/sec    0   1.19 MBytes       
    [  5]   8.00-9.00   sec  17.4 MBytes   146 Mbits/sec    0   1.19 MBytes       
    [  5]   9.00-10.00  sec  18.0 MBytes   151 Mbits/sec    0   1.25 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   178 MBytes   149 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   174 MBytes   146 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 43342 bytes (138 packets)
    TX: 48181 bytes (203 packets)
    signal: -43 dBm
    rx bitrate: 1080.6 MBit/s 80MHz HE-MCS 10 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">917</span> Mbits/sec | <span style="font-size: 1.5rem;">771</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 56983 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   110 MBytes   918 Mbits/sec                  
    [  5]   1.00-2.00   sec   111 MBytes   933 Mbits/sec                  
    [  5]   2.00-3.00   sec   111 MBytes   930 Mbits/sec                  
    [  5]   3.00-4.00   sec   110 MBytes   923 Mbits/sec                  
    [  5]   4.00-5.00   sec   108 MBytes   909 Mbits/sec                  
    [  5]   5.00-6.00   sec   107 MBytes   895 Mbits/sec                  
    [  5]   6.00-7.00   sec   107 MBytes   894 Mbits/sec                  
    [  5]   7.00-8.00   sec   110 MBytes   921 Mbits/sec                  
    [  5]   8.00-9.00   sec   108 MBytes   905 Mbits/sec                  
    [  5]   9.00-10.00  sec   109 MBytes   917 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  1.07 GBytes   917 Mbits/sec  357             sender
    [  5]   0.00-10.00  sec  1.06 GBytes   915 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 47823 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  97.9 MBytes   820 Mbits/sec  163    672 KBytes       
    [  5]   1.00-2.00   sec  94.0 MBytes   789 Mbits/sec  135    614 KBytes       
    [  5]   2.00-3.00   sec  89.2 MBytes   749 Mbits/sec  137    566 KBytes       
    [  5]   3.00-4.00   sec  92.2 MBytes   774 Mbits/sec  114    542 KBytes       
    [  5]   4.00-5.00   sec  85.1 MBytes   714 Mbits/sec  119    262 KBytes       
    [  5]   5.00-6.00   sec  83.9 MBytes   704 Mbits/sec    0    559 KBytes       
    [  5]   6.00-7.00   sec  94.5 MBytes   793 Mbits/sec  187    477 KBytes       
    [  5]   7.00-8.00   sec  93.6 MBytes   785 Mbits/sec  157    428 KBytes       
    [  5]   8.00-9.00   sec  95.1 MBytes   798 Mbits/sec  150    395 KBytes       
    [  5]   9.00-10.00  sec  93.6 MBytes   785 Mbits/sec  146    361 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   919 MBytes   771 Mbits/sec  1308             sender
    [  5]   0.00-10.01  sec   917 MBytes   769 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 55585 bytes (193 packets)
    TX: 47538 bytes (207 packets)
    signal: -29 dBm
    rx bitrate: 1729.6 MBit/s 160MHz HE-MCS 8 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">98.0</span> Mbits/sec | <span style="font-size: 1.5rem;">67.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.114 port 51755 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.5 MBytes  88.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.5 MBytes  96.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.8 MBytes  98.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   117 MBytes  98.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   114 MBytes  95.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.114 port 34847 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.88 MBytes  74.4 Mbits/sec    0    247 KBytes       
    [  5]   1.00-2.00   sec  8.00 MBytes  67.1 Mbits/sec    0    294 KBytes       
    [  5]   2.00-3.00   sec  8.12 MBytes  68.1 Mbits/sec    0    310 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  63.0 Mbits/sec    0    310 KBytes       
    [  5]   4.00-5.00   sec  8.50 MBytes  71.3 Mbits/sec    0    325 KBytes       
    [  5]   5.00-6.00   sec  7.50 MBytes  62.9 Mbits/sec    0    325 KBytes       
    [  5]   6.00-7.00   sec  8.12 MBytes  68.2 Mbits/sec    0    395 KBytes       
    [  5]   7.00-8.00   sec  8.12 MBytes  68.2 Mbits/sec    0    395 KBytes       
    [  5]   8.00-9.00   sec  7.50 MBytes  62.9 Mbits/sec    0    395 KBytes       
    [  5]   9.00-10.00  sec  8.00 MBytes  67.0 Mbits/sec    0    395 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  80.2 MBytes  67.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  78.5 MBytes  65.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 214699 bytes (649 packets)
    TX: 99154 bytes (536 packets)
    signal: -19 dBm
    rx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Atheros AR9271

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">57.7</span> Mbits/sec | <span style="font-size: 1.5rem;">50.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.113 port 53099 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.38 MBytes  53.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.38 MBytes  53.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.75 MBytes  56.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.62 MBytes  55.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  68.9 MBytes  57.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  65.6 MBytes  55.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.113 port 60027 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.50 MBytes  54.5 Mbits/sec    0    182 KBytes       
    [  5]   1.00-2.00   sec  6.25 MBytes  52.5 Mbits/sec    0    219 KBytes       
    [  5]   2.00-3.00   sec  6.25 MBytes  52.4 Mbits/sec    0    219 KBytes       
    [  5]   3.00-4.00   sec  5.62 MBytes  47.2 Mbits/sec    0    219 KBytes       
    [  5]   4.00-5.00   sec  6.12 MBytes  51.4 Mbits/sec    0    219 KBytes       
    [  5]   5.00-6.00   sec  5.88 MBytes  49.3 Mbits/sec    0    219 KBytes       
    [  5]   6.00-7.00   sec  5.25 MBytes  44.0 Mbits/sec    0    219 KBytes       
    [  5]   7.00-8.00   sec  6.50 MBytes  54.5 Mbits/sec    0    328 KBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0    328 KBytes       
    [  5]   9.00-10.00  sec  5.38 MBytes  45.1 Mbits/sec    0    328 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  60.0 MBytes  50.3 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  58.8 MBytes  49.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 75519 bytes (288 packets)
    TX: 54125 bytes (204 packets)
    signal: -50 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">39.8</span> Mbits/sec | <span style="font-size: 1.5rem;">42.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.112 port 35661 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.88 MBytes  15.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.75 MBytes  39.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.50 MBytes  37.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.50 MBytes  37.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.21  sec  48.5 MBytes  39.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  43.4 MBytes  36.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.112 port 36571 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.50 MBytes  54.5 Mbits/sec    0    308 KBytes       
    [  5]   1.00-2.00   sec  5.50 MBytes  46.1 Mbits/sec    0    543 KBytes       
    [  5]   2.00-3.00   sec  6.62 MBytes  55.6 Mbits/sec    0    765 KBytes       
    [  5]   3.00-4.00   sec  4.12 MBytes  34.6 Mbits/sec    0    943 KBytes       
    [  5]   4.00-5.00   sec  4.25 MBytes  35.6 Mbits/sec    0   1.01 MBytes       
    [  5]   5.00-6.00   sec  5.50 MBytes  46.1 Mbits/sec    0   1.04 MBytes       
    [  5]   6.00-7.00   sec  4.25 MBytes  35.7 Mbits/sec    0   1.22 MBytes       
    [  5]   7.00-8.00   sec  5.50 MBytes  46.1 Mbits/sec    1    938 KBytes       
    [  5]   8.00-9.00   sec  4.62 MBytes  38.8 Mbits/sec    2    686 KBytes       
    [  5]   9.00-10.00  sec  4.25 MBytes  35.6 Mbits/sec    0    744 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  51.1 MBytes  42.9 Mbits/sec    3             sender
    [  5]   0.00-10.01  sec  48.5 MBytes  40.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 73944 bytes (288 packets)
    TX: 49576 bytes (208 packets)
    signal: -29 dBm
    rx bitrate: 65.0 MBit/s MCS 6 short GI
    tx bitrate: 65.0 MBit/s MCS 7
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">98.3</span> Mbits/sec | <span style="font-size: 1.5rem;">68.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.111 port 54747 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.2 MBytes  94.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.4 MBytes  95.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.2 MBytes  94.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.4 MBytes  95.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.8 MBytes  98.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.5 MBytes  96.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.4 MBytes  95.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   117 MBytes  98.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   114 MBytes  96.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.111 port 39507 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.38 MBytes  78.6 Mbits/sec    0    232 KBytes       
    [  5]   1.00-2.00   sec  7.88 MBytes  66.1 Mbits/sec    0    253 KBytes       
    [  5]   2.00-3.00   sec  8.12 MBytes  68.2 Mbits/sec    0    269 KBytes       
    [  5]   3.00-4.00   sec  7.75 MBytes  65.0 Mbits/sec    0    269 KBytes       
    [  5]   4.00-5.00   sec  8.00 MBytes  67.1 Mbits/sec    0    280 KBytes       
    [  5]   5.00-6.00   sec  8.50 MBytes  71.3 Mbits/sec    0    291 KBytes       
    [  5]   6.00-7.00   sec  8.12 MBytes  68.2 Mbits/sec    0    315 KBytes       
    [  5]   7.00-8.00   sec  8.38 MBytes  70.3 Mbits/sec    0    315 KBytes       
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec    0    315 KBytes       
    [  5]   9.00-10.00  sec  8.12 MBytes  68.1 Mbits/sec    0    315 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  81.9 MBytes  68.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  80.4 MBytes  67.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 223878 bytes (686 packets)
    TX: 107951 bytes (541 packets)
    signal: -32 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">43.7</span> Mbits/sec | <span style="font-size: 1.5rem;">35.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.110 port 38995 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.12 MBytes  34.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.35  sec  53.9 MBytes  43.7 Mbits/sec   90             sender
    [  5]   0.00-10.00  sec  50.2 MBytes  42.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.110 port 49719 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.62 MBytes  38.8 Mbits/sec    0    236 KBytes       
    [  5]   1.00-2.00   sec  4.00 MBytes  33.6 Mbits/sec    0    291 KBytes       
    [  5]   2.00-3.00   sec  4.00 MBytes  33.6 Mbits/sec    0    328 KBytes       
    [  5]   3.00-4.00   sec  4.12 MBytes  34.6 Mbits/sec    0    346 KBytes       
    [  5]   4.00-5.00   sec  4.50 MBytes  37.7 Mbits/sec    0    363 KBytes       
    [  5]   5.00-6.00   sec  3.75 MBytes  31.5 Mbits/sec    0    383 KBytes       
    [  5]   6.00-7.00   sec  4.00 MBytes  33.6 Mbits/sec    0    383 KBytes       
    [  5]   7.00-8.00   sec  4.62 MBytes  38.8 Mbits/sec    0    383 KBytes       
    [  5]   8.00-9.00   sec  4.12 MBytes  34.6 Mbits/sec    0    383 KBytes       
    [  5]   9.00-10.00  sec  4.38 MBytes  36.7 Mbits/sec    0    510 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  42.1 MBytes  35.3 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  40.2 MBytes  33.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 104573 bytes (351 packets)
    TX: 51543 bytes (210 packets)
    signal: -28 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">29.3</span> Mbits/sec | <span style="font-size: 1.5rem;">42.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.109 port 60739 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.25 MBytes  27.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.62 MBytes  30.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.75 MBytes  31.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.07  sec  35.1 MBytes  29.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  32.5 MBytes  27.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.109 port 48323 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.00 MBytes  41.9 Mbits/sec    0    257 KBytes       
    [  5]   1.00-2.00   sec  5.62 MBytes  47.2 Mbits/sec    1    232 KBytes       
    [  5]   2.00-3.00   sec  4.25 MBytes  35.7 Mbits/sec    0    264 KBytes       
    [  5]   3.00-4.00   sec  5.12 MBytes  43.0 Mbits/sec    0    288 KBytes       
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec    0    301 KBytes       
    [  5]   5.00-6.00   sec  5.00 MBytes  41.9 Mbits/sec    0    305 KBytes       
    [  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec    0    305 KBytes       
    [  5]   7.00-8.00   sec  5.00 MBytes  41.9 Mbits/sec    0    305 KBytes       
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec    0    308 KBytes       
    [  5]   9.00-10.00  sec  5.12 MBytes  43.0 Mbits/sec    0    318 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  50.1 MBytes  42.0 Mbits/sec    1             sender
    [  5]   0.00-10.02  sec  48.5 MBytes  40.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 76282 bytes (291 packets)
    TX: 51971 bytes (206 packets)
    signal: -48 dBm
    rx bitrate: 52.0 MBit/s MCS 5
    tx bitrate: 72.2 MBit/s MCS 7 short GI
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
