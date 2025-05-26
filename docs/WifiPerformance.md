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
**Test Date:** [2025-05-26 09:33 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15249700364)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">226</span> Mbits/sec | <span style="font-size: 1.5rem;">262</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 49963 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  27.4 MBytes   230 Mbits/sec                  
    [  5]   1.00-2.00   sec  27.7 MBytes   232 Mbits/sec                  
    [  5]   2.00-3.00   sec  26.6 MBytes   224 Mbits/sec                  
    [  5]   3.00-4.00   sec  27.2 MBytes   228 Mbits/sec                  
    [  5]   4.00-5.00   sec  27.1 MBytes   227 Mbits/sec                  
    [  5]   5.00-6.00   sec  26.7 MBytes   224 Mbits/sec                  
    [  5]   6.00-7.00   sec  26.3 MBytes   220 Mbits/sec                  
    [  5]   7.00-8.00   sec  26.0 MBytes   218 Mbits/sec                  
    [  5]   8.00-9.00   sec  26.0 MBytes   218 Mbits/sec                  
    [  5]   9.00-10.00  sec  26.7 MBytes   224 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.08  sec   271 MBytes   226 Mbits/sec   60             sender
    [  5]   0.00-10.00  sec   268 MBytes   225 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 45251 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  34.0 MBytes   285 Mbits/sec    0    880 KBytes       
    [  5]   1.00-2.00   sec  31.2 MBytes   262 Mbits/sec    0   1.01 MBytes       
    [  5]   2.00-3.00   sec  28.8 MBytes   241 Mbits/sec    0   1.18 MBytes       
    [  5]   3.00-4.00   sec  31.2 MBytes   262 Mbits/sec    0   1.37 MBytes       
    [  5]   4.00-5.00   sec  31.2 MBytes   262 Mbits/sec    0   1.45 MBytes       
    [  5]   5.00-6.00   sec  31.2 MBytes   262 Mbits/sec    0   1.45 MBytes       
    [  5]   6.00-7.00   sec  31.2 MBytes   262 Mbits/sec    0   1.45 MBytes       
    [  5]   7.00-8.00   sec  31.2 MBytes   262 Mbits/sec    0   1.61 MBytes       
    [  5]   8.00-9.00   sec  31.2 MBytes   262 Mbits/sec    0   1.69 MBytes       
    [  5]   9.00-10.00  sec  31.2 MBytes   262 Mbits/sec    0   1.69 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   313 MBytes   262 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   310 MBytes   260 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 155059 bytes (400 packets)
    TX: 92534 bytes (529 packets)
    signal: -37 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 390.0 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">117</span> Mbits/sec | <span style="font-size: 1.5rem;">106</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 45175 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.9 MBytes   116 Mbits/sec                  
    [  5]   2.00-3.00   sec  12.2 MBytes   102 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.2 MBytes   110 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.7 MBytes   115 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.9 MBytes   116 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.8 MBytes   116 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.8 MBytes   116 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.04  sec   140 MBytes   117 Mbits/sec   14             sender
    [  5]   0.00-10.00  sec   136 MBytes   114 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 50879 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  12.8 MBytes   107 Mbits/sec    0    356 KBytes       
    [  5]   1.00-2.00   sec  12.2 MBytes   103 Mbits/sec    0    510 KBytes       
    [  5]   2.00-3.00   sec  12.4 MBytes   104 Mbits/sec    0    595 KBytes       
    [  5]   3.00-4.00   sec  13.2 MBytes   111 Mbits/sec    0    625 KBytes       
    [  5]   4.00-5.00   sec  12.6 MBytes   106 Mbits/sec    0    625 KBytes       
    [  5]   5.00-6.00   sec  12.9 MBytes   108 Mbits/sec    0    625 KBytes       
    [  5]   6.00-7.00   sec  12.4 MBytes   104 Mbits/sec    0    666 KBytes       
    [  5]   7.00-8.00   sec  12.3 MBytes   103 Mbits/sec    0    666 KBytes       
    [  5]   8.00-9.00   sec  12.9 MBytes   108 Mbits/sec    0    666 KBytes       
    [  5]   9.00-10.00  sec  12.7 MBytes   106 Mbits/sec    0    666 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   126 MBytes   106 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   125 MBytes   105 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 135259 bytes (564 packets)
    TX: 56389 bytes (239 packets)
    signal: -35 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```
### N

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">56.3</span> Mbits/sec | <span style="font-size: 1.5rem;">44.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.164 port 41195 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.21 MBytes  52.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.34 MBytes  53.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.57 MBytes  55.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.42 MBytes  53.9 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.52 MBytes  54.7 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.52 MBytes  54.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.56 MBytes  55.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.41 MBytes  53.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.57 MBytes  55.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.58 MBytes  55.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  67.2 MBytes  56.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  64.7 MBytes  54.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.164 port 45493 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.77 MBytes  48.4 Mbits/sec    0    206 KBytes       
    [  5]   1.00-2.00   sec  5.03 MBytes  42.2 Mbits/sec    0    238 KBytes       
    [  5]   2.00-3.00   sec  5.34 MBytes  44.8 Mbits/sec    0    238 KBytes       
    [  5]   3.00-4.00   sec  5.22 MBytes  43.8 Mbits/sec    0    238 KBytes       
    [  5]   4.00-5.00   sec  5.22 MBytes  43.8 Mbits/sec    0    238 KBytes       
    [  5]   5.00-6.00   sec  5.47 MBytes  45.9 Mbits/sec    0    260 KBytes       
    [  5]   6.00-7.00   sec  5.28 MBytes  44.3 Mbits/sec    0    272 KBytes       
    [  5]   7.00-8.00   sec  5.34 MBytes  44.8 Mbits/sec    0    276 KBytes       
    [  5]   8.00-9.00   sec  5.22 MBytes  43.8 Mbits/sec    0    324 KBytes       
    [  5]   9.00-10.00  sec  5.22 MBytes  43.8 Mbits/sec    0    324 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  53.1 MBytes  44.6 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  52.4 MBytes  43.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 88351 bytes (278 packets)
    TX: 69197 bytes (314 packets)
    signal: -50 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### UWE 5622

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/UWE5622.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.0-trunk.538, 6.12.23-current-sunxi64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">144</span> Mbits/sec | <span style="font-size: 1.5rem;">138</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 55879 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  16.0 MBytes   135 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   2.00-3.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   3.00-4.00   sec  17.1 MBytes   143 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.1 MBytes   143 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.9 MBytes   141 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.8 MBytes   141 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   172 MBytes   144 Mbits/sec  183             sender
    [  5]   0.00-10.00  sec   169 MBytes   141 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 52747 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  16.8 MBytes   141 Mbits/sec    0    276 KBytes       
    [  5]   1.00-2.00   sec  16.8 MBytes   141 Mbits/sec    0    290 KBytes       
    [  5]   2.00-3.00   sec  16.3 MBytes   137 Mbits/sec    0    315 KBytes       
    [  5]   3.00-4.00   sec  16.8 MBytes   141 Mbits/sec    0    335 KBytes       
    [  5]   4.00-5.00   sec  16.4 MBytes   138 Mbits/sec    0    354 KBytes       
    [  5]   5.00-6.00   sec  15.8 MBytes   133 Mbits/sec    0    354 KBytes       
    [  5]   6.00-7.00   sec  16.7 MBytes   140 Mbits/sec    0    372 KBytes       
    [  5]   7.00-8.00   sec  16.5 MBytes   139 Mbits/sec    0    372 KBytes       
    [  5]   8.00-9.00   sec  16.4 MBytes   138 Mbits/sec    0    372 KBytes       
    [  5]   9.00-10.00  sec  16.2 MBytes   136 Mbits/sec    0    372 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   165 MBytes   138 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   164 MBytes   137 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 2207302055 bytes (1833922 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">17.8</span> Mbits/sec | <span style="font-size: 1.5rem;">10.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.170 port 49123 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.58 MBytes  13.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.85 MBytes  15.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.57 MBytes  13.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.71 MBytes  14.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.95 MBytes  16.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.98 MBytes  16.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.00 MBytes  16.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.39 MBytes  20.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.14 MBytes  17.9 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.81 MBytes  15.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.13  sec  21.5 MBytes  17.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  19.0 MBytes  15.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.170 port 60339 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.26 MBytes  10.6 Mbits/sec    2   33.9 KBytes       
    [  5]   1.00-2.00   sec  1.19 MBytes  10.0 Mbits/sec    1   45.2 KBytes       
    [  5]   2.00-3.00   sec  1.45 MBytes  12.2 Mbits/sec    0   65.0 KBytes       
    [  5]   3.00-4.00   sec  1.37 MBytes  11.5 Mbits/sec    0   77.8 KBytes       
    [  5]   4.00-5.00   sec  1018 KBytes  8.34 Mbits/sec    1   21.2 KBytes       
    [  5]   5.00-6.00   sec  1018 KBytes  8.34 Mbits/sec    5   28.3 KBytes       
    [  5]   6.00-7.00   sec  1.24 MBytes  10.4 Mbits/sec    2   36.8 KBytes       
    [  5]   7.00-8.00   sec  1.37 MBytes  11.5 Mbits/sec    1   32.5 KBytes       
    [  5]   8.00-9.00   sec  1018 KBytes  8.34 Mbits/sec    8   29.7 KBytes       
    [  5]   9.00-10.00  sec  1.37 MBytes  11.5 Mbits/sec    1   41.0 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  12.2 MBytes  10.3 Mbits/sec   21             sender
    [  5]   0.00-10.00  sec  12.0 MBytes  10.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 52298 bytes (166 packets)
    TX: 62711 bytes (257 packets)
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
