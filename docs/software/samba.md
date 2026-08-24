---
title: "Samba"
seo_title: "Install Samba on Armbian"
description: "Install and run Samba on Armbian — SAMBA Remote File share. Runs on ARM64 and x86 single-board computers."
image: /images/SMB001.png
category: "Management"
comments: true
---
# Samba


<!--- section image START from tools/include/images/SMB001.png --->
![Samba](/images/SMB001.png){ .app-logo }
<!--- section image STOP from tools/include/images/SMB001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://forum.armbian.com/)


<!--- header START from tools/include/markdown/SMB001-header.md --->
Samba is an open-source software suite that enables seamless file and printer sharing between Linux/Unix servers and Windows clients. It allows a Linux machine to act as a domain controller, file server, or print server within a Windows network environment, supporting cross-platform interoperability.

<!--- header STOP from tools/include/markdown/SMB001-header.md --->


Install from **[armbian-config](/config/) → Software → Management → Samba**

~~~ custombash title="SAMBA Remote File share"
armbian-config --cmd SMB001
~~~


---

_Part of Armbian's [Remote File & Management tools](/User-Guide_Armbian-Software/Management/) software._
