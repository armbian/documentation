---
seo_title: "Armbian SSH daemon & 2FA remote access"
description: "Manage the SSH daemon, harden remote access and enable two-factor authentication (2FA) on Armbian single-board computers with armbian-config."
comments: true
---

# SSH daemon


Manage SSH daemon options, enable 2FA

## Native


Disable root login


<!--- section image START from tools/include/images/ACC001.png --->
![Native](/images/ACC001.png)
<!--- section image STOP from tools/include/images/ACC001.png --->


<!--- header START from tools/include/markdown/ACC001-header.md --->
Manage native SSH daemon allows you to configure SSH server settings such as login security, authentication methods, and connection restrictions. It also enables setting up Two-Factor Authentication (2FA) to further secure SSH access using time-based codes (TOTP), adding an extra layer of protection beyond passwords.

<!--- header STOP from tools/include/markdown/ACC001-header.md --->


~~~ bash title="Native"
armbian-config --cmd ACC001
~~~


~~~ bash title="Enable root login"
armbian-config --cmd ACC002
~~~


~~~ bash title="Disable password login"
armbian-config --cmd ACC003
~~~


~~~ bash title="Enable password login"
armbian-config --cmd ACC004
~~~


~~~ bash title="Disable Public key authentication login"
armbian-config --cmd ACC005
~~~


~~~ bash title="Enable Public key authentication login"
armbian-config --cmd ACC006
~~~


~~~ bash title="Disable OTP authentication"
armbian-config --cmd ACC007
~~~


~~~ bash title="Enable OTP authentication"
armbian-config --cmd ACC008
~~~


~~~ bash title="Generate new OTP authentication QR code"
armbian-config --cmd ACC009
~~~


~~~ bash title="Show OTP authentication QR code"
armbian-config --cmd ACC010
~~~


~~~ bash title="Disable last login banner"
armbian-config --cmd ACC011
~~~


~~~ bash title="Enable last login banner"
armbian-config --cmd ACC012
~~~













## Containerised


Sandboxed & containerised SSH server


<!--- section image START from tools/include/images/SSH001.png --->
![Containerised](/images/SSH001.png)
<!--- section image STOP from tools/include/images/SSH001.png --->


<!--- header START from tools/include/markdown/SSH001-header.md --->
Sandboxed & containerised SSH server allows ssh access without giving keys to the entire server. Giving ssh access via private key often means giving full access to the server. This container creates a limited and sandboxed environment that others can ssh into. The users only have access to the folders mapped and the processes running inside this container.
<!--- header STOP from tools/include/markdown/SSH001-header.md --->


~~~ bash title="Containerised"
armbian-config --cmd SSH001
~~~


<!--- footer START from tools/include/markdown/SSH001-footer.md --->
=== "Access to SSH server"

    - `ssh username@<your.IP> -p 2222`

=== "Directories"

    - Install directory: `/armbian/openssh-server`
    - Configuration directory: `/armbian/openssh-server/config`
    - Shared storage directory: `USER_DEFINED`

=== "View logs"

    ```sh
    docker logs -f openssh-server
    ```

<!--- footer STOP from tools/include/markdown/SSH001-footer.md --->


~~~ bash title="Remove sandboxed SSH server"
armbian-config --cmd SSH002
~~~


~~~ bash title="Purge sandboxed SSH server with data folder"
armbian-config --cmd SSH003
~~~



