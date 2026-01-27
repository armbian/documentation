---
comments: true
---

# Manage your finances

## Actual Budget


Do your finances with Actual Budget


<!--- section image START from tools/include/images/ABU001.png --->
[![Actual Budget](/images/ABU001.png)](#)
<!--- section image STOP from tools/include/images/ABU001.png --->


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

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/ABU001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/ABU001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span>  
__Maintainer:__ @igorpecovnik  
__Documentation:__ [Link](https://actualbudget.org/docs)  

~~~ custombash
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


~~~ bash title="Actual Budget remove:"
armbian-config --cmd ABU002
~~~


~~~ bash title="Actual Budget purge with data folder:"
armbian-config --cmd ABU003
~~~



