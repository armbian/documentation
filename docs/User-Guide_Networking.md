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

![](https://www.armbian.com/wp-content/uploads/2016/12/wifi-1.png)

Replace `SSID` with the name of your hot-spot




If you do not know, you can browse and then connect

	nmtui-connect

![](https://www.armbian.com/wp-content/uploads/2016/12/wifi-2.png)

## How to set fixed IP?

By default your main network adapter's IP is assigned by your router DHCP server and all network interfaces are managed by **NetworkManager**:

	user@boardname:~$ nmcli con show
	NAME	UUID	TYPE	DEVICE 
	Wired connection 1	xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx	802-3-ethernet	eth0 

The connection can now be edited with the following:

	nmcli con mod "Wired connection 1"
	  ipv4.addresses "HOST_IP_ADDRESS"
	  ipv4.gateway "IP_GATEWAY"
	  ipv4.dns "DNS_SERVER(S)"
	  ipv4.dns-search "DOMAIN_NAME"
	  ipv4.method "manual"

The same changes can also be done with NetworkManagers text user interface:

	sudo nmtui
