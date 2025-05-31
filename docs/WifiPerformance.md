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
**Test Date:** [2025-05-31 16:46 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15365208918)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">51.2</span> Mbits/sec | <span style="font-size: 1.5rem;">55.0</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 52107 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.99 MBytes  50.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.55 MBytes  46.6 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.64 MBytes  47.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.85 MBytes  49.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.84 MBytes  49.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.78 MBytes  48.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.75 MBytes  48.3 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.95 MBytes  49.9 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.85 MBytes  49.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.82 MBytes  48.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  61.1 MBytes  51.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  58.0 MBytes  48.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 36587 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  7.62 MBytes  63.9 Mbits/sec    0    337 KBytes       
    [  5]   1.00-2.00   sec  7.52 MBytes  63.1 Mbits/sec    0    559 KBytes       
    [  5]   2.00-3.00   sec  6.96 MBytes  58.4 Mbits/sec    0    594 KBytes       
    [  5]   3.00-4.00   sec  6.02 MBytes  50.5 Mbits/sec    0    677 KBytes       
    [  5]   4.00-5.00   sec  6.25 MBytes  52.4 Mbits/sec    0    725 KBytes       
    [  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0    772 KBytes       
    [  5]   6.00-7.00   sec  6.25 MBytes  52.4 Mbits/sec    0    822 KBytes       
    [  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0    913 KBytes       
    [  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0    913 KBytes       
    [  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0    913 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  65.6 MBytes  55.0 Mbits/sec    0             sender
    [  5]   0.00-10.04  sec  63.0 MBytes  52.6 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 36895 bytes (141 packets)
    TX: 51194 bytes (193 packets)
    signal: -28 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">146</span> Mbits/sec | <span style="font-size: 1.5rem;">180</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 36593 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  22.6 MBytes   190 Mbits/sec                  
    [  5]   1.00-2.00   sec  22.1 MBytes   185 Mbits/sec                  
    [  5]   2.00-3.00   sec  22.5 MBytes   189 Mbits/sec                  
    [  5]   3.00-4.00   sec  15.2 MBytes   127 Mbits/sec                  
    [  5]   4.00-5.00   sec  14.7 MBytes   123 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.8 MBytes   124 Mbits/sec                  
    [  5]   6.00-7.00   sec  15.1 MBytes   126 Mbits/sec                  
    [  5]   7.00-8.00   sec  15.1 MBytes   126 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   9.00-10.00  sec  15.0 MBytes   126 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   174 MBytes   146 Mbits/sec   68             sender
    [  5]   0.00-10.00  sec   171 MBytes   143 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 57531 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  21.2 MBytes   177 Mbits/sec    0    634 KBytes       
    [  5]   1.00-2.00   sec  21.7 MBytes   182 Mbits/sec    0    693 KBytes       
    [  5]   2.00-3.00   sec  21.5 MBytes   180 Mbits/sec    0    813 KBytes       
    [  5]   3.00-4.00   sec  20.4 MBytes   171 Mbits/sec    0    813 KBytes       
    [  5]   4.00-5.00   sec  21.3 MBytes   178 Mbits/sec    0    858 KBytes       
    [  5]   5.00-6.00   sec  22.2 MBytes   187 Mbits/sec    0    858 KBytes       
    [  5]   6.00-7.00   sec  21.0 MBytes   176 Mbits/sec    0    954 KBytes       
    [  5]   7.00-8.00   sec  21.8 MBytes   183 Mbits/sec    0   1003 KBytes       
    [  5]   8.00-9.00   sec  20.4 MBytes   172 Mbits/sec    0   1003 KBytes       
    [  5]   9.00-10.00  sec  22.6 MBytes   189 Mbits/sec    0   1003 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   214 MBytes   180 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   212 MBytes   178 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 129214 bytes (539 packets)
    TX: 58051 bytes (249 packets)
    signal: -44 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">233</span> Mbits/sec | <span style="font-size: 1.5rem;">238</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.163 port 46535 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  22.2 MBytes   186 Mbits/sec                  
    [  5]   1.00-2.00   sec  26.2 MBytes   220 Mbits/sec                  
    [  5]   2.00-3.00   sec  28.4 MBytes   238 Mbits/sec                  
    [  5]   3.00-4.00   sec  28.8 MBytes   241 Mbits/sec                  
    [  5]   4.00-5.00   sec  30.1 MBytes   253 Mbits/sec                  
    [  5]   5.00-6.00   sec  28.1 MBytes   236 Mbits/sec                  
    [  5]   6.00-7.00   sec  28.8 MBytes   241 Mbits/sec                  
    [  5]   7.00-8.00   sec  27.9 MBytes   234 Mbits/sec                  
    [  5]   8.00-9.00   sec  25.6 MBytes   215 Mbits/sec                  
    [  5]   9.00-10.00  sec  28.9 MBytes   242 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   278 MBytes   233 Mbits/sec  682             sender
    [  5]   0.00-10.00  sec   275 MBytes   231 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.163 port 38859 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  32.6 MBytes   273 Mbits/sec   10   1.12 MBytes       
    [  5]   1.00-2.00   sec  31.2 MBytes   262 Mbits/sec    1    576 KBytes       
    [  5]   2.00-3.00   sec  29.5 MBytes   247 Mbits/sec    0    601 KBytes       
    [  5]   3.00-4.00   sec  28.2 MBytes   237 Mbits/sec    2    195 KBytes       
    [  5]   4.00-5.00   sec  22.6 MBytes   190 Mbits/sec    1    272 KBytes       
    [  5]   5.00-6.00   sec  29.4 MBytes   246 Mbits/sec    0    395 KBytes       
    [  5]   6.00-7.00   sec  26.1 MBytes   219 Mbits/sec   11    197 KBytes       
    [  5]   7.00-8.00   sec  26.0 MBytes   218 Mbits/sec    0    341 KBytes       
    [  5]   8.00-9.00   sec  28.8 MBytes   241 Mbits/sec    0    441 KBytes       
    [  5]   9.00-10.00  sec  29.6 MBytes   248 Mbits/sec    0    518 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   284 MBytes   238 Mbits/sec   25             sender
    [  5]   0.00-10.01  sec   281 MBytes   236 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">579</span> Mbits/sec | <span style="font-size: 1.5rem;">460</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 51413 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  75.4 MBytes   633 Mbits/sec                  
    [  5]   1.00-2.00   sec  76.9 MBytes   645 Mbits/sec                  
    [  5]   2.00-3.00   sec  78.4 MBytes   658 Mbits/sec                  
    [  5]   3.00-4.00   sec  71.8 MBytes   602 Mbits/sec                  
    [  5]   4.00-5.00   sec  67.7 MBytes   568 Mbits/sec                  
    [  5]   5.00-6.00   sec  66.4 MBytes   557 Mbits/sec                  
    [  5]   6.00-7.00   sec  59.4 MBytes   498 Mbits/sec                  
    [  5]   7.00-8.00   sec  60.5 MBytes   508 Mbits/sec                  
    [  5]   8.00-9.00   sec  63.5 MBytes   532 Mbits/sec                  
    [  5]   9.00-10.00  sec  66.9 MBytes   562 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   691 MBytes   579 Mbits/sec  439             sender
    [  5]   0.00-10.00  sec   687 MBytes   576 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 45931 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  66.2 MBytes   556 Mbits/sec  199   3.21 MBytes       
    [  5]   1.00-2.00   sec  63.8 MBytes   535 Mbits/sec  168   1.61 MBytes       
    [  5]   2.00-3.00   sec  62.5 MBytes   524 Mbits/sec  325    858 KBytes       
    [  5]   3.00-4.00   sec  60.0 MBytes   503 Mbits/sec  225    477 KBytes       
    [  5]   4.00-5.00   sec  52.5 MBytes   440 Mbits/sec    0    617 KBytes       
    [  5]   5.00-6.00   sec  47.5 MBytes   398 Mbits/sec   50    469 KBytes       
    [  5]   6.00-7.00   sec  46.2 MBytes   389 Mbits/sec   59    410 KBytes       
    [  5]   7.00-8.00   sec  45.0 MBytes   377 Mbits/sec   41    376 KBytes       
    [  5]   8.00-9.00   sec  51.2 MBytes   430 Mbits/sec    0    539 KBytes       
    [  5]   9.00-10.00  sec  53.8 MBytes   451 Mbits/sec  142    409 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   549 MBytes   460 Mbits/sec  1209             sender
    [  5]   0.00-10.00  sec   546 MBytes   458 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 139094 bytes (492 packets)
    TX: 60335 bytes (217 packets)
    signal: -33 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    
    ```
### AX

#### Intel AX200

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/AX200.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-rockchip64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">388</span> Mbits/sec | <span style="font-size: 1.5rem;">187</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 52293 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  24.2 MBytes   203 Mbits/sec                  
    [  5]   1.00-2.00   sec  26.0 MBytes   218 Mbits/sec                  
    [  5]   2.00-3.00   sec  29.6 MBytes   248 Mbits/sec                  
    [  5]   3.00-4.00   sec  61.4 MBytes   515 Mbits/sec                  
    [  5]   4.00-5.00   sec  65.1 MBytes   546 Mbits/sec                  
    [  5]   5.00-6.00   sec  55.4 MBytes   464 Mbits/sec                  
    [  5]   6.00-7.00   sec  63.5 MBytes   533 Mbits/sec                  
    [  5]   7.00-8.00   sec  56.2 MBytes   472 Mbits/sec                  
    [  5]   8.00-9.00   sec  32.6 MBytes   274 Mbits/sec                  
    [  5]   9.00-10.00  sec  45.5 MBytes   382 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   463 MBytes   388 Mbits/sec  751             sender
    [  5]   0.00-10.00  sec   460 MBytes   386 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 47221 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  32.6 MBytes   274 Mbits/sec    0   5.22 MBytes       
    [  5]   1.00-2.00   sec  48.8 MBytes   409 Mbits/sec  123    689 KBytes       
    [  5]   2.00-3.00   sec  29.6 MBytes   249 Mbits/sec    0    744 KBytes       
    [  5]   3.00-4.00   sec  26.2 MBytes   220 Mbits/sec   12    427 KBytes       
    [  5]   4.00-5.00   sec  19.1 MBytes   160 Mbits/sec    1   1.41 KBytes       
    [  5]   5.00-6.00   sec  33.1 MBytes   278 Mbits/sec   23    300 KBytes       
    [  5]   6.00-7.00   sec  11.6 MBytes  97.5 Mbits/sec    1   1.41 KBytes       
    [  5]   7.00-8.00   sec  11.9 MBytes  99.6 Mbits/sec    0    389 KBytes       
    [  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    1    389 KBytes       
    [  5]   9.00-10.00  sec  10.0 MBytes  83.8 Mbits/sec    0    421 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   223 MBytes   187 Mbits/sec  161             sender
    [  5]   0.00-10.04  sec   220 MBytes   184 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 72378 bytes (258 packets)
    TX: 89895 bytes (349 packets)
    signal: -35 dBm
    rx bitrate: 1441.3 MBit/s 160MHz HE-MCS 7 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">48.1</span> Mbits/sec | <span style="font-size: 1.5rem;">38.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.164 port 53511 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.28 MBytes  44.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.29 MBytes  44.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.39 MBytes  45.2 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.32 MBytes  44.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.42 MBytes  45.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.65 MBytes  47.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.43 MBytes  45.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.46 MBytes  45.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.49 MBytes  46.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.55 MBytes  46.6 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  57.4 MBytes  48.1 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  54.3 MBytes  45.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.164 port 48619 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.20 MBytes  43.6 Mbits/sec    0    219 KBytes       
    [  5]   1.00-2.00   sec  4.23 MBytes  35.4 Mbits/sec    0    219 KBytes       
    [  5]   2.00-3.00   sec  4.23 MBytes  35.4 Mbits/sec    0    232 KBytes       
    [  5]   3.00-4.00   sec  4.78 MBytes  40.1 Mbits/sec    0    232 KBytes       
    [  5]   4.00-5.00   sec  4.35 MBytes  36.5 Mbits/sec    0    232 KBytes       
    [  5]   5.00-6.00   sec  4.60 MBytes  38.6 Mbits/sec    0    232 KBytes       
    [  5]   6.00-7.00   sec  4.47 MBytes  37.5 Mbits/sec    0    266 KBytes       
    [  5]   7.00-8.00   sec  4.66 MBytes  39.1 Mbits/sec    0    266 KBytes       
    [  5]   8.00-9.00   sec  4.66 MBytes  39.1 Mbits/sec    0    266 KBytes       
    [  5]   9.00-10.00  sec  4.66 MBytes  39.1 Mbits/sec    0    266 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  45.8 MBytes  38.4 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  45.1 MBytes  37.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 68540 bytes (217 packets)
    TX: 61267 bytes (264 packets)
    signal: -57 dBm
    rx bitrate: 72.2 MBit/s
    tx bitrate: 72.2 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">52.5</span> Mbits/sec | <span style="font-size: 1.5rem;">55.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 55045 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  7.02 MBytes  58.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  6.20 MBytes  52.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.94 MBytes  49.8 Mbits/sec                  
    [  5]   3.00-4.00   sec  6.64 MBytes  55.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.43 MBytes  45.6 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.95 MBytes  49.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.97 MBytes  50.0 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.64 MBytes  47.3 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.78 MBytes  48.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.92 MBytes  49.7 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.09  sec  63.1 MBytes  52.5 Mbits/sec    4             sender
    [  5]   0.00-10.00  sec  60.5 MBytes  50.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 38347 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.07 MBytes  50.9 Mbits/sec    0    177 KBytes       
    [  5]   1.00-2.00   sec  5.65 MBytes  47.5 Mbits/sec    0    216 KBytes       
    [  5]   2.00-3.00   sec  6.84 MBytes  57.4 Mbits/sec    0    267 KBytes       
    [  5]   3.00-4.00   sec  6.09 MBytes  51.1 Mbits/sec    0    283 KBytes       
    [  5]   4.00-5.00   sec  6.34 MBytes  53.2 Mbits/sec    0    311 KBytes       
    [  5]   5.00-6.00   sec  7.58 MBytes  63.6 Mbits/sec    0    378 KBytes       
    [  5]   6.00-7.00   sec  6.28 MBytes  52.7 Mbits/sec    0    378 KBytes       
    [  5]   7.00-8.00   sec  6.52 MBytes  54.7 Mbits/sec    0    420 KBytes       
    [  5]   8.00-9.00   sec  8.26 MBytes  69.3 Mbits/sec    0    515 KBytes       
    [  5]   9.00-10.00  sec  6.34 MBytes  53.2 Mbits/sec    0    515 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  66.0 MBytes  55.3 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec  63.5 MBytes  53.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 75387 bytes (200 packets)
    TX: 50513 bytes (236 packets)
    signal: -51 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">11.6</span> Mbits/sec | <span style="font-size: 1.5rem;">26.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 55119 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  9.08 MBytes  76.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.48 MBytes  12.4 Mbits/sec                  
    [  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec                  
    [  5]   3.00-4.00   sec  0.00 Bytes  0.00 bits/sec                  
    [  5]   4.00-5.00   sec   276 KBytes  2.26 Mbits/sec                  
    [  5]   5.00-6.00   sec  0.00 Bytes  0.00 bits/sec                  
    [  5]   6.00-7.00   sec  11.3 KBytes  92.7 Kbits/sec                  
    [  5]   7.00-8.00   sec   656 KBytes  5.38 Mbits/sec                  
    [  5]   8.00-9.00   sec   150 KBytes  1.23 Mbits/sec                  
    [  5]   9.00-10.00  sec  9.90 KBytes  81.0 Kbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  13.9 MBytes  11.6 Mbits/sec   91             sender
    [  5]   0.00-10.00  sec  11.6 MBytes  9.76 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 42341 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.71 MBytes  73.1 Mbits/sec    0    431 KBytes       
    [  5]   1.00-2.00   sec  5.72 MBytes  48.0 Mbits/sec    0    680 KBytes       
    [  5]   2.00-3.00   sec  1.80 MBytes  15.1 Mbits/sec    0    775 KBytes       
    [  5]   3.00-4.00   sec  1.74 MBytes  14.6 Mbits/sec    0    872 KBytes       
    [  5]   4.00-5.00   sec  3.17 MBytes  26.6 Mbits/sec    0    935 KBytes       
    [  5]   5.00-6.00   sec  1.18 MBytes  9.90 Mbits/sec    0    966 KBytes       
    [  5]   6.00-7.00   sec  3.43 MBytes  28.8 Mbits/sec    0   1.04 MBytes       
    [  5]   7.00-8.00   sec  2.35 MBytes  19.7 Mbits/sec    0   1.04 MBytes       
    [  5]   8.00-9.00   sec  2.30 MBytes  19.3 Mbits/sec    0   1.04 MBytes       
    [  5]   9.00-10.00  sec  1.18 MBytes  9.90 Mbits/sec    0   1.08 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  31.6 MBytes  26.5 Mbits/sec    0             sender
    [  5]   0.00-10.06  sec  29.9 MBytes  24.9 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">127</span> Mbits/sec | <span style="font-size: 1.5rem;">140</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 42345 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.1 MBytes   126 Mbits/sec                  
    [  5]   1.00-2.00   sec  15.1 MBytes   127 Mbits/sec                  
    [  5]   2.00-3.00   sec  14.3 MBytes   120 Mbits/sec                  
    [  5]   3.00-4.00   sec  15.5 MBytes   130 Mbits/sec                  
    [  5]   4.00-5.00   sec  14.0 MBytes   118 Mbits/sec                  
    [  5]   5.00-6.00   sec  15.4 MBytes   129 Mbits/sec                  
    [  5]   6.00-7.00   sec  15.6 MBytes   130 Mbits/sec                  
    [  5]   7.00-8.00   sec  14.6 MBytes   122 Mbits/sec                  
    [  5]   8.00-9.00   sec  14.5 MBytes   122 Mbits/sec                  
    [  5]   9.00-10.00  sec  14.2 MBytes   119 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   151 MBytes   127 Mbits/sec  266             sender
    [  5]   0.00-10.00  sec   148 MBytes   124 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 41157 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  18.3 MBytes   154 Mbits/sec    0    397 KBytes       
    [  5]   1.00-2.00   sec  16.3 MBytes   137 Mbits/sec    0    419 KBytes       
    [  5]   2.00-3.00   sec  16.8 MBytes   141 Mbits/sec    0    419 KBytes       
    [  5]   3.00-4.00   sec  16.1 MBytes   135 Mbits/sec    0    419 KBytes       
    [  5]   4.00-5.00   sec  16.8 MBytes   141 Mbits/sec    0    419 KBytes       
    [  5]   5.00-6.00   sec  16.7 MBytes   140 Mbits/sec    0    419 KBytes       
    [  5]   6.00-7.00   sec  16.6 MBytes   139 Mbits/sec    0    419 KBytes       
    [  5]   7.00-8.00   sec  15.8 MBytes   132 Mbits/sec    0    419 KBytes       
    [  5]   8.00-9.00   sec  16.7 MBytes   140 Mbits/sec    0    419 KBytes       
    [  5]   9.00-10.00  sec  16.9 MBytes   142 Mbits/sec    0    419 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   167 MBytes   140 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   165 MBytes   138 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 3889849687 bytes (3212088 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">16.8</span> Mbits/sec | <span style="font-size: 1.5rem;">10.5</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.249 port 43589 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.86 MBytes  15.6 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.79 MBytes  15.0 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.82 MBytes  15.3 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.88 MBytes  15.7 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.84 MBytes  15.4 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.59 MBytes  13.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  1.74 MBytes  14.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  1.84 MBytes  15.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  1.81 MBytes  15.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.97 MBytes  16.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.11  sec  20.2 MBytes  16.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  18.1 MBytes  15.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.249 port 37667 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.49 MBytes  12.5 Mbits/sec    0    109 KBytes       
    [  5]   1.00-2.00   sec  1.06 MBytes  8.86 Mbits/sec    2   82.0 KBytes       
    [  5]   2.00-3.00   sec  1.37 MBytes  11.5 Mbits/sec    0   99.0 KBytes       
    [  5]   3.00-4.00   sec  1.24 MBytes  10.4 Mbits/sec    0    106 KBytes       
    [  5]   4.00-5.00   sec  1.24 MBytes  10.4 Mbits/sec    0    109 KBytes       
    [  5]   5.00-6.00   sec  1.24 MBytes  10.4 Mbits/sec    0    109 KBytes       
    [  5]   6.00-7.00   sec  1.24 MBytes  10.4 Mbits/sec    0    109 KBytes       
    [  5]   7.00-8.00   sec  1.12 MBytes  9.38 Mbits/sec    6   77.8 KBytes       
    [  5]   8.00-9.00   sec  1.24 MBytes  10.4 Mbits/sec    0   97.6 KBytes       
    [  5]   9.00-10.00  sec  1.24 MBytes  10.4 Mbits/sec    0    105 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  12.5 MBytes  10.5 Mbits/sec    8             sender
    [  5]   0.00-10.04  sec  12.2 MBytes  10.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 53577 bytes (142 packets)
    TX: 60590 bytes (252 packets)
    signal: -30 dBm
    rx bitrate: 6.0 MBit/s
    tx bitrate: 65.0 MBit/s MCS 7
    
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
