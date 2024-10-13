# Welcome to the Armbian build framework documentation!

Overview:

### (ANSI) Logging

Log output is stored in `output/logs` and provided in a few different formats. ANSI coloring is applied to both the screen and the log files themselves.  
_Please_ add `SHARE_LOG=yes` to automatically upload logs to our paste service and provide us with the given url when reporting issues.  
That will allows us to check the logs on a web browser and keep to correct formatting.

## Command line syntax has changed

General CLI syntax: `./compile.sh PARAM=value OTHER_PARAM=other_value [<configfile> <configfile> ...] [<command>]`

- where `command` defaults to `build` if not specified; could also be `kernel-config` or `u-boot` etc...
- config file names _must not_ have the same name as a possible `<command>` (system will check & bomb if so)
- also: there is no more `default` config -- you have to be explicit
- also: there is no more `docker` config -- Docker is fully auto-managed now. The system will complain if you have one.
- parameters like `PARAM=value`, `<configfile>` or `<command>` can be applied in _any order_.

## No more `config-default.conf`, config file name needs to be specified in the command line

- No "default" config is auto-loaded anymore. Default config lead to unreproducible failing builds and was a source of
  confusion.
- The configs still go to the same place, `userpatches/config-xyz.conf` -- but the name has to be provided to the build system to,
  like `./compile.sh BOARD=xxx xyz`; otherwise works the same.

## Artifacts, cache, what the ...?

The `armbian/build` system is currently undergoing refactoring to improve its structure. Previously, the build system
was a single, very complex bash script that mixed the building of `.deb` packages with the creation of images.

This was reworked into a `1-to-N` image-to-artifact dependency tree; a certain image build will depend on N possible
"artifacts". Artifacts are either `.deb` packages, a `.tar` of multiple `.deb` packages, or a `rootfs.tar.zstd`. Each
artifact can be individually built, and has a specific name and a _version_.

Each artifact is also now **cached by default** using OCI storage at ghcr.io (GitHub Container Registry). To achieve
_consistent caching_, each artifact produces a version that includes _hashes_ of its composing files, variables,
patches, hooks, external git SHA1 references, etc. That way we can consistently check the remote OCI cache for previously-built
artifacts, and possibly save image builders from having to build heavy packages just to produce an image.

### TL;DR about artifacts and caching:

- `KERNEL_ONLY=yes` and `KERNEL_ONLY=no` are deprecated. Use the `kernel` CLI command instead.
- `ARTIFACT_IGNORE_CACHE=yes` can help with false positives. Please also report the problem, with a complete logfile.

## Automatic Docker/sudo launcher

- `compile.sh` will prefer to use Docker if it detects Docker is installed and working.
    - This handles Docker Desktop and Rancher Desktop (in Docker emulation mode) under macOS/Darwin, including Apple
      M1/M2.
    - You **don't need and actually can't have the old docker config file**.
- If Docker is not installed, it will try to use `sudo` to run the build as root.
- If you run directly as root, it will give a warning and asks to run without `sudo`.

## Kernel Git Trees: shallow vs full

During the build, depending on which local or remote caches are hit, it might be necessary to build the Linux Kernel from scratch.

The kernel's git repo is huge. Most build systems resort to fetching "shallow" trees directly from upstream git servers,
to save bandwidth. Unfortunately that creates immense extra CPU load on the git servers. To avoid this problem,
Armbian produces daily automated git tree exports cached in ghcr.io OCI repositories, and only uses `git fetch` to
update the relatively small new changes from the upstream git server.

There are two types of cached Kernel git trees:

- `full` is a complete git tree, including all of Torvald's `master` and all of the currently-supported `stable`
  branches.
    - `full` is very large download and requires a lot of disk space.
    - `full` is more useful over time and when building multiple different kernels on the same machine, like for CI
      servers or developer workstations.
- `shallow` is a shallow tree for a specific `stable` branch
    - `shallow` is a much smaller download and requires less disk space
    - `shallow` is appropriate for restricted devices like SBCs which will build a single kernel

**TL;DR: ** `KERNEL_GIT=full` or `KERNEL_GIT=shallow` or let the system decide for you.

## Consider forking before cloning the repo

Before cloning the repo, consider forking it first. This will allow you to make changes and submit pull requests.
You will need a GitHub account to do this;
see [GitHub's documentation](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) for more
information.
If you fork, make sure to keep your fork up-to-date with the main repo, by rebasing your fork.

## Some really confusing stuff still remains

This is (by far) not a complete list:

- wifi/other kernel drivers are still using pre-armbian-next code, and are very hard to work with. it is not only the
  contents are a mess, the way the whole thing works leads to more and more compounding work. To make it worse, family
  patches sometimes need to patch driver code, leading to a cycle of sadness for developers. We are still coming up with
  a plan to completely replace this lest most of us go insane.
- although "aggregation" has been rewritten in Python, it still mostly works using the legacy principle, by scanning
  directories and files in a very complex and error-prone way. This is a source of many bugs and confusion. We plan to
  replace this with pure extensions eventually.
- we have mostly working kernel headers (linux-headers pkg) for 5.10+ including some vendor kernels

## Multiple u-boot's for same board

We can build u-boot twice, using `UBOOT_TARGET_MAP`. Some example I did in https://github.com/armbian/build/blob/main/config/boards/odroidhc4.conf#L15-L20 may help.


