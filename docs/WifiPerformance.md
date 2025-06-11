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
**Test Date:** [2025-06-11 17:02 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15590094999)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">232</span> Mbits/sec | <span style="font-size: 1.5rem;">264</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.160 port 33583 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  28.1 MBytes   236 Mbits/sec                  
    [  5]   1.00-2.00   sec  28.1 MBytes   236 Mbits/sec                  
    [  5]   2.00-3.00   sec  26.4 MBytes   222 Mbits/sec                  
    [  5]   3.00-4.00   sec  27.0 MBytes   226 Mbits/sec                  
    [  5]   4.00-5.00   sec  26.4 MBytes   222 Mbits/sec                  
    [  5]   5.00-6.00   sec  26.8 MBytes   225 Mbits/sec                  
    [  5]   6.00-7.00   sec  26.9 MBytes   226 Mbits/sec                  
    [  5]   7.00-8.00   sec  27.1 MBytes   227 Mbits/sec                  
    [  5]   8.00-9.00   sec  27.2 MBytes   228 Mbits/sec                  
    [  5]   9.00-10.00  sec  29.3 MBytes   246 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   277 MBytes   232 Mbits/sec  406             sender
    [  5]   0.00-10.00  sec   273 MBytes   229 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.160 port 35105 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  33.5 MBytes   281 Mbits/sec    0    865 KBytes       
    [  5]   1.00-2.00   sec  30.0 MBytes   252 Mbits/sec    0   1.13 MBytes       
    [  5]   2.00-3.00   sec  31.2 MBytes   262 Mbits/sec    0   1.20 MBytes       
    [  5]   3.00-4.00   sec  31.2 MBytes   262 Mbits/sec    0   1.20 MBytes       
    [  5]   4.00-5.00   sec  31.2 MBytes   262 Mbits/sec    0   1.26 MBytes       
    [  5]   5.00-6.00   sec  32.5 MBytes   273 Mbits/sec    0   1.33 MBytes       
    [  5]   6.00-7.00   sec  31.2 MBytes   262 Mbits/sec    0   1.33 MBytes       
    [  5]   7.00-8.00   sec  31.2 MBytes   262 Mbits/sec    0   1.33 MBytes       
    [  5]   8.00-9.00   sec  31.2 MBytes   262 Mbits/sec    0   1.33 MBytes       
    [  5]   9.00-10.00  sec  31.2 MBytes   262 Mbits/sec    0   1.33 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   315 MBytes   264 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   312 MBytes   262 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 138671 bytes (378 packets)
    TX: 82508 bytes (491 packets)
    signal: -39 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">229</span> Mbits/sec | <span style="font-size: 1.5rem;">184</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.158 port 48631 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  27.6 MBytes   231 Mbits/sec                  
    [  5]   1.00-2.00   sec  27.1 MBytes   227 Mbits/sec                  
    [  5]   2.00-3.00   sec  26.4 MBytes   221 Mbits/sec                  
    [  5]   3.00-4.00   sec  26.3 MBytes   221 Mbits/sec                  
    [  5]   4.00-5.00   sec  26.9 MBytes   226 Mbits/sec                  
    [  5]   5.00-6.00   sec  27.1 MBytes   227 Mbits/sec                  
    [  5]   6.00-7.00   sec  27.4 MBytes   230 Mbits/sec                  
    [  5]   7.00-8.00   sec  28.0 MBytes   235 Mbits/sec                  
    [  5]   8.00-9.00   sec  27.4 MBytes   230 Mbits/sec                  
    [  5]   9.00-10.00  sec  26.7 MBytes   224 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   274 MBytes   229 Mbits/sec   51             sender
    [  5]   0.00-10.00  sec   271 MBytes   227 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.158 port 48871 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  22.4 MBytes   188 Mbits/sec    0    648 KBytes       
    [  5]   1.00-2.00   sec  20.4 MBytes   171 Mbits/sec    0    686 KBytes       
    [  5]   2.00-3.00   sec  22.0 MBytes   185 Mbits/sec    0    754 KBytes       
    [  5]   3.00-4.00   sec  22.1 MBytes   185 Mbits/sec    0    766 KBytes       
    [  5]   4.00-5.00   sec  21.7 MBytes   182 Mbits/sec    0    766 KBytes       
    [  5]   5.00-6.00   sec  20.8 MBytes   175 Mbits/sec    0    766 KBytes       
    [  5]   6.00-7.00   sec  22.9 MBytes   192 Mbits/sec    0    850 KBytes       
    [  5]   7.00-8.00   sec  23.0 MBytes   193 Mbits/sec    0    850 KBytes       
    [  5]   8.00-9.00   sec  22.4 MBytes   187 Mbits/sec    0    850 KBytes       
    [  5]   9.00-10.00  sec  21.1 MBytes   177 Mbits/sec    0    850 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   219 MBytes   184 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   217 MBytes   182 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 119027 bytes (495 packets)
    TX: 58451 bytes (225 packets)
    signal: -39 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">198</span> Mbits/sec | <span style="font-size: 1.5rem;">252</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 37175 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  21.0 MBytes   176 Mbits/sec                  
    [  5]   1.00-2.00   sec  24.8 MBytes   208 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.5 MBytes   197 Mbits/sec                  
    [  5]   3.00-4.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   4.00-5.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   5.00-6.00   sec  23.6 MBytes   198 Mbits/sec                  
    [  5]   6.00-7.00   sec  24.0 MBytes   201 Mbits/sec                  
    [  5]   7.00-8.00   sec  23.8 MBytes   199 Mbits/sec                  
    [  5]   8.00-9.00   sec  23.5 MBytes   197 Mbits/sec                  
    [  5]   9.00-10.00  sec  23.2 MBytes   195 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   236 MBytes   198 Mbits/sec  256             sender
    [  5]   0.00-10.00  sec   233 MBytes   196 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 41429 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  35.8 MBytes   300 Mbits/sec    0   1.30 MBytes       
    [  5]   1.00-2.00   sec  31.9 MBytes   267 Mbits/sec    0   1.33 MBytes       
    [  5]   2.00-3.00   sec  32.1 MBytes   269 Mbits/sec    0   1.33 MBytes       
    [  5]   3.00-4.00   sec  31.8 MBytes   266 Mbits/sec    0   1.33 MBytes       
    [  5]   4.00-5.00   sec  31.1 MBytes   261 Mbits/sec    0   1.33 MBytes       
    [  5]   5.00-6.00   sec  28.4 MBytes   238 Mbits/sec    0   1.33 MBytes       
    [  5]   6.00-7.00   sec  27.9 MBytes   234 Mbits/sec    0   1.33 MBytes       
    [  5]   7.00-8.00   sec  29.6 MBytes   248 Mbits/sec    0   1.33 MBytes       
    [  5]   8.00-9.00   sec  29.8 MBytes   250 Mbits/sec    0   1.33 MBytes       
    [  5]   9.00-10.00  sec  22.1 MBytes   186 Mbits/sec    0   1.33 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   300 MBytes   252 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   297 MBytes   249 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 177886 bytes (337 packets)
    TX: 91815 bytes (448 packets)
    signal: -38 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">189</span> Mbits/sec | <span style="font-size: 1.5rem;">187</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 57353 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   1.00-2.00   sec  23.2 MBytes   195 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.2 MBytes   195 Mbits/sec                  
    [  5]   3.00-4.00   sec  22.1 MBytes   186 Mbits/sec                  
    [  5]   4.00-5.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   5.00-6.00   sec  22.2 MBytes   187 Mbits/sec                  
    [  5]   6.00-7.00   sec  21.0 MBytes   176 Mbits/sec                  
    [  5]   7.00-8.00   sec  22.1 MBytes   186 Mbits/sec                  
    [  5]   8.00-9.00   sec  22.1 MBytes   185 Mbits/sec                  
    [  5]   9.00-10.00  sec  22.5 MBytes   189 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   226 MBytes   189 Mbits/sec  271             sender
    [  5]   0.00-10.00  sec   222 MBytes   186 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 57491 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.6 MBytes   164 Mbits/sec    0    454 KBytes       
    [  5]   1.00-2.00   sec  21.0 MBytes   176 Mbits/sec    0    567 KBytes       
    [  5]   2.00-3.00   sec  22.9 MBytes   192 Mbits/sec    0    635 KBytes       
    [  5]   3.00-4.00   sec  23.2 MBytes   195 Mbits/sec    0    635 KBytes       
    [  5]   4.00-5.00   sec  24.9 MBytes   209 Mbits/sec    0    675 KBytes       
    [  5]   5.00-6.00   sec  23.5 MBytes   197 Mbits/sec    0    716 KBytes       
    [  5]   6.00-7.00   sec  19.5 MBytes   164 Mbits/sec    0    751 KBytes       
    [  5]   7.00-8.00   sec  22.2 MBytes   187 Mbits/sec    0    751 KBytes       
    [  5]   8.00-9.00   sec  22.1 MBytes   186 Mbits/sec    0    751 KBytes       
    [  5]   9.00-10.00  sec  23.4 MBytes   196 Mbits/sec    0    793 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   222 MBytes   187 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   219 MBytes   183 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">92.6</span> Mbits/sec | <span style="font-size: 1.5rem;">119</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 41395 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.1 MBytes  84.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.25 MBytes  77.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   110 MBytes  92.6 Mbits/sec   70             sender
    [  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 38843 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  17.1 MBytes   144 Mbits/sec    0    595 KBytes       
    [  5]   1.00-2.00   sec  13.6 MBytes   114 Mbits/sec    0    759 KBytes       
    [  5]   2.00-3.00   sec  14.1 MBytes   118 Mbits/sec    0    803 KBytes       
    [  5]   3.00-4.00   sec  14.4 MBytes   121 Mbits/sec    0    928 KBytes       
    [  5]   4.00-5.00   sec  13.0 MBytes   109 Mbits/sec    0    976 KBytes       
    [  5]   5.00-6.00   sec  14.1 MBytes   118 Mbits/sec    0    976 KBytes       
    [  5]   6.00-7.00   sec  14.4 MBytes   121 Mbits/sec    0   1.00 MBytes       
    [  5]   7.00-8.00   sec  14.2 MBytes   120 Mbits/sec    0   1.00 MBytes       
    [  5]   8.00-9.00   sec  12.8 MBytes   107 Mbits/sec    0   1.00 MBytes       
    [  5]   9.00-10.00  sec  14.2 MBytes   120 Mbits/sec    0   1.06 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   142 MBytes   119 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   139 MBytes   117 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    signal: -38 dBm
    tx bitrate: 174.0 MBit/s
    ```

#### Realtek 8821CU #1

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">145</span> Mbits/sec | <span style="font-size: 1.5rem;">219</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 52857 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.9 MBytes  99.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.9 MBytes   150 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   173 MBytes   145 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   173 MBytes   145 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 36725 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  31.0 MBytes   260 Mbits/sec    0    645 KBytes       
    [  5]   1.00-2.00   sec  26.1 MBytes   219 Mbits/sec    0    645 KBytes       
    [  5]   2.00-3.00   sec  26.2 MBytes   220 Mbits/sec    0    645 KBytes       
    [  5]   3.00-4.00   sec  24.8 MBytes   208 Mbits/sec    0    645 KBytes       
    [  5]   4.00-5.00   sec  25.4 MBytes   213 Mbits/sec    0    680 KBytes       
    [  5]   5.00-6.00   sec  26.0 MBytes   218 Mbits/sec    0    680 KBytes       
    [  5]   6.00-7.00   sec  24.8 MBytes   208 Mbits/sec    0    680 KBytes       
    [  5]   7.00-8.00   sec  26.1 MBytes   219 Mbits/sec    0    680 KBytes       
    [  5]   8.00-9.00   sec  26.0 MBytes   218 Mbits/sec    0    680 KBytes       
    [  5]   9.00-10.00  sec  24.8 MBytes   208 Mbits/sec    0    680 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   261 MBytes   219 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   258 MBytes   216 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 78198 bytes (260 packets)
    TX: 53223 bytes (192 packets)
    signal: -39 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">4.66</span> Mbits/sec | <span style="font-size: 1.5rem;">27.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.157 port 53375 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.25 MBytes  10.5 Mbits/sec                  
    [  5]   1.00-2.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   2.00-3.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   3.00-4.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   4.00-5.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   5.00-6.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   6.00-7.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   7.00-8.00   sec   384 KBytes  3.15 Mbits/sec                  
    [  5]   8.00-9.00   sec   512 KBytes  4.19 Mbits/sec                  
    [  5]   9.00-10.00  sec   256 KBytes  2.10 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-11.94  sec  6.62 MBytes  4.66 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  3.62 MBytes  3.04 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.157 port 60813 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.50 MBytes  54.5 Mbits/sec    0    648 KBytes       
    [  5]   1.00-2.00   sec  2.75 MBytes  23.1 Mbits/sec    0    666 KBytes       
    [  5]   2.00-3.00   sec  2.62 MBytes  22.0 Mbits/sec    0    741 KBytes       
    [  5]   3.00-4.00   sec  2.75 MBytes  23.1 Mbits/sec    0    768 KBytes       
    [  5]   4.00-5.00   sec  2.75 MBytes  23.1 Mbits/sec    0    768 KBytes       
    [  5]   5.00-6.00   sec  2.75 MBytes  23.1 Mbits/sec    0   1.00 MBytes       
    [  5]   6.00-7.00   sec  2.75 MBytes  23.1 Mbits/sec    0   1.00 MBytes       
    [  5]   7.00-8.00   sec  2.75 MBytes  23.1 Mbits/sec    0   1.00 MBytes       
    [  5]   8.00-9.00   sec  2.75 MBytes  23.1 Mbits/sec    0   1.00 MBytes       
    [  5]   9.00-10.00  sec  4.00 MBytes  33.5 Mbits/sec    0   1.00 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  32.4 MBytes  27.2 Mbits/sec    0             sender
    [  5]   0.00-10.06  sec  29.4 MBytes  24.5 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">464</span> Mbits/sec | <span style="font-size: 1.5rem;">492</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.156 port 47239 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  59.7 MBytes   501 Mbits/sec                  
    [  5]   1.00-2.00   sec  56.6 MBytes   475 Mbits/sec                  
    [  5]   2.00-3.00   sec  54.8 MBytes   459 Mbits/sec                  
    [  5]   3.00-4.00   sec  51.2 MBytes   430 Mbits/sec                  
    [  5]   4.00-5.00   sec  50.9 MBytes   427 Mbits/sec                  
    [  5]   5.00-6.00   sec  55.5 MBytes   466 Mbits/sec                  
    [  5]   6.00-7.00   sec  56.1 MBytes   471 Mbits/sec                  
    [  5]   7.00-8.00   sec  58.4 MBytes   490 Mbits/sec                  
    [  5]   8.00-9.00   sec  54.9 MBytes   461 Mbits/sec                  
    [  5]   9.00-10.00  sec  51.8 MBytes   434 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   553 MBytes   464 Mbits/sec  510             sender
    [  5]   0.00-10.00  sec   550 MBytes   461 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.156 port 57795 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  74.1 MBytes   620 Mbits/sec  289   2.61 MBytes       
    [  5]   1.00-2.00   sec  71.2 MBytes   599 Mbits/sec  271   1.33 MBytes       
    [  5]   2.00-3.00   sec  71.2 MBytes   598 Mbits/sec  476    742 KBytes       
    [  5]   3.00-4.00   sec  61.2 MBytes   514 Mbits/sec  177    443 KBytes       
    [  5]   4.00-5.00   sec  52.5 MBytes   440 Mbits/sec   74    305 KBytes       
    [  5]   5.00-6.00   sec  50.0 MBytes   420 Mbits/sec    0    488 KBytes       
    [  5]   6.00-7.00   sec  48.8 MBytes   409 Mbits/sec   17    440 KBytes       
    [  5]   7.00-8.00   sec  56.2 MBytes   472 Mbits/sec    0    598 KBytes       
    [  5]   8.00-9.00   sec  52.5 MBytes   440 Mbits/sec   96    452 KBytes       
    [  5]   9.00-10.00  sec  48.8 MBytes   409 Mbits/sec   46    382 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   587 MBytes   492 Mbits/sec  1446             sender
    [  5]   0.00-10.01  sec   584 MBytes   490 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 133084 bytes (476 packets)
    TX: 61180 bytes (218 packets)
    signal: -36 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
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
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">126</span> Mbits/sec | <span style="font-size: 1.5rem;">141</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 51193 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  14.2 MBytes   119 Mbits/sec                  
    [  5]   1.00-2.00   sec  14.8 MBytes   124 Mbits/sec                  
    [  5]   2.00-3.00   sec  15.0 MBytes   126 Mbits/sec                  
    [  5]   3.00-4.00   sec  15.0 MBytes   126 Mbits/sec                  
    [  5]   4.00-5.00   sec  14.8 MBytes   124 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.6 MBytes   123 Mbits/sec                  
    [  5]   6.00-7.00   sec  15.0 MBytes   126 Mbits/sec                  
    [  5]   7.00-8.00   sec  14.8 MBytes   124 Mbits/sec                  
    [  5]   8.00-9.00   sec  14.6 MBytes   123 Mbits/sec                  
    [  5]   9.00-10.00  sec  14.8 MBytes   124 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   150 MBytes   126 Mbits/sec   84             sender
    [  5]   0.00-10.00  sec   148 MBytes   124 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 53177 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  17.8 MBytes   149 Mbits/sec    0    561 KBytes       
    [  5]   1.00-2.00   sec  16.2 MBytes   136 Mbits/sec    0    872 KBytes       
    [  5]   2.00-3.00   sec  17.5 MBytes   147 Mbits/sec    0    976 KBytes       
    [  5]   3.00-4.00   sec  16.5 MBytes   138 Mbits/sec    0   1.12 MBytes       
    [  5]   4.00-5.00   sec  16.5 MBytes   138 Mbits/sec    0   1.20 MBytes       
    [  5]   5.00-6.00   sec  15.9 MBytes   133 Mbits/sec    0   1.28 MBytes       
    [  5]   6.00-7.00   sec  17.2 MBytes   145 Mbits/sec    0   1.28 MBytes       
    [  5]   7.00-8.00   sec  17.4 MBytes   146 Mbits/sec    0   1.49 MBytes       
    [  5]   8.00-9.00   sec  15.6 MBytes   131 Mbits/sec    0   1.57 MBytes       
    [  5]   9.00-10.00  sec  17.1 MBytes   144 Mbits/sec    0   1.57 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   168 MBytes   141 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   166 MBytes   139 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 64032 bytes (247 packets)
    TX: 51143 bytes (225 packets)
    signal: -36 dBm
    rx bitrate: 286.7 MBit/s HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 286.7 MBit/s HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">191</span> Mbits/sec | <span style="font-size: 1.5rem;">176</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.155 port 36771 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   1.00-2.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.1 MBytes   194 Mbits/sec                  
    [  5]   3.00-4.00   sec  22.4 MBytes   188 Mbits/sec                  
    [  5]   4.00-5.00   sec  22.9 MBytes   192 Mbits/sec                  
    [  5]   5.00-6.00   sec  23.5 MBytes   197 Mbits/sec                  
    [  5]   6.00-7.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   7.00-8.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   8.00-9.00   sec  22.9 MBytes   192 Mbits/sec                  
    [  5]   9.00-10.00  sec  23.4 MBytes   196 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   228 MBytes   191 Mbits/sec  179             sender
    [  5]   0.00-10.00  sec   224 MBytes   188 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.155 port 58455 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  22.6 MBytes   190 Mbits/sec    0   3.66 MBytes       
    [  5]   1.00-2.00   sec  21.1 MBytes   177 Mbits/sec    0   3.66 MBytes       
    [  5]   2.00-3.00   sec  19.5 MBytes   164 Mbits/sec    0   3.66 MBytes       
    [  5]   3.00-4.00   sec  21.6 MBytes   181 Mbits/sec    0   3.97 MBytes       
    [  5]   4.00-5.00   sec  21.5 MBytes   180 Mbits/sec    0   3.97 MBytes       
    [  5]   5.00-6.00   sec  19.6 MBytes   165 Mbits/sec    0   3.97 MBytes       
    [  5]   6.00-7.00   sec  21.1 MBytes   177 Mbits/sec    0   3.97 MBytes       
    [  5]   7.00-8.00   sec  20.4 MBytes   171 Mbits/sec    0   3.97 MBytes       
    [  5]   8.00-9.00   sec  21.0 MBytes   176 Mbits/sec    0   3.97 MBytes       
    [  5]   9.00-10.00  sec  21.0 MBytes   176 Mbits/sec    0   3.97 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   210 MBytes   176 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   206 MBytes   173 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 37310 bytes (132 packets)
    TX: 47102 bytes (193 packets)
    signal: -27 dBm
    rx bitrate: 143.3 MBit/s HE-MCS 11 HE-NSS 1 HE-GI 0 HE-DCM 0
    tx bitrate: 58.5 MBit/s HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">57.8</span> Mbits/sec | <span style="font-size: 1.5rem;">63.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 33109 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.00 MBytes  50.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.62 MBytes  63.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.88 MBytes  57.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.75 MBytes  39.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.88 MBytes  57.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  69.0 MBytes  57.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  65.4 MBytes  54.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 54653 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  10.1 MBytes  84.9 Mbits/sec    0    496 KBytes       
    [  5]   1.00-2.00   sec  8.75 MBytes  73.4 Mbits/sec    0    728 KBytes       
    [  5]   2.00-3.00   sec  5.88 MBytes  49.3 Mbits/sec    0    844 KBytes       
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec    0    904 KBytes       
    [  5]   4.00-5.00   sec  5.62 MBytes  47.2 Mbits/sec    0    962 KBytes       
    [  5]   5.00-6.00   sec  8.25 MBytes  69.2 Mbits/sec    0    962 KBytes       
    [  5]   6.00-7.00   sec  8.25 MBytes  69.0 Mbits/sec    0    962 KBytes       
    [  5]   7.00-8.00   sec  6.88 MBytes  57.8 Mbits/sec    0   1.04 MBytes       
    [  5]   8.00-9.00   sec  6.88 MBytes  57.7 Mbits/sec    0   1.10 MBytes       
    [  5]   9.00-10.00  sec  7.12 MBytes  59.7 Mbits/sec    0   1.10 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  76.1 MBytes  63.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  73.0 MBytes  61.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 190323 bytes (595 packets)
    TX: 91890 bytes (540 packets)
    signal: -17 dBm
    rx bitrate: 240.0 MBit/s MCS 13 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">55.7</span> Mbits/sec | <span style="font-size: 1.5rem;">39.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.154 port 45441 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.96 MBytes  50.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.56 MBytes  55.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.26 MBytes  52.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.36 MBytes  53.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.34 MBytes  53.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.57 MBytes  55.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.42 MBytes  53.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.54 MBytes  54.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.20 MBytes  52.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  66.5 MBytes  55.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  63.5 MBytes  53.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.154 port 33947 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.18 MBytes  43.4 Mbits/sec    0    188 KBytes       
    [  5]   1.00-2.00   sec  4.91 MBytes  41.2 Mbits/sec    0    238 KBytes       
    [  5]   2.00-3.00   sec  4.72 MBytes  39.6 Mbits/sec    0    249 KBytes       
    [  5]   3.00-4.00   sec  4.66 MBytes  39.1 Mbits/sec    0    262 KBytes       
    [  5]   4.00-5.00   sec  4.66 MBytes  39.1 Mbits/sec    0    262 KBytes       
    [  5]   5.00-6.00   sec  4.35 MBytes  36.5 Mbits/sec    0    262 KBytes       
    [  5]   6.00-7.00   sec  4.10 MBytes  34.4 Mbits/sec    0    274 KBytes       
    [  5]   7.00-8.00   sec  4.41 MBytes  37.0 Mbits/sec    0    274 KBytes       
    [  5]   8.00-9.00   sec  4.91 MBytes  41.2 Mbits/sec    0    372 KBytes       
    [  5]   9.00-10.00  sec  4.60 MBytes  38.6 Mbits/sec    0    372 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  46.5 MBytes  39.0 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  45.5 MBytes  38.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 54608 bytes (160 packets)
    TX: 57274 bytes (254 packets)
    signal: -59 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">42.7</span> Mbits/sec | <span style="font-size: 1.5rem;">14.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.153 port 56623 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.22 MBytes  43.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.47 MBytes  37.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.35 MBytes  36.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.09 MBytes  42.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.13 MBytes  43.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.13 MBytes  43.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.95 MBytes  41.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.57 MBytes  46.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.47 MBytes  45.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.07 MBytes  42.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.52  sec  53.6 MBytes  42.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  50.5 MBytes  42.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.153 port 37475 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  2.06 MBytes  17.3 Mbits/sec    0    115 KBytes       
    [  5]   1.00-2.00   sec  1.68 MBytes  14.1 Mbits/sec    0    178 KBytes       
    [  5]   2.00-3.00   sec   827 KBytes  6.78 Mbits/sec    0    201 KBytes       
    [  5]   3.00-4.00   sec   954 KBytes  7.82 Mbits/sec    0    238 KBytes       
    [  5]   4.00-5.00   sec   509 KBytes  4.17 Mbits/sec    0    242 KBytes       
    [  5]   5.00-6.00   sec   636 KBytes  5.21 Mbits/sec    1    168 KBytes       
    [  5]   6.00-7.00   sec  1.55 MBytes  13.0 Mbits/sec    0    204 KBytes       
    [  5]   7.00-8.00   sec  2.55 MBytes  21.3 Mbits/sec    0    225 KBytes       
    [  5]   8.00-9.00   sec  1.49 MBytes  12.5 Mbits/sec    0    238 KBytes       
    [  5]   9.00-10.00  sec  5.22 MBytes  43.8 Mbits/sec    0    242 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  17.4 MBytes  14.6 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec  16.1 MBytes  13.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 72782 bytes (247 packets)
    TX: 52868 bytes (258 packets)
    signal: -52 dBm
    rx bitrate: 292.5 MBit/s
    tx bitrate: 325.0 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">38.9</span> Mbits/sec | <span style="font-size: 1.5rem;">50.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 59829 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.25 MBytes  35.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.50 MBytes  37.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.12 MBytes  34.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  46.4 MBytes  38.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  42.8 MBytes  35.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 43139 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec    0    279 KBytes       
    [  5]   1.00-2.00   sec  6.00 MBytes  50.3 Mbits/sec    0    537 KBytes       
    [  5]   2.00-3.00   sec  6.62 MBytes  55.6 Mbits/sec    0    747 KBytes       
    [  5]   3.00-4.00   sec  5.50 MBytes  46.1 Mbits/sec    0    936 KBytes       
    [  5]   4.00-5.00   sec  6.88 MBytes  57.7 Mbits/sec    1    778 KBytes       
    [  5]   5.00-6.00   sec  5.62 MBytes  47.2 Mbits/sec    0    819 KBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec    0    939 KBytes       
    [  5]   7.00-8.00   sec  7.00 MBytes  58.7 Mbits/sec    0   1014 KBytes       
    [  5]   8.00-9.00   sec  5.88 MBytes  49.3 Mbits/sec    1    747 KBytes       
    [  5]   9.00-10.00  sec  4.38 MBytes  36.7 Mbits/sec    0    800 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  59.6 MBytes  50.0 Mbits/sec    2             sender
    [  5]   0.00-10.01  sec  56.9 MBytes  47.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 98286 bytes (419 packets)
    TX: 56473 bytes (226 packets)
    signal: -29 dBm
    rx bitrate: 65.0 MBit/s MCS 6 short GI
    tx bitrate: 65.0 MBit/s MCS 7
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">88.1</span> Mbits/sec | <span style="font-size: 1.5rem;">67.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 49703 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.00 MBytes  75.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  9.88 MBytes  82.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  10.9 MBytes  91.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   105 MBytes  88.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   102 MBytes  85.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 49085 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.38 MBytes  61.8 Mbits/sec    0    280 KBytes       
    [  5]   1.00-2.00   sec  8.38 MBytes  70.2 Mbits/sec    0    437 KBytes       
    [  5]   2.00-3.00   sec  9.00 MBytes  75.5 Mbits/sec    0    539 KBytes       
    [  5]   3.00-4.00   sec  6.88 MBytes  57.6 Mbits/sec    0    604 KBytes       
    [  5]   4.00-5.00   sec  7.50 MBytes  63.0 Mbits/sec    0    604 KBytes       
    [  5]   5.00-6.00   sec  8.75 MBytes  73.4 Mbits/sec    0    604 KBytes       
    [  5]   6.00-7.00   sec  7.88 MBytes  66.1 Mbits/sec    0    641 KBytes       
    [  5]   7.00-8.00   sec  8.12 MBytes  68.1 Mbits/sec    0    701 KBytes       
    [  5]   8.00-9.00   sec  8.38 MBytes  70.2 Mbits/sec    0    701 KBytes       
    [  5]   9.00-10.00  sec  8.25 MBytes  69.2 Mbits/sec    0    701 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  80.5 MBytes  67.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  77.1 MBytes  64.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 100140 bytes (437 packets)
    TX: 55932 bytes (244 packets)
    signal: -24 dBm
    rx bitrate: 240.0 MBit/s MCS 13 40MHz short GI
    tx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">37.2</span> Mbits/sec | <span style="font-size: 1.5rem;">26.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 55559 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.12 MBytes  26.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.50 MBytes  37.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.50 MBytes  37.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.25 MBytes  35.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  44.4 MBytes  37.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  41.4 MBytes  34.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 52261 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.38 MBytes  36.7 Mbits/sec    5   60.8 KBytes       
    [  5]   1.00-2.00   sec  4.12 MBytes  34.6 Mbits/sec    4   41.0 KBytes       
    [  5]   2.00-3.00   sec  3.25 MBytes  27.3 Mbits/sec   27   18.4 KBytes       
    [  5]   3.00-4.00   sec  3.00 MBytes  25.2 Mbits/sec   39   2.83 KBytes       
    [  5]   4.00-5.00   sec  3.00 MBytes  25.2 Mbits/sec   28   14.1 KBytes       
    [  5]   5.00-6.00   sec  1.75 MBytes  14.7 Mbits/sec   49   7.07 KBytes       
    [  5]   6.00-7.00   sec  2.12 MBytes  17.8 Mbits/sec   45   8.48 KBytes       
    [  5]   7.00-8.00   sec  2.38 MBytes  19.9 Mbits/sec   50   5.66 KBytes       
    [  5]   8.00-9.00   sec  3.38 MBytes  28.3 Mbits/sec   25   18.4 KBytes       
    [  5]   9.00-10.00  sec  4.12 MBytes  34.6 Mbits/sec   10   42.4 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  31.5 MBytes  26.4 Mbits/sec  282             sender
    [  5]   0.00-10.00  sec  31.1 MBytes  26.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 48211 bytes (119 packets)
    TX: 49921 bytes (207 packets)
    signal: -33 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">43.4</span> Mbits/sec | <span style="font-size: 1.5rem;">30.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.152 port 56613 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.07 MBytes  50.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.13 MBytes  34.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.72 MBytes  31.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.66 MBytes  30.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.43 MBytes  28.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.29 MBytes  52.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.46 MBytes  45.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.11 MBytes  42.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.57 MBytes  46.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.18 MBytes  43.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  51.9 MBytes  43.4 Mbits/sec   12             sender
    [  5]   0.00-10.00  sec  48.6 MBytes  40.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.152 port 55843 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.52 MBytes  46.3 Mbits/sec    0    339 KBytes       
    [  5]   1.00-2.00   sec  4.54 MBytes  38.1 Mbits/sec    0    530 KBytes       
    [  5]   2.00-3.00   sec  3.54 MBytes  29.7 Mbits/sec    0    700 KBytes       
    [  5]   3.00-4.00   sec  3.60 MBytes  30.2 Mbits/sec    0    824 KBytes       
    [  5]   4.00-5.00   sec  3.79 MBytes  31.8 Mbits/sec    0    916 KBytes       
    [  5]   5.00-6.00   sec  2.24 MBytes  18.8 Mbits/sec    0    971 KBytes       
    [  5]   6.00-7.00   sec  3.52 MBytes  29.6 Mbits/sec    0   1.09 MBytes       
    [  5]   7.00-8.00   sec  4.88 MBytes  40.9 Mbits/sec    0   1.22 MBytes       
    [  5]   8.00-9.00   sec  1.25 MBytes  10.5 Mbits/sec    0   1.28 MBytes       
    [  5]   9.00-10.00  sec  3.75 MBytes  31.5 Mbits/sec    0   1.42 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  36.6 MBytes  30.7 Mbits/sec    0             sender
    [  5]   0.00-10.10  sec  34.8 MBytes  28.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">38.3</span> Mbits/sec | <span style="font-size: 1.5rem;">46.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 53209 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.50 MBytes  29.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.12 MBytes  34.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  45.8 MBytes  38.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  42.8 MBytes  35.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 37651 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.88 MBytes  49.2 Mbits/sec    0    272 KBytes       
    [  5]   1.00-2.00   sec  6.00 MBytes  50.3 Mbits/sec    0    444 KBytes       
    [  5]   2.00-3.00   sec  5.75 MBytes  48.2 Mbits/sec    0    488 KBytes       
    [  5]   3.00-4.00   sec  5.12 MBytes  43.0 Mbits/sec    0    516 KBytes       
    [  5]   4.00-5.00   sec  5.25 MBytes  44.0 Mbits/sec    0    542 KBytes       
    [  5]   5.00-6.00   sec  5.50 MBytes  46.1 Mbits/sec    0    571 KBytes       
    [  5]   6.00-7.00   sec  5.75 MBytes  48.2 Mbits/sec    0    625 KBytes       
    [  5]   7.00-8.00   sec  5.00 MBytes  41.9 Mbits/sec    0    625 KBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0    625 KBytes       
    [  5]   9.00-10.00  sec  5.00 MBytes  41.9 Mbits/sec    0    653 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  55.5 MBytes  46.6 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  52.6 MBytes  44.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 72435 bytes (279 packets)
    TX: 50131 bytes (205 packets)
    signal: -36 dBm
    rx bitrate: 26.0 MBit/s MCS 3
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">113</span> Mbits/sec | <span style="font-size: 1.5rem;">103</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.151 port 42485 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.7 MBytes   107 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.9 MBytes  91.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.5 MBytes   114 Mbits/sec                  
    [  5]   4.00-5.00   sec  14.0 MBytes   118 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.7 MBytes   107 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.3 MBytes   112 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   134 MBytes   113 Mbits/sec  185             sender
    [  5]   0.00-10.00  sec   131 MBytes   110 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.151 port 41557 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  16.4 MBytes   137 Mbits/sec    0    349 KBytes       
    [  5]   1.00-2.00   sec  16.6 MBytes   139 Mbits/sec    1    273 KBytes       
    [  5]   2.00-3.00   sec  16.3 MBytes   137 Mbits/sec    0    320 KBytes       
    [  5]   3.00-4.00   sec  15.8 MBytes   132 Mbits/sec    1    243 KBytes       
    [  5]   4.00-5.00   sec  15.4 MBytes   129 Mbits/sec    0    280 KBytes       
    [  5]   5.00-6.00   sec  15.8 MBytes   132 Mbits/sec    0    307 KBytes       
    [  5]   6.00-7.00   sec  8.64 MBytes  72.5 Mbits/sec    4    124 KBytes       
    [  5]   7.00-8.00   sec  5.47 MBytes  45.9 Mbits/sec    0    156 KBytes       
    [  5]   8.00-9.00   sec  5.53 MBytes  46.4 Mbits/sec    4    136 KBytes       
    [  5]   9.00-10.00  sec  7.02 MBytes  58.9 Mbits/sec    0    171 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   123 MBytes   103 Mbits/sec   10             sender
    [  5]   0.00-10.00  sec   121 MBytes   102 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 371471149 bytes (303213 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">18.1</span> Mbits/sec | <span style="font-size: 1.5rem;">10.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.136 port 41545 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.57 MBytes  13.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.37 MBytes  11.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.03 MBytes  17.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.31 MBytes  19.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.94 MBytes  16.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.80 MBytes  15.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  1.95 MBytes  16.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.14 MBytes  17.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.19 MBytes  18.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.35 MBytes  19.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.14  sec  21.9 MBytes  18.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  19.6 MBytes  16.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.136 port 57407 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.59 MBytes  13.3 Mbits/sec    7   69.3 KBytes       
    [  5]   1.00-2.00   sec  1.12 MBytes  9.38 Mbits/sec    3   46.7 KBytes       
    [  5]   2.00-3.00   sec  1.24 MBytes  10.4 Mbits/sec    4   38.2 KBytes       
    [  5]   3.00-4.00   sec   827 KBytes  6.77 Mbits/sec   10   14.1 KBytes       
    [  5]   4.00-5.00   sec  1.12 MBytes  9.39 Mbits/sec    2   38.2 KBytes       
    [  5]   5.00-6.00   sec  1.18 MBytes  9.90 Mbits/sec    1   39.6 KBytes       
    [  5]   6.00-7.00   sec  1.12 MBytes  9.38 Mbits/sec    2   33.9 KBytes       
    [  5]   7.00-8.00   sec  1.30 MBytes  11.0 Mbits/sec    3   46.7 KBytes       
    [  5]   8.00-9.00   sec  1.37 MBytes  11.5 Mbits/sec    1   45.2 KBytes       
    [  5]   9.00-10.00  sec  1.24 MBytes  10.4 Mbits/sec    0   62.2 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  12.1 MBytes  10.1 Mbits/sec   33             sender
    [  5]   0.00-10.03  sec  11.9 MBytes  9.93 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 51448 bytes (148 packets)
    TX: 62487 bytes (250 packets)
    signal: -27 dBm
    rx bitrate: 6.0 MBit/s
    tx bitrate: 65.0 MBit/s MCS 7
    
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
