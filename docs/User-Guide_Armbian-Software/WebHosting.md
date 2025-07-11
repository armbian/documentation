---
comments: true
---

# Web server, LEMP, reverse proxy, Let's Encrypt SSL

## SWAG


SWAG reverse proxy


<!--- section image START from tools/include/images/SWAG01.png --->
[![SWAG](/images/SWAG01.png)](#)
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

__Edit:__ [footer](https://github.com/armbian/configng/new/main/tools/include/markdown/SWAG01-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/SWAG01-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://github.com/linuxserver/docker-swag)  

~~~ custombash
armbian-config --cmd SWAG01
~~~


~~~ bash title="SWAG reverse proxy .htpasswd set:"
armbian-config --cmd SWAG02
~~~


~~~ bash title="SWAG remove:"
armbian-config --cmd SWAG03
~~~


~~~ bash title="SWAG purge with data folder:"
armbian-config --cmd SWAG04
~~~





## Ghost


Ghost CMS install


<!--- section image START from tools/include/images/GHOST1.png --->
[![Ghost](/images/GHOST1.png)](#)
<!--- section image STOP from tools/include/images/GHOST1.png --->


<!--- header START from tools/include/markdown/GHOST1-header.md --->
Ghost is a powerful open-source publishing platform designed for professional publishing, newsletters, and modern blogs. It’s built on Node.js and provides a clean, fast, and customizable CMS experience.

<!--- header STOP from tools/include/markdown/GHOST1-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/GHOST1-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/GHOST1-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://ghost.org/docs/)  

~~~ custombash
armbian-config --cmd GHOST1
~~~


<!--- footer START from tools/include/markdown/GHOST1-footer.md --->
=== "Configuration"

    Initial setup includes:

    - automatic database schema setup on first run
    - admin account created via web interface
    - Default port: `9190`
    - Admin URL: `http://<your.IP>:9190/ghost` (or behind reverse proxy like SWAG)
    - Site: `http://<your.IP>:9190`

=== "Directories"

    - Install directory: `/armbian/ghost`

=== "View logs"

    ```sh
    docker logs -f ghost
    ```

<!--- footer STOP from tools/include/markdown/GHOST1-footer.md --->


~~~ bash title="Ghost CMS remove:"
armbian-config --cmd GHOST2
~~~


~~~ bash title="Ghost CMS purge with data folder:"
armbian-config --cmd GHOST3
~~~



