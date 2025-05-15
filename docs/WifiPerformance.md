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
**Test Date:** [2025-05-15 12:48 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15044497720)
### AC

#### BCM4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">8.96</span> Mbits/sec | <span style="font-size: 1.5rem;">13.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 53671 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.22 MBytes  27.0 Mbits/sec                  
    [  5]   1.00-2.00   sec   667 KBytes  5.47 Mbits/sec                  
    [  5]   2.00-3.00   sec   106 KBytes   869 Kbits/sec                  
    [  5]   3.00-4.00   sec   126 KBytes  1.03 Mbits/sec                  
    [  5]   4.00-5.00   sec   119 KBytes   973 Kbits/sec                  
    [  5]   5.00-6.00   sec   188 KBytes  1.54 Mbits/sec                  
    [  5]   6.00-7.00   sec   354 KBytes  2.90 Mbits/sec                  
    [  5]   7.00-8.00   sec   233 KBytes  1.91 Mbits/sec                  
    [  5]   8.00-9.00   sec   390 KBytes  3.20 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.88 MBytes  15.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.06  sec  10.8 MBytes  8.96 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  7.23 MBytes  6.07 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 52871 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.48 MBytes  12.4 Mbits/sec   42   24.0 KBytes       
    [  5]   1.00-2.00   sec   382 KBytes  3.13 Mbits/sec    9   7.07 KBytes       
    [  5]   2.00-3.00   sec   891 KBytes  7.30 Mbits/sec    0   36.8 KBytes       
    [  5]   3.00-4.00   sec  1.12 MBytes  9.38 Mbits/sec    0   55.1 KBytes       
    [  5]   4.00-5.00   sec   700 KBytes  5.73 Mbits/sec    9   32.5 KBytes       
    [  5]   5.00-6.00   sec  1.62 MBytes  13.6 Mbits/sec    3   36.8 KBytes       
    [  5]   6.00-7.00   sec  4.60 MBytes  38.6 Mbits/sec    1   83.4 KBytes       
    [  5]   7.00-8.00   sec  2.86 MBytes  24.0 Mbits/sec   52   41.0 KBytes       
    [  5]   8.00-9.00   sec  1.12 MBytes  9.38 Mbits/sec   24   15.6 KBytes       
    [  5]   9.00-10.00  sec  1.86 MBytes  15.6 Mbits/sec   12   32.5 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  16.6 MBytes  13.9 Mbits/sec  152             sender
    [  5]   0.00-10.01  sec  16.2 MBytes  13.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 61272 bytes (182 packets)
    TX: 78749 bytes (298 packets)
    signal: -40 dBm
    rx bitrate: 260.0 MBit/s
    tx bitrate: 65.0 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">117</span> Mbits/sec | <span style="font-size: 1.5rem;">107</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 60537 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.3 MBytes   111 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.9 MBytes   116 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.4 MBytes   113 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.3 MBytes   112 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.8 MBytes   116 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   140 MBytes   117 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   136 MBytes   114 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 54659 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.9 MBytes   108 Mbits/sec    0    434 KBytes       
    [  5]   1.00-2.00   sec  12.5 MBytes   105 Mbits/sec    0    557 KBytes       
    [  5]   2.00-3.00   sec  12.4 MBytes   104 Mbits/sec    0    622 KBytes       
    [  5]   3.00-4.00   sec  12.3 MBytes   103 Mbits/sec    0    658 KBytes       
    [  5]   4.00-5.00   sec  13.7 MBytes   115 Mbits/sec    0    805 KBytes       
    [  5]   5.00-6.00   sec  12.7 MBytes   107 Mbits/sec    0    805 KBytes       
    [  5]   6.00-7.00   sec  12.9 MBytes   108 Mbits/sec    0    805 KBytes       
    [  5]   7.00-8.00   sec  12.7 MBytes   107 Mbits/sec    0    854 KBytes       
    [  5]   8.00-9.00   sec  13.3 MBytes   112 Mbits/sec    0    854 KBytes       
    [  5]   9.00-10.00  sec  12.7 MBytes   107 Mbits/sec    0    854 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   128 MBytes   107 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   126 MBytes   105 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 98380 bytes (388 packets)
    TX: 51815 bytes (223 packets)
    signal: -23 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">93.8</span> Mbits/sec | <span style="font-size: 1.5rem;">61.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 57013 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.50 MBytes  79.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.5 MBytes  96.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   112 MBytes  93.8 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   111 MBytes  93.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 41899 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.25 MBytes  69.1 Mbits/sec    0    358 KBytes       
    [  5]   1.00-2.00   sec  7.50 MBytes  62.9 Mbits/sec    0    626 KBytes       
    [  5]   2.00-3.00   sec  6.75 MBytes  56.6 Mbits/sec    0    735 KBytes       
    [  5]   3.00-4.00   sec  7.12 MBytes  59.8 Mbits/sec    0    858 KBytes       
    [  5]   4.00-5.00   sec  7.00 MBytes  58.7 Mbits/sec    0    858 KBytes       
    [  5]   5.00-6.00   sec  7.25 MBytes  60.8 Mbits/sec    0    858 KBytes       
    [  5]   6.00-7.00   sec  7.00 MBytes  58.7 Mbits/sec    0    858 KBytes       
    [  5]   7.00-8.00   sec  7.12 MBytes  59.8 Mbits/sec    0    909 KBytes       
    [  5]   8.00-9.00   sec  7.12 MBytes  59.8 Mbits/sec    0    997 KBytes       
    [  5]   9.00-10.00  sec  8.50 MBytes  71.3 Mbits/sec    0    997 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  73.6 MBytes  61.8 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  70.1 MBytes  58.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 206385 bytes (487 packets)
    TX: 106112 bytes (535 packets)
    signal: -34 dBm
    rx bitrate: 130.0 MBit/s MCS 15
    tx bitrate: 130.0 MBit/s MCS 15
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">167</span> Mbits/sec | <span style="font-size: 1.5rem;">60.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 54935 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   1.00-2.00   sec  20.5 MBytes   172 Mbits/sec                  
    [  5]   2.00-3.00   sec  20.9 MBytes   175 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   5.00-6.00   sec  20.1 MBytes   169 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.8 MBytes   157 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   199 MBytes   167 Mbits/sec  215             sender
    [  5]   0.00-10.00  sec   196 MBytes   164 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 34687 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  10.4 MBytes  86.9 Mbits/sec    0    313 KBytes       
    [  5]   1.00-2.00   sec  9.00 MBytes  75.5 Mbits/sec    0    387 KBytes       
    [  5]   2.00-3.00   sec  8.25 MBytes  69.2 Mbits/sec    0    407 KBytes       
    [  5]   3.00-4.00   sec  8.50 MBytes  71.3 Mbits/sec    0    407 KBytes       
    [  5]   4.00-5.00   sec  8.12 MBytes  68.2 Mbits/sec    0    431 KBytes       
    [  5]   5.00-6.00   sec  7.12 MBytes  59.8 Mbits/sec    0    431 KBytes       
    [  5]   6.00-7.00   sec  6.12 MBytes  51.4 Mbits/sec    0    431 KBytes       
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec    0    431 KBytes       
    [  5]   8.00-9.00   sec  5.25 MBytes  44.0 Mbits/sec    0    431 KBytes       
    [  5]   9.00-10.00  sec  4.38 MBytes  36.7 Mbits/sec    0    431 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  72.4 MBytes  60.7 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  70.1 MBytes  58.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -26 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">167</span> Mbits/sec | <span style="font-size: 1.5rem;">48.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 42215 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   1.00-2.00   sec  20.1 MBytes   169 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   5.00-6.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   7.00-8.00   sec  19.6 MBytes   165 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   9.00-10.00  sec  19.4 MBytes   163 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   200 MBytes   167 Mbits/sec   64             sender
    [  5]   0.00-10.00  sec   196 MBytes   164 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 54845 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  10.0 MBytes  83.8 Mbits/sec    0    525 KBytes       
    [  5]   1.00-2.00   sec  6.50 MBytes  54.5 Mbits/sec    0    525 KBytes       
    [  5]   2.00-3.00   sec  5.38 MBytes  45.1 Mbits/sec    0    525 KBytes       
    [  5]   3.00-4.00   sec  5.38 MBytes  45.1 Mbits/sec    0    525 KBytes       
    [  5]   4.00-5.00   sec  4.12 MBytes  34.6 Mbits/sec    0    525 KBytes       
    [  5]   5.00-6.00   sec  5.38 MBytes  45.1 Mbits/sec    0    525 KBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec    0    525 KBytes       
    [  5]   7.00-8.00   sec  4.38 MBytes  36.7 Mbits/sec    0    525 KBytes       
    [  5]   8.00-9.00   sec  6.38 MBytes  53.5 Mbits/sec    0    525 KBytes       
    [  5]   9.00-10.00  sec  4.25 MBytes  35.6 Mbits/sec    0    525 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  57.2 MBytes  48.0 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  55.4 MBytes  46.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -32 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8814AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">134</span> Mbits/sec | <span style="font-size: 1.5rem;">129</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.106 port 47295 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   1.00-2.00   sec  15.4 MBytes   129 Mbits/sec                  
    [  5]   2.00-3.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   3.00-4.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   4.00-5.00   sec  15.6 MBytes   131 Mbits/sec                  
    [  5]   5.00-6.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   6.00-7.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   7.00-8.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   8.00-9.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   9.00-10.00  sec  15.1 MBytes   127 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   160 MBytes   134 Mbits/sec  448             sender
    [  5]   0.00-10.00  sec   156 MBytes   131 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.106 port 55601 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  15.8 MBytes   132 Mbits/sec    0    683 KBytes       
    [  5]   1.00-2.00   sec  15.1 MBytes   127 Mbits/sec    0   1.09 MBytes       
    [  5]   2.00-3.00   sec  15.2 MBytes   128 Mbits/sec    0   1.35 MBytes       
    [  5]   3.00-4.00   sec  15.8 MBytes   132 Mbits/sec    0   1.51 MBytes       
    [  5]   4.00-5.00   sec  16.1 MBytes   135 Mbits/sec    0   1.59 MBytes       
    [  5]   5.00-6.00   sec  14.6 MBytes   123 Mbits/sec    0   1.59 MBytes       
    [  5]   6.00-7.00   sec  15.5 MBytes   130 Mbits/sec    0   1.77 MBytes       
    [  5]   7.00-8.00   sec  16.1 MBytes   135 Mbits/sec    0   1.86 MBytes       
    [  5]   8.00-9.00   sec  14.9 MBytes   125 Mbits/sec    0   1.96 MBytes       
    [  5]   9.00-10.00  sec  14.6 MBytes   123 Mbits/sec    0   1.96 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   154 MBytes   129 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   151 MBytes   127 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    signal: -37 dBm
    tx bitrate: 174.0 MBit/s
    ```

#### Realtek 8822CE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8822CE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.21-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">652</span> Mbits/sec | <span style="font-size: 1.5rem;">589</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 55511 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  76.8 MBytes   644 Mbits/sec                  
    [  5]   1.00-2.00   sec  79.6 MBytes   668 Mbits/sec                  
    [  5]   2.00-3.00   sec  82.6 MBytes   693 Mbits/sec                  
    [  5]   3.00-4.00   sec  79.2 MBytes   664 Mbits/sec                  
    [  5]   4.00-5.00   sec  78.1 MBytes   655 Mbits/sec                  
    [  5]   5.00-6.00   sec  80.1 MBytes   672 Mbits/sec                  
    [  5]   6.00-7.00   sec  77.4 MBytes   649 Mbits/sec                  
    [  5]   7.00-8.00   sec  72.8 MBytes   611 Mbits/sec                  
    [  5]   8.00-9.00   sec  73.4 MBytes   616 Mbits/sec                  
    [  5]   9.00-10.00  sec  74.0 MBytes   621 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   778 MBytes   652 Mbits/sec  557             sender
    [  5]   0.00-10.00  sec   774 MBytes   649 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 49405 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  68.8 MBytes   577 Mbits/sec    0   5.21 MBytes       
    [  5]   1.00-2.00   sec  73.8 MBytes   619 Mbits/sec  147   2.61 MBytes       
    [  5]   2.00-3.00   sec  72.5 MBytes   608 Mbits/sec    0   2.61 MBytes       
    [  5]   3.00-4.00   sec  75.0 MBytes   629 Mbits/sec    0   2.61 MBytes       
    [  5]   4.00-5.00   sec  70.0 MBytes   587 Mbits/sec    0   2.61 MBytes       
    [  5]   5.00-6.00   sec  76.2 MBytes   640 Mbits/sec    0   2.61 MBytes       
    [  5]   6.00-7.00   sec  71.2 MBytes   598 Mbits/sec  140   1.33 MBytes       
    [  5]   7.00-8.00   sec  67.5 MBytes   566 Mbits/sec    5    727 KBytes       
    [  5]   8.00-9.00   sec  60.0 MBytes   503 Mbits/sec    0    839 KBytes       
    [  5]   9.00-10.00  sec  67.5 MBytes   566 Mbits/sec    0    946 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   702 MBytes   589 Mbits/sec  292             sender
    [  5]   0.00-10.01  sec   700 MBytes   586 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 147261 bytes (520 packets)
    TX: 56969 bytes (214 packets)
    signal: -27 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">79.8</span> Mbits/sec | <span style="font-size: 1.5rem;">143</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.117 port 58121 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  9.50 MBytes  79.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  9.25 MBytes  77.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  9.38 MBytes  78.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  8.00 MBytes  67.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  7.88 MBytes  66.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.25 MBytes  77.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  95.2 MBytes  79.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  91.8 MBytes  77.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.117 port 50355 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  16.2 MBytes   136 Mbits/sec    0    683 KBytes       
    [  5]   1.00-2.00   sec  15.6 MBytes   131 Mbits/sec    0   1.06 MBytes       
    [  5]   2.00-3.00   sec  16.8 MBytes   141 Mbits/sec    0   1.49 MBytes       
    [  5]   3.00-4.00   sec  16.8 MBytes   140 Mbits/sec    0   1.49 MBytes       
    [  5]   4.00-5.00   sec  18.1 MBytes   152 Mbits/sec    0   1.49 MBytes       
    [  5]   5.00-6.00   sec  17.2 MBytes   145 Mbits/sec    0   1.49 MBytes       
    [  5]   6.00-7.00   sec  16.9 MBytes   142 Mbits/sec    0   1.62 MBytes       
    [  5]   7.00-8.00   sec  17.5 MBytes   147 Mbits/sec    0   1.77 MBytes       
    [  5]   8.00-9.00   sec  18.1 MBytes   152 Mbits/sec    0   1.77 MBytes       
    [  5]   9.00-10.00  sec  17.5 MBytes   147 Mbits/sec    0   1.77 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   171 MBytes   143 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   167 MBytes   140 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 48113 bytes (185 packets)
    TX: 52657 bytes (216 packets)
    signal: -38 dBm
    rx bitrate: 600.4 MBit/s 80MHz HE-MCS 11 HE-NSS 1 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">145</span> Mbits/sec | <span style="font-size: 1.5rem;">63.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 59595 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   896 KBytes  7.33 Mbits/sec                  
    [  5]   1.00-2.00   sec  0.00 Bytes  0.00 bits/sec                  
    [  5]   2.00-3.00   sec  4.50 MBytes  37.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  27.8 MBytes   233 Mbits/sec                  
    [  5]   5.00-6.00   sec  20.9 MBytes   175 Mbits/sec                  
    [  5]   6.00-7.00   sec  37.0 MBytes   310 Mbits/sec                  
    [  5]   7.00-8.00   sec  8.38 MBytes  70.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  24.9 MBytes   209 Mbits/sec                  
    [  5]   9.00-10.00  sec  37.4 MBytes   314 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   173 MBytes   145 Mbits/sec  426             sender
    [  5]   0.00-10.00  sec   170 MBytes   143 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 56845 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.6 MBytes   164 Mbits/sec  170   2.14 MBytes       
    [  5]   1.00-2.00   sec  11.1 MBytes  93.3 Mbits/sec    1   2.14 MBytes       
    [  5]   2.00-3.00   sec  5.88 MBytes  49.3 Mbits/sec   46   1.07 MBytes       
    [  5]   3.00-4.00   sec  17.8 MBytes   149 Mbits/sec    6    557 KBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    1    573 KBytes       
    [  5]   5.00-6.00   sec  6.12 MBytes  51.4 Mbits/sec   25   1.41 KBytes       
    [  5]   6.00-7.00   sec  1.50 MBytes  12.6 Mbits/sec    0    297 KBytes       
    [  5]   7.00-8.00   sec  4.62 MBytes  38.8 Mbits/sec    0    313 KBytes       
    [  5]   8.00-9.00   sec  1.38 MBytes  11.5 Mbits/sec    0    320 KBytes       
    [  5]   9.00-10.00  sec  1.38 MBytes  11.5 Mbits/sec    1    322 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  75.6 MBytes  63.4 Mbits/sec  250             sender
    [  5]   0.00-10.28  sec  73.0 MBytes  59.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 38875 bytes (153 packets)
    TX: 51771 bytes (215 packets)
    signal: -29 dBm
    rx bitrate: 6.0 MBit/s 40MHz
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">86.4</span> Mbits/sec | <span style="font-size: 1.5rem;">66.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.114 port 37801 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.00 MBytes  75.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  9.88 MBytes  82.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.50 MBytes  79.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   103 MBytes  86.4 Mbits/sec   21             sender
    [  5]   0.00-10.00  sec   101 MBytes  84.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.114 port 36747 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.50 MBytes  62.8 Mbits/sec    0    260 KBytes       
    [  5]   1.00-2.00   sec  8.62 MBytes  72.4 Mbits/sec    0    414 KBytes       
    [  5]   2.00-3.00   sec  8.00 MBytes  67.1 Mbits/sec    0    479 KBytes       
    [  5]   3.00-4.00   sec  7.88 MBytes  66.1 Mbits/sec   20    379 KBytes       
    [  5]   4.00-5.00   sec  8.00 MBytes  67.1 Mbits/sec    0    434 KBytes       
    [  5]   5.00-6.00   sec  7.62 MBytes  64.0 Mbits/sec    0    486 KBytes       
    [  5]   6.00-7.00   sec  7.75 MBytes  65.0 Mbits/sec    0    506 KBytes       
    [  5]   7.00-8.00   sec  8.12 MBytes  68.2 Mbits/sec    0    518 KBytes       
    [  5]   8.00-9.00   sec  7.50 MBytes  62.9 Mbits/sec    0    532 KBytes       
    [  5]   9.00-10.00  sec  7.88 MBytes  66.0 Mbits/sec    0    532 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  78.9 MBytes  66.2 Mbits/sec   20             sender
    [  5]   0.00-10.01  sec  76.0 MBytes  63.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 183026 bytes (533 packets)
    TX: 93821 bytes (523 packets)
    signal: -17 dBm
    rx bitrate: 216.0 MBit/s MCS 13 40MHz
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Atheros AR9271

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">56.1</span> Mbits/sec | <span style="font-size: 1.5rem;">48.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.113 port 47417 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.00 MBytes  50.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.50 MBytes  54.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  67.1 MBytes  56.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  64.6 MBytes  54.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.113 port 50395 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.50 MBytes  54.5 Mbits/sec    0    240 KBytes       
    [  5]   1.00-2.00   sec  5.75 MBytes  48.2 Mbits/sec    0    269 KBytes       
    [  5]   2.00-3.00   sec  5.88 MBytes  49.3 Mbits/sec    0    283 KBytes       
    [  5]   3.00-4.00   sec  5.50 MBytes  46.1 Mbits/sec    0    283 KBytes       
    [  5]   4.00-5.00   sec  6.00 MBytes  50.3 Mbits/sec    0    283 KBytes       
    [  5]   5.00-6.00   sec  5.25 MBytes  44.0 Mbits/sec    0    283 KBytes       
    [  5]   6.00-7.00   sec  6.00 MBytes  50.3 Mbits/sec    0    283 KBytes       
    [  5]   7.00-8.00   sec  5.38 MBytes  45.1 Mbits/sec    0    283 KBytes       
    [  5]   8.00-9.00   sec  5.50 MBytes  46.1 Mbits/sec    0    283 KBytes       
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec    0    283 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  57.4 MBytes  48.1 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  56.4 MBytes  47.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 81614 bytes (316 packets)
    TX: 46973 bytes (198 packets)
    signal: -36 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### BCM 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">45.9</span> Mbits/sec | <span style="font-size: 1.5rem;">54.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 32865 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.29 MBytes  52.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.39 MBytes  45.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.27 MBytes  44.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.06 MBytes  42.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.72 MBytes  39.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.79 MBytes  40.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.80 MBytes  40.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.91 MBytes  41.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.86 MBytes  49.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.49 MBytes  46.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.22  sec  55.9 MBytes  45.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  52.6 MBytes  44.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 37267 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.76 MBytes  73.5 Mbits/sec    0    341 KBytes       
    [  5]   1.00-2.00   sec  5.72 MBytes  48.0 Mbits/sec    0    341 KBytes       
    [  5]   2.00-3.00   sec  7.21 MBytes  60.5 Mbits/sec    0    341 KBytes       
    [  5]   3.00-4.00   sec  5.72 MBytes  47.9 Mbits/sec    0    341 KBytes       
    [  5]   4.00-5.00   sec  6.40 MBytes  53.7 Mbits/sec    0    363 KBytes       
    [  5]   5.00-6.00   sec  6.03 MBytes  50.6 Mbits/sec    0    363 KBytes       
    [  5]   6.00-7.00   sec  6.03 MBytes  50.5 Mbits/sec    0    363 KBytes       
    [  5]   7.00-8.00   sec  6.03 MBytes  50.6 Mbits/sec   22    270 KBytes       
    [  5]   8.00-9.00   sec  6.71 MBytes  56.3 Mbits/sec    0    324 KBytes       
    [  5]   9.00-10.00  sec  6.09 MBytes  51.1 Mbits/sec    0    338 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  64.7 MBytes  54.3 Mbits/sec   22             sender
    [  5]   0.00-10.01  sec  63.4 MBytes  53.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 76765 bytes (203 packets)
    TX: 52071 bytes (244 packets)
    signal: -49 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">20.6</span> Mbits/sec | <span style="font-size: 1.5rem;">27.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.112 port 46451 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.88 MBytes  15.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  2.12 MBytes  17.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.38 MBytes  19.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.50 MBytes  21.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.88 MBytes  15.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.62 MBytes  22.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.50 MBytes  21.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.75 MBytes  23.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.11  sec  24.9 MBytes  20.6 Mbits/sec    8             sender
    [  5]   0.00-10.00  sec  23.5 MBytes  19.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.112 port 52773 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.50 MBytes  46.1 Mbits/sec    0    250 KBytes       
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec    4    256 KBytes       
    [  5]   2.00-3.00   sec  3.38 MBytes  28.3 Mbits/sec   13    204 KBytes       
    [  5]   3.00-4.00   sec  2.88 MBytes  24.1 Mbits/sec    8    157 KBytes       
    [  5]   4.00-5.00   sec  3.38 MBytes  28.3 Mbits/sec    0    174 KBytes       
    [  5]   5.00-6.00   sec  3.38 MBytes  28.3 Mbits/sec    0    184 KBytes       
    [  5]   6.00-7.00   sec  3.50 MBytes  29.4 Mbits/sec    8    153 KBytes       
    [  5]   7.00-8.00   sec  2.75 MBytes  23.1 Mbits/sec    7    123 KBytes       
    [  5]   8.00-9.00   sec  2.00 MBytes  16.8 Mbits/sec    0    136 KBytes       
    [  5]   9.00-10.00  sec  2.75 MBytes  23.0 Mbits/sec    0    148 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  32.8 MBytes  27.5 Mbits/sec   40             sender
    [  5]   0.00-10.01  sec  31.2 MBytes  26.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 125604 bytes (493 packets)
    TX: 53755 bytes (213 packets)
    signal: -31 dBm
    rx bitrate: 57.8 MBit/s MCS 5 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">94.7</span> Mbits/sec | <span style="font-size: 1.5rem;">68.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.111 port 44299 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.2 MBytes  85.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.2 MBytes  94.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   113 MBytes  94.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   111 MBytes  93.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.111 port 59869 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.12 MBytes  76.5 Mbits/sec    0    277 KBytes       
    [  5]   1.00-2.00   sec  8.25 MBytes  69.2 Mbits/sec    0    331 KBytes       
    [  5]   2.00-3.00   sec  7.62 MBytes  64.0 Mbits/sec    0    349 KBytes       
    [  5]   3.00-4.00   sec  8.38 MBytes  70.3 Mbits/sec    0    349 KBytes       
    [  5]   4.00-5.00   sec  8.25 MBytes  69.2 Mbits/sec    0    395 KBytes       
    [  5]   5.00-6.00   sec  8.00 MBytes  67.1 Mbits/sec    0    395 KBytes       
    [  5]   6.00-7.00   sec  8.12 MBytes  68.2 Mbits/sec    0    395 KBytes       
    [  5]   7.00-8.00   sec  8.12 MBytes  68.2 Mbits/sec    0    395 KBytes       
    [  5]   8.00-9.00   sec  8.00 MBytes  67.1 Mbits/sec    0    395 KBytes       
    [  5]   9.00-10.00  sec  8.12 MBytes  68.1 Mbits/sec    0    395 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  82.0 MBytes  68.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  80.5 MBytes  67.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 192856 bytes (578 packets)
    TX: 110970 bytes (552 packets)
    signal: -34 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">44.1</span> Mbits/sec | <span style="font-size: 1.5rem;">48.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.110 port 39085 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.50 MBytes  37.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.75 MBytes  39.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  52.8 MBytes  44.1 Mbits/sec   54             sender
    [  5]   0.00-10.00  sec  49.6 MBytes  41.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.110 port 39197 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.62 MBytes  55.5 Mbits/sec    0    280 KBytes       
    [  5]   1.00-2.00   sec  6.00 MBytes  50.3 Mbits/sec    0    352 KBytes       
    [  5]   2.00-3.00   sec  5.88 MBytes  49.3 Mbits/sec    0    482 KBytes       
    [  5]   3.00-4.00   sec  6.12 MBytes  51.4 Mbits/sec    0    482 KBytes       
    [  5]   4.00-5.00   sec  6.00 MBytes  50.3 Mbits/sec    0    482 KBytes       
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec    0    482 KBytes       
    [  5]   6.00-7.00   sec  6.00 MBytes  50.3 Mbits/sec    0    482 KBytes       
    [  5]   7.00-8.00   sec  5.12 MBytes  43.0 Mbits/sec    0    482 KBytes       
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec    0    482 KBytes       
    [  5]   9.00-10.00  sec  5.38 MBytes  45.1 Mbits/sec    0    516 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  57.2 MBytes  48.0 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  55.2 MBytes  46.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 75524 bytes (241 packets)
    TX: 54645 bytes (224 packets)
    signal: -32 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">27.4</span> Mbits/sec | <span style="font-size: 1.5rem;">44.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.109 port 47471 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   4.00-5.00   sec   768 KBytes  6.29 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.62 MBytes  22.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.38 MBytes  19.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.06  sec  32.9 MBytes  27.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  29.1 MBytes  24.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.109 port 52855 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.50 MBytes  54.5 Mbits/sec    0    277 KBytes       
    [  5]   1.00-2.00   sec  5.25 MBytes  44.0 Mbits/sec    0    324 KBytes       
    [  5]   2.00-3.00   sec  5.50 MBytes  46.2 Mbits/sec    0    431 KBytes       
    [  5]   3.00-4.00   sec  5.12 MBytes  43.0 Mbits/sec    0    447 KBytes       
    [  5]   4.00-5.00   sec  5.88 MBytes  49.3 Mbits/sec    0    502 KBytes       
    [  5]   5.00-6.00   sec  4.12 MBytes  34.6 Mbits/sec    0    532 KBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec    0    564 KBytes       
    [  5]   7.00-8.00   sec  5.62 MBytes  47.2 Mbits/sec    0    597 KBytes       
    [  5]   8.00-9.00   sec  4.75 MBytes  39.8 Mbits/sec    0    597 KBytes       
    [  5]   9.00-10.00  sec  4.88 MBytes  40.9 Mbits/sec    0    626 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  53.1 MBytes  44.6 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  49.8 MBytes  41.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 75912 bytes (282 packets)
    TX: 53915 bytes (221 packets)
    signal: -36 dBm
    rx bitrate: 39.0 MBit/s MCS 4
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8821CU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">127</span> Mbits/sec | <span style="font-size: 1.5rem;">119</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.136 port 44949 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.2 MBytes  85.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   3.00-4.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   5.00-6.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   7.00-8.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   8.00-9.00   sec  15.8 MBytes   132 Mbits/sec                  
    [  5]   9.00-10.00  sec  15.9 MBytes   133 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   152 MBytes   127 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   151 MBytes   127 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.136 port 57807 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.0 MBytes   151 Mbits/sec    0    458 KBytes       
    [  5]   1.00-2.00   sec  12.8 MBytes   107 Mbits/sec    0    537 KBytes       
    [  5]   2.00-3.00   sec  13.0 MBytes   109 Mbits/sec    0    591 KBytes       
    [  5]   3.00-4.00   sec  12.0 MBytes   101 Mbits/sec    0    591 KBytes       
    [  5]   4.00-5.00   sec  13.2 MBytes   111 Mbits/sec    0    591 KBytes       
    [  5]   5.00-6.00   sec  12.1 MBytes   102 Mbits/sec    0    591 KBytes       
    [  5]   6.00-7.00   sec  14.2 MBytes   120 Mbits/sec    0    591 KBytes       
    [  5]   7.00-8.00   sec  15.1 MBytes   127 Mbits/sec    0    662 KBytes       
    [  5]   8.00-9.00   sec  16.2 MBytes   136 Mbits/sec    0    662 KBytes       
    [  5]   9.00-10.00  sec  14.9 MBytes   125 Mbits/sec    0    662 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   142 MBytes   119 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   139 MBytes   116 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 194772 bytes (372 packets)
    TX: 102357 bytes (482 packets)
    signal: -47 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">139</span> Mbits/sec | <span style="font-size: 1.5rem;">142</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 36591 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.1 MBytes   127 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.5 MBytes   139 Mbits/sec                  
    [  5]   2.00-3.00   sec  15.7 MBytes   132 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.5 MBytes   138 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.2 MBytes   136 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   166 MBytes   139 Mbits/sec  241             sender
    [  5]   0.00-10.00  sec   162 MBytes   136 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 56441 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.4 MBytes   154 Mbits/sec    0    458 KBytes       
    [  5]   1.00-2.00   sec  17.1 MBytes   143 Mbits/sec    0    458 KBytes       
    [  5]   2.00-3.00   sec  17.0 MBytes   142 Mbits/sec    0    458 KBytes       
    [  5]   3.00-4.00   sec  16.3 MBytes   137 Mbits/sec    0    458 KBytes       
    [  5]   4.00-5.00   sec  16.0 MBytes   134 Mbits/sec    0    458 KBytes       
    [  5]   5.00-6.00   sec  17.2 MBytes   144 Mbits/sec    0    458 KBytes       
    [  5]   6.00-7.00   sec  16.9 MBytes   142 Mbits/sec    0    458 KBytes       
    [  5]   7.00-8.00   sec  16.0 MBytes   134 Mbits/sec    0    458 KBytes       
    [  5]   8.00-9.00   sec  16.3 MBytes   137 Mbits/sec    0    458 KBytes       
    [  5]   9.00-10.00  sec  17.9 MBytes   150 Mbits/sec    0    718 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   169 MBytes   142 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   166 MBytes   139 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 256580352 bytes (223586 packets)
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
