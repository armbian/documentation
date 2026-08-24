---
seo_title: "Armbian storage setup: eMMC, ZFS, NFS"
description: "Install Armbian to eMMC, SATA or NVMe and set up ZFS, NFS and a read-only root filesystem on single-board computers using armbian-config."
comments: true
---

# Storage


Install to internal media, ZFS, NFS, read-only rootfs

## Install


Install the running system to internal media (eMMC/NVMe/SATA/USB/UFS, or Windows dual-boot)


<!--- header START from tools/include/markdown/STO001-header.md --->
- Clones your current live OS installation
- Keeps your settings, configuration, installed packages, and user data
- Essentially “transfer my existing system to internal/external storage”

Use this option to **transfer your current live Armbian system** to another storage device (eMMC, SSD, USB, etc.).  This copies your existing installation exactly as it is — including settings, installed packages, and user data.

<!--- header STOP from tools/include/markdown/STO001-header.md --->


~~~ bash title="Install"
armbian-config --cmd STO001
~~~


## Download and flash


Download a fresh, official Armbian OS image and write it to a device


<!--- section image START from tools/include/images/FLASH1.png --->
![Download and flash](/images/FLASH1.png)
<!--- section image STOP from tools/include/images/FLASH1.png --->


<!--- header START from tools/include/markdown/FLASH1-header.md --->
What can this tool do?

- Install Armbian onto internal **eMMC, SSD, or other storage**
- Create **bootable SD cards or USB drives** for any supported board
- Recover a system by **re-flashing a clean image**
- Switch between different **OS variants, kernel branches, or preinstalled applications**
- Accelerate development with **fast, repeatable deployments** for testing and automation

<!--- header STOP from tools/include/markdown/FLASH1-header.md --->


~~~ bash title="Download and flash"
armbian-config --cmd FLASH1
~~~


<!--- footer START from tools/include/markdown/FLASH1-footer.md --->

<!--- footer STOP from tools/include/markdown/FLASH1-footer.md --->


~~~ bash title="Remove cached images"
armbian-config --cmd FLASH2
~~~



## Read Only FS


Enable read only filesystem


<!--- header START from tools/include/markdown/ROO001-header.md --->
Read-only filesystem is enabled using overlayroot, a utility that places a temporary writable layer over the system root filesystem. Changes made during runtime are redirected into RAM or an alternative writable storage, while the underlying system remains untouched. This ensures that after a reboot, the system returns to a clean original state. It's ideal for kiosks, appliances, SD card-based systems, and scenarios where long-term filesystem durability and recovery are critical.

<!--- header STOP from tools/include/markdown/ROO001-header.md --->


~~~ bash title="Read Only FS"
armbian-config --cmd ROO001
~~~


~~~ bash title="Disable read only filesystem"
armbian-config --cmd ROO002
~~~



## NFS


Enable Network filesystem (NFS) support


~~~ bash title="NFS"
armbian-config --cmd NETF01
~~~


~~~ bash title="Disable Network filesystem (NFS) support"
armbian-config --cmd NETF02
~~~



#### NFS server


Enable network filesystem (NFS) daemon


~~~ bash title="NFS server"
armbian-config --cmd NETF04
~~~


~~~ bash title="Configure network filesystem (NFS) daemon"
armbian-config --cmd NETF05
~~~


~~~ bash title="Remove network filesystem (NFS) daemon"
armbian-config --cmd NETF06
~~~


~~~ bash title="Show network filesystem (NFS) daemon clients"
armbian-config --cmd NETF07
~~~





#### Find NFS servers


Find NFS servers in subnet and mount shares


~~~ bash title="Find NFS servers"
armbian-config --cmd NETF09
~~~


~~~ bash title="Show and manage NFS mounts"
armbian-config --cmd NETF10
~~~



## ZFS


ZFS filesystem - enable support


<!--- section image START from tools/include/images/ZFS001.png --->
![ZFS](/images/ZFS001.png)
<!--- section image STOP from tools/include/images/ZFS001.png --->


<!--- header START from tools/include/markdown/ZFS001-header.md --->
ZFS is an advanced, high-performance file system and volume manager designed for data integrity, scalability, and ease of use. It offers features like copy-on-write snapshots, native compression, data deduplication, automatic repair, and efficient storage pooling. Originally developed by Sun Microsystems, ZFS is ideal for handling large amounts of data reliably with minimal maintenance.

When enabling ZFS support, Armbian checks if the running kernel can support ZFS, installs matching kernel headers if necessary, and builds the ZFS DKMS (Dynamic Kernel Module Support) module automatically.

