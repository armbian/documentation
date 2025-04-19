---
comments: true
---
# Testing the speed of wireless adapters

All wireless adapters were tested under consistent conditions - each positioned in close proximity (1-2m) and connected to the same wireless access point (AP). The adapters utilized various interface types, including USB, SDIO, and PCI, to evaluate performance across different hardware configurations.

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

- **Infrastructure Database**: [NetBox](https://netbox.dev) for resource modeling and inventory
- **Automation**: GitHub Actions for workflow orchestration and test execution
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
**Test Date:** [15.3.2025](https://github.com/armbian/armbian.github.io/actions/runs/14422377005)
### Realtek 8188CUS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8192CU.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8192CU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">45.3</span> Mbits/sec | <span style="font-size: 1.5rem;">43.2</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.245 port 38909 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.12 MBytes  42.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.50 MBytes  46.2 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.12 MBytes  43.0 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.25  sec  55.4 MBytes  45.3 Mbits/sec   35             sender
    [  5]   0.00-10.00  sec  52.2 MBytes  43.8 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.245 port 53065 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.25 MBytes  52.4 Mbits/sec    0    253 KBytes       
    [  5]   1.00-2.00   sec  4.75 MBytes  39.8 Mbits/sec    0    344 KBytes       
    [  5]   2.00-3.00   sec  5.00 MBytes  41.9 Mbits/sec    0    349 KBytes       
    [  5]   3.00-4.00   sec  4.38 MBytes  36.7 Mbits/sec    0    349 KBytes       
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec    0    349 KBytes       
    [  5]   5.00-6.00   sec  4.50 MBytes  37.7 Mbits/sec    0    349 KBytes       
    [  5]   6.00-7.00   sec  5.12 MBytes  43.0 Mbits/sec    0    369 KBytes       
    [  5]   7.00-8.00   sec  5.75 MBytes  48.2 Mbits/sec    0    393 KBytes       
    [  5]   8.00-9.00   sec  4.88 MBytes  40.9 Mbits/sec    0    393 KBytes       
    [  5]   9.00-10.00  sec  5.75 MBytes  48.2 Mbits/sec    0    464 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  51.5 MBytes  43.2 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  49.4 MBytes  41.3 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 2462.0
    RX: 86152 bytes (339 packets)
    TX: 60846 bytes (234 packets)
    signal: -28 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">97.6</span> Mbits/sec | <span style="font-size: 1.5rem;">67.5</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.246 port 53395 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.5 MBytes  88.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.6 MBytes  97.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   116 MBytes  97.6 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   114 MBytes  95.5 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.246 port 34547 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.12 MBytes  76.5 Mbits/sec    0    242 KBytes       
    [  5]   1.00-2.00   sec  7.38 MBytes  61.9 Mbits/sec    0    274 KBytes       
    [  5]   2.00-3.00   sec  7.50 MBytes  62.9 Mbits/sec    0    274 KBytes       
    [  5]   3.00-4.00   sec  7.88 MBytes  66.1 Mbits/sec    0    274 KBytes       
    [  5]   4.00-5.00   sec  7.88 MBytes  66.1 Mbits/sec    0    297 KBytes       
    [  5]   5.00-6.00   sec  8.25 MBytes  69.2 Mbits/sec    0    314 KBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0    339 KBytes       
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec    0    358 KBytes       
    [  5]   8.00-9.00   sec  8.00 MBytes  67.1 Mbits/sec    0    403 KBytes       
    [  5]   9.00-10.00  sec  9.12 MBytes  76.5 Mbits/sec    0    549 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  80.5 MBytes  67.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  77.4 MBytes  64.9 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500.0
    RX: 205689 bytes (656 packets)
    TX: 103453 bytes (546 packets)
    signal: -17 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

### Realtek 8822CE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8822CE.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.21-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">318</span> Mbits/sec | <span style="font-size: 1.5rem;">530</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.244 port 46891 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  50.3 MBytes   422 Mbits/sec                  
    [  5]   1.00-2.00   sec  40.4 MBytes   339 Mbits/sec                  
    [  5]   2.00-3.00   sec  34.9 MBytes   293 Mbits/sec                  
    [  5]   3.00-4.00   sec  37.9 MBytes   318 Mbits/sec                  
    [  5]   4.00-5.00   sec  37.4 MBytes   314 Mbits/sec                  
    [  5]   5.00-6.00   sec  37.6 MBytes   315 Mbits/sec                  
    [  5]   6.00-7.00   sec  35.6 MBytes   299 Mbits/sec                  
    [  5]   7.00-8.00   sec  37.7 MBytes   316 Mbits/sec                  
    [  5]   8.00-9.00   sec  36.3 MBytes   305 Mbits/sec                  
    [  5]   9.00-10.00  sec  28.7 MBytes   241 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   380 MBytes   318 Mbits/sec  271             sender
    [  5]   0.00-10.00  sec   377 MBytes   316 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.244 port 41513 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  68.0 MBytes   570 Mbits/sec    0   5.27 MBytes       
    [  5]   1.00-2.00   sec  53.8 MBytes   451 Mbits/sec    0   5.27 MBytes       
    [  5]   2.00-3.01   sec  61.2 MBytes   511 Mbits/sec    0   5.27 MBytes       
    [  5]   3.01-4.00   sec  66.2 MBytes   559 Mbits/sec    0   5.27 MBytes       
    [  5]   4.00-5.00   sec  65.0 MBytes   545 Mbits/sec    0   5.27 MBytes       
    [  5]   5.00-6.01   sec  66.2 MBytes   552 Mbits/sec    0   5.27 MBytes       
    [  5]   6.01-7.01   sec  66.2 MBytes   556 Mbits/sec   62   2.64 MBytes       
    [  5]   7.01-8.00   sec  65.0 MBytes   547 Mbits/sec    1   1.34 MBytes       
    [  5]   8.00-9.00   sec  61.2 MBytes   515 Mbits/sec  603    720 KBytes       
    [  5]   9.00-10.00  sec  58.8 MBytes   493 Mbits/sec    0    831 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   632 MBytes   530 Mbits/sec  666             sender
    [  5]   0.00-10.01  sec   630 MBytes   528 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500
    RX: 126010 bytes (465 packets)
    TX: 59523 bytes (214 packets)
    signal: -32 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 780.0 MBit/s VHT-MCS 8 80MHz short GI VHT-NSS 2
    
    ```

### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">904</span> Mbits/sec | <span style="font-size: 1.5rem;">706</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.229 port 41331 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec   100 MBytes   840 Mbits/sec                  
    [  5]   1.00-2.00   sec   111 MBytes   930 Mbits/sec                  
    [  5]   2.00-3.00   sec   111 MBytes   932 Mbits/sec                  
    [  5]   3.00-4.00   sec   111 MBytes   929 Mbits/sec                  
    [  5]   4.00-5.00   sec   108 MBytes   908 Mbits/sec                  
    [  5]   5.00-6.00   sec   106 MBytes   885 Mbits/sec                  
    [  5]   6.00-7.00   sec   102 MBytes   860 Mbits/sec                  
    [  5]   7.00-8.00   sec   107 MBytes   895 Mbits/sec                  
    [  5]   8.00-9.00   sec   110 MBytes   922 Mbits/sec                  
    [  5]   9.00-10.00  sec   109 MBytes   912 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  1.05 GBytes   904 Mbits/sec  386             sender
    [  5]   0.00-10.00  sec  1.05 GBytes   901 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.229 port 35517 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  95.8 MBytes   802 Mbits/sec   11   2.21 MBytes       
    [  5]   1.00-2.00   sec  66.4 MBytes   557 Mbits/sec  139   1.11 MBytes       
    [  5]   2.00-3.00   sec  90.9 MBytes   762 Mbits/sec  153    672 KBytes       
    [  5]   3.00-4.00   sec  91.6 MBytes   769 Mbits/sec    0    846 KBytes       
    [  5]   4.00-5.00   sec  77.0 MBytes   646 Mbits/sec    0    967 KBytes       
    [  5]   5.00-6.00   sec  82.8 MBytes   694 Mbits/sec  162    632 KBytes       
    [  5]   6.00-7.00   sec  84.0 MBytes   705 Mbits/sec    0    800 KBytes       
    [  5]   7.00-8.00   sec  87.5 MBytes   734 Mbits/sec   29    549 KBytes       
    [  5]   8.00-9.00   sec  86.1 MBytes   722 Mbits/sec    0    742 KBytes       
    [  5]   9.00-10.00  sec  80.4 MBytes   674 Mbits/sec   60    503 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   842 MBytes   706 Mbits/sec  554             sender
    [  5]   0.00-10.01  sec   839 MBytes   703 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500.0
    RX: 34965 bytes (133 packets)
    TX: 46200 bytes (195 packets)
    signal: -33 dBm
    rx bitrate: 1297.1 MBit/s 160MHz HE-MCS 6 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```

### Realtek 8814AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8814AU.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8814AU</span> | <span style="font-size: 1.5rem;">AC1200</span> | <span style="font-size: 1.5rem;">154</span> Mbits/sec | <span style="font-size: 1.5rem;">275</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.101 port 44807 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.4 MBytes   146 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.1 MBytes   152 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   184 MBytes   154 Mbits/sec    4             sender
    [  5]   0.00-10.00  sec   181 MBytes   152 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.101 port 60619 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  35.6 MBytes   299 Mbits/sec    0    608 KBytes       
    [  5]   1.00-2.00   sec  31.8 MBytes   266 Mbits/sec    0    755 KBytes       
    [  5]   2.00-3.00   sec  32.5 MBytes   273 Mbits/sec    0    795 KBytes       
    [  5]   3.00-4.00   sec  32.6 MBytes   274 Mbits/sec    0    795 KBytes       
    [  5]   4.00-5.00   sec  32.4 MBytes   272 Mbits/sec    0    795 KBytes       
    [  5]   5.00-6.00   sec  32.6 MBytes   274 Mbits/sec    0    795 KBytes       
    [  5]   6.00-7.00   sec  32.6 MBytes   274 Mbits/sec    0    795 KBytes       
    [  5]   7.00-8.00   sec  32.4 MBytes   272 Mbits/sec    0    836 KBytes       
    [  5]   8.00-9.00   sec  32.4 MBytes   272 Mbits/sec    0    836 KBytes       
    [  5]   9.00-10.00  sec  32.6 MBytes   274 Mbits/sec    0    836 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   328 MBytes   275 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   324 MBytes   272 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500.0
    signal: -36 dBm
    tx bitrate: 867.0 MBit/s
    ```

### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">23.2</span> Mbits/sec | <span style="font-size: 1.5rem;">33.9</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.252 port 57637 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.00 MBytes  25.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  3.50 MBytes  29.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.38 MBytes  19.9 Mbits/sec                  
    [  5]   5.00-6.00   sec   896 KBytes  7.34 Mbits/sec                  
    [  5]   6.00-7.00   sec  1.00 MBytes  8.39 Mbits/sec                  
    [  5]   7.00-8.00   sec   896 KBytes  7.34 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.75 MBytes  31.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.11  sec  28.0 MBytes  23.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  25.4 MBytes  21.3 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.252 port 52535 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.25 MBytes  44.0 Mbits/sec    0    279 KBytes       
    [  5]   1.00-2.00   sec  4.00 MBytes  33.6 Mbits/sec    0    335 KBytes       
    [  5]   2.00-3.00   sec  4.12 MBytes  34.6 Mbits/sec    0    335 KBytes       
    [  5]   3.00-4.00   sec  4.12 MBytes  34.6 Mbits/sec    0    335 KBytes       
    [  5]   4.00-5.00   sec  4.25 MBytes  35.7 Mbits/sec    0    355 KBytes       
    [  5]   5.00-6.00   sec  3.75 MBytes  31.4 Mbits/sec    0    355 KBytes       
    [  5]   6.00-7.00   sec  3.75 MBytes  31.5 Mbits/sec    0    355 KBytes       
    [  5]   7.00-8.00   sec  3.88 MBytes  32.5 Mbits/sec    0    393 KBytes       
    [  5]   8.00-9.00   sec  4.00 MBytes  33.6 Mbits/sec    0    393 KBytes       
    [  5]   9.00-10.00  sec  3.25 MBytes  27.3 Mbits/sec    0    393 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  40.4 MBytes  33.9 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  38.9 MBytes  32.5 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 2462.0
    RX: 87135 bytes (367 packets)
    TX: 57009 bytes (213 packets)
    signal: -36 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC600</span> | <span style="font-size: 1.5rem;">153</span> Mbits/sec | <span style="font-size: 1.5rem;">195</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.254 port 44881 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  14.4 MBytes   120 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.6 MBytes   156 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.4 MBytes   154 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   183 MBytes   153 Mbits/sec   33             sender
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.254 port 34613 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  24.8 MBytes   207 Mbits/sec    0    718 KBytes       
    [  5]   1.00-2.00   sec  22.6 MBytes   190 Mbits/sec    0    798 KBytes       
    [  5]   2.00-3.00   sec  21.2 MBytes   178 Mbits/sec    0    839 KBytes       
    [  5]   3.00-4.00   sec  22.5 MBytes   189 Mbits/sec    0    839 KBytes       
    [  5]   4.00-5.00   sec  24.2 MBytes   203 Mbits/sec    0    839 KBytes       
    [  5]   5.00-6.00   sec  22.4 MBytes   188 Mbits/sec    0    884 KBytes       
    [  5]   6.00-7.00   sec  24.9 MBytes   209 Mbits/sec    0    935 KBytes       
    [  5]   7.00-8.00   sec  21.0 MBytes   176 Mbits/sec   59    653 KBytes       
    [  5]   8.00-9.00   sec  23.4 MBytes   196 Mbits/sec    0    675 KBytes       
    [  5]   9.00-10.00  sec  25.0 MBytes   210 Mbits/sec    0    675 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   232 MBytes   195 Mbits/sec   59             sender
    [  5]   0.00-10.01  sec   228 MBytes   191 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500.0
    signal: -37 dBm
    tx bitrate: 434.0 MBit/s
    ```

### Atheros AR9271

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AR9271.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AR9271</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">57.9</span> Mbits/sec | <span style="font-size: 1.5rem;">52.4</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.247 port 34851 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.38 MBytes  53.4 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.75 MBytes  56.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.62 MBytes  55.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.75 MBytes  56.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.38 MBytes  53.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec  69.2 MBytes  57.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  65.8 MBytes  55.1 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.247 port 55677 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.88 MBytes  57.6 Mbits/sec    0    195 KBytes       
    [  5]   1.00-2.00   sec  6.12 MBytes  51.4 Mbits/sec    0    204 KBytes       
    [  5]   2.00-3.00   sec  6.25 MBytes  52.4 Mbits/sec    0    239 KBytes       
    [  5]   3.00-4.00   sec  6.12 MBytes  51.4 Mbits/sec    0    250 KBytes       
    [  5]   4.00-5.00   sec  6.38 MBytes  53.5 Mbits/sec    0    262 KBytes       
    [  5]   5.00-6.00   sec  6.12 MBytes  51.4 Mbits/sec    0    262 KBytes       
    [  5]   6.00-7.00   sec  5.62 MBytes  47.2 Mbits/sec    0    262 KBytes       
    [  5]   7.00-8.00   sec  6.12 MBytes  51.4 Mbits/sec    0    262 KBytes       
    [  5]   8.00-9.00   sec  6.12 MBytes  51.4 Mbits/sec    0    262 KBytes       
    [  5]   9.00-10.00  sec  6.75 MBytes  56.6 Mbits/sec    0    262 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  62.5 MBytes  52.4 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  61.1 MBytes  51.2 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 2462.0
    RX: 82572 bytes (352 packets)
    TX: 56542 bytes (204 packets)
    signal: -52 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC600</span> | <span style="font-size: 1.5rem;">155</span> Mbits/sec | <span style="font-size: 1.5rem;">271</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.100 port 46441 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   2.00-3.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   3.00-4.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   6.00-7.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.2 MBytes   153 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.4 MBytes   154 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   185 MBytes   155 Mbits/sec    3             sender
    [  5]   0.00-10.00  sec   182 MBytes   153 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.100 port 45805 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  33.5 MBytes   281 Mbits/sec    0    823 KBytes       
    [  5]   1.00-2.00   sec  32.9 MBytes   276 Mbits/sec    0   1.03 MBytes       
    [  5]   2.00-3.00   sec  32.2 MBytes   271 Mbits/sec    5    805 KBytes       
    [  5]   3.00-4.00   sec  32.4 MBytes   272 Mbits/sec    0    860 KBytes       
    [  5]   4.00-5.00   sec  31.6 MBytes   265 Mbits/sec    0    950 KBytes       
    [  5]   5.00-6.00   sec  32.5 MBytes   273 Mbits/sec    0    963 KBytes       
    [  5]   6.00-7.00   sec  31.5 MBytes   264 Mbits/sec    0   1.01 MBytes       
    [  5]   7.00-8.00   sec  33.2 MBytes   279 Mbits/sec    0   1.02 MBytes       
    [  5]   8.00-9.00   sec  32.0 MBytes   268 Mbits/sec  143    779 KBytes       
    [  5]   9.00-10.00  sec  31.8 MBytes   266 Mbits/sec    0    824 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   324 MBytes   271 Mbits/sec  148             sender
    [  5]   0.00-10.01  sec   321 MBytes   269 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500.0
    signal: -35 dBm
    tx bitrate: 867.0 MBit/s
    ```

### Realtek 8852BE

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8852BE.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8852BE</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">468</span> Mbits/sec | <span style="font-size: 1.5rem;">424</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.230 port 40491 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  55.8 MBytes   468 Mbits/sec                  
    [  5]   1.00-2.00   sec  53.9 MBytes   452 Mbits/sec                  
    [  5]   2.00-3.00   sec  55.9 MBytes   469 Mbits/sec                  
    [  5]   3.00-4.00   sec  54.3 MBytes   455 Mbits/sec                  
    [  5]   4.00-5.00   sec  54.7 MBytes   459 Mbits/sec                  
    [  5]   5.00-6.00   sec  56.9 MBytes   478 Mbits/sec                  
    [  5]   6.00-7.00   sec  57.0 MBytes   478 Mbits/sec                  
    [  5]   7.00-8.00   sec  54.8 MBytes   459 Mbits/sec                  
    [  5]   8.00-9.00   sec  55.4 MBytes   465 Mbits/sec                  
    [  5]   9.00-10.00  sec  55.7 MBytes   467 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   558 MBytes   468 Mbits/sec  293             sender
    [  5]   0.00-10.00  sec   555 MBytes   465 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.230 port 48919 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  35.6 MBytes   299 Mbits/sec    0   4.88 MBytes       
    [  5]   1.00-2.00   sec  33.8 MBytes   283 Mbits/sec    0   6.44 MBytes       
    [  5]   2.00-3.00   sec  32.5 MBytes   273 Mbits/sec    0   6.44 MBytes       
    [  5]   3.00-4.00   sec  52.5 MBytes   440 Mbits/sec   37   3.22 MBytes       
    [  5]   4.00-5.00   sec  58.8 MBytes   493 Mbits/sec    0   3.22 MBytes       
    [  5]   5.00-6.00   sec  58.8 MBytes   493 Mbits/sec    0   3.22 MBytes       
    [  5]   6.00-7.00   sec  57.5 MBytes   482 Mbits/sec    0   3.22 MBytes       
    [  5]   7.00-8.00   sec  58.8 MBytes   493 Mbits/sec    0   3.22 MBytes       
    [  5]   8.00-9.00   sec  58.8 MBytes   493 Mbits/sec    0   3.22 MBytes       
    [  5]   9.00-10.00  sec  58.8 MBytes   493 Mbits/sec    0   3.22 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   506 MBytes   424 Mbits/sec   37             sender
    [  5]   0.00-10.02  sec   504 MBytes   422 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500
    RX: 98627 bytes (407 packets)
    TX: 53367 bytes (196 packets)
    signal: -30 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    
    ```

### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">27.4</span> Mbits/sec | <span style="font-size: 1.5rem;">9.96</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.250 port 56283 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  3.25 MBytes  27.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.00 MBytes  25.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.12 MBytes  17.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.88 MBytes  24.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  3.38 MBytes  28.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  3.25 MBytes  27.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  3.38 MBytes  28.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.12  sec  33.0 MBytes  27.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  30.2 MBytes  25.4 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.250 port 32979 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  3.25 MBytes  27.3 Mbits/sec    0    163 KBytes       
    [  5]   1.00-2.00   sec   896 KBytes  7.34 Mbits/sec    1    136 KBytes       
    [  5]   2.00-3.00   sec   896 KBytes  7.34 Mbits/sec    3   50.9 KBytes       
    [  5]   3.00-4.00   sec  1.12 MBytes  9.44 Mbits/sec    3   33.9 KBytes       
    [  5]   4.00-5.00   sec  1.12 MBytes  9.44 Mbits/sec    2   45.2 KBytes       
    [  5]   5.00-6.00   sec   896 KBytes  7.35 Mbits/sec    2   36.8 KBytes       
    [  5]   6.00-7.00   sec  1.25 MBytes  10.5 Mbits/sec   10   15.6 KBytes       
    [  5]   7.00-8.00   sec   896 KBytes  7.34 Mbits/sec    1   35.4 KBytes       
    [  5]   8.00-9.00   sec   768 KBytes  6.29 Mbits/sec    3   42.4 KBytes       
    [  5]   9.00-10.00  sec   896 KBytes  7.34 Mbits/sec    2   32.5 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  11.9 MBytes  9.96 Mbits/sec   27             sender
    [  5]   0.00-10.01  sec  11.0 MBytes  9.22 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 2462.0
    RX: 80823 bytes (356 packets)
    TX: 56930 bytes (208 packets)
    signal: -31 dBm
    rx bitrate: 52.0 MBit/s MCS 5
    tx bitrate: 65.0 MBit/s MCS 7
    ```

### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">95.2</span> Mbits/sec | <span style="font-size: 1.5rem;">67.4</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.251 port 34495 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.4 MBytes  86.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   114 MBytes  95.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   112 MBytes  93.7 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.251 port 34569 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.00 MBytes  75.4 Mbits/sec    0    206 KBytes       
    [  5]   1.00-2.00   sec  8.00 MBytes  67.1 Mbits/sec    0    230 KBytes       
    [  5]   2.00-3.00   sec  8.25 MBytes  69.2 Mbits/sec    0    263 KBytes       
    [  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec    0    287 KBytes       
    [  5]   4.00-5.00   sec  8.12 MBytes  68.1 Mbits/sec    0    287 KBytes       
    [  5]   5.00-6.00   sec  7.88 MBytes  66.1 Mbits/sec    0    303 KBytes       
    [  5]   6.00-7.00   sec  8.00 MBytes  67.1 Mbits/sec    0    303 KBytes       
    [  5]   7.00-8.00   sec  8.12 MBytes  68.1 Mbits/sec    0    303 KBytes       
    [  5]   8.00-9.00   sec  8.12 MBytes  68.2 Mbits/sec    0    303 KBytes       
    [  5]   9.00-10.00  sec  7.38 MBytes  61.8 Mbits/sec    0    303 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  80.4 MBytes  67.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  79.1 MBytes  66.4 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500.0
    RX: 212032 bytes (654 packets)
    TX: 119823 bytes (600 packets)
    signal: -28 dBm
    rx bitrate: 270.0 MBit/s MCS 14 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">113</span> Mbits/sec | <span style="font-size: 1.5rem;">149</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.248 port 41421 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.4 MBytes   112 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   135 MBytes   113 Mbits/sec    1             sender
    [  5]   0.00-10.00  sec   133 MBytes   111 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.248 port 37601 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.1 MBytes   160 Mbits/sec    0    568 KBytes       
    [  5]   1.00-2.00   sec  18.0 MBytes   151 Mbits/sec    0    824 KBytes       
    [  5]   2.00-3.00   sec  17.0 MBytes   143 Mbits/sec    0    824 KBytes       
    [  5]   3.00-4.00   sec  18.5 MBytes   155 Mbits/sec    0    872 KBytes       
    [  5]   4.00-5.00   sec  16.5 MBytes   138 Mbits/sec    0    971 KBytes       
    [  5]   5.00-6.00   sec  17.9 MBytes   150 Mbits/sec    0   1.16 MBytes       
    [  5]   6.00-7.00   sec  18.1 MBytes   152 Mbits/sec    0   1.16 MBytes       
    [  5]   7.00-8.00   sec  16.8 MBytes   140 Mbits/sec    0   1.16 MBytes       
    [  5]   8.00-9.00   sec  17.5 MBytes   147 Mbits/sec    0   1.16 MBytes       
    [  5]   9.00-10.00  sec  18.1 MBytes   152 Mbits/sec    0   1.16 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   178 MBytes   149 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   174 MBytes   146 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500.0
    RX: 46199 bytes (195 packets)
    TX: 54572 bytes (199 packets)
    signal: -42 dBm
    rx bitrate: 1080.6 MBit/s 80MHz HE-MCS 10 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```

### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC600</span> | <span style="font-size: 1.5rem;">95.4</span> Mbits/sec | <span style="font-size: 1.5rem;">90.8</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.249 port 46325 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  11.0 MBytes  92.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  11.0 MBytes  92.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.8 MBytes  98.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.05  sec   114 MBytes  95.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   113 MBytes  95.1 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.249 port 51445 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.8 MBytes   107 Mbits/sec    0    574 KBytes       
    [  5]   1.00-2.00   sec  10.8 MBytes  90.2 Mbits/sec    0    752 KBytes       
    [  5]   2.00-3.00   sec  9.62 MBytes  80.7 Mbits/sec    0    752 KBytes       
    [  5]   3.00-4.00   sec  11.4 MBytes  95.4 Mbits/sec    0    872 KBytes       
    [  5]   4.00-5.00   sec  9.75 MBytes  81.8 Mbits/sec    0    923 KBytes       
    [  5]   5.00-6.00   sec  9.62 MBytes  80.7 Mbits/sec    0    923 KBytes       
    [  5]   6.00-7.00   sec  11.1 MBytes  93.3 Mbits/sec    0    923 KBytes       
    [  5]   7.00-8.00   sec  11.0 MBytes  92.3 Mbits/sec    0    923 KBytes       
    [  5]   8.00-9.00   sec  11.0 MBytes  92.3 Mbits/sec    0    923 KBytes       
    [  5]   9.00-10.00  sec  11.2 MBytes  94.3 Mbits/sec    0    923 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   108 MBytes  90.8 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   106 MBytes  88.2 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 2462.0
    RX: 205794 bytes (517 packets)
    TX: 105235 bytes (524 packets)
    signal: -32 dBm
    rx bitrate: 130.0 MBit/s MCS 15
    tx bitrate: 144.4 MBit/s MCS 15 short GI
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