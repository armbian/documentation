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
**Test Date:** [2025-06-28 01:42 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15938708274)
### AC

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">152</span> Mbits/sec | <span style="font-size: 1.5rem;">272</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 33069 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.8 MBytes   157 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   182 MBytes   152 Mbits/sec  132             sender
    [  5]   0.00-10.00  sec   179 MBytes   150 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 43351 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.2 MBytes   287 Mbits/sec    0   1.12 MBytes       
    [  5]   1.00-2.00   sec  33.0 MBytes   277 Mbits/sec    0   1.24 MBytes       
    [  5]   2.00-3.00   sec  31.6 MBytes   265 Mbits/sec    0   1.28 MBytes       
    [  5]   3.00-4.00   sec  32.9 MBytes   276 Mbits/sec    0   1.28 MBytes       
    [  5]   4.00-5.00   sec  31.4 MBytes   263 Mbits/sec    0   1.28 MBytes       
    [  5]   5.00-6.00   sec  31.6 MBytes   265 Mbits/sec    0   1.35 MBytes       
    [  5]   6.00-7.00   sec  33.1 MBytes   278 Mbits/sec    0   1.41 MBytes       
    [  5]   7.00-8.00   sec  31.6 MBytes   265 Mbits/sec    0   1.41 MBytes       
    [  5]   8.00-9.00   sec  32.9 MBytes   276 Mbits/sec    0   1.48 MBytes       
    [  5]   9.00-10.00  sec  31.8 MBytes   266 Mbits/sec    0   1.48 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   324 MBytes   272 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   322 MBytes   269 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 188332 bytes (332 packets)
    TX: 94717 bytes (468 packets)
    signal: -35 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">196</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 37909 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.2 MBytes   145 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.2 MBytes   153 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec   183 MBytes   153 Mbits/sec   33             sender
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 47967 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.5 MBytes   214 Mbits/sec    0    619 KBytes       
    [  5]   1.00-2.00   sec  24.4 MBytes   204 Mbits/sec    0    687 KBytes       
    [  5]   2.00-3.00   sec  24.0 MBytes   201 Mbits/sec    0    762 KBytes       
    [  5]   3.00-4.00   sec  22.8 MBytes   191 Mbits/sec    0    762 KBytes       
    [  5]   4.00-5.00   sec  24.2 MBytes   203 Mbits/sec    0    762 KBytes       
    [  5]   5.00-6.00   sec  22.4 MBytes   188 Mbits/sec    0    807 KBytes       
    [  5]   6.00-7.00   sec  24.2 MBytes   203 Mbits/sec    0    848 KBytes       
    [  5]   7.00-8.00   sec  21.0 MBytes   176 Mbits/sec    0    848 KBytes       
    [  5]   8.00-9.00   sec  21.1 MBytes   177 Mbits/sec    0    848 KBytes       
    [  5]   9.00-10.00  sec  23.6 MBytes   198 Mbits/sec    0    848 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   233 MBytes   196 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   230 MBytes   193 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">271</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 33053 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.6 MBytes   148 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   183 MBytes   153 Mbits/sec    7             sender
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 35399 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  35.1 MBytes   294 Mbits/sec    0    874 KBytes       
    [  5]   1.00-2.00   sec  31.0 MBytes   260 Mbits/sec    0   1.07 MBytes       
    [  5]   2.00-3.00   sec  33.1 MBytes   278 Mbits/sec    0   1.13 MBytes       
    [  5]   3.00-4.00   sec  32.6 MBytes   274 Mbits/sec    0   1.37 MBytes       
    [  5]   4.00-5.00   sec  31.8 MBytes   266 Mbits/sec    0   1.44 MBytes       
    [  5]   5.00-6.00   sec  32.0 MBytes   268 Mbits/sec    0   1.52 MBytes       
    [  5]   6.00-7.00   sec  33.2 MBytes   279 Mbits/sec    0   1.61 MBytes       
    [  5]   7.00-8.00   sec  32.1 MBytes   269 Mbits/sec    0   1.70 MBytes       
    [  5]   8.00-9.00   sec  32.1 MBytes   269 Mbits/sec    0   1.70 MBytes       
    [  5]   9.00-10.00  sec  30.5 MBytes   256 Mbits/sec    0   1.79 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   324 MBytes   271 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   321 MBytes   269 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">144</span> Mbits/sec | <span style="font-size: 1.5rem;">212</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 38341 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.0 MBytes  92.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  14.2 MBytes   120 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   5.00-6.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.8 MBytes   149 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   172 MBytes   144 Mbits/sec   96             sender
    [  5]   0.00-10.00  sec   168 MBytes   141 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 50679 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  27.0 MBytes   226 Mbits/sec    0    608 KBytes       
    [  5]   1.00-2.00   sec  24.8 MBytes   208 Mbits/sec    0    676 KBytes       
    [  5]   2.00-3.00   sec  25.9 MBytes   217 Mbits/sec    0    676 KBytes       
    [  5]   3.00-4.00   sec  24.4 MBytes   204 Mbits/sec    0    676 KBytes       
    [  5]   4.00-5.00   sec  26.2 MBytes   220 Mbits/sec    0    778 KBytes       
    [  5]   5.00-6.00   sec  26.4 MBytes   221 Mbits/sec    0    778 KBytes       
    [  5]   6.00-7.00   sec  23.5 MBytes   197 Mbits/sec    0    814 KBytes       
    [  5]   7.00-8.00   sec  24.8 MBytes   208 Mbits/sec    0    814 KBytes       
    [  5]   8.00-9.00   sec  24.8 MBytes   208 Mbits/sec    0    814 KBytes       
    [  5]   9.00-10.00  sec  24.6 MBytes   206 Mbits/sec    0    814 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   252 MBytes   212 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   250 MBytes   209 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 197740 bytes (382 packets)
    TX: 96213 bytes (470 packets)
    signal: -37 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```
### AX

#### Ampak 6275P

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AP6275P.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.149, 6.12.33-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AP6275P</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">328</span> Mbits/sec | <span style="font-size: 1.5rem;">332</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 49203 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  35.5 MBytes   298 Mbits/sec                  
    [  5]   1.00-2.00   sec  36.5 MBytes   306 Mbits/sec                  
    [  5]   2.00-3.00   sec  39.6 MBytes   332 Mbits/sec                  
    [  5]   3.00-4.00   sec  37.9 MBytes   318 Mbits/sec                  
    [  5]   4.00-5.00   sec  40.6 MBytes   340 Mbits/sec                  
    [  5]   5.00-6.00   sec  39.8 MBytes   334 Mbits/sec                  
    [  5]   6.00-7.00   sec  39.2 MBytes   329 Mbits/sec                  
    [  5]   7.00-8.00   sec  39.2 MBytes   329 Mbits/sec                  
    [  5]   8.00-9.00   sec  39.4 MBytes   330 Mbits/sec                  
    [  5]   9.00-10.00  sec  41.3 MBytes   346 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   391 MBytes   328 Mbits/sec   59             sender
    [  5]   0.00-10.00  sec   389 MBytes   326 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 34781 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  48.2 MBytes   405 Mbits/sec    0   6.43 MBytes       
    [  5]   1.00-2.00   sec  47.5 MBytes   398 Mbits/sec    0   6.43 MBytes       
    [  5]   2.00-3.00   sec  38.8 MBytes   325 Mbits/sec    0   6.43 MBytes       
    [  5]   3.00-4.00   sec  41.2 MBytes   346 Mbits/sec    0   6.43 MBytes       
    [  5]   4.00-5.00   sec  40.0 MBytes   336 Mbits/sec    0   6.43 MBytes       
    [  5]   5.00-6.00   sec  38.8 MBytes   325 Mbits/sec    0   6.43 MBytes       
    [  5]   6.00-7.00   sec  43.8 MBytes   367 Mbits/sec    0   6.43 MBytes       
    [  5]   7.00-8.00   sec  31.2 MBytes   262 Mbits/sec    0   6.43 MBytes       
    [  5]   8.00-9.00   sec  27.5 MBytes   231 Mbits/sec    0   6.43 MBytes       
    [  5]   9.00-10.00  sec  38.8 MBytes   325 Mbits/sec    0   6.43 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   396 MBytes   332 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   394 MBytes   330 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 61887 bytes (126 packets)
    TX: 55182 bytes (208 packets)
    signal: -70 dBm
    rx bitrate: 720.5 MBit/s
    tx bitrate: 648.5 MBit/s
    
    ```

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">114</span> Mbits/sec | <span style="font-size: 1.5rem;">150</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 56011 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.1 MBytes   110 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   136 MBytes   114 Mbits/sec   76             sender
    [  5]   0.00-10.00  sec   132 MBytes   111 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 36495 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.1 MBytes   160 Mbits/sec    0    518 KBytes       
    [  5]   1.00-2.00   sec  18.5 MBytes   155 Mbits/sec    0    670 KBytes       
    [  5]   2.00-3.00   sec  18.0 MBytes   151 Mbits/sec    0    792 KBytes       
    [  5]   3.00-4.00   sec  16.8 MBytes   141 Mbits/sec    0    792 KBytes       
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec    0    836 KBytes       
    [  5]   5.00-6.00   sec  18.0 MBytes   151 Mbits/sec    0    880 KBytes       
    [  5]   6.00-7.00   sec  17.1 MBytes   144 Mbits/sec    0    925 KBytes       
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec    0    925 KBytes       
    [  5]   8.00-9.00   sec  17.0 MBytes   143 Mbits/sec    0   1022 KBytes       
    [  5]   9.00-10.00  sec  18.2 MBytes   153 Mbits/sec    0   1022 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   179 MBytes   150 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   176 MBytes   148 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 47333 bytes (187 packets)
    TX: 53127 bytes (215 packets)
    signal: -37 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">95.7</span> Mbits/sec | <span style="font-size: 1.5rem;">64.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 53581 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.9 MBytes  91.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   114 MBytes  95.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   112 MBytes  94.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 37229 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.38 MBytes  70.2 Mbits/sec    0    206 KBytes       
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec    0    216 KBytes       
    [  5]   2.00-3.00   sec  7.75 MBytes  65.0 Mbits/sec    0    216 KBytes       
    [  5]   3.00-4.00   sec  7.38 MBytes  61.9 Mbits/sec    0    216 KBytes       
    [  5]   4.00-5.00   sec  8.00 MBytes  67.1 Mbits/sec    0    272 KBytes       
    [  5]   5.00-6.00   sec  7.88 MBytes  66.1 Mbits/sec    0    272 KBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0    307 KBytes       
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec    0    328 KBytes       
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec    0    328 KBytes       
    [  5]   9.00-10.00  sec  7.50 MBytes  62.9 Mbits/sec    0    328 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  77.2 MBytes  64.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  75.8 MBytes  63.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 193848 bytes (614 packets)
    TX: 96511 bytes (552 packets)
    signal: -23 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">2.09</span> Mbits/sec | <span style="font-size: 1.5rem;">12.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 35967 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   1.00-2.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   2.00-3.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   3.00-4.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   4.00-5.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   5.00-6.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   6.00-7.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   7.00-8.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   8.00-9.00   sec   384 KBytes  3.15 Mbits/sec                  
    [  5]   9.00-10.00  sec   256 KBytes  2.10 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  2.50 MBytes  2.09 Mbits/sec   60             sender
    [  5]   0.00-10.00  sec  2.25 MBytes  1.89 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 53415 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.25 MBytes  10.5 Mbits/sec    0   84.8 KBytes       
    [  5]   1.00-2.00   sec  1.38 MBytes  11.5 Mbits/sec    0    139 KBytes       
    [  5]   2.00-3.00   sec   768 KBytes  6.29 Mbits/sec    1    115 KBytes       
    [  5]   3.00-4.00   sec  1.50 MBytes  12.6 Mbits/sec    0    143 KBytes       
    [  5]   4.00-5.00   sec  1.62 MBytes  13.6 Mbits/sec    0    157 KBytes       
    [  5]   5.00-6.00   sec  1.50 MBytes  12.6 Mbits/sec    1    113 KBytes       
    [  5]   6.00-7.00   sec  1.50 MBytes  12.6 Mbits/sec    0    130 KBytes       
    [  5]   7.00-8.00   sec  1.50 MBytes  12.6 Mbits/sec    1    103 KBytes       
    [  5]   8.00-9.00   sec  1.38 MBytes  11.5 Mbits/sec    0    110 KBytes       
    [  5]   9.00-10.00  sec  2.62 MBytes  22.0 Mbits/sec    0    126 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  15.0 MBytes  12.6 Mbits/sec    3             sender
    [  5]   0.00-10.01  sec  14.2 MBytes  11.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 90702 bytes (371 packets)
    TX: 57054 bytes (227 packets)
    signal: -31 dBm
    rx bitrate: 43.3 MBit/s MCS 4 short GI
    tx bitrate: 57.8 MBit/s MCS 5 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">97.8</span> Mbits/sec | <span style="font-size: 1.5rem;">67.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 33861 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.9 MBytes  91.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.5 MBytes  96.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   117 MBytes  97.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   114 MBytes  95.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 47263 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.75 MBytes  73.3 Mbits/sec    0    218 KBytes       
    [  5]   1.00-2.00   sec  7.88 MBytes  66.1 Mbits/sec    0    218 KBytes       
    [  5]   2.00-3.00   sec  7.88 MBytes  66.1 Mbits/sec    0    218 KBytes       
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec    0    229 KBytes       
    [  5]   4.00-5.00   sec  8.00 MBytes  67.1 Mbits/sec    0    229 KBytes       
    [  5]   5.00-6.00   sec  7.88 MBytes  66.1 Mbits/sec    0    229 KBytes       
    [  5]   6.00-7.00   sec  7.00 MBytes  58.7 Mbits/sec    0    229 KBytes       
    [  5]   7.00-8.00   sec  8.12 MBytes  68.2 Mbits/sec    0    288 KBytes       
    [  5]   8.00-9.00   sec  8.38 MBytes  70.3 Mbits/sec    0    397 KBytes       
    [  5]   9.00-10.00  sec  8.12 MBytes  68.1 Mbits/sec    0    397 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  80.4 MBytes  67.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  78.4 MBytes  65.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 91683 bytes (379 packets)
    TX: 63887 bytes (306 packets)
    signal: -30 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">38.0</span> Mbits/sec | <span style="font-size: 1.5rem;">25.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 48019 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.50 MBytes  37.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.38 MBytes  36.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.18  sec  46.1 MBytes  38.0 Mbits/sec   35             sender
    [  5]   0.00-10.00  sec  43.2 MBytes  36.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 48263 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.88 MBytes  32.5 Mbits/sec    0    202 KBytes       
    [  5]   1.00-2.00   sec  3.38 MBytes  28.3 Mbits/sec    0    238 KBytes       
    [  5]   2.00-3.00   sec  3.25 MBytes  27.3 Mbits/sec    0    257 KBytes       
    [  5]   3.00-4.00   sec  2.88 MBytes  24.1 Mbits/sec    0    273 KBytes       
    [  5]   4.00-5.00   sec  3.62 MBytes  30.4 Mbits/sec    0    304 KBytes       
    [  5]   5.00-6.00   sec  2.50 MBytes  21.0 Mbits/sec    0    320 KBytes       
    [  5]   6.00-7.00   sec  2.62 MBytes  22.0 Mbits/sec    0    320 KBytes       
    [  5]   7.00-8.00   sec  2.62 MBytes  22.0 Mbits/sec    0    337 KBytes       
    [  5]   8.00-9.00   sec  3.50 MBytes  29.4 Mbits/sec    0    337 KBytes       
    [  5]   9.00-10.00  sec  2.12 MBytes  17.8 Mbits/sec    0    337 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  30.4 MBytes  25.5 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  29.1 MBytes  24.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 90877 bytes (331 packets)
    TX: 57334 bytes (224 packets)
    signal: -40 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">25.0</span> Mbits/sec | <span style="font-size: 1.5rem;">43.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 49075 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.12 MBytes  26.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.38 MBytes  19.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  1.12 MBytes  9.44 Mbits/sec                  
    [  5]   8.00-9.00   sec  1.75 MBytes  14.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.88 MBytes  15.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.11  sec  30.1 MBytes  25.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  27.5 MBytes  23.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 50737 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.88 MBytes  49.2 Mbits/sec    0    270 KBytes       
    [  5]   1.00-2.00   sec  5.88 MBytes  49.3 Mbits/sec    0    411 KBytes       
    [  5]   2.00-3.00   sec  4.88 MBytes  40.9 Mbits/sec    0    411 KBytes       
    [  5]   3.00-4.00   sec  5.12 MBytes  43.0 Mbits/sec    0    411 KBytes       
    [  5]   4.00-5.00   sec  5.25 MBytes  44.0 Mbits/sec    0    438 KBytes       
    [  5]   5.00-6.00   sec  4.38 MBytes  36.7 Mbits/sec    0    460 KBytes       
    [  5]   6.00-7.00   sec  5.62 MBytes  47.2 Mbits/sec    0    484 KBytes       
    [  5]   7.00-8.00   sec  5.12 MBytes  43.0 Mbits/sec    0    484 KBytes       
    [  5]   8.00-9.00   sec  5.00 MBytes  42.0 Mbits/sec    0    512 KBytes       
    [  5]   9.00-10.00  sec  5.25 MBytes  44.0 Mbits/sec    0    512 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  52.4 MBytes  43.9 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  49.6 MBytes  41.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 85631 bytes (355 packets)
    TX: 57865 bytes (210 packets)
    signal: -48 dBm
    rx bitrate: 58.5 MBit/s MCS 6
    tx bitrate: 72.2 MBit/s MCS 7 short GI
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
