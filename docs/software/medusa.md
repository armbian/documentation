---
title: "Medusa"
seo_title: "Install Medusa on Armbian"
description: "Install and run Medusa on Armbian — Medusa automatic downloader for TV shows. Runs on ARM64 and x86 single-board computers."
image: /images/MDS001.png
category: "Downloaders"
comments: true
---
# Medusa


<!--- section image START from tools/include/images/MDS001.png --->
![Medusa](/images/MDS001.png){ .app-logo }
<!--- section image STOP from tools/include/images/MDS001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://github.com/pymedusa/Medusa/wiki) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8081`


<!--- header START from tools/include/markdown/MDS001-header.md --->
Medusa is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

<!--- header STOP from tools/include/markdown/MDS001-header.md --->


Install from **[armbian-config](/config/) → Software → Downloaders → Medusa**

~~~ custombash title="CLI install"
armbian-config --cmd MDS001
~~~


<!--- footer START from tools/include/markdown/MDS001-footer.md --->
=== "Directories"

    - Install directory: `/armbian/medusa`
    - Site configuration directory: `/armbian/medusa/config`
    - Download directory: `/armbian/medusa/downloads`
    - Download directory TV shows: `/armbian/medusa/downloads/tv`

=== "View logs"

    ```sh
    docker logs -f medusa
    ```

<!--- footer STOP from tools/include/markdown/MDS001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_medusa install` |
| Medusa TV shows downloader remove | `armbian-config --api module_medusa remove` |
| Medusa TV shows downloader purge | `armbian-config --api module_medusa purge` |
| Status | `armbian-config --api module_medusa status` |
| Help | `armbian-config --api module_medusa help` |

---

_Part of Armbian's [Download apps for movies, TV shows, music and subtitles](/User-Guide_Armbian-Software/Downloaders/) software._
