---
comments: true
---

# Backup solutions for your data

## Duplicati


Duplicati install


<!--- section image START from tools/include/images/DPL001.png --->
[![Duplicati](/images/DPL001.png)](#)
<!--- section image STOP from tools/include/images/DPL001.png --->


<!--- header START from tools/include/markdown/DPL001-header.md --->
Duplicati is a versatile and secure backup tool designed for everyone, including:

- Users new to backup systems who need a simple and reliable solution.
- Experienced users who want full control over encrypted backups and storage destinations.
- System administrators who require automated, encrypted backups across multiple platforms.

Duplicati offers powerful features such as strong AES-256 encryption, backup scheduling, and flexible storage support (local folders, NAS, cloud providers like Google Drive, Dropbox, S3, and more).  
Through its web-based interface, users can easily configure, monitor, and restore backups from any browser.

Thanks to Duplicati’s smart design — working through standard protocols and containerized deployment — it fits seamlessly into any environment, from personal setups to enterprise infrastructures.

<!--- header STOP from tools/include/markdown/DPL001-header.md --->

__Maintainer:__ @igorpecovnik  
__Status:__ Stable  
__Architecture:__ x86-64 arm64  
__Documentation:__ [Link](https://prev-docs.duplicati.com/en/latest/)  

~~~ custombash
armbian-config --cmd DPL001
~~~


<!--- footer START from tools/include/markdown/DPL001-footer.md --->
=== "Access to the web interface"

    The web interface is accessible via port **8200**:

    - URL: `http://<your.IP>:8200`

=== "Directories"

    - Install directory: `/armbian/duplicati`
    - Configuration directory: `/armbian/duplicati/config`
    - Backup target directory: `/armbian/duplicati/backups`

=== "View logs"

    ```sh
    docker logs -f duplicati
    ```

<!--- footer STOP from tools/include/markdown/DPL001-footer.md --->


~~~ bash title="Duplicati remove:"
armbian-config --cmd DPL002
~~~


~~~ bash title="Duplicati purge with data folder:"
armbian-config --cmd DPL003
~~~



