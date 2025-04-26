---
comments: true
---

# Fixed and wireless network settings

**Author:** @igorpecovnik


<!--- section image START from tools/include/images/NET001.png --->
[![Basic Network Setup](/images/NET001.png)](#)
<!--- section image STOP from tools/include/images/NET001.png --->


~~~ bash title="Basic Network Setup:"
armbian-config --cmd NET001
~~~


~~~ bash title="Remove Fallback DHCP Configuration:"
armbian-config --cmd NET002
~~~


~~~ bash title="Remove Fallback DHCP Configuration:"
armbian-config --cmd NET002
~~~

**Author:** @igorpecovnik


<!--- section image START from tools/include/images/VNS001.png --->
[![View Network Settings](/images/VNS001.png)](#)
<!--- section image STOP from tools/include/images/VNS001.png --->


~~~ bash title="View Network Settings:"
armbian-config --cmd VNS001
~~~

**Author:** @igorpecovnik


~~~ bash title="Add / change interface:"
armbian-config --cmd NEA001
~~~


~~~ bash title="Revert to Armbian defaults:"
armbian-config --cmd NEA002
~~~


~~~ bash title="Show configuration:"
armbian-config --cmd NEA003
~~~


~~~ bash title="Show active status:"
armbian-config --cmd NEA004
~~~

**Author:** @armbian


<!--- section image START from tools/include/images/WG001.png --->
[![WireGuard VPN client / server](/images/WG001.png)](#)
<!--- section image STOP from tools/include/images/WG001.png --->


<!--- header START from tools/include/markdown/WG001-header.md --->
WireGuard is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. Regarded as the most secure, easiest to use, and simplest VPN solution in the industry.
<!--- header STOP from tools/include/markdown/WG001-header.md --->


~~~ bash title="WireGuard VPN client / server:"
armbian-config --cmd WG001
~~~


~~~ bash title="WireGuard remove:"
armbian-config --cmd WG002
~~~


~~~ bash title="WireGuard clients QR codes:"
armbian-config --cmd WG003
~~~


~~~ bash title="WireGuard purge with data folder:"
armbian-config --cmd WG004
~~~
