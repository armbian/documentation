---
title: "Duplicati"
description: "Install and run Duplicati on Armbian — Duplicati install. Runs on ARM64 and x86 single-board computers."
image: /images/DPL001.png
category: "Backup"
comments: true
---
# Duplicati


<!--- section image START from tools/include/images/DPL001.png --->
![Duplicati](/images/DPL001.png){ .app-logo }
<!--- section image STOP from tools/include/images/DPL001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://prev-docs.duplicati.com/en/latest/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8200`


<!--- header START from tools/include/markdown/DPL001-header.md --->
Duplicati is a versatile and secure backup tool designed for everyone, including:

- Users new to backup systems who need a simple and reliable solution.
- Experienced users who want full control over encrypted backups and storage destinations.
- System administrators who require automated, encrypted backups across multiple platforms.

Duplicati offers powerful features such as strong AES-256 encryption, backup scheduling, and flexible storage support (local folders, NAS, cloud providers like Google Drive, Dropbox, S3, and more).  
Through its web-based interface, users can easily configure, monitor, and restore backups from any browser.

Thanks to Duplicati’s smart design — working through standard protocols and containerized deployment — it fits seamlessly into any environment, from personal setups to enterprise infrastructures.

<!--- header STOP from tools/include/markdown/DPL001-header.md --->


Install from **[armbian-config](/config/) → Software → Backup → Duplicati**

~~~ custombash title="CLI install"
armbian-config --cmd DPL001
~~~


<!--- footer START from tools/include/markdown/DPL001-footer.md --->
=== "Directories"

    - Install directory: `/armbian/duplicati`
    - Configuration directory: `/armbian/duplicati/config`
    - Backup target directory: `/armbian/duplicati/backups`

=== "View logs"

    ```sh
    docker logs -f duplicati
    ```

<!--- footer STOP from tools/include/markdown/DPL001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_duplicati install` |
| Duplicati remove | `armbian-config --api module_duplicati remove` |
| Duplicati purge with data folder | `armbian-config --api module_duplicati purge` |
| Status | `armbian-config --api module_duplicati status` |
| Help | `armbian-config --api module_duplicati help` |

---

_Part of Armbian's [Backup solutions for your data](/User-Guide_Armbian-Software/Backup/) software._
