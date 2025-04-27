# Armbian Software

The **Armbian Software** section is a vital part of the **armbian-config** tool, providing an easy and powerful way to install a wide range of ready-to-run and optimized software for your device.  

It automates the entire installation and configuration process, saving time and reducing complexity.  

Beyond just installing software, it applies specific performance optimizations and hardware-specific adjustments to ensure maximum compatibility and efficiency for your board.

With Armbian Software, you gain access to curated, lightweight, and reliable solutions tailored specifically for Armbian-supported devices.  

This guarantees that your system runs faster, more reliably, and remains easy to maintain — making Armbian Software an essential resource for getting the most out of your hardware.


``` mermaid
flowchart LR
  A[Software] ----> B["Containerlization"];
  A[Software] ----> C["Desktops"];
  A[Software] -----> D["DNS blockers"];
  A[Software] -----> E["Home Automation"];
  A[Software] ------> F["Monitoring"];
  A[Software] ------> G["Development"];
  A[Software] ------> J["Network tools"];
  A[Software] ----------> H["Remote Management tools"];
  A[Software] ----------> I["Media Servers"];
```


To start the Armbian software section, use the following command and choose `software` section:
~~~
armbian-config
~~~

## Adding a new feature

Please check [instructions](/Contribute/Armbian-config/).