=== "ARC Cache Tuning"

    The **ARC (Adaptive Replacement Cache)** is ZFS's intelligent caching system.

    **Recommended Settings:**
    
    - **ARC Min:** 1/8 of RAM (minimum cache size)
    - **ARC Max:** 1/2 of RAM (maximum cache size)

    For memory-constrained ARM devices (1-2 GB RAM):
    
    - Consider limiting ARC to 256-512 MB to leave memory for applications
    - ARC Max = 0 means "use all available RAM" (may not be ideal for small systems)

    **Impact:**
    
    - Higher ARC = better read performance for frequently accessed data
    - Too high ARC can cause system swapping and degraded performance

=== "Dirty Data Tuning"

    **Dirty data** is modified data waiting to be written to disk.

    **Recommended Setting:**
    
    - **4% of RAM** (or 4% of ARC size, whichever is smaller)

    **Impact:**
    
    - Higher values = better write performance, more data loss risk on power failure
    - Lower values = safer data, more frequent disk writes

=== "TXG Timeout Tuning"

    **TXG (Transaction Group)** controls how often ZFS writes changes to disk.

    **Recommended Setting:**
    
    - **5 seconds** (default)

    **Range:** 1-30 seconds

    **Impact:**
    
    - Lower (1-3s): Better data safety, more disk writes, lower performance
    - Higher (10-30s): Better performance, more data loss risk on power failure

=== "Compression"

    ZFS compression is transparent and can actually **improve performance** by reducing I/O.

    **Options:**
    
    - **lz4**: Fast, good compression (recommended for most)
    - **zstd**: Better compression ratio, slightly slower CPU usage
    - **gzip**: Maximum compression, slowest
    - **off**: Disable compression

    **Note:** Compression setting only affects **new** datasets. Existing datasets keep their compression setting.

=== "Applying Configuration"

    Configuration is saved to `/etc/modprobe.d/zfs.conf` and requires reloading the ZFS module:

    ```bash
    # Option 1: Reboot (simplest)
    reboot

    # Option 2: Reload module (requires exporting all ZFS pools)
    zpool export -a
    rmmod zfs
    modprobe zfs
    ```

=== "Reset to Defaults"

    The tuning interface includes a "Reset to Defaults" option that:

    - Removes custom configuration from `/etc/modprobe.d/zfs.conf`
    - Resets all parameters to ZFS defaults
    - Requires module reload to take effect

=== "Pool Import"

    ZFS pools can be imported when they are not currently mounted. This is useful when:

    - Moving pools between systems
    - Booting from a different system with ZFS pools present
    - Pools were exported and need to be re-imported

    **Import Options:**

    - **Scan:** Lists all available pools that can be imported
    - **Import with original mount points:** Pool datasets mount at their configured locations
    - **Import with alternate mount point:** Pool datasets mount under a custom root directory

    **Force Import:**

    The import function uses `-f` flag to force import, which handles:

    - HostID mismatches between systems
    - Pool state issues
    - Active pools on other systems (use with caution)

    **Alternate Mount Point:**

    When importing with an alternate root (`altroot`):

    - Datasets mount under the specified path (e.g., `/mnt/pool`)
    - Original mount point configuration is preserved
    - Useful for temporary access or recovery scenarios

    **Note:** Default behavior is to use the pool's original mount points for maximum compatibility.

<!--- header STOP from tools/include/markdown/ZFS001-header.md --->


~~~ bash title="ZFS"
armbian-config --cmd ZFS001
~~~


<!--- footer START from tools/include/markdown/ZFS001-footer.md --->
##### Key Features

###### Data Integrity
- **Copy-on-Write (CoW):** Prevents data corruption by never overwriting live data.
- **Checksumming:** Detects and corrects silent data corruption (bit rot).

###### Storage Management
- **Pooled Storage:** Eliminates the need for traditional partitions; all storage is managed dynamically.
- **Snapshots & Clones:** Creates instant backups without using extra storage.

###### Performance & Scalability
- **Efficient Compression & Deduplication:** Reduces storage usage without performance loss.
- **Dynamic Striping & Caching:** Distributes data across multiple disks for optimized read/write speeds.

###### Advanced Security
- **Native Encryption:** Supports dataset-level encryption for secure data storage.
- **RAID-Z:** A superior RAID alternative that prevents write-hole issues.


<!--- footer STOP from tools/include/markdown/ZFS001-footer.md --->


~~~ bash title="ZFS filesystem - remove support"
armbian-config --cmd ZFS002
~~~


~~~ bash title="Tune ZFS"
armbian-config --cmd ZFS003
~~~


~~~ bash title="Import ZFS Pool"
armbian-config --cmd ZFS004
~~~





## Memory


Memory management - enable features


