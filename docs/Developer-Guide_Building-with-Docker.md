# Officially supported and tested method for building with Docker

This method works for building u-boot and kernel packages as well as building full OS images.

Building additional packages (`EXTERNAL_NEW`) is not supported.

## Requirements

- x86/x64 Linux host that supports running a recent Docker daemon. Refer to [Docker documentation](https://docs.docker.com/) for details.
- Docker version 17.06 CE or newer. Installation on Ubuntu Bionic:

		apt-key adv --keyserver pool.sks-keyservers.net --recv-keys 0EBFCD88 
		echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" > /etc/apt/sources.list.d/docker.list
		apt update
		apt install docker-ce

- Enough free disk space on the storage used for Docker containers and named volumes. Named volumes path can be changed using standard Docker utilites,
  refer to Docker documentation for details.

## Details

There are 2 options to start build process:

1. By passing configuration file name (`config-<conf_name>.conf`), stored in `userpatches` directory, as an argument:

		# ./compile.sh docker <conf_name>

2. By passing addtional line arguments to `compile.sh` after `docker`:

		# ./compile.sh docker KERNEL_ONLY=yes BOARD=cubietruck BRANCH=current KERNEL_CONFIGURE=yes

The process creates and runs a named Docker container `armbian` with 2 named volumes `armbian-cache` and `armbian-ccache`,
and mount local directories `output` and `userpatches`.

# Creating and running Docker container manually

NOTE: These methods are not supported by Armbian developers. Use them at your own risk.

### Example: Building Armbian using Red Hat or CentOS

Tested by [@rfrht](https://github.com/rfrht)

First of all, it is important to notice that you will be able to build `kernel` and `u-boot` packages. The container method is not suitable for building full Armbian images (the full SD card image containing the userland packages).

This setup procedure was validated to work with Red Hat Enterprise Linux 7.

#### Preparing your build host

In order to be able to run Docker containers, if you have not done so, just install the Docker package:

        # yum install -y docker

By default, the `docker` service is not started upon system reboot. If you wish to do so:

        # systemctl enable docker

Ensure that you have the `docker` service running:

        # systemctl start docker`

Next step, chdir to a directory where you will be checking out the Armbian `build` repository. I use `/usr/src`. And then, check out using git (with shallow tree, using `--depth 1`, in order to speed up the process):

        # cd /usr/src
        # git clone --depth 1 https://github.com/armbian/build

And in order to not mistake the newly created `build` directory, I rename it to `build-armbian`. `cd` to the directory:

        # mv build build-armbian
        # cd build-armbian

#### Preparing the Container

Our Build toolchain provides a scripted way to create a container and run the container. Run:

        # ./compile.sh docker

Give it some minutes, as it downloads a non-neglectible amount of data.

After your image is created (named `armbian`), it will automatically spawn the Armbian build container.

**NOTICE**: In some cases, it is possible that SELinux might block your access to `/root/armbian/cache` temporary build directory. You can fix it by either adding the correct SELinux context to your **host** cache directory, or, disabling SELinux.

Get acquainted with the Build system.

If you want to get a shell in the container, skipping the compile script, you can also run:

        # docker run -dit --entrypoint=/bin/bash -v /mnt:/root/armbian/cache armbian_dev

The above command will start the container with a shell. To get the shell session:

        # docker attach <UUID of your container, returned in the above command>

If you want to run SSH in your container, log in and install the `ssh` package:

        # apt-get install -y ssh

Now, define a password and prepare the settings so you `sshd` can run and you can log in as root:

        # passwd
        # sed -i -e 's/PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
        # mkdir /var/run/sshd
        # chmod 0755 /var/run/sshd

And finally start `sshd`:

        # /usr/sbin/sshd

**Do NOT** type `exit` - that will stop your container. To leave your container running after starting `sshd`, just type `<Ctrl-P>` and `<Ctrl-Q>`. Now you can ssh to your container.
