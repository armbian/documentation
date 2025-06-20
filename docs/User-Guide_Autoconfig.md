# Automatic first boot configuration

## Reading presets from local config

It is possible to configure your device automatically at first boot. Settings like: root password, IP address, connecting to wireless.

After flashing an image to boot media, mount it and add a file containing your config to `/root/.not_logged_in_yet`

???+ tip
    You may also mount the image and edit it prior to flashing, if this is preferable.

## Loading a remote config

It is also possible to load this config file from a remote server, as above, however the **only** directive you should include is:

```bash title="/root/.not_logged_in_yet"
PRESET_CONFIGURATION="http://path/to/config/file"
```

## Configuration directives

- The directives in this file are specified using `key="value"` format.  
- To ask for a value interactively, leave it unset or comment out the directive.  
- For fully-unattended setup, specify all values.  

!!! caution
    No validation of this network config is performed, wrong settings will lead to broken network.  
    Armbian supports [netplan.io](https://netplan.io), this is the preferred config method.  
    See [netplan guides](https://netplan.readthedocs.io/en/stable/examples/) for various example configurations.  
    Netplan config is stored in `/etc/netplan/`.  

| Configuration directive | `[default]` \| `option` | Description: |
| :---------------------- | :-------------- | :----------- |
| `PRESET_CONFIGURATION` |  `http://path/to/config/file` |  See [Loading a remote config](#loading-a-remote-config) |
| `PRESET_NET_CHANGE_DEFAULTS` | `[0]` \| `1` | Change default network settings<br>if unset, **no network changes will be applied** |
| `PRESET_NET_ETHERNET_ENABLED` | `0` \| `1` | Enable Ethernet, ignored if WiFi enabled |
| `PRESET_NET_WIFI_ENABLED` | `0` \| `1` | Enable WiFi, **takes priority over Ethernet** |
| `PRESET_NET_WIFI_SSID` | `MySSID` | WiFi SSID |
| `PRESET_NET_WIFI_KEY` | `MyWPA-PSK` | WiFi Pre-Shared Key (Password), **stored in plaintext** |
| `PRESET_NET_WIFI_COUNTRYCODE` | `CC` | Country code, **required** for WiFi<br>e.g. `GB`, `US`, `DE`; see [Wikipedia/ISO_3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |
| `PRESET_CONNECT_WIRELESS` | `Y` \| `n` | Set to `Y` for interactive mode, `n` uses values from file |
| `PRESET_NET_USE_STATIC` | `[0]` \| `1` | Use the static IP provided, DHCP is the default<br>Leaving **any** value unset will result in a broken config |
| `PRESET_NET_STATIC_IP` | `xxx.xxx.xxx.xxx` | Static IPv4 address, dotted decimal notation |
| `PRESET_NET_STATIC_MASK` | `xxx.xxx.xxx.xxx` | Subnet mask, typically `255.255.255.0` |
| `PRESET_NET_STATIC_GATEWAY` | `xxx.xxx.xxx.xxx` | Default gateway address |
| `PRESET_NET_STATIC_DNS` | `x.x.x.x x.x.x.x` | DNS Servers to use, separated by a space. If unsure:<br>CloudFlare is `1.1.1.1 1.0.0.1`<br>Google is `8.8.8.8 8.8.4.4` |
| `SET_LANG_BASED_ON_LOCATION` | `Y` \| `n` | "Set user language based on your location?" |
| `PRESET_LOCALE` | `locale` | Locale e.g. `en_GB.UTF-8`, `de_DE.UTF-8`, `zh_TW.UTF-8` |
| `PRESET_TIMEZONE` | `timezone` | Timezone e.g. `Etc/UTC`, |
| `PRESET_ROOT_PASSWORD` | `[1234]` \| `password` | Preset `root` password<br>**Stored in plaintext**, *SSH keys are safer!* |
| `PRESET_ROOT_KEY` | `https://path/to/key.file` | Fetches public key from specified URL for `root` user |
| `PRESET_USER_NAME` | `username` | Username to create |
| `PRESET_USER_PASSWORD` | `password` | Preset created user password<br>**Stored in plaintext**, *SSH keys are safer!* |
| `PRESET_USER_KEY` | `https://path/to/key.file` | Fetches public key from specified URL for created user |
| `PRESET_DEFAULT_REALNAME` | `Real Name` | RealName to use for created user |
| `PRESET_USER_SHELL` | `shell` | Currently only `bash` (default) or `zsh` (`armbian-zsh`) supported |

## Sample config file

The following is an example configuration, it may be used as a template  

```bash title="/root/.not_logged_in_yet"
#/root/.not_logged_in_yet
# Network Settings
PRESET_NET_CHANGE_DEFAULTS="1"
## Ethernet
PRESET_NET_ETHERNET_ENABLED="1"     #   Ignored due to WiFi
## WiFi
PRESET_NET_WIFI_ENABLED="1"
PRESET_NET_WIFI_SSID="MySSID"
PRESET_NET_WIFI_KEY="MyWiFiKEY"
PRESET_NET_WIFI_COUNTRYCODE="GB"
PRESET_CONNECT_WIRELESS="n"
## Static IP
PRESET_NET_USE_STATIC="1"
PRESET_NET_STATIC_IP="192.168.0.100"
PRESET_NET_STATIC_MASK="255.255.255.0"
PRESET_NET_STATIC_GATEWAY="192.168.0.1"
PRESET_NET_STATIC_DNS="8.8.8.8 8.8.4.4"

# System
SET_LANG_BASED_ON_LOCATION="y"
PRESET_LOCALE="en_US.UTF-8"
PRESET_TIMEZONE="Etc/UTC"

# Root
PRESET_ROOT_PASSWORD="RootPassword"
PRESET_ROOT_KEY=""

# User
PRESET_USER_NAME="armbian"
PRESET_USER_PASSWORD="UserPassword"
PRESET_USER_KEY=""
PRESET_DEFAULT_REALNAME="Armbian user"
PRESET_USER_SHELL="bash"
```

???+ tip

    If you want to use first run automatic configuration at build time, [check this GitHub pull request](https://github.com/armbian/build/pull/6194).

    tl;dr;

    1. Copy the template with `cp extensions/preset-firstrun.sh userpatches/extensions/`
    2. Edit the template `userpatches/extensions/preset-firstrun.sh` according to your situation
    3. Build your Armbian image using the additional parameter `ENABLE_EXTENSIONS=preset-firstrun`

## Provisioning script

`/root/provisioning.sh` is executed once as root after the first successful login, either manual or automated. It’s used to perform final system setup tasks like installing packages, configuring the system, or enabling services.

The example script updates package lists, installs htop, sets a custom hostname.


```bash title="/root/provisioning.sh"
#!/bin/bash
set -e
echo "Provisioning started"
apt update && apt install -y htop
hostnamectl set-hostname my-device
echo "Provisioning complete"
```
