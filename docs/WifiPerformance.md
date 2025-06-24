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
**Test Date:** [2025-06-24 19:12 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15858530686)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">46.4</span> Mbits/sec | <span style="font-size: 1.5rem;">54.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.129 port 52933 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.21 MBytes  43.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.22 MBytes  43.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.22 MBytes  43.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.13 MBytes  43.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.20 MBytes  43.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.10 MBytes  42.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.36 MBytes  44.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.34 MBytes  44.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.28 MBytes  44.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  55.4 MBytes  46.4 Mbits/sec   12             sender
    [  5]   0.00-10.00  sec  51.7 MBytes  43.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.129 port 58007 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.50 MBytes  62.9 Mbits/sec    0    358 KBytes       
    [  5]   1.00-2.00   sec  6.75 MBytes  56.7 Mbits/sec    0    629 KBytes       
    [  5]   2.00-3.00   sec  6.25 MBytes  52.4 Mbits/sec    0    752 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0    892 KBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    0    928 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.02 MBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.21 MBytes       
    [  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.21 MBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.28 MBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.43 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  65.5 MBytes  54.9 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  62.4 MBytes  52.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 145333 bytes (398 packets)
    TX: 82833 bytes (508 packets)
    signal: -27 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">79.9</span> Mbits/sec | <span style="font-size: 1.5rem;">95.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 52319 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.10 MBytes  76.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.69 MBytes  72.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.13 MBytes  76.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.93 MBytes  74.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  9.13 MBytes  76.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  9.22 MBytes  77.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  9.16 MBytes  76.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  9.62 MBytes  80.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  9.80 MBytes  82.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.39 MBytes  78.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  95.4 MBytes  79.9 Mbits/sec   39             sender
    [  5]   0.00-10.00  sec  92.2 MBytes  77.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 34851 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  11.0 MBytes  92.7 Mbits/sec    0    409 KBytes       
    [  5]   1.00-2.00   sec  11.3 MBytes  94.9 Mbits/sec    0    553 KBytes       
    [  5]   2.00-3.00   sec  12.1 MBytes   102 Mbits/sec    0    646 KBytes       
    [  5]   3.00-4.00   sec  11.0 MBytes  92.3 Mbits/sec    0    677 KBytes       
    [  5]   4.00-5.00   sec  11.9 MBytes   100 Mbits/sec    0    757 KBytes       
    [  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0    757 KBytes       
    [  5]   6.00-7.00   sec  11.5 MBytes  96.4 Mbits/sec    0    757 KBytes       
    [  5]   7.00-8.00   sec  11.8 MBytes  99.0 Mbits/sec    0    796 KBytes       
    [  5]   8.00-9.00   sec  10.6 MBytes  88.6 Mbits/sec    0    796 KBytes       
    [  5]   9.00-10.00  sec  11.5 MBytes  96.4 Mbits/sec    0    796 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   114 MBytes  95.6 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   112 MBytes  94.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 129965 bytes (550 packets)
    TX: 60364 bytes (244 packets)
    signal: -33 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">90.0</span> Mbits/sec | <span style="font-size: 1.5rem;">73.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 41029 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.62 MBytes  80.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.4 MBytes  87.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.9 MBytes  91.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.0 MBytes  92.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  10.8 MBytes  90.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   107 MBytes  90.0 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   107 MBytes  89.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 57913 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.88 MBytes  82.7 Mbits/sec    0    491 KBytes       
    [  5]   1.00-2.00   sec  8.75 MBytes  73.4 Mbits/sec    0    634 KBytes       
    [  5]   2.00-3.00   sec  10.4 MBytes  87.0 Mbits/sec    0    641 KBytes       
    [  5]   3.00-4.00   sec  8.25 MBytes  69.2 Mbits/sec    0    669 KBytes       
    [  5]   4.00-5.00   sec  8.25 MBytes  69.2 Mbits/sec    0    704 KBytes       
    [  5]   5.00-6.00   sec  8.38 MBytes  70.3 Mbits/sec    0    745 KBytes       
    [  5]   6.00-7.00   sec  8.25 MBytes  69.2 Mbits/sec    0    745 KBytes       
    [  5]   7.00-8.00   sec  8.38 MBytes  70.3 Mbits/sec    0    785 KBytes       
    [  5]   8.00-9.00   sec  8.50 MBytes  71.3 Mbits/sec    0    785 KBytes       
    [  5]   9.00-10.00  sec  8.38 MBytes  70.2 Mbits/sec    0    785 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  87.4 MBytes  73.3 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  84.1 MBytes  70.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 177296 bytes (443 packets)
    TX: 91012 bytes (478 packets)
    signal: -38 dBm
    rx bitrate: 130.0 MBit/s MCS 15
    tx bitrate: 144.4 MBit/s MCS 15 short GI
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">155</span> Mbits/sec | <span style="font-size: 1.5rem;">196</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 56369 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.6 MBytes   131 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   7.00-8.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   9.00-10.00  sec  19.0 MBytes   159 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   185 MBytes   155 Mbits/sec  170             sender
    [  5]   0.00-10.00  sec   182 MBytes   153 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 43987 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  26.6 MBytes   223 Mbits/sec    0    648 KBytes       
    [  5]   1.00-2.00   sec  23.0 MBytes   193 Mbits/sec    0    682 KBytes       
    [  5]   2.00-3.00   sec  24.2 MBytes   203 Mbits/sec    0    716 KBytes       
    [  5]   3.00-4.00   sec  22.9 MBytes   192 Mbits/sec    0    716 KBytes       
    [  5]   4.00-5.00   sec  23.0 MBytes   193 Mbits/sec    0    764 KBytes       
    [  5]   5.00-6.00   sec  24.0 MBytes   201 Mbits/sec    0    858 KBytes       
    [  5]   6.00-7.00   sec  22.9 MBytes   192 Mbits/sec    0    912 KBytes       
    [  5]   7.00-8.00   sec  20.9 MBytes   175 Mbits/sec    0    912 KBytes       
    [  5]   8.00-9.00   sec  22.2 MBytes   187 Mbits/sec    0    912 KBytes       
    [  5]   9.00-10.00  sec  23.6 MBytes   198 Mbits/sec    0    912 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   233 MBytes   196 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   230 MBytes   193 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -36 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">109</span> Mbits/sec | <span style="font-size: 1.5rem;">102</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 49593 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.0 MBytes   101 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   3.00-4.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   6.00-7.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.4 MBytes   112 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   130 MBytes   109 Mbits/sec  414             sender
    [  5]   0.00-10.00  sec   126 MBytes   106 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 59989 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  13.8 MBytes   115 Mbits/sec    0    452 KBytes       
    [  5]   1.00-2.00   sec  12.2 MBytes   103 Mbits/sec    0    636 KBytes       
    [  5]   2.00-3.00   sec  11.4 MBytes  95.4 Mbits/sec    0    737 KBytes       
    [  5]   3.00-4.00   sec  11.8 MBytes  98.6 Mbits/sec    0    773 KBytes       
    [  5]   4.00-5.00   sec  12.9 MBytes   108 Mbits/sec    0    773 KBytes       
    [  5]   5.00-6.00   sec  11.4 MBytes  95.4 Mbits/sec    0    773 KBytes       
    [  5]   6.00-7.00   sec  11.5 MBytes  96.5 Mbits/sec    0    773 KBytes       
    [  5]   7.00-8.00   sec  12.6 MBytes   106 Mbits/sec    0    817 KBytes       
    [  5]   8.00-9.00   sec  12.4 MBytes   104 Mbits/sec    0    863 KBytes       
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec    0    923 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   121 MBytes   102 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   118 MBytes  98.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    signal: -42 dBm
    tx bitrate: 174.0 MBit/s
    ```

#### Realtek 8821CU #1

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">124</span> Mbits/sec | <span style="font-size: 1.5rem;">193</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 36021 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  15.6 MBytes   131 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.2 MBytes   136 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   148 MBytes   124 Mbits/sec    2             sender
    [  5]   0.00-10.00  sec   148 MBytes   124 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 53325 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  29.8 MBytes   249 Mbits/sec    0    783 KBytes       
    [  5]   1.00-2.00   sec  25.0 MBytes   210 Mbits/sec    0    826 KBytes       
    [  5]   2.00-3.00   sec  22.0 MBytes   185 Mbits/sec    0    826 KBytes       
    [  5]   3.00-4.00   sec  22.0 MBytes   185 Mbits/sec    0    826 KBytes       
    [  5]   4.00-5.00   sec  22.4 MBytes   188 Mbits/sec    0    826 KBytes       
    [  5]   5.00-6.00   sec  23.2 MBytes   195 Mbits/sec    0    826 KBytes       
    [  5]   6.00-7.00   sec  22.0 MBytes   185 Mbits/sec    0    826 KBytes       
    [  5]   7.00-8.00   sec  23.5 MBytes   197 Mbits/sec    0    826 KBytes       
    [  5]   8.00-9.00   sec  20.6 MBytes   173 Mbits/sec    0    826 KBytes       
    [  5]   9.00-10.00  sec  19.1 MBytes   160 Mbits/sec    0    826 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   230 MBytes   193 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   227 MBytes   190 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 161879 bytes (304 packets)
    TX: 87275 bytes (440 packets)
    signal: -44 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">178</span> Mbits/sec | <span style="font-size: 1.5rem;">174</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 45905 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.2 MBytes   145 Mbits/sec                  
    [  5]   1.00-2.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   2.00-3.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.8 MBytes   157 Mbits/sec                  
    [  5]   4.00-5.00   sec  21.5 MBytes   180 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   6.00-7.00   sec  26.2 MBytes   220 Mbits/sec                  
    [  5]   7.00-8.00   sec  21.2 MBytes   178 Mbits/sec                  
    [  5]   8.00-9.00   sec  27.0 MBytes   226 Mbits/sec                  
    [  5]   9.00-10.00  sec  25.5 MBytes   214 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   213 MBytes   178 Mbits/sec  319             sender
    [  5]   0.00-10.00  sec   209 MBytes   175 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 43975 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  30.2 MBytes   253 Mbits/sec    0   4.95 MBytes       
    [  5]   1.00-2.00   sec  27.4 MBytes   230 Mbits/sec    0   4.95 MBytes       
    [  5]   2.00-3.00   sec  29.2 MBytes   245 Mbits/sec    0   4.95 MBytes       
    [  5]   3.00-4.00   sec  28.5 MBytes   239 Mbits/sec    0   4.95 MBytes       
    [  5]   4.00-5.00   sec  23.5 MBytes   197 Mbits/sec    0   4.95 MBytes       
    [  5]   5.00-6.00   sec  16.1 MBytes   135 Mbits/sec    0   4.95 MBytes       
    [  5]   6.00-7.00   sec  11.0 MBytes  92.3 Mbits/sec    0   4.95 MBytes       
    [  5]   7.00-8.00   sec  14.2 MBytes   120 Mbits/sec    0   4.95 MBytes       
    [  5]   8.00-9.00   sec  12.4 MBytes   104 Mbits/sec    0   4.95 MBytes       
    [  5]   9.00-10.00  sec  14.4 MBytes   120 Mbits/sec    0   4.95 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   207 MBytes   174 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   204 MBytes   171 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">524</span> Mbits/sec | <span style="font-size: 1.5rem;">316</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 52375 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  69.0 MBytes   579 Mbits/sec                  
    [  5]   1.00-2.00   sec  73.2 MBytes   614 Mbits/sec                  
    [  5]   2.00-3.00   sec  58.2 MBytes   488 Mbits/sec                  
    [  5]   3.00-4.00   sec  60.7 MBytes   509 Mbits/sec                  
    [  5]   4.00-5.00   sec  60.9 MBytes   511 Mbits/sec                  
    [  5]   5.00-6.00   sec  58.3 MBytes   489 Mbits/sec                  
    [  5]   6.00-7.00   sec  58.9 MBytes   494 Mbits/sec                  
    [  5]   7.00-8.00   sec  58.3 MBytes   489 Mbits/sec                  
    [  5]   8.00-9.00   sec  60.7 MBytes   510 Mbits/sec                  
    [  5]   9.00-10.00  sec  63.0 MBytes   528 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   624 MBytes   524 Mbits/sec  516             sender
    [  5]   0.00-10.00  sec   621 MBytes   521 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 42001 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  40.0 MBytes   335 Mbits/sec    0   6.03 MBytes       
    [  5]   1.00-2.00   sec  37.5 MBytes   315 Mbits/sec    0   6.43 MBytes       
    [  5]   2.00-3.00   sec  35.0 MBytes   294 Mbits/sec   78   3.22 MBytes       
    [  5]   3.00-4.00   sec  37.5 MBytes   315 Mbits/sec   75   1.63 MBytes       
    [  5]   4.00-5.00   sec  40.0 MBytes   336 Mbits/sec    0   1.65 MBytes       
    [  5]   5.00-6.00   sec  42.5 MBytes   356 Mbits/sec   95    895 KBytes       
    [  5]   6.00-7.00   sec  40.0 MBytes   336 Mbits/sec    0    957 KBytes       
    [  5]   7.00-8.00   sec  37.5 MBytes   315 Mbits/sec    0   1005 KBytes       
    [  5]   8.00-9.00   sec  31.2 MBytes   262 Mbits/sec    0   1.01 MBytes       
    [  5]   9.00-10.00  sec  35.0 MBytes   294 Mbits/sec    0   1.05 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   376 MBytes   316 Mbits/sec  248             sender
    [  5]   0.00-10.01  sec   373 MBytes   313 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 143539 bytes (516 packets)
    TX: 57746 bytes (209 packets)
    signal: -33 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    
    ```
### AX

#### Ampak 6275P

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AP6275P.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.149, 6.12.33-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AP6275P</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">348</span> Mbits/sec | <span style="font-size: 1.5rem;">424</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 48119 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  41.2 MBytes   346 Mbits/sec                  
    [  5]   1.00-2.00   sec  40.1 MBytes   337 Mbits/sec                  
    [  5]   2.00-3.00   sec  42.1 MBytes   353 Mbits/sec                  
    [  5]   3.00-4.00   sec  41.8 MBytes   350 Mbits/sec                  
    [  5]   4.00-5.00   sec  41.6 MBytes   349 Mbits/sec                  
    [  5]   5.00-6.00   sec  40.4 MBytes   339 Mbits/sec                  
    [  5]   6.00-7.00   sec  41.5 MBytes   348 Mbits/sec                  
    [  5]   7.00-8.00   sec  41.3 MBytes   346 Mbits/sec                  
    [  5]   8.00-9.00   sec  40.7 MBytes   341 Mbits/sec                  
    [  5]   9.00-10.00  sec  42.5 MBytes   356 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   415 MBytes   348 Mbits/sec  117             sender
    [  5]   0.00-10.00  sec   413 MBytes   347 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 43337 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  57.2 MBytes   480 Mbits/sec    0   5.25 MBytes       
    [  5]   1.00-2.00   sec  55.0 MBytes   461 Mbits/sec    0   5.25 MBytes       
    [  5]   2.00-3.00   sec  55.0 MBytes   461 Mbits/sec    0   5.25 MBytes       
    [  5]   3.00-4.00   sec  48.8 MBytes   409 Mbits/sec    0   5.25 MBytes       
    [  5]   4.00-5.00   sec  45.0 MBytes   377 Mbits/sec    0   5.25 MBytes       
    [  5]   5.00-6.00   sec  47.5 MBytes   398 Mbits/sec    0   5.25 MBytes       
    [  5]   6.00-7.00   sec  55.0 MBytes   461 Mbits/sec    0   5.25 MBytes       
    [  5]   7.00-8.00   sec  47.5 MBytes   398 Mbits/sec    0   5.25 MBytes       
    [  5]   8.00-9.00   sec  47.5 MBytes   398 Mbits/sec    0   5.25 MBytes       
    [  5]   9.00-10.00  sec  47.5 MBytes   398 Mbits/sec    0   5.25 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   506 MBytes   424 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   505 MBytes   423 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 71102 bytes (135 packets)
    TX: 54178 bytes (203 packets)
    signal: -63 dBm
    rx bitrate: 720.5 MBit/s
    tx bitrate: 648.5 MBit/s
    
    ```

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">111</span> Mbits/sec | <span style="font-size: 1.5rem;">145</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 38089 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.1 MBytes   110 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   132 MBytes   111 Mbits/sec   86             sender
    [  5]   0.00-10.00  sec   130 MBytes   109 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 34047 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.9 MBytes   158 Mbits/sec    0    550 KBytes       
    [  5]   1.00-2.00   sec  17.0 MBytes   143 Mbits/sec    0    636 KBytes       
    [  5]   2.00-3.00   sec  17.9 MBytes   150 Mbits/sec    0    747 KBytes       
    [  5]   3.00-4.00   sec  16.6 MBytes   140 Mbits/sec    0    747 KBytes       
    [  5]   4.00-5.00   sec  16.9 MBytes   142 Mbits/sec    0    747 KBytes       
    [  5]   5.00-6.00   sec  16.9 MBytes   142 Mbits/sec    0    792 KBytes       
    [  5]   6.00-7.00   sec  18.1 MBytes   152 Mbits/sec    0    872 KBytes       
    [  5]   7.00-8.00   sec  16.9 MBytes   142 Mbits/sec    0    918 KBytes       
    [  5]   8.00-9.00   sec  16.6 MBytes   140 Mbits/sec    0    918 KBytes       
    [  5]   9.00-10.00  sec  17.2 MBytes   144 Mbits/sec    0    966 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   173 MBytes   145 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   170 MBytes   143 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 56547 bytes (224 packets)
    TX: 52451 bytes (207 packets)
    signal: -36 dBm
    rx bitrate: 960.7 MBit/s 80MHz HE-MCS 9 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">166</span> Mbits/sec | <span style="font-size: 1.5rem;">149</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.125 port 60111 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  19.6 MBytes   164 Mbits/sec                  
    [  5]   1.00-2.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.9 MBytes   158 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   5.00-6.00   sec  20.0 MBytes   168 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.5 MBytes   164 Mbits/sec                  
    [  5]   9.00-10.00  sec  19.8 MBytes   166 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   198 MBytes   166 Mbits/sec  166             sender
    [  5]   0.00-10.00  sec   194 MBytes   163 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.125 port 37707 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  21.6 MBytes   181 Mbits/sec    0   3.79 MBytes       
    [  5]   1.00-2.00   sec  16.5 MBytes   138 Mbits/sec    0   3.79 MBytes       
    [  5]   2.00-3.00   sec  18.4 MBytes   154 Mbits/sec    0   3.79 MBytes       
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec    0   3.93 MBytes       
    [  5]   4.00-5.00   sec  15.8 MBytes   132 Mbits/sec    0   3.93 MBytes       
    [  5]   5.00-6.00   sec  16.4 MBytes   137 Mbits/sec    0   3.93 MBytes       
    [  5]   6.00-7.00   sec  16.2 MBytes   136 Mbits/sec    0   3.93 MBytes       
    [  5]   7.00-8.00   sec  18.6 MBytes   156 Mbits/sec    0   3.93 MBytes       
    [  5]   8.00-9.00   sec  17.6 MBytes   148 Mbits/sec    0   3.93 MBytes       
    [  5]   9.00-10.00  sec  18.4 MBytes   154 Mbits/sec    0   3.93 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   178 MBytes   149 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec   175 MBytes   146 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 41149 bytes (169 packets)
    TX: 54665 bytes (195 packets)
    signal: -27 dBm
    rx bitrate: 286.7 MBit/s HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 58.5 MBit/s HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">70.3</span> Mbits/sec | <span style="font-size: 1.5rem;">64.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 41953 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.62 MBytes  55.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  9.50 MBytes  79.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.50 MBytes  62.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  7.00 MBytes  58.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  8.12 MBytes  68.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  8.00 MBytes  67.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  8.38 MBytes  70.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  9.12 MBytes  76.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  8.12 MBytes  68.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  7.88 MBytes  66.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  83.9 MBytes  70.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  80.2 MBytes  67.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 47745 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.50 MBytes  54.5 Mbits/sec    0    257 KBytes       
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec    0    396 KBytes       
    [  5]   2.00-3.00   sec  8.50 MBytes  71.3 Mbits/sec    0    479 KBytes       
    [  5]   3.00-4.00   sec  6.88 MBytes  57.7 Mbits/sec    0    479 KBytes       
    [  5]   4.00-5.00   sec  8.38 MBytes  70.3 Mbits/sec    0    543 KBytes       
    [  5]   5.00-6.00   sec  7.88 MBytes  66.1 Mbits/sec    0    543 KBytes       
    [  5]   6.00-7.00   sec  8.00 MBytes  67.1 Mbits/sec    0    609 KBytes       
    [  5]   7.00-8.00   sec  8.00 MBytes  67.1 Mbits/sec    0    643 KBytes       
    [  5]   8.00-9.00   sec  6.62 MBytes  55.6 Mbits/sec    0    643 KBytes       
    [  5]   9.00-10.00  sec  8.12 MBytes  68.1 Mbits/sec    0    683 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  76.2 MBytes  64.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  73.2 MBytes  61.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 95175 bytes (415 packets)
    TX: 55933 bytes (239 packets)
    signal: -23 dBm
    rx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    tx bitrate: 270.0 MBit/s MCS 15 40MHz
    ```

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">42.6</span> Mbits/sec | <span style="font-size: 1.5rem;">35.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.124 port 37163 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.60 MBytes  38.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.91 MBytes  41.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.95 MBytes  41.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.99 MBytes  41.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.13 MBytes  43.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.86 MBytes  40.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.46 MBytes  45.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.28 MBytes  44.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.26 MBytes  44.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.81 MBytes  40.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.42  sec  52.9 MBytes  42.6 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  50.3 MBytes  42.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.124 port 55529 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.45 MBytes  37.3 Mbits/sec    0    216 KBytes       
    [  5]   1.00-2.00   sec  4.54 MBytes  38.1 Mbits/sec    0    229 KBytes       
    [  5]   2.00-3.00   sec  4.10 MBytes  34.4 Mbits/sec    0    229 KBytes       
    [  5]   3.00-4.00   sec  4.16 MBytes  34.9 Mbits/sec    0    229 KBytes       
    [  5]   4.00-5.00   sec  4.23 MBytes  35.4 Mbits/sec    0    229 KBytes       
    [  5]   5.00-6.00   sec  4.29 MBytes  36.0 Mbits/sec    0    284 KBytes       
    [  5]   6.00-7.00   sec  4.04 MBytes  33.9 Mbits/sec    0    284 KBytes       
    [  5]   7.00-8.00   sec  4.29 MBytes  36.0 Mbits/sec    0    395 KBytes       
    [  5]   8.00-9.00   sec  4.35 MBytes  36.5 Mbits/sec    0    395 KBytes       
    [  5]   9.00-10.00  sec  4.35 MBytes  36.5 Mbits/sec    0    395 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  42.8 MBytes  35.9 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  41.6 MBytes  34.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 61520 bytes (197 packets)
    TX: 59257 bytes (244 packets)
    signal: -56 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">48.7</span> Mbits/sec | <span style="font-size: 1.5rem;">56.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.123 port 38251 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.29 MBytes  52.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.45 MBytes  45.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.36 MBytes  53.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.36 MBytes  53.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.57 MBytes  46.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.64 MBytes  47.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.48 MBytes  46.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.48 MBytes  46.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.09 MBytes  42.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.29 MBytes  44.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.47  sec  60.8 MBytes  48.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  57.0 MBytes  47.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.123 port 42883 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.00 MBytes  58.7 Mbits/sec    0    232 KBytes       
    [  5]   1.00-2.00   sec  6.59 MBytes  55.3 Mbits/sec    0    246 KBytes       
    [  5]   2.00-3.00   sec  6.90 MBytes  57.9 Mbits/sec    0    277 KBytes       
    [  5]   3.00-4.00   sec  5.59 MBytes  46.9 Mbits/sec    0    277 KBytes       
    [  5]   4.00-5.00   sec  8.14 MBytes  68.3 Mbits/sec    0    382 KBytes       
    [  5]   5.00-6.00   sec  6.52 MBytes  54.7 Mbits/sec    0    399 KBytes       
    [  5]   6.00-7.00   sec  6.46 MBytes  54.2 Mbits/sec    0    399 KBytes       
    [  5]   7.00-8.00   sec  6.65 MBytes  55.8 Mbits/sec    0    399 KBytes       
    [  5]   8.00-9.00   sec  6.71 MBytes  56.3 Mbits/sec    0    399 KBytes       
    [  5]   9.00-10.00  sec  6.59 MBytes  55.2 Mbits/sec    0    399 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  67.1 MBytes  56.3 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  65.1 MBytes  54.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 60726 bytes (198 packets)
    TX: 54855 bytes (227 packets)
    signal: -50 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">15.8</span> Mbits/sec | <span style="font-size: 1.5rem;">16.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 37141 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.12 MBytes  9.43 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.62 MBytes  13.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.38 MBytes  11.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.88 MBytes  15.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  1.75 MBytes  14.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  1.00 MBytes  8.39 Mbits/sec                  
    [  5]   8.00-9.00   sec  1.75 MBytes  14.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.75 MBytes  14.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  18.9 MBytes  15.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  16.2 MBytes  13.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 39215 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.75 MBytes  14.7 Mbits/sec    0    126 KBytes       
    [  5]   1.00-2.00   sec  1.00 MBytes  8.39 Mbits/sec    0    170 KBytes       
    [  5]   2.00-3.00   sec  1.12 MBytes  9.43 Mbits/sec    2   91.9 KBytes       
    [  5]   3.00-4.00   sec  1.88 MBytes  15.7 Mbits/sec    0    103 KBytes       
    [  5]   4.00-5.00   sec  2.00 MBytes  16.8 Mbits/sec    0    115 KBytes       
    [  5]   5.00-6.00   sec  2.00 MBytes  16.8 Mbits/sec    0   46.7 KBytes       
    [  5]   6.00-7.00   sec  2.62 MBytes  22.0 Mbits/sec    1    112 KBytes       
    [  5]   7.00-8.00   sec  1.50 MBytes  12.6 Mbits/sec    0    124 KBytes       
    [  5]   8.00-9.00   sec  3.00 MBytes  25.1 Mbits/sec    0    133 KBytes       
    [  5]   9.00-10.00  sec  2.25 MBytes  18.9 Mbits/sec    0    143 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  19.1 MBytes  16.0 Mbits/sec    3             sender
    [  5]   0.00-10.01  sec  18.1 MBytes  15.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 101321 bytes (431 packets)
    TX: 56028 bytes (213 packets)
    signal: -31 dBm
    rx bitrate: 65.0 MBit/s MCS 6 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">65.2</span> Mbits/sec | <span style="font-size: 1.5rem;">47.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 47009 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.38 MBytes  36.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  7.50 MBytes  62.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  8.50 MBytes  71.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  8.12 MBytes  68.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  8.25 MBytes  69.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  7.38 MBytes  61.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  77.9 MBytes  65.2 Mbits/sec   20             sender
    [  5]   0.00-10.00  sec  75.1 MBytes  63.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 56165 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.38 MBytes  53.4 Mbits/sec    8    151 KBytes       
    [  5]   1.00-2.00   sec  5.25 MBytes  44.0 Mbits/sec    0    181 KBytes       
    [  5]   2.00-3.00   sec  5.12 MBytes  43.0 Mbits/sec    8    143 KBytes       
    [  5]   3.00-4.00   sec  6.12 MBytes  51.4 Mbits/sec    8    126 KBytes       
    [  5]   4.00-5.00   sec  4.75 MBytes  39.8 Mbits/sec    0    148 KBytes       
    [  5]   5.00-6.00   sec  5.75 MBytes  48.2 Mbits/sec   16    116 KBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec   14    102 KBytes       
    [  5]   7.00-8.00   sec  4.88 MBytes  40.9 Mbits/sec    0    133 KBytes       
    [  5]   8.00-9.00   sec  3.75 MBytes  31.5 Mbits/sec   16   80.6 KBytes       
    [  5]   9.00-10.00  sec  7.00 MBytes  58.7 Mbits/sec    0    129 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  56.5 MBytes  47.4 Mbits/sec   70             sender
    [  5]   0.00-10.00  sec  55.4 MBytes  46.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 95692 bytes (400 packets)
    TX: 58313 bytes (276 packets)
    signal: -30 dBm
    rx bitrate: 162.0 MBit/s MCS 12 40MHz
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">41.3</span> Mbits/sec | <span style="font-size: 1.5rem;">26.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 60323 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.50 MBytes  37.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.88 MBytes  40.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.62 MBytes  38.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.45  sec  51.5 MBytes  41.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  48.2 MBytes  40.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 48217 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.62 MBytes  30.4 Mbits/sec    0    184 KBytes       
    [  5]   1.00-2.00   sec  3.38 MBytes  28.3 Mbits/sec    0    243 KBytes       
    [  5]   2.00-3.00   sec  3.25 MBytes  27.3 Mbits/sec    0    276 KBytes       
    [  5]   3.00-4.00   sec  3.00 MBytes  25.2 Mbits/sec    0    293 KBytes       
    [  5]   4.00-5.00   sec  3.25 MBytes  27.3 Mbits/sec    0    308 KBytes       
    [  5]   5.00-6.00   sec  3.12 MBytes  26.2 Mbits/sec    0    308 KBytes       
    [  5]   6.00-7.00   sec  3.25 MBytes  27.3 Mbits/sec    0    308 KBytes       
    [  5]   7.00-8.00   sec  2.62 MBytes  22.0 Mbits/sec    0    322 KBytes       
    [  5]   8.00-9.00   sec  2.75 MBytes  23.1 Mbits/sec    0    322 KBytes       
    [  5]   9.00-10.00  sec  3.38 MBytes  28.3 Mbits/sec    0    322 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  31.6 MBytes  26.5 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  29.9 MBytes  25.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 99361 bytes (365 packets)
    TX: 59007 bytes (223 packets)
    signal: -38 dBm
    rx bitrate: 58.5 MBit/s MCS 6
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">40.3</span> Mbits/sec | <span style="font-size: 1.5rem;">27.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.122 port 37755 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.12 MBytes  42.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.68 MBytes  30.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.77 MBytes  40.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.45 MBytes  29.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.61 MBytes  13.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.02 MBytes  33.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.64 MBytes  47.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.56 MBytes  46.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.62 MBytes  47.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.91 MBytes  49.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.04  sec  48.2 MBytes  40.3 Mbits/sec   26             sender
    [  5]   0.00-10.00  sec  45.4 MBytes  38.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.122 port 42385 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.97 MBytes  50.1 Mbits/sec    0    298 KBytes       
    [  5]   1.00-2.00   sec  4.91 MBytes  41.2 Mbits/sec    0    499 KBytes       
    [  5]   2.00-3.00   sec  3.17 MBytes  26.6 Mbits/sec    0    650 KBytes       
    [  5]   3.00-4.00   sec  3.42 MBytes  28.7 Mbits/sec    0    752 KBytes       
    [  5]   4.00-5.00   sec  2.61 MBytes  21.9 Mbits/sec    0    800 KBytes       
    [  5]   5.00-6.00   sec  1.74 MBytes  14.6 Mbits/sec    0    830 KBytes       
    [  5]   6.00-7.00   sec  1.86 MBytes  15.6 Mbits/sec    0    923 KBytes       
    [  5]   7.00-8.00   sec  3.17 MBytes  26.6 Mbits/sec    0   1.01 MBytes       
    [  5]   8.00-9.00   sec  3.48 MBytes  29.2 Mbits/sec    0   1.03 MBytes       
    [  5]   9.00-10.00  sec  2.30 MBytes  19.3 Mbits/sec    0   1.03 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  32.6 MBytes  27.4 Mbits/sec    0             sender
    [  5]   0.00-10.15  sec  30.4 MBytes  25.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.269, 6.12.34-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">29.2</span> Mbits/sec | <span style="font-size: 1.5rem;">41.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 34601 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.12 MBytes  26.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.25 MBytes  18.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.38 MBytes  19.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.75 MBytes  31.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  34.9 MBytes  29.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  32.2 MBytes  27.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 35777 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.00 MBytes  50.3 Mbits/sec    0    287 KBytes       
    [  5]   1.00-2.00   sec  4.75 MBytes  39.8 Mbits/sec    0    335 KBytes       
    [  5]   2.00-3.00   sec  5.38 MBytes  45.1 Mbits/sec    0    409 KBytes       
    [  5]   3.00-4.00   sec  4.00 MBytes  33.6 Mbits/sec    0    409 KBytes       
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec    0    409 KBytes       
    [  5]   5.00-6.00   sec  4.88 MBytes  40.9 Mbits/sec    0    409 KBytes       
    [  5]   6.00-7.00   sec  4.88 MBytes  40.9 Mbits/sec    0    409 KBytes       
    [  5]   7.00-8.00   sec  5.12 MBytes  43.0 Mbits/sec    0    428 KBytes       
    [  5]   8.00-9.00   sec  4.50 MBytes  37.7 Mbits/sec    0    486 KBytes       
    [  5]   9.00-10.00  sec  5.25 MBytes  44.0 Mbits/sec    0    601 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  49.8 MBytes  41.7 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  47.4 MBytes  39.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 85834 bytes (333 packets)
    TX: 62779 bytes (243 packets)
    signal: -48 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek RT3070

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL2870.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.265, 6.12.34-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL2870</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">10.6</span> Mbits/sec | <span style="font-size: 1.5rem;">29.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 39705 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   896 KBytes  7.33 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.00 MBytes  8.39 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.00 MBytes  8.39 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.00 MBytes  8.39 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.12 MBytes  9.44 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.00 MBytes  8.39 Mbits/sec                  
    [  5]   6.00-7.00   sec  1.00 MBytes  8.39 Mbits/sec                  
    [  5]   7.00-8.00   sec   896 KBytes  7.34 Mbits/sec                  
    [  5]   8.00-9.00   sec  1.00 MBytes  8.39 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.00 MBytes  8.39 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  12.6 MBytes  10.6 Mbits/sec    0            sender
    [  5]   0.00-10.00  sec  9.88 MBytes  8.28 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 50039 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.88 MBytes  49.2 Mbits/sec    0    846 KBytes       
    [  5]   1.00-2.00   sec  2.88 MBytes  24.1 Mbits/sec    1    619 KBytes       
    [  5]   2.00-3.00   sec  2.88 MBytes  24.1 Mbits/sec    0    624 KBytes       
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec    0    628 KBytes       
    [  5]   4.00-5.00   sec  4.38 MBytes  36.7 Mbits/sec    0    632 KBytes       
    [  5]   5.00-6.00   sec  1.38 MBytes  11.5 Mbits/sec    0    636 KBytes       
    [  5]   6.00-7.00   sec  4.12 MBytes  34.6 Mbits/sec    0    636 KBytes       
    [  5]   7.00-8.00   sec  2.75 MBytes  23.1 Mbits/sec    0    638 KBytes       
    [  5]   8.00-9.00   sec  4.12 MBytes  34.6 Mbits/sec    0    641 KBytes       
    [  5]   9.00-10.00  sec  2.75 MBytes  23.0 Mbits/sec    0    643 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  35.4 MBytes  29.7 Mbits/sec    1            sender
    [  5]   0.00-10.01  sec  32.0 MBytes  26.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 111649 bytes (478 packets)
    TX: 58619 bytes (232 packets)
    signal: -51 dBm
    rx bitrate: 39.0 MBit/s MCS 4
    tx bitrate: 57.8 MBit/s MCS 5 short GI
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.154, 6.12.30-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">106</span> Mbits/sec | <span style="font-size: 1.5rem;">117</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.121 port 48855 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.8 MBytes   108 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.4 MBytes   104 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.8 MBytes  98.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.9 MBytes   100 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.2 MBytes  94.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.1 MBytes  93.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  10.7 MBytes  89.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   126 MBytes   106 Mbits/sec   57             sender
    [  5]   0.00-10.00  sec   122 MBytes   103 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.121 port 38873 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  16.2 MBytes   136 Mbits/sec    0    544 KBytes       
    [  5]   1.00-2.00   sec  14.6 MBytes   122 Mbits/sec    1    426 KBytes       
    [  5]   2.00-3.00   sec  14.7 MBytes   124 Mbits/sec    2    228 KBytes       
    [  5]   3.00-4.00   sec  14.5 MBytes   122 Mbits/sec    0    272 KBytes       
    [  5]   4.00-5.00   sec  14.9 MBytes   125 Mbits/sec    2    223 KBytes       
    [  5]   5.00-6.00   sec  13.7 MBytes   115 Mbits/sec    1    209 KBytes       
    [  5]   6.00-7.00   sec  13.7 MBytes   115 Mbits/sec    0    256 KBytes       
    [  5]   7.00-8.00   sec  12.4 MBytes   104 Mbits/sec    0    287 KBytes       
    [  5]   8.00-9.00   sec  12.4 MBytes   104 Mbits/sec    1    225 KBytes       
    [  5]   9.00-10.00  sec  12.5 MBytes   105 Mbits/sec    1    187 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   140 MBytes   117 Mbits/sec    8             sender
    [  5]   0.00-10.01  sec   137 MBytes   115 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 253338307 bytes (218864 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">17.8</span> Mbits/sec | <span style="font-size: 1.5rem;">11.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.115 port 36769 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.37 MBytes  11.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.44 MBytes  12.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.46 MBytes  12.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.84 MBytes  15.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.95 MBytes  16.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.87 MBytes  15.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.18 MBytes  18.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.30 MBytes  19.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.35 MBytes  19.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.23 MBytes  18.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.14  sec  21.5 MBytes  17.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  19.0 MBytes  15.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.115 port 46153 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.49 MBytes  12.5 Mbits/sec    2   50.9 KBytes       
    [  5]   1.00-2.00   sec  1.33 MBytes  11.2 Mbits/sec    3   53.7 KBytes       
    [  5]   2.00-3.00   sec  1.23 MBytes  10.3 Mbits/sec    3   48.1 KBytes       
    [  5]   3.00-4.00   sec  1.49 MBytes  12.5 Mbits/sec    0   66.5 KBytes       
    [  5]   4.00-5.00   sec  1.37 MBytes  11.5 Mbits/sec    0   77.8 KBytes       
    [  5]   5.00-6.00   sec  1.37 MBytes  11.5 Mbits/sec    0   84.8 KBytes       
    [  5]   6.00-7.00   sec  1.24 MBytes  10.4 Mbits/sec    0   91.9 KBytes       
    [  5]   7.00-8.00   sec  1.37 MBytes  11.5 Mbits/sec    0   96.2 KBytes       
    [  5]   8.00-9.00   sec  1.24 MBytes  10.4 Mbits/sec    1   50.9 KBytes       
    [  5]   9.00-10.00  sec  1.37 MBytes  11.5 Mbits/sec    0   76.4 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  13.5 MBytes  11.3 Mbits/sec    9             sender
    [  5]   0.00-10.04  sec  13.2 MBytes  11.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 51129 bytes (158 packets)
    TX: 62496 bytes (246 packets)
    signal: -30 dBm
    rx bitrate: 6.0 MBit/s
    tx bitrate: 65.0 MBit/s MCS 7
    
    ```

## Failed Devices

| Commercial Name | Chip | Class |
|:-----|:--------|:------|
| AIC8800 | AIC8800 | AX |
| Atheros AR9271 | AR9271 | N |
| BrosTrend 1800 | RTL8852AU | AXE3000 |
| Mediatek MT7925 | MT7925 | AX |
| Mediatek MT7925E #1 | MT7925E | AX |
| Mediatek MT7925E #2 | MT7925E | AX |
| Ralink MT7601U | MT7601U |  |
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
