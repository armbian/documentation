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
**Test Date:** [2025-06-01 10:44 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15372871986)
### AC

#### Broadcom 4345

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM4345.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.2, 6.12.15-current-bcm2711</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM4345</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">225</span> Mbits/sec | <span style="font-size: 1.5rem;">259</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.131 port 37199 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  25.6 MBytes   215 Mbits/sec                  
    [  5]   1.00-2.00   sec  26.7 MBytes   224 Mbits/sec                  
    [  5]   2.00-3.00   sec  26.6 MBytes   223 Mbits/sec                  
    [  5]   3.00-4.00   sec  26.7 MBytes   224 Mbits/sec                  
    [  5]   4.00-5.00   sec  26.3 MBytes   220 Mbits/sec                  
    [  5]   5.00-6.00   sec  26.4 MBytes   222 Mbits/sec                  
    [  5]   6.00-7.00   sec  26.9 MBytes   226 Mbits/sec                  
    [  5]   7.00-8.00   sec  27.0 MBytes   226 Mbits/sec                  
    [  5]   8.00-9.00   sec  26.6 MBytes   224 Mbits/sec                  
    [  5]   9.00-10.00  sec  26.9 MBytes   226 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.03  sec   268 MBytes   225 Mbits/sec  479             sender
    [  5]   0.00-10.00  sec   266 MBytes   223 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.131 port 58809 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  32.9 MBytes   276 Mbits/sec    0    987 KBytes       
    [  5]   1.00-2.00   sec  27.5 MBytes   231 Mbits/sec    0   1.42 MBytes       
    [  5]   2.00-3.00   sec  31.2 MBytes   262 Mbits/sec    0   1.85 MBytes       
    [  5]   3.00-4.00   sec  31.2 MBytes   262 Mbits/sec    0   2.06 MBytes       
    [  5]   4.00-5.00   sec  31.2 MBytes   262 Mbits/sec    0   2.17 MBytes       
    [  5]   5.00-6.00   sec  31.2 MBytes   262 Mbits/sec    0   2.28 MBytes       
    [  5]   6.00-7.00   sec  31.2 MBytes   262 Mbits/sec    0   2.40 MBytes       
    [  5]   7.00-8.00   sec  30.0 MBytes   252 Mbits/sec    0   2.52 MBytes       
    [  5]   8.00-9.00   sec  31.2 MBytes   262 Mbits/sec    0   2.52 MBytes       
    [  5]   9.00-10.00  sec  31.2 MBytes   262 Mbits/sec    0   2.52 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   309 MBytes   259 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   306 MBytes   257 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 38679 bytes (147 packets)
    TX: 49295 bytes (191 packets)
    signal: -40 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Compex WLE900VX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/QCA9880.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.08.0-trunk, 6.12.28-edge-mvebu</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">QCA9880</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">148</span> Mbits/sec | <span style="font-size: 1.5rem;">179</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.126 port 48631 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  23.7 MBytes   198 Mbits/sec                  
    [  5]   1.00-2.00   sec  24.1 MBytes   202 Mbits/sec                  
    [  5]   2.00-3.00   sec  23.2 MBytes   195 Mbits/sec                  
    [  5]   3.00-4.00   sec  14.7 MBytes   124 Mbits/sec                  
    [  5]   4.00-5.00   sec  15.2 MBytes   127 Mbits/sec                  
    [  5]   5.00-6.00   sec  14.4 MBytes   121 Mbits/sec                  
    [  5]   6.00-7.00   sec  14.7 MBytes   123 Mbits/sec                  
    [  5]   7.00-8.00   sec  14.6 MBytes   123 Mbits/sec                  
    [  5]   8.00-9.00   sec  14.2 MBytes   119 Mbits/sec                  
    [  5]   9.00-10.00  sec  15.0 MBytes   126 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   176 MBytes   148 Mbits/sec  237             sender
    [  5]   0.00-10.00  sec   174 MBytes   146 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.126 port 33057 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  21.2 MBytes   178 Mbits/sec  114    420 KBytes       
    [  5]   1.00-2.00   sec  21.3 MBytes   179 Mbits/sec    0    484 KBytes       
    [  5]   2.00-3.00   sec  21.1 MBytes   177 Mbits/sec    0    533 KBytes       
    [  5]   3.00-4.00   sec  20.4 MBytes   171 Mbits/sec    0    566 KBytes       
    [  5]   4.00-5.00   sec  21.9 MBytes   184 Mbits/sec    0    584 KBytes       
    [  5]   5.00-6.00   sec  22.7 MBytes   190 Mbits/sec    0    594 KBytes       
    [  5]   6.00-7.00   sec  21.1 MBytes   177 Mbits/sec    0    597 KBytes       
    [  5]   7.00-8.00   sec  21.1 MBytes   177 Mbits/sec    0    597 KBytes       
    [  5]   8.00-9.00   sec  21.5 MBytes   180 Mbits/sec    0    597 KBytes       
    [  5]   9.00-10.00  sec  21.4 MBytes   179 Mbits/sec    0    602 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   214 MBytes   179 Mbits/sec  114             sender
    [  5]   0.00-10.01  sec   212 MBytes   178 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 130292 bytes (538 packets)
    TX: 56227 bytes (231 packets)
    signal: -45 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    
    ```

#### Realtek 8821CU #2

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.28-current-meson64</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">269</span> Mbits/sec | <span style="font-size: 1.5rem;">256</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.163 port 54585 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  23.5 MBytes   197 Mbits/sec                  
    [  5]   1.00-2.00   sec  32.0 MBytes   268 Mbits/sec                  
    [  5]   2.00-3.00   sec  33.1 MBytes   278 Mbits/sec                  
    [  5]   3.00-4.00   sec  33.1 MBytes   278 Mbits/sec                  
    [  5]   4.00-5.00   sec  32.8 MBytes   275 Mbits/sec                  
    [  5]   5.00-6.00   sec  33.0 MBytes   277 Mbits/sec                  
    [  5]   6.00-7.00   sec  32.8 MBytes   275 Mbits/sec                  
    [  5]   7.00-8.00   sec  32.6 MBytes   274 Mbits/sec                  
    [  5]   8.00-9.00   sec  32.1 MBytes   269 Mbits/sec                  
    [  5]   9.00-10.00  sec  32.5 MBytes   273 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   321 MBytes   269 Mbits/sec   50             sender
    [  5]   0.00-10.00  sec   318 MBytes   266 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.163 port 33825 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  30.8 MBytes   258 Mbits/sec    0   1.68 MBytes       
    [  5]   1.00-2.00   sec  30.8 MBytes   258 Mbits/sec  124   1.08 MBytes       
    [  5]   2.00-3.00   sec  31.4 MBytes   263 Mbits/sec    0   1.09 MBytes       
    [  5]   3.00-4.00   sec  29.8 MBytes   250 Mbits/sec    0   1.09 MBytes       
    [  5]   4.00-5.00   sec  30.9 MBytes   259 Mbits/sec    0   1.09 MBytes       
    [  5]   5.00-6.00   sec  30.2 MBytes   254 Mbits/sec    0   1.09 MBytes       
    [  5]   6.00-7.00   sec  30.6 MBytes   257 Mbits/sec    0   1.09 MBytes       
    [  5]   7.00-8.00   sec  30.4 MBytes   255 Mbits/sec    0   1.09 MBytes       
    [  5]   8.00-9.00   sec  29.8 MBytes   250 Mbits/sec    0   1.09 MBytes       
    [  5]   9.00-10.00  sec  30.2 MBytes   254 Mbits/sec    0   1.09 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   305 MBytes   256 Mbits/sec  124             sender
    [  5]   0.00-10.01  sec   302 MBytes   253 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">RTL8822CE</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">579</span> Mbits/sec | <span style="font-size: 1.5rem;">595</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.127 port 37071 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  77.7 MBytes   652 Mbits/sec                  
    [  5]   1.00-2.00   sec  76.9 MBytes   645 Mbits/sec                  
    [  5]   2.00-3.00   sec  77.5 MBytes   650 Mbits/sec                  
    [  5]   3.00-4.00   sec  70.7 MBytes   593 Mbits/sec                  
    [  5]   4.00-5.00   sec  62.7 MBytes   526 Mbits/sec                  
    [  5]   5.00-6.00   sec  60.1 MBytes   504 Mbits/sec                  
    [  5]   6.00-7.00   sec  63.2 MBytes   530 Mbits/sec                  
    [  5]   7.00-8.00   sec  64.8 MBytes   544 Mbits/sec                  
    [  5]   8.00-9.00   sec  67.2 MBytes   563 Mbits/sec                  
    [  5]   9.00-10.00  sec  66.4 MBytes   557 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   691 MBytes   579 Mbits/sec  983             sender
    [  5]   0.00-10.00  sec   687 MBytes   576 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.127 port 39737 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  78.0 MBytes   654 Mbits/sec    0   6.44 MBytes       
    [  5]   1.00-2.00   sec  76.2 MBytes   640 Mbits/sec  178   3.22 MBytes       
    [  5]   2.00-3.00   sec  71.2 MBytes   598 Mbits/sec  186    895 KBytes       
    [  5]   3.00-4.00   sec  70.0 MBytes   587 Mbits/sec    0   1003 KBytes       
    [  5]   4.00-5.00   sec  71.2 MBytes   598 Mbits/sec    0   1.07 MBytes       
    [  5]   5.00-6.00   sec  72.5 MBytes   608 Mbits/sec    0   1.16 MBytes       
    [  5]   6.00-7.00   sec  70.0 MBytes   587 Mbits/sec  118    656 KBytes       
    [  5]   7.00-8.00   sec  63.8 MBytes   533 Mbits/sec    0    785 KBytes       
    [  5]   8.00-9.00   sec  67.5 MBytes   567 Mbits/sec    0    902 KBytes       
    [  5]   9.00-10.00  sec  68.8 MBytes   577 Mbits/sec    0   1007 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   709 MBytes   595 Mbits/sec  482             sender
    [  5]   0.00-10.01  sec   707 MBytes   593 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 145690 bytes (521 packets)
    TX: 59796 bytes (218 packets)
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
|<span style="font-size: 1.5rem;">AX200</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">474</span> Mbits/sec | <span style="font-size: 1.5rem;">254</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.116 port 57331 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  52.0 MBytes   436 Mbits/sec                  
    [  5]   1.00-2.00   sec  82.8 MBytes   694 Mbits/sec                  
    [  5]   2.00-3.00   sec  60.0 MBytes   503 Mbits/sec                  
    [  5]   3.00-4.00   sec  69.0 MBytes   579 Mbits/sec                  
    [  5]   4.00-5.00   sec  51.9 MBytes   435 Mbits/sec                  
    [  5]   5.00-6.00   sec  57.4 MBytes   481 Mbits/sec                  
    [  5]   6.00-7.00   sec  40.6 MBytes   341 Mbits/sec                  
    [  5]   7.00-8.00   sec  33.0 MBytes   277 Mbits/sec                  
    [  5]   8.00-9.00   sec  64.4 MBytes   540 Mbits/sec                  
    [  5]   9.00-10.00  sec  51.8 MBytes   434 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   566 MBytes   474 Mbits/sec  292             sender
    [  5]   0.00-10.00  sec   563 MBytes   472 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.116 port 53987 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.5 MBytes   214 Mbits/sec  320    392 KBytes       
    [  5]   1.00-2.00   sec  41.0 MBytes   344 Mbits/sec    0    520 KBytes       
    [  5]   2.00-3.00   sec  30.5 MBytes   256 Mbits/sec   37    325 KBytes       
    [  5]   3.00-4.00   sec  28.8 MBytes   241 Mbits/sec    0    437 KBytes       
    [  5]   4.00-5.00   sec  38.0 MBytes   319 Mbits/sec    0    547 KBytes       
    [  5]   5.00-6.00   sec  38.0 MBytes   319 Mbits/sec    9    355 KBytes       
    [  5]   6.00-7.00   sec  33.8 MBytes   283 Mbits/sec   30    245 KBytes       
    [  5]   7.00-8.00   sec  19.0 MBytes   159 Mbits/sec    0    337 KBytes       
    [  5]   8.00-9.00   sec  22.1 MBytes   186 Mbits/sec    0    419 KBytes       
    [  5]   9.00-10.00  sec  26.0 MBytes   218 Mbits/sec    3    328 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   303 MBytes   254 Mbits/sec  399             sender
    [  5]   0.00-10.01  sec   300 MBytes   251 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 41770 bytes (144 packets)
    TX: 48246 bytes (212 packets)
    signal: -35 dBm
    rx bitrate: 1200.9 MBit/s 160MHz HE-MCS 11 HE-NSS 1 HE-GI 0 HE-DCM 0
    tx bitrate: 490.0 MBit/s 160MHz HE-MCS 3 HE-NSS 2 HE-GI 2 HE-DCM 0
    ```
