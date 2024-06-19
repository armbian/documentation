# Networking

Armbian uses **Netplan.io** to describe networking configurations. This is the same on minimal IOT, server CLI and desktop images. However, backends are different. Minimal images are using networkd, which has smaller footprint, while server CLI and desktop are using Network Manager. Which provides GUI tools for managing configurations.

# Default Armbian configuration 

Aembian preinstalled default configuration will run DHCP on all ethernet devices in order to help you connecting to the device and configure it appropriate.

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

 # Fixed IP address

        network:
          version: 2
          renderer: networkd
          ethernets:
            eth0:
              addresses:
                - 10.0.40.199/24


network:
  version: 2
  renderer: NetworkManager

# Connecting to wireless hotspot

You can add to existing configuration or you can make a separate config file for wireless network. Replace `wlan0` with a device used on your system.

Generate a file `/etc/netplan/armbian-default.yaml`

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

# Applying configuration

### Fix permission to get rid of warnings
sudo chmod 600 /etc/netplan/*.yaml 

### Syntax test of configuration
sudo netplan try

### Apply configuration
sudo netplan apply
