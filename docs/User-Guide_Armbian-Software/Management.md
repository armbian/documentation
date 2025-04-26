---
comments: true
---

# Remote File & Management tools

## Cockpit web-based management tool

**Author:** @Tearran

**Status:** Stable


<!--- section image START from tools/include/images/MAN001.png --->
[![Cockpit web-based management tool](/images/MAN001.png)](#)
<!--- section image STOP from tools/include/images/MAN001.png --->


~~~ custombash title="Cockpit web-based management tool:"
armbian-config --cmd MAN001
~~~


<!--- footer START from tools/include/markdown/MAN001-footer.md --->
Introducing Cockpit
Cockpit is a web-based graphical interface for servers, intended for everyone, especially those who are:

- new to Linux
(including Windows admins)
- familiar with Linux
and want an easy, graphical way to administer servers
- expert admins
who mainly use other tools but want an overview on individual systems

Thanks to Cockpit intentionally using system APIs and commands, a whole team of admins can manage a system in the way they prefer, including the command line and utilities right alongside Cockpit.
<!--- footer STOP from tools/include/markdown/MAN001-footer.md --->


~~~ custombash title="SAMBA Remote File share:"
armbian-config --cmd MAN002
~~~


~~~ custombash title="Webmin web-based management tool:"
armbian-config --cmd MAN005
~~~


<!--- footer START from tools/include/markdown/MAN005-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **10000**:

    - URL: `https://<your.IP>:10000`
    - Username/Password: your system login credentials


<!--- footer STOP from tools/include/markdown/MAN005-footer.md --->
