---
title: "Stirling"
description: "Install and run Stirling on Armbian — Stirling PDF tools for viewing and editing PDF files. Runs on ARM64 and x86 single-board computers."
image: /images/STR001.png
category: "Media"
comments: true
---
# Stirling


<!--- section image START from tools/include/images/STR001.png --->
![Stirling](/images/STR001.png)
<!--- section image STOP from tools/include/images/STR001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.stirlingpdf.com) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8075`


<!--- header START from tools/include/markdown/STR001-header.md --->
Stirling-PDF is a robust, locally hosted web-based PDF manipulation tool using Docker. It enables you to carry out various operations on PDF files, including splitting, merging, converting, reorganizing, adding images, rotating, compressing, and more. This locally hosted web application has evolved to encompass a comprehensive set of features, addressing all your PDF requirements.

<!--- header STOP from tools/include/markdown/STR001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Media → Stirling**

~~~ custombash title="CLI install"
armbian-config --cmd STR001
~~~


<!--- footer START from tools/include/markdown/STR001-footer.md --->
=== "Directories"

    - Install directory: `/armbian/stirling`

=== "View logs"

    ```sh
    docker logs -f stirling-pdf
    ```

<!--- footer STOP from tools/include/markdown/STR001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_stirling install` |
| Stirling PDF remove | `armbian-config --api module_stirling remove` |
| Stirling PDF purge with data folder | `armbian-config --api module_stirling purge` |
| Status | `armbian-config --api module_stirling status` |
| Help | `armbian-config --api module_stirling help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
