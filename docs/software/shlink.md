---
title: "Shlink"
seo_title: "Install Shlink on Armbian"
description: "Install and run Shlink on Armbian — Shlink URL shortener. Runs on ARM64 and x86 single-board computers."
image: /images/SHL001.png
category: "WebHosting"
comments: true
---
# Shlink


<!--- section image START from tools/include/images/SHL001.png --->
![Shlink](/images/SHL001.png){ .app-logo }
<!--- section image STOP from tools/include/images/SHL001.png --->


:material-cpu-64-bit:{ title="Architecture" } <span style="background-color:#e0e0e0; color:#333333; padding:3px 6px; border-radius:4px; font-size:90%;">x86-64</span> <span style="background-color:#d3f9d8; color:#1b5e20; padding:3px 6px; border-radius:4px; font-size:90%;">arm64</span> · <span style="background-color:#ffffff; color:#039BE5; padding:3px 6px; border-radius:4px; font-size:90%;">🐳 Docker</span> · :material-book-open-variant:{ title="Documentation" } [Documentation](https://shlink.io/documentation/) · :material-lan-connect:{ title="Access port" } `http://<your.IP>:8085`


<!--- header START from tools/include/markdown/SHL001-header.md --->
[Shlink](https://shlink.io) is a self-hosted URL shortener. It turns long links into short ones on your own domain, with custom slugs, tags, expiry dates and QR codes.
Manage links with the REST API, the `shlink` command line or the [Shlink web client](https://app.shlink.io).

<!--- header STOP from tools/include/markdown/SHL001-header.md --->


Install from **[armbian-config](/config/) → Software → Web Hosting → Shlink**

The app has no separate image. [Install an Armbian OS image first](/software/#how-to-install-an-app), then the app. For help with the app, [read its documentation](https://shlink.io/documentation/).

~~~ custombash title="CLI install"
armbian-config --cmd SHL001
~~~


<!--- footer START from tools/include/markdown/SHL001-footer.md --->
=== "Short domain"

    The install asks for the domain of the short links, for example `go.example.com`.

    - A domain without a port uses HTTPS. Shlink then listens on `127.0.0.1:8085` only. Put a reverse proxy with a certificate in front, for example [SWAG](https://docs.armbian.com/software/swag/).
    - Keep the default `<your.IP>:8085` to use Shlink on the local network only.
    - For an unattended install, set the domain in the environment:

    ```sh
    sudo SHLINK_DOMAIN=go.example.com armbian-config --api module_shlink install
    ```

=== "API key"

    The install creates an API key. Read it from the settings file:

    ```sh
    sudo grep INITIAL_API_KEY /armbian/shlink/shlink.env
    ```

    Create a short link. Use your short domain over HTTPS. The `http://<your.IP>:8085` form is for local network installs only.

    ```sh
    curl -X POST https://go.example.com/rest/v3/short-urls \
      -H "X-Api-Key: <key>" -H "Content-Type: application/json" \
      -d '{"longUrl": "https://docs.armbian.com/", "customSlug": "docs"}'
    ```

=== "Command line"

    ```sh
    docker exec -it shlink shlink short-url:create https://docs.armbian.com/
    docker exec -it shlink shlink short-url:list
    ```

=== "Directories"

    - Settings and API key: `/armbian/shlink/shlink.env`
    - Data: `/armbian/shlink/data/`

=== "View logs"

    ```sh
    docker logs -f shlink
    ```

<!--- footer STOP from tools/include/markdown/SHL001-footer.md --->


**All `armbian-config` commands**

| Action | Command |
| --- | --- |
| Install | `armbian-config --api module_shlink install` |
| Shlink remove | `armbian-config --api module_shlink remove` |
| Shlink purge with data folder | `armbian-config --api module_shlink purge` |
| Status | `armbian-config --api module_shlink status` |
| Help | `armbian-config --api module_shlink help` |

---

_Part of Armbian's [Web server, LEMP, reverse proxy, Let's Encrypt SSL](/software/web-hosting/) software._
