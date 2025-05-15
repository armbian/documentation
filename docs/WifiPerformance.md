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
**Test Date:** [2025-05-15 22:31 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15055899754)
### AC

#### BCM4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">51.1</span> Mbits/sec | <span style="font-size: 1.5rem;">59.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 49231 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.63 MBytes  47.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.81 MBytes  48.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.70 MBytes  47.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.66 MBytes  47.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.68 MBytes  47.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.84 MBytes  49.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.68 MBytes  47.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.81 MBytes  48.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.83 MBytes  48.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.74 MBytes  48.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  61.0 MBytes  51.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  57.4 MBytes  48.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 51401 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.38 MBytes  70.3 Mbits/sec    0    431 KBytes       
    [  5]   1.00-2.00   sec  7.75 MBytes  65.0 Mbits/sec    0    641 KBytes       
    [  5]   2.00-3.00   sec  6.25 MBytes  52.4 Mbits/sec    0    737 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0    901 KBytes       
    [  5]   4.00-5.00   sec  7.50 MBytes  62.9 Mbits/sec    0    974 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0    974 KBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.01 MBytes       
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.06 MBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.06 MBytes       
    [  5]   9.00-10.00  sec  7.50 MBytes  62.9 Mbits/sec    0   1.13 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  71.1 MBytes  59.7 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  67.8 MBytes  56.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 37373 bytes (143 packets)
    TX: 53759 bytes (202 packets)
    signal: -25 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">118</span> Mbits/sec | <span style="font-size: 1.5rem;">107</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 48527 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.2 MBytes   110 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.9 MBytes   117 Mbits/sec                  
    [  5]   3.00-4.00   sec  14.0 MBytes   117 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.0 MBytes   117 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.8 MBytes   116 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec   141 MBytes   118 Mbits/sec   15             sender
    [  5]   0.00-10.00  sec   138 MBytes   116 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 60315 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.9 MBytes   108 Mbits/sec    0    454 KBytes       
    [  5]   1.00-2.00   sec  13.0 MBytes   109 Mbits/sec    0    526 KBytes       
    [  5]   2.00-3.00   sec  12.2 MBytes   102 Mbits/sec    0    590 KBytes       
    [  5]   3.00-4.00   sec  12.6 MBytes   106 Mbits/sec    0    659 KBytes       
    [  5]   4.00-5.00   sec  13.2 MBytes   111 Mbits/sec    0    693 KBytes       
    [  5]   5.00-6.00   sec  13.0 MBytes   109 Mbits/sec    0    740 KBytes       
    [  5]   6.00-7.00   sec  11.8 MBytes  99.0 Mbits/sec    0    740 KBytes       
    [  5]   7.00-8.00   sec  13.5 MBytes   113 Mbits/sec    0    789 KBytes       
    [  5]   8.00-9.00   sec  12.6 MBytes   106 Mbits/sec    0    789 KBytes       
    [  5]   9.00-10.00  sec  12.2 MBytes   103 Mbits/sec    0    789 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   127 MBytes   107 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   126 MBytes   105 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 107744 bytes (470 packets)
    TX: 57816 bytes (228 packets)
    signal: -36 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">52.9</span> Mbits/sec | <span style="font-size: 1.5rem;">63.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.107 port 38165 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.88 MBytes  49.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.38 MBytes  53.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.38 MBytes  53.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.12 MBytes  51.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.25 MBytes  52.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.12 MBytes  51.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.12 MBytes  51.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  63.2 MBytes  52.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  62.5 MBytes  52.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.107 port 43407 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.12 MBytes  68.1 Mbits/sec    0    406 KBytes       
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec    0    577 KBytes       
    [  5]   2.00-3.00   sec  6.88 MBytes  57.7 Mbits/sec    0    738 KBytes       
    [  5]   3.00-4.00   sec  7.00 MBytes  58.7 Mbits/sec    0    824 KBytes       
    [  5]   4.00-5.00   sec  7.00 MBytes  58.7 Mbits/sec    0    870 KBytes       
    [  5]   5.00-6.00   sec  7.12 MBytes  59.8 Mbits/sec    0    930 KBytes       
    [  5]   6.00-7.00   sec  8.50 MBytes  71.3 Mbits/sec    0   1.04 MBytes       
    [  5]   7.00-8.00   sec  8.25 MBytes  69.2 Mbits/sec    0   1.10 MBytes       
    [  5]   8.00-9.00   sec  7.12 MBytes  59.8 Mbits/sec    0   1.10 MBytes       
    [  5]   9.00-10.00  sec  8.38 MBytes  70.2 Mbits/sec    0   1.17 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  75.8 MBytes  63.5 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  72.2 MBytes  60.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 186769 bytes (420 packets)
    TX: 108375 bytes (543 packets)
    signal: -43 dBm
    rx bitrate: 117.0 MBit/s MCS 14
    tx bitrate: 104.0 MBit/s MCS 13
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">190</span> Mbits/sec | <span style="font-size: 1.5rem;">199</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.119 port 33317 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  22.4 MBytes   188 Mbits/sec                  
    [  5]   1.00-2.00   sec  22.4 MBytes   188 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.1 MBytes   194 Mbits/sec                  
    [  5]   3.00-4.00   sec  22.4 MBytes   188 Mbits/sec                  
    [  5]   4.00-5.00   sec  22.4 MBytes   188 Mbits/sec                  
    [  5]   5.00-6.00   sec  22.1 MBytes   186 Mbits/sec                  
    [  5]   6.00-7.00   sec  22.2 MBytes   187 Mbits/sec                  
    [  5]   7.00-8.00   sec  22.5 MBytes   189 Mbits/sec                  
    [  5]   8.00-9.00   sec  22.1 MBytes   186 Mbits/sec                  
    [  5]   9.00-10.00  sec  22.2 MBytes   187 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   227 MBytes   190 Mbits/sec  441             sender
    [  5]   0.00-10.00  sec   224 MBytes   188 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.119 port 59647 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  26.6 MBytes   223 Mbits/sec    0    684 KBytes       
    [  5]   1.00-2.00   sec  22.4 MBytes   188 Mbits/sec    0    724 KBytes       
    [  5]   2.00-3.00   sec  23.4 MBytes   196 Mbits/sec    0    724 KBytes       
    [  5]   3.00-4.00   sec  23.4 MBytes   196 Mbits/sec    0    724 KBytes       
    [  5]   4.00-5.00   sec  23.8 MBytes   199 Mbits/sec    0    857 KBytes       
    [  5]   5.00-6.00   sec  23.5 MBytes   197 Mbits/sec    0    902 KBytes       
    [  5]   6.00-7.00   sec  23.4 MBytes   196 Mbits/sec    0    902 KBytes       
    [  5]   7.00-8.00   sec  23.5 MBytes   197 Mbits/sec    0    959 KBytes       
    [  5]   8.00-9.00   sec  23.5 MBytes   197 Mbits/sec    0    959 KBytes       
    [  5]   9.00-10.00  sec  23.5 MBytes   197 Mbits/sec   38    696 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   237 MBytes   199 Mbits/sec   38             sender
    [  5]   0.00-10.01  sec   234 MBytes   196 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -32 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">179</span> Mbits/sec | <span style="font-size: 1.5rem;">277</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.118 port 55437 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  19.0 MBytes   159 Mbits/sec                  
    [  5]   1.00-2.00   sec  21.2 MBytes   178 Mbits/sec                  
    [  5]   2.00-3.00   sec  21.5 MBytes   180 Mbits/sec                  
    [  5]   3.00-4.00   sec  21.4 MBytes   179 Mbits/sec                  
    [  5]   4.00-5.00   sec  21.6 MBytes   181 Mbits/sec                  
    [  5]   5.00-6.00   sec  21.1 MBytes   177 Mbits/sec                  
    [  5]   6.00-7.00   sec  21.5 MBytes   180 Mbits/sec                  
    [  5]   7.00-8.00   sec  21.2 MBytes   178 Mbits/sec                  
    [  5]   8.00-9.00   sec  21.1 MBytes   177 Mbits/sec                  
    [  5]   9.00-10.00  sec  21.2 MBytes   178 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   214 MBytes   179 Mbits/sec   27             sender
    [  5]   0.00-10.00  sec   211 MBytes   177 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.118 port 59477 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  35.2 MBytes   295 Mbits/sec    0    885 KBytes       
    [  5]   1.00-2.00   sec  33.2 MBytes   279 Mbits/sec    0   1.03 MBytes       
    [  5]   2.00-3.00   sec  32.0 MBytes   268 Mbits/sec    0   1.03 MBytes       
    [  5]   3.00-4.00   sec  33.0 MBytes   277 Mbits/sec    0   1.03 MBytes       
    [  5]   4.00-5.00   sec  33.5 MBytes   281 Mbits/sec    0   1.09 MBytes       
    [  5]   5.00-6.00   sec  32.1 MBytes   269 Mbits/sec    0   1.09 MBytes       
    [  5]   6.00-7.00   sec  33.5 MBytes   281 Mbits/sec    0   1.22 MBytes       
    [  5]   7.00-8.00   sec  32.2 MBytes   271 Mbits/sec    0   1.37 MBytes       
    [  5]   8.00-9.00   sec  33.1 MBytes   278 Mbits/sec    0   1.45 MBytes       
    [  5]   9.00-10.00  sec  32.1 MBytes   269 Mbits/sec    0   1.45 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   330 MBytes   277 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   328 MBytes   275 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -30 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8822CE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8822CE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.21-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">404</span> Mbits/sec | <span style="font-size: 1.5rem;">567</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 49837 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  33.3 MBytes   280 Mbits/sec                  
    [  5]   1.00-2.00   sec  40.3 MBytes   338 Mbits/sec                  
    [  5]   2.00-3.00   sec  63.5 MBytes   533 Mbits/sec                  
    [  5]   3.00-4.00   sec  62.6 MBytes   525 Mbits/sec                  
    [  5]   4.00-5.00   sec  31.8 MBytes   267 Mbits/sec                  
    [  5]   5.00-6.00   sec  41.1 MBytes   345 Mbits/sec                  
    [  5]   6.00-7.00   sec  67.3 MBytes   565 Mbits/sec                  
    [  5]   7.00-8.00   sec  61.2 MBytes   514 Mbits/sec                  
    [  5]   8.00-9.00   sec  38.2 MBytes   321 Mbits/sec                  
    [  5]   9.00-10.00  sec  38.9 MBytes   327 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   482 MBytes   404 Mbits/sec  387             sender
    [  5]   0.00-10.00  sec   478 MBytes   401 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 54409 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  72.8 MBytes   610 Mbits/sec  217    921 KBytes       
    [  5]   1.00-2.00   sec  72.5 MBytes   606 Mbits/sec    0   1.01 MBytes       
    [  5]   2.00-3.00   sec  71.2 MBytes   600 Mbits/sec    0   1.10 MBytes       
    [  5]   3.00-4.00   sec  67.5 MBytes   566 Mbits/sec   28    642 KBytes       
    [  5]   4.00-5.00   sec  63.8 MBytes   535 Mbits/sec    0    773 KBytes       
    [  5]   5.00-6.00   sec  68.8 MBytes   577 Mbits/sec    0    891 KBytes       
    [  5]   6.00-7.00   sec  66.2 MBytes   556 Mbits/sec   47    516 KBytes       
    [  5]   7.00-8.00   sec  60.0 MBytes   503 Mbits/sec    0    665 KBytes       
    [  5]   8.00-9.00   sec  65.0 MBytes   545 Mbits/sec    0    792 KBytes       
    [  5]   9.00-10.00  sec  68.8 MBytes   577 Mbits/sec    0    909 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   676 MBytes   567 Mbits/sec  292             sender
    [  5]   0.00-10.01  sec   674 MBytes   565 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 136866 bytes (494 packets)
    TX: 60484 bytes (229 packets)
    signal: -30 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">891</span> Mbits/sec | <span style="font-size: 1.5rem;">691</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 54159 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   107 MBytes   894 Mbits/sec                  
    [  5]   1.00-2.00   sec   106 MBytes   891 Mbits/sec                  
    [  5]   2.00-3.00   sec   104 MBytes   877 Mbits/sec                  
    [  5]   3.00-4.00   sec   104 MBytes   869 Mbits/sec                  
    [  5]   4.00-5.00   sec   105 MBytes   883 Mbits/sec                  
    [  5]   5.00-6.00   sec   102 MBytes   858 Mbits/sec                  
    [  5]   6.00-7.00   sec   106 MBytes   890 Mbits/sec                  
    [  5]   7.00-8.00   sec   110 MBytes   923 Mbits/sec                  
    [  5]   8.00-9.00   sec   109 MBytes   911 Mbits/sec                  
    [  5]   9.00-10.00  sec   106 MBytes   885 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  1.04 GBytes   891 Mbits/sec  1102             sender
    [  5]   0.00-10.00  sec  1.03 GBytes   888 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 58827 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec   103 MBytes   864 Mbits/sec  550   3.21 MBytes       
    [  5]   1.00-2.00   sec  98.8 MBytes   828 Mbits/sec  814    525 KBytes       
    [  5]   2.00-3.00   sec  88.4 MBytes   741 Mbits/sec  222    387 KBytes       
    [  5]   3.00-4.00   sec  82.2 MBytes   690 Mbits/sec  127    314 KBytes       
    [  5]   4.00-5.00   sec  79.6 MBytes   668 Mbits/sec    0    573 KBytes       
    [  5]   5.00-6.00   sec  73.5 MBytes   617 Mbits/sec   46    535 KBytes       
    [  5]   6.00-7.00   sec  74.5 MBytes   625 Mbits/sec   27    503 KBytes       
    [  5]   7.00-8.00   sec  75.9 MBytes   636 Mbits/sec   85    481 KBytes       
    [  5]   8.00-9.00   sec  74.1 MBytes   622 Mbits/sec  108    454 KBytes       
    [  5]   9.00-10.00  sec  73.6 MBytes   617 Mbits/sec  123    424 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   824 MBytes   691 Mbits/sec  2102             sender
    [  5]   0.00-10.00  sec   820 MBytes   688 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 45702 bytes (158 packets)
    TX: 53290 bytes (228 packets)
    signal: -30 dBm
    rx bitrate: 1729.6 MBit/s 160MHz HE-MCS 8 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">103</span> Mbits/sec | <span style="font-size: 1.5rem;">72.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.114 port 50809 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.6 MBytes  97.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  12.2 MBytes   103 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.4 MBytes   104 Mbits/sec                  
    [  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.6 MBytes   106 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   123 MBytes   103 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   120 MBytes   101 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.114 port 44047 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.88 MBytes  82.8 Mbits/sec    0    385 KBytes       
    [  5]   1.00-2.00   sec  8.88 MBytes  74.4 Mbits/sec    0    530 KBytes       
    [  5]   2.00-3.00   sec  8.50 MBytes  71.3 Mbits/sec    0    530 KBytes       
    [  5]   3.00-4.00   sec  8.50 MBytes  71.3 Mbits/sec    0    530 KBytes       
    [  5]   4.00-5.00   sec  9.00 MBytes  75.5 Mbits/sec    0    584 KBytes       
    [  5]   5.00-6.00   sec  8.75 MBytes  73.4 Mbits/sec    0    617 KBytes       
    [  5]   6.00-7.00   sec  7.75 MBytes  65.0 Mbits/sec    0    617 KBytes       
    [  5]   7.00-8.00   sec  8.75 MBytes  73.4 Mbits/sec    0    617 KBytes       
    [  5]   8.00-9.00   sec  8.88 MBytes  74.4 Mbits/sec    0    617 KBytes       
    [  5]   9.00-10.00  sec  7.75 MBytes  65.0 Mbits/sec    0    617 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  86.6 MBytes  72.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  83.9 MBytes  70.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 117115 bytes (446 packets)
    TX: 72833 bytes (304 packets)
    signal: -17 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Atheros AR9271

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">56.6</span> Mbits/sec | <span style="font-size: 1.5rem;">41.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.113 port 59207 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.38 MBytes  53.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.50 MBytes  54.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  67.6 MBytes  56.6 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  64.6 MBytes  54.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.113 port 36355 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.75 MBytes  48.2 Mbits/sec    0    230 KBytes       
    [  5]   1.00-2.00   sec  5.25 MBytes  44.0 Mbits/sec    0    259 KBytes       
    [  5]   2.00-3.00   sec  5.12 MBytes  43.0 Mbits/sec    0    269 KBytes       
    [  5]   3.00-4.00   sec  4.50 MBytes  37.8 Mbits/sec    0    269 KBytes       
    [  5]   4.00-5.00   sec  4.62 MBytes  38.8 Mbits/sec    0    283 KBytes       
    [  5]   5.00-6.00   sec  4.88 MBytes  40.9 Mbits/sec    0    283 KBytes       
    [  5]   6.00-7.00   sec  4.38 MBytes  36.7 Mbits/sec    0    298 KBytes       
    [  5]   7.00-8.00   sec  5.00 MBytes  41.9 Mbits/sec    0    298 KBytes       
    [  5]   8.00-9.00   sec  4.38 MBytes  36.7 Mbits/sec    0    298 KBytes       
    [  5]   9.00-10.00  sec  5.12 MBytes  43.0 Mbits/sec    0    298 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  49.0 MBytes  41.1 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  47.4 MBytes  39.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 79055 bytes (302 packets)
    TX: 51735 bytes (210 packets)
    signal: -40 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### BCM 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">49.7</span> Mbits/sec | <span style="font-size: 1.5rem;">55.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 42843 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.76 MBytes  56.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  8.89 MBytes  74.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.10 MBytes  42.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.26 MBytes  44.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.73 MBytes  39.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.38 MBytes  45.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.23 MBytes  43.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.68 MBytes  39.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.19 MBytes  43.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.11  sec  59.9 MBytes  49.7 Mbits/sec    3             sender
    [  5]   0.00-10.00  sec  56.7 MBytes  47.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 38861 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.63 MBytes  55.5 Mbits/sec    0    215 KBytes       
    [  5]   1.00-2.00   sec  6.59 MBytes  55.2 Mbits/sec    0    273 KBytes       
    [  5]   2.00-3.00   sec  6.40 MBytes  53.7 Mbits/sec    0    284 KBytes       
    [  5]   3.00-4.00   sec  7.33 MBytes  61.5 Mbits/sec    0    334 KBytes       
    [  5]   4.00-5.00   sec  5.53 MBytes  46.4 Mbits/sec    0    334 KBytes       
    [  5]   5.00-6.00   sec  6.52 MBytes  54.8 Mbits/sec    0    351 KBytes       
    [  5]   6.00-7.00   sec  6.59 MBytes  55.2 Mbits/sec    0    351 KBytes       
    [  5]   7.00-8.00   sec  6.28 MBytes  52.7 Mbits/sec    0    375 KBytes       
    [  5]   8.00-9.00   sec  8.14 MBytes  68.3 Mbits/sec    0    450 KBytes       
    [  5]   9.00-10.00  sec  5.53 MBytes  46.4 Mbits/sec    0    450 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  65.5 MBytes  55.0 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  63.5 MBytes  53.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 51489 bytes (183 packets)
    TX: 57695 bytes (233 packets)
    signal: -50 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 390.0 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">39.3</span> Mbits/sec | <span style="font-size: 1.5rem;">51.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.112 port 60113 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.25 MBytes  35.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.50 MBytes  37.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.50 MBytes  37.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.38 MBytes  36.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  46.9 MBytes  39.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  43.6 MBytes  36.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.112 port 52947 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.38 MBytes  53.4 Mbits/sec    0    304 KBytes       
    [  5]   1.00-2.00   sec  7.25 MBytes  60.8 Mbits/sec    0    564 KBytes       
    [  5]   2.00-3.00   sec  6.75 MBytes  56.6 Mbits/sec    0    803 KBytes       
    [  5]   3.00-4.00   sec  5.50 MBytes  46.1 Mbits/sec    0    963 KBytes       
    [  5]   4.00-5.00   sec  6.88 MBytes  57.7 Mbits/sec    0   1024 KBytes       
    [  5]   5.00-6.00   sec  5.62 MBytes  47.2 Mbits/sec    0   1.05 MBytes       
    [  5]   6.00-7.00   sec  5.75 MBytes  48.2 Mbits/sec    0   1.06 MBytes       
    [  5]   7.00-8.00   sec  5.75 MBytes  48.2 Mbits/sec    0   1.19 MBytes       
    [  5]   8.00-9.00   sec  5.50 MBytes  46.1 Mbits/sec    1    880 KBytes       
    [  5]   9.00-10.00  sec  6.00 MBytes  50.3 Mbits/sec    0    979 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  61.4 MBytes  51.5 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec  59.1 MBytes  49.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 111557 bytes (428 packets)
    TX: 47051 bytes (199 packets)
    signal: -29 dBm
    rx bitrate: 58.5 MBit/s MCS 6
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">97.2</span> Mbits/sec | <span style="font-size: 1.5rem;">67.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.111 port 45473 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.0 MBytes  92.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.8 MBytes  98.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   116 MBytes  97.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   114 MBytes  95.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.111 port 41251 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.75 MBytes  73.3 Mbits/sec    0    206 KBytes       
    [  5]   1.00-2.00   sec  8.75 MBytes  73.4 Mbits/sec    0    242 KBytes       
    [  5]   2.00-3.00   sec  8.38 MBytes  70.3 Mbits/sec    0    305 KBytes       
    [  5]   3.00-4.00   sec  9.00 MBytes  75.5 Mbits/sec    0    359 KBytes       
    [  5]   4.00-5.00   sec  8.25 MBytes  69.2 Mbits/sec    0    359 KBytes       
    [  5]   5.00-6.00   sec  7.88 MBytes  66.1 Mbits/sec    0    378 KBytes       
    [  5]   6.00-7.00   sec  7.88 MBytes  66.1 Mbits/sec   12    269 KBytes       
    [  5]   7.00-8.00   sec  7.38 MBytes  61.8 Mbits/sec    6    206 KBytes       
    [  5]   8.00-9.00   sec  7.62 MBytes  64.0 Mbits/sec    0    218 KBytes       
    [  5]   9.00-10.00  sec  6.88 MBytes  57.6 Mbits/sec    0    228 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  80.8 MBytes  67.7 Mbits/sec   18             sender
    [  5]   0.00-10.00  sec  78.8 MBytes  66.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 185588 bytes (547 packets)
    TX: 106666 bytes (540 packets)
    signal: -22 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">34.5</span> Mbits/sec | <span style="font-size: 1.5rem;">46.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.110 port 34915 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.12 MBytes  26.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.25 MBytes  35.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.50 MBytes  37.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  3.88 MBytes  32.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.12 MBytes  34.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.28  sec  42.2 MBytes  34.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  39.2 MBytes  32.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.110 port 33217 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.25 MBytes  44.0 Mbits/sec    0    230 KBytes       
    [  5]   1.00-2.00   sec  5.50 MBytes  46.1 Mbits/sec    0    327 KBytes       
    [  5]   2.00-3.00   sec  6.12 MBytes  51.4 Mbits/sec    0    411 KBytes       
    [  5]   3.00-4.00   sec  5.88 MBytes  49.3 Mbits/sec    0    411 KBytes       
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec    0    411 KBytes       
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec    0    431 KBytes       
    [  5]   6.00-7.00   sec  6.38 MBytes  53.5 Mbits/sec    0    455 KBytes       
    [  5]   7.00-8.00   sec  5.00 MBytes  41.9 Mbits/sec    0    482 KBytes       
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec    0    482 KBytes       
    [  5]   9.00-10.00  sec  6.00 MBytes  50.3 Mbits/sec    0    482 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  55.4 MBytes  46.4 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  53.0 MBytes  44.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 101448 bytes (328 packets)
    TX: 50092 bytes (215 packets)
    signal: -31 dBm
    rx bitrate: 58.5 MBit/s MCS 6
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">2.41</span> Mbits/sec | <span style="font-size: 1.5rem;">45.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.109 port 53179 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   1.00-2.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   2.00-3.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   3.00-4.00   sec   128 KBytes  1.05 Mbits/sec                  
    [  5]   4.00-5.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   5.00-6.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   6.00-7.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   7.00-8.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   8.00-9.00   sec   256 KBytes  2.10 Mbits/sec                  
    [  5]   9.00-10.00  sec   384 KBytes  3.15 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  2.88 MBytes  2.41 Mbits/sec   89             sender
    [  5]   0.00-10.00  sec  2.38 MBytes  1.99 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.109 port 35059 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec    0    281 KBytes       
    [  5]   1.00-2.00   sec  5.25 MBytes  44.1 Mbits/sec    0    328 KBytes       
    [  5]   2.00-3.00   sec  5.88 MBytes  49.3 Mbits/sec    0    403 KBytes       
    [  5]   3.00-4.00   sec  5.62 MBytes  47.2 Mbits/sec    0    403 KBytes       
    [  5]   4.00-5.00   sec  4.88 MBytes  40.9 Mbits/sec    0    403 KBytes       
    [  5]   5.00-6.00   sec  5.25 MBytes  44.0 Mbits/sec    0    468 KBytes       
    [  5]   6.00-7.00   sec  4.62 MBytes  38.7 Mbits/sec    0    468 KBytes       
    [  5]   7.00-8.00   sec  5.62 MBytes  47.3 Mbits/sec    0    468 KBytes       
    [  5]   8.00-9.00   sec  4.62 MBytes  38.8 Mbits/sec    0    468 KBytes       
    [  5]   9.00-10.00  sec  5.62 MBytes  47.1 Mbits/sec    0    468 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  53.6 MBytes  45.0 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  51.5 MBytes  43.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 86834 bytes (339 packets)
    TX: 53995 bytes (221 packets)
    signal: -36 dBm
    rx bitrate: 39.0 MBit/s MCS 4
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8821CU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.550, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">82.5</span> Mbits/sec | <span style="font-size: 1.5rem;">3.98</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.136 port 51659 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.75 MBytes  56.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  7.00 MBytes  58.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.8 MBytes   124 Mbits/sec                  
    [  5]   6.00-7.00   sec  8.12 MBytes  68.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.9 MBytes   117 Mbits/sec                  
    [  5]   9.00-10.00  sec  15.0 MBytes   126 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  98.4 MBytes  82.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  97.8 MBytes  82.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.136 port 45417 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec   768 KBytes  6.28 Mbits/sec    0   69.3 KBytes       
    [  5]   1.00-2.00   sec   640 KBytes  5.24 Mbits/sec    0   73.5 KBytes       
    [  5]   2.00-3.00   sec   256 KBytes  2.10 Mbits/sec    0   77.8 KBytes       
    [  5]   3.00-4.00   sec   384 KBytes  3.15 Mbits/sec    0   82.0 KBytes       
    [  5]   4.00-5.00   sec   640 KBytes  5.24 Mbits/sec    0   89.1 KBytes       
    [  5]   5.00-6.00   sec   640 KBytes  5.24 Mbits/sec    0    120 KBytes       
    [  5]   6.00-7.00   sec   256 KBytes  2.10 Mbits/sec    0    120 KBytes       
    [  5]   7.00-8.00   sec   512 KBytes  4.20 Mbits/sec    0    120 KBytes       
    [  5]   8.00-9.00   sec   256 KBytes  2.10 Mbits/sec    0    120 KBytes       
    [  5]   9.00-10.00  sec   512 KBytes  4.19 Mbits/sec    0    120 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  4.75 MBytes  3.98 Mbits/sec    0             sender
    [  5]   0.00-10.06  sec  4.25 MBytes  3.54 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 179820 bytes (362 packets)
    TX: 99999 bytes (487 packets)
    signal: -44 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 292.5 MBit/s VHT-MCS 7 80MHz VHT-NSS 1
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">142</span> Mbits/sec | <span style="font-size: 1.5rem;">139</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 53867 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.6 MBytes   131 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.7 MBytes   140 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.5 MBytes   139 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   169 MBytes   142 Mbits/sec  125             sender
    [  5]   0.00-10.00  sec   166 MBytes   140 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 53413 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  17.0 MBytes   143 Mbits/sec    0    303 KBytes       
    [  5]   1.00-2.00   sec  16.7 MBytes   140 Mbits/sec    0    303 KBytes       
    [  5]   2.00-3.00   sec  16.0 MBytes   134 Mbits/sec    0    303 KBytes       
    [  5]   3.00-4.00   sec  17.2 MBytes   144 Mbits/sec    0    335 KBytes       
    [  5]   4.00-5.00   sec  16.2 MBytes   136 Mbits/sec    0    335 KBytes       
    [  5]   5.00-6.00   sec  16.4 MBytes   138 Mbits/sec    0    368 KBytes       
    [  5]   6.00-7.00   sec  16.8 MBytes   141 Mbits/sec    0    368 KBytes       
    [  5]   7.00-8.00   sec  16.0 MBytes   134 Mbits/sec    0    368 KBytes       
    [  5]   8.00-9.00   sec  16.7 MBytes   140 Mbits/sec    0    368 KBytes       
    [  5]   9.00-10.00  sec  16.2 MBytes   136 Mbits/sec    0    368 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   165 MBytes   139 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   164 MBytes   137 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 795151423 bytes (666880 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">20.2</span> Mbits/sec | <span style="font-size: 1.5rem;">12.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.138 port 60105 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  2.03 MBytes  17.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.89 MBytes  15.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.67 MBytes  14.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.28 MBytes  19.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.13 MBytes  17.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.24 MBytes  18.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.26 MBytes  19.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.35 MBytes  19.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.38 MBytes  20.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.32 MBytes  19.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.10  sec  24.4 MBytes  20.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  21.6 MBytes  18.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.138 port 47921 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.72 MBytes  14.4 Mbits/sec    0    102 KBytes       
    [  5]   1.00-2.00   sec  1.62 MBytes  13.6 Mbits/sec    0    127 KBytes       
    [  5]   2.00-3.00   sec  1.30 MBytes  10.9 Mbits/sec    0   39.6 KBytes       
    [  5]   3.00-4.00   sec  1.30 MBytes  10.9 Mbits/sec    3   76.4 KBytes       
    [  5]   4.00-5.00   sec  1.30 MBytes  10.9 Mbits/sec    2   62.2 KBytes       
    [  5]   5.00-6.00   sec  1.49 MBytes  12.5 Mbits/sec    3   58.0 KBytes       
    [  5]   6.00-7.00   sec  1.49 MBytes  12.5 Mbits/sec    0   74.9 KBytes       
    [  5]   7.00-8.00   sec  1.49 MBytes  12.5 Mbits/sec    0   86.3 KBytes       
    [  5]   8.00-9.00   sec  1.30 MBytes  10.9 Mbits/sec    0   94.7 KBytes       
    [  5]   9.00-10.00  sec  1.49 MBytes  12.5 Mbits/sec    0    102 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  14.5 MBytes  12.2 Mbits/sec    8             sender
    [  5]   0.00-10.03  sec  14.2 MBytes  11.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 81254 bytes (214 packets)
    TX: 57853 bytes (271 packets)
    signal: -31 dBm
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
