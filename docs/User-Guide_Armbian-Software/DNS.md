# DNS blockers


***

## Install Pi-hole DNS ad blocker

<!--- section image START from tools/include/images/DNS001.png --->
[![Install Pi-hole DNS ad blocker](/images/DNS001.png)](#)
<!--- section image STOP from tools/include/images/DNS001.png --->


<!--- header START from tools/include/markdown/DNS001-header.md --->
Pi-hole is a DNS sinkhole with web interface that will block ads for any device on your network.


<!--- header STOP from tools/include/markdown/DNS001-header.md --->

**Command:** 
~~~
armbian-config --cmd DNS001
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/DNS001-footer.md --->
=== "Access the web interface"

    The web interface of Pi-hole can be accessed via:

    - URL = `http://<your.IP>/admin`
    - Password = 'Set / adjust from armbian-config'

=== "Documentation"

<https://docs.pi-hole.net/>

<!--- footer STOP from tools/include/markdown/DNS001-footer.md --->



***

## Set Pi-hole web admin password
**Command:** 
~~~
armbian-config --cmd DNS002
~~~

**Author:** @armbian

**Status:** Stable



***

## Remove Pi-hole DNS ad blocker
**Command:** 
~~~
armbian-config --cmd DNS003
~~~

**Author:** @armbian

**Status:** Stable



***

