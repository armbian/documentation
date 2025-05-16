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
**Test Date:** [2025-05-16 20:10 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15075940859)
### AC

#### BCM4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">57.7</span> Mbits/sec | <span style="font-size: 1.5rem;">59.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 46021 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.53 MBytes  54.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.57 MBytes  55.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.83 MBytes  57.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.62 MBytes  55.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.57 MBytes  55.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.64 MBytes  55.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.60 MBytes  55.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.65 MBytes  55.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.65 MBytes  55.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  68.9 MBytes  57.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  66.3 MBytes  55.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 35167 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.92 MBytes  66.4 Mbits/sec    0    421 KBytes       
    [  5]   1.00-2.00   sec  8.83 MBytes  74.1 Mbits/sec    0    734 KBytes       
    [  5]   2.00-3.00   sec  6.25 MBytes  52.4 Mbits/sec    0    895 KBytes       
    [  5]   3.00-4.00   sec  6.25 MBytes  52.4 Mbits/sec    0    947 KBytes       
    [  5]   4.00-5.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1022 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.13 MBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.34 MBytes       
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.53 MBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.53 MBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.63 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  70.5 MBytes  59.1 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  67.9 MBytes  56.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 157571 bytes (428 packets)
    TX: 95453 bytes (542 packets)
    signal: -25 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 65.0 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">116</span> Mbits/sec | <span style="font-size: 1.5rem;">105</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 34245 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.4 MBytes   113 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.3 MBytes   112 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.6 MBytes   114 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   138 MBytes   116 Mbits/sec   44             sender
    [  5]   0.00-10.00  sec   135 MBytes   113 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 55639 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.9 MBytes   108 Mbits/sec    0    447 KBytes       
    [  5]   1.00-2.00   sec  11.4 MBytes  95.4 Mbits/sec    0    494 KBytes       
    [  5]   2.00-3.00   sec  12.1 MBytes   102 Mbits/sec    0    525 KBytes       
    [  5]   3.00-4.00   sec  12.6 MBytes   105 Mbits/sec    0    577 KBytes       
    [  5]   4.00-5.00   sec  12.7 MBytes   106 Mbits/sec    0    608 KBytes       
    [  5]   5.00-6.00   sec  13.3 MBytes   112 Mbits/sec    0    672 KBytes       
    [  5]   6.00-7.00   sec  12.3 MBytes   103 Mbits/sec    0    672 KBytes       
    [  5]   7.00-8.00   sec  13.4 MBytes   112 Mbits/sec    0    672 KBytes       
    [  5]   8.00-9.00   sec  12.5 MBytes   105 Mbits/sec    0    672 KBytes       
    [  5]   9.00-10.00  sec  12.4 MBytes   104 Mbits/sec    0    707 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   125 MBytes   105 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   124 MBytes   104 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 111902 bytes (468 packets)
    TX: 53783 bytes (240 packets)
    signal: -38 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">83.3</span> Mbits/sec | <span style="font-size: 1.5rem;">76.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 39141 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  8.25 MBytes  69.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.12 MBytes  76.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  9.25 MBytes  77.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.1 MBytes  93.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  99.4 MBytes  83.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  98.6 MBytes  82.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 45003 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  10.8 MBytes  90.1 Mbits/sec    0    491 KBytes       
    [  5]   1.00-2.00   sec  9.75 MBytes  81.8 Mbits/sec    0    703 KBytes       
    [  5]   2.00-3.00   sec  8.50 MBytes  71.3 Mbits/sec    0    793 KBytes       
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec    0    830 KBytes       
    [  5]   4.00-5.00   sec  8.88 MBytes  74.5 Mbits/sec    3    588 KBytes       
    [  5]   5.00-6.00   sec  9.75 MBytes  81.8 Mbits/sec    0    617 KBytes       
    [  5]   6.00-7.00   sec  8.50 MBytes  71.3 Mbits/sec    0    717 KBytes       
    [  5]   7.00-8.00   sec  7.00 MBytes  58.7 Mbits/sec    0    717 KBytes       
    [  5]   8.00-9.00   sec  11.1 MBytes  93.3 Mbits/sec    0    717 KBytes       
    [  5]   9.00-10.00  sec  8.50 MBytes  71.3 Mbits/sec    0    717 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  91.1 MBytes  76.4 Mbits/sec    3             sender
    [  5]   0.00-10.03  sec  88.5 MBytes  74.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 197448 bytes (500 packets)
    TX: 105269 bytes (518 packets)
    signal: -43 dBm
    rx bitrate: 117.0 MBit/s MCS 14
    tx bitrate: 104.0 MBit/s MCS 13
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">191</span> Mbits/sec | <span style="font-size: 1.5rem;">200</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 56171 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  19.6 MBytes   164 Mbits/sec                  
    [  5]   1.00-2.00   sec  22.9 MBytes   192 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.1 MBytes   194 Mbits/sec                  
    [  5]   3.00-4.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   4.00-5.00   sec  22.5 MBytes   189 Mbits/sec                  
    [  5]   5.00-6.00   sec  22.9 MBytes   192 Mbits/sec                  
    [  5]   6.00-7.00   sec  22.6 MBytes   190 Mbits/sec                  
    [  5]   7.00-8.00   sec  22.2 MBytes   187 Mbits/sec                  
    [  5]   8.00-9.00   sec  22.1 MBytes   186 Mbits/sec                  
    [  5]   9.00-10.00  sec  22.6 MBytes   190 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   228 MBytes   191 Mbits/sec   22             sender
    [  5]   0.00-10.00  sec   224 MBytes   188 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 51407 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.4 MBytes   213 Mbits/sec    0    636 KBytes       
    [  5]   1.00-2.00   sec  24.4 MBytes   204 Mbits/sec    0    711 KBytes       
    [  5]   2.00-3.00   sec  23.6 MBytes   198 Mbits/sec    0    761 KBytes       
    [  5]   3.00-4.00   sec  22.5 MBytes   189 Mbits/sec    0    834 KBytes       
    [  5]   4.00-5.00   sec  23.8 MBytes   199 Mbits/sec    0    858 KBytes       
    [  5]   5.00-6.00   sec  23.8 MBytes   199 Mbits/sec    0    908 KBytes       
    [  5]   6.00-7.00   sec  23.8 MBytes   199 Mbits/sec    0    908 KBytes       
    [  5]   7.00-8.00   sec  23.6 MBytes   198 Mbits/sec    0    908 KBytes       
    [  5]   8.00-9.00   sec  23.9 MBytes   200 Mbits/sec    0    908 KBytes       
    [  5]   9.00-10.00  sec  23.8 MBytes   199 Mbits/sec    0    908 KBytes       
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
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">66.1</span> Mbits/sec | <span style="font-size: 1.5rem;">87.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 44809 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  7.38 MBytes  61.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  7.00 MBytes  58.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.88 MBytes  66.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  7.38 MBytes  61.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  7.50 MBytes  62.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  7.75 MBytes  65.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  7.25 MBytes  60.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.04  sec  79.1 MBytes  66.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  75.2 MBytes  63.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 60807 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  13.4 MBytes   112 Mbits/sec    0    523 KBytes       
    [  5]   1.00-2.00   sec  11.4 MBytes  95.4 Mbits/sec    0    656 KBytes       
    [  5]   2.00-3.00   sec  11.5 MBytes  96.5 Mbits/sec    0    748 KBytes       
    [  5]   3.00-4.00   sec  9.75 MBytes  81.8 Mbits/sec    0    788 KBytes       
    [  5]   4.00-5.00   sec  8.50 MBytes  71.3 Mbits/sec    0    788 KBytes       
    [  5]   5.00-6.00   sec  9.88 MBytes  82.8 Mbits/sec    0    788 KBytes       
    [  5]   6.00-7.00   sec  9.88 MBytes  82.8 Mbits/sec    0    788 KBytes       
    [  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0    788 KBytes       
    [  5]   8.00-9.00   sec  9.75 MBytes  81.8 Mbits/sec    0    788 KBytes       
    [  5]   9.00-10.00  sec  9.75 MBytes  81.7 Mbits/sec    0    788 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   104 MBytes  87.0 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   100 MBytes  84.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    signal: -41 dBm
    tx bitrate: 174.0 MBit/s
    ```

#### Realtek 8814AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">168</span> Mbits/sec | <span style="font-size: 1.5rem;">278</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.106 port 33833 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  20.0 MBytes   168 Mbits/sec                  
    [  5]   1.00-2.00   sec  20.1 MBytes   169 Mbits/sec                  
    [  5]   2.00-3.00   sec  20.1 MBytes   169 Mbits/sec                  
    [  5]   3.00-4.00   sec  20.2 MBytes   170 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.8 MBytes   166 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.1 MBytes   160 Mbits/sec                  
    [  5]   7.00-8.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   9.00-10.00  sec  20.1 MBytes   169 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   201 MBytes   168 Mbits/sec  144             sender
    [  5]   0.00-10.00  sec   197 MBytes   165 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.106 port 33815 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  35.0 MBytes   293 Mbits/sec    0    624 KBytes       
    [  5]   1.00-2.00   sec  33.8 MBytes   283 Mbits/sec    0    701 KBytes       
    [  5]   2.00-3.00   sec  32.6 MBytes   274 Mbits/sec    0    735 KBytes       
    [  5]   3.00-4.00   sec  32.0 MBytes   268 Mbits/sec    0    782 KBytes       
    [  5]   4.00-5.00   sec  34.0 MBytes   285 Mbits/sec    0    782 KBytes       
    [  5]   5.00-6.00   sec  32.5 MBytes   273 Mbits/sec    0    826 KBytes       
    [  5]   6.00-7.00   sec  32.4 MBytes   271 Mbits/sec    0    826 KBytes       
    [  5]   7.00-8.00   sec  33.6 MBytes   282 Mbits/sec    0    826 KBytes       
    [  5]   8.00-9.00   sec  32.4 MBytes   272 Mbits/sec    0    826 KBytes       
    [  5]   9.00-10.00  sec  32.8 MBytes   275 Mbits/sec    0    870 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   331 MBytes   278 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   329 MBytes   275 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -33 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8822CE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8822CE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.21-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">325</span> Mbits/sec | <span style="font-size: 1.5rem;">571</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 46473 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  51.7 MBytes   433 Mbits/sec                  
    [  5]   1.00-2.00   sec  35.5 MBytes   298 Mbits/sec                  
    [  5]   2.00-3.00   sec  36.9 MBytes   310 Mbits/sec                  
    [  5]   3.00-4.00   sec  37.2 MBytes   312 Mbits/sec                  
    [  5]   4.00-5.00   sec  37.4 MBytes   314 Mbits/sec                  
    [  5]   5.00-6.00   sec  36.0 MBytes   302 Mbits/sec                  
    [  5]   6.00-7.00   sec  37.0 MBytes   310 Mbits/sec                  
    [  5]   7.00-8.00   sec  38.2 MBytes   320 Mbits/sec                  
    [  5]   8.00-9.00   sec  38.6 MBytes   324 Mbits/sec                  
    [  5]   9.00-10.00  sec  35.8 MBytes   300 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   388 MBytes   325 Mbits/sec  772             sender
    [  5]   0.00-10.00  sec   384 MBytes   322 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 33355 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  77.1 MBytes   647 Mbits/sec   57   3.21 MBytes       
    [  5]   1.00-2.00   sec  78.8 MBytes   661 Mbits/sec   69   1.65 MBytes       
    [  5]   2.00-3.00   sec  75.0 MBytes   629 Mbits/sec   20    898 KBytes       
    [  5]   3.00-4.00   sec  60.0 MBytes   503 Mbits/sec   32    588 KBytes       
    [  5]   4.00-5.00   sec  63.8 MBytes   533 Mbits/sec    0    727 KBytes       
    [  5]   5.00-6.00   sec  67.5 MBytes   568 Mbits/sec    0    853 KBytes       
    [  5]   6.00-7.00   sec  65.0 MBytes   545 Mbits/sec   13    522 KBytes       
    [  5]   7.00-8.00   sec  60.0 MBytes   503 Mbits/sec    0    667 KBytes       
    [  5]   8.00-9.00   sec  66.2 MBytes   556 Mbits/sec    0    799 KBytes       
    [  5]   9.00-10.00  sec  67.5 MBytes   566 Mbits/sec    0    912 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   681 MBytes   571 Mbits/sec  191             sender
    [  5]   0.00-10.00  sec   679 MBytes   569 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 112422 bytes (387 packets)
    TX: 54574 bytes (206 packets)
    signal: -30 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">121</span> Mbits/sec | <span style="font-size: 1.5rem;">146</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.117 port 37607 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   1.00-2.00   sec  14.2 MBytes   120 Mbits/sec                  
    [  5]   2.00-3.00   sec  14.4 MBytes   121 Mbits/sec                  
    [  5]   3.00-4.00   sec  14.1 MBytes   118 Mbits/sec                  
    [  5]   4.00-5.00   sec  14.0 MBytes   117 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.1 MBytes   118 Mbits/sec                  
    [  5]   6.00-7.00   sec  14.2 MBytes   120 Mbits/sec                  
    [  5]   7.00-8.00   sec  14.2 MBytes   120 Mbits/sec                  
    [  5]   8.00-9.00   sec  14.4 MBytes   121 Mbits/sec                  
    [  5]   9.00-10.00  sec  14.4 MBytes   121 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   145 MBytes   121 Mbits/sec   63             sender
    [  5]   0.00-10.00  sec   142 MBytes   119 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.117 port 43393 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.5 MBytes   155 Mbits/sec    0    559 KBytes       
    [  5]   1.00-2.00   sec  17.1 MBytes   143 Mbits/sec    0    690 KBytes       
    [  5]   2.00-3.00   sec  17.0 MBytes   143 Mbits/sec    0    843 KBytes       
    [  5]   3.00-4.00   sec  18.0 MBytes   151 Mbits/sec    0    889 KBytes       
    [  5]   4.00-5.00   sec  17.1 MBytes   144 Mbits/sec    0   1.09 MBytes       
    [  5]   5.00-6.00   sec  17.9 MBytes   150 Mbits/sec    0   1.20 MBytes       
    [  5]   6.00-7.00   sec  16.5 MBytes   138 Mbits/sec    0   1.28 MBytes       
    [  5]   7.00-8.00   sec  18.1 MBytes   152 Mbits/sec    0   1.35 MBytes       
    [  5]   8.00-9.00   sec  16.9 MBytes   142 Mbits/sec    0   1.35 MBytes       
    [  5]   9.00-10.00  sec  17.2 MBytes   145 Mbits/sec    0   1.35 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   174 MBytes   146 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   172 MBytes   144 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 49360 bytes (187 packets)
    TX: 54023 bytes (231 packets)
    signal: -36 dBm
    rx bitrate: 286.7 MBit/s HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 286.7 MBit/s HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">796</span> Mbits/sec | <span style="font-size: 1.5rem;">631</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 45011 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  90.6 MBytes   760 Mbits/sec                  
    [  5]   1.00-2.00   sec   108 MBytes   910 Mbits/sec                  
    [  5]   2.00-3.00   sec   105 MBytes   880 Mbits/sec                  
    [  5]   3.00-4.00   sec  96.5 MBytes   810 Mbits/sec                  
    [  5]   4.00-5.00   sec  87.5 MBytes   734 Mbits/sec                  
    [  5]   5.00-6.00   sec  92.8 MBytes   778 Mbits/sec                  
    [  5]   6.00-7.00   sec  85.9 MBytes   721 Mbits/sec                  
    [  5]   7.00-8.00   sec  90.2 MBytes   757 Mbits/sec                  
    [  5]   8.00-9.00   sec  89.0 MBytes   747 Mbits/sec                  
    [  5]   9.00-10.00  sec  99.5 MBytes   834 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   949 MBytes   796 Mbits/sec  289             sender
    [  5]   0.00-10.00  sec   946 MBytes   793 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 42039 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  84.0 MBytes   704 Mbits/sec  944    725 KBytes       
    [  5]   1.00-2.00   sec  86.5 MBytes   726 Mbits/sec    0    881 KBytes       
    [  5]   2.00-3.00   sec  71.4 MBytes   599 Mbits/sec    9    584 KBytes       
    [  5]   3.00-4.00   sec  79.2 MBytes   665 Mbits/sec    0    757 KBytes       
    [  5]   4.00-5.00   sec  72.8 MBytes   610 Mbits/sec  192    530 KBytes       
    [  5]   5.00-6.00   sec  75.1 MBytes   630 Mbits/sec    0    706 KBytes       
    [  5]   6.00-7.00   sec  83.1 MBytes   697 Mbits/sec    0    861 KBytes       
    [  5]   7.00-8.00   sec  71.4 MBytes   599 Mbits/sec    1    583 KBytes       
    [  5]   8.00-9.00   sec  66.4 MBytes   557 Mbits/sec   84    400 KBytes       
    [  5]   9.00-10.00  sec  62.4 MBytes   522 Mbits/sec    6    584 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   752 MBytes   631 Mbits/sec  1236             sender
    [  5]   0.00-10.01  sec   750 MBytes   628 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 39473 bytes (166 packets)
    TX: 51518 bytes (183 packets)
    signal: -30 dBm
    rx bitrate: 2401.9 MBit/s 160MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">102</span> Mbits/sec | <span style="font-size: 1.5rem;">72.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.114 port 52293 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.2 MBytes   103 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   122 MBytes   102 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   120 MBytes   100 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.114 port 44983 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.00 MBytes  67.0 Mbits/sec    0    331 KBytes       
    [  5]   1.00-2.00   sec  9.50 MBytes  79.7 Mbits/sec    0    460 KBytes       
    [  5]   2.00-3.00   sec  8.25 MBytes  69.2 Mbits/sec    0    522 KBytes       
    [  5]   3.00-4.00   sec  8.88 MBytes  74.4 Mbits/sec    0    608 KBytes       
    [  5]   4.00-5.00   sec  8.88 MBytes  74.4 Mbits/sec    0    636 KBytes       
    [  5]   5.00-6.00   sec  9.00 MBytes  75.5 Mbits/sec    0    672 KBytes       
    [  5]   6.00-7.00   sec  8.38 MBytes  70.2 Mbits/sec    0    672 KBytes       
    [  5]   7.00-8.00   sec  8.38 MBytes  70.2 Mbits/sec    0    672 KBytes       
    [  5]   8.00-9.00   sec  8.25 MBytes  69.2 Mbits/sec    0    710 KBytes       
    [  5]   9.00-10.00  sec  8.62 MBytes  72.3 Mbits/sec    0    710 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  86.1 MBytes  72.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  82.9 MBytes  69.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 89010 bytes (363 packets)
    TX: 64572 bytes (242 packets)
    signal: -17 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Atheros AR9271

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">57.6</span> Mbits/sec | <span style="font-size: 1.5rem;">52.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.113 port 45659 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.38 MBytes  53.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.75 MBytes  56.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.75 MBytes  56.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  68.9 MBytes  57.6 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  65.6 MBytes  55.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.113 port 43023 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.12 MBytes  59.7 Mbits/sec    0    247 KBytes       
    [  5]   1.00-2.00   sec  6.00 MBytes  50.3 Mbits/sec    0    262 KBytes       
    [  5]   2.00-3.00   sec  6.12 MBytes  51.4 Mbits/sec    0    262 KBytes       
    [  5]   3.00-4.00   sec  6.12 MBytes  51.4 Mbits/sec    0    262 KBytes       
    [  5]   4.00-5.00   sec  5.62 MBytes  47.2 Mbits/sec    0    262 KBytes       
    [  5]   5.00-6.00   sec  6.12 MBytes  51.4 Mbits/sec    0    262 KBytes       
    [  5]   6.00-7.00   sec  6.12 MBytes  51.4 Mbits/sec    0    262 KBytes       
    [  5]   7.00-8.00   sec  6.75 MBytes  56.6 Mbits/sec    0    407 KBytes       
    [  5]   8.00-9.00   sec  6.50 MBytes  54.5 Mbits/sec    0    407 KBytes       
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec    0    407 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  62.1 MBytes  52.1 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  60.4 MBytes  50.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 101758 bytes (422 packets)
    TX: 58331 bytes (222 packets)
    signal: -35 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### BCM 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">54.4</span> Mbits/sec | <span style="font-size: 1.5rem;">54.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 45763 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.30 MBytes  52.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.37 MBytes  45.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.66 MBytes  64.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.26 MBytes  44.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.58 MBytes  46.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  7.48 MBytes  62.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  7.53 MBytes  63.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.73 MBytes  48.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.36 MBytes  53.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.89 MBytes  49.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  65.0 MBytes  54.4 Mbits/sec    3             sender
    [  5]   0.00-10.00  sec  63.2 MBytes  53.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 34723 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.57 MBytes  55.1 Mbits/sec    0    214 KBytes       
    [  5]   1.00-2.00   sec  6.65 MBytes  55.8 Mbits/sec    0    280 KBytes       
    [  5]   2.00-3.00   sec  7.15 MBytes  59.9 Mbits/sec    0    345 KBytes       
    [  5]   3.00-4.00   sec  6.71 MBytes  56.3 Mbits/sec    0    365 KBytes       
    [  5]   4.00-5.00   sec  5.97 MBytes  50.0 Mbits/sec    0    365 KBytes       
    [  5]   5.00-6.00   sec  6.84 MBytes  57.4 Mbits/sec    0    365 KBytes       
    [  5]   6.00-7.00   sec  6.09 MBytes  51.1 Mbits/sec    0    365 KBytes       
    [  5]   7.00-8.00   sec  6.21 MBytes  52.1 Mbits/sec    0    365 KBytes       
    [  5]   8.00-9.00   sec  6.84 MBytes  57.3 Mbits/sec    0    365 KBytes       
    [  5]   9.00-10.00  sec  6.03 MBytes  50.6 Mbits/sec    0    365 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  65.0 MBytes  54.6 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  63.6 MBytes  53.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 46196 bytes (124 packets)
    TX: 50552 bytes (228 packets)
    signal: -55 dBm
    rx bitrate: 390.0 MBit/s
    tx bitrate: 390.0 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">52.3</span> Mbits/sec | <span style="font-size: 1.5rem;">47.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.112 port 40459 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.62 MBytes  47.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.12 MBytes  51.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.12 MBytes  51.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.25 MBytes  52.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.00 MBytes  50.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  62.5 MBytes  52.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  59.4 MBytes  49.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.112 port 41917 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.88 MBytes  32.5 Mbits/sec    0    212 KBytes       
    [  5]   1.00-2.00   sec  5.12 MBytes  43.0 Mbits/sec    0    416 KBytes       
    [  5]   2.00-3.00   sec  6.75 MBytes  56.6 Mbits/sec    0    659 KBytes       
    [  5]   3.00-4.00   sec  5.50 MBytes  46.1 Mbits/sec    0    881 KBytes       
    [  5]   4.00-5.00   sec  6.38 MBytes  53.5 Mbits/sec    0    901 KBytes       
    [  5]   5.00-6.00   sec  4.38 MBytes  36.7 Mbits/sec    0    959 KBytes       
    [  5]   6.00-7.00   sec  6.88 MBytes  57.7 Mbits/sec    0   1.10 MBytes       
    [  5]   7.00-8.00   sec  5.50 MBytes  46.2 Mbits/sec    1    580 KBytes       
    [  5]   8.00-9.00   sec  5.50 MBytes  46.1 Mbits/sec    0    926 KBytes       
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec    0   1012 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  56.5 MBytes  47.4 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec  54.0 MBytes  45.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 101344 bytes (447 packets)
    TX: 56715 bytes (219 packets)
    signal: -31 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">90.8</span> Mbits/sec | <span style="font-size: 1.5rem;">71.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.111 port 46151 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.4 MBytes  86.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.5 MBytes  88.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.6 MBytes  88.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.4 MBytes  87.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.4 MBytes  86.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.6 MBytes  89.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  10.8 MBytes  90.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   108 MBytes  90.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   105 MBytes  88.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.111 port 40299 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.00 MBytes  75.4 Mbits/sec    0    239 KBytes       
    [  5]   1.00-2.00   sec  8.75 MBytes  73.4 Mbits/sec    0    324 KBytes       
    [  5]   2.00-3.00   sec  8.88 MBytes  74.5 Mbits/sec    0    380 KBytes       
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec    0    440 KBytes       
    [  5]   4.00-5.00   sec  7.88 MBytes  66.1 Mbits/sec    0    461 KBytes       
    [  5]   5.00-6.00   sec  9.12 MBytes  76.5 Mbits/sec    0    513 KBytes       
    [  5]   6.00-7.00   sec  8.25 MBytes  69.2 Mbits/sec    0    513 KBytes       
    [  5]   7.00-8.00   sec  8.38 MBytes  70.3 Mbits/sec    0    513 KBytes       
    [  5]   8.00-9.00   sec  8.38 MBytes  70.3 Mbits/sec    0    513 KBytes       
    [  5]   9.00-10.00  sec  7.75 MBytes  65.0 Mbits/sec    0    513 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  84.8 MBytes  71.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  82.2 MBytes  69.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 221110 bytes (681 packets)
    TX: 115735 bytes (594 packets)
    signal: -22 dBm
    rx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">28.1</span> Mbits/sec | <span style="font-size: 1.5rem;">30.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.110 port 49295 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.62 MBytes  30.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.12 MBytes  26.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  1.62 MBytes  13.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.00 MBytes  16.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.49  sec  35.1 MBytes  28.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  31.8 MBytes  26.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.110 port 48303 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.12 MBytes  42.9 Mbits/sec    0    272 KBytes       
    [  5]   1.00-2.00   sec  4.12 MBytes  34.6 Mbits/sec    0    298 KBytes       
    [  5]   2.00-3.00   sec  3.75 MBytes  31.5 Mbits/sec    0    314 KBytes       
    [  5]   3.00-4.00   sec  4.62 MBytes  38.8 Mbits/sec    0    314 KBytes       
    [  5]   4.00-5.00   sec  4.50 MBytes  37.7 Mbits/sec    0    332 KBytes       
    [  5]   5.00-6.00   sec  3.62 MBytes  30.4 Mbits/sec    0    332 KBytes       
    [  5]   6.00-7.00   sec  2.00 MBytes  16.8 Mbits/sec    0    332 KBytes       
    [  5]   7.00-8.00   sec  2.75 MBytes  23.1 Mbits/sec    0    332 KBytes       
    [  5]   8.00-9.00   sec  2.75 MBytes  23.1 Mbits/sec    0    332 KBytes       
    [  5]   9.00-10.00  sec  3.62 MBytes  30.4 Mbits/sec    0    332 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  36.9 MBytes  30.9 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  35.1 MBytes  29.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 199682 bytes (507 packets)
    TX: 130752 bytes (730 packets)
    signal: -34 dBm
    rx bitrate: 58.5 MBit/s MCS 6
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">47.0</span> Mbits/sec | <span style="font-size: 1.5rem;">30.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 46857 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.81 MBytes  48.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.91 MBytes  41.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.47 MBytes  29.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.03 MBytes  25.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.16 MBytes  51.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.63 MBytes  38.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.23 MBytes  52.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.10 MBytes  51.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.15 MBytes  51.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  56.0 MBytes  47.0 Mbits/sec   26             sender
    [  5]   0.00-10.00  sec  52.7 MBytes  44.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 37261 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.33 MBytes  44.7 Mbits/sec    0    276 KBytes       
    [  5]   1.00-2.00   sec  5.28 MBytes  44.3 Mbits/sec    0    508 KBytes       
    [  5]   2.00-3.00   sec  3.60 MBytes  30.2 Mbits/sec    0    673 KBytes       
    [  5]   3.00-4.00   sec  4.10 MBytes  34.4 Mbits/sec    0    735 KBytes       
    [  5]   4.00-5.00   sec  3.48 MBytes  29.2 Mbits/sec    0    851 KBytes       
    [  5]   5.00-6.00   sec  3.29 MBytes  27.6 Mbits/sec    0    949 KBytes       
    [  5]   6.00-7.00   sec  3.29 MBytes  27.6 Mbits/sec    0   1015 KBytes       
    [  5]   7.00-8.00   sec  2.37 MBytes  19.9 Mbits/sec    0   1.10 MBytes       
    [  5]   8.00-9.00   sec  2.38 MBytes  19.9 Mbits/sec    0   1.23 MBytes       
    [  5]   9.00-10.00  sec  3.75 MBytes  31.5 Mbits/sec    0   1.36 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  36.9 MBytes  30.9 Mbits/sec    0             sender
    [  5]   0.00-10.07  sec  34.5 MBytes  28.7 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">3.56</span> Mbits/sec | <span style="font-size: 1.5rem;">20.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.109 port 52765 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.12 MBytes  9.43 Mbits/sec                  
    [  5]   1.00-2.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   2.00-3.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   3.00-4.00   sec   384 KBytes  3.15 Mbits/sec                  
    [  5]   4.00-5.00   sec   384 KBytes  3.15 Mbits/sec                  
    [  5]   5.00-6.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   6.00-7.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   7.00-8.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   8.00-9.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   9.00-10.00  sec   128 KBytes  1.05 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  4.25 MBytes  3.56 Mbits/sec  101             sender
    [  5]   0.00-10.00  sec  3.12 MBytes  2.62 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.109 port 44381 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.12 MBytes  26.2 Mbits/sec    0    156 KBytes       
    [  5]   1.00-2.00   sec  3.38 MBytes  28.3 Mbits/sec   12    168 KBytes       
    [  5]   2.00-3.00   sec  1.75 MBytes  14.7 Mbits/sec    0    192 KBytes       
    [  5]   3.00-4.00   sec  1.75 MBytes  14.7 Mbits/sec    0    206 KBytes       
    [  5]   4.00-5.00   sec  1.75 MBytes  14.7 Mbits/sec    0    214 KBytes       
    [  5]   5.00-6.00   sec  1.75 MBytes  14.7 Mbits/sec    0    214 KBytes       
    [  5]   6.00-7.00   sec  1.75 MBytes  14.7 Mbits/sec    0    214 KBytes       
    [  5]   7.00-8.00   sec  1.75 MBytes  14.7 Mbits/sec    0    215 KBytes       
    [  5]   8.00-9.00   sec  3.12 MBytes  26.2 Mbits/sec    0    225 KBytes       
    [  5]   9.00-10.00  sec  4.62 MBytes  38.8 Mbits/sec    0    242 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  24.8 MBytes  20.8 Mbits/sec   12             sender
    [  5]   0.00-10.03  sec  23.8 MBytes  19.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 79580 bytes (327 packets)
    TX: 59674 bytes (221 packets)
    signal: 0 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8821CU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">132</span> Mbits/sec | <span style="font-size: 1.5rem;">210</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.136 port 36283 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   1.00-2.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   2.00-3.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   3.00-4.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   4.00-5.00   sec  15.6 MBytes   131 Mbits/sec                  
    [  5]   5.00-6.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   6.00-7.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   7.00-8.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   8.00-9.00   sec  15.6 MBytes   131 Mbits/sec                  
    [  5]   9.00-10.00  sec  15.8 MBytes   132 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   157 MBytes   132 Mbits/sec   45             sender
    [  5]   0.00-10.00  sec   157 MBytes   131 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.136 port 48063 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  27.2 MBytes   228 Mbits/sec    0    563 KBytes       
    [  5]   1.00-2.00   sec  25.0 MBytes   210 Mbits/sec    0    621 KBytes       
    [  5]   2.00-3.00   sec  25.1 MBytes   211 Mbits/sec    0    621 KBytes       
    [  5]   3.00-4.00   sec  23.6 MBytes   198 Mbits/sec    0    652 KBytes       
    [  5]   4.00-5.00   sec  25.0 MBytes   210 Mbits/sec    0    652 KBytes       
    [  5]   5.00-6.00   sec  25.8 MBytes   216 Mbits/sec    0    684 KBytes       
    [  5]   6.00-7.00   sec  24.8 MBytes   208 Mbits/sec    0    684 KBytes       
    [  5]   7.00-8.00   sec  24.6 MBytes   207 Mbits/sec    0    684 KBytes       
    [  5]   8.00-9.00   sec  24.6 MBytes   207 Mbits/sec    0    684 KBytes       
    [  5]   9.00-10.00  sec  24.6 MBytes   207 Mbits/sec    0    721 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   250 MBytes   210 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   247 MBytes   207 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 209539 bytes (396 packets)
    TX: 100889 bytes (477 packets)
    signal: -35 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">54.2</span> Mbits/sec | <span style="font-size: 1.5rem;">60.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 33577 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.07 MBytes  50.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.12 MBytes  51.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.03 MBytes  50.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.17 MBytes  51.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.19 MBytes  51.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.01 MBytes  50.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.13 MBytes  51.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.16 MBytes  51.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.33 MBytes  53.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.18 MBytes  51.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  64.6 MBytes  54.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  61.4 MBytes  51.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 35237 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.56 MBytes  71.8 Mbits/sec    0    358 KBytes       
    [  5]   1.00-2.00   sec  6.90 MBytes  57.9 Mbits/sec    0    560 KBytes       
    [  5]   2.00-3.00   sec  8.67 MBytes  72.7 Mbits/sec    0    689 KBytes       
    [  5]   3.00-4.00   sec  6.25 MBytes  52.4 Mbits/sec    0    800 KBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    0    871 KBytes       
    [  5]   5.00-6.00   sec  7.50 MBytes  62.9 Mbits/sec    0    916 KBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0    967 KBytes       
    [  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.05 MBytes       
    [  5]   8.00-9.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.05 MBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.05 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  71.6 MBytes  60.1 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  69.0 MBytes  57.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 48601 bytes (207 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">19.0</span> Mbits/sec | <span style="font-size: 1.5rem;">13.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.138 port 58077 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.81 MBytes  15.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.29 MBytes  10.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.59 MBytes  13.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.96 MBytes  16.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.23 MBytes  18.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.03 MBytes  17.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.39 MBytes  20.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.46 MBytes  20.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.44 MBytes  20.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.99 MBytes  16.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.11  sec  22.9 MBytes  19.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  20.2 MBytes  16.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.138 port 53655 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.94 MBytes  16.3 Mbits/sec    0    106 KBytes       
    [  5]   1.00-2.00   sec  1.55 MBytes  13.0 Mbits/sec    0    129 KBytes       
    [  5]   2.00-3.00   sec  1.49 MBytes  12.5 Mbits/sec    0    134 KBytes       
    [  5]   3.00-4.00   sec  1.68 MBytes  14.1 Mbits/sec    0    140 KBytes       
    [  5]   4.00-5.00   sec  1.49 MBytes  12.5 Mbits/sec    0    140 KBytes       
    [  5]   5.00-6.00   sec  1.49 MBytes  12.5 Mbits/sec    0    146 KBytes       
    [  5]   6.00-7.00   sec  1.68 MBytes  14.1 Mbits/sec    0    146 KBytes       
    [  5]   7.00-8.00   sec  1.68 MBytes  14.1 Mbits/sec    0    194 KBytes       
    [  5]   8.00-9.00   sec  1.49 MBytes  12.5 Mbits/sec    0    194 KBytes       
    [  5]   9.00-10.00  sec  1.24 MBytes  10.4 Mbits/sec    4    140 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  15.7 MBytes  13.2 Mbits/sec    4             sender
    [  5]   0.00-10.04  sec  15.2 MBytes  12.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 60041 bytes (191 packets)
    TX: 66671 bytes (282 packets)
    signal: -30 dBm
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
