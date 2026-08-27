---
seo_title: "Run an Armbian mirror: rsync sync & registration"
description: "How to contribute an Armbian mirror: set up an HTTPS host, sync the images and packages over rsync, and register the server with the redirector network."
---
# Run a mirror

Armbian's downloads are served by a network of community mirrors behind a
redirector. If you can host one, here is how. You can see the
[current mirrors and how the system works](/status/mirrors/) on the status page.

### 1. Set up an HTTP(S) host

The mirror must be reachable over HTTPS (plain HTTP is also accepted). Point a hostname at it before you start syncing.

### 2. Sync with `rsync`

Pull the content you want to serve from one of the official modules, and run it from cron every **2-4 hours**:

| Content | Command | Required space |
|---------|---------|---------------:|
| Current images | `rsync -av rsync://rsync.armbian.com/dl` | 556G |
| Packages | `rsync -av rsync://rsync.armbian.com/apt` | 84G |
| Archived images | `rsync -av rsync://rsync.armbian.com/archive` | 1.9T |
| Very old images | `rsync -av rsync://rsync.armbian.com/oldarchive` | 5.4T |

### 3. Tell us about it

Once the server is running, reach out through the [contact form](https://www.armbian.com/contact/) so we can add it to the official redirector.

Thanks for helping keep Armbian's downloads fast and reliable worldwide.
