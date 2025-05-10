---
comments: true
---

# Music servers and streamers

## Navidrome


Navidrome music server and streamer compatible with Subsonic/Airsonic


<!--- section image START from tools/include/images/NAV001.png --->
[![Navidrome](/images/NAV001.png)](#)
<!--- section image STOP from tools/include/images/NAV001.png --->


<!--- header START from tools/include/markdown/NAV001-header.md --->
Navidrome is a modern, lightweight, and self-hosted music server and streamer. It's designed to be compatible with the Subsonic and Airsonic APIs, making it a drop-in replacement for users of those systems. With Navidrome, you can stream your personal music collection from anywhere using any compatible Subsonic client (mobile or desktop). It supports multi-user access, real-time updates, album artwork, and is built with performance and simplicity in mind—perfect for organizing and accessing large music libraries.

<!--- header STOP from tools/include/markdown/NAV001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/NAV001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/NAV001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/pynavidrome/navidrome/wiki)  

~~~ custombash
armbian-config --cmd NAV001
~~~


~~~ bash title="Navidrome remove:"
armbian-config --cmd NAV002
~~~


~~~ bash title="Navidrome purge with data folder:"
armbian-config --cmd NAV003
~~~



