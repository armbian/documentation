---
comments: true
---

# SQL database servers and web interface managers

## Mariadb SQL database server

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/DAT001.png --->
[![Mariadb SQL database server](/images/DAT001.png)](#)
<!--- section image STOP from tools/include/images/DAT001.png --->


<!--- header START from tools/include/markdown/DAT001-header.md --->
Mariadb is one of the most popular database servers. Made by the original developers of MySQL.

<!--- header STOP from tools/include/markdown/DAT001-header.md --->


~~~ bash title="Mariadb SQL database server:"
armbian-config --cmd DAT001
~~~

## Mariadb remove


~~~ bash title="Mariadb remove:"
armbian-config --cmd DAT002
~~~

## Mariadb purge with data folder


~~~ bash title="Mariadb purge with data folder:"
armbian-config --cmd DAT003
~~~

## phpMyAdmin web interface manager


<!--- section image START from tools/include/images/DAT005.png --->
[![phpMyAdmin web interface manager](/images/DAT005.png)](#)
<!--- section image STOP from tools/include/images/DAT005.png --->


<!--- header START from tools/include/markdown/DAT005-header.md --->
Phpmyadmin is a free software tool written in PHP, intended to handle the administration of MySQL over the Web. phpMyAdmin supports a wide range of operations on MySQL and MariaDB.

<!--- header STOP from tools/include/markdown/DAT005-header.md --->


~~~ bash title="phpMyAdmin web interface manager:"
armbian-config --cmd DAT005
~~~

## phpMyAdmin remove


~~~ bash title="phpMyAdmin remove:"
armbian-config --cmd DAT006
~~~

## phpMyAdmin purge with data folder


~~~ bash title="phpMyAdmin purge with data folder:"
armbian-config --cmd DAT007
~~~
