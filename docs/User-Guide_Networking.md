# Networking

Armbian uses **Netplan.io** to describe networking configurations. This is the same on minimal IOT, server CLI and desktop images. However, backends are different. Minimal images are using networkd, which has smaller footprint, while server CLI and desktop are using Network Manager. Which provides GUI tools for managing configurations.

Default Armbian configuration (/etc/netplan/armbian-default.yaml)

        network:
          version: 2
          renderer: networkd
          ethernets:
            alleths:
              match:
                name: e*
              dhcp4: true

Default configuration will run DHCP on all ethernet devices. So you can connect to the device and configure it appropriate. Setting up fixed IP address:

        network:
          version: 2
          renderer: NetworkManager
          ethernets:
            eth0:
              addresses:
                - 10.0.40.199/24
              nameservers:
                addresses:
                  - 10.0.10.10


network:
  version: 2
  renderer: NetworkManager

Connecting to wireless hotspot

Generate a file /etc/netplan/armbian-default.yaml

version: 2
renderer: NetworkManager
network:
  wifis:
    wlan0:
      dhcp4: yes
      dhcp6: yes
      access-points:
        "GOSTJE50":
          password: "password"

Followed by: 

sudo chmod 600 /etc/netplan/armbian-default.yaml 
sudo netplan try
sudo netplan apply

Default permissions are too open. It will still work, but warning would be logged. We use command »try« to check if configuration syntax is ok and apply when we want to change settings.
