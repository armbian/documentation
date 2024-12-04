# Media Servers and Editors


***

## Install Plex Media server
This operation will install Plex Media server.

**Command:** 
~~~
armbian-config --cmd MED001
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Remove Plex Media server
This operation will purge Plex Media server.

**Command:** 
~~~
armbian-config --cmd MED002
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Install Emby server
This operation will install Emby server.

**Command:** 
~~~
armbian-config --cmd MED003
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Remove Emby server
This operation will purge Emby server.

**Command:** 
~~~
armbian-config --cmd MED004
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Stirling-PDF Install

<!--- section image START from tools/include/images/MED010.png --->
[![Stirling-PDF Install](/images/MED010.png)](#)
<!--- section image STOP from tools/include/images/MED010.png --->


<!--- header START from tools/include/markdown/MED010-header.md --->
Stirling-PDF is a robust, locally hosted web-based PDF manipulation tool using Docker. It enables you to carry out various operations on PDF files, including splitting, merging, converting, reorganizing, adding images, rotating, compressing, and more. This locally hosted web application has evolved to encompass a comprehensive set of features, addressing all your PDF requirements.

<!--- header STOP from tools/include/markdown/MED010-header.md --->

**Command:** 
~~~
armbian-config --cmd MED010
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/MED010-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8077**:

    - URL: `https://<your.IP>:8077`

=== "Directories"

    - Install directory: `/armbian/stirling`

=== "View logs"

    ```sh
    docker logs -f stirling-pdf
    ```

<!--- footer STOP from tools/include/markdown/MED010-footer.md --->



***

## Stirling-PDF Remove
**Command:** 
~~~
armbian-config --cmd MED011
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Stirling-PDF Purge data folder
**Command:** 
~~~
armbian-config --cmd MED012
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Syncthing Install

<!--- section image START from tools/include/images/MED015.png --->
[![Syncthing Install](/images/MED015.png)](#)
<!--- section image STOP from tools/include/images/MED015.png --->


<!--- header START from tools/include/markdown/MED015-header.md --->
Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

<!--- header STOP from tools/include/markdown/MED015-header.md --->

**Command:** 
~~~
armbian-config --cmd MED015
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/MED015-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8884**:

    - URL: `https://<your.IP>:8884`
    - Username/Password: There is none, but it is highly suggested setting a password for this container. To do this go to Actions -> Settings -> set user/password for the webUI.

=== "Directories"

    - Install directory: `/armbian/syncthing`
    - Site configuration directory: `/armbian/syncthing/config`
    - Data directory: `/armbian/syncthing/data1` `/armbian/syncthing/data2`

=== "View logs"

    ```sh
    docker logs -f syncthing
    ```

<!--- footer STOP from tools/include/markdown/MED015-footer.md --->



***

## Syncthing Remove
**Command:** 
~~~
armbian-config --cmd MED016
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Syncthing Purge data folder
**Command:** 
~~~
armbian-config --cmd MED017
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Nextcloud Install

<!--- section image START from tools/include/images/MED020.png --->
[![Nextcloud Install](/images/MED020.png)](#)
<!--- section image STOP from tools/include/images/MED020.png --->


<!--- header START from tools/include/markdown/MED020-header.md --->
Nextcloud gives you access to all your files wherever you are.
<br>
Where are your photos and documents? With Nextcloud you pick a server of your choice, at home, in a data center or at a provider. And that is where your files will be. Nextcloud runs on that server, protecting your data and giving you access from your desktop or mobile devices. Through Nextcloud you also access, sync and share your existing data on that FTP drive at the office, a Dropbox or a NAS you have at home.

<!--- header STOP from tools/include/markdown/MED020-header.md --->

**Command:** 
~~~
armbian-config --cmd MED020
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/MED020-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **443**:

    - URL: `https://<your.IP>:443`
    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/nextcloud`
    - Site configuration directory: `/armbian/nextcloud/config`
    - Data directory: `/armbian/nextcloud/data`

=== "View logs"

    ```sh
    docker logs -f nextcloud
    ```

<!--- footer STOP from tools/include/markdown/MED020-footer.md --->



***

## Nextcloud Remove
**Command:** 
~~~
armbian-config --cmd MED021
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Nextcloud Purge data folder
**Command:** 
~~~
armbian-config --cmd MED022
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Owncloud Install
**Command:** 
~~~
armbian-config --cmd MED025
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Owncloud Remove
**Command:** 
~~~
armbian-config --cmd MED026
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Owncloud Purge data folder

<!--- header START from tools/include/markdown/MED027-header.md --->
ownCloud is a free and open-source software project for content collaboration and sharing and syncing of files in distributed and federated enterprise scenarios.

<!--- header STOP from tools/include/markdown/MED027-header.md --->

**Command:** 
~~~
armbian-config --cmd MED027
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/MED027-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **7787**:

    - URL: `http://<your.IP>:7787`
    - Username/Password: admin / admin

=== "Directories"

    - Install directory: `/armbian/owncloud`
    - Site configuration directory: `/armbian/owncloud/config`
    - Data directory: `/armbian/owncloud/data`

=== "View logs"

    ```sh
    docker logs -f owncloud
    ```

<!--- footer STOP from tools/include/markdown/MED027-footer.md --->



***

