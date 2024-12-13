# Database


***

## Mariadb install

<!--- section image START from tools/include/images/DAT001.png --->
[![Mariadb install](/images/DAT001.png)](#)
<!--- section image STOP from tools/include/images/DAT001.png --->


<!--- header START from tools/include/markdown/DAT001-header.md --->
Mariadb is one of the most popular database servers. Made by the original developers of MySQL.

<!--- header STOP from tools/include/markdown/DAT001-header.md --->

**Command:** 
~~~
armbian-config --cmd DAT001
~~~

**Author:** @armbian

**Status:** Stable


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



***

## Mariadb remove
**Command:** 
~~~
armbian-config --cmd DAT002
~~~

**Author:** @armbian

**Status:** Stable



***

## Mariadb purge
**Command:** 
~~~
armbian-config --cmd DAT003
~~~

**Author:** @armbian

**Status:** Stable



***

## phpMyAdmin install

<!--- section image START from tools/include/images/DAT005.png --->
[![phpMyAdmin install](/images/DAT005.png)](#)
<!--- section image STOP from tools/include/images/DAT005.png --->


<!--- header START from tools/include/markdown/DAT005-header.md --->
Phpmyadmin is a free software tool written in PHP, intended to handle the administration of MySQL over the Web. phpMyAdmin supports a wide range of operations on MySQL and MariaDB.

<!--- header STOP from tools/include/markdown/DAT005-header.md --->

**Command:** 
~~~
armbian-config --cmd DAT005
~~~

**Author:** @armbian

**Status:** Stable


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



***

## phpMyAdmin remove
**Command:** 
~~~
armbian-config --cmd DAT006
~~~

**Author:** @armbian

**Status:** Stable



***

## phpMyAdmin purge
**Command:** 
~~~
armbian-config --cmd DAT007
~~~

**Author:** @armbian

**Status:** Stable



***

