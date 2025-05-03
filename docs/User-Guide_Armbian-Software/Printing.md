---
comments: true
---

# Tools for printing and 3D printing

## OctoPrint


OctoPrint web-based 3D printers management tool


<!--- section image START from tools/include/images/OCT001.png --->
[![OctoPrint](/images/OCT001.png)](#)
<!--- section image STOP from tools/include/images/OCT001.png --->


<!--- header START from tools/include/markdown/OCT001-header.md --->
OctoPrint is an open source 3D printer controller application, which provides a web interface for the connected printers. It displays printers status and key parameters and allows user to schedule prints and remotely control the printer.
<!--- header STOP from tools/include/markdown/OCT001-header.md --->

__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://transmissionbt.com/)  

~~~ custombash
armbian-config --cmd OCT001
~~~


<!--- footer START from tools/include/markdown/OCT001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **7981**:

    - URL: `https://<your.IP>:7981`

=== "Directories"

    - Install directory: `/armbian/octoprint`

=== "View logs"

    ```sh
    docker logs -f octoprint
    ```

<!--- footer STOP from tools/include/markdown/OCT001-footer.md --->


~~~ bash title="OctoPrint remove:"
armbian-config --cmd OCT002
~~~


~~~ bash title="OctoPrint purge with data folder:"
armbian-config --cmd OCT003
~~~



