# Build commands

### kernel

Builds kernel and device tree (where applicable) and places it to the `output/debs`

Usage:
```bash
./compile.sh kernel BOARD=nanopi-r5c BRANCH=edge 
```

### dts-check

Validate dts files and improve board & patch development overall.

This option validates the dts/dtb file for the selected board against the device tree bindings and outputs the validation logs to the user. It can be used when adding a new board, developing or improving a dts file.

Usage:
```bash
./compile.sh dts-check BOARD=nanopi-r5c BRANCH=edge 
```
### inventory-boards

Outputs a one-board-per-line CSV inventory of boards.

Sets `TARGETS_FILE` to something that doesn't exist, so the `default-targets.yaml` is used (so same list for everyone, save for userpatched-boards)

Usage:
```bash
./compile.sh inventory-boards
```
Outputs /info/boards-inventory.csv

### kernel-dtb

Builds only DTB and outputs full preprocessed dts source

Outputs preprocessed DTS source for the board in question to `output/`
also outputs the same preprocessed DTS source, ran through `dtc` with input and output DTS formats for "normalized" comparisons

Usage:
```bash
./compile.sh kernel-dtb BOARD=xxxxx BRANCH=edge
```

### rewrite-uboot-patches

Prepares git, applies patches to git, and rewrites them back from git
same as kernel, it does git archeology for mbox-less patches, etc.

- uboot-patches-to-git alias is also added, but my guess is that the rewrite is more useful.
- refactor a common config function for both kernel and uboot.

Usage:
```bash
./compile.sh rewrite-uboot-patches BOARD=xxxx BRANCH=edge 
```

### targets

Generates output/info/git_sources.json file containing URL, branch, and commit hash combo.

The easiest way to generate file for all devices is to run `./compile.sh targets`. Then, at the time of release, we will copy the output/info/git_sources.json file to config/sources/git_sources.json. Once the file is copied, the hash information from the file will be used to fetch resources for git repositories where branches are specified instead of tags or commits.

Usage:
```bash
./compile.sh targets
```