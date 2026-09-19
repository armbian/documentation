---
seo_title: "Armbian member storage: share images over SFTP"
description: "Public file storage for Armbian GitHub organization members: upload test images, packages and custom builds over SFTP and share them with a plain download link."
---

# Member storage

Members of the [Armbian organization](https://github.com/armbian) on GitHub get
public storage space at [storage.armbian.com](https://storage.armbian.com/). It
is made for easy sharing — test images, packages, customized builds — without
resorting to sketchy cloud or download services. SFTP is all it needs.

## Requirements

- You are a member of the [Armbian organization](https://github.com/armbian) on
  GitHub. Not a member yet? See
  [Roles and what they unlock](index.md#roles-and-what-they-unlock).
- You have an [SSH key added to your GitHub account](https://github.com/settings/keys).
  DSA keys are not accepted.
- You have a tool that speaks
  [SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol), such as
  `sftp`, `scp` or a graphical client.

## How to connect

| Setting | Value |
| :------ | :---- |
| Host | `storage.armbian.com` |
| Port | `23` |
| Protocol | SFTP |
| User | your GitHub username (**case sensitive**) |

Authentication uses the SSH keys from your GitHub account, so connect with the
matching private key:

```bash
sftp -i <path-to-private-key> -P 23 <GitHubUser>@storage.armbian.com
```

!!! warning "Use port 23, not 22"
    Repeatedly failing to connect to port 22 will likely trigger fail2ban and
    lock you out.

A real session looks like this:

```console
$ sftp -i keys/evilolaf_github.key -P 23 EvilOlaf@storage.armbian.com
Enter passphrase for key 'keys/evilolaf_github.key':
Connected to storage.armbian.com.
sftp> cd EvilOlaf/
sftp> dir
10M   asdf
sftp>
```

To avoid typing the options every time, add a host entry to `~/.ssh/config`:

```text
Host armbian-storage
    HostName storage.armbian.com
    Port 23
    User <GitHubUser>
    IdentityFile <path-to-private-key>
```

After that, `sftp armbian-storage` is enough.

## Sharing files

Uploads go into the directory named after your GitHub username. Everything in
it is publicly browsable and downloadable at:

```text
https://storage.armbian.com/<GitHubUser>/
```

For example, the session above serves its files from
<https://storage.armbian.com/EvilOlaf/>. Hand out that link, or the link to a
single file, and you are done.

!!! warning "Everything you upload is public"
    There is no private space. Do not upload secrets, keys, credentials or
    anything else you would not post in the open.

## Good to know

- The total quota across all users is currently 5T.
- Account creation can take up to 24 hours after you acquire organization
  membership.
- If your organization membership is revoked, your account is locked
  automatically.
