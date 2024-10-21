# Automatic first boot configuration

## Reading presets from local config

It is possible to configure your image automatically when you first boot your device. After flashing a fresh image writing config to the file:

???+ info

    This file will be read at your first login and configure system automatically.

```bash
/root/.not_logged_in_yet
```

Mount your live image _before your first boot_ and use this example for reference:

```bash
# Set PRESET_NET_CHANGE_DEFAULTS to 1 to apply any network related 
# settings below
PRESET_NET_CHANGE_DEFAULTS="1"

# Enable WiFi or Ethernet. # If both are enabled, WiFi will take priority 
# and Ethernet will be disabled.
PRESET_NET_ETHERNET_ENABLED="1"
PRESET_NET_WIFI_ENABLED="1"

# Enter your WiFi credentials
# SECURITY WARN: Your wifi keys will be stored in plaintext, no encryption.
PRESET_NET_WIFI_SSID="MySSID"
PRESET_NET_WIFI_KEY="MyWiFiKEY"

# Country code to enable power ratings and channels for your country. 
# eg: GB US DE | https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
PRESET_NET_WIFI_COUNTRYCODE="GB"

#If you want to use a static ip, set it here
PRESET_NET_USE_STATIC="1"
PRESET_NET_STATIC_IP="192.168.0.100"
PRESET_NET_STATIC_MASK="255.255.255.0"
PRESET_NET_STATIC_GATEWAY="192.168.0.1"
PRESET_NET_STATIC_DNS="8.8.8.8 8.8.4.4"

# Preset user default shell, you can choose bash or zsh
PRESET_USER_SHELL="bash"

# Set PRESET_CONNECT_WIRELESS=y if you want to connect wifi manually 
# at first login
PRESET_CONNECT_WIRELESS="n"

# Set SET_LANG_BASED_ON_LOCATION=n if you want to choose 
# "Set user language based on your location?" with "n" at first login
SET_LANG_BASED_ON_LOCATION="y"

# Preset default locale
PRESET_LOCALE="en_US.UTF-8"

# Preset timezone
PRESET_TIMEZONE="Etc/UTC"

# Preset root password
PRESET_ROOT_PASSWORD="RootPassword"

# Preset URL for root SSH key
# Use GitHub stored keys: https://github.com/<username>.keys
PRESET_ROOT_KEY=""

# Preset username
PRESET_USER_NAME="armbian"

# Preset user password
PRESET_USER_PASSWORD="UserPassword"

# Preset URL for user SSH key
# Use GitHub stored keys: https://github.com/<username>.keys
PRESET_USER_KEY=""

# Preset user default realname
PRESET_DEFAULT_REALNAME="Armbian user"

```

## Reading presets from remote config

You can use the same config file for more images. In this case you create file that is accessible via HTTP with the same content and place only URL to this config

```bash
/root/.not_logged_in_yet
```

```
PRESET_CONFIGURATION="http://URL_OF_THIS_CONFIG"
```

???+ tip

    If you want to use first run automatic configuration at build time, [check this GitHub pull request](https://github.com/armbian/build/pull/6194).

    tl;dr;

    1. Copy the template with `cp extensions/preset-firstrun.sh userpatches/extensions/`
    2. Edit the template `userpatches/extensions/preset-firstrun.sh` according to your situation
    3. Build your Armbian image using the additional parameter `ENABLE_EXTENSIONS=preset-firstrun`