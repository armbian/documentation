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

