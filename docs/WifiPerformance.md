# Testing the speed of wireless connections

All Wi-Fi adapters were tested under consistent conditions—each positioned in close proximity and connected to the same wireless access point (AP). The adapters utilized various interface types, including USB, SDIO, and PCI, to evaluate performance across different hardware configurations.

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
**Test Date:** [15.3.2025](https://github.com/armbian/armbian.github.io/actions/runs/14419550871)
### Alfa RT3572

<img src=https://stuff.armbian.com/netbox/media/devicetype-images/RT3572.png>

<span style="font-size: 0.5rem;">OS: Armbian v25.2.3, 6.12.22-current-x86</span>

| Chipset | Class | Average forward speed | Average reverse speed |
|:-----|------|:-------|:-------|
|<span style="font-size: 1.5rem;">RT3572</span> | <span style="font-size: 1.5rem;">N</span> | <span style="font-size: 1.5rem;">90.3</span> Mbits/sec | <span style="font-size: 1.5rem;">65.1</span> Mbits/sec |

=== "Forward mode (client to server)"

    ```
    Connecting to host 10.0.60.10, port 5201
    Reverse mode, remote host 10.0.60.10 is sending
    [  5] local 10.0.50.246 port 39519 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  5]   0.00-1.00   sec  10.2 MBytes  86.0 Mbits/sec                  
    [  5]   1.00-2.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   2.00-3.00   sec  10.4 MBytes  87.1 Mbits/sec                  
    [  5]   3.00-4.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   4.00-5.00   sec  10.6 MBytes  89.1 Mbits/sec                  
    [  5]   5.00-6.00   sec  10.1 MBytes  84.9 Mbits/sec                  
    [  5]   6.00-7.00   sec  10.8 MBytes  90.2 Mbits/sec                  
    [  5]   7.00-8.00   sec  10.9 MBytes  91.2 Mbits/sec                  
    [  5]   8.00-9.00   sec  11.1 MBytes  93.4 Mbits/sec                  
    [  5]   9.00-10.00  sec  11.0 MBytes  92.2 Mbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.01  sec   108 MBytes  90.3 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   106 MBytes  88.8 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Reverse mode (server to client)"

    ```
    Connecting to host 10.0.60.10, port 5201
    [  5] local 10.0.50.246 port 33001 connected to 10.0.60.10 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  8.50 MBytes  71.2 Mbits/sec    0    249 KBytes       
    [  5]   1.00-2.00   sec  8.12 MBytes  68.2 Mbits/sec    0    321 KBytes       
    [  5]   2.00-3.00   sec  7.75 MBytes  65.0 Mbits/sec    0    379 KBytes       
    [  5]   3.00-4.00   sec  7.38 MBytes  61.9 Mbits/sec    0    397 KBytes       
    [  5]   4.00-5.00   sec  7.38 MBytes  61.9 Mbits/sec    0    397 KBytes       
    [  5]   5.00-6.00   sec  8.38 MBytes  70.3 Mbits/sec    0    421 KBytes       
    [  5]   6.00-7.00   sec  7.00 MBytes  58.7 Mbits/sec    0    421 KBytes       
    [  5]   7.00-8.00   sec  7.88 MBytes  66.1 Mbits/sec    0    443 KBytes       
    [  5]   8.00-9.00   sec  7.25 MBytes  60.8 Mbits/sec    0    443 KBytes       
    [  5]   9.00-10.00  sec  8.00 MBytes  67.0 Mbits/sec    0    443 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec  77.6 MBytes  65.1 Mbits/sec    0             sender
    [  5]   0.00-10.01  sec  75.1 MBytes  63.0 Mbits/sec                  receiver
    
    iperf Done.
    ```

=== "Wireless link info"

    ```
    freq: 5500.0
    RX: 88023 bytes (375 packets)
    TX: 66512 bytes (240 packets)
    signal: -23 dBm
    rx bitrate: 240.0 MBit/s MCS 13 40MHz short GI
    tx bitrate: 300.0 MBit/s MCS 15 40MHz short GI
    ```
<!-- DUT-STOP -->

## Contribute

We're working hard to push the boundaries of wireless performance testing, but we need your support to make it happen! Your contribution will help us acquire the essential equipment to improve our testing capabilities, ensuring more accurate and comprehensive results.

Every donation counts - buy us a wireless adaptor that is not yet here.
https://www.amazon.de/hz/wishlist/ls/1GA17IGQ2MF0V?ref_=wl_share

## Other resources


- [USB WiFi Adapter Information for Linux](https://github.com/morrownr/USB-WiFi)
