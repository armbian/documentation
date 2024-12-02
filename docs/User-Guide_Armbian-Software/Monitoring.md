# Monitoring


***

## Uptime Kuma install 
**Command:** 
~~~
armbian-config --cmd MON001
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/MON001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **3001**:

    - URL: `https://<your.IP>:3001`
    - Username/Password: Are set at first web interface login

???+ "Uptime Kuma features"

    - Monitoring uptime for HTTP(s) / TCP / HTTP(s) Keyword / HTTP(s) Json Query / Ping / DNS Record / Push / Steam Game Server / Docker Containers
    - Fancy, Reactive, Fast UI/UX
    - Notifications via Telegram, Discord, Gotify, Slack, Pushover, Email (SMTP), and 90+ notification services, click here for the full list
    - 20-second intervals
    - Multi Languages
    - Multiple status pages
    - Map status pages to specific domains
    - Ping chart
    - Certificate info
    - Proxy support
    - 2FA support

<!--- footer STOP from tools/include/markdown/MON001-footer.md --->



***

## Uptime Kuma remove
**Command:** 
~~~
armbian-config --cmd MON002
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Uptime Kuma purge data folder
**Command:** 
~~~
armbian-config --cmd MON003
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Netdata Install

<!--- section image START from tools/include/images/MON005.png --->
[![Netdata Install](/images/MON005.png)](#)
<!--- section image STOP from tools/include/images/MON005.png --->


<!--- header START from tools/include/markdown/MON005-header.md --->
Netdata is a partially open source tool designed to collect real-time metrics, such as CPU usage, disk activity, bandwidth usage, website visits, etc., and then display them in live, easy-to-interpret charts.

<!--- header STOP from tools/include/markdown/MON005-header.md --->

**Command:** 
~~~
armbian-config --cmd MON005
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Netdata remove
**Command:** 
~~~
armbian-config --cmd MON006
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

## Netdata purge data folder
**Command:** 
~~~
armbian-config --cmd MON007
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

