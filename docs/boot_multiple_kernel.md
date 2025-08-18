# Using Multiple Kernels on SBC with Armbian via SD Cards

A common and effective way to use multiple kernels on a single-board computer (SBC) running Armbian is to use separate SD cards. This method is especially useful for testing new kernels, different versions of a kernel, or different Linux distributions without risking your primary, stable system. It also simplifies the process by leveraging the standard SBC boot sequence, which typically checks for a bootable SD card first.  

This tutorial will walk you through the process of setting up multiple SD cards with different Armbian kernels.

---

## Prerequisites

Before you begin, you'll need a few things:

- **Your SBC**: A compatible single-board computer (e.g., Orange Pi, Rock Pi, Odroid).  
- **Multiple SD cards**: One for each kernel or system you want to run. Use reliable, high-speed cards from a reputable brand.  
- **A computer** to write the images to the SD cards.  
- **A reliable power supply** for your SBC.  
- **Armbian images**: The specific Armbian images for your board, each with the desired kernel version (`current`, `edge`, or `legacy`). You can download these from the [official Armbian website](https://www.armbian.com/download/).  

---

## Step 1: Prepare the SD Cards 💾

Each SD card must be flashed with a different Armbian image.

1. **Download the Images**  
   Go to the official Armbian download page and find the images for your specific SBC model.  
   Example: one with the `current` kernel and another with the `edge` kernel.  

2. **Flash the SD Cards**  
   Use a flashing tool like **BalenaEtcher** or the `dd` command-line utility.

   ### Using BalenaEtcher
   - Insert an SD card into your computer.  
   - Open Etcher, select the downloaded Armbian image file.  
   - Select your SD card from the list of drives.  
   - Click **Flash!** to start the process.  
   - Repeat for each SD card and image.  

   ### Using `dd` (Linux/macOS users)
   - Unzip the Armbian image file (`.xz`).  
   - Identify your SD card's device name with `lsblk` or `diskutil list`.  
   - Run:  
     ```bash
     sudo dd if=/path/to/armbian-image.img of=/dev/sdX bs=1M status=progress && sync
     ```  
     Replace `/path/to/armbian-image.img` and `/dev/sdX` with the correct path and device name.  
   - **Be extremely careful** to select the right device to avoid data loss.  

---

## Step 2: Initial Boot and Configuration ⚙️

After flashing, each SD card is a self-contained, bootable system.

1. **Insert and Boot**  
   Insert one SD card into your SBC and connect power. The SBC’s bootloader (usually U-Boot) will detect and boot from it.  

2. **Initial Setup**  
   On first boot, Armbian will:  
   - Resize the filesystem  
   - Prompt for a root password  
   - Prompt to create a new user  

   Complete these steps for each SD card.  

3. **Shut Down and Swap**  
   - Power down the SBC.  
   - Remove the first SD card.  
   - Insert the second SD card.  
   - Repeat the boot and setup process.  

---

## Step 3: Managing and Using Different Kernels 🧑💻

Now you have multiple independent systems on separate SD cards.

- **Swapping SD Cards**  
  To switch kernels, power down, swap SD cards, and power back up. The bootloader handles everything automatically.  

- **Testing and Development**  
  - Use one SD card for a stable, “production” kernel.  
  - Use another for experimental or development kernels.  
  - If something fails, swap back to your stable card instantly.  

- **Kernel Version Management**  
  While Armbian’s `armbian-config` tool allows kernel management inside a single installation, using separate SD cards gives **full isolation**.  
  This prevents conflicts between kernel versions and ensures a clean test environment.  

---
