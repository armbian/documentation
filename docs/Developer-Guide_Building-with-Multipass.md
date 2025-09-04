# Building with Multipass

In order to build an Armbian image from scratch, whether for development purposes or to [apply user customizations](https://docs.armbian.com/Developer-Guide_User-Configurations/) on top of a base image, a build environment is required. Per the Armbian documentation, Ubuntu 24.04 is [the officially supported](https://docs.armbian.com/Developer-Guide_Build-Preparation/) build platform.

[Multipass](https://multipass.run/) that is designed for quick and painless provisioning of Ubuntu VMs.


### Creating a VM and preparing for build

Multipass is [available](https://multipass.run/install) for macOS, Windows and Linux platforms.

Once you have multipass installed, a Jammy (22.04) instance with 4 CPUs, 4GB of RAM and 25GB of space available can be provisioned with a single command:

```bash
multipass launch --cpus 4 --disk 25G --mem 4G --name jammy
```

### Clone the build repo

You can run commands direct on the instance to clone the build repo:

```bash
multipass exec jammy -- bash -c "git clone --depth 1 https://github.com/armbian/build" 
```

### Use an instance
Then you can get a shell to the instance and run the build as needed:

```bash
C:\> multipass shell armbian
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.4.0-48-generic x86_64)
Last login: Tue Jan 30 12:23:08 2024 from 172.22.111.1
# Let's get building!  
ubuntu@armbian:~$ cd build
ubuntu@armbian:~/build$ ./compile.sh BOARD=orangepizero ... etc
```

### Share data with an instance

The recommended way to share data between your host and an instance with Multipass is the command:mount
```bash
multipass mount /my/dir jammy
multipass info jammy
```

Mounts:         /my/dir => /my/dir

From this point on will be available inside the instance./my/dir
