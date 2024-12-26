# Docker containerization and KVM virtual machines


***

## Docker minimal

<!--- section image START from tools/include/images/CON001.webp --->
[![Docker minimal](/images/CON001.webp)](#)
<!--- section image STOP from tools/include/images/CON001.webp --->

This operation will install Docker Minimal.

**Command:** 
~~~
armbian-config --cmd CON001
~~~

**Author:** @schwar3kat

**Status:** Stable


<!--- footer START from tools/include/markdown/CON001-footer.md --->
What is Docker? Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management.

<!--- footer STOP from tools/include/markdown/CON001-footer.md --->



***

## Docker engine
This operation will install Docker Engine.

**Command:** 
~~~
armbian-config --cmd CON002
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Docker remove
This operation will purge Docker.

**Command:** 
~~~
armbian-config --cmd CON003
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Docker purge with all images, containers, and volumes
This operation will delete all Docker images, containers, and volumes.

**Command:** 
~~~
armbian-config --cmd CON004
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Portainer container management platform

<!--- section image START from tools/include/images/CON005.webp --->
[![Portainer container management platform](/images/CON005.webp)](#)
<!--- section image STOP from tools/include/images/CON005.webp --->


<!--- header START from tools/include/markdown/CON005-header.md --->
Portainer simplifies your Docker container management via Portainer web interface. It enables faster deploy of the applications and it gives real time visibility.

<!--- header STOP from tools/include/markdown/CON005-header.md --->

**Command:** 
~~~
armbian-config --cmd CON005
~~~

**Author:** @armbian

**Status:** Stable


<!--- footer START from tools/include/markdown/CON005-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **9002**:

    - URL = `http://<your.IP>:9002`

<!--- footer STOP from tools/include/markdown/CON005-footer.md --->



***

## Portainer remove
**Command:** 
~~~
armbian-config --cmd CON006
~~~

**Author:** @armbian

**Status:** Stable



***

## Portainer purge with with data folder
**Command:** 
~~~
armbian-config --cmd CON007
~~~

**Author:** @armbian

**Status:** Stable



***

