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
**Test Date:** [2025-05-23 14:40 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15212001294)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">58.8</span> Mbits/sec | <span style="font-size: 1.5rem;">59.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 52297 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.39 MBytes  53.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.73 MBytes  56.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.78 MBytes  56.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.64 MBytes  55.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.78 MBytes  56.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.56 MBytes  55.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.72 MBytes  56.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.73 MBytes  56.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.72 MBytes  56.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.62 MBytes  55.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  70.2 MBytes  58.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  66.7 MBytes  55.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 47597 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.83 MBytes  74.1 Mbits/sec    0    440 KBytes       
    [  5]   1.00-2.00   sec  7.64 MBytes  64.1 Mbits/sec    0    591 KBytes       
    [  5]   2.00-3.00   sec  7.40 MBytes  62.1 Mbits/sec    0    796 KBytes       
    [  5]   3.00-4.00   sec  6.25 MBytes  52.4 Mbits/sec    0    935 KBytes       
    [  5]   4.00-5.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.02 MBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.18 MBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.18 MBytes       
    [  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.18 MBytes       
    [  5]   8.00-9.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.25 MBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.26 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  71.4 MBytes  59.9 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  68.8 MBytes  57.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 37311 bytes (142 packets)
    TX: 49917 bytes (196 packets)
    signal: -28 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">115</span> Mbits/sec | <span style="font-size: 1.5rem;">104</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 52479 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.4 MBytes   104 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.5 MBytes   113 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.05  sec   138 MBytes   115 Mbits/sec   90             sender
    [  5]   0.00-10.00  sec   134 MBytes   112 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 40751 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  13.0 MBytes   109 Mbits/sec    0    468 KBytes       
    [  5]   1.00-2.00   sec  12.1 MBytes   101 Mbits/sec    0    540 KBytes       
    [  5]   2.00-3.00   sec  12.4 MBytes   104 Mbits/sec    0    566 KBytes       
    [  5]   3.00-4.00   sec  12.4 MBytes   104 Mbits/sec    0    566 KBytes       
    [  5]   4.00-5.00   sec  12.2 MBytes   102 Mbits/sec    0    592 KBytes       
    [  5]   5.00-6.00   sec  12.6 MBytes   105 Mbits/sec    0    655 KBytes       
    [  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec    0    734 KBytes       
    [  5]   7.00-8.00   sec  12.9 MBytes   108 Mbits/sec    0    734 KBytes       
    [  5]   8.00-9.00   sec  12.4 MBytes   104 Mbits/sec    0    734 KBytes       
    [  5]   9.00-10.00  sec  12.2 MBytes   102 Mbits/sec    0    734 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   124 MBytes   104 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   123 MBytes   103 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 127969 bytes (552 packets)
    TX: 56319 bytes (243 packets)
    signal: -35 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">97.8</span> Mbits/sec | <span style="font-size: 1.5rem;">99.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 47897 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.4 MBytes  86.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.8 MBytes  98.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   117 MBytes  97.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   116 MBytes  97.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 35515 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  14.8 MBytes   124 Mbits/sec    0    643 KBytes       
    [  5]   1.00-2.00   sec  10.8 MBytes  90.2 Mbits/sec    0    675 KBytes       
    [  5]   2.00-3.00   sec  12.4 MBytes   104 Mbits/sec    0    747 KBytes       
    [  5]   3.00-4.00   sec  12.4 MBytes   104 Mbits/sec    0    795 KBytes       
    [  5]   4.00-5.00   sec  11.1 MBytes  93.3 Mbits/sec    0    841 KBytes       
    [  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec    0    841 KBytes       
    [  5]   6.00-7.00   sec  12.6 MBytes   106 Mbits/sec    0    888 KBytes       
    [  5]   7.00-8.00   sec  9.62 MBytes  80.7 Mbits/sec    0    888 KBytes       
    [  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0    888 KBytes       
    [  5]   9.00-10.00  sec  11.1 MBytes  93.3 Mbits/sec    0    888 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   118 MBytes  99.4 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   115 MBytes  96.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 181788 bytes (434 packets)
    TX: 105538 bytes (502 packets)
    signal: -36 dBm
    rx bitrate: 130.0 MBit/s MCS 15
    tx bitrate: 144.4 MBit/s MCS 15 short GI
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">139</span> Mbits/sec | <span style="font-size: 1.5rem;">106</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 38093 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.8 MBytes   115 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.5 MBytes   138 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   6.00-7.00   sec  15.6 MBytes   131 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.6 MBytes   139 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   166 MBytes   139 Mbits/sec  141             sender
    [  5]   0.00-10.00  sec   162 MBytes   136 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 50979 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  14.5 MBytes   122 Mbits/sec    0    501 KBytes       
    [  5]   1.00-2.00   sec  13.9 MBytes   116 Mbits/sec    0    557 KBytes       
    [  5]   2.00-3.00   sec  14.2 MBytes   120 Mbits/sec    0    585 KBytes       
    [  5]   3.00-4.00   sec  12.4 MBytes   104 Mbits/sec    0    585 KBytes       
    [  5]   4.00-5.00   sec  9.50 MBytes  79.7 Mbits/sec    0    585 KBytes       
    [  5]   5.00-6.00   sec  11.9 MBytes  99.6 Mbits/sec    0    585 KBytes       
    [  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec    0    659 KBytes       
    [  5]   7.00-8.00   sec  12.2 MBytes   103 Mbits/sec    0    659 KBytes       
    [  5]   8.00-9.00   sec  12.1 MBytes   102 Mbits/sec    0    659 KBytes       
    [  5]   9.00-10.00  sec  13.2 MBytes   111 Mbits/sec    0    659 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   126 MBytes   106 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   124 MBytes   104 Mbits/sec                  receiver
    
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
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">109</span> Mbits/sec | <span style="font-size: 1.5rem;">103</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 56907 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.1 MBytes  93.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   3.00-4.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.9 MBytes   108 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   130 MBytes   109 Mbits/sec  455             sender
    [  5]   0.00-10.00  sec   126 MBytes   106 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 32849 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  15.0 MBytes   126 Mbits/sec    0    496 KBytes       
    [  5]   1.00-2.00   sec  11.9 MBytes  99.6 Mbits/sec    0    559 KBytes       
    [  5]   2.00-3.00   sec  12.5 MBytes   105 Mbits/sec    0    619 KBytes       
    [  5]   3.00-4.00   sec  11.0 MBytes  92.3 Mbits/sec    0    697 KBytes       
    [  5]   4.00-5.00   sec  12.6 MBytes   106 Mbits/sec    0    734 KBytes       
    [  5]   5.00-6.00   sec  12.9 MBytes   108 Mbits/sec    0    734 KBytes       
    [  5]   6.00-7.00   sec  9.62 MBytes  80.7 Mbits/sec    0    734 KBytes       
    [  5]   7.00-8.00   sec  11.4 MBytes  95.4 Mbits/sec    0    734 KBytes       
    [  5]   8.00-9.00   sec  12.5 MBytes   105 Mbits/sec    0    734 KBytes       
    [  5]   9.00-10.00  sec  13.0 MBytes   109 Mbits/sec    0    734 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   122 MBytes   103 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   119 MBytes  99.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    signal: -44 dBm
    tx bitrate: 174.0 MBit/s
    ```

#### Realtek 8814AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">147</span> Mbits/sec | <span style="font-size: 1.5rem;">23.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.106 port 52293 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.1 MBytes   135 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.8 MBytes   149 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   176 MBytes   147 Mbits/sec  142             sender
    [  5]   0.00-10.00  sec   173 MBytes   145 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.106 port 46047 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.38 MBytes  28.3 Mbits/sec    0    201 KBytes       
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec    0    308 KBytes       
    [  5]   2.00-3.00   sec  2.62 MBytes  22.0 Mbits/sec    0    325 KBytes       
    [  5]   3.00-4.00   sec  2.75 MBytes  23.1 Mbits/sec    0    342 KBytes       
    [  5]   4.00-5.00   sec  2.75 MBytes  23.1 Mbits/sec    0    342 KBytes       
    [  5]   5.00-6.00   sec  2.75 MBytes  23.1 Mbits/sec    0    342 KBytes       
    [  5]   6.00-7.00   sec  2.88 MBytes  24.1 Mbits/sec    0    342 KBytes       
    [  5]   7.00-8.00   sec  3.00 MBytes  25.2 Mbits/sec    0    361 KBytes       
    [  5]   8.00-9.00   sec  2.25 MBytes  18.9 Mbits/sec    0    387 KBytes       
    [  5]   9.00-10.00  sec  2.50 MBytes  21.0 Mbits/sec    1    270 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  28.1 MBytes  23.6 Mbits/sec    1             sender
    [  5]   0.00-10.09  sec  26.9 MBytes  22.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -37 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8821CU #1

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">116</span> Mbits/sec | <span style="font-size: 1.5rem;">203</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.136 port 51013 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  15.0 MBytes   126 Mbits/sec                  
    [  5]   8.00-9.00   sec  15.9 MBytes   133 Mbits/sec                  
    [  5]   9.00-10.00  sec  15.9 MBytes   133 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   139 MBytes   116 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   138 MBytes   116 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.136 port 46429 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  29.4 MBytes   246 Mbits/sec    0    636 KBytes       
    [  5]   1.00-2.00   sec  25.5 MBytes   214 Mbits/sec    0    636 KBytes       
    [  5]   2.00-3.00   sec  24.8 MBytes   208 Mbits/sec    0    667 KBytes       
    [  5]   3.00-4.00   sec  24.0 MBytes   201 Mbits/sec    0    667 KBytes       
    [  5]   4.00-5.00   sec  24.1 MBytes   202 Mbits/sec    0    667 KBytes       
    [  5]   5.00-6.00   sec  22.8 MBytes   191 Mbits/sec    0    667 KBytes       
    [  5]   6.00-7.00   sec  23.1 MBytes   194 Mbits/sec    0    704 KBytes       
    [  5]   7.00-8.00   sec  22.1 MBytes   186 Mbits/sec    0    704 KBytes       
    [  5]   8.00-9.00   sec  23.2 MBytes   195 Mbits/sec    2    704 KBytes       
    [  5]   9.00-10.00  sec  23.4 MBytes   196 Mbits/sec    0    704 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   242 MBytes   203 Mbits/sec    2             sender
    [  5]   0.00-10.02  sec   239 MBytes   200 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 195141 bytes (375 packets)
    TX: 101644 bytes (475 packets)
    signal: -36 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">35.7</span> Mbits/sec | <span style="font-size: 1.5rem;">175</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.163 port 40003 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  8.12 MBytes  68.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.88 MBytes  74.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.62 MBytes  22.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.75 MBytes  23.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.38 MBytes  11.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.62 MBytes  13.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.00 MBytes  33.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.05  sec  42.8 MBytes  35.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  39.6 MBytes  33.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.163 port 60179 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.8 MBytes   216 Mbits/sec    0   3.20 MBytes       
    [  5]   1.00-2.00   sec  25.9 MBytes   217 Mbits/sec    0   3.89 MBytes       
    [  5]   2.00-3.00   sec  27.0 MBytes   226 Mbits/sec    0   5.53 MBytes       
    [  5]   3.00-4.00   sec  26.6 MBytes   223 Mbits/sec    0   5.53 MBytes       
    [  5]   4.00-5.00   sec  23.9 MBytes   200 Mbits/sec    0   6.10 MBytes       
    [  5]   5.00-6.00   sec  23.1 MBytes   194 Mbits/sec    0   6.24 MBytes       
    [  5]   6.00-7.00   sec  15.8 MBytes   132 Mbits/sec    0   6.42 MBytes       
    [  5]   7.00-8.00   sec  16.9 MBytes   141 Mbits/sec    0   6.42 MBytes       
    [  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   6.42 MBytes       
    [  5]   9.00-10.00  sec  12.9 MBytes   108 Mbits/sec    0   6.42 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   209 MBytes   175 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   209 MBytes   175 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">514</span> Mbits/sec | <span style="font-size: 1.5rem;">315</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 43813 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  68.0 MBytes   570 Mbits/sec                  
    [  5]   1.00-2.00   sec  67.8 MBytes   569 Mbits/sec                  
    [  5]   2.00-3.00   sec  56.2 MBytes   471 Mbits/sec                  
    [  5]   3.00-4.00   sec  59.9 MBytes   502 Mbits/sec                  
    [  5]   4.00-5.00   sec  60.3 MBytes   506 Mbits/sec                  
    [  5]   5.00-6.00   sec  55.6 MBytes   467 Mbits/sec                  
    [  5]   6.00-7.00   sec  59.3 MBytes   498 Mbits/sec                  
    [  5]   7.00-8.00   sec  59.5 MBytes   499 Mbits/sec                  
    [  5]   8.00-9.00   sec  63.5 MBytes   533 Mbits/sec                  
    [  5]   9.00-10.00  sec  60.2 MBytes   505 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   614 MBytes   514 Mbits/sec  334             sender
    [  5]   0.00-10.00  sec   610 MBytes   512 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 54887 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.5 MBytes   214 Mbits/sec   14    185 KBytes       
    [  5]   1.00-2.00   sec  36.4 MBytes   305 Mbits/sec   52   87.7 KBytes       
    [  5]   2.00-3.00   sec  32.5 MBytes   273 Mbits/sec    7    252 KBytes       
    [  5]   3.00-4.00   sec  50.8 MBytes   426 Mbits/sec    0    457 KBytes       
    [  5]   4.00-5.00   sec  45.4 MBytes   381 Mbits/sec   14    219 KBytes       
    [  5]   5.00-6.00   sec  41.4 MBytes   348 Mbits/sec   14    146 KBytes       
    [  5]   6.00-7.00   sec  37.6 MBytes   315 Mbits/sec    7    202 KBytes       
    [  5]   7.00-8.00   sec  43.3 MBytes   363 Mbits/sec    7    216 KBytes       
    [  5]   8.00-9.00   sec  30.6 MBytes   257 Mbits/sec   21    204 KBytes       
    [  5]   9.00-10.00  sec  31.6 MBytes   265 Mbits/sec   14    238 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   375 MBytes   315 Mbits/sec  150             sender
    [  5]   0.00-10.01  sec   372 MBytes   312 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 135215 bytes (495 packets)
    TX: 60332 bytes (223 packets)
    signal: -31 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">97.6</span> Mbits/sec | <span style="font-size: 1.5rem;">152</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.117 port 45117 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.8 MBytes  90.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.9 MBytes  99.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.1 MBytes  93.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   116 MBytes  97.6 Mbits/sec  147             sender
    [  5]   0.00-10.00  sec   114 MBytes  95.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.117 port 51683 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  20.1 MBytes   169 Mbits/sec    0    559 KBytes       
    [  5]   1.00-2.00   sec  18.2 MBytes   153 Mbits/sec    0    669 KBytes       
    [  5]   2.00-3.00   sec  17.5 MBytes   147 Mbits/sec    0    669 KBytes       
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec    0    706 KBytes       
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec    0    706 KBytes       
    [  5]   5.00-6.00   sec  16.8 MBytes   141 Mbits/sec    0    738 KBytes       
    [  5]   6.00-7.00   sec  18.2 MBytes   153 Mbits/sec    0    738 KBytes       
    [  5]   7.00-8.00   sec  17.1 MBytes   144 Mbits/sec    0    738 KBytes       
    [  5]   8.00-9.00   sec  18.2 MBytes   153 Mbits/sec    0    738 KBytes       
    [  5]   9.00-10.00  sec  18.1 MBytes   152 Mbits/sec    0    781 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   181 MBytes   152 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   177 MBytes   148 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 160034 bytes (501 packets)
    TX: 88354 bytes (496 packets)
    signal: -38 dBm
    rx bitrate: 1080.6 MBit/s 80MHz HE-MCS 10 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 960.7 MBit/s 80MHz HE-MCS 9 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">311</span> Mbits/sec | <span style="font-size: 1.5rem;">737</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 59875 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  30.0 MBytes   251 Mbits/sec                  
    [  5]   1.00-2.00   sec  34.4 MBytes   288 Mbits/sec                  
    [  5]   2.00-3.00   sec  40.0 MBytes   336 Mbits/sec                  
    [  5]   3.00-4.00   sec  32.4 MBytes   272 Mbits/sec                  
    [  5]   4.00-5.00   sec  32.5 MBytes   273 Mbits/sec                  
    [  5]   5.00-6.00   sec  36.8 MBytes   308 Mbits/sec                  
    [  5]   6.00-7.00   sec  35.4 MBytes   297 Mbits/sec                  
    [  5]   7.00-8.00   sec  46.9 MBytes   393 Mbits/sec                  
    [  5]   8.00-9.00   sec  40.2 MBytes   338 Mbits/sec                  
    [  5]   9.00-10.00  sec  39.1 MBytes   328 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   372 MBytes   311 Mbits/sec  160             sender
    [  5]   0.00-10.00  sec   368 MBytes   308 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 60531 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec   104 MBytes   874 Mbits/sec    0   6.43 MBytes       
    [  5]   1.00-2.00   sec   104 MBytes   876 Mbits/sec    0   6.43 MBytes       
    [  5]   2.00-3.00   sec   106 MBytes   891 Mbits/sec    0   6.43 MBytes       
    [  5]   3.00-4.00   sec  95.0 MBytes   797 Mbits/sec    0   6.43 MBytes       
    [  5]   4.00-5.00   sec  95.5 MBytes   801 Mbits/sec   37   3.21 MBytes       
    [  5]   5.00-6.00   sec   100 MBytes   842 Mbits/sec    0   3.21 MBytes       
    [  5]   6.00-7.00   sec  73.0 MBytes   612 Mbits/sec   96    858 KBytes       
    [  5]   7.00-8.00   sec  64.9 MBytes   544 Mbits/sec    0    963 KBytes       
    [  5]   8.00-9.00   sec  72.5 MBytes   608 Mbits/sec   29    570 KBytes       
    [  5]   9.00-10.00  sec  62.6 MBytes   525 Mbits/sec    0    711 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   879 MBytes   737 Mbits/sec  162             sender
    [  5]   0.00-10.01  sec   875 MBytes   734 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 78806 bytes (273 packets)
    TX: 51439 bytes (229 packets)
    signal: -33 dBm
    rx bitrate: 1297.1 MBit/s 160MHz HE-MCS 6 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">87.3</span> Mbits/sec | <span style="font-size: 1.5rem;">65.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.114 port 40121 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.75 MBytes  81.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.0 MBytes  83.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.2 MBytes  86.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.1 MBytes  85.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.2 MBytes  85.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  10.1 MBytes  84.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   104 MBytes  87.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   102 MBytes  85.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.114 port 40119 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.50 MBytes  71.2 Mbits/sec    0    222 KBytes       
    [  5]   1.00-2.00   sec  7.50 MBytes  62.9 Mbits/sec    0    272 KBytes       
    [  5]   2.00-3.00   sec  7.38 MBytes  61.9 Mbits/sec    0    284 KBytes       
    [  5]   3.00-4.00   sec  7.75 MBytes  65.0 Mbits/sec    0    354 KBytes       
    [  5]   4.00-5.00   sec  8.25 MBytes  69.2 Mbits/sec    0    375 KBytes       
    [  5]   5.00-6.00   sec  7.50 MBytes  63.0 Mbits/sec    0    375 KBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0    375 KBytes       
    [  5]   7.00-8.00   sec  7.75 MBytes  65.0 Mbits/sec    0    375 KBytes       
    [  5]   8.00-9.00   sec  7.38 MBytes  61.9 Mbits/sec    0    375 KBytes       
    [  5]   9.00-10.00  sec  8.75 MBytes  73.3 Mbits/sec    0    527 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  78.2 MBytes  65.6 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  75.2 MBytes  63.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 193222 bytes (585 packets)
    TX: 99469 bytes (543 packets)
    signal: -17 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">56.1</span> Mbits/sec | <span style="font-size: 1.5rem;">43.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.164 port 45037 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.32 MBytes  53.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.29 MBytes  52.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.60 MBytes  55.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.59 MBytes  55.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.61 MBytes  55.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.39 MBytes  53.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.40 MBytes  53.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.68 MBytes  56.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.53 MBytes  54.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.78 MBytes  48.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  67.0 MBytes  56.1 Mbits/sec  145             sender
    [  5]   0.00-10.00  sec  64.2 MBytes  53.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.164 port 34893 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.72 MBytes  48.0 Mbits/sec    0    250 KBytes       
    [  5]   1.00-2.00   sec  5.28 MBytes  44.3 Mbits/sec    0    263 KBytes       
    [  5]   2.00-3.00   sec  5.28 MBytes  44.3 Mbits/sec    0    263 KBytes       
    [  5]   3.00-4.00   sec  4.97 MBytes  41.7 Mbits/sec    0    263 KBytes       
    [  5]   4.00-5.00   sec  4.97 MBytes  41.7 Mbits/sec    0    270 KBytes       
    [  5]   5.00-6.00   sec  4.97 MBytes  41.7 Mbits/sec    0    277 KBytes       
    [  5]   6.00-7.00   sec  5.28 MBytes  44.3 Mbits/sec    0    277 KBytes       
    [  5]   7.00-8.00   sec  5.22 MBytes  43.8 Mbits/sec    0    351 KBytes       
    [  5]   8.00-9.00   sec  5.22 MBytes  43.8 Mbits/sec    0    351 KBytes       
    [  5]   9.00-10.00  sec  5.34 MBytes  44.8 Mbits/sec    0    351 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  52.3 MBytes  43.8 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  51.4 MBytes  43.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 66355 bytes (194 packets)
    TX: 59173 bytes (281 packets)
    signal: -51 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">45.0</span> Mbits/sec | <span style="font-size: 1.5rem;">52.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 34085 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.58 MBytes  46.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.69 MBytes  47.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.02 MBytes  42.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.53 MBytes  46.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.68 MBytes  39.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.78 MBytes  40.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.26 MBytes  44.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.38  sec  55.6 MBytes  45.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  52.1 MBytes  43.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 50963 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.68 MBytes  56.0 Mbits/sec    0    201 KBytes       
    [  5]   1.00-2.00   sec  6.40 MBytes  53.7 Mbits/sec    0    236 KBytes       
    [  5]   2.00-3.00   sec  5.65 MBytes  47.4 Mbits/sec    0    250 KBytes       
    [  5]   3.00-4.00   sec  7.21 MBytes  60.5 Mbits/sec    0    305 KBytes       
    [  5]   4.00-5.00   sec  6.03 MBytes  50.6 Mbits/sec    0    321 KBytes       
    [  5]   5.00-6.00   sec  6.09 MBytes  51.1 Mbits/sec    0    321 KBytes       
    [  5]   6.00-7.00   sec  6.09 MBytes  51.1 Mbits/sec    0    321 KBytes       
    [  5]   7.00-8.00   sec  6.84 MBytes  57.4 Mbits/sec    0    321 KBytes       
    [  5]   8.00-9.00   sec  5.47 MBytes  45.9 Mbits/sec    0    321 KBytes       
    [  5]   9.00-10.00  sec  5.97 MBytes  50.0 Mbits/sec    0    321 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  62.4 MBytes  52.4 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  60.9 MBytes  51.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 57203 bytes (181 packets)
    TX: 53948 bytes (235 packets)
    signal: -52 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">25.5</span> Mbits/sec | <span style="font-size: 1.5rem;">35.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.112 port 51909 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.25 MBytes  10.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  2.62 MBytes  22.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.75 MBytes  23.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.75 MBytes  23.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.75 MBytes  23.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.25 MBytes  27.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  30.5 MBytes  25.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  27.1 MBytes  22.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.112 port 44927 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.88 MBytes  40.9 Mbits/sec    0    228 KBytes       
    [  5]   1.00-2.00   sec  4.50 MBytes  37.7 Mbits/sec    0    409 KBytes       
    [  5]   2.00-3.00   sec  5.25 MBytes  44.0 Mbits/sec    0    573 KBytes       
    [  5]   3.00-4.00   sec  4.00 MBytes  33.5 Mbits/sec    0    734 KBytes       
    [  5]   4.00-5.00   sec  4.12 MBytes  34.6 Mbits/sec    0    829 KBytes       
    [  5]   5.00-6.00   sec  2.75 MBytes  23.1 Mbits/sec    0   1000 KBytes       
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec    1    716 KBytes       
    [  5]   7.00-8.00   sec  2.75 MBytes  23.1 Mbits/sec    0    793 KBytes       
    [  5]   8.00-9.00   sec  4.12 MBytes  34.6 Mbits/sec    0    878 KBytes       
    [  5]   9.00-10.00  sec  4.25 MBytes  35.6 Mbits/sec    1    655 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  42.1 MBytes  35.3 Mbits/sec    2             sender
    [  5]   0.00-10.01  sec  39.0 MBytes  32.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 86377 bytes (366 packets)
    TX: 55984 bytes (217 packets)
    signal: -27 dBm
    rx bitrate: 58.5 MBit/s MCS 6
    tx bitrate: 65.0 MBit/s MCS 7
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">88.1</span> Mbits/sec | <span style="font-size: 1.5rem;">65.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.111 port 53039 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  8.62 MBytes  72.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.75 MBytes  81.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  10.6 MBytes  89.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   105 MBytes  88.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   102 MBytes  85.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.111 port 44471 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.62 MBytes  72.3 Mbits/sec    0    228 KBytes       
    [  5]   1.00-2.00   sec  8.00 MBytes  67.1 Mbits/sec    0    257 KBytes       
    [  5]   2.00-3.00   sec  7.50 MBytes  62.9 Mbits/sec    0    257 KBytes       
    [  5]   3.00-4.00   sec  7.88 MBytes  66.1 Mbits/sec    0    257 KBytes       
    [  5]   4.00-5.00   sec  7.75 MBytes  65.0 Mbits/sec    0    257 KBytes       
    [  5]   5.00-6.00   sec  7.88 MBytes  66.1 Mbits/sec    0    257 KBytes       
    [  5]   6.00-7.00   sec  7.75 MBytes  65.1 Mbits/sec    0    257 KBytes       
    [  5]   7.00-8.00   sec  7.12 MBytes  59.7 Mbits/sec    0    301 KBytes       
    [  5]   8.00-9.00   sec  7.50 MBytes  62.9 Mbits/sec    0    301 KBytes       
    [  5]   9.00-10.00  sec  8.00 MBytes  67.1 Mbits/sec    0    301 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  78.0 MBytes  65.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  76.4 MBytes  64.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 192994 bytes (589 packets)
    TX: 103146 bytes (527 packets)
    signal: -34 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 270.0 MBit/s MCS 15 40MHz
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.28-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">48.1</span> Mbits/sec | <span style="font-size: 1.5rem;">28.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.110 port 48305 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.20  sec  58.5 MBytes  48.1 Mbits/sec   52             sender
    [  5]   0.00-10.00  sec  55.5 MBytes  46.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.110 port 40967 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.25 MBytes  35.6 Mbits/sec    0    208 KBytes       
    [  5]   1.00-2.00   sec  3.75 MBytes  31.5 Mbits/sec    0    273 KBytes       
    [  5]   2.00-3.00   sec  3.12 MBytes  26.2 Mbits/sec    0    314 KBytes       
    [  5]   3.00-4.00   sec  4.00 MBytes  33.6 Mbits/sec    0    339 KBytes       
    [  5]   4.00-5.00   sec  3.00 MBytes  25.2 Mbits/sec    0    355 KBytes       
    [  5]   5.00-6.00   sec  3.75 MBytes  31.5 Mbits/sec    0    358 KBytes       
    [  5]   6.00-7.00   sec  3.00 MBytes  25.2 Mbits/sec    0    358 KBytes       
    [  5]   7.00-8.00   sec  3.75 MBytes  31.5 Mbits/sec    0    358 KBytes       
    [  5]   8.00-9.00   sec  3.25 MBytes  27.3 Mbits/sec    0    387 KBytes       
    [  5]   9.00-10.00  sec  2.38 MBytes  19.9 Mbits/sec    0    387 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  34.2 MBytes  28.7 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  32.9 MBytes  27.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 85722 bytes (308 packets)
    TX: 51703 bytes (205 packets)
    signal: -36 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">36.6</span> Mbits/sec | <span style="font-size: 1.5rem;">47.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 41613 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.03 MBytes  50.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.04 MBytes  42.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.14 MBytes  34.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.04 MBytes  33.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.10 MBytes  17.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.48 MBytes  20.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.88 MBytes  32.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.69 MBytes  31.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.46 MBytes  37.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.46 MBytes  37.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.08  sec  44.0 MBytes  36.6 Mbits/sec   38             sender
    [  5]   0.00-10.00  sec  40.3 MBytes  33.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 45499 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.14 MBytes  51.5 Mbits/sec    0    372 KBytes       
    [  5]   1.00-2.00   sec  5.59 MBytes  46.9 Mbits/sec    0    543 KBytes       
    [  5]   2.00-3.00   sec  5.10 MBytes  42.7 Mbits/sec    0    543 KBytes       
    [  5]   3.00-4.00   sec  5.59 MBytes  46.9 Mbits/sec    0    543 KBytes       
    [  5]   4.00-5.00   sec  5.72 MBytes  48.0 Mbits/sec    0    543 KBytes       
    [  5]   5.00-6.00   sec  5.97 MBytes  50.0 Mbits/sec    0    571 KBytes       
    [  5]   6.00-7.00   sec  5.59 MBytes  46.9 Mbits/sec    0    571 KBytes       
    [  5]   7.00-8.00   sec  5.59 MBytes  46.9 Mbits/sec    0    571 KBytes       
    [  5]   8.00-9.00   sec  5.59 MBytes  46.9 Mbits/sec    0    571 KBytes       
    [  5]   9.00-10.00  sec  5.59 MBytes  46.9 Mbits/sec    0    571 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  56.5 MBytes  47.4 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  55.1 MBytes  46.0 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">34.3</span> Mbits/sec | <span style="font-size: 1.5rem;">45.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.109 port 38923 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.75 MBytes  31.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.38 MBytes  36.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.17  sec  41.6 MBytes  34.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  38.8 MBytes  32.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.109 port 53447 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.38 MBytes  53.4 Mbits/sec    0    257 KBytes       
    [  5]   1.00-2.00   sec  5.38 MBytes  45.1 Mbits/sec    0    365 KBytes       
    [  5]   2.00-3.00   sec  5.50 MBytes  46.2 Mbits/sec    0    440 KBytes       
    [  5]   3.00-4.00   sec  5.50 MBytes  46.1 Mbits/sec    0    498 KBytes       
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec    0    523 KBytes       
    [  5]   5.00-6.00   sec  5.25 MBytes  44.0 Mbits/sec    0    523 KBytes       
    [  5]   6.00-7.00   sec  5.38 MBytes  45.1 Mbits/sec    0    523 KBytes       
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec    0    523 KBytes       
    [  5]   8.00-9.00   sec  5.25 MBytes  44.1 Mbits/sec    0    523 KBytes       
    [  5]   9.00-10.00  sec  5.38 MBytes  45.1 Mbits/sec    0    588 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  54.4 MBytes  45.6 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  51.4 MBytes  43.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 83111 bytes (350 packets)
    TX: 58717 bytes (225 packets)
    signal: -48 dBm
    rx bitrate: 52.0 MBit/s MCS 5
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">2.08</span> Mbits/sec | <span style="font-size: 1.5rem;">15.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 42067 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   478 KBytes  3.92 Mbits/sec                  
    [  5]   1.00-2.00   sec  99.0 KBytes   811 Kbits/sec                  
    [  5]   2.00-3.00   sec  91.9 KBytes   753 Kbits/sec                  
    [  5]   3.00-4.00   sec  84.8 KBytes   695 Kbits/sec                  
    [  5]   4.00-5.00   sec  93.3 KBytes   765 Kbits/sec                  
    [  5]   5.00-6.00   sec  86.3 KBytes   707 Kbits/sec                  
    [  5]   6.00-7.00   sec  93.3 KBytes   765 Kbits/sec                  
    [  5]   7.00-8.00   sec  91.9 KBytes   753 Kbits/sec                  
    [  5]   8.00-9.00   sec  87.7 KBytes   718 Kbits/sec                  
    [  5]   9.00-10.00  sec  97.6 KBytes   799 Kbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.06  sec  2.50 MBytes  2.08 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec  1.27 MBytes  1.07 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 54741 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.98 MBytes  16.6 Mbits/sec    0    140 KBytes       
    [  5]   1.00-2.00   sec  1.93 MBytes  16.2 Mbits/sec    0    211 KBytes       
    [  5]   2.00-3.00   sec  1.55 MBytes  13.0 Mbits/sec    0    270 KBytes       
    [  5]   3.00-4.00   sec  1.93 MBytes  16.2 Mbits/sec    0    314 KBytes       
    [  5]   4.00-5.00   sec  1.37 MBytes  11.5 Mbits/sec    0    341 KBytes       
    [  5]   5.00-6.00   sec  1.43 MBytes  12.0 Mbits/sec    0    375 KBytes       
    [  5]   6.00-7.00   sec  2.42 MBytes  20.3 Mbits/sec    0    426 KBytes       
    [  5]   7.00-8.00   sec  1.80 MBytes  15.1 Mbits/sec    0    452 KBytes       
    [  5]   8.00-9.00   sec  1.86 MBytes  15.6 Mbits/sec    0    452 KBytes       
    [  5]   9.00-10.00  sec  2.11 MBytes  17.7 Mbits/sec    0    501 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  18.4 MBytes  15.4 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  15.9 MBytes  13.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 1747456873 bytes (1445198 packets)
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
