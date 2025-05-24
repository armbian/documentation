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
**Test Date:** [2025-05-24 09:15 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15225171778)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">58.0</span> Mbits/sec | <span style="font-size: 1.5rem;">60.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 58645 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.45 MBytes  54.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.73 MBytes  56.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.69 MBytes  56.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.59 MBytes  55.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.60 MBytes  55.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.58 MBytes  55.2 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.63 MBytes  55.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.66 MBytes  55.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.70 MBytes  56.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.61 MBytes  55.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  69.1 MBytes  58.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  66.2 MBytes  55.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 43917 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.98 MBytes  75.3 Mbits/sec    0    444 KBytes       
    [  5]   1.00-2.00   sec  6.71 MBytes  56.3 Mbits/sec    8    443 KBytes       
    [  5]   2.00-3.00   sec  7.02 MBytes  58.9 Mbits/sec    0    498 KBytes       
    [  5]   3.00-4.00   sec  6.96 MBytes  58.4 Mbits/sec    0    539 KBytes       
    [  5]   4.00-5.00   sec  7.08 MBytes  59.4 Mbits/sec    0    561 KBytes       
    [  5]   5.00-6.00   sec  7.00 MBytes  58.7 Mbits/sec    0    577 KBytes       
    [  5]   6.00-7.00   sec  7.11 MBytes  59.7 Mbits/sec    0    580 KBytes       
    [  5]   7.00-8.00   sec  7.01 MBytes  58.8 Mbits/sec    0    583 KBytes       
    [  5]   8.00-9.00   sec  7.00 MBytes  58.7 Mbits/sec    0    583 KBytes       
    [  5]   9.00-10.00  sec  7.00 MBytes  58.7 Mbits/sec    0    584 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  71.9 MBytes  60.3 Mbits/sec    8             sender
    [  5]   0.00-10.02  sec  69.0 MBytes  57.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 43790 bytes (166 packets)
    TX: 51833 bytes (203 packets)
    signal: -26 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">118</span> Mbits/sec | <span style="font-size: 1.5rem;">103</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 33211 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.4 MBytes   113 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.9 MBytes   117 Mbits/sec                  
    [  5]   4.00-5.00   sec  12.6 MBytes   106 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.7 MBytes   124 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.9 MBytes   117 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   9.00-10.00  sec  14.0 MBytes   117 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   141 MBytes   118 Mbits/sec  409             sender
    [  5]   0.00-10.00  sec   138 MBytes   115 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 40439 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.6 MBytes   106 Mbits/sec    0    389 KBytes       
    [  5]   1.00-2.00   sec  12.6 MBytes   105 Mbits/sec    0    452 KBytes       
    [  5]   2.00-3.00   sec  12.2 MBytes   103 Mbits/sec    0    475 KBytes       
    [  5]   3.00-4.00   sec  11.7 MBytes  98.0 Mbits/sec    0    475 KBytes       
    [  5]   4.00-5.00   sec  12.7 MBytes   106 Mbits/sec    0    523 KBytes       
    [  5]   5.00-6.00   sec  11.9 MBytes  99.6 Mbits/sec   60    382 KBytes       
    [  5]   6.00-7.00   sec  12.1 MBytes   101 Mbits/sec    0    440 KBytes       
    [  5]   7.00-8.00   sec  12.6 MBytes   105 Mbits/sec    0    478 KBytes       
    [  5]   8.00-9.00   sec  12.0 MBytes   101 Mbits/sec    0    499 KBytes       
    [  5]   9.00-10.00  sec  12.3 MBytes   103 Mbits/sec    0    512 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   123 MBytes   103 Mbits/sec   60             sender
    [  5]   0.00-10.02  sec   122 MBytes   102 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 141426 bytes (609 packets)
    TX: 62344 bytes (260 packets)
    signal: -35 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">271</span> Mbits/sec | <span style="font-size: 1.5rem;">258</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.163 port 39177 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  24.8 MBytes   207 Mbits/sec                  
    [  5]   1.00-2.00   sec  33.0 MBytes   277 Mbits/sec                  
    [  5]   2.00-3.00   sec  33.2 MBytes   279 Mbits/sec                  
    [  5]   3.00-4.00   sec  33.2 MBytes   279 Mbits/sec                  
    [  5]   4.00-5.00   sec  33.2 MBytes   279 Mbits/sec                  
    [  5]   5.00-6.00   sec  32.6 MBytes   274 Mbits/sec                  
    [  5]   6.00-7.00   sec  33.0 MBytes   277 Mbits/sec                  
    [  5]   7.00-8.00   sec  32.6 MBytes   274 Mbits/sec                  
    [  5]   8.00-9.00   sec  31.8 MBytes   266 Mbits/sec                  
    [  5]   9.00-10.00  sec  32.0 MBytes   268 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   323 MBytes   271 Mbits/sec  249             sender
    [  5]   0.00-10.00  sec   320 MBytes   268 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.163 port 56043 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  32.1 MBytes   269 Mbits/sec    0   1.84 MBytes       
    [  5]   1.00-2.00   sec  30.9 MBytes   259 Mbits/sec    0   2.18 MBytes       
    [  5]   2.00-3.00   sec  30.1 MBytes   253 Mbits/sec    0   2.53 MBytes       
    [  5]   3.00-4.00   sec  31.0 MBytes   260 Mbits/sec    0   2.53 MBytes       
    [  5]   4.00-5.00   sec  30.8 MBytes   258 Mbits/sec    0   2.83 MBytes       
    [  5]   5.00-6.00   sec  29.2 MBytes   245 Mbits/sec    0   2.83 MBytes       
    [  5]   6.00-7.00   sec  31.6 MBytes   265 Mbits/sec    0   2.83 MBytes       
    [  5]   7.00-8.00   sec  29.4 MBytes   246 Mbits/sec    0   3.54 MBytes       
    [  5]   8.00-9.00   sec  30.6 MBytes   257 Mbits/sec    0   3.54 MBytes       
    [  5]   9.00-10.00  sec  31.4 MBytes   263 Mbits/sec    0   3.54 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   307 MBytes   258 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   304 MBytes   254 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">578</span> Mbits/sec | <span style="font-size: 1.5rem;">603</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 57363 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  70.3 MBytes   589 Mbits/sec                  
    [  5]   1.00-2.00   sec  71.7 MBytes   602 Mbits/sec                  
    [  5]   2.00-3.00   sec  67.3 MBytes   565 Mbits/sec                  
    [  5]   3.00-4.00   sec  68.1 MBytes   571 Mbits/sec                  
    [  5]   4.00-5.00   sec  66.0 MBytes   554 Mbits/sec                  
    [  5]   5.00-6.00   sec  66.1 MBytes   554 Mbits/sec                  
    [  5]   6.00-7.00   sec  66.9 MBytes   561 Mbits/sec                  
    [  5]   7.00-8.00   sec  67.9 MBytes   570 Mbits/sec                  
    [  5]   8.00-9.00   sec  70.2 MBytes   589 Mbits/sec                  
    [  5]   9.00-10.00  sec  72.4 MBytes   607 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   689 MBytes   578 Mbits/sec  422             sender
    [  5]   0.00-10.00  sec   687 MBytes   576 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 38269 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.01   sec  78.0 MBytes   651 Mbits/sec    0   5.21 MBytes       
    [  5]   1.01-2.00   sec  78.8 MBytes   664 Mbits/sec    0   5.21 MBytes       
    [  5]   2.00-3.00   sec  78.8 MBytes   661 Mbits/sec    0   5.21 MBytes       
    [  5]   3.00-4.00   sec  76.2 MBytes   640 Mbits/sec  114   2.60 MBytes       
    [  5]   4.00-5.00   sec  73.8 MBytes   619 Mbits/sec  202    696 KBytes       
    [  5]   5.00-6.00   sec  66.2 MBytes   556 Mbits/sec    0    823 KBytes       
    [  5]   6.00-7.00   sec  70.0 MBytes   587 Mbits/sec    0    939 KBytes       
    [  5]   7.00-8.00   sec  72.5 MBytes   608 Mbits/sec    0   1.02 MBytes       
    [  5]   8.00-9.00   sec  62.5 MBytes   524 Mbits/sec  112    638 KBytes       
    [  5]   9.00-10.00  sec  62.5 MBytes   525 Mbits/sec    0    768 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   719 MBytes   603 Mbits/sec  428             sender
    [  5]   0.00-10.01  sec   717 MBytes   601 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 129317 bytes (457 packets)
    TX: 58526 bytes (217 packets)
    signal: -31 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">676</span> Mbits/sec | <span style="font-size: 1.5rem;">665</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 48693 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  92.5 MBytes   775 Mbits/sec                  
    [  5]   1.00-2.00   sec  82.5 MBytes   692 Mbits/sec                  
    [  5]   2.00-3.00   sec  78.1 MBytes   655 Mbits/sec                  
    [  5]   3.00-4.00   sec  74.0 MBytes   621 Mbits/sec                  
    [  5]   4.00-5.00   sec  77.4 MBytes   649 Mbits/sec                  
    [  5]   5.00-6.00   sec  79.1 MBytes   664 Mbits/sec                  
    [  5]   6.00-7.00   sec  91.9 MBytes   771 Mbits/sec                  
    [  5]   7.00-8.00   sec  74.6 MBytes   626 Mbits/sec                  
    [  5]   8.00-9.00   sec  75.2 MBytes   631 Mbits/sec                  
    [  5]   9.00-10.00  sec  77.1 MBytes   647 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   806 MBytes   676 Mbits/sec  661             sender
    [  5]   0.00-10.00  sec   803 MBytes   673 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 47315 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  94.0 MBytes   788 Mbits/sec    0   5.21 MBytes       
    [  5]   1.00-2.00   sec  82.2 MBytes   690 Mbits/sec  564   1.36 MBytes       
    [  5]   2.00-3.00   sec  95.9 MBytes   804 Mbits/sec    0   1.46 MBytes       
    [  5]   3.00-4.00   sec  72.9 MBytes   611 Mbits/sec  350    846 KBytes       
    [  5]   4.00-5.00   sec  63.1 MBytes   530 Mbits/sec   61    574 KBytes       
    [  5]   5.00-6.00   sec  79.1 MBytes   664 Mbits/sec    0    745 KBytes       
    [  5]   6.00-7.00   sec  83.8 MBytes   703 Mbits/sec    0    894 KBytes       
    [  5]   7.00-8.00   sec  83.5 MBytes   700 Mbits/sec   91    515 KBytes       
    [  5]   8.00-9.00   sec  69.9 MBytes   586 Mbits/sec    0    686 KBytes       
    [  5]   9.00-10.00  sec  68.5 MBytes   574 Mbits/sec  219    467 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   793 MBytes   665 Mbits/sec  1285             sender
    [  5]   0.00-10.01  sec   790 MBytes   662 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 59066 bytes (234 packets)
    TX: 58924 bytes (249 packets)
    signal: -33 dBm
    rx bitrate: 1921.5 MBit/s 160MHz HE-MCS 9 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 2041.6 MBit/s 160MHz HE-MCS 11 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">51.1</span> Mbits/sec | <span style="font-size: 1.5rem;">31.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.164 port 42617 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.75 MBytes  48.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.05 MBytes  50.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.09 MBytes  42.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.02 MBytes  50.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.33 MBytes  53.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.12 MBytes  51.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.05 MBytes  50.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.23 MBytes  52.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.93 MBytes  49.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.47 MBytes  54.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.41  sec  63.4 MBytes  51.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  60.0 MBytes  50.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.164 port 34215 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.57 MBytes  29.9 Mbits/sec    1   73.5 KBytes       
    [  5]   1.00-2.00   sec  3.75 MBytes  31.5 Mbits/sec    0    105 KBytes       
    [  5]   2.00-3.00   sec  3.85 MBytes  32.3 Mbits/sec    0    129 KBytes       
    [  5]   3.00-4.00   sec  3.91 MBytes  32.8 Mbits/sec    0    148 KBytes       
    [  5]   4.00-5.00   sec  4.35 MBytes  36.5 Mbits/sec    0    163 KBytes       
    [  5]   5.00-6.00   sec  2.98 MBytes  25.0 Mbits/sec    8    119 KBytes       
    [  5]   6.00-7.00   sec  2.61 MBytes  21.9 Mbits/sec    0    143 KBytes       
    [  5]   7.00-8.00   sec  3.36 MBytes  28.1 Mbits/sec    0    158 KBytes       
    [  5]   8.00-9.00   sec  4.16 MBytes  34.9 Mbits/sec    0    164 KBytes       
    [  5]   9.00-10.00  sec  4.41 MBytes  37.0 Mbits/sec    0    165 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  37.0 MBytes  31.0 Mbits/sec    9             sender
    [  5]   0.00-10.03  sec  36.6 MBytes  30.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 81299 bytes (328 packets)
    TX: 71010 bytes (287 packets)
    signal: -54 dBm
    rx bitrate: 65.0 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">49.7</span> Mbits/sec | <span style="font-size: 1.5rem;">54.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 43919 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.18 MBytes  43.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.06 MBytes  42.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.37 MBytes  45.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.30 MBytes  44.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.33 MBytes  44.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  7.02 MBytes  58.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.63 MBytes  55.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.46 MBytes  45.8 Mbits/sec                  
    [  5]   9.00-10.00  sec  7.42 MBytes  62.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.44  sec  61.9 MBytes  49.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  58.3 MBytes  48.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 48845 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.03 MBytes  58.9 Mbits/sec    0    229 KBytes       
    [  5]   1.00-2.00   sec  6.52 MBytes  54.7 Mbits/sec    0    262 KBytes       
    [  5]   2.00-3.00   sec  5.65 MBytes  47.4 Mbits/sec    0    276 KBytes       
    [  5]   3.00-4.00   sec  6.40 MBytes  53.7 Mbits/sec    0    310 KBytes       
    [  5]   4.00-5.00   sec  6.96 MBytes  58.4 Mbits/sec    0    310 KBytes       
    [  5]   5.00-6.00   sec  5.78 MBytes  48.5 Mbits/sec    0    310 KBytes       
    [  5]   6.00-7.00   sec  5.90 MBytes  49.5 Mbits/sec    0    310 KBytes       
    [  5]   7.00-8.00   sec  7.83 MBytes  65.7 Mbits/sec    0    395 KBytes       
    [  5]   8.00-9.00   sec  6.46 MBytes  54.2 Mbits/sec    0    395 KBytes       
    [  5]   9.00-10.00  sec  6.46 MBytes  54.2 Mbits/sec    0    395 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  65.0 MBytes  54.5 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  62.9 MBytes  52.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 51557 bytes (182 packets)
    TX: 55817 bytes (222 packets)
    signal: -48 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 390.0 MBit/s
    
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">35.9</span> Mbits/sec | <span style="font-size: 1.5rem;">47.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 40753 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.74 MBytes  48.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.09 MBytes  42.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.11 MBytes  34.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.43 MBytes  37.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.67 MBytes  30.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.72 MBytes  14.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.07 MBytes  34.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.70 MBytes  31.0 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.10 MBytes  26.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.44 MBytes  28.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  42.9 MBytes  35.9 Mbits/sec   21             sender
    [  5]   0.00-10.00  sec  39.1 MBytes  32.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 38331 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.36 MBytes  53.3 Mbits/sec    0    298 KBytes       
    [  5]   1.00-2.00   sec  5.65 MBytes  47.4 Mbits/sec    0    329 KBytes       
    [  5]   2.00-3.00   sec  5.72 MBytes  48.0 Mbits/sec    0    365 KBytes       
    [  5]   3.00-4.00   sec  5.34 MBytes  44.8 Mbits/sec    0    365 KBytes       
    [  5]   4.00-5.00   sec  5.59 MBytes  46.9 Mbits/sec    0    365 KBytes       
    [  5]   5.00-6.00   sec  5.72 MBytes  48.0 Mbits/sec    0    365 KBytes       
    [  5]   6.00-7.00   sec  5.47 MBytes  45.9 Mbits/sec    0    365 KBytes       
    [  5]   7.00-8.00   sec  5.47 MBytes  45.9 Mbits/sec    0    383 KBytes       
    [  5]   8.00-9.00   sec  5.65 MBytes  47.4 Mbits/sec    0    383 KBytes       
    [  5]   9.00-10.00  sec  5.65 MBytes  47.4 Mbits/sec    0    383 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  56.6 MBytes  47.5 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  55.9 MBytes  46.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```

    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">144</span> Mbits/sec | <span style="font-size: 1.5rem;">141</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 42225 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.3 MBytes   128 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.9 MBytes   141 Mbits/sec                  
    [  5]   3.00-4.00   sec  17.1 MBytes   143 Mbits/sec                  
    [  5]   4.00-5.00   sec  14.8 MBytes   124 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.8 MBytes   158 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.1 MBytes   143 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   171 MBytes   144 Mbits/sec  351             sender
    [  5]   0.00-10.00  sec   168 MBytes   141 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 37751 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.9 MBytes   159 Mbits/sec    0    461 KBytes       
    [  5]   1.00-2.00   sec  16.3 MBytes   137 Mbits/sec    0    461 KBytes       
    [  5]   2.00-3.00   sec  16.0 MBytes   134 Mbits/sec    0    461 KBytes       
    [  5]   3.00-4.00   sec  17.0 MBytes   142 Mbits/sec    0    461 KBytes       
    [  5]   4.00-5.00   sec  16.2 MBytes   136 Mbits/sec    0    461 KBytes       
    [  5]   5.00-6.00   sec  17.1 MBytes   143 Mbits/sec    0    461 KBytes       
    [  5]   6.00-7.00   sec  16.1 MBytes   135 Mbits/sec    0    461 KBytes       
    [  5]   7.00-8.00   sec  17.1 MBytes   143 Mbits/sec    0    461 KBytes       
    [  5]   8.00-9.00   sec  16.1 MBytes   135 Mbits/sec    0    461 KBytes       
    [  5]   9.00-10.00  sec  17.0 MBytes   143 Mbits/sec    0    461 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   168 MBytes   141 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   165 MBytes   138 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 1832022069 bytes (1528062 packets)
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
