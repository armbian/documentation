# Media servers, organizers and editors


***

## Emby organizes video, music, live TV, and photos

<!--- section image START from tools/include/images/MED003.png --->
[![Emby organizes video, music, live TV, and photos](/images/MED003.png)](#)
<!--- section image STOP from tools/include/images/MED003.png --->


<!--- header START from tools/include/markdown/MED003-header.md --->
Emby organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

<!--- header STOP from tools/include/markdown/MED003-header.md --->

This operation will install Emby server.

**Command:** 
~~~
armbian-config --cmd MED003
~~~

**Author:** @schwar3kat

**Status:** Stable


<!--- footer START from tools/include/markdown/MED003-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8096**:

    - URL: `https://<your.IP>:8096`

=== "Directories"

    - Install directory: `/armbian/emby`
    - Site configuration directory: `/armbian/emby/config`
    - Data directory: `/armbian/emby/tvshows` `/armbian/emby/movies`

=== "View logs"

    ```sh
    docker logs -f emby
    ```

<!--- footer STOP from tools/include/markdown/MED003-footer.md --->



***

## Emby server remove
This operation will remove Emby server

**Command:** 
~~~
armbian-config --cmd MED004
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Emby server purge with data folder
**Command:** 
~~~
armbian-config --cmd MED005
~~~

**Author:** @schwar3kat

**Status:** Stable



***

## Stirling PDF tools for viewing and editing PDF files

<!--- section image START from tools/include/images/MED010.png --->
[![Stirling PDF tools for viewing and editing PDF files](/images/MED010.png)](#)
<!--- section image STOP from tools/include/images/MED010.png --->


<!--- header START from tools/include/markdown/MED010-header.md --->
Stirling-PDF is a robust, locally hosted web-based PDF manipulation tool using Docker. It enables you to carry out various operations on PDF files, including splitting, merging, converting, reorganizing, adding images, rotating, compressing, and more. This locally hosted web application has evolved to encompass a comprehensive set of features, addressing all your PDF requirements.

<!--- header STOP from tools/include/markdown/MED010-header.md --->

This operation will install Stirling-PDF tools.

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

## Stirling PDF remove
This operation will remove Stirling-PDF tools.

**Command:** 
~~~
armbian-config --cmd MED011
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Stirling PDF purge with data folder
This operation will purge Stirling-PDF tools with data folder.

**Command:** 
~~~
armbian-config --cmd MED012
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Syncthing continuous file synchronization

<!--- section image START from tools/include/images/MED015.png --->
[![Syncthing continuous file synchronization](/images/MED015.png)](#)
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

## Syncthing remove
**Command:** 
~~~
armbian-config --cmd MED016
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Syncthing purge with data folder
**Command:** 
~~~
armbian-config --cmd MED017
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Nextcloud content collaboration platform

<!--- section image START from tools/include/images/MED020.png --->
[![Nextcloud content collaboration platform](/images/MED020.png)](#)
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

## Nextcloud remove
**Command:** 
~~~
armbian-config --cmd MED021
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Nextcloud purge with data folder
**Command:** 
~~~
armbian-config --cmd MED022
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Owncloud share files and folders, easy and secure
**Command:** 
~~~
armbian-config --cmd MED025
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Owncloud remove
**Command:** 
~~~
armbian-config --cmd MED026
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Owncloud purge with data folder

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

## Jellyfin Media System

<!--- section image START from tools/include/images/MED030.png --->
[![Jellyfin Media System](/images/MED030.png)](#)
<!--- section image STOP from tools/include/images/MED030.png --->


<!--- header START from tools/include/markdown/MED030-header.md --->
Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it.

<!--- header STOP from tools/include/markdown/MED030-header.md --->

**Command:** 
~~~
armbian-config --cmd MED030
~~~

**Author:** @igorpecovnik

**Status:** Preview


<!--- footer START from tools/include/markdown/MED030-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8096**:

    - URL: `http://<your.IP>:8096`
    - Username and password are set at first login

=== "Directories"

    - Install directory: `/armbian/jellyfin`
    - Site configuration directory: `/armbian/jellyfin/config`
    - TV shows directory: `/armbian/jellyfin/tvseries`
    - Movies directory: `/armbian/jellyfin/movies`

=== "View logs"

    ```sh
    docker logs -f jellyfin
    ```

<!--- footer STOP from tools/include/markdown/MED030-footer.md --->



***

## Jellyfin remove
**Command:** 
~~~
armbian-config --cmd MED031
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

## Jellyfin purge with data folder
**Command:** 
~~~
armbian-config --cmd MED032
~~~

**Author:** @igorpecovnik

**Status:** Preview



***

