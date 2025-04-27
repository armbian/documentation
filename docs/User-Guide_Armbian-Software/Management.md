---
comments: true
---

# Remote File & Management tools

## Cockpit


Cockpit web-based management tool


<!--- section image START from tools/include/images/CPT001.png --->
[![Cockpit](/images/CPT001.png)](#)
<!--- section image STOP from tools/include/images/CPT001.png --->


<!--- header START from tools/include/markdown/CPT001-header.md --->
Introducing Cockpit
Cockpit is a web-based graphical interface for servers, intended for everyone, especially those who are:

- new to Linux
(including Windows admins)
- familiar with Linux
and want an easy, graphical way to administer servers
- expert admins
who mainly use other tools but want an overview on individual systems

Thanks to Cockpit intentionally using system APIs and commands, a whole team of admins can manage a system in the way they prefer, including the command line and utilities right alongside Cockpit.
<!--- header STOP from tools/include/markdown/CPT001-header.md --->

**Author:** @Tearran

**Status:** Stable


~~~ custombash
armbian-config --cmd CPT001
~~~


<!--- footer START from tools/include/markdown/CPT001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9090**:

    - URL: `https://<your.IP>:9090`
    - Username/Password: your system login credentials

=== "Video instructions"


    <iframe width="1200" height="676" src="https://www.youtube.com/embed/L9fMWCRcqIE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!--- footer STOP from tools/include/markdown/CPT001-footer.md --->


## Samba


SAMBA Remote File share


<!--- section image START from tools/include/images/SMB001.png --->
[![Samba](/images/SMB001.png)](#)
<!--- section image STOP from tools/include/images/SMB001.png --->


<!--- header START from tools/include/markdown/SMB001-header.md --->
Samba is an open-source software suite that enables seamless file and printer sharing between Linux/Unix servers and Windows clients. It allows a Linux machine to act as a domain controller, file server, or print server within a Windows network environment, supporting cross-platform interoperability.

<!--- header STOP from tools/include/markdown/SMB001-header.md --->

**Author:** @Tearran

**Status:** Stable


~~~ custombash
armbian-config --cmd SMB001
~~~


## Webmin


Webmin web-based management tool


<!--- section image START from tools/include/images/WBM001.png --->
[![Webmin](/images/WBM001.png)](#)
<!--- section image STOP from tools/include/images/WBM001.png --->


<!--- header START from tools/include/markdown/WBM001-header.md --->
Webmin is a web-based system administration tool for Unix-like servers. It provides an easy-to-use browser interface to manage users, configure services, edit files, monitor system performance, and control almost every aspect of your server — without needing to touch the command line.

<!--- header STOP from tools/include/markdown/WBM001-header.md --->

**Author:** @Tearran

**Status:** Stable


~~~ custombash
armbian-config --cmd WBM001
~~~


<!--- footer START from tools/include/markdown/WBM001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **10000**:

    - URL: `https://<your.IP>:10000`
    - Username/Password: your system login credentials


<!--- footer STOP from tools/include/markdown/WBM001-footer.md --->

