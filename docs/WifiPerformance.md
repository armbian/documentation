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
  - Netgear XS712T (10Gb)
  - Netgear XS508M (10Gb)
  - TP Link SG3218XP-M2 (2.5Gb PoE)
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
**Test Date:** [2025-08-22 22:29 UTC](https://github.com/armbian/armbian.github.io/actions/runs/17166681702)
### AC

#### Broadcom 4345

<img src=https://netbox.armbian.com/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">53.7</span> Mbits/sec | <span style="font-size: 1.5rem;">51.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.152 port 50517 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.91 MBytes  49.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.97 MBytes  50.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.02 MBytes  50.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.05 MBytes  50.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.13 MBytes  51.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.13 MBytes  51.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.08 MBytes  51.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.05 MBytes  50.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.07 MBytes  50.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.10 MBytes  51.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  64.1 MBytes  53.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  60.5 MBytes  50.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.152 port 58709 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.56 MBytes  63.4 Mbits/sec    0    395 KBytes       
    [  5]   1.00-2.00   sec  6.09 MBytes  51.1 Mbits/sec    0    594 KBytes       
    [  5]   2.00-3.00   sec  6.22 MBytes  52.2 Mbits/sec    0    814 KBytes       
    [  5]   3.00-4.00   sec  6.25 MBytes  52.4 Mbits/sec    0    867 KBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    0    969 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0    969 KBytes       
    [  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec    0    969 KBytes       
    [  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0    969 KBytes       
    [  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec    0    969 KBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0    969 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  61.1 MBytes  51.3 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  58.5 MBytes  48.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 152679 bytes (415 packets)
    TX: 84283 bytes (522 packets)
    signal: -33 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://netbox.armbian.com/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">103</span> Mbits/sec | <span style="font-size: 1.5rem;">91.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.151 port 60127 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   2.00-3.00   sec  12.1 MBytes   101 Mbits/sec                  
    [  5]   3.00-4.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.9 MBytes  99.7 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.0 MBytes   100 Mbits/sec                  
    [  5]   8.00-9.00   sec  12.1 MBytes   101 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.2 MBytes   103 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.06  sec   123 MBytes   103 Mbits/sec  295             sender
    [  5]   0.00-10.00  sec   120 MBytes   101 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.151 port 53591 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  10.9 MBytes  91.7 Mbits/sec    0    419 KBytes       
    [  5]   1.00-2.00   sec  11.4 MBytes  95.4 Mbits/sec    0    488 KBytes       
    [  5]   2.00-3.00   sec  11.4 MBytes  95.9 Mbits/sec    0    566 KBytes       
    [  5]   3.00-4.00   sec  11.1 MBytes  92.8 Mbits/sec    0    566 KBytes       
    [  5]   4.00-5.00   sec  11.6 MBytes  97.0 Mbits/sec    0    566 KBytes       
    [  5]   5.00-6.00   sec  10.9 MBytes  91.7 Mbits/sec    0    592 KBytes       
    [  5]   6.00-7.00   sec  11.6 MBytes  97.5 Mbits/sec    0    592 KBytes       
    [  5]   7.00-8.00   sec  11.4 MBytes  95.9 Mbits/sec    0    631 KBytes       
    [  5]   8.00-9.00   sec  9.32 MBytes  78.2 Mbits/sec    0    676 KBytes       
    [  5]   9.00-10.00  sec  9.38 MBytes  78.7 Mbits/sec    0    707 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   109 MBytes  91.5 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   108 MBytes  90.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 98916 bytes (394 packets)
    TX: 52049 bytes (224 packets)
    signal: -40 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### EDUP EP-AC1681

<img src=https://netbox.armbian.com/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">84.8</span> Mbits/sec | <span style="font-size: 1.5rem;">68.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.132 port 40459 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.50 MBytes  79.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  9.88 MBytes  82.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  9.88 MBytes  82.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.88 MBytes  82.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   101 MBytes  84.8 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   100 MBytes  84.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.132 port 56627 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  10.8 MBytes  90.1 Mbits/sec    0    495 KBytes       
    [  5]   1.00-2.00   sec  8.88 MBytes  74.4 Mbits/sec    0    677 KBytes       
    [  5]   2.00-3.00   sec  8.38 MBytes  70.2 Mbits/sec    0    677 KBytes       
    [  5]   3.00-4.00   sec  7.00 MBytes  58.7 Mbits/sec    0    754 KBytes       
    [  5]   4.00-5.00   sec  8.50 MBytes  71.3 Mbits/sec    0    754 KBytes       
    [  5]   5.00-6.00   sec  7.00 MBytes  58.7 Mbits/sec    0    754 KBytes       
    [  5]   6.00-7.00   sec  8.38 MBytes  70.3 Mbits/sec    0    844 KBytes       
    [  5]   7.00-8.00   sec  7.12 MBytes  59.8 Mbits/sec    0    844 KBytes       
    [  5]   8.00-9.00   sec  8.50 MBytes  71.3 Mbits/sec    0    844 KBytes       
    [  5]   9.00-10.00  sec  7.00 MBytes  58.7 Mbits/sec    0    844 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  81.5 MBytes  68.4 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  79.2 MBytes  66.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 194931 bytes (471 packets)
    TX: 97054 bytes (525 packets)
    signal: -39 dBm
    rx bitrate: 130.0 MBit/s MCS 15
    tx bitrate: 144.4 MBit/s MCS 15 short GI
    ```

#### Realtek 8821CU #1

<img src=https://netbox.armbian.com/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">134</span> Mbits/sec | <span style="font-size: 1.5rem;">203</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 33397 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.0 MBytes  83.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  14.8 MBytes   124 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   3.00-4.00   sec  15.2 MBytes   128 Mbits/sec                  
    [  5]   4.00-5.00   sec  15.4 MBytes   129 Mbits/sec                  
    [  5]   5.00-6.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.5 MBytes   147 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.2 MBytes   145 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   160 MBytes   134 Mbits/sec    6             sender
    [  5]   0.00-10.00  sec   159 MBytes   133 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 41881 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.0 MBytes   209 Mbits/sec   50    286 KBytes       
    [  5]   1.00-2.00   sec  24.9 MBytes   209 Mbits/sec    0    345 KBytes       
    [  5]   2.00-3.00   sec  23.9 MBytes   200 Mbits/sec    0    393 KBytes       
    [  5]   3.00-4.00   sec  24.0 MBytes   201 Mbits/sec    0    424 KBytes       
    [  5]   4.00-5.00   sec  24.0 MBytes   201 Mbits/sec    0    445 KBytes       
    [  5]   5.00-6.00   sec  23.9 MBytes   200 Mbits/sec    0    462 KBytes       
    [  5]   6.00-7.00   sec  24.1 MBytes   202 Mbits/sec    0    474 KBytes       
    [  5]   7.00-8.00   sec  24.8 MBytes   208 Mbits/sec    0    477 KBytes       
    [  5]   8.00-9.00   sec  22.8 MBytes   191 Mbits/sec    0    481 KBytes       
    [  5]   9.00-10.00  sec  24.8 MBytes   207 Mbits/sec    0    488 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   242 MBytes   203 Mbits/sec   50             sender
    [  5]   0.00-10.02  sec   240 MBytes   201 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 89639 bytes (286 packets)
    TX: 69319 bytes (273 packets)
    signal: -44 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```

#### Realtek 8821CU #2

<img src=https://netbox.armbian.com/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">256</span> Mbits/sec | <span style="font-size: 1.5rem;">253</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.150 port 51227 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  27.9 MBytes   234 Mbits/sec                  
    [  5]   1.00-2.00   sec  34.1 MBytes   286 Mbits/sec                  
    [  5]   2.00-3.00   sec  33.0 MBytes   277 Mbits/sec                  
    [  5]   3.00-4.00   sec  31.4 MBytes   263 Mbits/sec                  
    [  5]   4.00-5.00   sec  26.1 MBytes   219 Mbits/sec                  
    [  5]   5.00-6.00   sec  28.9 MBytes   242 Mbits/sec                  
    [  5]   6.00-7.00   sec  30.2 MBytes   254 Mbits/sec                  
    [  5]   7.00-8.00   sec  27.9 MBytes   234 Mbits/sec                  
    [  5]   8.00-9.00   sec  30.4 MBytes   255 Mbits/sec                  
    [  5]   9.00-10.00  sec  32.5 MBytes   273 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   306 MBytes   256 Mbits/sec  138             sender
    [  5]   0.00-10.00  sec   302 MBytes   254 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.150 port 50725 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  32.8 MBytes   274 Mbits/sec    0   2.22 MBytes       
    [  5]   1.00-2.00   sec  30.9 MBytes   259 Mbits/sec    0   2.22 MBytes       
    [  5]   2.00-3.00   sec  31.0 MBytes   260 Mbits/sec    0   2.22 MBytes       
    [  5]   3.00-4.00   sec  29.5 MBytes   247 Mbits/sec    0   2.96 MBytes       
    [  5]   4.00-5.00   sec  30.2 MBytes   254 Mbits/sec   58    851 KBytes       
    [  5]   5.00-6.00   sec  28.0 MBytes   235 Mbits/sec  154    457 KBytes       
    [  5]   6.00-7.00   sec  29.4 MBytes   246 Mbits/sec    0    512 KBytes       
    [  5]   7.00-8.00   sec  30.6 MBytes   257 Mbits/sec    0    561 KBytes       
    [  5]   8.00-9.00   sec  29.5 MBytes   247 Mbits/sec    0    594 KBytes       
    [  5]   9.00-10.00  sec  29.8 MBytes   249 Mbits/sec    0    619 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   302 MBytes   253 Mbits/sec  212             sender
    [  5]   0.00-10.01  sec   299 MBytes   250 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### Realtek 88X2CS

<img src=https://netbox.armbian.com/media/devicetype-images/RTL88X2CS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.1, 6.12.42-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88X2CS</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">104</span> Mbits/sec | <span style="font-size: 1.5rem;">192</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.136 port 46429 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.1 MBytes  93.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.9 MBytes  99.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.4 MBytes   104 Mbits/sec                  
    [  5]   5.00-6.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   6.00-7.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.2 MBytes   103 Mbits/sec                  
    [  5]   8.00-9.00   sec  10.5 MBytes  88.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.0 MBytes  92.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   124 MBytes   104 Mbits/sec   83            sender
    [  5]   0.00-10.00  sec   121 MBytes   102 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.136 port 57695 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  23.2 MBytes   195 Mbits/sec    0   5.21 MBytes       
    [  5]   1.00-2.00   sec  25.8 MBytes   216 Mbits/sec    0   5.21 MBytes       
    [  5]   2.00-3.00   sec  23.0 MBytes   193 Mbits/sec    0   5.21 MBytes       
    [  5]   3.00-4.00   sec  23.2 MBytes   195 Mbits/sec    0   5.21 MBytes       
    [  5]   4.00-5.00   sec  21.5 MBytes   180 Mbits/sec    0   5.21 MBytes       
    [  5]   5.00-6.00   sec  24.1 MBytes   202 Mbits/sec    0   5.21 MBytes       
    [  5]   6.00-7.00   sec  23.5 MBytes   197 Mbits/sec   61   2.60 MBytes       
    [  5]   7.00-8.00   sec  21.4 MBytes   179 Mbits/sec   64   1.31 MBytes       
    [  5]   8.00-9.00   sec  21.1 MBytes   177 Mbits/sec   92    205 KBytes       
    [  5]   9.00-10.00  sec  21.5 MBytes   180 Mbits/sec    0    321 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   228 MBytes   192 Mbits/sec  217            sender
    [  5]   0.00-10.01  sec   225 MBytes   189 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 183705 bytes (369 packets)
    TX: 100341 bytes (481 packets)
    signal: -39 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```
### AX

#### Ampak 6275P

<img src=https://netbox.armbian.com/media/devicetype-images/AP6275P.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.149, 6.12.33-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AP6275P</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">437</span> Mbits/sec | <span style="font-size: 1.5rem;">452</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 37781 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  43.1 MBytes   361 Mbits/sec                  
    [  5]   1.00-2.00   sec  48.1 MBytes   404 Mbits/sec                  
    [  5]   2.00-3.00   sec  53.8 MBytes   451 Mbits/sec                  
    [  5]   3.00-4.00   sec  52.0 MBytes   437 Mbits/sec                  
    [  5]   4.00-5.00   sec  55.8 MBytes   468 Mbits/sec                  
    [  5]   5.00-6.00   sec  55.6 MBytes   466 Mbits/sec                  
    [  5]   6.00-7.00   sec  54.3 MBytes   455 Mbits/sec                  
    [  5]   7.00-8.00   sec  51.0 MBytes   427 Mbits/sec                  
    [  5]   8.00-9.00   sec  54.9 MBytes   460 Mbits/sec                  
    [  5]   9.00-10.00  sec  50.3 MBytes   422 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   522 MBytes   437 Mbits/sec  310             sender
    [  5]   0.00-10.00  sec   519 MBytes   435 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 41501 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  68.0 MBytes   570 Mbits/sec  323    749 KBytes       
    [  5]   1.00-2.00   sec  65.0 MBytes   545 Mbits/sec    1    482 KBytes       
    [  5]   2.00-3.00   sec  58.8 MBytes   493 Mbits/sec    0    635 KBytes       
    [  5]   3.00-4.00   sec  45.0 MBytes   377 Mbits/sec   24    311 KBytes       
    [  5]   4.00-5.00   sec  35.0 MBytes   294 Mbits/sec    3    296 KBytes       
    [  5]   5.00-6.00   sec  22.5 MBytes   189 Mbits/sec   68    249 KBytes       
    [  5]   6.00-7.00   sec  45.0 MBytes   377 Mbits/sec    0    438 KBytes       
    [  5]   7.00-8.00   sec  57.5 MBytes   482 Mbits/sec    0    597 KBytes       
    [  5]   8.00-9.00   sec  68.8 MBytes   577 Mbits/sec    0    745 KBytes       
    [  5]   9.00-10.00  sec  73.8 MBytes   619 Mbits/sec    0    878 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   539 MBytes   452 Mbits/sec  419             sender
    [  5]   0.00-10.01  sec   537 MBytes   450 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 61458 bytes (126 packets)
    TX: 54154 bytes (196 packets)
    signal: -33 dBm
    rx bitrate: 1200.9 MBit/s
    tx bitrate: 1200.9 MBit/s
    
    ```

#### Comfast CF953AX

<img src=https://netbox.armbian.com/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">103</span> Mbits/sec | <span style="font-size: 1.5rem;">107</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 47657 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.0 MBytes   101 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.5 MBytes   105 Mbits/sec                  
    [  5]   2.00-3.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.0 MBytes   101 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.4 MBytes   104 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.9 MBytes  99.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  12.1 MBytes   102 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   123 MBytes   103 Mbits/sec  265             sender
    [  5]   0.00-10.00  sec   120 MBytes   101 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 41445 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.01   sec  13.9 MBytes   116 Mbits/sec    0    416 KBytes       
    [  5]   1.01-2.00   sec  12.1 MBytes   102 Mbits/sec    0    580 KBytes       
    [  5]   2.00-3.02   sec  13.1 MBytes   108 Mbits/sec    0    652 KBytes       
    [  5]   3.02-4.01   sec  12.6 MBytes   108 Mbits/sec    0    735 KBytes       
    [  5]   4.01-5.05   sec  14.2 MBytes   114 Mbits/sec    0    782 KBytes       
    [  5]   5.05-6.02   sec  13.8 MBytes   119 Mbits/sec    0    782 KBytes       
    [  5]   6.02-7.01   sec  11.6 MBytes  99.2 Mbits/sec    0    782 KBytes       
    [  5]   7.01-8.06   sec  12.6 MBytes   100 Mbits/sec    0    782 KBytes       
    [  5]   8.06-9.04   sec  10.8 MBytes  92.5 Mbits/sec    0    782 KBytes       
    [  5]   9.04-10.01  sec  12.9 MBytes   111 Mbits/sec    0    782 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   128 MBytes   107 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   124 MBytes   104 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 146917 bytes (453 packets)
    TX: 79810 bytes (491 packets)
    signal: -37 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

#### Intel AX200

<img src=https://netbox.armbian.com/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">644</span> Mbits/sec | <span style="font-size: 1.5rem;">485</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 51665 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   107 MBytes   898 Mbits/sec                  
    [  5]   1.00-2.00   sec   107 MBytes   900 Mbits/sec                  
    [  5]   2.00-3.00   sec  96.1 MBytes   806 Mbits/sec                  
    [  5]   3.00-4.00   sec  70.1 MBytes   588 Mbits/sec                  
    [  5]   4.00-5.00   sec  62.9 MBytes   527 Mbits/sec                  
    [  5]   5.00-6.00   sec  61.0 MBytes   512 Mbits/sec                  
    [  5]   6.00-7.00   sec  77.5 MBytes   650 Mbits/sec                  
    [  5]   7.00-8.00   sec  68.4 MBytes   574 Mbits/sec                  
    [  5]   8.00-9.00   sec  57.8 MBytes   484 Mbits/sec                  
    [  5]   9.00-10.00  sec  56.5 MBytes   474 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   768 MBytes   644 Mbits/sec  434             sender
    [  5]   0.00-10.00  sec   765 MBytes   641 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 43967 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  30.1 MBytes   252 Mbits/sec    0   2.58 MBytes       
    [  5]   1.00-2.00   sec  55.5 MBytes   466 Mbits/sec  124    745 KBytes       
    [  5]   2.00-3.00   sec  73.6 MBytes   618 Mbits/sec   50    557 KBytes       
    [  5]   3.00-4.00   sec  81.5 MBytes   684 Mbits/sec    0    740 KBytes       
    [  5]   4.00-5.00   sec  72.5 MBytes   608 Mbits/sec    1    465 KBytes       
    [  5]   5.00-6.00   sec  47.4 MBytes   397 Mbits/sec    0    595 KBytes       
    [  5]   6.00-7.00   sec  71.9 MBytes   603 Mbits/sec   10    397 KBytes       
    [  5]   7.00-8.00   sec  58.2 MBytes   489 Mbits/sec    0    573 KBytes       
    [  5]   8.00-9.00   sec  54.9 MBytes   460 Mbits/sec   24    216 KBytes       
    [  5]   9.00-10.00  sec  32.4 MBytes   271 Mbits/sec    0    375 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   578 MBytes   485 Mbits/sec  209             sender
    [  5]   0.00-10.01  sec   576 MBytes   482 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 38883 bytes (169 packets)
    TX: 53625 bytes (188 packets)
    signal: -29 dBm
    rx bitrate: 1200.9 MBit/s 160MHz HE-MCS 11 HE-NSS 1 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```

#### Realtek 8852AE

<img src=https://netbox.armbian.com/media/devicetype-images/RTL8852AE.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.1, 6.12.42-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8852AE</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">541</span> Mbits/sec | <span style="font-size: 1.5rem;">539</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.135 port 44147 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  71.1 MBytes   596 Mbits/sec                  
    [  5]   1.00-2.00   sec  73.1 MBytes   613 Mbits/sec                  
    [  5]   2.00-3.00   sec  49.2 MBytes   412 Mbits/sec                  
    [  5]   3.00-4.00   sec  62.4 MBytes   523 Mbits/sec                  
    [  5]   4.00-5.00   sec  69.2 MBytes   581 Mbits/sec                  
    [  5]   5.00-6.00   sec  73.1 MBytes   614 Mbits/sec                  
    [  5]   6.00-7.00   sec  77.7 MBytes   651 Mbits/sec                  
    [  5]   7.00-8.00   sec  75.6 MBytes   634 Mbits/sec                  
    [  5]   8.00-9.00   sec  43.7 MBytes   366 Mbits/sec                  
    [  5]   9.00-10.00  sec  46.7 MBytes   392 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   645 MBytes   541 Mbits/sec  205             sender
    [  5]   0.00-10.00  sec   642 MBytes   538 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.135 port 35269 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  91.2 MBytes   765 Mbits/sec  441   2.81 MBytes       
    [  5]   1.00-2.00   sec  88.8 MBytes   744 Mbits/sec    0   2.81 MBytes       
    [  5]   2.00-3.00   sec  82.5 MBytes   692 Mbits/sec  457    757 KBytes       
    [  5]   3.00-4.00   sec  66.2 MBytes   556 Mbits/sec   11    317 KBytes       
    [  5]   4.00-5.00   sec  61.2 MBytes   514 Mbits/sec    0    529 KBytes       
    [  5]   5.00-6.00   sec  53.8 MBytes   451 Mbits/sec   34    240 KBytes       
    [  5]   6.00-7.00   sec  30.0 MBytes   252 Mbits/sec   30    112 KBytes       
    [  5]   7.00-8.00   sec  35.0 MBytes   294 Mbits/sec    0    337 KBytes       
    [  5]   8.00-9.00   sec  63.8 MBytes   535 Mbits/sec    0    544 KBytes       
    [  5]   9.00-10.00  sec  70.0 MBytes   585 Mbits/sec    0    707 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   642 MBytes   539 Mbits/sec  973             sender
    [  5]   0.00-10.01  sec   640 MBytes   536 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 129681 bytes (490 packets)
    TX: 60051 bytes (222 packets)
    signal: -30 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    
    ```

#### Realtek 8852BS

<img src=https://netbox.armbian.com/media/devicetype-images/RTL8852BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.1, 6.6.99-current-spacemit</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8852BS</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">389</span> Mbits/sec | <span style="font-size: 1.5rem;">365</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 45169 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  41.9 MBytes   351 Mbits/sec                  
    [  5]   1.00-2.00   sec  53.0 MBytes   445 Mbits/sec                  
    [  5]   2.00-3.00   sec  52.2 MBytes   438 Mbits/sec                  
    [  5]   3.00-4.00   sec  51.5 MBytes   432 Mbits/sec                  
    [  5]   4.00-5.00   sec  47.8 MBytes   401 Mbits/sec                  
    [  5]   5.00-6.00   sec  40.9 MBytes   343 Mbits/sec                  
    [  5]   6.00-7.00   sec  31.5 MBytes   264 Mbits/sec                  
    [  5]   7.00-8.00   sec  45.2 MBytes   380 Mbits/sec                  
    [  5]   8.00-9.00   sec  48.5 MBytes   407 Mbits/sec                  
    [  5]   9.00-10.00  sec  48.5 MBytes   407 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   464 MBytes   389 Mbits/sec  238             sender
    [  5]   0.00-10.00  sec   461 MBytes   387 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 56765 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  32.9 MBytes   275 Mbits/sec   12    447 KBytes       
    [  5]   1.00-2.00   sec  42.4 MBytes   355 Mbits/sec    0    509 KBytes       
    [  5]   2.00-3.00   sec  41.8 MBytes   350 Mbits/sec    0    568 KBytes       
    [  5]   3.00-4.00   sec  41.4 MBytes   347 Mbits/sec    0    624 KBytes       
    [  5]   4.00-5.00   sec  46.5 MBytes   390 Mbits/sec    0    676 KBytes       
    [  5]   5.00-6.00   sec  43.6 MBytes   366 Mbits/sec    0    724 KBytes       
    [  5]   6.00-7.00   sec  47.4 MBytes   397 Mbits/sec    0    772 KBytes       
    [  5]   7.00-8.00   sec  47.4 MBytes   397 Mbits/sec    0    817 KBytes       
    [  5]   8.00-9.00   sec  47.2 MBytes   396 Mbits/sec    0    854 KBytes       
    [  5]   9.00-10.00  sec  44.6 MBytes   374 Mbits/sec    0    889 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   436 MBytes   365 Mbits/sec   12             sender
    [  5]   0.00-10.01  sec   434 MBytes   363 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 50231 bytes (137 packets)
    TX: 51503 bytes (217 packets)
    ```
### N

#### Alfa RT3572

<img src=https://netbox.armbian.com/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">85.5</span> Mbits/sec | <span style="font-size: 1.5rem;">43.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 55069 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  8.75 MBytes  73.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  9.12 MBytes  76.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.00 MBytes  75.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  9.75 MBytes  81.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.6 MBytes  97.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.62 MBytes  80.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   102 MBytes  85.5 Mbits/sec   40             sender
    [  5]   0.00-10.00  sec  98.4 MBytes  82.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 42775 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.00 MBytes  58.7 Mbits/sec    0    192 KBytes       
    [  5]   1.00-2.00   sec  5.50 MBytes  46.1 Mbits/sec    0    214 KBytes       
    [  5]   2.00-3.00   sec  4.88 MBytes  40.9 Mbits/sec    0    214 KBytes       
    [  5]   3.00-4.00   sec  5.25 MBytes  44.0 Mbits/sec    1    165 KBytes       
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec    0    180 KBytes       
    [  5]   5.00-6.00   sec  5.12 MBytes  43.0 Mbits/sec    0    198 KBytes       
    [  5]   6.00-7.00   sec  4.75 MBytes  39.8 Mbits/sec    0    198 KBytes       
    [  5]   7.00-8.00   sec  5.25 MBytes  44.0 Mbits/sec    0    212 KBytes       
    [  5]   8.00-9.00   sec  4.88 MBytes  40.9 Mbits/sec    0    212 KBytes       
    [  5]   9.00-10.00  sec  4.75 MBytes  39.8 Mbits/sec    0    212 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  52.4 MBytes  43.9 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec  51.5 MBytes  43.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 190803 bytes (598 packets)
    TX: 94368 bytes (547 packets)
    signal: -17 dBm
    rx bitrate: 150.0 MBit/s MCS 7 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Atheros AR9271

<img src=https://netbox.armbian.com/media/devicetype-images/AR9271.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">50.8</span> Mbits/sec | <span style="font-size: 1.5rem;">44.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.129 port 38349 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.62 MBytes  47.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.75 MBytes  48.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.88 MBytes  49.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.75 MBytes  48.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  60.6 MBytes  50.8 Mbits/sec    8             sender
    [  5]   0.00-10.00  sec  56.8 MBytes  47.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.129 port 51923 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec    0    208 KBytes       
    [  5]   1.00-2.00   sec  5.00 MBytes  41.9 Mbits/sec    0    230 KBytes       
    [  5]   2.00-3.00   sec  5.62 MBytes  47.2 Mbits/sec    0    250 KBytes       
    [  5]   3.00-4.00   sec  5.62 MBytes  47.2 Mbits/sec    0    263 KBytes       
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec    0    263 KBytes       
    [  5]   5.00-6.00   sec  5.00 MBytes  41.9 Mbits/sec    0    263 KBytes       
    [  5]   6.00-7.00   sec  5.12 MBytes  43.0 Mbits/sec    0    263 KBytes       
    [  5]   7.00-8.00   sec  5.50 MBytes  46.1 Mbits/sec    0    263 KBytes       
    [  5]   8.00-9.00   sec  5.12 MBytes  43.0 Mbits/sec    0    263 KBytes       
    [  5]   9.00-10.00  sec  5.00 MBytes  41.9 Mbits/sec    0    263 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  53.2 MBytes  44.7 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  52.2 MBytes  43.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 102557 bytes (363 packets)
    TX: 49880 bytes (208 packets)
    signal: -52 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Broadcom 43430

<img src=https://netbox.armbian.com/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">51.2</span> Mbits/sec | <span style="font-size: 1.5rem;">37.2</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 37887 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.40 MBytes  45.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.04 MBytes  50.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.94 MBytes  49.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.99 MBytes  50.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.07 MBytes  50.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.94 MBytes  49.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.08 MBytes  51.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.54 MBytes  46.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.44 MBytes  45.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.81 MBytes  48.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  61.2 MBytes  51.2 Mbits/sec  131             sender
    [  5]   0.00-10.00  sec  58.2 MBytes  48.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 58533 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.06 MBytes  42.5 Mbits/sec    0    181 KBytes       
    [  5]   1.00-2.00   sec  4.54 MBytes  38.1 Mbits/sec    0    198 KBytes       
    [  5]   2.00-3.00   sec  4.47 MBytes  37.5 Mbits/sec    0    198 KBytes       
    [  5]   3.00-4.00   sec  4.47 MBytes  37.5 Mbits/sec    0    198 KBytes       
    [  5]   4.00-5.00   sec  4.47 MBytes  37.5 Mbits/sec    0    208 KBytes       
    [  5]   5.00-6.00   sec  4.29 MBytes  36.0 Mbits/sec    0    208 KBytes       
    [  5]   6.00-7.00   sec  3.60 MBytes  30.2 Mbits/sec    0    239 KBytes       
    [  5]   7.00-8.00   sec  4.41 MBytes  37.0 Mbits/sec    0    239 KBytes       
    [  5]   8.00-9.00   sec  4.60 MBytes  38.6 Mbits/sec    1    199 KBytes       
    [  5]   9.00-10.00  sec  4.47 MBytes  37.5 Mbits/sec    0    216 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  44.4 MBytes  37.2 Mbits/sec    1             sender
    [  5]   0.00-10.02  sec  43.8 MBytes  36.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 83933 bytes (269 packets)
    TX: 65367 bytes (297 packets)
    signal: -54 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://netbox.armbian.com/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">47.2</span> Mbits/sec | <span style="font-size: 1.5rem;">50.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 37015 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.90 MBytes  49.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.23 MBytes  43.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.06 MBytes  42.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.81 MBytes  48.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.46 MBytes  54.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.30 MBytes  44.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.51 MBytes  46.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.28 MBytes  35.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.34 MBytes  53.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.98 MBytes  41.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.19  sec  57.4 MBytes  47.2 Mbits/sec  291             sender
    [  5]   0.00-10.00  sec  54.9 MBytes  46.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 33731 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.55 MBytes  54.9 Mbits/sec    0    199 KBytes       
    [  5]   1.00-2.00   sec  6.21 MBytes  52.2 Mbits/sec    0    243 KBytes       
    [  5]   2.00-3.00   sec  6.21 MBytes  52.1 Mbits/sec    0    276 KBytes       
    [  5]   3.00-4.00   sec  6.21 MBytes  52.1 Mbits/sec    0    294 KBytes       
    [  5]   4.00-5.00   sec  5.59 MBytes  46.9 Mbits/sec    0    294 KBytes       
    [  5]   5.00-6.00   sec  5.72 MBytes  47.9 Mbits/sec    0    294 KBytes       
    [  5]   6.00-7.00   sec  6.28 MBytes  52.7 Mbits/sec    0    311 KBytes       
    [  5]   7.00-8.00   sec  5.84 MBytes  48.9 Mbits/sec    0    311 KBytes       
    [  5]   8.00-9.00   sec  5.59 MBytes  47.0 Mbits/sec    0    311 KBytes       
    [  5]   9.00-10.00  sec  6.40 MBytes  53.7 Mbits/sec    0    311 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  60.6 MBytes  50.8 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  59.1 MBytes  49.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 53511 bytes (137 packets)
    TX: 50848 bytes (242 packets)
    signal: -45 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Ralink RT5370

<img src=https://netbox.armbian.com/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">46.5</span> Mbits/sec | <span style="font-size: 1.5rem;">38.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 43847 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  55.5 MBytes  46.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  53.0 MBytes  44.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 41709 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.75 MBytes  48.2 Mbits/sec    0    264 KBytes       
    [  5]   1.00-2.00   sec  5.00 MBytes  41.9 Mbits/sec    0    419 KBytes       
    [  5]   2.00-3.00   sec  4.88 MBytes  40.9 Mbits/sec    0    455 KBytes       
    [  5]   3.00-4.00   sec  4.25 MBytes  35.7 Mbits/sec    0    488 KBytes       
    [  5]   4.00-5.00   sec  4.00 MBytes  33.5 Mbits/sec    0    488 KBytes       
    [  5]   5.00-6.00   sec  4.50 MBytes  37.8 Mbits/sec    0    550 KBytes       
    [  5]   6.00-7.00   sec  3.75 MBytes  31.5 Mbits/sec    0    550 KBytes       
    [  5]   7.00-8.00   sec  5.62 MBytes  47.2 Mbits/sec    0    550 KBytes       
    [  5]   8.00-9.00   sec  4.50 MBytes  37.7 Mbits/sec    0    550 KBytes       
    [  5]   9.00-10.00  sec  3.50 MBytes  29.3 Mbits/sec    0    550 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  45.8 MBytes  38.4 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  43.6 MBytes  36.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 80744 bytes (339 packets)
    TX: 55518 bytes (210 packets)
    signal: -33 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://netbox.armbian.com/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">65.1</span> Mbits/sec | <span style="font-size: 1.5rem;">49.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 57105 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.12 MBytes  51.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  9.38 MBytes  78.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.62 MBytes  55.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  8.00 MBytes  67.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.25 MBytes  52.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  9.25 MBytes  77.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  7.25 MBytes  60.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  7.88 MBytes  66.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  77.6 MBytes  65.1 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec  75.6 MBytes  63.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 60063 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.50 MBytes  54.5 Mbits/sec    0    191 KBytes       
    [  5]   1.00-2.00   sec  6.00 MBytes  50.3 Mbits/sec    0    199 KBytes       
    [  5]   2.00-3.00   sec  5.75 MBytes  48.2 Mbits/sec    0    199 KBytes       
    [  5]   3.00-4.00   sec  5.75 MBytes  48.2 Mbits/sec    0    206 KBytes       
    [  5]   4.00-5.00   sec  5.75 MBytes  48.3 Mbits/sec    0    206 KBytes       
    [  5]   5.00-6.00   sec  5.25 MBytes  44.1 Mbits/sec    0    206 KBytes       
    [  5]   6.00-7.00   sec  5.75 MBytes  48.2 Mbits/sec    0    225 KBytes       
    [  5]   7.00-8.00   sec  5.88 MBytes  49.3 Mbits/sec    0    225 KBytes       
    [  5]   8.00-9.00   sec  6.12 MBytes  51.4 Mbits/sec    0    293 KBytes       
    [  5]   9.00-10.00  sec  5.62 MBytes  47.1 Mbits/sec    0    293 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  58.4 MBytes  49.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  56.8 MBytes  47.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 96933 bytes (406 packets)
    TX: 59777 bytes (286 packets)
    signal: -28 dBm
    rx bitrate: 180.0 MBit/s MCS 12 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8188CUS

<img src=https://netbox.armbian.com/media/devicetype-images/RTL8192CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.11.0-trunk.49, 6.12.42-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">19.2</span> Mbits/sec | <span style="font-size: 1.5rem;">37.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 46113 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.75 MBytes  14.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.12 MBytes  17.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  2.12 MBytes  17.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.88 MBytes  15.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.75 MBytes  14.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  22.9 MBytes  19.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  19.6 MBytes  16.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 58385 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.12 MBytes  34.6 Mbits/sec    0    205 KBytes       
    [  5]   1.00-2.00   sec  4.38 MBytes  36.7 Mbits/sec    0    328 KBytes       
    [  5]   2.00-3.00   sec  3.88 MBytes  32.5 Mbits/sec    0    413 KBytes       
    [  5]   3.00-4.00   sec  5.12 MBytes  43.0 Mbits/sec    0    471 KBytes       
    [  5]   4.00-5.00   sec  4.00 MBytes  33.6 Mbits/sec    0    471 KBytes       
    [  5]   5.00-6.00   sec  5.00 MBytes  41.9 Mbits/sec    5    365 KBytes       
    [  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec    0    407 KBytes       
    [  5]   7.00-8.00   sec  4.75 MBytes  39.8 Mbits/sec    0    438 KBytes       
    [  5]   8.00-9.00   sec  4.88 MBytes  40.9 Mbits/sec    0    458 KBytes       
    [  5]   9.00-10.00  sec  4.00 MBytes  33.5 Mbits/sec    0    458 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  45.1 MBytes  37.8 Mbits/sec    5             sender
    [  5]   0.00-10.02  sec  43.1 MBytes  36.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437.0
    RX: 91384 bytes (324 packets)
    TX: 61293 bytes (226 packets)
    signal: -40 dBm
    rx bitrate: 52.0 MBit/s MCS 5
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Realtek 8723BS

<img src=https://netbox.armbian.com/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">29.4</span> Mbits/sec | <span style="font-size: 1.5rem;">22.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.140 port 57017 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.04 MBytes  33.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.47 MBytes  29.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.18 MBytes  18.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.95 MBytes  33.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.27 MBytes  27.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.61 MBytes  21.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.75 MBytes  31.5 Mbits/sec                  
    [  5]   8.00-9.00   sec   831 KBytes  6.81 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.00 MBytes  33.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  35.1 MBytes  29.4 Mbits/sec   47             sender
    [  5]   0.00-10.00  sec  31.8 MBytes  26.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.140 port 55955 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.91 MBytes  41.2 Mbits/sec    0    263 KBytes       
    [  5]   1.00-2.00   sec  3.73 MBytes  31.3 Mbits/sec    0    443 KBytes       
    [  5]   2.00-3.00   sec  2.98 MBytes  25.0 Mbits/sec    0    510 KBytes       
    [  5]   3.00-4.00   sec  2.67 MBytes  22.4 Mbits/sec    0    612 KBytes       
    [  5]   4.00-5.00   sec  2.11 MBytes  17.7 Mbits/sec    0    716 KBytes       
    [  5]   5.00-6.00   sec  2.42 MBytes  20.3 Mbits/sec    0    778 KBytes       
    [  5]   6.00-7.00   sec  3.60 MBytes  30.2 Mbits/sec    0    778 KBytes       
    [  5]   7.00-8.00   sec  1.74 MBytes  14.6 Mbits/sec    0    847 KBytes       
    [  5]   8.00-9.00   sec  1.86 MBytes  15.6 Mbits/sec    0    872 KBytes       
    [  5]   9.00-10.00  sec  1018 KBytes  8.34 Mbits/sec    0    921 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  27.0 MBytes  22.7 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  26.0 MBytes  21.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### UWE 5622

<img src=https://netbox.armbian.com/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.154, 6.12.30-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">134</span> Mbits/sec | <span style="font-size: 1.5rem;">137</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.138 port 39627 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.4 MBytes   129 Mbits/sec                  
    [  5]   1.00-2.00   sec  15.7 MBytes   132 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.6 MBytes   139 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.8 MBytes   124 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.3 MBytes   137 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.6 MBytes   140 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   160 MBytes   134 Mbits/sec  116             sender
    [  5]   0.00-10.00  sec   158 MBytes   132 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.138 port 42441 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.1 MBytes   152 Mbits/sec    0    362 KBytes       
    [  5]   1.00-2.00   sec  16.6 MBytes   139 Mbits/sec    0    362 KBytes       
    [  5]   2.00-3.00   sec  16.6 MBytes   139 Mbits/sec    0    362 KBytes       
    [  5]   3.00-4.00   sec  15.9 MBytes   133 Mbits/sec    0    362 KBytes       
    [  5]   4.00-5.00   sec  16.7 MBytes   140 Mbits/sec    0    362 KBytes       
    [  5]   5.00-6.00   sec  16.6 MBytes   139 Mbits/sec    0    362 KBytes       
    [  5]   6.00-7.00   sec  16.6 MBytes   139 Mbits/sec    0    362 KBytes       
    [  5]   7.00-8.00   sec  16.1 MBytes   135 Mbits/sec    0    362 KBytes       
    [  5]   8.00-9.00   sec  16.0 MBytes   134 Mbits/sec   12    209 KBytes       
    [  5]   9.00-10.00  sec  14.2 MBytes   119 Mbits/sec    7    129 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   163 MBytes   137 Mbits/sec   19             sender
    [  5]   0.00-10.01  sec   162 MBytes   136 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 67614130 bytes (64446 packets)
    ```

#### Xradio XR819

<img src=https://netbox.armbian.com/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.16.0-edge-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">8.01</span> Mbits/sec | <span style="font-size: 1.5rem;">5.98</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.130 port 59335 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   624 KBytes  5.11 Mbits/sec                  
    [  5]   1.00-2.00   sec   700 KBytes  5.73 Mbits/sec                  
    [  5]   2.00-3.00   sec   716 KBytes  5.86 Mbits/sec                  
    [  5]   3.00-4.00   sec   687 KBytes  5.63 Mbits/sec                  
    [  5]   4.00-5.00   sec   676 KBytes  5.54 Mbits/sec                  
    [  5]   5.00-6.00   sec   701 KBytes  5.75 Mbits/sec                  
    [  5]   6.00-7.00   sec   761 KBytes  6.23 Mbits/sec                  
    [  5]   7.00-8.00   sec   676 KBytes  5.54 Mbits/sec                  
    [  5]   8.00-9.00   sec   725 KBytes  5.94 Mbits/sec                  
    [  5]   9.00-10.00  sec   663 KBytes  5.43 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.07  sec  9.62 MBytes  8.01 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  6.77 MBytes  5.68 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.130 port 59255 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec   556 KBytes  4.55 Mbits/sec    2   22.6 KBytes       
    [  5]   1.00-2.00   sec   390 KBytes  3.20 Mbits/sec    1   21.2 KBytes       
    [  5]   2.00-3.00   sec   539 KBytes  4.41 Mbits/sec    0   32.5 KBytes       
    [  5]   3.00-4.00   sec   694 KBytes  5.69 Mbits/sec    0   39.6 KBytes       
    [  5]   4.00-5.00   sec   769 KBytes  6.30 Mbits/sec    0   48.1 KBytes       
    [  5]   5.00-6.00   sec   837 KBytes  6.86 Mbits/sec    0   53.7 KBytes       
    [  5]   6.00-7.00   sec   816 KBytes  6.68 Mbits/sec    1   42.4 KBytes       
    [  5]   7.00-8.00   sec   837 KBytes  6.86 Mbits/sec    0   50.9 KBytes       
    [  5]   8.00-9.00   sec   987 KBytes  8.09 Mbits/sec    0   55.1 KBytes       
    [  5]   9.00-10.00  sec   880 KBytes  7.20 Mbits/sec    0   55.1 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  7.13 MBytes  5.98 Mbits/sec    4             sender
    [  5]   0.00-10.04  sec  7.00 MBytes  5.85 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 51356 bytes (125 packets)
    TX: 59397 bytes (269 packets)
    signal: -38 dBm
    rx bitrate: 9.0 MBit/s
    tx bitrate: 58.5 MBit/s MCS 6
    
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

Access: <https://netbox.armbian.com/dcim/sites/>

- Sites in NetBox represent physical locations of wireless test equipment.
- Each site have devices such as Access Points (APs), iperf3 servers, and wireless test clients.
- Register your testing location first if it doesn't exist yet. Create a new site with a clear name (e.g., Office Berlin, Lab Maribor) and add necessary data.

!!! warning
    Make sure to check if site is not already define to not clutter database!

???+ success "Update Relevant Information"

    - Access point SSID: `Your SSID`
    - Iperf3 server IP: your local `IP address` that runs iperf3 server and can be accessible from wireless client

### 7. Register Device Type

Add [new device type](https://netbox.armbian.com/dcim/manufacturers/61/) 
 
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
