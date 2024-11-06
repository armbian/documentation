# Home Automation


***

## Install openHAB

<!--- section image START from tools/include/images/HA001.png --->
[![Install openHAB](/images/HA001.png)](#)
<!--- section image STOP from tools/include/images/HA001.png --->

**Command:** 
~~~
armbian-config --cmd HA001
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/HA001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8444**:

    - URL: `https://<your.IP>:8444`
    - Username/Password: Are set at first web interface login

=== "Directories"

    - Install directory: `/usr/share/openhab`
    - Site configuration directory: `/etc/openhab`
    - Config file: `/etc/default/openhab`
    - Data directory: `/var/lib/openhab`

    See also [openHAB file locations](https://www.openhab.org/docs/installation/linux.html#file-locations).

=== "View logs"

    ```sh
    journalctl -u openhab
    ```

<!--- footer STOP from tools/include/markdown/HA001-footer.md --->



***

## Remove openHAB
**Command:** 
~~~
armbian-config --cmd HA002
~~~

**Author:** @armbian

**Status:** Stable



***

