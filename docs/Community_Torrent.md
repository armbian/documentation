# Seed our torrents


To secure top download speed around the globe, we need to have as many torrent seeders as possible. Currently we have dedicated seeders in: Estonia, Germany, Pakistan, Slovenia, Argentina, Singapore, USA, ... but we might be slower in China or Japan.

 

## Prerequisite:

- Armbian or any Debian or Ubuntu based distribution (check instructions how to run `armbian-config` on a generic Debian/Ubuntu)
- `wget` and `unzip` packages installed
- 1TB of free space


a) Installation and auto-config with armbian-config:

 

    login and obtain superuser rights,
    execute armbian-config,
    select Software -> Softy,
    install Transmission server. (use space to confirm and enter to proceed with install)
     

 

Leave `armbian-config` and after a few minutes check your torrent server status with the following command:

`transmission-remote -n 'transmission:transmission' -l`

and you should see some progress:

```
ID     Done       Have  ETA           Up    Down  Ratio  Status       Name
   1     0%       None  Unknown      0.0     0.0   None  Idle         Armbian_5.25_Bananapi_Debian_jessie_default_3.4.113.7z
   2    19%   40.62 MB  10 min       0.0  1085.0    0.0  Downloading  Armbian_5.25_Bananapi_Debian_jessie_next_4.9.7.7z
   3     0%       None  Unknown      0.0     0.0   None  Idle         Armbian_5.25_Bananapim2plus_Debian_jessie_default_3.4.113.7z
   4     0%       None  Unknown      0.0     0.0   None  Idle         Armbian_5.25_Bananapim2plus_Ubuntu_xenial_default_3.4.113.7z
   5     0%       None  Unknown      0.0     0.0   None  Idle         Armbian_5.25_Bananapim2plus_Ubuntu_xenial_default_3.4.113_desktop.7z
   
  [...]
  
 158     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Tinkerboard_Ubuntu_xenial_default_4.4.66_desktop.7z
 159     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Tinkerboard_Ubuntu_xenial_next_4.11.0.7z
 160     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Tinkerboard_Ubuntu_xenial_next_4.11.0_desktop.7z
Sum:          40.62 MB               0.0  1085.0
```

_Note:_
Torrent server installed this way is auto updating - it checks daily for new images, adds new and purge old ones.

 
 

b) Installation to an existing Transmission daemon (manual configuration)


Create file:

`sudo nano /etc/cron.daily/seed-armbian-torrent`

with this content:

```
#!/bin/bash
#
# armbian torrents auto update
#
# download latest torrent pack
TEMP_DIR=$(mktemp -d || exit 1)
chmod 700 ${TEMP_DIR}
trap "rm -rf \"${TEMP_DIR}\" ; exit 0" 0 1 2 3 15
wget -qO- -O ${TEMP_DIR}/armbian-torrents.zip https://dl.armbian.com/torrent/all-torrents.zip
# test zip for corruption
unzip -t ${TEMP_DIR}/armbian-torrents.zip >/dev/null 2>&1
[[ $? -ne 0 ]] && echo "Error in zip" && exit
# extract zip
unzip -o ${TEMP_DIR}/armbian-torrents.zip -d ${TEMP_DIR}/torrent-tmp >/dev/null 2>&1
# create list of current active torrents
transmission-remote -n 'transmission:transmission' -l | sed '1d; $d' > ${TEMP_DIR}/torrent-tmp/active.torrents
# loop and add/update torrent files
for f in ${TEMP_DIR}/torrent-tmp/*.torrent; do
        transmission-remote -n 'transmission:transmission' -a $f > /dev/null 2>&1
        # remove added from the list
        pattern="${f//.torrent}"; pattern="${pattern##*/}";
        sed -i "/$pattern/d" ${TEMP_DIR}/torrent-tmp/active.torrents
done
# remove old armbian torrents
while read i; do
        [[ $i == *Armbian_* || $i == *gcc-linaro-* || $i == *tar.lz4 ]] && transmission-remote -n 'transmission:transmission' -t $(echo "$i" | awk '{print $1}';) --remove-and-delete
done < ${TEMP_DIR}/torrent-tmp/active.torrents
```

 

Change username(transmission) and password(transmission) if have something else than stock, save and exit, then run:

```
sudo chmod +x /etc/cron.daily/seed-armbian-torrent
sudo /etc/cron.daily/seed-armbian-torrent
```


How to stop seeding torrents?

    Remove cron job:

    sudo rm /etc/cron.daily/seed-armbian-torrent


    Remove torrents: 

    transmission-remote -n transmission:transmission -t all --remove-and-delete

    This command will remove ALL files on your torrent server! If you seed other stuff do a cherry pick.

