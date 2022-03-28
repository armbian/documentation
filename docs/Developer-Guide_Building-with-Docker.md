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

1\. By passing configuration file name (`config-<conf_name>.conf`), stored in `userpatches` directory, as an argument:
```
./compile.sh docker <conf_name>
```
2\. By passing addtional line arguments to `compile.sh` after `docker`:
```
./compile.sh docker KERNEL_ONLY=yes BOARD=cubietruck BRANCH=current KERNEL_CONFIGURE=yes
```
3\. Interactively run inside docker container
```
./compile.sh docker-shell BOARD=rockpi-4a BRANCH=edge RELEASE=focal
```

The process creates and runs a named Docker container `armbian` with two named volumes `armbian-cache` and `armbian-ccache`,
and mounts local directories `output` and `userpatches`.

Options 1 and 2 compile the same as without Docker but in separate environment to prevent changes to the base system.

The dockerfile of the created container is placed in `userpatches` directory, and all container-related options can be changed
in `userpatches/config-docker.conf` file. Templates of both files are located in the `config/templates` directory.

### docker-shell interactive mode

The docker-shell interactive mode is useful for when you need to do more than just "make an image." This mode allows you to edit
U-Boot and kernel sources before and after applying patches, investigate compilation errors, and so on.

This mode also allows you to manually run individual steps of the build process.

First, start docker-shell on the host build system:
```
@droid:~/armbian$ ./compile.sh docker-shell RELEASE=buster BOARD=rockpi-4a BRANCH=edge
```
From there, `RELEASE=buster BOARD=rockpi-4a BRANCH=edge` are passed into shell and will be set into
envirounment variables. 

Next, we can simply start building an image:
```
root@75ec76203b65:~/armbian# ./compile.sh
```
Alternatively, you can run any function defined in the compile.sh script.

For example, to compile U-Boot, prepare the environment with:
```
./compile.sh default prepare_host compile_sunxi_tools install_rkbin_tools
```
Then, build U-Boot:
```
./compile.sh default compile_uboot
```
To compile only the source code as it is without patching or modifications, run:
```
./compile.sh default COMPILE_ONLY=yes compile_uboot
```
Note that you must enter docker-shell after a docker build, as you must
download all of the required toolchains and sourcecodes beforehand.
