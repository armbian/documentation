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
**Test Date:** [2025-08-21 04:44 UTC](https://github.com/armbian/armbian.github.io/actions/runs/17116698960)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">50.5</span> Mbits/sec | <span style="font-size: 1.5rem;">51.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.152 port 53835 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.73 MBytes  48.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.08 MBytes  42.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.68 MBytes  47.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.84 MBytes  49.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.93 MBytes  49.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.52 MBytes  46.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.50 MBytes  46.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.69 MBytes  47.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.77 MBytes  48.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  60.4 MBytes  50.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  56.6 MBytes  47.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.152 port 43525 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.47 MBytes  62.7 Mbits/sec    0    383 KBytes       
    [  5]   1.00-2.00   sec  5.65 MBytes  47.4 Mbits/sec    0    485 KBytes       
    [  5]   2.00-3.00   sec  6.71 MBytes  56.3 Mbits/sec    0    600 KBytes       
    [  5]   3.00-4.00   sec  6.03 MBytes  50.6 Mbits/sec    0    634 KBytes       
    [  5]   4.00-5.00   sec  6.13 MBytes  51.4 Mbits/sec    0    728 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0    728 KBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0    809 KBytes       
    [  5]   7.00-8.00   sec  5.00 MBytes  41.9 Mbits/sec    0    809 KBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0    911 KBytes       
    [  5]   9.00-10.00  sec  5.00 MBytes  41.9 Mbits/sec    0    911 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  60.8 MBytes  51.0 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  58.1 MBytes  48.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 34995 bytes (133 packets)
    TX: 53410 bytes (199 packets)
    signal: -32 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">95.6</span> Mbits/sec | <span style="font-size: 1.5rem;">86.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.151 port 39207 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.0 MBytes  92.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.6 MBytes  89.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.6 MBytes  89.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.1 MBytes  93.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.2 MBytes  93.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.4 MBytes  95.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.4 MBytes  95.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.4 MBytes  95.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.6 MBytes  97.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.8 MBytes  99.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   114 MBytes  95.6 Mbits/sec   35             sender
    [  5]   0.00-10.00  sec   112 MBytes  94.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.151 port 39687 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  10.7 MBytes  89.5 Mbits/sec    0    419 KBytes       
    [  5]   1.00-2.00   sec  10.9 MBytes  91.2 Mbits/sec    0    488 KBytes       
    [  5]   2.00-3.00   sec  10.9 MBytes  91.7 Mbits/sec    0    571 KBytes       
    [  5]   3.00-4.00   sec  9.69 MBytes  81.3 Mbits/sec    0    571 KBytes       
    [  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0    605 KBytes       
    [  5]   5.00-6.00   sec  9.57 MBytes  80.3 Mbits/sec    0    605 KBytes       
    [  5]   6.00-7.00   sec  10.1 MBytes  84.4 Mbits/sec    0    605 KBytes       
    [  5]   7.00-8.00   sec  10.5 MBytes  88.1 Mbits/sec    0    636 KBytes       
    [  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0    636 KBytes       
    [  5]   9.00-10.00  sec  10.9 MBytes  91.2 Mbits/sec    0    636 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   103 MBytes  86.6 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   102 MBytes  84.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 108424 bytes (478 packets)
    TX: 58633 bytes (229 packets)
    signal: -44 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">174</span> Mbits/sec | <span style="font-size: 1.5rem;">229</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.132 port 36711 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  20.9 MBytes   175 Mbits/sec                  
    [  5]   1.00-2.00   sec  21.6 MBytes   181 Mbits/sec                  
    [  5]   2.00-3.00   sec  22.0 MBytes   185 Mbits/sec                  
    [  5]   3.00-4.00   sec  21.5 MBytes   180 Mbits/sec                  
    [  5]   4.00-5.00   sec  21.5 MBytes   180 Mbits/sec                  
    [  5]   5.00-6.00   sec  21.4 MBytes   179 Mbits/sec                  
    [  5]   6.00-7.00   sec  21.2 MBytes   178 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   8.00-9.00   sec  21.2 MBytes   178 Mbits/sec                  
    [  5]   9.00-10.00  sec  22.0 MBytes   185 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   207 MBytes   174 Mbits/sec  109             sender
    [  5]   0.00-10.00  sec   206 MBytes   173 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.132 port 55969 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  20.4 MBytes   171 Mbits/sec    4    178 KBytes       
    [  5]   1.00-2.00   sec  14.0 MBytes   117 Mbits/sec   28   93.3 KBytes       
    [  5]   2.00-3.00   sec  26.4 MBytes   221 Mbits/sec    0    221 KBytes       
    [  5]   3.00-4.00   sec  30.5 MBytes   256 Mbits/sec    0    308 KBytes       
    [  5]   4.00-5.00   sec  30.0 MBytes   252 Mbits/sec    0    376 KBytes       
    [  5]   5.00-6.00   sec  30.2 MBytes   254 Mbits/sec    0    433 KBytes       
    [  5]   6.00-7.00   sec  30.9 MBytes   259 Mbits/sec    0    484 KBytes       
    [  5]   7.00-8.00   sec  29.9 MBytes   251 Mbits/sec    0    530 KBytes       
    [  5]   8.00-9.00   sec  31.0 MBytes   260 Mbits/sec    0    573 KBytes       
    [  5]   9.00-10.00  sec  30.0 MBytes   252 Mbits/sec    0    612 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   273 MBytes   229 Mbits/sec   32             sender
    [  5]   0.00-10.02  sec   271 MBytes   227 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 182771 bytes (349 packets)
    TX: 96473 bytes (476 packets)
    signal: -34 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```

#### Realtek 8821CU #1

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">150</span> Mbits/sec | <span style="font-size: 1.5rem;">200</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 54775 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.4 MBytes   162 Mbits/sec                  
    [  5]   5.00-6.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.6 MBytes   156 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   179 MBytes   150 Mbits/sec    2             sender
    [  5]   0.00-10.00  sec   178 MBytes   149 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 47739 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  26.2 MBytes   220 Mbits/sec    0    573 KBytes       
    [  5]   1.00-2.00   sec  23.8 MBytes   199 Mbits/sec    0    604 KBytes       
    [  5]   2.00-3.00   sec  25.0 MBytes   210 Mbits/sec    0    634 KBytes       
    [  5]   3.00-4.00   sec  23.0 MBytes   193 Mbits/sec    0    666 KBytes       
    [  5]   4.00-5.00   sec  24.5 MBytes   206 Mbits/sec    0    666 KBytes       
    [  5]   5.00-6.00   sec  24.4 MBytes   204 Mbits/sec    0    666 KBytes       
    [  5]   6.00-7.00   sec  22.1 MBytes   186 Mbits/sec   72    133 KBytes       
    [  5]   7.00-8.00   sec  22.6 MBytes   190 Mbits/sec    0    228 KBytes       
    [  5]   8.00-9.00   sec  24.2 MBytes   204 Mbits/sec    0    298 KBytes       
    [  5]   9.00-10.00  sec  22.9 MBytes   192 Mbits/sec    0    355 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   239 MBytes   200 Mbits/sec   72             sender
    [  5]   0.00-10.01  sec   236 MBytes   198 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 165932 bytes (319 packets)
    TX: 86106 bytes (435 packets)
    signal: -43 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">236</span> Mbits/sec | <span style="font-size: 1.5rem;">255</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.150 port 52311 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  23.9 MBytes   200 Mbits/sec                  
    [  5]   1.00-2.00   sec  30.1 MBytes   253 Mbits/sec                  
    [  5]   2.00-3.00   sec  29.5 MBytes   247 Mbits/sec                  
    [  5]   3.00-4.00   sec  27.8 MBytes   233 Mbits/sec                  
    [  5]   4.00-5.00   sec  29.0 MBytes   243 Mbits/sec                  
    [  5]   5.00-6.00   sec  25.0 MBytes   210 Mbits/sec                  
    [  5]   6.00-7.00   sec  25.8 MBytes   216 Mbits/sec                  
    [  5]   7.00-8.00   sec  27.5 MBytes   231 Mbits/sec                  
    [  5]   8.00-9.00   sec  29.1 MBytes   244 Mbits/sec                  
    [  5]   9.00-10.00  sec  31.4 MBytes   263 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   282 MBytes   236 Mbits/sec  206             sender
    [  5]   0.00-10.00  sec   279 MBytes   234 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.150 port 58875 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  31.5 MBytes   264 Mbits/sec    0   1.55 MBytes       
    [  5]   1.00-2.00   sec  28.9 MBytes   242 Mbits/sec    0   1.86 MBytes       
    [  5]   2.00-3.00   sec  31.1 MBytes   261 Mbits/sec    0   3.16 MBytes       
    [  5]   3.00-4.00   sec  29.8 MBytes   250 Mbits/sec    0   3.16 MBytes       
    [  5]   4.00-5.00   sec  30.2 MBytes   254 Mbits/sec    0   5.51 MBytes       
    [  5]   5.00-6.00   sec  30.8 MBytes   258 Mbits/sec    0   5.51 MBytes       
    [  5]   6.00-7.00   sec  31.4 MBytes   263 Mbits/sec    0   5.51 MBytes       
    [  5]   7.00-8.00   sec  29.5 MBytes   247 Mbits/sec    0   5.51 MBytes       
    [  5]   8.00-9.00   sec  30.8 MBytes   258 Mbits/sec    0   5.51 MBytes       
    [  5]   9.00-10.00  sec  30.2 MBytes   254 Mbits/sec    0   5.51 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   304 MBytes   255 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   301 MBytes   252 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### Realtek 88X2CS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88X2CS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.1, 6.12.42-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88X2CS</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">90.5</span> Mbits/sec | <span style="font-size: 1.5rem;">200</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.136 port 43271 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.9 MBytes  91.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  9.38 MBytes  78.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.62 MBytes  80.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  9.88 MBytes  82.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   108 MBytes  90.5 Mbits/sec  142            sender
    [  5]   0.00-10.00  sec   107 MBytes  89.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.136 port 46661 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  24.1 MBytes   202 Mbits/sec    0   5.63 MBytes       
    [  5]   1.00-2.00   sec  24.6 MBytes   207 Mbits/sec    0   6.25 MBytes       
    [  5]   2.00-3.00   sec  24.0 MBytes   201 Mbits/sec    0   6.43 MBytes       
    [  5]   3.00-4.00   sec  25.4 MBytes   213 Mbits/sec    0   6.43 MBytes       
    [  5]   4.00-5.00   sec  24.8 MBytes   208 Mbits/sec    0   6.43 MBytes       
    [  5]   5.00-6.00   sec  23.5 MBytes   197 Mbits/sec    0   6.43 MBytes       
    [  5]   6.00-7.00   sec  23.5 MBytes   197 Mbits/sec    0   6.43 MBytes       
    [  5]   7.00-8.00   sec  21.5 MBytes   180 Mbits/sec   39    822 KBytes       
    [  5]   8.00-9.00   sec  24.1 MBytes   202 Mbits/sec    0    860 KBytes       
    [  5]   9.00-10.00  sec  23.0 MBytes   193 Mbits/sec    0    898 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   238 MBytes   200 Mbits/sec   39            sender
    [  5]   0.00-10.03  sec   236 MBytes   197 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 188985 bytes (382 packets)
    TX: 101823 bytes (499 packets)
    signal: -37 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 780.0 MBit/s VHT-MCS 8 80MHz short GI VHT-NSS 2
    ```
### AX

#### Ampak 6275P

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AP6275P.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.149, 6.12.33-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AP6275P</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">407</span> Mbits/sec | <span style="font-size: 1.5rem;">439</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 57597 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  45.3 MBytes   380 Mbits/sec                  
    [  5]   1.00-2.00   sec  48.0 MBytes   402 Mbits/sec                  
    [  5]   2.00-3.00   sec  47.7 MBytes   400 Mbits/sec                  
    [  5]   3.00-4.00   sec  49.3 MBytes   414 Mbits/sec                  
    [  5]   4.00-5.00   sec  49.6 MBytes   416 Mbits/sec                  
    [  5]   5.00-6.00   sec  49.3 MBytes   414 Mbits/sec                  
    [  5]   6.00-7.00   sec  46.8 MBytes   393 Mbits/sec                  
    [  5]   7.00-8.00   sec  46.0 MBytes   386 Mbits/sec                  
    [  5]   8.00-9.00   sec  51.3 MBytes   431 Mbits/sec                  
    [  5]   9.00-10.00  sec  48.9 MBytes   410 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   486 MBytes   407 Mbits/sec  170             sender
    [  5]   0.00-10.00  sec   482 MBytes   404 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 59711 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  84.0 MBytes   705 Mbits/sec  400   2.61 MBytes       
    [  5]   1.00-2.00   sec  76.2 MBytes   640 Mbits/sec  432    732 KBytes       
    [  5]   2.00-3.00   sec  58.8 MBytes   493 Mbits/sec  207    468 KBytes       
    [  5]   3.00-4.00   sec  50.0 MBytes   419 Mbits/sec   67    341 KBytes       
    [  5]   4.00-5.00   sec  47.5 MBytes   398 Mbits/sec    0    505 KBytes       
    [  5]   5.00-6.00   sec  52.5 MBytes   440 Mbits/sec    1    351 KBytes       
    [  5]   6.00-7.00   sec  46.2 MBytes   388 Mbits/sec    0    509 KBytes       
    [  5]   7.00-8.00   sec  26.2 MBytes   220 Mbits/sec   43    103 KBytes       
    [  5]   8.00-9.00   sec  33.8 MBytes   283 Mbits/sec    0    324 KBytes       
    [  5]   9.00-10.00  sec  47.5 MBytes   398 Mbits/sec    0    492 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   523 MBytes   439 Mbits/sec  1150             sender
    [  5]   0.00-10.01  sec   519 MBytes   435 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 64251 bytes (133 packets)
    TX: 56569 bytes (205 packets)
    signal: -35 dBm
    rx bitrate: 960.7 MBit/s
    tx bitrate: 1020.8 MBit/s
    
    ```

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">109</span> Mbits/sec | <span style="font-size: 1.5rem;">119</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 46167 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.62 MBytes  80.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.2 MBytes   111 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   131 MBytes   109 Mbits/sec    7             sender
    [  5]   0.00-10.00  sec   128 MBytes   108 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 56979 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  13.1 MBytes   110 Mbits/sec    0    573 KBytes       
    [  5]   1.00-2.00   sec  14.9 MBytes   125 Mbits/sec    0   1.07 MBytes       
    [  5]   2.00-3.00   sec  14.4 MBytes   121 Mbits/sec    0   1.44 MBytes       
    [  5]   3.00-4.00   sec  14.4 MBytes   121 Mbits/sec    0   1.54 MBytes       
    [  5]   4.00-5.00   sec  14.5 MBytes   122 Mbits/sec    0   1.71 MBytes       
    [  5]   5.00-6.02   sec  12.6 MBytes   104 Mbits/sec    0   1.81 MBytes       
    [  5]   6.02-7.00   sec  16.1 MBytes   138 Mbits/sec    0   1.81 MBytes       
    [  5]   7.00-8.00   sec  14.5 MBytes   122 Mbits/sec    0   1.81 MBytes       
    [  5]   8.00-9.01   sec  12.6 MBytes   105 Mbits/sec    0   1.81 MBytes       
    [  5]   9.01-10.01  sec  14.6 MBytes   123 Mbits/sec    0   1.81 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   142 MBytes   119 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   139 MBytes   116 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 49676 bytes (187 packets)
    TX: 50368 bytes (209 packets)
    signal: -35 dBm
    rx bitrate: 258.0 MBit/s HE-MCS 10 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 286.7 MBit/s HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">574</span> Mbits/sec | <span style="font-size: 1.5rem;">597</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 37617 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  62.1 MBytes   521 Mbits/sec                  
    [  5]   1.00-2.00   sec  41.0 MBytes   344 Mbits/sec                  
    [  5]   2.00-3.00   sec  69.9 MBytes   586 Mbits/sec                  
    [  5]   3.00-4.00   sec  91.8 MBytes   770 Mbits/sec                  
    [  5]   4.00-5.00   sec  97.2 MBytes   816 Mbits/sec                  
    [  5]   5.00-6.00   sec  85.6 MBytes   718 Mbits/sec                  
    [  5]   6.00-7.00   sec  70.2 MBytes   589 Mbits/sec                  
    [  5]   7.00-8.00   sec  35.9 MBytes   301 Mbits/sec                  
    [  5]   8.00-9.00   sec  60.1 MBytes   504 Mbits/sec                  
    [  5]   9.00-10.00  sec  68.2 MBytes   573 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   685 MBytes   574 Mbits/sec  275             sender
    [  5]   0.00-10.00  sec   682 MBytes   572 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 58459 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  85.9 MBytes   720 Mbits/sec   37    860 KBytes       
    [  5]   1.00-2.00   sec  64.9 MBytes   544 Mbits/sec   64    602 KBytes       
    [  5]   2.00-3.00   sec  56.6 MBytes   475 Mbits/sec   74    491 KBytes       
    [  5]   3.00-4.00   sec  75.2 MBytes   631 Mbits/sec    0    676 KBytes       
    [  5]   4.00-5.00   sec  70.1 MBytes   588 Mbits/sec   21    526 KBytes       
    [  5]   5.00-6.00   sec  74.5 MBytes   625 Mbits/sec    0    701 KBytes       
    [  5]   6.00-7.00   sec  77.1 MBytes   647 Mbits/sec    0    847 KBytes       
    [  5]   7.00-8.00   sec  78.6 MBytes   660 Mbits/sec   16    557 KBytes       
    [  5]   8.00-9.00   sec  67.9 MBytes   569 Mbits/sec    3    389 KBytes       
    [  5]   9.00-10.00  sec  60.6 MBytes   507 Mbits/sec    0    570 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   712 MBytes   597 Mbits/sec  215             sender
    [  5]   0.00-10.01  sec   709 MBytes   594 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 37330 bytes (157 packets)
    TX: 54023 bytes (196 packets)
    signal: -28 dBm
    rx bitrate: 2401.9 MBit/s 160MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```

#### Realtek 8852AE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8852AE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.1, 6.12.42-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8852AE</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">482</span> Mbits/sec | <span style="font-size: 1.5rem;">606</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.135 port 45657 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  75.2 MBytes   631 Mbits/sec                  
    [  5]   1.00-2.00   sec  75.7 MBytes   635 Mbits/sec                  
    [  5]   2.00-3.00   sec  63.3 MBytes   531 Mbits/sec                  
    [  5]   3.00-4.00   sec  49.2 MBytes   413 Mbits/sec                  
    [  5]   4.00-5.00   sec  49.6 MBytes   416 Mbits/sec                  
    [  5]   5.00-6.00   sec  41.8 MBytes   351 Mbits/sec                  
    [  5]   6.00-7.00   sec  27.8 MBytes   233 Mbits/sec                  
    [  5]   7.00-8.00   sec  51.5 MBytes   432 Mbits/sec                  
    [  5]   8.00-9.00   sec  64.8 MBytes   543 Mbits/sec                  
    [  5]   9.00-10.00  sec  71.7 MBytes   601 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   574 MBytes   482 Mbits/sec  293             sender
    [  5]   0.00-10.00  sec   571 MBytes   479 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.135 port 55669 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  66.8 MBytes   560 Mbits/sec  1324    467 KBytes       
    [  5]   1.00-2.00   sec  55.0 MBytes   461 Mbits/sec   49    361 KBytes       
    [  5]   2.00-3.00   sec  53.8 MBytes   451 Mbits/sec    0    533 KBytes       
    [  5]   3.00-4.00   sec  72.5 MBytes   608 Mbits/sec    0    704 KBytes       
    [  5]   4.00-5.00   sec  77.5 MBytes   650 Mbits/sec   21    462 KBytes       
    [  5]   5.00-6.00   sec  73.8 MBytes   619 Mbits/sec    0    652 KBytes       
    [  5]   6.00-7.00   sec  81.2 MBytes   682 Mbits/sec    0    813 KBytes       
    [  5]   7.00-8.00   sec  85.0 MBytes   711 Mbits/sec    0    953 KBytes       
    [  5]   8.00-9.00   sec  81.2 MBytes   683 Mbits/sec   40    583 KBytes       
    [  5]   9.00-10.00  sec  76.2 MBytes   638 Mbits/sec    0    748 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   723 MBytes   606 Mbits/sec  1434             sender
    [  5]   0.00-10.01  sec   720 MBytes   604 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 125021 bytes (476 packets)
    TX: 58911 bytes (215 packets)
    signal: -29 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    
    ```

#### Realtek 8852BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8852BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.1, 6.6.99-current-spacemit</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8852BS</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">405</span> Mbits/sec | <span style="font-size: 1.5rem;">341</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 58587 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  41.5 MBytes   348 Mbits/sec                  
    [  5]   1.00-2.00   sec  49.9 MBytes   418 Mbits/sec                  
    [  5]   2.00-3.00   sec  47.4 MBytes   397 Mbits/sec                  
    [  5]   3.00-4.00   sec  49.5 MBytes   415 Mbits/sec                  
    [  5]   4.00-5.00   sec  47.0 MBytes   394 Mbits/sec                  
    [  5]   5.00-6.00   sec  48.8 MBytes   409 Mbits/sec                  
    [  5]   6.00-7.00   sec  49.6 MBytes   416 Mbits/sec                  
    [  5]   7.00-8.00   sec  48.6 MBytes   408 Mbits/sec                  
    [  5]   8.00-9.00   sec  49.1 MBytes   412 Mbits/sec                  
    [  5]   9.00-10.00  sec  48.1 MBytes   404 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   483 MBytes   405 Mbits/sec  151             sender
    [  5]   0.00-10.00  sec   480 MBytes   402 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 46195 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  31.4 MBytes   263 Mbits/sec   23    266 KBytes       
    [  5]   1.00-2.00   sec  34.8 MBytes   292 Mbits/sec    0    352 KBytes       
    [  5]   2.00-3.00   sec  41.0 MBytes   344 Mbits/sec    0    434 KBytes       
    [  5]   3.00-4.00   sec  41.6 MBytes   349 Mbits/sec    0    503 KBytes       
    [  5]   4.00-5.00   sec  41.9 MBytes   351 Mbits/sec    0    563 KBytes       
    [  5]   5.00-6.00   sec  41.8 MBytes   350 Mbits/sec    0    618 KBytes       
    [  5]   6.00-7.00   sec  45.0 MBytes   377 Mbits/sec    0    670 KBytes       
    [  5]   7.00-8.00   sec  44.5 MBytes   373 Mbits/sec   12    526 KBytes       
    [  5]   8.00-9.00   sec  42.4 MBytes   355 Mbits/sec    0    592 KBytes       
    [  5]   9.00-10.00  sec  42.8 MBytes   358 Mbits/sec    0    638 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   407 MBytes   341 Mbits/sec   35             sender
    [  5]   0.00-10.01  sec   405 MBytes   339 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 43628 bytes (79 packets)
    TX: 42924 bytes (218 packets)
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">82.7</span> Mbits/sec | <span style="font-size: 1.5rem;">44.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 40311 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  8.75 MBytes  73.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  9.88 MBytes  82.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.38 MBytes  78.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  9.25 MBytes  77.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  9.62 MBytes  80.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  9.75 MBytes  81.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.75 MBytes  81.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  98.6 MBytes  82.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  96.1 MBytes  80.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 38265 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec    0    209 KBytes       
    [  5]   1.00-2.00   sec  4.62 MBytes  38.8 Mbits/sec    0    228 KBytes       
    [  5]   2.00-3.00   sec  5.50 MBytes  46.1 Mbits/sec    0    228 KBytes       
    [  5]   3.00-4.00   sec  4.50 MBytes  37.7 Mbits/sec    0    252 KBytes       
    [  5]   4.00-5.00   sec  4.50 MBytes  37.7 Mbits/sec    0    252 KBytes       
    [  5]   5.00-6.00   sec  5.25 MBytes  44.1 Mbits/sec    0    252 KBytes       
    [  5]   6.00-7.00   sec  4.62 MBytes  38.8 Mbits/sec    0    252 KBytes       
    [  5]   7.00-8.00   sec  5.38 MBytes  45.1 Mbits/sec    0    252 KBytes       
    [  5]   8.00-9.00   sec  6.12 MBytes  51.4 Mbits/sec    0    327 KBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.3 Mbits/sec    0    327 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  53.0 MBytes  44.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  51.1 MBytes  42.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 185215 bytes (591 packets)
    TX: 91276 bytes (526 packets)
    signal: -17 dBm
    rx bitrate: 150.0 MBit/s MCS 7 40MHz short GI
    tx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    ```

#### Atheros AR9271

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">47.4</span> Mbits/sec | <span style="font-size: 1.5rem;">43.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.129 port 43035 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.38 MBytes  45.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  56.6 MBytes  47.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  52.9 MBytes  44.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.129 port 37501 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.88 MBytes  49.2 Mbits/sec    0    202 KBytes       
    [  5]   1.00-2.00   sec  5.12 MBytes  43.0 Mbits/sec    0    214 KBytes       
    [  5]   2.00-3.00   sec  5.00 MBytes  41.9 Mbits/sec    0    214 KBytes       
    [  5]   3.00-4.00   sec  5.25 MBytes  44.0 Mbits/sec    0    225 KBytes       
    [  5]   4.00-5.00   sec  4.50 MBytes  37.7 Mbits/sec    0    225 KBytes       
    [  5]   5.00-6.00   sec  5.00 MBytes  41.9 Mbits/sec    0    225 KBytes       
    [  5]   6.00-7.00   sec  5.75 MBytes  48.2 Mbits/sec    0    257 KBytes       
    [  5]   7.00-8.00   sec  5.12 MBytes  43.0 Mbits/sec    0    257 KBytes       
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec    0    257 KBytes       
    [  5]   9.00-10.00  sec  4.88 MBytes  40.9 Mbits/sec    0    257 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  51.5 MBytes  43.2 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  50.6 MBytes  42.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 90402 bytes (378 packets)
    TX: 55728 bytes (211 packets)
    signal: -39 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 52.0 MBit/s MCS 5
    ```

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">44.3</span> Mbits/sec | <span style="font-size: 1.5rem;">35.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 51791 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.83 MBytes  40.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.19 MBytes  43.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.18 MBytes  43.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.30 MBytes  44.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.28 MBytes  44.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.09 MBytes  42.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.17 MBytes  43.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.15 MBytes  43.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.26 MBytes  44.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.36 MBytes  45.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.47  sec  55.2 MBytes  44.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  51.8 MBytes  43.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 48267 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.00 MBytes  42.0 Mbits/sec    0    195 KBytes       
    [  5]   1.00-2.00   sec  4.54 MBytes  38.1 Mbits/sec    0    205 KBytes       
    [  5]   2.00-3.00   sec  3.48 MBytes  29.2 Mbits/sec    0    205 KBytes       
    [  5]   3.00-4.00   sec  4.23 MBytes  35.4 Mbits/sec    0    205 KBytes       
    [  5]   4.00-5.00   sec  4.47 MBytes  37.5 Mbits/sec    0    205 KBytes       
    [  5]   5.00-6.00   sec  4.23 MBytes  35.4 Mbits/sec    0    219 KBytes       
    [  5]   6.00-7.00   sec  4.47 MBytes  37.5 Mbits/sec    1    160 KBytes       
    [  5]   7.00-8.00   sec  4.23 MBytes  35.4 Mbits/sec    0    188 KBytes       
    [  5]   8.00-9.00   sec  3.73 MBytes  31.3 Mbits/sec    0    204 KBytes       
    [  5]   9.00-10.00  sec  4.47 MBytes  37.5 Mbits/sec    0    214 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  42.8 MBytes  35.9 Mbits/sec    1             sender
    [  5]   0.00-10.03  sec  42.2 MBytes  35.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 55584 bytes (151 packets)
    TX: 54072 bytes (265 packets)
    signal: -53 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">47.4</span> Mbits/sec | <span style="font-size: 1.5rem;">54.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 44919 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.70 MBytes  47.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.42 MBytes  53.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.85 MBytes  49.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.41 MBytes  45.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.14 MBytes  43.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.55 MBytes  46.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.08 MBytes  42.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.06 MBytes  42.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.39 MBytes  45.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.59 MBytes  46.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  56.6 MBytes  47.4 Mbits/sec   17             sender
    [  5]   0.00-10.00  sec  55.2 MBytes  46.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 46105 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.16 MBytes  51.6 Mbits/sec    0    201 KBytes       
    [  5]   1.00-2.00   sec  6.34 MBytes  53.2 Mbits/sec    0    242 KBytes       
    [  5]   2.00-3.00   sec  7.15 MBytes  59.8 Mbits/sec    0    283 KBytes       
    [  5]   3.00-4.00   sec  7.27 MBytes  61.1 Mbits/sec    0    361 KBytes       
    [  5]   4.00-5.00   sec  6.21 MBytes  52.2 Mbits/sec    0    380 KBytes       
    [  5]   5.00-6.00   sec  5.34 MBytes  44.8 Mbits/sec    2    266 KBytes       
    [  5]   6.00-7.00   sec  6.28 MBytes  52.7 Mbits/sec    0    266 KBytes       
    [  5]   7.00-8.00   sec  6.21 MBytes  52.1 Mbits/sec    0    284 KBytes       
    [  5]   8.00-9.00   sec  7.46 MBytes  62.5 Mbits/sec    0    341 KBytes       
    [  5]   9.00-10.00  sec  6.34 MBytes  53.1 Mbits/sec    0    341 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  64.8 MBytes  54.3 Mbits/sec    2             sender
    [  5]   0.00-10.02  sec  63.0 MBytes  52.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 50725 bytes (135 packets)
    TX: 50261 bytes (244 packets)
    signal: -44 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">45.9</span> Mbits/sec | <span style="font-size: 1.5rem;">41.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 53993 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.12 MBytes  43.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  54.8 MBytes  45.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  52.0 MBytes  43.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 54929 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.12 MBytes  51.3 Mbits/sec    0    283 KBytes       
    [  5]   1.00-2.00   sec  5.88 MBytes  49.3 Mbits/sec    0    454 KBytes       
    [  5]   2.00-3.00   sec  5.25 MBytes  44.1 Mbits/sec    0    588 KBytes       
    [  5]   3.00-4.00   sec  5.38 MBytes  45.1 Mbits/sec    0    675 KBytes       
    [  5]   4.00-5.00   sec  4.00 MBytes  33.6 Mbits/sec    0    713 KBytes       
    [  5]   5.00-6.00   sec  4.25 MBytes  35.6 Mbits/sec    0    748 KBytes       
    [  5]   6.00-7.00   sec  5.62 MBytes  47.2 Mbits/sec    0    795 KBytes       
    [  5]   7.00-8.00   sec  4.25 MBytes  35.7 Mbits/sec    1    556 KBytes       
    [  5]   8.00-9.00   sec  4.12 MBytes  34.6 Mbits/sec    0    581 KBytes       
    [  5]   9.00-10.00  sec  4.12 MBytes  34.6 Mbits/sec    0    626 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  49.0 MBytes  41.1 Mbits/sec    1             sender
    [  5]   0.00-10.01  sec  45.4 MBytes  38.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 94099 bytes (393 packets)
    TX: 56049 bytes (221 packets)
    signal: -31 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">69.0</span> Mbits/sec | <span style="font-size: 1.5rem;">46.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 54317 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.12 MBytes  68.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  8.88 MBytes  74.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.12 MBytes  68.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  7.50 MBytes  62.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  7.50 MBytes  62.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  8.12 MBytes  68.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  7.00 MBytes  58.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  8.50 MBytes  71.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  8.25 MBytes  69.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  82.2 MBytes  69.0 Mbits/sec    3             sender
    [  5]   0.00-10.00  sec  79.2 MBytes  66.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 59209 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.12 MBytes  59.7 Mbits/sec    0    209 KBytes       
    [  5]   1.00-2.00   sec  5.25 MBytes  44.0 Mbits/sec    0    218 KBytes       
    [  5]   2.00-3.00   sec  5.50 MBytes  46.1 Mbits/sec    0    226 KBytes       
    [  5]   3.00-4.00   sec  5.50 MBytes  46.1 Mbits/sec    0    226 KBytes       
    [  5]   4.00-5.00   sec  5.38 MBytes  45.1 Mbits/sec    0    239 KBytes       
    [  5]   5.00-6.00   sec  4.88 MBytes  40.9 Mbits/sec    3    180 KBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec    0    201 KBytes       
    [  5]   7.00-8.00   sec  5.00 MBytes  41.9 Mbits/sec    0    201 KBytes       
    [  5]   8.00-9.00   sec  5.50 MBytes  46.1 Mbits/sec    0    201 KBytes       
    [  5]   9.00-10.00  sec  5.38 MBytes  45.0 Mbits/sec    0    201 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  55.1 MBytes  46.2 Mbits/sec    3             sender
    [  5]   0.00-10.00  sec  54.1 MBytes  45.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 71954 bytes (352 packets)
    TX: 59182 bytes (255 packets)
    signal: -28 dBm
    rx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">35.2</span> Mbits/sec | <span style="font-size: 1.5rem;">28.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 38689 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.00 MBytes  33.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.62 MBytes  30.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.38 MBytes  36.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.15  sec  42.6 MBytes  35.2 Mbits/sec  202             sender
    [  5]   0.00-10.00  sec  39.9 MBytes  33.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 59035 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.62 MBytes  30.4 Mbits/sec    0    167 KBytes       
    [  5]   1.00-2.00   sec  3.62 MBytes  30.4 Mbits/sec    0    255 KBytes       
    [  5]   2.00-3.00   sec  3.62 MBytes  30.4 Mbits/sec    0    315 KBytes       
    [  5]   3.00-4.00   sec  3.38 MBytes  28.3 Mbits/sec    0    332 KBytes       
    [  5]   4.00-5.00   sec  3.00 MBytes  25.2 Mbits/sec    1   1.41 KBytes       
    [  5]   5.00-6.00   sec  4.00 MBytes  33.6 Mbits/sec    0    373 KBytes       
    [  5]   6.00-7.00   sec  3.12 MBytes  26.2 Mbits/sec    0    392 KBytes       
    [  5]   7.00-8.00   sec  3.25 MBytes  27.3 Mbits/sec    0    411 KBytes       
    [  5]   8.00-9.00   sec  3.50 MBytes  29.4 Mbits/sec    0    411 KBytes       
    [  5]   9.00-10.00  sec  3.25 MBytes  27.3 Mbits/sec    0    411 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  34.4 MBytes  28.8 Mbits/sec    1             sender
    [  5]   0.00-10.04  sec  32.6 MBytes  27.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 61776 bytes (180 packets)
    TX: 51776 bytes (211 packets)
    signal: -46 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">37.4</span> Mbits/sec | <span style="font-size: 1.5rem;">20.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 45949 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.55 MBytes  38.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.39 MBytes  36.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.20 MBytes  35.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.50 MBytes  37.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.79 MBytes  31.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  3.34 MBytes  28.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.54 MBytes  29.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.20 MBytes  35.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.39 MBytes  36.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.52 MBytes  37.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  44.6 MBytes  37.4 Mbits/sec    4             sender
    [  5]   0.00-10.00  sec  41.4 MBytes  34.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 40991 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.97 MBytes  41.7 Mbits/sec    0    256 KBytes       
    [  5]   1.00-2.00   sec  4.60 MBytes  38.6 Mbits/sec    0    472 KBytes       
    [  5]   2.00-3.00   sec  2.98 MBytes  25.0 Mbits/sec    0    559 KBytes       
    [  5]   3.00-4.00   sec  1.99 MBytes  16.7 Mbits/sec    0    648 KBytes       
    [  5]   4.00-5.00   sec  1.55 MBytes  13.0 Mbits/sec    0    700 KBytes       
    [  5]   5.00-6.00   sec  1.49 MBytes  12.5 Mbits/sec    0    700 KBytes       
    [  5]   6.00-7.00   sec   891 KBytes  7.30 Mbits/sec    0    700 KBytes       
    [  5]   7.00-8.00   sec  1.49 MBytes  12.5 Mbits/sec    0    720 KBytes       
    [  5]   8.00-9.00   sec  2.55 MBytes  21.4 Mbits/sec    0    802 KBytes       
    [  5]   9.00-10.00  sec  1.93 MBytes  16.2 Mbits/sec    0    846 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  24.4 MBytes  20.5 Mbits/sec    0             sender
    [  5]   0.00-10.19  sec  22.9 MBytes  18.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.154, 6.12.30-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">52.2</span> Mbits/sec | <span style="font-size: 1.5rem;">50.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.138 port 35535 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.60 MBytes  46.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.01 MBytes  50.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.97 MBytes  50.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.01 MBytes  50.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.17 MBytes  51.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.84 MBytes  49.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.90 MBytes  49.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.86 MBytes  40.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  7.21 MBytes  60.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.32 MBytes  44.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  62.2 MBytes  52.2 Mbits/sec   98             sender
    [  5]   0.00-10.00  sec  58.9 MBytes  49.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.138 port 44455 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.54 MBytes  63.3 Mbits/sec    0    327 KBytes       
    [  5]   1.00-2.00   sec  6.59 MBytes  55.3 Mbits/sec    0    417 KBytes       
    [  5]   2.00-3.00   sec  4.54 MBytes  38.0 Mbits/sec    0    461 KBytes       
    [  5]   3.00-4.00   sec  6.08 MBytes  51.0 Mbits/sec    0    533 KBytes       
    [  5]   4.00-5.00   sec  5.88 MBytes  49.3 Mbits/sec    0    615 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0    619 KBytes       
    [  5]   6.00-7.00   sec  6.00 MBytes  50.3 Mbits/sec    0    619 KBytes       
    [  5]   7.00-8.00   sec  5.00 MBytes  41.9 Mbits/sec    0    653 KBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0    653 KBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0    732 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  60.4 MBytes  50.6 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  57.1 MBytes  47.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 41916 bytes (174 packets)
    ```

## Failed Devices

| Commercial Name | Chip | Class |
|:-----|:--------|:------|
| AIC8800 | AIC8800 | AX |
| BrosTrend 1800 | RTL8852AU | AX |
| Mediatek MT7925 | MT7925 | AX |
| Mediatek MT7925E #1 | MT7925E | AX |
| Mediatek MT7925E #2 | MT7925E | AX |
| Ralink MT7601U | MT7601U | N |
| Realtek 8188EU | RTL8192CU | N |
| Realtek 8811AU | RTL8812AU | AC |
| Realtek 8812AU | RTL8812AU | AC |
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
