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
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

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




## Wallos


Install Wallos subscription tracker


<!--- section image START from tools/include/images/WAL001.png --->
[![Wallos](/images/WAL001.png)](#)
<!--- section image STOP from tools/include/images/WAL001.png --->


<!--- header START from tools/include/markdown/WAL001-header.md --->
Wallos is a self-hosted finance tracker and subscription management application. It helps you monitor recurring expenses, track subscriptions, and manage your financial commitments in one centralized location. With Wallos, you can visualize spending patterns, set renewal reminders, and take control of your recurring payments.

This Docker-based application runs as a lightweight web service, providing an intuitive interface for managing all your subscriptions and recurring expenses. The data is stored locally in SQLite database, ensuring your financial information remains private and under your control.

=== "Features"

    **Subscription Tracking**

    - Add and manage all your subscriptions (Netflix, Spotify, cloud services, etc.)
    - Track monthly, yearly, or one-time payments
    - Categorize expenses by type (streaming, software, utilities, etc.)
    - Set custom renewal dates and reminders

    **Financial Overview**

    - Visual dashboard showing total monthly/yearly expenses
    - Breakdown by category and service provider
    - Currency conversion support for international subscriptions
    - Export data to CSV for further analysis

    **Data Management**

    - Upload custom logos for service providers
    - Local SQLite database storage (no cloud dependency)
    - Automatic backups through Docker volume mounts
    - Import/export functionality for data portability

=== "Accessing Wallos"

    Once installed, access Wallos by navigating to:

    **http://your-server-ip:8282**

    On first access, you'll be guided through the initial setup:
    1. Create your admin account
    2. Configure currency preferences
    3. Set up default categories
    4. Start adding subscriptions

=== "Data Persistence"

    Wallos data is stored in Docker volumes for persistence:

    - **Database volume**: `/var/www/html/db` → stored at `${config_dir}/db`
    - **Logos volume**: `/var/www/html/images/uploads/logos` → stored at `${config_dir}/logos`

=== "Troubleshooting"

    **Container won't start**

    - Check port conflicts: `docker ps -a | grep wallos`
    - Verify volume mounts exist and have correct permissions
    - Review logs: `docker logs wallos`

    **Cannot access web interface**

    - Confirm container is running: `docker ps | grep wallos`
    - Check firewall rules allow port 8282
    - Verify correct IP address if accessing remotely

    **Data loss after restart**

    - Ensure Docker volumes are properly mounted
    - Check that persistence directories are not cleaned on reboot
    - Verify backup of `${config_dir}` before making changes

=== "View logs"

    ```sh
    docker logs -f wallos
    ```

<!--- header STOP from tools/include/markdown/WAL001-header.md --->

__Edit:__ [footer](https://github.com/armbian/configng/edit/main/tools/include/markdown/WAL001-footer.md) [header](https://github.com/armbian/configng/edit/main/tools/include/markdown/WAL001-header.md)  
__Status:__ Stable  
__Architecture:__ <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">aarch64</span> <span style="background-color:#fff3bf; color:#7c4d00; padding:3px 6px; border-radius:4px; font-size:90%;">armhf</span> <span style="background-color:#f3d9fa; color:#6a1b9a; padding:3px 6px; border-radius:4px; font-size:90%;">riscv64</span>  
__Maintainer:__ @armbian  
__Documentation:__ [Link](https://forum.armbian.com/)  
__Installation:__ <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span>  

~~~ custombash
armbian-config --cmd WAL001
~~~


<!--- footer START from tools/include/markdown/WAL001-footer.md --->
**Key Use Cases**

Personal Finance Management

- **Subscription Awareness**: Track all recurring payments in one place
- **Budget Planning**: See exactly how much you spend monthly on subscriptions
- **Renewal Reminders**: Never miss a payment or forget to cancel unwanted services
- **Cost Optimization**: Identify unused or redundant subscriptions to cancel

Family Finance

- **Shared Dashboard**: Multiple family members can access the same instance
- **Categorization**: Organize expenses by person or category
- **Total Visibility**: Get a complete picture of household recurring expenses

Small Business

- **Service Tracking**: Monitor software subscriptions, SaaS tools, and business services
- **Expense Categorization**: Separate personal and business subscriptions
- **Financial Planning**: Forecast recurring costs for better budget management

<!--- footer STOP from tools/include/markdown/WAL001-footer.md --->


~~~ bash title="Remove Wallos:"
armbian-config --cmd WAL002
~~~


~~~ bash title="Purge Wallos:"
armbian-config --cmd WAL003
~~~



