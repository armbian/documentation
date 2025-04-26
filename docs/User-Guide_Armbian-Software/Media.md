---
comments: true
---

# Media servers, organizers and editors

## Emby organizes video, music, live TV, and photos

**Author:** @schwar3kat

**Status:** Stable


<!--- section image START from tools/include/images/MED003.png --->
[![Emby organizes video, music, live TV, and photos](/images/MED003.png)](#)
<!--- section image STOP from tools/include/images/MED003.png --->


<!--- header START from tools/include/markdown/MED003-header.md --->
Emby organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

<!--- header STOP from tools/include/markdown/MED003-header.md --->


~~~ custombash title="Emby organizes video, music, live TV, and photos:"
armbian-config --cmd MED003
~~~


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


~~~ custombash title="Emby server remove:"
armbian-config --cmd MED004
~~~


~~~ custombash title="Emby server purge with data folder:"
armbian-config --cmd MED005
~~~


~~~ custombash title="Stirling PDF tools for viewing and editing PDF files:"
armbian-config --cmd MED010
~~~


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


~~~ custombash title="Stirling PDF remove:"
armbian-config --cmd MED011
~~~


~~~ custombash title="Stirling PDF purge with data folder:"
armbian-config --cmd MED012
~~~


~~~ custombash title="Syncthing continuous file synchronization:"
armbian-config --cmd MED015
~~~


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


~~~ custombash title="Syncthing remove:"
armbian-config --cmd MED016
~~~


~~~ custombash title="Syncthing purge with data folder:"
armbian-config --cmd MED017
~~~


~~~ custombash title="Nextcloud content collaboration platform:"
armbian-config --cmd MED020
~~~


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


~~~ custombash title="Nextcloud remove:"
armbian-config --cmd MED021
~~~


~~~ custombash title="Nextcloud purge with data folder:"
armbian-config --cmd MED022
~~~


~~~ custombash title="Owncloud share files and folders, easy and secure:"
armbian-config --cmd MED025
~~~


~~~ custombash title="Owncloud remove:"
armbian-config --cmd MED026
~~~


~~~ custombash title="Owncloud purge with data folder:"
armbian-config --cmd MED027
~~~


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


~~~ custombash title="Jellyfin Media System:"
armbian-config --cmd MED030
~~~


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


~~~ custombash title="Jellyfin remove:"
armbian-config --cmd MED031
~~~


~~~ custombash title="Jellyfin purge with data folder:"
armbian-config --cmd MED032
~~~


~~~ custombash title="Hastebin Paste Server:"
armbian-config --cmd MED033
~~~


~~~ custombash title="Hastebin remove:"
armbian-config --cmd MED034
~~~


~~~ custombash title="Hastebin purge with data folder:"
armbian-config --cmd MED035
~~~
