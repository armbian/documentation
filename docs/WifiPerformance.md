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
**Test Date:** [2025-05-13 09:25 UTC](https://github.com/armbian/armbian.github.io/actions/runs/14992570685)
### AC

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">163</span> Mbits/sec | <span style="font-size: 1.5rem;">269</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 38511 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   1.00-2.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.4 MBytes   162 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   5.00-6.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   7.00-8.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   9.00-10.00  sec  19.5 MBytes   164 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   194 MBytes   163 Mbits/sec   12             sender
    [  5]   0.00-10.00  sec   191 MBytes   160 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 50815 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.1 MBytes   286 Mbits/sec    0    990 KBytes       
    [  5]   1.00-2.00   sec  31.6 MBytes   265 Mbits/sec    0   1.26 MBytes       
    [  5]   2.00-3.00   sec  31.6 MBytes   265 Mbits/sec    0   1.26 MBytes       
    [  5]   3.00-4.00   sec  32.9 MBytes   276 Mbits/sec    0   1.32 MBytes       
    [  5]   4.00-5.00   sec  31.8 MBytes   266 Mbits/sec    0   1.32 MBytes       
    [  5]   5.00-6.00   sec  32.9 MBytes   276 Mbits/sec    0   1.32 MBytes       
    [  5]   6.00-7.00   sec  31.6 MBytes   265 Mbits/sec    0   1.39 MBytes       
    [  5]   7.00-8.00   sec  31.5 MBytes   264 Mbits/sec    0   1.47 MBytes       
    [  5]   8.00-9.00   sec  31.5 MBytes   264 Mbits/sec    0   1.47 MBytes       
    [  5]   9.00-10.00  sec  31.6 MBytes   265 Mbits/sec    0   1.47 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   321 MBytes   269 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   319 MBytes   267 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 5500.0
    RX: 195541 bytes (431 packets)
    TX: 105903 bytes (489 packets)
    signal: -36 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">156</span> Mbits/sec | <span style="font-size: 1.5rem;">200</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 36405 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.2 MBytes   153 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   187 MBytes   156 Mbits/sec  187             sender
    [  5]   0.00-10.00  sec   184 MBytes   154 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 58541 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.0 MBytes   210 Mbits/sec    0    577 KBytes       
    [  5]   1.00-2.00   sec  23.4 MBytes   196 Mbits/sec    0    611 KBytes       
    [  5]   2.00-3.00   sec  24.6 MBytes   207 Mbits/sec    0    643 KBytes       
    [  5]   3.00-4.00   sec  22.4 MBytes   188 Mbits/sec    0    643 KBytes       
    [  5]   4.00-5.00   sec  23.4 MBytes   196 Mbits/sec    0    718 KBytes       
    [  5]   5.00-6.00   sec  24.9 MBytes   209 Mbits/sec    0    764 KBytes       
    [  5]   6.00-7.00   sec  23.6 MBytes   198 Mbits/sec    0    814 KBytes       
    [  5]   7.00-8.00   sec  22.6 MBytes   190 Mbits/sec    0    814 KBytes       
    [  5]   8.00-9.00   sec  24.0 MBytes   201 Mbits/sec    0    814 KBytes       
    [  5]   9.00-10.00  sec  24.0 MBytes   201 Mbits/sec    0    814 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   238 MBytes   200 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   235 MBytes   197 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 5500.0
    signal: -30 dBm
    tx bitrate: 434.0 MBit/s
```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">155</span> Mbits/sec | <span style="font-size: 1.5rem;">272</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 47603 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.0 MBytes   151 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   186 MBytes   155 Mbits/sec   33             sender
    [  5]   0.00-10.00  sec   182 MBytes   152 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 33419 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  33.8 MBytes   283 Mbits/sec    0    749 KBytes       
    [  5]   1.00-2.00   sec  31.6 MBytes   265 Mbits/sec    0    895 KBytes       
    [  5]   2.00-3.00   sec  32.0 MBytes   268 Mbits/sec    0   1012 KBytes       
    [  5]   3.00-4.00   sec  33.5 MBytes   281 Mbits/sec    0   1.04 MBytes       
    [  5]   4.00-5.00   sec  31.4 MBytes   263 Mbits/sec    0   1.04 MBytes       
    [  5]   5.00-6.00   sec  32.5 MBytes   272 Mbits/sec    0   1.16 MBytes       
    [  5]   6.00-7.00   sec  31.6 MBytes   265 Mbits/sec    0   1.16 MBytes       
    [  5]   7.00-8.00   sec  31.8 MBytes   266 Mbits/sec    0   1.22 MBytes       
    [  5]   8.00-9.00   sec  33.5 MBytes   281 Mbits/sec    0   1.30 MBytes       
    [  5]   9.00-10.00  sec  32.5 MBytes   273 Mbits/sec    0   1.30 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   324 MBytes   272 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   321 MBytes   269 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">75.1</span> Mbits/sec | <span style="font-size: 1.5rem;">6.08</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.106 port 60901 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.0 MBytes  92.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  8.25 MBytes  69.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.50 MBytes  71.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  8.50 MBytes  71.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  8.38 MBytes  70.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  8.88 MBytes  74.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  9.12 MBytes  76.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.12 MBytes  76.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.28  sec  92.1 MBytes  75.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  89.2 MBytes  74.9 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.106 port 57261 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec   896 KBytes  7.33 Mbits/sec    0   69.3 KBytes       
    [  5]   1.00-2.00   sec   512 KBytes  4.20 Mbits/sec    0   96.2 KBytes       
    [  5]   2.00-3.00   sec   768 KBytes  6.28 Mbits/sec    0    127 KBytes       
    [  5]   3.00-4.00   sec   768 KBytes  6.29 Mbits/sec    0    157 KBytes       
    [  5]   4.00-5.00   sec   896 KBytes  7.34 Mbits/sec    0    185 KBytes       
    [  5]   5.00-6.00   sec   384 KBytes  3.15 Mbits/sec    0    215 KBytes       
    [  5]   6.00-7.00   sec  1.12 MBytes  9.43 Mbits/sec    0    245 KBytes       
    [  5]   7.00-8.00   sec   512 KBytes  4.19 Mbits/sec    0    277 KBytes       
    [  5]   8.00-9.00   sec   768 KBytes  6.30 Mbits/sec    0    375 KBytes       
    [  5]   9.00-10.00  sec   768 KBytes  6.28 Mbits/sec    0    375 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  7.25 MBytes  6.08 Mbits/sec    0             sender
    [  5]   0.00-10.40  sec  5.88 MBytes  4.74 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 2462.0
    signal: -30 dBm
    tx bitrate: 174.0 MBit/s
```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">113</span> Mbits/sec | <span style="font-size: 1.5rem;">153</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.117 port 39819 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.1 MBytes   110 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   135 MBytes   113 Mbits/sec  106             sender
    [  5]   0.00-10.00  sec   131 MBytes   110 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.117 port 50321 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  20.1 MBytes   169 Mbits/sec    0    583 KBytes       
    [  5]   1.00-2.00   sec  18.8 MBytes   157 Mbits/sec    0    723 KBytes       
    [  5]   2.00-3.00   sec  16.6 MBytes   139 Mbits/sec    0    872 KBytes       
    [  5]   3.00-4.00   sec  17.9 MBytes   150 Mbits/sec    0    872 KBytes       
    [  5]   4.00-5.00   sec  18.4 MBytes   154 Mbits/sec    0    921 KBytes       
    [  5]   5.00-6.00   sec  18.6 MBytes   156 Mbits/sec    0    974 KBytes       
    [  5]   6.00-7.00   sec  18.0 MBytes   151 Mbits/sec    0    974 KBytes       
    [  5]   7.00-8.00   sec  16.9 MBytes   141 Mbits/sec    0    974 KBytes       
    [  5]   8.00-9.00   sec  18.2 MBytes   153 Mbits/sec    0   1.01 MBytes       
    [  5]   9.00-10.00  sec  18.4 MBytes   154 Mbits/sec    0   1.07 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   182 MBytes   153 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   178 MBytes   149 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 5500.0
    RX: 47901 bytes (196 packets)
    TX: 53698 bytes (206 packets)
    signal: -42 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">196</span> Mbits/sec | <span style="font-size: 1.5rem;">173</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 43693 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  20.5 MBytes   172 Mbits/sec                  
    [  5]   1.00-2.00   sec  23.6 MBytes   198 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   3.00-4.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   4.00-5.00   sec  23.1 MBytes   194 Mbits/sec                  
    [  5]   5.00-6.00   sec  23.5 MBytes   197 Mbits/sec                  
    [  5]   6.00-7.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   7.00-8.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   8.00-9.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   9.00-10.00  sec  23.5 MBytes   197 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   234 MBytes   196 Mbits/sec   87             sender
    [  5]   0.00-10.00  sec   230 MBytes   193 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 48575 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  22.2 MBytes   186 Mbits/sec    0   3.20 MBytes       
    [  5]   1.00-2.00   sec  21.0 MBytes   176 Mbits/sec    0   3.53 MBytes       
    [  5]   2.00-3.00   sec  20.8 MBytes   174 Mbits/sec    0   3.63 MBytes       
    [  5]   3.00-4.00   sec  21.2 MBytes   178 Mbits/sec    0   4.03 MBytes       
    [  5]   4.00-5.00   sec  20.4 MBytes   171 Mbits/sec    0   4.03 MBytes       
    [  5]   5.00-6.00   sec  19.5 MBytes   164 Mbits/sec    0   4.03 MBytes       
    [  5]   6.00-7.00   sec  21.1 MBytes   177 Mbits/sec    0   4.03 MBytes       
    [  5]   7.00-8.00   sec  19.5 MBytes   164 Mbits/sec    0   5.38 MBytes       
    [  5]   8.00-9.00   sec  20.5 MBytes   172 Mbits/sec    0   5.58 MBytes       
    [  5]   9.00-10.00  sec  20.4 MBytes   171 Mbits/sec    0   5.58 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   207 MBytes   173 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   205 MBytes   171 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 2462.0
    RX: 39865 bytes (135 packets)
    TX: 48721 bytes (212 packets)
    signal: -23 dBm
    rx bitrate: 154.8 MBit/s HE-MCS 6 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 58.5 MBit/s HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">96.2</span> Mbits/sec | <span style="font-size: 1.5rem;">68.3</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.114 port 55617 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.2 MBytes  85.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.6 MBytes  97.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   115 MBytes  96.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   112 MBytes  94.2 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.114 port 52027 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.62 MBytes  72.3 Mbits/sec    0    280 KBytes       
    [  5]   1.00-2.00   sec  8.00 MBytes  67.1 Mbits/sec    0    298 KBytes       
    [  5]   2.00-3.00   sec  8.75 MBytes  73.4 Mbits/sec    0    298 KBytes       
    [  5]   3.00-4.00   sec  7.38 MBytes  61.9 Mbits/sec    0    298 KBytes       
    [  5]   4.00-5.00   sec  8.25 MBytes  69.2 Mbits/sec    0    298 KBytes       
    [  5]   5.00-6.00   sec  8.38 MBytes  70.3 Mbits/sec    0    318 KBytes       
    [  5]   6.00-7.00   sec  8.25 MBytes  69.2 Mbits/sec    0    335 KBytes       
    [  5]   7.00-8.00   sec  7.62 MBytes  64.0 Mbits/sec    0    335 KBytes       
    [  5]   8.00-9.00   sec  8.25 MBytes  69.2 Mbits/sec    0    335 KBytes       
    [  5]   9.00-10.00  sec  7.88 MBytes  66.0 Mbits/sec    0    335 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  81.4 MBytes  68.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  79.8 MBytes  66.9 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 5500.0
    RX: 197215 bytes (616 packets)
    TX: 103904 bytes (550 packets)
    signal: -17 dBm
    rx bitrate: 270.0 MBit/s MCS 15 40MHz
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
```

#### Atheros AR9271

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">57.5</span> Mbits/sec | <span style="font-size: 1.5rem;">50.6</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.113 port 55929 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.38 MBytes  53.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.38 MBytes  53.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.62 MBytes  55.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  68.6 MBytes  57.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  65.2 MBytes  54.7 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.113 port 43435 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.75 MBytes  56.6 Mbits/sec    0    214 KBytes       
    [  5]   1.00-2.00   sec  6.25 MBytes  52.4 Mbits/sec    0    235 KBytes       
    [  5]   2.00-3.00   sec  6.00 MBytes  50.3 Mbits/sec    0    235 KBytes       
    [  5]   3.00-4.00   sec  6.00 MBytes  50.3 Mbits/sec    0    249 KBytes       
    [  5]   4.00-5.00   sec  5.62 MBytes  47.2 Mbits/sec    0    266 KBytes       
    [  5]   5.00-6.00   sec  6.12 MBytes  51.4 Mbits/sec    0    266 KBytes       
    [  5]   6.00-7.00   sec  5.75 MBytes  48.2 Mbits/sec    0    266 KBytes       
    [  5]   7.00-8.00   sec  5.50 MBytes  46.1 Mbits/sec    0    266 KBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0    266 KBytes       
    [  5]   9.00-10.00  sec  6.12 MBytes  51.4 Mbits/sec    0    266 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  60.4 MBytes  50.6 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  58.9 MBytes  49.2 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 2462.0
    RX: 85237 bytes (360 packets)
    TX: 59504 bytes (212 packets)
    signal: -49 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">42.4</span> Mbits/sec | <span style="font-size: 1.5rem;">45.9</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.112 port 59815 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  2.62 MBytes  22.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.75 MBytes  39.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.75 MBytes  39.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  50.6 MBytes  42.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  47.4 MBytes  39.7 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.112 port 35801 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.62 MBytes  47.1 Mbits/sec    0    259 KBytes       
    [  5]   1.00-2.00   sec  6.12 MBytes  51.4 Mbits/sec    0    481 KBytes       
    [  5]   2.00-3.00   sec  6.12 MBytes  51.4 Mbits/sec    0    700 KBytes       
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec    0    911 KBytes       
    [  5]   4.00-5.00   sec  5.88 MBytes  49.3 Mbits/sec    0   1.03 MBytes       
    [  5]   5.00-6.00   sec  4.12 MBytes  34.6 Mbits/sec    0   1.03 MBytes       
    [  5]   6.00-7.00   sec  5.75 MBytes  48.2 Mbits/sec    0   1.12 MBytes       
    [  5]   7.00-8.00   sec  5.62 MBytes  47.2 Mbits/sec    0   1.23 MBytes       
    [  5]   8.00-9.00   sec  5.75 MBytes  48.3 Mbits/sec    0   1.32 MBytes       
    [  5]   9.00-10.00  sec  5.50 MBytes  46.1 Mbits/sec    0   1.44 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  54.8 MBytes  45.9 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  51.1 MBytes  42.8 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 2462.0
    RX: 84733 bytes (374 packets)
    TX: 56962 bytes (220 packets)
    signal: -29 dBm
    rx bitrate: 65.0 MBit/s MCS 6 short GI
    tx bitrate: 65.0 MBit/s MCS 7
```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">97.6</span> Mbits/sec | <span style="font-size: 1.5rem;">68.8</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.111 port 39313 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.50 MBytes  79.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.9 MBytes  99.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   116 MBytes  97.6 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   114 MBytes  96.0 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.111 port 49623 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.00 MBytes  75.4 Mbits/sec    0    202 KBytes       
    [  5]   1.00-2.00   sec  7.88 MBytes  66.1 Mbits/sec    0    240 KBytes       
    [  5]   2.00-3.00   sec  8.50 MBytes  71.3 Mbits/sec    0    250 KBytes       
    [  5]   3.00-4.00   sec  7.88 MBytes  66.1 Mbits/sec    0    260 KBytes       
    [  5]   4.00-5.00   sec  8.38 MBytes  70.2 Mbits/sec    0    260 KBytes       
    [  5]   5.00-6.00   sec  7.88 MBytes  66.1 Mbits/sec    0    260 KBytes       
    [  5]   6.00-7.00   sec  8.38 MBytes  70.3 Mbits/sec    0    260 KBytes       
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec    0    260 KBytes       
    [  5]   8.00-9.00   sec  8.38 MBytes  70.3 Mbits/sec    0    260 KBytes       
    [  5]   9.00-10.00  sec  7.88 MBytes  66.0 Mbits/sec    0    260 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  82.0 MBytes  68.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  80.9 MBytes  67.8 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 5500.0
    RX: 217378 bytes (660 packets)
    TX: 108335 bytes (602 packets)
    signal: -32 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">45.5</span> Mbits/sec | <span style="font-size: 1.5rem;">34.1</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.110 port 33717 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.12 MBytes  43.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  54.4 MBytes  45.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  50.9 MBytes  42.7 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.110 port 43581 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.50 MBytes  37.7 Mbits/sec    0    233 KBytes       
    [  5]   1.00-2.00   sec  4.00 MBytes  33.6 Mbits/sec    0    274 KBytes       
    [  5]   2.00-3.00   sec  3.88 MBytes  32.5 Mbits/sec    0    288 KBytes       
    [  5]   3.00-4.00   sec  4.62 MBytes  38.8 Mbits/sec    0    335 KBytes       
    [  5]   4.00-5.00   sec  3.50 MBytes  29.4 Mbits/sec    0    335 KBytes       
    [  5]   5.00-6.00   sec  4.12 MBytes  34.6 Mbits/sec    0    335 KBytes       
    [  5]   6.00-7.00   sec  4.12 MBytes  34.6 Mbits/sec    0    335 KBytes       
    [  5]   7.00-8.00   sec  4.12 MBytes  34.6 Mbits/sec    0    335 KBytes       
    [  5]   8.00-9.00   sec  3.50 MBytes  29.4 Mbits/sec    0    335 KBytes       
    [  5]   9.00-10.00  sec  4.25 MBytes  35.6 Mbits/sec    0    335 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  40.6 MBytes  34.1 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  39.0 MBytes  32.6 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 2462.0
    RX: 90128 bytes (334 packets)
    TX: 62214 bytes (237 packets)
    signal: -30 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">28.7</span> Mbits/sec | <span style="font-size: 1.5rem;">43.2</span> Mbits/sec |

=== "Forward mode (client to server)"
```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.109 port 56987 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  2.38 MBytes  19.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.62 MBytes  30.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.88 MBytes  15.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.75 MBytes  23.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.62 MBytes  30.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.00 MBytes  33.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.08  sec  34.5 MBytes  28.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  32.9 MBytes  27.6 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Reverse mode (server to client)"
```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.109 port 39317 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.00 MBytes  50.2 Mbits/sec    0    325 KBytes       
    [  5]   1.00-2.00   sec  5.50 MBytes  46.2 Mbits/sec    0    363 KBytes       
    [  5]   2.00-3.00   sec  4.75 MBytes  39.8 Mbits/sec    0    400 KBytes       
    [  5]   3.00-4.00   sec  5.00 MBytes  41.9 Mbits/sec    0    433 KBytes       
    [  5]   4.00-5.00   sec  6.12 MBytes  51.4 Mbits/sec    0    433 KBytes       
    [  5]   5.00-6.00   sec  4.50 MBytes  37.8 Mbits/sec    0    455 KBytes       
    [  5]   6.00-7.00   sec  4.62 MBytes  38.8 Mbits/sec    0    455 KBytes       
    [  5]   7.00-8.00   sec  4.75 MBytes  39.8 Mbits/sec    0    455 KBytes       
    [  5]   8.00-9.00   sec  5.50 MBytes  46.1 Mbits/sec    0    455 KBytes       
    [  5]   9.00-10.00  sec  4.75 MBytes  39.8 Mbits/sec    0    455 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  51.5 MBytes  43.2 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  49.6 MBytes  41.6 Mbits/sec                  receiver
    
    iperf Done.
```
=== "Wireless link info"
```
    freq: 2462.0
    RX: 76020 bytes (313 packets)
    TX: 58536 bytes (220 packets)
    signal: -44 dBm
    rx bitrate: 58.5 MBit/s MCS 6
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
