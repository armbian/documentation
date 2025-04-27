---
comments: true
---

# SQL database servers and web interface managers

## Mariadb


Mariadb SQL database server


<!--- section image START from tools/include/images/DAT001.png --->
[![Mariadb](/images/DAT001.png)](#)
<!--- section image STOP from tools/include/images/DAT001.png --->


<!--- header START from tools/include/markdown/DAT001-header.md --->
Mariadb is one of the most popular database servers. Made by the original developers of MySQL.

<!--- header STOP from tools/include/markdown/DAT001-header.md --->

**Author:** @armbian

**Status:** Stable


~~~ custombash
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


~~~ bash title="Mariadb remove:"
armbian-config --cmd DAT002
~~~


~~~ bash title="Mariadb purge with data folder:"
armbian-config --cmd DAT003
~~~




## phpMyAdmin


phpMyAdmin web interface manager


<!--- section image START from tools/include/images/MYA001.png --->
[![phpMyAdmin](/images/MYA001.png)](#)
<!--- section image STOP from tools/include/images/MYA001.png --->

**Author:** @armbian

**Status:** Stable


~~~ custombash
armbian-config --cmd MYA001
~~~


~~~ bash title="phpMyAdmin remove:"
armbian-config --cmd MYA002
~~~


~~~ bash title="phpMyAdmin purge with data folder:"
armbian-config --cmd MYA003
~~~



