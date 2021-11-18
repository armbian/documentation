# Building with Docker

## Officially supported and tested method for building with Docker

This method works for building u-boot and kernel packages as well as building full OS images.
Note! 
To write fresh-builded image directly to sdcard or other block device you have to enable 
Docker run in `privileged` mode.
Uncomment line `DOCKER_FLAGS+=(--privileged)` in file `userpatches\config-docker.conf` or your own docker-config file.

Building additional packages (`EXTERNAL_NEW`) is not supported.

### Requirements

- x86/x64/aarch64/armhf Linux host that supports running a recent Docker daemon. Refer to [Docker documentation](https://docs.docker.com/) for details.
- Docker version 17.06 CE or newer. 
- Enough free disk space on the storage used for Docker containers and named volumes. Named volumes path can be changed using standard Docker utilites,
  refer to Docker documentation for details.
  
Installation (https://docs.docker.com/engine/install/)

### Details

There are 3 options to start build process:

1. By passing configuration file name (`config-<conf_name>.conf`), stored in `userpatches` directory, as an argument:
```
./compile.sh docker <conf_name>
```
2. By passing addtional line arguments to `compile.sh` after `docker`:
```
./compile.sh docker KERNEL_ONLY=yes BOARD=cubietruck BRANCH=current KERNEL_CONFIGURE=yes
```
3. Interactively run inside docker container
```
./compile.sh docker-shell BOARD=rockpi-4a BRANCH=edge RELEASE=focal
```

The process creates and runs a named Docker container `armbian` with two named volumes `armbian-cache` and `armbian-ccache`,
and mount local directories `output` and `userpatches`.

1 and 2 docker modes uses same as no docker, but runs in separated builder environment, with minimal intervention to base system.

Dockerfile of container placed in `userpatches` directory, all container-related tunes can be changed
in `userpatches/config-docker.conf` file. Templates of both files located in `config/templates` directory.

### docker-shell interactive mode

Interactive mode of a docker usable when you need more than "just make an image". You may look to u-boot or
kernel sources before and after applying patches, investigate compilation errors, and so on.

And you can manual run separate steps of build process.

First, start docker-shell on a build system itself:
```
@droid:~/armbian$ ./compile.sh docker-shell RELEASE=buster BOARD=rockpi-4a BRANCH=edge
```
There `RELEASE=buster BOARD=rockpi-4a BRANCH=edge` just passed into shell and will be set into
envirounment variables. 

Then, we can simply start build image:
```
root@75ec76203b65:~/armbian# ./compile.sh
```
Or, you can run any function defined in the compile.sh script.

For example, to compile the U-Boot, prepare the environment first with:
```
./compile.sh default prepare_host compile_sunxi_tools install_rkbin_tools
```
Then build U-Boot for example:
```
./compile.sh default compile_uboot
```
To compile only the source code as it is without patching, run:
```
./compile.sh default COMPILE_ONLY=yes compile_uboot
```
Note that you must enter docker-shell after a docker build, which will
download all the required toolchains and sourcecodes first.

you can set `KERNEL_ONLY=yes` to build atf&u-boot&kernel only.
