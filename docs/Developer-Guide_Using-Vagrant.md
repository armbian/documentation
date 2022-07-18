# Quick Start with Vagrant

## Vagrant HOST Steps

The following steps are performed on the *host* that runs Vagrant.

### Installing Vagrant and Downloading Armbian

First, you'll need to [install Vagrant](https://www.vagrantup.com/downloads.html) on your host box. Then you have to choose if you want to run Virtualbox or Libvirt.

#### Virtualbox

[Install Virtualbox](https://www.virtualbox.org/manual/UserManual.html#installation), then you'll need to install a plug-in that will enable us to resize the primary storage device. Without it, the default Vagrant images are too small to build Armbian.

	vagrant plugin install vagrant-disksize

#### Libvirt

[Installing libvirt](https://libvirt.org/downloads.html) is a little bit more complex as you have to install an hypervisor too (like KVM/Qemu but others are available). Discussing about which one choosing and how to install it is out of scope. Once you have libvirt and an hypervisor installed, you'll need [vagrant-libvirt](https://github.com/vagrant-libvirt/vagrant-libvirt/blob/master/README.md#installation).
Finally, you need to tell vagrant to use libvirt and not default to Virtualbox.

	export VAGRANT_DEFAULT_PROVIDER=libvirt

#### Common steps

Now we'll need to [install git](https://git-scm.com/downloads) and clone the Armbian repo. While this might seem obvious, we rely on it being there when we use Vagrant to bring up our guest-build box.

	# Clone the project.  
	git clone --depth 1 https://github.com/armbian/build  

	# Make the Vagrant box available. This might take a while but only needs to be done once.  
	vagrant box add generic/ubuntu2204
	
	# If the box gets updated by the folks at HashiCorp, we'll want to update our copy too.  
	# This only needs done once and a while.  
	vagrant box update  

### Armbian Directory Structure

Before we bring up the box, take note of the [directory structure]( https://docs.armbian.com/Developer-Guide_Build-Process/#directory-structure) used by the Armbian build tool. When you read the Vagrantfile (which is in the build/config/templates directory)  you'll see that Vagrant will mount local *output* and *userpatches* directories. This is helpful as it enables you to easily retrieve your images from the host once built, and [customize the build process](https://docs.armbian.com/Developer-Guide_User-Configurations/).

### Creating the Vagrant Guest Box Used to Build 
Let's bring the box up. This might take a minute or two depending on your bandwidth and hardware.

	# We have to be in the same directory as the Vagrant file, which is in the build/config/templates directory.   
	
	cd build/config/templates  
	
	#  Note that you can edit the Vagrant  file to specify the number of cpus and amount of memory you want Vagrant to use.  
	
	# And now we simply let vagrant create our box and bring it up. 
	
	vagrant up  

	# When the box has been installed we can get access via ssh.
	# (No need for passwords, Vagrant installs the keys we'll need.)
	vagrant ssh  

### Shut down, clean up

Wrap up your vagrant box when no longer needed (log out of the guest before running these commands on the *host* system):

	# Shutdown, but leave the box around for more building at a later time:  
	vagrant halt  

	# Trash the box and remove all the related storage devices.  
	vagrant destroy  

## Important note

It is strongly recommended to halt and restart the Vagrant box after building an image. Check [this](https://github.com/armbian/build/issues/751) issue for details.

## Vagrant GUEST Steps

The following steps are all run on the *guest* Vagrant created for us.

Once it's finally up and you're logged in, it works much like any of the other install methods (NOTE: again, these commands are run on the *guest* box).

	# Let's get building!  
	cd armbian  
	sudo ./compile.sh  

## More Vagrant HOST Steps

Moved [here](Developer-Guide_Using-Vagrant.md#shut-down-clean-up).
