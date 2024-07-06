# Networking

Armbian uses **Netplan.io** to describe networking configurations. This is the same on minimal IOT, server CLI and desktop images, Debian or Ubuntu based. However, backends are different. 

# Minimal images with networkd

Minimal images are using `systemd-networkd`, which has **smaller footprint**. `systemd-networkd` is a system daemon that manages network configurations. It detects and configures network devices as they appear; it can also create virtual network devices. This service can be especially useful to set up complex network configurations. It also works fine on simple connections.

## Default Armbian configuration 

Preinstalled configuration will run DHCP on all ethernet devices in order to help you connecting to the device and configure it appropriate.

`/etc/netplan/armbian-default.yaml`

    network:
      version: 2
      renderer: networkd
      ethernets:
        alleths:
          match:
            name: e*
          dhcp4: true
          dhcp6: true

## Configuration examples

###  Set fixed IP address

`/etc/netplan/armbian-default.yaml`

    network:
      version: 2
      renderer: networkd
      ethernets:
        eth0:
          addresses:
          - 10.0.40.199/24
          routes:
          - to: default
            via: 10.0.40.1
          nameservers:
           addresses: [9.9.9.9,8.8.8.8,8.8.4.4]
               
### Connect to wireless hotspot

It is recommended to make a separate config file for wireless network.

Generate a file:

    sudo nano /etc/netplan/armbian-default.yaml

with content:

    version: 2
    renderer: networkd
    network:
      wifis:
        wlan0:
          dhcp4: true
          dhcp6: true
          access-points:
            "SSID":
              password: "password"

Replace `SSID` with the name of your hot-spot and `wlan0` with a device used on your system.

## Applying configuration

Once you are done with configuring your network its time to test syntax and apply it.

### 1.  Fix configurations permissions

    sudo chmod 600 /etc/netplan/*.yaml 

### 2. Test if syntax is correct

    sudo netplan try

### 3.  Apply configuration

    sudo netplan apply

# CLI and desktop images with NetworkManager

Cerver CLI and desktop images are using Network Manager. You can use the same methods as for minimal images.

###  Set fixed IP address

`/etc/netplan/armbian-default.yaml`

    network:
      version: 2
      renderer: NetworkManager
      ethernets:
        eth0:
          addresses:
          - 10.0.40.199/24
          routes:
          - to: default
            via: 10.0.40.1
          nameservers:
           addresses: [9.9.9.9,8.8.8.8,8.8.4.4]

But you can also use CLI / GUI tools

    nmtui-connect SSID

![](images/wifi-connect.png)

Replace `SSID` with the name of your hot-spot

    nmtui-edit eth0

![](images/edit-connection.png)

Replace `eth0` with the name of your network device.

# Automatic configuration at first run

It is possible to store first run preset network settings to the file `/root/.not_logged_in_yet` which is read and executed at first login.

Mount live image before first run and use this example:

    # Set PRESET_NET_CHANGE_DEFAULTS to 1 to apply any network related settings below
    
    PRESET_NET_CHANGE_DEFAULTS="1"

    # Enable WiFi or Ethernet.
    # NB: If both are enabled, WiFi will take priority and Ethernet will be disabled.
    
    PRESET_NET_ETHERNET_ENABLED=1
    PRESET_NET_WIFI_ENABLED=1

    # Enter your WiFi creds
    # SECURITY WARN: Your wifi keys will be stored in plaintext, no encryption.
    
    PRESET_NET_WIFI_SSID='MySSID'
    PRESET_NET_WIFI_KEY='MyWiFiKEY'

    # Country code to enable power ratings and channels for your country. 
    
    # eg: GB US DE | https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    PRESET_NET_WIFI_COUNTRYCODE='GB'

    # If you want to use a static ip, set it here
    
    PRESET_NET_USE_STATIC=1
    PRESET_NET_STATIC_IP='192.168.0.100'
    PRESET_NET_STATIC_MASK='255.255.255.0'
    PRESET_NET_STATIC_GATEWAY='192.168.0.1'
    PRESET_NET_STATIC_DNS='9.9.9.9 1.1.1.1'

If you want to use first run automatic configuration at build time, [check this](https://github.com/armbian/build/pull/6194).

1. Copy `cp extensions/preset-firstrun.sh userpatches/extensions/`
2. Edit `userpatches/extensions/preset-firstrun.sh` according to your situation
3. Build with additional parameter `ENABLE_EXTENSIONS=preset-firstrun`

Note: this method also adds new user, sets passwords, ...
