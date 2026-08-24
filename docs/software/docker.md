---
title: "Docker"
description: "Install and run Docker on Armbian — Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management. Runs on ARM64 and x86 single-board computers."
image: /images/CON001.png
category: "Containers"
comments: true
---
# Docker


Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management.


<!--- section image START from tools/include/images/CON001.png --->
![Docker](/images/CON001.png){ .app-logo }
<!--- section image STOP from tools/include/images/CON001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://docs.docker.com)


Install from **[armbian-config](/config/) → Software → Containers → Docker**

~~~ custombash title="CLI install"
armbian-config --cmd CON001
~~~


<!--- footer START from tools/include/markdown/CON001-footer.md --->
What is Docker? Docker helps developers build, share, run, and verify applications anywhere - without tedious environment configuration or management.

<!--- footer STOP from tools/include/markdown/CON001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_docker install` |
| Docker remove | `armbian-config --api module_docker remove` |
| Docker purge with all images, containers, and volumes | `armbian-config --api module_docker purge` |
| Status | `armbian-config --api module_docker status` |
| Help | `armbian-config --api module_docker help` |

---

_Part of Armbian's [Docker containerization and KVM virtual machines](/User-Guide_Armbian-Software/Containers/) software._
