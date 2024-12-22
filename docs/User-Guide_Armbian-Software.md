# Armbian Software


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
