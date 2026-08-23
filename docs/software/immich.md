---
title: "Immich"
description: "Install and run Immich on Armbian — high-performance self-hosted photo and video backup solution. Runs on ARM64 and x86 single-board computers."
image: /images/IMM001.png
category: "Media"
comments: true
---
# Immich


<!--- section image START from tools/include/images/IMM001.png --->
![Immich](/images/IMM001.png)
<!--- section image STOP from tools/include/images/IMM001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://immich.app/docs) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8077`


<!--- header START from tools/include/markdown/IMM001-header.md --->
[**Immich**](https://immich.app/) is a self-hosted photo and video backup solution, designed for individuals and families who want:

- An alternative to cloud-based services like Google Photos or iCloud  
- A private, secure place to store, browse, and share memories  
- Powerful features like automatic mobile uploads, facial recognition, and search  
- A modern, responsive web and mobile interface for easy access

Thanks to Immich being built with modern technologies like NestJS, TypeScript, and machine learning integrations, users enjoy a smooth, intelligent media experience. Whether you’re a casual user backing up phone photos or a tech-savvy person managing media across multiple devices, Immich provides the flexibility and control of a cloud solution—on your own server.

**Summary**

- **Immich** is ideal if you want full privacy, open-source flexibility, and control over your data.
- **Google Photos** is convenient and polished but comes with trade-offs in privacy and cost at scale.
- **Synology Photos** fits well in homes or small offices already using Synology NAS systems, offering good performance with integrated features.

<!--- header STOP from tools/include/markdown/IMM001-header.md --->


Install from **[armbian-config](/User-Guide_Armbian-Config/) → Software → Media → Immich**

~~~ custombash title="CLI install"
armbian-config --cmd IMM001
~~~


<!--- footer START from tools/include/markdown/IMM001-footer.md --->
=== "Default credentials"

    - Email: *(set during initial setup)*
    - Password: *(set during initial setup)*

=== "Directories"

    - Uploads: `/armbian/immich/photos/upload/`
    - Thumbnails: `/armbian/immich/photos/thumbs/`
    - Profile images: `/armbian/immich/photos/profile/`
    - Library: `/armbian/immich/photos/library/`
    - Encoded videos: `/armbian/immich/photos/encoded-video/`
    - Backups: `/armbian/immich/photos/backups/`

=== "View logs"

    ```sh
    docker logs -f immich
    ```

=== "Immich vs Google Photos vs Synology Photos"

    | Feature / Aspect               | **Immich**                                | **Google Photos**                           | **Synology Photos**                         |
    |-------------------------------|-------------------------------------------|---------------------------------------------|---------------------------------------------|
    | **Hosting**                   | Self-hosted                               | Cloud (Google infrastructure)               | Self-hosted (on Synology NAS)               |
    | **Privacy & Control**         | Full control, private data storage        | Data stored and analyzed by Google          | Full control within your NAS environment    |
    | **Automatic Uploads**         | Yes (via mobile app)                      | Yes (via mobile app)                        | Yes (via mobile app or Synology Drive)      |
    | **Facial Recognition**        | Yes (on-device)                           | Yes (cloud-based)                           | Yes (on-device)                             |
    | **Object & Scene Detection**  | Yes (limited but improving)               | Yes (advanced AI)                           | Yes (basic)                                 |
    | **Web Interface**             | Yes (modern and responsive)               | Yes                                         | Yes                                         |
    | **Mobile Apps**               | Yes (iOS & Android)                       | Yes (iOS & Android)                         | Yes (iOS & Android)                         |
    | **Albums & Sharing**          | Yes (with public and private sharing)     | Yes (advanced sharing options)              | Yes                                         |
    | **Multi-user Support**        | Yes                                       | Limited (mostly single user)                | Yes (multi-user, tied to NAS users)         |
    | **Backup Original Quality**   | Yes (no compression)                      | Only with paid storage                      | Yes (NAS dependent)                         |
    | **Offline Access**            | Limited (depends on app setup)            | Yes (with sync)                             | Yes                                         |
    | **Open Source**               | Yes                                       | No                                          | No                                          |
    | **Hardware Requirement**      | Any Docker-capable server or NAS          | N/A (runs on Google’s cloud)                | Synology NAS required                       |
    | **Price**                     | Free (self-hosted, you pay for hardware)  | Free (with limitations) / Paid for storage  | Included with NAS, hardware cost required   |

<!--- footer STOP from tools/include/markdown/IMM001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_immich install` |
| Immich remove | `armbian-config --api module_immich remove` |
| Immich purge with data folder | `armbian-config --api module_immich purge` |
| Status | `armbian-config --api module_immich status` |
| Help | `armbian-config --api module_immich help` |

---

_Part of Armbian's [Media servers, organizers and editors](/User-Guide_Armbian-Software/Media/) software._
