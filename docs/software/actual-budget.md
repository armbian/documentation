---
title: "Actual Budget"
seo_title: "Install Actual Budget on Armbian"
description: "Install and run Actual Budget on Armbian — Do your finances with Actual Budget. Runs on ARM64 and x86 single-board computers."
image: /images/ABU001.png
category: "Finance"
comments: true
---
# Actual Budget


<!--- section image START from tools/include/images/ABU001.png --->
![Actual Budget](/images/ABU001.png){ .app-logo }
<!--- section image STOP from tools/include/images/ABU001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://actualbudget.org/docs) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:5443`


<!--- header START from tools/include/markdown/ABU001-header.md --->
[Actual Budget](https://actualbudget.org/) is a **free, open-source personal finance app** built around the **envelope budgeting method**.

- **Privacy-focused**: Users can self-host their data or use encrypted cloud syncing.
- **Key Features**:
  - Multi-account tracking
  - Transaction importing
  - Customizable financial reports
  - Optional syncing via services like PikaPods
- **Ideal for**: Those who want a **transparent**, **self-hosted** alternative to proprietary budgeting tools.

<!--- header STOP from tools/include/markdown/ABU001-header.md --->


Install from **[armbian-config](/config/) → Software → Finance → Actual Budget**

~~~ custombash title="CLI install"
armbian-config --cmd ABU001
~~~


<!--- footer START from tools/include/markdown/ABU001-footer.md --->
!!! danger "Warning: HTTPS Certificate Required"

    After initially installing the Actual server, you might get stuck at the step:  
    **"Initializing the connection to the local database..."**

    The issue is due to the server not having an **HTTPS certificate**.  
    After activating an HTTPS certificate for the Actual server, everything should work fine.

    If you still encounter issues even after setting up HTTPS, we highly recommend reaching out to the [Actual Budget Discord server](https://discord.gg/actualbudget) — the developers and community there are very kind and helpful.


<!--- footer STOP from tools/include/markdown/ABU001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_actualbudget install` |
| Actual Budget remove | `armbian-config --api module_actualbudget remove` |
| Actual Budget purge with data folder | `armbian-config --api module_actualbudget purge` |
| Status | `armbian-config --api module_actualbudget status` |
| Help | `armbian-config --api module_actualbudget help` |

---

_Part of Armbian's [Manage your finances](/User-Guide_Armbian-Software/Finance/) software._
