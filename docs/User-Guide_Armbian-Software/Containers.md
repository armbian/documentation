---
comments: true
---

# Docker containerization and KVM virtual machines

## Docker minimal

**Author:** @schwar3kat

**Status:** Stable


<!--- section image START from tools/include/images/CON001.webp --->
[![Docker minimal](/images/CON001.webp)](#)
<!--- section image STOP from tools/include/images/CON001.webp --->


~~~ custombash title="Docker minimal:"
armbian-config --cmd CON001
~~~


<!--- footer START from tools/include/markdown/CON001-footer.md --->
What is Docker? Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management.

<!--- footer STOP from tools/include/markdown/CON001-footer.md --->


~~~ custombash title="Docker engine:"
armbian-config --cmd CON002
~~~


~~~ custombash title="Docker remove:"
armbian-config --cmd CON003
~~~


~~~ custombash title="Docker purge with all images, containers, and volumes:"
armbian-config --cmd CON004
~~~


~~~ custombash title="Portainer container management platform:"
armbian-config --cmd CON005
~~~


<!--- footer START from tools/include/markdown/CON005-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9002**:

    - URL = `http://<your.IP>:9002`

<!--- footer STOP from tools/include/markdown/CON005-footer.md --->


~~~ custombash title="Portainer remove:"
armbian-config --cmd CON006
~~~


~~~ custombash title="Portainer purge with with data folder:"
armbian-config --cmd CON007
~~~
