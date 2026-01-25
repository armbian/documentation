---
comments: true
---

# Docker containerization and KVM virtual machines

## Docker


<!--- section image START from tools/include/images/CON001.png --->
[![Docker](/images/CON001.png)](#)
<!--- section image STOP from tools/include/images/CON001.png --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/CON001-footer.md) [header](https://github.com/armbian/configng/new/main/tools/include/markdown/CON001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://docs.docker.com)  

~~~ custombash
armbian-config --cmd CON001
~~~


<!--- footer START from tools/include/markdown/CON001-footer.md --->
What is Docker? Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management.

<!--- footer STOP from tools/include/markdown/CON001-footer.md --->


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

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/POR001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/POR001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span>  
__Maintainer:__ @schwar3kat  
__Documentation:__ [Link](https://docs.portainer.io/)  

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



