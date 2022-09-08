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

<details>
  <summary>Details (click)</summary>
  
```
ID     Done       Have  ETA           Up    Down  Ratio  Status       Name
   1     0%       None  Unknown      0.0     0.0   None  Idle         Armbian_5.25_Bananapi_Debian_jessie_default_3.4.113.7z
   2    19%   40.62 MB  10 min       0.0  1085.0    0.0  Downloading  Armbian_5.25_Bananapi_Debian_jessie_next_4.9.7.7z
   3     0%       None  Unknown      0.0     0.0   None  Idle         Armbian_5.25_Bananapim2plus_Debian_jessie_default_3.4.113.7z
   4     0%       None  Unknown      0.0     0.0   None  Idle         Armbian_5.25_Bananapim2plus_Ubuntu_xenial_default_3.4.113.7z
   5     0%       None  Unknown      0.0     0.0   None  Idle         Armbian_5.25_Bananapim2plus_Ubuntu_xenial_default_3.4.113_desktop.7z
   6     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapipro_Debian_jessie_default_3.4.113.7z
   7     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapipro_Debian_jessie_next_4.9.7.7z
   8     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapipro_Ubuntu_xenial_default_3.4.113.7z
   9     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapipro_Ubuntu_xenial_default_3.4.113_desktop.7z
  10     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapipro_Ubuntu_xenial_next_4.9.7.7z
  11     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapipro_Ubuntu_xenial_next_4.9.7_desktop.7z
  12     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapi_Ubuntu_xenial_default_3.4.113.7z
  13     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapi_Ubuntu_xenial_default_3.4.113_desktop.7z
  14     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapi_Ubuntu_xenial_next_4.9.7.7z
  15     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Bananapi_Ubuntu_xenial_next_4.9.7_desktop.7z
  16     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Beelinkx2_Debian_jessie_default_3.4.113.7z
  17     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Beelinkx2_Ubuntu_xenial_default_3.4.113.7z
  18     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Beelinkx2_Ubuntu_xenial_default_3.4.113_desktop.7z
  19     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Clearfogbase_Debian_jessie_default_4.4.45.7z
  20     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Clearfogbase_Debian_jessie_next_4.9.7.7z
  21     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Clearfogbase_Ubuntu_xenial_default_4.4.45.7z
  22     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Clearfogbase_Ubuntu_xenial_next_4.9.7.7z
  23     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Clearfogpro_Debian_jessie_default_4.4.45.7z
  24     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Clearfogpro_Debian_jessie_next_4.9.7.7z
  25     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Clearfogpro_Ubuntu_xenial_default_4.4.45.7z
  26     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Clearfogpro_Ubuntu_xenial_next_4.9.7.7z
  27     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard2_Debian_jessie_default_3.4.113.7z
  28     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard2_Debian_jessie_next_4.9.7.7z
  29     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard2_Ubuntu_xenial_default_3.4.113.7z
  30     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard2_Ubuntu_xenial_default_3.4.113_desktop.7z
  31     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard2_Ubuntu_xenial_next_4.9.7.7z
  32     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard2_Ubuntu_xenial_next_4.9.7_desktop.7z
  33     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard_Debian_jessie_default_3.4.113.7z
  34     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard_Debian_jessie_next_4.9.7.7z
  35     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard_Ubuntu_xenial_default_3.4.113.7z
  36     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard_Ubuntu_xenial_default_3.4.113_desktop.7z
  37     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard_Ubuntu_xenial_next_4.9.7.7z
  38     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubieboard_Ubuntu_xenial_next_4.9.7_desktop.7z
  39     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubietruck_Debian_jessie_default_3.4.113.7z
  40     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubietruck_Debian_jessie_next_4.9.7.7z
  41     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubietruck_Ubuntu_xenial_default_3.4.113.7z
  42     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubietruck_Ubuntu_xenial_default_3.4.113_desktop.7z
  43     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubietruck_Ubuntu_xenial_next_4.9.7.7z
  44     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubietruck_Ubuntu_xenial_next_4.9.7_desktop.7z
  45     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubox-i_Debian_jessie_default_3.14.79.7z
  46     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubox-i_Debian_jessie_next_4.9.7.7z
  47     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubox-i_Ubuntu_xenial_default_3.14.79.7z
  48     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubox-i_Ubuntu_xenial_default_3.14.79_desktop.7z
  49     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubox-i_Ubuntu_xenial_dev_3.14.79.7z
  50     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubox-i_Ubuntu_xenial_next_4.9.7.7z
  51     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Cubox-i_Ubuntu_xenial_next_4.9.7_desktop.7z
  52     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lamobo-r1_Debian_jessie_default_3.4.113.7z
  53     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lamobo-r1_Debian_jessie_next_4.9.7.7z
  54     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lamobo-r1_Ubuntu_xenial_default_3.4.113.7z
  55     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lamobo-r1_Ubuntu_xenial_next_4.9.7.7z
  56     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime2_Debian_jessie_default_3.4.113.7z
  57     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime2_Debian_jessie_next_4.9.7.7z
  58     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime2_Ubuntu_xenial_default_3.4.113.7z
  59     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime2_Ubuntu_xenial_default_3.4.113_desktop.7z
  60     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime2_Ubuntu_xenial_next_4.9.7.7z
  61     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime2_Ubuntu_xenial_next_4.9.7_desktop.7z
  62     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime-a10_Debian_jessie_default_3.4.113.7z
  63     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime-a10_Debian_jessie_next_4.9.7.7z
  64     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime-a10_Ubuntu_xenial_default_3.4.113_desktop.7z
  65     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime-a10_Ubuntu_xenial_next_4.9.7_desktop.7z
  66     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime-a33_Debian_jessie_next_4.9.7.7z
  67     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime_Debian_jessie_default_3.4.113.7z
  68     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime_Debian_jessie_next_4.9.7.7z
  69     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime_Ubuntu_xenial_default_3.4.113.7z
  70     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime_Ubuntu_xenial_default_3.4.113_desktop.7z
  71     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime_Ubuntu_xenial_next_4.9.7.7z
  72     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Lime_Ubuntu_xenial_next_4.9.7_desktop.7z
  73     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Micro_Debian_jessie_default_3.4.113.7z
  74     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Micro_Debian_jessie_next_4.9.7.7z
  75     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Micro_Ubuntu_xenial_default_3.4.113.7z
  76     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Micro_Ubuntu_xenial_default_3.4.113_desktop.7z
  77     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Micro_Ubuntu_xenial_next_4.9.7.7z
  78     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Micro_Ubuntu_xenial_next_4.9.7_desktop.7z
  79     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopiair_Debian_jessie_default_3.4.113.7z
  80     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopiair_Ubuntu_xenial_default_3.4.113.7z
  81     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopim1_Debian_jessie_default_3.4.113.7z
  82     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopim1plus_Debian_jessie_default_3.4.113.7z
  83     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopim1plus_Ubuntu_xenial_default_3.4.113.7z
  84     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopim1plus_Ubuntu_xenial_default_3.4.113_desktop.7z
  85     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopim1_Ubuntu_xenial_default_3.4.113.7z
  86     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopim1_Ubuntu_xenial_default_3.4.113_desktop.7z
  87     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopineo_Debian_jessie_default_3.4.113.7z
  88     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Nanopineo_Ubuntu_xenial_default_3.4.113.7z
  89     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Odroidc1_Debian_jessie_default_3.10.104.7z
  90     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Odroidc1_Ubuntu_xenial_default_3.10.104.7z
  91     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Odroidc1_Ubuntu_xenial_default_3.10.104_desktop.7z
  92     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Odroidc2_Debian_jessie_default_3.14.79.7z
  93     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Odroidc2_Ubuntu_xenial_default_3.14.79.7z
  94     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Odroidc2_Ubuntu_xenial_default_3.14.79_desktop.7z
  95     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepi2_Debian_jessie_default_3.4.113.7z
  96     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepi2_Ubuntu_xenial_default_3.4.113.7z
  97     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepi2_Ubuntu_xenial_default_3.4.113_desktop.7z
  98     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepilite_Debian_jessie_default_3.4.113.7z
  99     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepilite_Ubuntu_xenial_default_3.4.113.7z
 100     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepilite_Ubuntu_xenial_default_3.4.113_desktop.7z
 101     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepione_Debian_jessie_default_3.4.113.7z
 102     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepione_Ubuntu_xenial_default_3.4.113.7z
 103     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepione_Ubuntu_xenial_default_3.4.113_desktop.7z
 104     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepipc_Debian_jessie_default_3.4.113.7z
 105     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepipcplus_Debian_jessie_default_3.4.113.7z
 106     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepipcplus_Ubuntu_xenial_default_3.4.113.7z
 107     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepipcplus_Ubuntu_xenial_default_3.4.113_desktop.7z
 108     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepipc_Ubuntu_xenial_default_3.4.113.7z
 109     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepipc_Ubuntu_xenial_default_3.4.113_desktop.7z
 110     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepiplus2e_Debian_jessie_default_3.4.113.7z
 111     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepiplus2e_Ubuntu_xenial_default_3.4.113.7z
 112     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepiplus2e_Ubuntu_xenial_default_3.4.113_desktop.7z
 113     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepiplus_Debian_jessie_default_3.4.113.7z
 114     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepiplus_Ubuntu_xenial_default_3.4.113.7z
 115     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepiplus_Ubuntu_xenial_default_3.4.113_desktop.7z
 116     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepizero_Debian_jessie_default_3.4.113.7z
 117     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Orangepizero_Ubuntu_xenial_default_3.4.113.7z
 118     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino2_Debian_jessie_default_3.4.113.7z
 119     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino2_Debian_jessie_next_4.9.7.7z
 120     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino2_Ubuntu_xenial_default_3.4.113_desktop.7z
 121     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino2_Ubuntu_xenial_next_4.9.7_desktop.7z
 122     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino3_Debian_jessie_default_3.4.113.7z
 123     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino3_Debian_jessie_next_4.9.7.7z
 124     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino3nano_Debian_jessie_default_3.4.113.7z
 125     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino3nano_Debian_jessie_next_4.9.7.7z
 126     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino3nano_Ubuntu_xenial_default_3.4.113_desktop.7z
 127     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino3nano_Ubuntu_xenial_next_4.9.7_desktop.7z
 128     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino3_Ubuntu_xenial_default_3.4.113_desktop.7z
 129     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pcduino3_Ubuntu_xenial_next_4.9.7_desktop.7z
 130     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pine64_Debian_jessie_default_3.10.104.7z
 131     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pine64_Ubuntu_xenial_default_3.10.104.7z
 132     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Pine64_Ubuntu_xenial_default_3.10.104_desktop.7z
 133     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Udoo_Debian_jessie_default_3.14.79.7z
 134     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Udoo_Debian_jessie_next_4.4.46.7z
 135     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Udoo-neo_Ubuntu_xenial_default_3.14.79.7z
 136     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Udoo_Ubuntu_xenial_default_3.14.79_desktop.7z
 137     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.25_Udoo_Ubuntu_xenial_next_4.4.46_desktop.7z
 138     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.26_Guitar_Debian_jessie_default_3.10.105.7z
 139     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.26_Guitar_Ubuntu_xenial_default_3.10.105_desktop.7z
 140     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.26_Roseapple_Debian_jessie_default_3.10.105.7z
 141     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.26_Roseapple_Ubuntu_xenial_default_3.10.105_desktop.7z
 142     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Bananapim2_Debian_jessie_next_4.10.14.7z
 143     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Bananapim2_Ubuntu_xenial_next_4.10.14_desktop.7z
 144     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Miqi_Ubuntu_xenial_default_4.4.66.7z
 145     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Miqi_Ubuntu_xenial_default_4.4.66_desktop.7z
 146     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Miqi_Ubuntu_xenial_next_4.11.0.7z
 147     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Miqi_Ubuntu_xenial_next_4.11.0_desktop.7z
 148     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Odroidxu4_Debian_jessie_default_3.10.105.7z
 149     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Odroidxu4_Debian_jessie_next_4.9.13.7z
 150     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Odroidxu4_Ubuntu_xenial_default_3.10.105.7z
 151     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Odroidxu4_Ubuntu_xenial_default_3.10.105_desktop.7z
 152     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Odroidxu4_Ubuntu_xenial_next_4.9.13.7z
 153     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Odroidxu4_Ubuntu_xenial_next_4.9.13_desktop.7z
 154     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Orangepizeroplus2-h3_Ubuntu_xenial_default_3.4.113.7z
 155     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Orangepizeroplus2-h3_Ubuntu_xenial_default_3.4.113_desktop.7z
 156     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Pine64so_Ubuntu_xenial_default_3.10.105.7z
 157     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Tinkerboard_Ubuntu_xenial_default_4.4.66.7z
 158     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Tinkerboard_Ubuntu_xenial_default_4.4.66_desktop.7z
 159     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Tinkerboard_Ubuntu_xenial_next_4.11.0.7z
 160     0%       None  Unknown      0.0     0.0   None  Queued       Armbian_5.27_Tinkerboard_Ubuntu_xenial_next_4.11.0_desktop.7z
Sum:          40.62 MB               0.0  1085.0
```

  
</details>

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

