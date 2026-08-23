---
title: "Webmin"
description: "Install and run Webmin on Armbian — Webmin web-based management tool. Runs on ARM64 and x86 single-board computers."
image: /images/WBM001.png
category: "Management"
comments: true
---
# Webmin


<!--- section image START from tools/include/images/WBM001.png --->
![Webmin](/images/WBM001.png)
<!--- section image STOP from tools/include/images/WBM001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://forum.armbian.com/)


<!--- header START from tools/include/markdown/WBM001-header.md --->
Webmin is a web-based system administration tool for Unix-like servers. It provides an easy-to-use browser interface to manage users, configure services, edit files, monitor system performance, and control almost every aspect of your server — without needing to touch the command line.

<!--- header STOP from tools/include/markdown/WBM001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Management → Webmin**

~~~ custombash title="Webmin web-based management tool"
armbian-config --cmd WBM001
~~~


<!--- footer START from tools/include/markdown/WBM001-footer.md --->
=== "Access to the web interface"

    - Username/Password: your system login credentials

<!--- footer STOP from tools/include/markdown/WBM001-footer.md --->


---

_Part of Armbian's [Remote File & Management tools](/User-Guide_Armbian-Software/Management/) software._
