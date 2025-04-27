---
comments: true
---

# Media servers, organizers and editors

## Emby


Emby organizes video, music, live TV, and photos


<!--- section image START from tools/include/images/EMB001.png --->
[![Emby](/images/EMB001.png)](#)
<!--- section image STOP from tools/include/images/EMB001.png --->


<!--- header START from tools/include/markdown/EMB001-header.md --->
Emby organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

<!--- header STOP from tools/include/markdown/EMB001-header.md --->

**Author:** @schwar3kat

**Status:** Stable


~~~ custombash
armbian-config --cmd EMB001
~~~


<!--- footer START from tools/include/markdown/EMB001-footer.md --->
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

<!--- footer STOP from tools/include/markdown/EMB001-footer.md --->


~~~ bash title="Emby server remove:"
armbian-config --cmd EMB002
~~~


~~~ bash title="Emby server purge with data folder:"
armbian-config --cmd EMB003
~~~




## Stirling


Stirling PDF tools for viewing and editing PDF files


<!--- section image START from tools/include/images/STR001.png --->
[![Stirling](/images/STR001.png)](#)
<!--- section image STOP from tools/include/images/STR001.png --->


<!--- header START from tools/include/markdown/STR001-header.md --->
Stirling-PDF is a robust, locally hosted web-based PDF manipulation tool using Docker. It enables you to carry out various operations on PDF files, including splitting, merging, converting, reorganizing, adding images, rotating, compressing, and more. This locally hosted web application has evolved to encompass a comprehensive set of features, addressing all your PDF requirements.

<!--- header STOP from tools/include/markdown/STR001-header.md --->

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash
armbian-config --cmd STR001
~~~


<!--- footer START from tools/include/markdown/STR001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8077**:

    - URL: `https://<your.IP>:8077`

=== "Directories"

    - Install directory: `/armbian/stirling`

=== "View logs"

    ```sh
    docker logs -f stirling-pdf
    ```

<!--- footer STOP from tools/include/markdown/STR001-footer.md --->


~~~ bash title="Stirling PDF remove:"
armbian-config --cmd STR002
~~~


~~~ bash title="Stirling PDF purge with data folder:"
armbian-config --cmd STR003
~~~




## Syncthing


Syncthing continuous file synchronization


<!--- section image START from tools/include/images/STC001.png --->
[![Syncthing](/images/STC001.png)](#)
<!--- section image STOP from tools/include/images/STC001.png --->

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash
armbian-config --cmd STC001
~~~


~~~ bash title="Syncthing remove:"
armbian-config --cmd STC002
~~~


~~~ bash title="Syncthing purge with data folder:"
armbian-config --cmd STC003
~~~




## Nextcloud


Nextcloud content collaboration platform


<!--- section image START from tools/include/images/NCT001.png --->
[![Nextcloud](/images/NCT001.png)](#)
<!--- section image STOP from tools/include/images/NCT001.png --->


<!--- header START from tools/include/markdown/NCT001-header.md --->
Nextcloud gives you access to all your files wherever you are. Where are your photos and documents? With Nextcloud you pick a server of your choice, at home, in a data center or at a provider. And that is where your files will be. Nextcloud runs on that server, protecting your data and giving you access from your desktop or mobile devices. Through Nextcloud you also access, sync and share your existing data on that FTP drive at the office, a Dropbox or a NAS you have at home.

<!--- header STOP from tools/include/markdown/NCT001-header.md --->

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash
armbian-config --cmd NCT001
~~~


<!--- footer START from tools/include/markdown/NCT001-footer.md --->
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

<!--- footer STOP from tools/include/markdown/NCT001-footer.md --->


~~~ bash title="Nextcloud remove:"
armbian-config --cmd NCT002
~~~


~~~ bash title="Nextcloud purge with data folder:"
armbian-config --cmd NCT003
~~~




## Owncloud


Owncloud share files and folders, easy and secure


<!--- section image START from tools/include/images/OWC001.png --->
[![Owncloud](/images/OWC001.png)](#)
<!--- section image STOP from tools/include/images/OWC001.png --->


<!--- header START from tools/include/markdown/OWC001-header.md --->
ownCloud is a free and open-source software project for content collaboration and sharing and syncing of files in distributed and federated enterprise scenarios.

<!--- header STOP from tools/include/markdown/OWC001-header.md --->

**Author:** @igorpecovnik

**Status:** Stable


~~~ custombash
armbian-config --cmd OWC001
~~~


<!--- footer START from tools/include/markdown/OWC001-footer.md --->
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

<!--- footer STOP from tools/include/markdown/OWC001-footer.md --->


~~~ bash title="Owncloud remove:"
armbian-config --cmd OWC002
~~~


~~~ bash title="Owncloud purge with data folder:"
armbian-config --cmd OWC003
~~~




## Jellyfin


Jellyfin Media System


<!--- section image START from tools/include/images/JMS001.png --->
[![Jellyfin](/images/JMS001.png)](#)
<!--- section image STOP from tools/include/images/JMS001.png --->


<!--- header START from tools/include/markdown/JMS001-header.md --->
Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it.

<!--- header STOP from tools/include/markdown/JMS001-header.md --->

**Author:** @igorpecovnik

**Status:** Preview


~~~ custombash
armbian-config --cmd JMS001
~~~


<!--- footer START from tools/include/markdown/JMS001-footer.md --->
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

<!--- footer STOP from tools/include/markdown/JMS001-footer.md --->


~~~ bash title="Jellyfin remove:"
armbian-config --cmd JMS002
~~~


~~~ bash title="Jellyfin purge with data folder:"
armbian-config --cmd JMS003
~~~




## Hastebin


Hastebin Paste Server


<!--- section image START from tools/include/images/HPS001.png --->
[![Hastebin](/images/HPS001.png)](#)
<!--- section image STOP from tools/include/images/HPS001.png --->


<!--- header START from tools/include/markdown/HPS001-header.md --->
Hastebin is a fast and simple self-hosted pastebin server. It allows users to quickly share text snippets like logs, code, or notes via a web interface or API. Hastebin is lightweight, easy to deploy with Docker, and ideal for teams needing private, temporary paste storage.

<!--- header STOP from tools/include/markdown/HPS001-header.md --->

**Author:** @efectn

**Status:** Stable


~~~ custombash
armbian-config --cmd HPS001
~~~


~~~ bash title="Hastebin remove:"
armbian-config --cmd HPS002
~~~


~~~ bash title="Hastebin purge with data folder:"
armbian-config --cmd HPS003
~~~



