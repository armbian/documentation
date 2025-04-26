---
comments: true
---

# SQL database servers and web interface managers

## Mariadb SQL database server

**Author:** @armbian

**Status:** Stable


<!--- section image START from tools/include/images/DAT001.png --->
[![Mariadb SQL database server](/images/DAT001.png)](#)
<!--- section image STOP from tools/include/images/DAT001.png --->


<!--- header START from tools/include/markdown/DAT001-header.md --->
Mariadb is one of the most popular database servers. Made by the original developers of MySQL.

<!--- header STOP from tools/include/markdown/DAT001-header.md --->


~~~ custombash title="Mariadb SQL database server:"
armbian-config --cmd DAT001
~~~


<!--- footer START from tools/include/markdown/DAT001-footer.md --->
=== "Configuration"

    Database access configuration is done at first install:
    - create root password
    - create database
    - create normal user
    - create password for normal user

    - Database host: `<your.IP>`

=== "Directories"

    - Install directory: `/armbian/mariadb`
    - Site configuration directory: `/armbian/mariadb/config`

=== "View logs"

    ```sh
    docker logs -f mariadb
    ```

<!--- footer STOP from tools/include/markdown/DAT001-footer.md --->


~~~ custombash title="Mariadb remove:"
armbian-config --cmd DAT002
~~~


~~~ custombash title="Mariadb purge with data folder:"
armbian-config --cmd DAT003
~~~


~~~ custombash title="phpMyAdmin web interface manager:"
armbian-config --cmd DAT005
~~~


<!--- footer START from tools/include/markdown/DAT005-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8071**:

    - URL: `https://<your.IP>:8071`
    - Server: IP from server you are connecting to. If you have installed MariaDB via this tool, then this is `<your.IP>`
    - Username: defined at SQL server install (MariaDb)
    - Password: defined at SQL server install (MariaDb)

=== "Directories"

    - Install directory: `/armbian/phpmyadmin`
    - Site configuration directory: `/armbian/phpmyadmin/config`

=== "View logs"

    ```sh
    docker logs -f phpmyadmin
    ```

<!--- footer STOP from tools/include/markdown/DAT005-footer.md --->


~~~ custombash title="phpMyAdmin remove:"
armbian-config --cmd DAT006
~~~


~~~ custombash title="phpMyAdmin purge with data folder:"
armbian-config --cmd DAT007
~~~
