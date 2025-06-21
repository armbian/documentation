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
**Test Date:** [2025-06-21 01:48 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15790377144)
### AC

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">272</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 42177 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   5.00-6.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.8 MBytes   166 Mbits/sec                  
    [  5]   7.00-8.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   9.00-10.00  sec  19.4 MBytes   163 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   183 MBytes   153 Mbits/sec   78             sender
    [  5]   0.00-10.00  sec   181 MBytes   152 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 54593 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.9 MBytes   292 Mbits/sec    0   1.23 MBytes       
    [  5]   1.00-2.00   sec  31.6 MBytes   265 Mbits/sec    0   1.23 MBytes       
    [  5]   2.00-3.00   sec  32.8 MBytes   275 Mbits/sec    0   1.23 MBytes       
    [  5]   3.00-4.00   sec  31.6 MBytes   265 Mbits/sec    0   1.23 MBytes       
    [  5]   4.00-5.00   sec  32.9 MBytes   276 Mbits/sec    0   1.29 MBytes       
    [  5]   5.00-6.00   sec  31.6 MBytes   265 Mbits/sec    0   1.29 MBytes       
    [  5]   6.00-7.00   sec  31.6 MBytes   265 Mbits/sec    0   1.29 MBytes       
    [  5]   7.00-8.00   sec  32.9 MBytes   276 Mbits/sec    0   1.29 MBytes       
    [  5]   8.00-9.00   sec  31.6 MBytes   265 Mbits/sec    0   1.29 MBytes       
    [  5]   9.00-10.00  sec  32.8 MBytes   275 Mbits/sec    0   1.29 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   324 MBytes   272 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   322 MBytes   269 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 186854 bytes (342 packets)
    TX: 93573 bytes (455 packets)
    signal: -37 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">154</span> Mbits/sec | <span style="font-size: 1.5rem;">199</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 54667 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.8 MBytes   157 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   184 MBytes   154 Mbits/sec    2             sender
    [  5]   0.00-10.00  sec   181 MBytes   152 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 45917 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  26.1 MBytes   219 Mbits/sec    0    608 KBytes       
    [  5]   1.00-2.00   sec  22.9 MBytes   192 Mbits/sec    0    608 KBytes       
    [  5]   2.00-3.00   sec  24.0 MBytes   201 Mbits/sec    0    724 KBytes       
    [  5]   3.00-4.00   sec  24.0 MBytes   201 Mbits/sec    0    724 KBytes       
    [  5]   4.00-5.00   sec  22.6 MBytes   190 Mbits/sec    0    724 KBytes       
    [  5]   5.00-6.00   sec  23.6 MBytes   198 Mbits/sec    0    724 KBytes       
    [  5]   6.00-7.00   sec  24.1 MBytes   202 Mbits/sec    0    768 KBytes       
    [  5]   7.00-8.00   sec  22.8 MBytes   191 Mbits/sec    0    810 KBytes       
    [  5]   8.00-9.00   sec  23.8 MBytes   199 Mbits/sec    0    810 KBytes       
    [  5]   9.00-10.00  sec  23.9 MBytes   200 Mbits/sec    0    810 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   238 MBytes   199 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   235 MBytes   197 Mbits/sec                  receiver
    
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
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">155</span> Mbits/sec | <span style="font-size: 1.5rem;">272</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 47975 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.0 MBytes   151 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   186 MBytes   155 Mbits/sec    5             sender
    [  5]   0.00-10.00  sec   182 MBytes   153 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 44373 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.0 MBytes   285 Mbits/sec    0    776 KBytes       
    [  5]   1.00-2.00   sec  32.5 MBytes   273 Mbits/sec    0    922 KBytes       
    [  5]   2.00-3.00   sec  31.6 MBytes   265 Mbits/sec    0    922 KBytes       
    [  5]   3.00-4.00   sec  32.1 MBytes   269 Mbits/sec    0   1.00 MBytes       
    [  5]   4.00-5.00   sec  32.2 MBytes   271 Mbits/sec    0   1.06 MBytes       
    [  5]   5.00-6.00   sec  31.5 MBytes   264 Mbits/sec    0   1.12 MBytes       
    [  5]   6.00-7.00   sec  32.9 MBytes   276 Mbits/sec    0   1.12 MBytes       
    [  5]   7.00-8.00   sec  32.1 MBytes   269 Mbits/sec    0   1.12 MBytes       
    [  5]   8.00-9.00   sec  32.9 MBytes   276 Mbits/sec    0   1.12 MBytes       
    [  5]   9.00-10.00  sec  31.9 MBytes   267 Mbits/sec    0   1.18 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   324 MBytes   272 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   321 MBytes   269 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -36 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8821CU #1

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">124</span> Mbits/sec | <span style="font-size: 1.5rem;">217</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 56973 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.5 MBytes  88.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   3.00-4.00   sec  14.9 MBytes   125 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.5 MBytes   138 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.4 MBytes   137 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   148 MBytes   124 Mbits/sec    4             sender
    [  5]   0.00-10.00  sec   147 MBytes   123 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 57047 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  30.8 MBytes   258 Mbits/sec    0    912 KBytes       
    [  5]   1.00-2.00   sec  26.1 MBytes   219 Mbits/sec    0    912 KBytes       
    [  5]   2.00-3.00   sec  24.8 MBytes   208 Mbits/sec    0    912 KBytes       
    [  5]   3.00-4.00   sec  24.9 MBytes   209 Mbits/sec    0    912 KBytes       
    [  5]   4.00-5.00   sec  26.2 MBytes   220 Mbits/sec    0    912 KBytes       
    [  5]   5.00-6.00   sec  24.8 MBytes   208 Mbits/sec    0    912 KBytes       
    [  5]   6.00-7.00   sec  24.6 MBytes   207 Mbits/sec    0    912 KBytes       
    [  5]   7.00-8.00   sec  26.1 MBytes   219 Mbits/sec    0    912 KBytes       
    [  5]   8.00-9.00   sec  26.1 MBytes   219 Mbits/sec    0    912 KBytes       
    [  5]   9.00-10.00  sec  24.6 MBytes   206 Mbits/sec    0    912 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   259 MBytes   217 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   256 MBytes   215 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 73116 bytes (221 packets)
    TX: 53488 bytes (191 packets)
    signal: -38 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">113</span> Mbits/sec | <span style="font-size: 1.5rem;">149</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 33175 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.1 MBytes   110 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   135 MBytes   113 Mbits/sec  160             sender
    [  5]   0.00-10.00  sec   132 MBytes   111 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 53727 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.6 MBytes   156 Mbits/sec    0    515 KBytes       
    [  5]   1.00-2.00   sec  18.2 MBytes   153 Mbits/sec    0    594 KBytes       
    [  5]   2.00-3.00   sec  17.9 MBytes   150 Mbits/sec    0    778 KBytes       
    [  5]   3.00-4.00   sec  16.6 MBytes   139 Mbits/sec    0    857 KBytes       
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec    0    898 KBytes       
    [  5]   5.00-6.00   sec  16.6 MBytes   139 Mbits/sec    0    947 KBytes       
    [  5]   6.00-7.00   sec  19.1 MBytes   161 Mbits/sec    0   1011 KBytes       
    [  5]   7.00-8.00   sec  16.9 MBytes   142 Mbits/sec    0   1011 KBytes       
    [  5]   8.00-9.00   sec  18.2 MBytes   153 Mbits/sec    0   1011 KBytes       
    [  5]   9.00-10.00  sec  16.9 MBytes   142 Mbits/sec    0   1.04 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   177 MBytes   149 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   175 MBytes   146 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 156098 bytes (479 packets)
    TX: 90721 bytes (515 packets)
    signal: -38 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">94.4</span> Mbits/sec | <span style="font-size: 1.5rem;">65.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 44915 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.2 MBytes  85.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.1 MBytes  93.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.1 MBytes  93.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.5 MBytes  96.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   113 MBytes  94.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   110 MBytes  92.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 54885 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.50 MBytes  71.3 Mbits/sec    0    201 KBytes       
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec    0    269 KBytes       
    [  5]   2.00-3.00   sec  7.75 MBytes  65.0 Mbits/sec    0    294 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0    294 KBytes       
    [  5]   4.00-5.00   sec  7.38 MBytes  61.9 Mbits/sec    0    294 KBytes       
    [  5]   5.00-6.00   sec  8.12 MBytes  68.2 Mbits/sec    0    294 KBytes       
    [  5]   6.00-7.00   sec  7.62 MBytes  64.0 Mbits/sec    0    325 KBytes       
    [  5]   7.00-8.00   sec  8.25 MBytes  69.2 Mbits/sec    0    325 KBytes       
    [  5]   8.00-9.00   sec  8.00 MBytes  67.1 Mbits/sec    0    406 KBytes       
    [  5]   9.00-10.00  sec  7.38 MBytes  61.9 Mbits/sec    0    460 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  77.9 MBytes  65.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  76.1 MBytes  63.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 92057 bytes (387 packets)
    TX: 58991 bytes (281 packets)
    signal: -19 dBm
    rx bitrate: 243.0 MBit/s MCS 14 40MHz
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">34.5</span> Mbits/sec | <span style="font-size: 1.5rem;">37.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 52835 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.62 MBytes  13.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.12 MBytes  26.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.00 MBytes  33.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.00 MBytes  33.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  41.2 MBytes  34.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  38.5 MBytes  32.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 42195 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.25 MBytes  44.0 Mbits/sec    0    272 KBytes       
    [  5]   1.00-2.00   sec  5.38 MBytes  45.1 Mbits/sec    0    496 KBytes       
    [  5]   2.00-3.00   sec  5.88 MBytes  49.3 Mbits/sec    0    677 KBytes       
    [  5]   3.00-4.00   sec  2.75 MBytes  23.1 Mbits/sec    0    846 KBytes       
    [  5]   4.00-5.00   sec  4.00 MBytes  33.6 Mbits/sec    0   1004 KBytes       
    [  5]   5.00-6.00   sec  2.75 MBytes  23.1 Mbits/sec    0   1.09 MBytes       
    [  5]   6.00-7.00   sec  4.25 MBytes  35.7 Mbits/sec    0   1.21 MBytes       
    [  5]   7.00-8.00   sec  5.62 MBytes  47.2 Mbits/sec    8    946 KBytes       
    [  5]   8.00-9.00   sec  4.25 MBytes  35.6 Mbits/sec    0    993 KBytes       
    [  5]   9.00-10.00  sec  4.62 MBytes  38.8 Mbits/sec    8    738 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  44.8 MBytes  37.5 Mbits/sec   16             sender
    [  5]   0.00-10.00  sec  41.4 MBytes  34.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 82941 bytes (337 packets)
    TX: 57524 bytes (226 packets)
    signal: -33 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 65.0 MBit/s MCS 6 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">92.5</span> Mbits/sec | <span style="font-size: 1.5rem;">67.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 49605 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.12 MBytes  76.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.8 MBytes  90.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.8 MBytes  98.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   110 MBytes  92.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   108 MBytes  90.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 48763 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.62 MBytes  72.2 Mbits/sec    0    239 KBytes       
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec    0    290 KBytes       
    [  5]   2.00-3.00   sec  8.12 MBytes  68.2 Mbits/sec    0    362 KBytes       
    [  5]   3.00-4.00   sec  8.50 MBytes  71.3 Mbits/sec    0    382 KBytes       
    [  5]   4.00-5.00   sec  7.88 MBytes  66.1 Mbits/sec    0    438 KBytes       
    [  5]   5.00-6.00   sec  8.00 MBytes  67.1 Mbits/sec    0    438 KBytes       
    [  5]   6.00-7.00   sec  8.00 MBytes  67.1 Mbits/sec    0    438 KBytes       
    [  5]   7.00-8.00   sec  8.25 MBytes  69.2 Mbits/sec    0    438 KBytes       
    [  5]   8.00-9.00   sec  7.38 MBytes  61.9 Mbits/sec    0    438 KBytes       
    [  5]   9.00-10.00  sec  8.12 MBytes  68.1 Mbits/sec    0    438 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  80.2 MBytes  67.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  78.0 MBytes  65.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 95735 bytes (404 packets)
    TX: 57462 bytes (271 packets)
    signal: -26 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">23.3</span> Mbits/sec | <span style="font-size: 1.5rem;">42.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 41341 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  2.25 MBytes  18.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  2.50 MBytes  21.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.38 MBytes  19.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.50 MBytes  21.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.50 MBytes  21.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.50 MBytes  21.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.12 MBytes  17.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.50 MBytes  21.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.50 MBytes  21.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.62 MBytes  22.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.13  sec  28.1 MBytes  23.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  24.4 MBytes  20.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 47945 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.50 MBytes  37.7 Mbits/sec    0    233 KBytes       
    [  5]   1.00-2.00   sec  5.38 MBytes  45.1 Mbits/sec    0    351 KBytes       
    [  5]   2.00-3.00   sec  5.38 MBytes  45.1 Mbits/sec    0    461 KBytes       
    [  5]   3.00-4.00   sec  5.75 MBytes  48.2 Mbits/sec    0    461 KBytes       
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec    0    492 KBytes       
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec    0    492 KBytes       
    [  5]   6.00-7.00   sec  4.62 MBytes  38.8 Mbits/sec    0    523 KBytes       
    [  5]   7.00-8.00   sec  4.50 MBytes  37.7 Mbits/sec    0    556 KBytes       
    [  5]   8.00-9.00   sec  5.62 MBytes  47.2 Mbits/sec    0    556 KBytes       
    [  5]   9.00-10.00  sec  4.50 MBytes  37.7 Mbits/sec    0    556 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  50.4 MBytes  42.3 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  47.8 MBytes  39.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 72334 bytes (237 packets)
    TX: 47858 bytes (200 packets)
    signal: -38 dBm
    rx bitrate: 58.5 MBit/s MCS 6
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">33.1</span> Mbits/sec | <span style="font-size: 1.5rem;">43.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 36873 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.62 MBytes  30.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  3.62 MBytes  30.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.25 MBytes  35.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.88 MBytes  32.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.12  sec  40.0 MBytes  33.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  38.0 MBytes  31.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 44261 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.62 MBytes  47.1 Mbits/sec    0    218 KBytes       
    [  5]   1.00-2.00   sec  5.75 MBytes  48.2 Mbits/sec    0    328 KBytes       
    [  5]   2.00-3.00   sec  5.62 MBytes  47.2 Mbits/sec    0    363 KBytes       
    [  5]   3.00-4.00   sec  4.75 MBytes  39.8 Mbits/sec    0    386 KBytes       
    [  5]   4.00-5.00   sec  4.75 MBytes  39.8 Mbits/sec    0    386 KBytes       
    [  5]   5.00-6.00   sec  4.88 MBytes  40.9 Mbits/sec    0    406 KBytes       
    [  5]   6.00-7.00   sec  5.25 MBytes  44.0 Mbits/sec    0    426 KBytes       
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec    0    426 KBytes       
    [  5]   8.00-9.00   sec  4.38 MBytes  36.7 Mbits/sec    0    426 KBytes       
    [  5]   9.00-10.00  sec  5.25 MBytes  44.0 Mbits/sec    0    426 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  51.5 MBytes  43.2 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  49.6 MBytes  41.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 93435 bytes (323 packets)
    TX: 50538 bytes (212 packets)
    signal: 0 dBm
    rx bitrate: 65.0 MBit/s MCS 7
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
