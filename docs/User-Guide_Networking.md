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

But you can also use CLI / GUI tools

	nmtui-connect SSID

![](images/wifi-connect.png)

Replace `SSID` with the name of your hot-spot

        nmtui-edit eth0

![](images/edit-connection.png)

Replace `eth0` with the name of your network device.
