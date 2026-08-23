---
title: "SABnzbd"
description: "Install and run SABnzbd on Armbian — SABnzbd newsgroup downloader. Runs on ARM64 and x86 single-board computers."
image: /images/SABN01.png
category: "Downloaders"
comments: true
---
# SABnzbd


<!--- section image START from tools/include/images/SABN01.png --->
![SABnzbd](/images/SABN01.png)
<!--- section image STOP from tools/include/images/SABN01.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://sabnzbd.org/wiki/faq) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8380`


<!--- header START from tools/include/markdown/SABN01-header.md --->
Sabnzbd⁠ makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

<!--- header STOP from tools/include/markdown/SABN01-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Downloaders → SABnzbd**

~~~ custombash title="CLI install"
armbian-config --cmd SABN01
~~~


<!--- footer START from tools/include/markdown/SABN01-footer.md --->
=== "Access to the web interface"

    - Username/Password: admin / generate at first web interface login

=== "Directories"

    - Install directory: `/armbian/sabnzbd`
    - Site configuration directory: `/armbian/sabnzbd/config`
    - Download directory: `/armbian/sabnzbd/downloads`
    - Incomplete downloads: `/armbian/sabnzbd/incomplete`

=== "View logs"

    ```sh
    docker logs -f sabnzbd
    ```

<!--- footer STOP from tools/include/markdown/SABN01-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_sabnzbd install` |
| SABnzbd remove | `armbian-config --api module_sabnzbd remove` |
| SABnzbd purge with data folder | `armbian-config --api module_sabnzbd purge` |
| Status | `armbian-config --api module_sabnzbd status` |
| Help | `armbian-config --api module_sabnzbd help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
