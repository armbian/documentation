## What it does?

- Builds custom **kernel**, **image** or a Debian based Linux **distribution** optimized for low-resource hardware,
- Include filesystem generation, low-level control software, kernel image and **bootloader** compilation,
- Provides a **consistent user experience** by keeping system standards across different platforms.

``` mermaid
graph LR
  A[./compile.sh] --> B{Change<br>kernel<br>config};
  B ---> |yes| C["HW"];
  B ---> |no| C["HW"];
  C ---> |branch| D["legacy<br>vendor<br>current<br>edge"];
  D --> |base| E["Debian<br>Ubuntu"];
  E ---> |type| F["CLI"];
  F ---> |type| G["Server"];
  F ---> |type| H["Minimal"];
  E ---> I["Desktop"];
  I ---> K["XFCE"];
  I ---> L["Gnome"];
  I ---> M["Cinammon"];
  I ---> N["KDE Neon"];
```

## Key Advantages

- Simplicity with interactive graphical interface.
- Generates widely recognized and well maintained userspace
- Fast learning curve for complex operations

Check other similarities, advantages and disadvantages compared with leading industry standard build software.

Function | Armbian | Yocto | Buildroot |
|:--|:--|:--|:--|
| Target | general purpose | embedded | embedded / IOT |
| U-boot and kernel | compiled from sources | compiled from sources | compiled from sources |
| Board support maintenance &nbsp; | complete | outside | outside |
| Root file system | Debian or Ubuntu based| custom | custom |
| Package manager | APT | any | none |
| Configurability | limited | large | large |
| Initramfs support | yes | yes | yes |
| Getting started | quick | very slow | slow |
| Cross compilation | yes | yes | yes |
