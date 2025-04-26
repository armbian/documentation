---
comments: true
---

# Tools for printing and 3D printing

## OctoPrint web-based 3D printers management tool

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/OCT001.png --->
[![OctoPrint web-based 3D printers management tool](/images/OCT001.png)](#)
<!--- section image STOP from tools/include/images/OCT001.png --->


<!--- header START from tools/include/markdown/OCT001-header.md --->
OctoPrint is an open source 3D printer controller application, which provides a web interface for the connected printers. It displays printers status and key parameters and allows user to schedule prints and remotely control the printer.
<!--- header STOP from tools/include/markdown/OCT001-header.md --->


~~~ bash title="OctoPrint web-based 3D printers management tool:"
armbian-config --cmd OCT001
~~~

## OctoPrint remove


~~~ bash title="OctoPrint remove:"
armbian-config --cmd OCT002
~~~

## OctoPrint purge with data folder


~~~ bash title="OctoPrint purge with data folder:"
armbian-config --cmd OCT003
~~~
