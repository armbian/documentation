---
comments: true
---

# Docker containerization and KVM virtual machines

## Docker


Docker minimal


<!--- section image START from tools/include/images/CON001.png --->
[![Docker](/images/CON001.png)](#)
<!--- section image STOP from tools/include/images/CON001.png --->

**Author:** @schwar3kat

**Status:** Stable


~~~ custombash
armbian-config --cmd CON001
~~~


<!--- footer START from tools/include/markdown/CON001-footer.md --->
What is Docker? Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management.

<!--- footer STOP from tools/include/markdown/CON001-footer.md --->


~~~ bash title="Docker engine:"
armbian-config --cmd CON002
~~~


~~~ bash title="Docker remove:"
armbian-config --cmd CON003
~~~


~~~ bash title="Docker purge with all images, containers, and volumes:"
armbian-config --cmd CON004
~~~





## Portainer


Portainer container management platform


<!--- section image START from tools/include/images/POR001.png --->
[![Portainer](/images/POR001.png)](#)
<!--- section image STOP from tools/include/images/POR001.png --->


<!--- header START from tools/include/markdown/POR001-header.md --->
Portainer simplifies your Docker container management via Portainer web interface. It enables faster deploy of the applications and it gives real time visibility.

<!--- header STOP from tools/include/markdown/POR001-header.md --->

**Author:** @armbian

**Status:** Stable


~~~ custombash
armbian-config --cmd POR001
~~~


<!--- footer START from tools/include/markdown/POR001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9002**:

    - URL = `http://<your.IP>:9002`

<!--- footer STOP from tools/include/markdown/POR001-footer.md --->


~~~ bash title="Portainer remove:"
armbian-config --cmd POR002
~~~


~~~ bash title="Portainer purge with with data folder:"
armbian-config --cmd POR003
~~~



