# Migration from Bananian to Armbian

*NOTE: THIS IS DEPRECATED*

While technically possible to do an **in-place** upgrade/crossgrade from latest Bananian release (or similar SBC distros) to Armbian currently there exists no tool helping with this and most probably will never exist. At the bottom is explained where to find ressources that help with a manual in-place upgrade but we start with outlining the problems and our recommendations:

## The challenges:

### SD cards wear out after a certain amount of data being written to

Only reasonable base for an migration to Armbian would be an updated Bananian installation (Bananian 16.04, already Debian Jessie based, Nico's 4.4 kernel). In case Bananian users are still on version 15.04 or earlier they need to upgrade to a more recent Bananian version anyway to move Bananian's base to Jessie. Such `apt-get dist-upgrade` tasks come with heavy write activity. Especially when planning a dist-upgrade to Stretch later this amount of random write activity on older/smaller SD cards might kill them. If the SD card is not brand new it's highly recommended to create a clone/backup first prior to every upgrade step. If the SD card is really old please be prepared that it might not survive an `apt-get dist-upgrade`.

### All hardware will die eventually

A lot of Bananian installations today have been running 24/7 for 3 years or even longer. While these little SBC are well suited for light-weight server tasks, the hardware can't exactly be called 'server grade'. Please keep this in mind if you're about to spend some time on a manual migration attempt that once you're done maybe your hardware will stop working few weeks/months later if it already runs +24 months.

### Hardware up to the task?

The vast majority of [boards Bananian runs on](https://www.bananian.org/hardware) is based on Allwinner's dual core A20 SoC which was a nice improvement over the first single-core Raspberry Pis few years ago but is pretty slow by today's standards. An awful lot of users (us Armbians **all** included) were excited by A20's 'native SATA' capabilities few years ago just to realize after purchase when using SATA attached storage that it's awfully slow and most probably the slowest 'native' SATA implementation existing (please wake up if in doubt and educate yourself [here](https://forum.armbian.com/topic/1925-some-storage-benchmarks-on-sbcs/&do=findComment&comment=34192), [here](http://linux-sunxi.org/Sunxi_devices_as_NAS#Influence_of_the_chosen_OS_image_on_NAS_performance) or [here](https://forum.openmediavault.org/index.php/Thread/19871-Which-energy-efficient-ARM-platform-to-choose/?postID=154980#post154980). Important: combining Allwinner's crappy SATA implementation with port multipliers [is always wrong](https://github.com/armbian/build/issues/548#issuecomment-332918004)).

At the time of this writing (Oct 2017) Armbian supports +25 other ARM boards that show between 2 and 6 times better CPU performance than A20 devices. +20 boards we support show better network performance (A20 Gigabit Ethernet is not fully capable of 940 Mbits/sec in both directions). +15 boards support 2GB DRAM (a few even more just recently). And if you don't need Gigabit Ethernet you can get a new and fully supported board still better suited for light-weight server tasks than any Banana Pi for as less as $11 shipping included (check [this overview](https://forum.armbian.com/topic/1351-h3-board-buyers-guide/&do=findComment&comment=28169) please).

While this diversity of ARM species might be confusing the good news is: When Armbian is running on them they all behave the same.

## Alternatives to an in-place migration:

### Continue on same hardware but prevent SD card hassles

Especially if you run since years off the same SD card please be prepared that it might not survive an `apt-get dist-upgrade` and similar upgrade/crossgrade tasks. It's **strongly** recommended to clone/backup your card prior to every necessary upgrade step. Since this is time consuming and just a measure to prepare for what will happen in the future anyway (your SD card failing eventually -- if you're lucky immediately, if you're out of luck it will corrupt a lot of data dying slowly) a great idea is to buy a new one **now**. Please see [our community's collection of SD card performance tests](https://forum.armbian.com/topic/954-sd-card-performance/) and especially the 3 links at the top dealing with reliability concerns.

Once you bought a new, fast and hopefully reliable SD card, you should [test it according to our documentation](https://docs.armbian.com/User-Guide_Getting-Started/#how-to-prepare-a-sd-card), then burn a fresh Armbian image on it and manually transfer data and settings from your Bananian installation. This way you preserve your current settings/data on the old Bananian SD card saving you also a lot of time/efforts to clone/backup stuff.

**Important note:** if you're interested in NAS use cases you could also choose an OMV image from official [download location](https://sourceforge.net/projects/openmediavault/files/) (all the ARM board images are now based on Armbian, funnily even the ones for Raspberry Pi)

### Replacing the hardware

If your Bananian installation has been running for years, you better think about evaluating new hardware now. As explained above, A20's SATA implementation is [awfully slow](https://forum.armbian.com/topic/1925-some-storage-benchmarks-on-sbcs/&do=findComment&comment=34192) compared to good SATA implementations (Espressobin, Clearfog, Helios4) or even recent USB3 solutions, also Banana Pis can not saturate Gigabit Ethernet. It's almost 2018 now and we can choose from a variety of energy efficient boards more suited for the job.

[My](https://forum.armbian.com/profile/7-tkaiser/) personal strategy was turning the various A20 servers into backup devices now receiving btrfs snapshots from better suited ARM servers in the meantime. New installation on new board, carefully migrating settings from Bananas, Cubietrucks or Lime boards to new server, testing, testing, testing, new installation on A20 device, setting up btrfs send|receive, testing, testing, testing, done.

## In-place migration tipps:

Since there is no easy migration tool you can only rely on contents collected below https://github.com/armbian/build/issues/648 -- if you read carefully through we had some hope experienced Bananian users would be volunteering in providing an in-place upgrade tool from Bananian to Armbian but unfortunately to no avail. So 6 months after the problem came to our attention we're now providing this document to help those affected taking the right decisions. Still no need to hurry, Bananian receives bug and security fixes for another 6 months so take your time and evaluate carefully which way to choose.

Trivia: Anyone understanding german **will** enjoy Nico's refreshing [Rise and Fall of Bananian Linux](https://frank-mankel.de/kategorien/36-froscon/288-froscon-12) talk.
