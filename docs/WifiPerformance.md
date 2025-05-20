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
**Test Date:** [2025-05-20 10:12 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15133953816)
### AC

#### BCM4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">57.1</span> Mbits/sec | <span style="font-size: 1.5rem;">58.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 34653 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.38 MBytes  53.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.46 MBytes  54.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.49 MBytes  54.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.55 MBytes  54.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.53 MBytes  54.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.43 MBytes  54.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.46 MBytes  54.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.48 MBytes  54.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.40 MBytes  53.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.38 MBytes  53.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  68.2 MBytes  57.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  64.6 MBytes  54.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 41983 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.83 MBytes  65.7 Mbits/sec    0    421 KBytes       
    [  5]   1.00-2.00   sec  8.55 MBytes  71.7 Mbits/sec    0    626 KBytes       
    [  5]   2.00-3.00   sec  7.50 MBytes  62.9 Mbits/sec    0    897 KBytes       
    [  5]   3.00-4.00   sec  6.25 MBytes  52.4 Mbits/sec    0    942 KBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1015 KBytes       
    [  5]   5.00-6.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.13 MBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.30 MBytes       
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.47 MBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.55 MBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.59 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  70.1 MBytes  58.8 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  68.0 MBytes  56.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 39959 bytes (160 packets)
    TX: 53708 bytes (215 packets)
    signal: -27 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">117</span> Mbits/sec | <span style="font-size: 1.5rem;">85.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 46183 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   2.00-3.00   sec  14.0 MBytes   117 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.8 MBytes   115 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.9 MBytes   117 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.9 MBytes   116 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.5 MBytes   113 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   140 MBytes   117 Mbits/sec    9             sender
    [  5]   0.00-10.00  sec   137 MBytes   115 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 37643 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  11.2 MBytes  94.2 Mbits/sec    0    448 KBytes       
    [  5]   1.00-2.00   sec  9.38 MBytes  78.7 Mbits/sec    0    530 KBytes       
    [  5]   2.00-3.00   sec  10.9 MBytes  91.7 Mbits/sec    0    590 KBytes       
    [  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0    590 KBytes       
    [  5]   4.00-5.00   sec  10.1 MBytes  85.0 Mbits/sec    0    650 KBytes       
    [  5]   5.00-6.00   sec  9.76 MBytes  81.8 Mbits/sec    0    650 KBytes       
    [  5]   6.00-7.00   sec  9.82 MBytes  82.4 Mbits/sec    0    691 KBytes       
    [  5]   7.00-8.00   sec  9.45 MBytes  79.2 Mbits/sec    0    691 KBytes       
    [  5]   8.00-9.00   sec  11.6 MBytes  97.0 Mbits/sec    0    691 KBytes       
    [  5]   9.00-10.00  sec  9.38 MBytes  78.7 Mbits/sec    0    691 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   102 MBytes  85.3 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec   100 MBytes  83.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 109370 bytes (476 packets)
    TX: 56861 bytes (230 packets)
    signal: -45 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">94.7</span> Mbits/sec | <span style="font-size: 1.5rem;">52.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 53693 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.62 MBytes  80.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  9.62 MBytes  80.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.8 MBytes  98.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   113 MBytes  94.7 Mbits/sec    2             sender
    [  5]   0.00-10.00  sec   112 MBytes  93.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 41189 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.25 MBytes  60.8 Mbits/sec    0    352 KBytes       
    [  5]   1.00-2.00   sec  6.75 MBytes  56.6 Mbits/sec    0    550 KBytes       
    [  5]   2.00-3.00   sec  6.00 MBytes  50.3 Mbits/sec    0    581 KBytes       
    [  5]   3.00-4.00   sec  6.25 MBytes  52.4 Mbits/sec    0    662 KBytes       
    [  5]   4.00-5.00   sec  5.25 MBytes  44.0 Mbits/sec    0    662 KBytes       
    [  5]   5.00-6.00   sec  7.00 MBytes  58.7 Mbits/sec    0    697 KBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec    0    740 KBytes       
    [  5]   7.00-8.00   sec  6.75 MBytes  56.6 Mbits/sec    0    740 KBytes       
    [  5]   8.00-9.00   sec  5.62 MBytes  47.2 Mbits/sec    0    778 KBytes       
    [  5]   9.00-10.00  sec  5.88 MBytes  49.3 Mbits/sec    0    778 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  62.2 MBytes  52.2 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  59.0 MBytes  49.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 173484 bytes (409 packets)
    TX: 90605 bytes (482 packets)
    signal: -37 dBm
    rx bitrate: 130.0 MBit/s MCS 15
    tx bitrate: 117.0 MBit/s MCS 14
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">189</span> Mbits/sec | <span style="font-size: 1.5rem;">190</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 32861 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  20.1 MBytes   169 Mbits/sec                  
    [  5]   1.00-2.00   sec  23.2 MBytes   195 Mbits/sec                  
    [  5]   2.00-3.00   sec  22.5 MBytes   189 Mbits/sec                  
    [  5]   3.00-4.00   sec  22.2 MBytes   187 Mbits/sec                  
    [  5]   4.00-5.00   sec  22.6 MBytes   190 Mbits/sec                  
    [  5]   5.00-6.00   sec  22.5 MBytes   189 Mbits/sec                  
    [  5]   6.00-7.00   sec  22.1 MBytes   186 Mbits/sec                  
    [  5]   7.00-8.00   sec  22.0 MBytes   185 Mbits/sec                  
    [  5]   8.00-9.00   sec  22.5 MBytes   189 Mbits/sec                  
    [  5]   9.00-10.00  sec  22.4 MBytes   188 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   225 MBytes   189 Mbits/sec  269             sender
    [  5]   0.00-10.00  sec   222 MBytes   186 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 59551 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.1 MBytes   211 Mbits/sec    0    585 KBytes       
    [  5]   1.00-2.00   sec  23.8 MBytes   199 Mbits/sec    0    701 KBytes       
    [  5]   2.00-3.00   sec  24.0 MBytes   201 Mbits/sec    0    740 KBytes       
    [  5]   3.00-4.00   sec  22.6 MBytes   190 Mbits/sec    0    740 KBytes       
    [  5]   4.00-5.00   sec  16.6 MBytes   139 Mbits/sec    0    781 KBytes       
    [  5]   5.00-6.00   sec  21.2 MBytes   178 Mbits/sec    0    781 KBytes       
    [  5]   6.00-7.00   sec  22.6 MBytes   190 Mbits/sec    0    781 KBytes       
    [  5]   7.00-8.00   sec  23.4 MBytes   196 Mbits/sec    0    781 KBytes       
    [  5]   8.00-9.00   sec  23.6 MBytes   198 Mbits/sec    0    875 KBytes       
    [  5]   9.00-10.00  sec  24.1 MBytes   202 Mbits/sec    0    875 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   227 MBytes   190 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   224 MBytes   187 Mbits/sec                  receiver
    
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
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">61.2</span> Mbits/sec | <span style="font-size: 1.5rem;">73.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 53725 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.00 MBytes  50.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.38 MBytes  78.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.75 MBytes  48.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  7.62 MBytes  63.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  73.0 MBytes  61.2 Mbits/sec   48             sender
    [  5]   0.00-10.00  sec  69.2 MBytes  58.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 59161 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.12 MBytes  68.1 Mbits/sec    0    379 KBytes       
    [  5]   1.00-2.00   sec  6.88 MBytes  57.7 Mbits/sec    0    566 KBytes       
    [  5]   2.00-3.00   sec  7.12 MBytes  59.8 Mbits/sec    0    601 KBytes       
    [  5]   3.00-4.00   sec  7.62 MBytes  64.0 Mbits/sec    0    667 KBytes       
    [  5]   4.00-5.00   sec  8.25 MBytes  69.2 Mbits/sec    0    676 KBytes       
    [  5]   5.00-6.00   sec  7.00 MBytes  58.7 Mbits/sec    0    757 KBytes       
    [  5]   6.00-7.00   sec  12.9 MBytes   108 Mbits/sec    0    798 KBytes       
    [  5]   7.00-8.00   sec  8.25 MBytes  69.2 Mbits/sec    0    798 KBytes       
    [  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0    839 KBytes       
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec    0    942 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  87.5 MBytes  73.4 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  84.0 MBytes  70.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    signal: -46 dBm
    tx bitrate: 174.0 MBit/s
    ```

#### Realtek 8814AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">165</span> Mbits/sec | <span style="font-size: 1.5rem;">24.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.106 port 39571 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  16.8 MBytes   140 Mbits/sec                  
    [  5]   1.00-2.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.8 MBytes   166 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.8 MBytes   166 Mbits/sec                  
    [  5]   5.00-6.00   sec  20.0 MBytes   168 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   7.00-8.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.8 MBytes   166 Mbits/sec                  
    [  5]   9.00-10.00  sec  19.4 MBytes   163 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   196 MBytes   165 Mbits/sec  105             sender
    [  5]   0.00-10.00  sec   194 MBytes   162 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.106 port 41803 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.62 MBytes  30.4 Mbits/sec    0    175 KBytes       
    [  5]   1.00-2.00   sec  2.88 MBytes  24.1 Mbits/sec    0    301 KBytes       
    [  5]   2.00-3.00   sec  3.25 MBytes  27.3 Mbits/sec    0    321 KBytes       
    [  5]   3.00-4.00   sec  2.75 MBytes  23.1 Mbits/sec    0    321 KBytes       
    [  5]   4.00-5.00   sec  2.12 MBytes  17.8 Mbits/sec    0    321 KBytes       
    [  5]   5.00-6.00   sec  2.62 MBytes  22.0 Mbits/sec    0    321 KBytes       
    [  5]   6.00-7.00   sec  3.25 MBytes  27.2 Mbits/sec    0    321 KBytes       
    [  5]   7.00-8.00   sec  2.62 MBytes  22.0 Mbits/sec    0    321 KBytes       
    [  5]   8.00-9.00   sec  2.75 MBytes  23.1 Mbits/sec    0    321 KBytes       
    [  5]   9.00-10.00  sec  3.00 MBytes  25.2 Mbits/sec    0    465 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  28.9 MBytes  24.2 Mbits/sec    0             sender
    [  5]   0.00-10.10  sec  27.1 MBytes  22.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -35 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8822CE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8822CE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.21-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">518</span> Mbits/sec | <span style="font-size: 1.5rem;">548</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 59667 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  74.0 MBytes   621 Mbits/sec                  
    [  5]   1.00-2.00   sec  64.0 MBytes   537 Mbits/sec                  
    [  5]   2.00-3.00   sec  60.3 MBytes   506 Mbits/sec                  
    [  5]   3.00-4.00   sec  57.8 MBytes   485 Mbits/sec                  
    [  5]   4.00-5.00   sec  60.0 MBytes   504 Mbits/sec                  
    [  5]   5.00-6.00   sec  62.4 MBytes   524 Mbits/sec                  
    [  5]   6.00-7.00   sec  60.9 MBytes   511 Mbits/sec                  
    [  5]   7.00-8.00   sec  57.6 MBytes   483 Mbits/sec                  
    [  5]   8.00-9.00   sec  58.4 MBytes   490 Mbits/sec                  
    [  5]   9.00-10.00  sec  58.8 MBytes   493 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   618 MBytes   518 Mbits/sec  1229             sender
    [  5]   0.00-10.00  sec   614 MBytes   515 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 54643 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  77.6 MBytes   650 Mbits/sec    0   6.43 MBytes       
    [  5]   1.00-2.00   sec  72.5 MBytes   609 Mbits/sec  838    875 KBytes       
    [  5]   2.00-3.00   sec  57.5 MBytes   482 Mbits/sec   11    583 KBytes       
    [  5]   3.00-4.00   sec  53.8 MBytes   451 Mbits/sec    2    445 KBytes       
    [  5]   4.00-5.00   sec  58.8 MBytes   492 Mbits/sec    0    607 KBytes       
    [  5]   5.00-6.00   sec  63.8 MBytes   535 Mbits/sec    0    742 KBytes       
    [  5]   6.00-7.00   sec  65.0 MBytes   545 Mbits/sec    0    861 KBytes       
    [  5]   7.00-8.00   sec  68.8 MBytes   575 Mbits/sec    0    969 KBytes       
    [  5]   8.00-9.00   sec  72.5 MBytes   610 Mbits/sec    0   1.05 MBytes       
    [  5]   9.00-10.00  sec  63.8 MBytes   535 Mbits/sec   18    643 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   654 MBytes   548 Mbits/sec  869             sender
    [  5]   0.00-10.01  sec   651 MBytes   546 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 132732 bytes (484 packets)
    TX: 62222 bytes (220 packets)
    signal: -32 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">122</span> Mbits/sec | <span style="font-size: 1.5rem;">147</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.117 port 43037 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.8 MBytes   115 Mbits/sec                  
    [  5]   1.00-2.00   sec  14.5 MBytes   122 Mbits/sec                  
    [  5]   2.00-3.00   sec  14.5 MBytes   122 Mbits/sec                  
    [  5]   3.00-4.00   sec  14.4 MBytes   121 Mbits/sec                  
    [  5]   4.00-5.00   sec  14.2 MBytes   120 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.1 MBytes   118 Mbits/sec                  
    [  5]   6.00-7.00   sec  14.2 MBytes   120 Mbits/sec                  
    [  5]   7.00-8.00   sec  14.1 MBytes   118 Mbits/sec                  
    [  5]   8.00-9.00   sec  14.4 MBytes   121 Mbits/sec                  
    [  5]   9.00-10.00  sec  14.5 MBytes   122 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   146 MBytes   122 Mbits/sec  149             sender
    [  5]   0.00-10.00  sec   143 MBytes   120 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.117 port 33229 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.4 MBytes   162 Mbits/sec    0    498 KBytes       
    [  5]   1.00-2.00   sec  17.8 MBytes   149 Mbits/sec    0    604 KBytes       
    [  5]   2.00-3.00   sec  16.4 MBytes   137 Mbits/sec    0    740 KBytes       
    [  5]   3.00-4.00   sec  18.2 MBytes   153 Mbits/sec    0    885 KBytes       
    [  5]   4.00-5.00   sec  17.5 MBytes   147 Mbits/sec    0    942 KBytes       
    [  5]   5.00-6.00   sec  16.8 MBytes   141 Mbits/sec    0    942 KBytes       
    [  5]   6.00-7.00   sec  18.0 MBytes   151 Mbits/sec    0    998 KBytes       
    [  5]   7.00-8.00   sec  17.1 MBytes   144 Mbits/sec    0    998 KBytes       
    [  5]   8.00-9.00   sec  17.4 MBytes   146 Mbits/sec    0    998 KBytes       
    [  5]   9.00-10.00  sec  17.1 MBytes   144 Mbits/sec    0   1.09 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   176 MBytes   147 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   173 MBytes   145 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 44963 bytes (146 packets)
    TX: 42671 bytes (198 packets)
    signal: -39 dBm
    rx bitrate: 1080.6 MBit/s 80MHz HE-MCS 10 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">196</span> Mbits/sec | <span style="font-size: 1.5rem;">152</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 55743 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   1.00-2.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   3.00-4.00   sec  23.5 MBytes   197 Mbits/sec                  
    [  5]   4.00-5.00   sec  23.1 MBytes   194 Mbits/sec                  
    [  5]   5.00-6.00   sec  23.4 MBytes   196 Mbits/sec                  
    [  5]   6.00-7.00   sec  23.5 MBytes   197 Mbits/sec                  
    [  5]   7.00-8.00   sec  23.9 MBytes   200 Mbits/sec                  
    [  5]   8.00-9.00   sec  21.0 MBytes   176 Mbits/sec                  
    [  5]   9.00-10.00  sec  23.0 MBytes   193 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   234 MBytes   196 Mbits/sec  104             sender
    [  5]   0.00-10.00  sec   231 MBytes   194 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 49255 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  21.0 MBytes   176 Mbits/sec    0   3.24 MBytes       
    [  5]   1.00-2.00   sec  16.4 MBytes   137 Mbits/sec    0   3.62 MBytes       
    [  5]   2.00-3.00   sec  18.9 MBytes   158 Mbits/sec    0   3.62 MBytes       
    [  5]   3.00-4.00   sec  19.2 MBytes   161 Mbits/sec    0   3.62 MBytes       
    [  5]   4.00-5.00   sec  15.2 MBytes   128 Mbits/sec    0   3.62 MBytes       
    [  5]   5.00-6.00   sec  17.9 MBytes   150 Mbits/sec    0   3.62 MBytes       
    [  5]   6.00-7.00   sec  18.2 MBytes   153 Mbits/sec    0   3.62 MBytes       
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec    0   3.62 MBytes       
    [  5]   8.00-9.00   sec  18.6 MBytes   156 Mbits/sec    0   4.77 MBytes       
    [  5]   9.00-10.00  sec  17.5 MBytes   147 Mbits/sec    0   4.77 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   181 MBytes   152 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec   179 MBytes   150 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 38256 bytes (168 packets)
    TX: 55539 bytes (196 packets)
    signal: -27 dBm
    rx bitrate: 286.7 MBit/s HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 58.5 MBit/s HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">93.6</span> Mbits/sec | <span style="font-size: 1.5rem;">69.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.114 port 52051 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.1 MBytes  84.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.0 MBytes  92.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   112 MBytes  93.6 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   109 MBytes  91.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.114 port 51519 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.00 MBytes  75.4 Mbits/sec    0    284 KBytes       
    [  5]   1.00-2.00   sec  8.50 MBytes  71.3 Mbits/sec    0    331 KBytes       
    [  5]   2.00-3.00   sec  7.75 MBytes  65.0 Mbits/sec    0    370 KBytes       
    [  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec    0    370 KBytes       
    [  5]   4.00-5.00   sec  8.12 MBytes  68.2 Mbits/sec    0    370 KBytes       
    [  5]   5.00-6.00   sec  7.62 MBytes  64.0 Mbits/sec    0    436 KBytes       
    [  5]   6.00-7.00   sec  8.12 MBytes  68.2 Mbits/sec    0    436 KBytes       
    [  5]   7.00-8.00   sec  8.50 MBytes  71.3 Mbits/sec    0    467 KBytes       
    [  5]   8.00-9.00   sec  8.12 MBytes  68.2 Mbits/sec    0    467 KBytes       
    [  5]   9.00-10.00  sec  8.62 MBytes  72.3 Mbits/sec    0    467 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  83.1 MBytes  69.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  80.4 MBytes  67.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 93484 bytes (354 packets)
    TX: 111260 bytes (291 packets)
    signal: -17 dBm
    rx bitrate: 180.0 MBit/s MCS 12 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### BCM 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">42.4</span> Mbits/sec | <span style="font-size: 1.5rem;">54.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 34923 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.99 MBytes  41.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.46 MBytes  45.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.49 MBytes  46.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.13 MBytes  43.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.60 MBytes  38.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.65 MBytes  39.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.73 MBytes  39.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.74 MBytes  39.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.61 MBytes  38.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.15 MBytes  43.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.53  sec  53.2 MBytes  42.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  49.6 MBytes  41.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 49449 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.54 MBytes  63.2 Mbits/sec    0    235 KBytes       
    [  5]   1.00-2.00   sec  5.47 MBytes  45.9 Mbits/sec    0    245 KBytes       
    [  5]   2.00-3.00   sec  5.72 MBytes  47.9 Mbits/sec    0    256 KBytes       
    [  5]   3.00-4.00   sec  6.21 MBytes  52.1 Mbits/sec    0    269 KBytes       
    [  5]   4.00-5.00   sec  6.28 MBytes  52.7 Mbits/sec    0    283 KBytes       
    [  5]   5.00-6.00   sec  5.72 MBytes  47.9 Mbits/sec    0    296 KBytes       
    [  5]   6.00-7.00   sec  8.51 MBytes  71.4 Mbits/sec    0    430 KBytes       
    [  5]   7.00-8.00   sec  6.09 MBytes  51.1 Mbits/sec    0    430 KBytes       
    [  5]   8.00-9.00   sec  6.21 MBytes  52.1 Mbits/sec    0    430 KBytes       
    [  5]   9.00-10.00  sec  6.96 MBytes  58.4 Mbits/sec    0    430 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  64.7 MBytes  54.3 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  62.2 MBytes  52.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 54204 bytes (167 packets)
    TX: 54794 bytes (232 packets)
    signal: -52 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">49.9</span> Mbits/sec | <span style="font-size: 1.5rem;">51.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.112 port 50329 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.38 MBytes  45.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.50 MBytes  46.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  59.5 MBytes  49.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  56.0 MBytes  47.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.112 port 45049 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.00 MBytes  58.7 Mbits/sec    0    345 KBytes       
    [  5]   1.00-2.00   sec  6.75 MBytes  56.6 Mbits/sec    0    624 KBytes       
    [  5]   2.00-3.00   sec  7.00 MBytes  58.7 Mbits/sec    0    822 KBytes       
    [  5]   3.00-4.00   sec  5.62 MBytes  47.2 Mbits/sec    0    957 KBytes       
    [  5]   4.00-5.00   sec  5.50 MBytes  46.2 Mbits/sec    0   1.05 MBytes       
    [  5]   5.00-6.00   sec  5.62 MBytes  47.2 Mbits/sec    0   1.12 MBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec    0   1.12 MBytes       
    [  5]   7.00-8.00   sec  5.62 MBytes  47.2 Mbits/sec    0   1.25 MBytes       
    [  5]   8.00-9.00   sec  5.62 MBytes  47.2 Mbits/sec    0   1.32 MBytes       
    [  5]   9.00-10.00  sec  7.00 MBytes  58.7 Mbits/sec    0   1.32 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  61.2 MBytes  51.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  58.1 MBytes  48.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 86097 bytes (345 packets)
    TX: 48386 bytes (206 packets)
    signal: -29 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">68.8</span> Mbits/sec | <span style="font-size: 1.5rem;">65.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.111 port 35437 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  7.75 MBytes  65.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.75 MBytes  73.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.88 MBytes  66.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  7.88 MBytes  66.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  8.62 MBytes  72.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  8.25 MBytes  69.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  7.75 MBytes  65.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  7.62 MBytes  64.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  82.1 MBytes  68.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  79.4 MBytes  66.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.111 port 43953 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.12 MBytes  68.1 Mbits/sec    0    276 KBytes       
    [  5]   1.00-2.00   sec  7.62 MBytes  63.9 Mbits/sec    0    341 KBytes       
    [  5]   2.00-3.00   sec  7.75 MBytes  65.0 Mbits/sec    0    362 KBytes       
    [  5]   3.00-4.00   sec  7.38 MBytes  61.9 Mbits/sec    0    404 KBytes       
    [  5]   4.00-5.00   sec  8.38 MBytes  70.2 Mbits/sec    0    404 KBytes       
    [  5]   5.00-6.00   sec  7.50 MBytes  62.9 Mbits/sec    0    404 KBytes       
    [  5]   6.00-7.00   sec  8.12 MBytes  68.2 Mbits/sec    0    404 KBytes       
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0    404 KBytes       
    [  5]   8.00-9.00   sec  8.25 MBytes  69.2 Mbits/sec    0    433 KBytes       
    [  5]   9.00-10.00  sec  7.00 MBytes  58.7 Mbits/sec    0    433 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  77.6 MBytes  65.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  75.4 MBytes  63.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 191138 bytes (569 packets)
    TX: 93186 bytes (526 packets)
    signal: -28 dBm
    rx bitrate: 240.0 MBit/s MCS 13 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">42.9</span> Mbits/sec | <span style="font-size: 1.5rem;">49.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.110 port 48427 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.00 MBytes  33.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.50 MBytes  37.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.00 MBytes  41.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.04  sec  51.4 MBytes  42.9 Mbits/sec   46             sender
    [  5]   0.00-10.00  sec  47.9 MBytes  40.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.110 port 34343 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.88 MBytes  57.6 Mbits/sec    0    327 KBytes       
    [  5]   1.00-2.00   sec  5.50 MBytes  46.1 Mbits/sec    0    389 KBytes       
    [  5]   2.00-3.00   sec  6.88 MBytes  57.7 Mbits/sec    0    468 KBytes       
    [  5]   3.00-4.00   sec  5.75 MBytes  48.2 Mbits/sec    0    468 KBytes       
    [  5]   4.00-5.00   sec  6.00 MBytes  50.3 Mbits/sec    0    489 KBytes       
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec    0    489 KBytes       
    [  5]   6.00-7.00   sec  6.38 MBytes  53.5 Mbits/sec    0    516 KBytes       
    [  5]   7.00-8.00   sec  5.50 MBytes  46.1 Mbits/sec    0    516 KBytes       
    [  5]   8.00-9.00   sec  5.38 MBytes  45.1 Mbits/sec    0    516 KBytes       
    [  5]   9.00-10.00  sec  5.38 MBytes  45.1 Mbits/sec    0    516 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  58.8 MBytes  49.3 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  56.8 MBytes  47.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 57467 bytes (166 packets)
    TX: 49194 bytes (209 packets)
    signal: -36 dBm
    rx bitrate: 52.0 MBit/s MCS 5
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">50.0</span> Mbits/sec | <span style="font-size: 1.5rem;">48.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 48345 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.98 MBytes  50.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.23 MBytes  27.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.23 MBytes  43.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.62 MBytes  47.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.30 MBytes  52.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.20 MBytes  52.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.21 MBytes  52.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.08 MBytes  51.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.12 MBytes  51.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.17 MBytes  51.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  59.8 MBytes  50.0 Mbits/sec   21             sender
    [  5]   0.00-10.00  sec  57.1 MBytes  47.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 50465 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.36 MBytes  53.4 Mbits/sec    0    363 KBytes       
    [  5]   1.00-2.00   sec  5.78 MBytes  48.5 Mbits/sec    0    462 KBytes       
    [  5]   2.00-3.00   sec  5.47 MBytes  45.9 Mbits/sec    0    491 KBytes       
    [  5]   3.00-4.00   sec  6.09 MBytes  51.1 Mbits/sec    0    516 KBytes       
    [  5]   4.00-5.00   sec  5.34 MBytes  44.8 Mbits/sec    0    543 KBytes       
    [  5]   5.00-6.00   sec  5.72 MBytes  48.0 Mbits/sec    0    543 KBytes       
    [  5]   6.00-7.00   sec  5.72 MBytes  48.0 Mbits/sec    0    543 KBytes       
    [  5]   7.00-8.00   sec  5.65 MBytes  47.4 Mbits/sec    0    543 KBytes       
    [  5]   8.00-9.00   sec  5.28 MBytes  44.3 Mbits/sec    0    543 KBytes       
    [  5]   9.00-10.00  sec  5.84 MBytes  49.0 Mbits/sec    0    543 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  57.3 MBytes  48.0 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  56.0 MBytes  46.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">2.82</span> Mbits/sec | <span style="font-size: 1.5rem;">19.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.109 port 41217 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   640 KBytes  5.24 Mbits/sec                  
    [  5]   1.00-2.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   2.00-3.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   3.00-4.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   4.00-5.00   sec   384 KBytes  3.15 Mbits/sec                  
    [  5]   5.00-6.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   6.00-7.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   7.00-8.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec                  
    [  5]   9.00-10.00  sec   256 KBytes  2.10 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.05  sec  3.38 MBytes  2.82 Mbits/sec   94             sender
    [  5]   0.00-10.00  sec  2.50 MBytes  2.10 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.109 port 43105 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  2.12 MBytes  17.8 Mbits/sec    0    124 KBytes       
    [  5]   1.00-2.00   sec  4.12 MBytes  34.6 Mbits/sec    0    272 KBytes       
    [  5]   2.00-3.00   sec  2.88 MBytes  24.1 Mbits/sec    0    355 KBytes       
    [  5]   3.00-4.00   sec  2.50 MBytes  21.0 Mbits/sec    0    444 KBytes       
    [  5]   4.00-5.00   sec  1.88 MBytes  15.7 Mbits/sec    0    495 KBytes       
    [  5]   5.00-6.00   sec  2.25 MBytes  18.9 Mbits/sec    0    585 KBytes       
    [  5]   6.00-7.00   sec  2.50 MBytes  21.0 Mbits/sec    0    655 KBytes       
    [  5]   7.00-8.00   sec  1.38 MBytes  11.5 Mbits/sec    0    723 KBytes       
    [  5]   8.00-9.00   sec  2.75 MBytes  23.1 Mbits/sec    0    823 KBytes       
    [  5]   9.00-10.00  sec  1.38 MBytes  11.5 Mbits/sec   30    776 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  23.8 MBytes  19.9 Mbits/sec   30             sender
    [  5]   0.00-10.01  sec  22.1 MBytes  18.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 77599 bytes (277 packets)
    TX: 50123 bytes (216 packets)
    signal: -36 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8821CU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">144</span> Mbits/sec | <span style="font-size: 1.5rem;">209</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.136 port 55049 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.4 MBytes   104 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.8 MBytes   115 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   3.00-4.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.5 MBytes   155 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   172 MBytes   144 Mbits/sec   22             sender
    [  5]   0.00-10.00  sec   170 MBytes   143 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.136 port 53579 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  27.6 MBytes   231 Mbits/sec    0    622 KBytes       
    [  5]   1.00-2.00   sec  23.8 MBytes   199 Mbits/sec    0    622 KBytes       
    [  5]   2.00-3.00   sec  24.8 MBytes   208 Mbits/sec    0    655 KBytes       
    [  5]   3.00-4.00   sec  25.1 MBytes   211 Mbits/sec    0    655 KBytes       
    [  5]   4.00-5.00   sec  25.4 MBytes   213 Mbits/sec    0    655 KBytes       
    [  5]   5.00-6.00   sec  23.8 MBytes   199 Mbits/sec    0    655 KBytes       
    [  5]   6.00-7.00   sec  26.1 MBytes   219 Mbits/sec    0    689 KBytes       
    [  5]   7.00-8.00   sec  23.4 MBytes   196 Mbits/sec    0    689 KBytes       
    [  5]   8.00-9.00   sec  24.6 MBytes   206 Mbits/sec    0    689 KBytes       
    [  5]   9.00-10.00  sec  25.0 MBytes   210 Mbits/sec    0    724 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   250 MBytes   209 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   247 MBytes   207 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 202170 bytes (378 packets)
    TX: 128718 bytes (516 packets)
    signal: -40 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">143</span> Mbits/sec | <span style="font-size: 1.5rem;">138</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 37745 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   5.00-6.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.0 MBytes   142 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   171 MBytes   143 Mbits/sec   30             sender
    [  5]   0.00-10.00  sec   168 MBytes   141 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 38025 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  17.5 MBytes   147 Mbits/sec    0    301 KBytes       
    [  5]   1.00-2.00   sec  16.0 MBytes   134 Mbits/sec    0    301 KBytes       
    [  5]   2.00-3.00   sec  16.2 MBytes   136 Mbits/sec    0    317 KBytes       
    [  5]   3.00-4.00   sec  17.2 MBytes   144 Mbits/sec    0    335 KBytes       
    [  5]   4.00-5.00   sec  16.2 MBytes   136 Mbits/sec    0    352 KBytes       
    [  5]   5.00-6.00   sec  16.5 MBytes   139 Mbits/sec    0    352 KBytes       
    [  5]   6.00-7.00   sec  16.5 MBytes   139 Mbits/sec    0    352 KBytes       
    [  5]   7.00-8.00   sec  16.2 MBytes   136 Mbits/sec    0    352 KBytes       
    [  5]   8.00-9.00   sec  16.4 MBytes   138 Mbits/sec    0    352 KBytes       
    [  5]   9.00-10.00  sec  16.3 MBytes   137 Mbits/sec    0    352 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   165 MBytes   138 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   164 MBytes   137 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 817591805 bytes (683054 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">18.2</span> Mbits/sec | <span style="font-size: 1.5rem;">12.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.154 port 54617 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.70 MBytes  14.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.84 MBytes  15.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.88 MBytes  15.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.89 MBytes  15.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.72 MBytes  14.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.83 MBytes  15.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.44 MBytes  20.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.45 MBytes  20.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  1.96 MBytes  16.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.43 MBytes  20.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.15  sec  22.0 MBytes  18.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  20.2 MBytes  16.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.154 port 44849 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.83 MBytes  15.4 Mbits/sec    0    107 KBytes       
    [  5]   1.00-2.00   sec  1.55 MBytes  13.0 Mbits/sec    0    119 KBytes       
    [  5]   2.00-3.00   sec  1.55 MBytes  13.0 Mbits/sec    0    130 KBytes       
    [  5]   3.00-4.00   sec  1.30 MBytes  10.9 Mbits/sec    3    107 KBytes       
    [  5]   4.00-5.00   sec  1.49 MBytes  12.5 Mbits/sec    1   86.3 KBytes       
    [  5]   5.00-6.00   sec  1.30 MBytes  10.9 Mbits/sec    1   73.5 KBytes       
    [  5]   6.00-7.00   sec  1.30 MBytes  10.9 Mbits/sec    3   65.0 KBytes       
    [  5]   7.00-8.00   sec  1.49 MBytes  12.5 Mbits/sec    0   80.6 KBytes       
    [  5]   8.00-9.00   sec  1.49 MBytes  12.5 Mbits/sec    0   91.9 KBytes       
    [  5]   9.00-10.00  sec  1.49 MBytes  12.5 Mbits/sec    4   70.7 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  14.8 MBytes  12.4 Mbits/sec   12             sender
    [  5]   0.00-10.04  sec  14.4 MBytes  12.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 51168 bytes (168 packets)
    TX: 63170 bytes (244 packets)
    signal: -27 dBm
    rx bitrate: 6.0 MBit/s
    tx bitrate: 39.0 MBit/s MCS 4
    
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
