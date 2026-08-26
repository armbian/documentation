---
seo_title: "Armbian build commands for compile.sh"
description: "Commands for the Armbian build framework's compile.sh: build an image, flash it, manage the container, and advanced kernel, patch and board-development tooling."
---

# Build commands

The build framework is driven by a single script, `compile.sh`:

```bash
./compile.sh PARAM=value OTHER_PARAM=value [<configfile> ...] [<command>]
```

- `<command>` defaults to `build` when omitted; the other commands are listed below.
- Parameters (`PARAM=value`, see [Build Switches](/build-framework/switches/)), config files and the command may be given in **any order**.
- There is **no default config file** — if you keep your settings in `userpatches/config-<name>.conf`, name it explicitly on the command line (`./compile.sh BOARD=... <name>`). A config file must not share a name with a command.

Commands are grouped by audience:

| Page | Commands |
|---|---|
| [Basic commands](basic.md) | Set up the host and build a full image, kernel or bootloader — including their interactive config |
| [Advanced commands](advanced.md) | Container management, flashing, patch creation and rewriting, device-tree checks, and release and inspection tooling |