### N

#### Broadcom 43430

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43430.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43430</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">46.2</span> Mbits/sec | <span style="font-size: 1.5rem;">40.1</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.164 port 34053 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.80 MBytes  40.2 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.62 MBytes  47.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.06 MBytes  42.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.86 MBytes  40.8 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.30 MBytes  44.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.12 MBytes  42.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.96 MBytes  41.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.32 MBytes  44.6 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.28 MBytes  44.3 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.35 MBytes  44.9 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec  55.2 MBytes  46.2 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  51.7 MBytes  43.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.164 port 59297 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.22 MBytes  43.8 Mbits/sec    0    199 KBytes       
    [  5]   1.00-2.00   sec  4.78 MBytes  40.1 Mbits/sec    0    219 KBytes       
    [  5]   2.00-3.00   sec  4.72 MBytes  39.6 Mbits/sec    0    229 KBytes       
    [  5]   3.00-4.00   sec  4.78 MBytes  40.1 Mbits/sec    0    229 KBytes       
    [  5]   4.00-5.00   sec  4.78 MBytes  40.1 Mbits/sec    0    242 KBytes       
    [  5]   5.00-6.00   sec  4.54 MBytes  38.1 Mbits/sec    0    242 KBytes       
    [  5]   6.00-7.00   sec  4.97 MBytes  41.7 Mbits/sec    0    256 KBytes       
    [  5]   7.00-8.00   sec  4.78 MBytes  40.1 Mbits/sec    0    307 KBytes       
    [  5]   8.00-9.00   sec  4.72 MBytes  39.6 Mbits/sec    0    307 KBytes       
    [  5]   9.00-10.00  sec  4.54 MBytes  38.1 Mbits/sec    0    307 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  47.8 MBytes  40.1 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  47.1 MBytes  39.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 78764 bytes (231 packets)
    TX: 61055 bytes (292 packets)
    signal: -57 dBm
    rx bitrate: 65.0 MBit/s
    tx bitrate: 65.0 MBit/s
    
    ```

#### Broadcom 43455

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/BCM43455.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">BCM43455</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">43.0</span> Mbits/sec | <span style="font-size: 1.5rem;">54.9</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.120 port 55497 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  5.40 MBytes  45.3 Mbits/sec                  
    [  5]   1.00-2.00   sec  5.27 MBytes  44.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.11 MBytes  42.9 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.24 MBytes  44.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.31 MBytes  44.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.06 MBytes  42.5 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.79 MBytes  40.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.82 MBytes  40.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.03 MBytes  42.2 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.83 MBytes  40.5 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.52  sec  53.9 MBytes  43.0 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  50.9 MBytes  42.7 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.120 port 50257 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.98 MBytes  58.5 Mbits/sec    0    233 KBytes       
    [  5]   1.00-2.00   sec  6.84 MBytes  57.3 Mbits/sec    0    276 KBytes       
    [  5]   2.00-3.00   sec  5.84 MBytes  49.0 Mbits/sec    0    276 KBytes       
    [  5]   3.00-4.00   sec  6.90 MBytes  57.8 Mbits/sec    0    310 KBytes       
    [  5]   4.00-5.00   sec  5.90 MBytes  49.6 Mbits/sec    0    310 KBytes       
    [  5]   5.00-6.00   sec  6.65 MBytes  55.8 Mbits/sec    0    327 KBytes       
    [  5]   6.00-7.00   sec  6.21 MBytes  52.1 Mbits/sec    0    341 KBytes       
    [  5]   7.00-8.00   sec  6.84 MBytes  57.3 Mbits/sec    0    362 KBytes       
    [  5]   8.00-9.00   sec  5.28 MBytes  44.3 Mbits/sec    0    362 KBytes       
    [  5]   9.00-10.00  sec  8.06 MBytes  67.7 Mbits/sec    0    618 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  65.5 MBytes  54.9 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  63.1 MBytes  52.9 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 68794 bytes (197 packets)
    TX: 57710 bytes (265 packets)
    signal: -51 dBm
    rx bitrate: 433.3 MBit/s
    tx bitrate: 433.3 MBit/s
    
    ```

