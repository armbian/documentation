# Armbian Config

``` mermaid
flowchart LR
  A[armbian-config] -----> B["System"];
  A[armbian-config] -----> C["Network"];
  A[armbian-config] -----> D["Localistation"];
  A[armbian-config] -----> E["Software"];
  A[armbian-config] -----> F["Help"];
```

<img src="https://raw.githubusercontent.com/armbian/configng/main/share/icons/hicolor/scalable/configng-tux.svg">

Utility for configuring your board, adjusting services, and installing applications. It comes with Armbian by default.

To start the Armbian configuration utility, use the following command:
~~~
armbian-config
~~~

## Adding a new feature

Please check [instructions](/Contribute/Armbian-config/).
