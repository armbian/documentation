---
comments: true
---

# Web server, LEMP, reverse proxy, Let's Encrypt SSL

## SWAG reverse proxy

**Status:** Stable

**Author:** @armbian


<!--- section image START from tools/include/images/SWAG01.png --->
[![SWAG reverse proxy](/images/SWAG01.png)](#)
<!--- section image STOP from tools/include/images/SWAG01.png --->


<!--- header START from tools/include/markdown/SWAG01-header.md --->
SWAG - Secure Web Application Gateway sets up an Nginx webserver and reverse proxy with php support and a built-in certbot client that automates free SSL server certificate generation and renewal processes (Let's Encrypt). It also contains fail2ban for intrusion prevention.

After entering required information, your server will have auto updating SSL secured website! To this website you can attach several services, for example: https://my.server.com/netdata will run [Netdata](https://www.netdata.cloud/) instance.

=== "Requirements"

    - this computer port 80 and 443 must be open to the internet
    - your domain name (myserver.mydomain.com) DNS server should point to your router WAN address
    - make sure to set additional .htpasswd username and password as you don't want to expose your services without password

=== "Directories"

    - Config directory: `/armbian/swag/config/`
    - Website root folder: `/armbian/swag/config/www/`
    - Reverse proxy configuration samples: `/armbian/swag/config/nginx/proxy-confs/`

=== "Advanced setup"

    - Please follow this comprehensive guide: <https://github.com/linuxserver/docker-swag>

<!--- header STOP from tools/include/markdown/SWAG01-header.md --->


~~~ bash title="SWAG reverse proxy:"
armbian-config --cmd SWAG01
~~~

## SWAG reverse proxy .htpasswd set


~~~ bash title="SWAG reverse proxy .htpasswd set:"
armbian-config --cmd SWAG02
~~~

## SWAG remove


~~~ bash title="SWAG remove:"
armbian-config --cmd SWAG03
~~~

## SWAG purge with data folder


~~~ bash title="SWAG purge with data folder:"
armbian-config --cmd SWAG04
~~~