#### Realtek 8723BS

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BS.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.2.1, 6.12.13-current-rockchip</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BS</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">23.8</span> Mbits/sec | <span style="font-size: 1.5rem;">49.4</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.134 port 49701 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  8.88 MBytes  74.5 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.80 MBytes  40.3 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.13 MBytes  34.6 Mbits/sec                  
    [  5]   3.00-4.00   sec   348 KBytes  2.85 Mbits/sec                  
    [  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec                  
    [  5]   5.00-6.00   sec  2.27 MBytes  19.0 Mbits/sec                  
    [  5]   6.00-7.00   sec   389 KBytes  3.19 Mbits/sec                  
    [  5]   7.00-8.00   sec  2.09 MBytes  17.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  2.51 MBytes  21.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  28.4 MBytes  23.8 Mbits/sec    6             sender
    [  5]   0.00-10.00  sec  25.4 MBytes  21.3 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.134 port 60521 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  9.38 MBytes  78.7 Mbits/sec    0    464 KBytes       
    [  5]   1.00-2.00   sec  5.53 MBytes  46.4 Mbits/sec    0    703 KBytes       
    [  5]   2.00-3.00   sec  2.49 MBytes  20.9 Mbits/sec    0    765 KBytes       
    [  5]   3.00-4.00   sec  2.73 MBytes  22.9 Mbits/sec    0    874 KBytes       
    [  5]   4.00-5.00   sec  4.10 MBytes  34.4 Mbits/sec    0    983 KBytes       
    [  5]   5.00-6.00   sec  2.24 MBytes  18.8 Mbits/sec    0   1.04 MBytes       
    [  5]   6.00-7.00   sec  7.83 MBytes  65.7 Mbits/sec    0   1.04 MBytes       
    [  5]   7.00-8.00   sec  7.83 MBytes  65.7 Mbits/sec    0   1.04 MBytes       
    [  5]   8.00-9.00   sec  7.83 MBytes  65.7 Mbits/sec    0   1.04 MBytes       
    [  5]   9.00-10.00  sec  8.95 MBytes  75.1 Mbits/sec    0   1.04 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  58.9 MBytes  49.4 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec  56.2 MBytes  47.0 Mbits/sec                  receiver
    
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
|<span style="font-size: 1.5rem;">UWE5622</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">145</span> Mbits/sec | <span style="font-size: 1.5rem;">139</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.128 port 59635 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  15.8 MBytes   133 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   3.00-4.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   4.00-5.00   sec  15.3 MBytes   128 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.7 MBytes   157 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.0 MBytes   143 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.2 MBytes   144 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.0 MBytes   142 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   173 MBytes   145 Mbits/sec  402             sender
    [  5]   0.00-10.00  sec   169 MBytes   142 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.128 port 48169 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  17.6 MBytes   147 Mbits/sec    0    311 KBytes       
    [  5]   1.00-2.00   sec  16.3 MBytes   137 Mbits/sec    0    311 KBytes       
    [  5]   2.00-3.00   sec  16.2 MBytes   136 Mbits/sec    0    311 KBytes       
    [  5]   3.00-4.00   sec  16.8 MBytes   141 Mbits/sec    0    344 KBytes       
    [  5]   4.00-5.00   sec  16.0 MBytes   134 Mbits/sec    0    344 KBytes       
    [  5]   5.00-6.00   sec  17.0 MBytes   143 Mbits/sec    0    344 KBytes       
    [  5]   6.00-7.00   sec  16.8 MBytes   141 Mbits/sec    0    395 KBytes       
    [  5]   7.00-8.00   sec  16.3 MBytes   137 Mbits/sec    0    395 KBytes       
    [  5]   8.00-9.00   sec  16.5 MBytes   138 Mbits/sec    0    395 KBytes       
    [  5]   9.00-10.00  sec  16.5 MBytes   139 Mbits/sec    0    395 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   166 MBytes   139 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   164 MBytes   137 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500
    RX: 4237083085 bytes (3498008 packets)
    ```

#### Xradio XR819

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/XR819.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.5.1, 6.12.23-current-sunxi</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">XR819</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">16.4</span> Mbits/sec | <span style="font-size: 1.5rem;">10.7</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.247 port 57947 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.87 MBytes  15.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  1.85 MBytes  15.5 Mbits/sec                  
    [  5]   2.00-3.00   sec  1.68 MBytes  14.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  1.96 MBytes  16.4 Mbits/sec                  
    [  5]   4.00-5.00   sec  1.78 MBytes  14.9 Mbits/sec                  
    [  5]   5.00-6.00   sec  1.68 MBytes  14.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  1.69 MBytes  14.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  1.72 MBytes  14.4 Mbits/sec                  
    [  5]   8.00-9.00   sec  1.86 MBytes  15.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  1.84 MBytes  15.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.32  sec  20.1 MBytes  16.4 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  17.9 MBytes  15.0 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.247 port 47845 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  1.49 MBytes  12.5 Mbits/sec    0    102 KBytes       
    [  5]   1.00-2.00   sec  1.24 MBytes  10.4 Mbits/sec    0    112 KBytes       
    [  5]   2.00-3.00   sec  1.37 MBytes  11.5 Mbits/sec    0    112 KBytes       
    [  5]   3.00-4.00   sec  1.24 MBytes  10.4 Mbits/sec    0    116 KBytes       
    [  5]   4.00-5.00   sec  1.12 MBytes  9.38 Mbits/sec    6   82.0 KBytes       
    [  5]   5.00-6.00   sec  1.24 MBytes  10.4 Mbits/sec    0    102 KBytes       
    [  5]   6.00-7.00   sec  1.24 MBytes  10.4 Mbits/sec    0    109 KBytes       
    [  5]   7.00-8.00   sec  1.24 MBytes  10.4 Mbits/sec    0    112 KBytes       
    [  5]   8.00-9.00   sec  1.24 MBytes  10.4 Mbits/sec    0    112 KBytes       
    [  5]   9.00-10.00  sec  1.30 MBytes  10.9 Mbits/sec    0    115 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  12.7 MBytes  10.7 Mbits/sec    6             sender
    [  5]   0.00-10.05  sec  12.5 MBytes  10.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2437
    RX: 58098 bytes (156 packets)
    TX: 59859 bytes (258 packets)
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
