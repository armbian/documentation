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
**Test Date:** [2025-05-25 09:15 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15235904340)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">57.3</span> Mbits/sec | <span style="font-size: 1.5rem;">59.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 33707 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  6.47 MBytes  54.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.54 MBytes  54.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.40 MBytes  53.7 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.48 MBytes  54.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.59 MBytes  55.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.72 MBytes  56.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.53 MBytes  54.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.45 MBytes  54.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.50 MBytes  54.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.48 MBytes  54.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  68.4 MBytes  57.3 Mbits/sec   10             sender
    [  5]   0.00-10.00  sec  65.2 MBytes  54.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 45889 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.47 MBytes  62.7 Mbits/sec    0    335 KBytes       
    [  5]   1.00-2.00   sec  8.14 MBytes  68.3 Mbits/sec    0    535 KBytes       
    [  5]   2.00-3.00   sec  7.26 MBytes  60.9 Mbits/sec    0    716 KBytes       
    [  5]   3.00-4.00   sec  6.25 MBytes  52.4 Mbits/sec    0    820 KBytes       
    [  5]   4.00-5.00   sec  7.50 MBytes  62.9 Mbits/sec    0    915 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.03 MBytes       
    [  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.16 MBytes       
    [  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.16 MBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.16 MBytes       
    [  5]   9.00-10.00  sec  7.50 MBytes  62.9 Mbits/sec    0   1.16 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  70.4 MBytes  59.0 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  66.8 MBytes  55.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 157178 bytes (411 packets)
    TX: 90602 bytes (511 packets)
    signal: -27 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">116</span> Mbits/sec | <span style="font-size: 1.5rem;">108</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 41399 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  13.2 MBytes   111 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.8 MBytes   115 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   3.00-4.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.5 MBytes   113 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  13.3 MBytes   112 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.3 MBytes   112 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.7 MBytes   114 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   138 MBytes   116 Mbits/sec  128             sender
    [  5]   0.00-10.00  sec   135 MBytes   113 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 41243 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  13.3 MBytes   112 Mbits/sec    0    447 KBytes       
    [  5]   1.00-2.00   sec  12.3 MBytes   103 Mbits/sec    0    574 KBytes       
    [  5]   2.00-3.00   sec  12.9 MBytes   108 Mbits/sec    0    714 KBytes       
    [  5]   3.00-4.00   sec  13.5 MBytes   114 Mbits/sec    0    759 KBytes       
    [  5]   4.00-5.00   sec  12.1 MBytes   102 Mbits/sec    0    759 KBytes       
    [  5]   5.00-6.00   sec  12.4 MBytes   104 Mbits/sec    0    759 KBytes       
    [  5]   6.00-7.00   sec  12.7 MBytes   107 Mbits/sec    0    759 KBytes       
    [  5]   7.00-8.00   sec  12.7 MBytes   106 Mbits/sec    0    759 KBytes       
    [  5]   8.00-9.00   sec  13.2 MBytes   111 Mbits/sec    0    798 KBytes       
    [  5]   9.00-10.00  sec  13.3 MBytes   112 Mbits/sec    0    798 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   128 MBytes   108 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   126 MBytes   106 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 118553 bytes (524 packets)
    TX: 60367 bytes (241 packets)
    signal: -35 dBm
    rx bitrate: 144.4 MBit/s MCS 15 short GI
    
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">258</span> Mbits/sec | <span style="font-size: 1.5rem;">239</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.163 port 44693 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  25.5 MBytes   214 Mbits/sec                  
    [  5]   1.00-2.00   sec  28.2 MBytes   237 Mbits/sec                  
    [  5]   2.00-3.00   sec  28.5 MBytes   239 Mbits/sec                  
    [  5]   3.00-4.00   sec  28.1 MBytes   236 Mbits/sec                  
    [  5]   4.00-5.00   sec  30.9 MBytes   259 Mbits/sec                  
    [  5]   5.00-6.00   sec  32.4 MBytes   272 Mbits/sec                  
    [  5]   6.00-7.00   sec  32.6 MBytes   274 Mbits/sec                  
    [  5]   7.00-8.00   sec  32.9 MBytes   276 Mbits/sec                  
    [  5]   8.00-9.00   sec  32.8 MBytes   275 Mbits/sec                  
    [  5]   9.00-10.00  sec  33.2 MBytes   279 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   308 MBytes   258 Mbits/sec  166             sender
    [  5]   0.00-10.00  sec   305 MBytes   256 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.163 port 58619 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  29.2 MBytes   245 Mbits/sec    0   1.28 MBytes       
    [  5]   1.00-2.00   sec  29.6 MBytes   249 Mbits/sec    0   2.14 MBytes       
    [  5]   2.00-3.00   sec  26.9 MBytes   225 Mbits/sec   37    168 KBytes       
    [  5]   3.00-4.00   sec  19.9 MBytes   167 Mbits/sec    0    298 KBytes       
    [  5]   4.00-5.00   sec  29.2 MBytes   245 Mbits/sec    0    411 KBytes       
    [  5]   5.00-6.00   sec  29.2 MBytes   245 Mbits/sec    0    492 KBytes       
    [  5]   6.00-7.00   sec  29.6 MBytes   249 Mbits/sec    0    547 KBytes       
    [  5]   7.00-8.00   sec  30.8 MBytes   258 Mbits/sec    0    584 KBytes       
    [  5]   8.00-9.00   sec  29.8 MBytes   250 Mbits/sec    0    618 KBytes       
    [  5]   9.00-10.00  sec  30.0 MBytes   251 Mbits/sec    0    646 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   285 MBytes   239 Mbits/sec   37             sender
    [  5]   0.00-10.01  sec   282 MBytes   236 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">633</span> Mbits/sec | <span style="font-size: 1.5rem;">558</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 53455 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  79.0 MBytes   662 Mbits/sec                  
    [  5]   1.00-2.00   sec  81.3 MBytes   682 Mbits/sec                  
    [  5]   2.00-3.00   sec  83.0 MBytes   696 Mbits/sec                  
    [  5]   3.00-4.00   sec  77.6 MBytes   650 Mbits/sec                  
    [  5]   4.00-5.00   sec  81.5 MBytes   684 Mbits/sec                  
    [  5]   5.00-6.00   sec  76.5 MBytes   642 Mbits/sec                  
    [  5]   6.00-7.00   sec  69.5 MBytes   583 Mbits/sec                  
    [  5]   7.00-8.00   sec  68.0 MBytes   570 Mbits/sec                  
    [  5]   8.00-9.00   sec  69.2 MBytes   581 Mbits/sec                  
    [  5]   9.00-10.00  sec  67.2 MBytes   564 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   755 MBytes   633 Mbits/sec  1238             sender
    [  5]   0.00-10.00  sec   753 MBytes   631 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 34985 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  79.2 MBytes   662 Mbits/sec  115   3.22 MBytes       
    [  5]   1.00-2.00   sec  76.2 MBytes   642 Mbits/sec    0   3.22 MBytes       
    [  5]   2.00-3.01   sec  76.2 MBytes   636 Mbits/sec   90   1.64 MBytes       
    [  5]   3.01-4.00   sec  70.0 MBytes   590 Mbits/sec   41    472 KBytes       
    [  5]   4.00-5.00   sec  55.0 MBytes   461 Mbits/sec    0    619 KBytes       
    [  5]   5.00-6.00   sec  63.8 MBytes   535 Mbits/sec    0    754 KBytes       
    [  5]   6.00-7.00   sec  53.8 MBytes   451 Mbits/sec    6    537 KBytes       
    [  5]   7.00-8.00   sec  58.8 MBytes   493 Mbits/sec    0    679 KBytes       
    [  5]   8.00-9.00   sec  65.0 MBytes   545 Mbits/sec    0    806 KBytes       
    [  5]   9.00-10.00  sec  67.5 MBytes   566 Mbits/sec    0    918 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   666 MBytes   558 Mbits/sec  252             sender
    [  5]   0.00-10.01  sec   663 MBytes   556 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 149706 bytes (542 packets)
    TX: 59074 bytes (215 packets)
    signal: -32 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">191</span> Mbits/sec | <span style="font-size: 1.5rem;">194</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 60801 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  19.9 MBytes   167 Mbits/sec                  
    [  5]   1.00-2.00   sec  23.2 MBytes   195 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.9 MBytes   200 Mbits/sec                  
    [  5]   3.00-4.00   sec  23.0 MBytes   193 Mbits/sec                  
    [  5]   4.00-5.00   sec  23.2 MBytes   195 Mbits/sec                  
    [  5]   5.00-6.00   sec  21.8 MBytes   182 Mbits/sec                  
    [  5]   6.00-7.00   sec  22.1 MBytes   186 Mbits/sec                  
    [  5]   7.00-8.00   sec  22.0 MBytes   185 Mbits/sec                  
    [  5]   8.00-9.00   sec  22.9 MBytes   192 Mbits/sec                  
    [  5]   9.00-10.00  sec  23.0 MBytes   193 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   229 MBytes   191 Mbits/sec  150             sender
    [  5]   0.00-10.00  sec   225 MBytes   189 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 46681 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.6 MBytes   215 Mbits/sec    0   4.55 MBytes       
    [  5]   1.00-2.00   sec  22.8 MBytes   191 Mbits/sec   25   2.27 MBytes       
    [  5]   2.00-3.00   sec  21.9 MBytes   184 Mbits/sec    0   2.28 MBytes       
    [  5]   3.00-4.00   sec  24.8 MBytes   208 Mbits/sec    0   2.28 MBytes       
    [  5]   4.00-5.00   sec  22.6 MBytes   190 Mbits/sec    0   2.28 MBytes       
    [  5]   5.00-6.00   sec  23.4 MBytes   196 Mbits/sec    0   2.28 MBytes       
    [  5]   6.00-7.00   sec  21.5 MBytes   180 Mbits/sec    0   2.28 MBytes       
    [  5]   7.00-8.00   sec  22.9 MBytes   192 Mbits/sec    7   1.14 MBytes       
    [  5]   8.00-9.00   sec  23.2 MBytes   195 Mbits/sec    0   1.15 MBytes       
    [  5]   9.00-10.00  sec  23.2 MBytes   195 Mbits/sec    0   1.17 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   232 MBytes   194 Mbits/sec   32             sender
    [  5]   0.00-10.02  sec   228 MBytes   191 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 36341 bytes (126 packets)
    TX: 48163 bytes (196 packets)
    signal: -23 dBm
    rx bitrate: 154.8 MBit/s HE-MCS 6 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 58.5 MBit/s HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">53.7</span> Mbits/sec | <span style="font-size: 1.5rem;">36.6</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.164 port 52039 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.58 MBytes  46.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.21 MBytes  52.1 Mbits/sec                  
    [  5]   2.00-3.00   sec  6.26 MBytes  52.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.43 MBytes  45.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  6.07 MBytes  50.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.20 MBytes  52.0 Mbits/sec                  
    [  5]   6.00-7.00   sec  6.46 MBytes  54.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.40 MBytes  53.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  6.34 MBytes  53.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  6.46 MBytes  54.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  64.1 MBytes  53.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  61.4 MBytes  51.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.164 port 60903 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  4.77 MBytes  40.0 Mbits/sec    0    175 KBytes       
    [  5]   1.00-2.00   sec  4.16 MBytes  34.9 Mbits/sec    0    201 KBytes       
    [  5]   2.00-3.00   sec  4.41 MBytes  37.0 Mbits/sec    3    153 KBytes       
    [  5]   3.00-4.00   sec  3.98 MBytes  33.4 Mbits/sec    0    175 KBytes       
    [  5]   4.00-5.00   sec  3.98 MBytes  33.4 Mbits/sec    0    185 KBytes       
    [  5]   5.00-6.00   sec  4.23 MBytes  35.4 Mbits/sec    0    194 KBytes       
    [  5]   6.00-7.00   sec  4.72 MBytes  39.6 Mbits/sec    0    199 KBytes       
    [  5]   7.00-8.00   sec  4.72 MBytes  39.6 Mbits/sec    0    201 KBytes       
    [  5]   8.00-9.00   sec  4.23 MBytes  35.4 Mbits/sec    0    201 KBytes       
    [  5]   9.00-10.00  sec  4.47 MBytes  37.5 Mbits/sec    0    202 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  43.7 MBytes  36.6 Mbits/sec    3             sender
    [  5]   0.00-10.02  sec  43.2 MBytes  36.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 61708 bytes (176 packets)
    TX: 57521 bytes (276 packets)
    signal: -57 dBm
    rx bitrate: 65.0 MBit/s
    tx bitrate: 65.0 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">53.8</span> Mbits/sec | <span style="font-size: 1.5rem;">56.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 44551 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.99 MBytes  83.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.81 MBytes  48.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.84 MBytes  49.0 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.15 MBytes  51.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.51 MBytes  46.2 Mbits/sec                  
    [  5]   5.00-6.00   sec  6.19 MBytes  51.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.11 MBytes  42.9 Mbits/sec                  
    [  5]   7.00-8.00   sec  6.15 MBytes  51.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.51 MBytes  46.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.80 MBytes  40.3 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.11  sec  64.9 MBytes  53.8 Mbits/sec  355             sender
    [  5]   0.00-10.00  sec  61.1 MBytes  51.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 34743 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.08 MBytes  51.0 Mbits/sec    0    181 KBytes       
    [  5]   1.00-2.00   sec  5.97 MBytes  50.0 Mbits/sec    0    204 KBytes       
    [  5]   2.00-3.00   sec  5.59 MBytes  46.9 Mbits/sec    0    219 KBytes       
    [  5]   3.00-4.00   sec  6.65 MBytes  55.7 Mbits/sec    0    267 KBytes       
    [  5]   4.00-5.00   sec  6.21 MBytes  52.2 Mbits/sec    0    297 KBytes       
    [  5]   5.00-6.00   sec  6.90 MBytes  57.9 Mbits/sec    0    314 KBytes       
    [  5]   6.00-7.00   sec  11.8 MBytes  99.0 Mbits/sec    0    574 KBytes       
    [  5]   7.00-8.00   sec  5.67 MBytes  47.6 Mbits/sec    0    574 KBytes       
    [  5]   8.00-9.00   sec  7.00 MBytes  58.7 Mbits/sec    0    604 KBytes       
    [  5]   9.00-10.00  sec  5.97 MBytes  50.1 Mbits/sec    0    604 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  67.8 MBytes  56.9 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  65.1 MBytes  54.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 49933 bytes (136 packets)
    TX: 50705 bytes (240 packets)
    signal: -49 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">34.9</span> Mbits/sec | <span style="font-size: 1.5rem;">46.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 49829 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.61 MBytes  47.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  3.46 MBytes  29.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.35 MBytes  36.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.97 MBytes  16.5 Mbits/sec                  
    [  5]   4.00-5.00   sec  3.04 MBytes  25.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  3.89 MBytes  32.6 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.49 MBytes  37.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.97 MBytes  41.7 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.06 MBytes  34.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.27 MBytes  19.1 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  41.6 MBytes  34.9 Mbits/sec   19             sender
    [  5]   0.00-10.00  sec  38.1 MBytes  32.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 34841 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.17 MBytes  51.8 Mbits/sec    0    301 KBytes       
    [  5]   1.00-2.00   sec  4.66 MBytes  39.1 Mbits/sec    0    516 KBytes       
    [  5]   2.00-3.00   sec  4.91 MBytes  41.2 Mbits/sec    0    563 KBytes       
    [  5]   3.00-4.00   sec  5.59 MBytes  46.9 Mbits/sec    0    563 KBytes       
    [  5]   4.00-5.00   sec  5.59 MBytes  46.9 Mbits/sec    0    563 KBytes       
    [  5]   5.00-6.00   sec  5.59 MBytes  46.9 Mbits/sec    0    563 KBytes       
    [  5]   6.00-7.00   sec  5.59 MBytes  46.9 Mbits/sec    0    563 KBytes       
    [  5]   7.00-8.00   sec  5.59 MBytes  46.9 Mbits/sec    0    563 KBytes       
    [  5]   8.00-9.00   sec  5.59 MBytes  46.9 Mbits/sec    0    563 KBytes       
    [  5]   9.00-10.00  sec  5.59 MBytes  46.9 Mbits/sec    0    563 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  54.9 MBytes  46.0 Mbits/sec    0             sender
    [  5]   0.00-10.05  sec  53.8 MBytes  44.9 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">143</span> Mbits/sec | <span style="font-size: 1.5rem;">139</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 52415 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   1.00-2.00   sec  16.9 MBytes   142 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   3.00-4.00   sec  17.1 MBytes   143 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   8.00-9.00   sec  17.1 MBytes   144 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.2 MBytes   144 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   171 MBytes   143 Mbits/sec  214             sender
    [  5]   0.00-10.00  sec   168 MBytes   141 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 37689 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  17.0 MBytes   143 Mbits/sec    0    308 KBytes       
    [  5]   1.00-2.00   sec  17.0 MBytes   142 Mbits/sec    0    327 KBytes       
    [  5]   2.00-3.00   sec  16.5 MBytes   139 Mbits/sec    0    327 KBytes       
    [  5]   3.00-4.00   sec  16.7 MBytes   140 Mbits/sec    0    346 KBytes       
    [  5]   4.00-5.00   sec  16.1 MBytes   135 Mbits/sec    0    346 KBytes       
    [  5]   5.00-6.00   sec  16.7 MBytes   140 Mbits/sec    0    346 KBytes       
    [  5]   6.00-7.00   sec  16.7 MBytes   140 Mbits/sec    0    346 KBytes       
    [  5]   7.00-8.00   sec  15.9 MBytes   133 Mbits/sec    0    346 KBytes       
    [  5]   8.00-9.00   sec  16.7 MBytes   140 Mbits/sec    0    346 KBytes       
    [  5]   9.00-10.00  sec  17.0 MBytes   142 Mbits/sec    0    346 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   166 MBytes   139 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   164 MBytes   138 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 2019625477 bytes (1680907 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">19.2</span> Mbits/sec | <span style="font-size: 1.5rem;">12.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.165 port 51867 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.92 MBytes  16.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.87 MBytes  15.7 Mbits/sec                  
    [  5]   2.00-3.00   sec  2.02 MBytes  16.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.99 MBytes  16.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  2.09 MBytes  17.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  2.14 MBytes  17.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  2.16 MBytes  18.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.10 MBytes  17.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.16 MBytes  18.1 Mbits/sec                  
    [  5]   9.00-10.00  sec  2.23 MBytes  18.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.14  sec  23.2 MBytes  19.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  20.7 MBytes  17.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.165 port 39931 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.75 MBytes  14.7 Mbits/sec    0    117 KBytes       
    [  5]   1.00-2.00   sec  1.62 MBytes  13.6 Mbits/sec    0    137 KBytes       
    [  5]   2.00-3.00   sec  1.49 MBytes  12.5 Mbits/sec    0    137 KBytes       
    [  5]   3.00-4.00   sec  1.30 MBytes  10.9 Mbits/sec    0    137 KBytes       
    [  5]   4.00-5.00   sec  1.49 MBytes  12.5 Mbits/sec    0    137 KBytes       
    [  5]   5.00-6.00   sec  1.49 MBytes  12.5 Mbits/sec    0    137 KBytes       
    [  5]   6.00-7.00   sec  1.49 MBytes  12.5 Mbits/sec    0    137 KBytes       
    [  5]   7.00-8.00   sec  1.49 MBytes  12.5 Mbits/sec    0    137 KBytes       
    [  5]   8.00-9.00   sec  1.49 MBytes  12.5 Mbits/sec    0    137 KBytes       
    [  5]   9.00-10.00  sec  1.18 MBytes  9.90 Mbits/sec    3    105 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  14.8 MBytes  12.4 Mbits/sec    3             sender
    [  5]   0.00-10.05  sec  14.4 MBytes  12.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462
    RX: 56830 bytes (131 packets)
    TX: 59844 bytes (278 packets)
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
