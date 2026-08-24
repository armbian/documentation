---
seo_title: "Armbian build output & diagnostics switches"
description: "Diagnostics for Armbian builds: SHARE_LOG to upload full build logs, SHOW_LOG to stream command output live, and SHOW_DEBUG for verbose messages."
---

# Output & diagnostics

Logs and diagnostic output for a build.

#### SHARE_LOG

`string`

- `yes`
- `no` (default)

Automatically upload the full build log to one of Armbian's paste servers at the end of the build, and print the URL. Include it when reporting a build issue.

```sh
./compile.sh SHARE_LOG=yes
```

#### SHOW_LOG

`string` · default: `yes` when attached to a terminal

Stream command output to the terminal live as the build runs, instead of only writing it to `output/logs`.

#### SHOW_DEBUG

`string` · default: `no`

Emit verbose debug-level messages. Automatically enabled when `DEBUG=yes`.