<!--- section image START from tools/include/images/MEM001.png --->
![Memory](/images/MEM001.png)
<!--- section image STOP from tools/include/images/MEM001.png --->


<!--- header START from tools/include/markdown/MEM001-header.md --->
ZRAM is a Linux kernel module that creates compressed RAM-based block devices. It extends available memory by compressing pages and storing them in RAM, giving you more usable memory at the cost of some CPU overhead. On devices with limited RAM, ZRAM can significantly improve system responsiveness and prevent out-of-memory conditions.

When enabling memory management, Armbian installs the `zram-config` package if not already present, enables the `armbian-zram-config` service, and configures optimal swappiness settings for ZRAM-based swapping.

*Key Features*

- **Memory Compression**: Transparent ZRAM-based swap that extends available memory without application changes
- **Parallel Compression**: Multiple ZRAM devices utilize all CPU cores for maximum throughput
- **Algorithm Choice**: Select optimal compression for your hardware (lzo, lz4, zstd, lzo-rle)
- **Adaptive Swapping**: Swappiness tuned for ZRAM's in-RAM characteristics
- **Memory Overcommitment**: Support for swap sizes larger than physical RAM
- **Safe Defaults**: Sensible defaults based on your system's memory size

---

Perfect for **ARM-based SBCs**, **small form-factor PCs**, and **servers** where physical RAM is limited and disk-based swap would cause excessive I/O.

<!--- header STOP from tools/include/markdown/MEM001-header.md --->


~~~ bash title="Memory"
armbian-config --cmd MEM001
~~~


<!--- footer START from tools/include/markdown/MEM001-footer.md --->
=== "Recommended Settings"

    Settings are automatically selected based on system memory:

    | System | ZRAM Size | Memory Limit | Swappiness |
    |--------|-----------|--------------|------------|
    | < 4 GB RAM | 50% | 50% | 100 |
    | 4+ GB RAM | 25% | 25% | 80 |

    - **Max Devices**: Set to CPU core count (capped at 8)
    - **Algorithm**: lzo (best for ARM), lz4 (fast on x86), zstd (best ratio, slower)

=== "Tuning Parameters"

    - **ZRAM Percentage** (10-300%): Swap space relative to physical RAM. With 50% on a 2GB system you get 1GB of swap, but compression (2:1 to 3:1) effectively holds 2-3GB
    - **Memory Limit** (10-100%): Prevents ZRAM from consuming too much physical RAM. Should generally match ZRAM percentage
    - **Swappiness** (1-100): How aggressively the kernel swaps to ZRAM. Use 80-100 for ZRAM (unlike disk swap where 60 is default)
    - **Max Devices** (1-8): Number of ZRAM devices, usually one per CPU core for parallel compression

=== "Troubleshooting"

    - **ZRAM not working**: Check `systemctl status armbian-zram-config` and `swapon --show`
    - **High CPU usage**: Normal during memory pressure. Reduce `ZRAM_PERCENTAGE` or switch to `lzo` algorithm
    - **Still out of memory**: Increase `ZRAM_PERCENTAGE` (up to 200-300% for read-heavy workloads)
    - **Algorithm not supported**: Run `cat /sys/block/zram0/comp_algorithm` to see available options
    - **Changes not applying**: Run `systemctl restart armbian-zram-config` or reboot

=== "Advanced Configuration"

    Edit `/etc/default/armbian-zram-config` directly for advanced options:

    ```sh
    # Backup first
    cp /etc/default/armbian-zram-config /etc/default/armbian-zram-config.bak

    # Edit configuration
    nano /etc/default/armbian-zram-config

    # Restart to apply
    systemctl restart armbian-zram-config
    ```

    **ZRAM backing device** - for systems with fast NVMe storage:

    ```sh
    # Add to /etc/default/armbian-zram-config
    ZRAM_BACKING_DEV=/dev/nvme0n1p4
    ```

    **Monitoring**:

    ```sh
    # Check compression ratio
    echo "scale=2; $(cat /sys/block/zram0/orig_data_size) / $(cat /sys/block/zram0/compr_data_size)" | bc

    # Monitor swap usage
    watch -n 1 'swapon --show && free -h'
    ```

=== "Configuration Files"

    - **`/etc/default/armbian-zram-config`**: Main ZRAM configuration
    - **`/etc/sysctl.d/99-armbian-memory.conf`**: Swappiness and VM parameters
    - **`zramctl`**: Show detailed ZRAM device statistics
    - **`swapon --show`**: Display active swap devices including ZRAM

<!--- footer STOP from tools/include/markdown/MEM001-footer.md --->


~~~ bash title="Memory"
armbian-config --cmd MEM002
~~~


~~~ bash title="Tune Memory"
armbian-config --cmd MEM003
~~~



