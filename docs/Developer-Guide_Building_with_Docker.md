# Building Armbian using Red Hat or CentOS

## How to build my own kernel?

First of all, it is important to notice that you will be able to build `kernel` and `uBoot`. The container method is not suitable for building full Armbian images (the full SD card image containing the userland packages).

This setup procedure was validated to work with Red Hat Enterprise Linux 7.

### Preparing your build host

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

### Preparing the Container

Docker will now check out the correct Ubuntu image to your build enviromnent and create a Docker **image** that will used as a template for your containers. This image template will be named `armbian_dev`:

        # docker build -t armbian_dev .

Give it some minutes, as it downloads a non-neglectible amount of data.

After your image is created (you can check it with `docker images` command), you can now spawn your container. However, by default RHEL provides only 20 GB of disk to your Container, which is not enough to a successful kernel or uBoot. So in order to overcome it, attach a volume that will bind to `/root/armbian/cache`, where the build data will be saved. In the below example, we will export the host `/mnt` to container in `/root/armbian/cache`:

        # docker run -v /mnt:/root/armbian/cache armbian_dev

**NOTICE**: It is possible that SELinux might block your access to `/root/armbian/cache` because it lies outside your container. You can fix it by either adding the correct SELinux context to your **host** cache directory, or, disabling SELinux.

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

Do **NOT** type exit - that will terminate your container. To leave your container running after starting `sshd`, just type Ctrl-P and Ctrl-P. Now you can ssh to your container.
