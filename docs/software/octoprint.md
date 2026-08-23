---
title: "OctoPrint"
description: "Install and run OctoPrint on Armbian — OctoPrint web-based 3D printers management tool. Runs on ARM64 and x86 single-board computers."
image: /images/OCT001.png
category: "Printing"
comments: true
---
# OctoPrint


<!--- section image START from tools/include/images/OCT001.png --->
![OctoPrint](/images/OCT001.png)
<!--- section image STOP from tools/include/images/OCT001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://transmissionbt.com/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:7981`


<!--- header START from tools/include/markdown/OCT001-header.md --->
OctoPrint is an open source 3D printer controller application, which provides a web interface for the connected printers. It displays printers status and key parameters and allows user to schedule prints and remotely control the printer.
<!--- header STOP from tools/include/markdown/OCT001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Printing → OctoPrint**

~~~ custombash title="CLI install"
armbian-config --cmd OCT001
~~~


<!--- footer START from tools/include/markdown/OCT001-footer.md --->
=== "Directories"

    - Install directory: `/armbian/octoprint`

=== "View logs"

    ```sh
    docker logs -f octoprint
    ```

<!--- footer STOP from tools/include/markdown/OCT001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_octoprint install` |
| OctoPrint remove | `armbian-config --api module_octoprint remove` |
| OctoPrint purge with data folder | `armbian-config --api module_octoprint purge` |
| Status | `armbian-config --api module_octoprint status` |
| Help | `armbian-config --api module_octoprint help` |

---

_Part of Armbian's [Tools for printing and 3D printing](/User-Guide_Armbian-Software/Printing/) software._
