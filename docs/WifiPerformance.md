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
**Test Date:** [2025-06-14 01:48 UTC](https://github.com/armbian/armbian.github.io/actions/runs/15646660760)
### AC

#### EDUP EP-AC1681

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL88x2BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL88x2BU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">154</span> Mbits/sec | <span style="font-size: 1.5rem;">257</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.148 port 38703 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  14.1 MBytes   118 Mbits/sec                  
    [  5]   1.00-2.00   sec  12.1 MBytes   102 Mbits/sec                  
    [  5]   2.00-3.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   3.00-4.00   sec  19.2 MBytes   161 Mbits/sec                  
    [  5]   4.00-5.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   5.00-6.00   sec  19.1 MBytes   160 Mbits/sec                  
    [  5]   6.00-7.00   sec  19.4 MBytes   163 Mbits/sec                  
    [  5]   7.00-8.00   sec  19.1 MBytes   160 Mbits/sec                  
    [  5]   8.00-9.00   sec  19.8 MBytes   166 Mbits/sec                  
    [  5]   9.00-10.00  sec  19.0 MBytes   159 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   184 MBytes   154 Mbits/sec  186             sender
    [  5]   0.00-10.00  sec   180 MBytes   151 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.148 port 59123 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  27.2 MBytes   228 Mbits/sec    0    641 KBytes       
    [  5]   1.00-2.00   sec  26.4 MBytes   221 Mbits/sec    0    713 KBytes       
    [  5]   2.00-3.00   sec  29.2 MBytes   245 Mbits/sec    0    822 KBytes       
    [  5]   3.00-4.00   sec  30.4 MBytes   255 Mbits/sec    0    865 KBytes       
    [  5]   4.00-5.00   sec  33.0 MBytes   277 Mbits/sec    0   1.22 MBytes       
    [  5]   5.00-6.00   sec  31.5 MBytes   264 Mbits/sec    0   1.22 MBytes       
    [  5]   6.00-7.00   sec  31.5 MBytes   264 Mbits/sec    0   1.22 MBytes       
    [  5]   7.00-8.00   sec  32.9 MBytes   276 Mbits/sec    0   1.22 MBytes       
    [  5]   8.00-9.00   sec  31.6 MBytes   265 Mbits/sec    0   1.22 MBytes       
    [  5]   9.00-10.00  sec  32.8 MBytes   275 Mbits/sec    0   1.22 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   306 MBytes   257 Mbits/sec    0             sender
    [  5]   0.00-10.03  sec   304 MBytes   254 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 177520 bytes (317 packets)
    TX: 91657 bytes (445 packets)
    signal: -37 dBm
    rx bitrate: 780.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 2
    tx bitrate: 866.7 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 2
    ```

#### Realtek 8811AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">152</span> Mbits/sec | <span style="font-size: 1.5rem;">196</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.147 port 42137 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.0 MBytes   142 Mbits/sec                  
    [  5]   1.00-2.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.4 MBytes   154 Mbits/sec                  
    [  5]   4.00-5.00   sec  18.5 MBytes   155 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.2 MBytes   145 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.8 MBytes   141 Mbits/sec                  
    [  5]   9.00-10.00  sec  17.5 MBytes   147 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   181 MBytes   152 Mbits/sec  198             sender
    [  5]   0.00-10.00  sec   177 MBytes   148 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.147 port 34603 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  25.0 MBytes   210 Mbits/sec    0    583 KBytes       
    [  5]   1.00-2.00   sec  24.0 MBytes   201 Mbits/sec    0    655 KBytes       
    [  5]   2.00-3.00   sec  23.8 MBytes   199 Mbits/sec    0    730 KBytes       
    [  5]   3.00-4.00   sec  22.4 MBytes   188 Mbits/sec    0    730 KBytes       
    [  5]   4.00-5.00   sec  21.0 MBytes   176 Mbits/sec    0    730 KBytes       
    [  5]   5.00-6.00   sec  22.1 MBytes   186 Mbits/sec    0    851 KBytes       
    [  5]   6.00-7.00   sec  23.5 MBytes   197 Mbits/sec    0    851 KBytes       
    [  5]   7.00-8.00   sec  23.8 MBytes   199 Mbits/sec    0    851 KBytes       
    [  5]   8.00-9.00   sec  24.9 MBytes   209 Mbits/sec    0    851 KBytes       
    [  5]   9.00-10.00  sec  23.5 MBytes   197 Mbits/sec    0    851 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   234 MBytes   196 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   231 MBytes   194 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -35 dBm
    tx bitrate: 434.0 MBit/s
    ```

#### Realtek 8812AU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8812AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8812AU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">152</span> Mbits/sec | <span style="font-size: 1.5rem;">270</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.146 port 39293 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  17.6 MBytes   148 Mbits/sec                  
    [  5]   1.00-2.00   sec  18.1 MBytes   152 Mbits/sec                  
    [  5]   2.00-3.00   sec  17.8 MBytes   149 Mbits/sec                  
    [  5]   3.00-4.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   4.00-5.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   5.00-6.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   6.00-7.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   7.00-8.00   sec  17.9 MBytes   150 Mbits/sec                  
    [  5]   8.00-9.00   sec  18.0 MBytes   151 Mbits/sec                  
    [  5]   9.00-10.00  sec  18.0 MBytes   151 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.02  sec   182 MBytes   152 Mbits/sec    3             sender
    [  5]   0.00-10.00  sec   179 MBytes   150 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.146 port 47843 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  32.6 MBytes   273 Mbits/sec    0    827 KBytes       
    [  5]   1.00-2.00   sec  32.9 MBytes   276 Mbits/sec    0    994 KBytes       
    [  5]   2.00-3.00   sec  31.0 MBytes   260 Mbits/sec    0   1.07 MBytes       
    [  5]   3.00-4.00   sec  33.2 MBytes   279 Mbits/sec    0   1.19 MBytes       
    [  5]   4.00-5.00   sec  31.9 MBytes   267 Mbits/sec    0   1.19 MBytes       
    [  5]   5.00-6.00   sec  32.8 MBytes   275 Mbits/sec    0   1.34 MBytes       
    [  5]   6.00-7.00   sec  31.6 MBytes   265 Mbits/sec    0   1.34 MBytes       
    [  5]   7.00-8.00   sec  32.4 MBytes   272 Mbits/sec    0   1.41 MBytes       
    [  5]   8.00-9.00   sec  32.2 MBytes   270 Mbits/sec    0   1.41 MBytes       
    [  5]   9.00-10.00  sec  31.0 MBytes   260 Mbits/sec    0   1.41 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   322 MBytes   270 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec   319 MBytes   268 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    signal: -35 dBm
    tx bitrate: 867.0 MBit/s
    ```

#### Realtek 8821CU #1

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8821CU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8821CU</span> | <span style="font-size: 1.5rem;">AC</span> | <span style="font-size: 1.5rem;">130</span> Mbits/sec | <span style="font-size: 1.5rem;">219</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.145 port 40827 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.6 MBytes   114 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.4 MBytes   112 Mbits/sec                  
    [  5]   3.00-4.00   sec  16.0 MBytes   134 Mbits/sec                  
    [  5]   4.00-5.00   sec  16.5 MBytes   138 Mbits/sec                  
    [  5]   5.00-6.00   sec  16.5 MBytes   138 Mbits/sec                  
    [  5]   6.00-7.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   7.00-8.00   sec  16.4 MBytes   137 Mbits/sec                  
    [  5]   8.00-9.00   sec  16.2 MBytes   136 Mbits/sec                  
    [  5]   9.00-10.00  sec  16.4 MBytes   137 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   155 MBytes   130 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   154 MBytes   129 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.145 port 44807 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  29.1 MBytes   244 Mbits/sec    0    625 KBytes       
    [  5]   1.00-2.00   sec  26.2 MBytes   220 Mbits/sec    0    625 KBytes       
    [  5]   2.00-3.00   sec  25.0 MBytes   210 Mbits/sec    0    625 KBytes       
    [  5]   3.00-4.00   sec  26.1 MBytes   219 Mbits/sec    0    656 KBytes       
    [  5]   4.00-5.00   sec  26.4 MBytes   221 Mbits/sec    0    656 KBytes       
    [  5]   5.00-6.00   sec  25.1 MBytes   211 Mbits/sec    0    656 KBytes       
    [  5]   6.00-7.00   sec  25.1 MBytes   211 Mbits/sec    0    656 KBytes       
    [  5]   7.00-8.00   sec  26.2 MBytes   220 Mbits/sec    0    656 KBytes       
    [  5]   8.00-9.00   sec  25.0 MBytes   210 Mbits/sec    0    656 KBytes       
    [  5]   9.00-10.00  sec  26.2 MBytes   220 Mbits/sec    0    656 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   261 MBytes   219 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   258 MBytes   216 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 187553 bytes (368 packets)
    TX: 92909 bytes (469 packets)
    signal: -37 dBm
    rx bitrate: 390.0 MBit/s VHT-MCS 9 80MHz VHT-NSS 1
    tx bitrate: 433.3 MBit/s VHT-MCS 9 80MHz short GI VHT-NSS 1
    ```
### AX

#### Comfast CF953AX

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/MT7921AU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">MT7921AU</span> | <span style="font-size: 1.5rem;">AX</span> | <span style="font-size: 1.5rem;">112</span> Mbits/sec | <span style="font-size: 1.5rem;">149</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.144 port 34569 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  12.8 MBytes   107 Mbits/sec                  
    [  5]   1.00-2.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   2.00-3.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   3.00-4.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   4.00-5.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   5.00-6.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   6.00-7.00   sec  13.1 MBytes   110 Mbits/sec                  
    [  5]   7.00-8.00   sec  12.9 MBytes   108 Mbits/sec                  
    [  5]   8.00-9.00   sec  13.0 MBytes   109 Mbits/sec                  
    [  5]   9.00-10.00  sec  13.0 MBytes   109 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   133 MBytes   112 Mbits/sec  156             sender
    [  5]   0.00-10.00  sec   130 MBytes   109 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.144 port 48305 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  19.5 MBytes   163 Mbits/sec    0    576 KBytes       
    [  5]   1.00-2.00   sec  17.6 MBytes   148 Mbits/sec    0    684 KBytes       
    [  5]   2.00-3.00   sec  18.0 MBytes   151 Mbits/sec    0    721 KBytes       
    [  5]   3.00-4.00   sec  17.1 MBytes   144 Mbits/sec    0    796 KBytes       
    [  5]   4.00-5.00   sec  16.9 MBytes   142 Mbits/sec    0    796 KBytes       
    [  5]   5.00-6.00   sec  18.1 MBytes   152 Mbits/sec    0    905 KBytes       
    [  5]   6.00-7.00   sec  18.1 MBytes   152 Mbits/sec    0    949 KBytes       
    [  5]   7.00-8.00   sec  18.0 MBytes   151 Mbits/sec    0    998 KBytes       
    [  5]   8.00-9.00   sec  16.8 MBytes   141 Mbits/sec    0    998 KBytes       
    [  5]   9.00-10.00  sec  17.2 MBytes   145 Mbits/sec    0    998 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   177 MBytes   149 Mbits/sec    0             sender
    [  5]   0.00-10.02  sec   175 MBytes   147 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 146759 bytes (452 packets)
    TX: 80189 bytes (496 packets)
    signal: -37 dBm
    rx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    tx bitrate: 1200.9 MBit/s 80MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
    ```
### N

#### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">96.5</span> Mbits/sec | <span style="font-size: 1.5rem;">65.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.143 port 53855 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.9 MBytes  91.1 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.6 MBytes  89.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.2 MBytes  94.3 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.6 MBytes  97.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   115 MBytes  96.5 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   113 MBytes  94.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.143 port 47287 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.88 MBytes  74.4 Mbits/sec    0    243 KBytes       
    [  5]   1.00-2.00   sec  7.75 MBytes  65.0 Mbits/sec    0    270 KBytes       
    [  5]   2.00-3.00   sec  7.25 MBytes  60.8 Mbits/sec    0    270 KBytes       
    [  5]   3.00-4.00   sec  8.25 MBytes  69.2 Mbits/sec    0    288 KBytes       
    [  5]   4.00-5.00   sec  7.75 MBytes  65.0 Mbits/sec    0    318 KBytes       
    [  5]   5.00-6.00   sec  7.75 MBytes  65.0 Mbits/sec    0    318 KBytes       
    [  5]   6.00-7.00   sec  7.38 MBytes  61.9 Mbits/sec    0    318 KBytes       
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec    0    318 KBytes       
    [  5]   8.00-9.00   sec  8.00 MBytes  67.1 Mbits/sec    0    318 KBytes       
    [  5]   9.00-10.00  sec  7.62 MBytes  63.9 Mbits/sec    0    318 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  78.5 MBytes  65.8 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  76.9 MBytes  64.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 198193 bytes (623 packets)
    TX: 95562 bytes (557 packets)
    signal: -17 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Ralink RT5370

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5370.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5370</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">42.9</span> Mbits/sec | <span style="font-size: 1.5rem;">40.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.142 port 46035 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  1.75 MBytes  14.7 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.50 MBytes  37.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   4.00-5.00   sec  5.12 MBytes  43.0 Mbits/sec                  
    [  5]   5.00-6.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   6.00-7.00   sec  5.38 MBytes  45.1 Mbits/sec                  
    [  5]   7.00-8.00   sec  5.50 MBytes  46.1 Mbits/sec                  
    [  5]   8.00-9.00   sec  5.25 MBytes  44.0 Mbits/sec                  
    [  5]   9.00-10.00  sec  5.62 MBytes  47.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec  51.2 MBytes  42.9 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  49.1 MBytes  41.2 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.142 port 49927 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  5.38 MBytes  45.0 Mbits/sec    1    263 KBytes       
    [  5]   1.00-2.00   sec  4.12 MBytes  34.6 Mbits/sec    0    397 KBytes       
    [  5]   2.00-3.00   sec  6.00 MBytes  50.4 Mbits/sec    0    530 KBytes       
    [  5]   3.00-4.00   sec  5.12 MBytes  43.0 Mbits/sec    0    646 KBytes       
    [  5]   4.00-5.00   sec  5.50 MBytes  46.1 Mbits/sec    0    793 KBytes       
    [  5]   5.00-6.00   sec  4.12 MBytes  34.6 Mbits/sec    0    928 KBytes       
    [  5]   6.00-7.00   sec  4.50 MBytes  37.7 Mbits/sec    0    928 KBytes       
    [  5]   7.00-8.00   sec  4.38 MBytes  36.7 Mbits/sec    0    994 KBytes       
    [  5]   8.00-9.00   sec  5.38 MBytes  45.1 Mbits/sec    0    994 KBytes       
    [  5]   9.00-10.00  sec  4.12 MBytes  34.5 Mbits/sec    0   1.09 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  48.6 MBytes  40.8 Mbits/sec    1             sender
    [  5]   0.00-10.01  sec  46.0 MBytes  38.5 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 83729 bytes (362 packets)
    TX: 57585 bytes (205 packets)
    signal: -31 dBm
    rx bitrate: 72.2 MBit/s MCS 7 short GI
    tx bitrate: 72.2 MBit/s MCS 7 short GI
    ```

#### Ralink RT5572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT5572.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RT5572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">95.7</span> Mbits/sec | <span style="font-size: 1.5rem;">66.3</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.141 port 35565 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.4 MBytes  86.9 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   2.00-3.00   sec  11.4 MBytes  95.4 Mbits/sec                  
    [  5]   3.00-4.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   4.00-5.00   sec  11.1 MBytes  93.3 Mbits/sec                  
    [  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   6.00-7.00   sec  11.8 MBytes  98.6 Mbits/sec                  
    [  5]   7.00-8.00   sec  11.5 MBytes  96.5 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   114 MBytes  95.7 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   112 MBytes  93.8 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.141 port 52807 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.62 MBytes  72.3 Mbits/sec    0    178 KBytes       
    [  5]   1.00-2.00   sec  7.25 MBytes  60.8 Mbits/sec    0    222 KBytes       
    [  5]   2.00-3.00   sec  8.00 MBytes  67.1 Mbits/sec    0    253 KBytes       
    [  5]   3.00-4.00   sec  7.75 MBytes  65.0 Mbits/sec    0    274 KBytes       
    [  5]   4.00-5.00   sec  7.88 MBytes  66.1 Mbits/sec    0    274 KBytes       
    [  5]   5.00-6.00   sec  7.88 MBytes  66.1 Mbits/sec    0    274 KBytes       
    [  5]   6.00-7.00   sec  8.00 MBytes  67.1 Mbits/sec    0    286 KBytes       
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec    0    318 KBytes       
    [  5]   8.00-9.00   sec  8.00 MBytes  67.1 Mbits/sec    0    318 KBytes       
    [  5]   9.00-10.00  sec  7.75 MBytes  65.0 Mbits/sec    0    318 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  79.0 MBytes  66.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec  77.6 MBytes  65.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 5500.0
    RX: 96415 bytes (401 packets)
    TX: 59622 bytes (277 packets)
    signal: -24 dBm
    rx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```

#### Realtek 8723BU

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RTL8723BU.png>
<span style="font-size: 0.5rem;">OS: Armbian v25.8.0-trunk.151, 6.12.33-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|-------:|-------:|
|<span style="font-size: 1.5rem;">RTL8723BU</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">40.2</span> Mbits/sec | <span style="font-size: 1.5rem;">48.8</span> Mbits/sec |

=== "Forward mode (client to server)"
    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.149 port 52851 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   1.00-2.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   2.00-3.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   3.00-4.00   sec  4.12 MBytes  34.6 Mbits/sec                  
    [  5]   4.00-5.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   5.00-6.00   sec  4.38 MBytes  36.7 Mbits/sec                  
    [  5]   6.00-7.00   sec  4.62 MBytes  38.8 Mbits/sec                  
    [  5]   7.00-8.00   sec  4.75 MBytes  39.8 Mbits/sec                  
    [  5]   8.00-9.00   sec  4.00 MBytes  33.6 Mbits/sec                  
    [  5]   9.00-10.00  sec  4.62 MBytes  38.8 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.09  sec  48.4 MBytes  40.2 Mbits/sec   35             sender
    [  5]   0.00-10.00  sec  44.6 MBytes  37.4 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Reverse mode (server to client)"
    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.149 port 46737 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  6.88 MBytes  57.6 Mbits/sec    0    334 KBytes       
    [  5]   1.00-2.00   sec  6.50 MBytes  54.5 Mbits/sec    0    450 KBytes       
    [  5]   2.00-3.00   sec  5.62 MBytes  47.2 Mbits/sec    0    450 KBytes       
    [  5]   3.00-4.00   sec  5.62 MBytes  47.2 Mbits/sec    0    501 KBytes       
    [  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec    0    501 KBytes       
    [  5]   5.00-6.00   sec  5.25 MBytes  44.0 Mbits/sec    0    523 KBytes       
    [  5]   6.00-7.00   sec  6.62 MBytes  55.6 Mbits/sec    0    550 KBytes       
    [  5]   7.00-8.00   sec  4.75 MBytes  39.8 Mbits/sec    0    583 KBytes       
    [  5]   8.00-9.00   sec  5.88 MBytes  49.3 Mbits/sec    0    583 KBytes       
    [  5]   9.00-10.00  sec  6.00 MBytes  50.3 Mbits/sec    0    583 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  58.1 MBytes  48.8 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  55.0 MBytes  46.1 Mbits/sec                  receiver
    
    iperf Done.
    ```
=== "Wireless link info"
    ```
    freq: 2462.0
    RX: 112207 bytes (411 packets)
    TX: 62016 bytes (268 packets)
    signal: -50 dBm
    rx bitrate: 65.0 MBit/s MCS 7
    tx bitrate: 72.2 MBit/s MCS 7 short GI
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
