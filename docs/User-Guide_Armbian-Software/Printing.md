# Tools for printing and 3D printing


***

## OctoPrint web-based 3D printers management tool

<!--- section image START from tools/include/images/OCT001.png --->
[![OctoPrint web-based 3D printers management tool](/images/OCT001.png)](#)
<!--- section image STOP from tools/include/images/OCT001.png --->


<!--- header START from tools/include/markdown/OCT001-header.md --->
OctoPrint is an open source 3D printer controller application, which provides a web interface for the connected printers. It displays printers status and key parameters and allows user to schedule prints and remotely control the printer.
<!--- header STOP from tools/include/markdown/OCT001-header.md --->

This operation will install OctoPrint

**Command:** 
~~~
armbian-config --cmd OCT001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## OctoPrint remove
This operation will remove OctoPrint

**Command:** 
~~~
armbian-config --cmd OCT002
~~~

**Author:** @armbian

**Status:** Stable



***

## OctoPrint purge with data folder
This operation will purge OctoPrint with data folder

**Command:** 
~~~
armbian-config --cmd OCT003
~~~

**Author:** @armbian

**Status:** Stable



***

