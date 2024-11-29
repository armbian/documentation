# Fixed and wireless network settings


***

## Configure network interfaces


***

### Add / change interface

<!--- header START from tools/include/markdown/NE002-header.md --->
``` mermaid
graph LR
  A[Network] --> B[Add / Change interface];
  A[Network] --> O[Revert to defaults];
  A[Network] --> P[Show configuration];
  B ---->E[Wired];
  B ---->F[Wireless];
  E -->R[DHCP];
  E -->T[Static];
  E -->S[Spoof MAC];
  F -->X[Station];
  F -->W[Access point]; 
```

<!--- header STOP from tools/include/markdown/NE002-header.md --->

**Command:** 
~~~
armbian-config --cmd NE002
~~~

**Author:** @igorpecovnik

**Status:** Stable


<!--- footer START from tools/include/markdown/NE002-footer.md --->
=== "Wired device check"

    In order to configure your network devices, they need to be supported the kernel.

    To verify, use command:

    ```sh
    ip addr
    ```

    It is usually something like eth0, enp4s3 or lan.

=== "Wireless device check"

    In order to configure your wireless network devices, they need to be supported the kernel.

    To verify, use command:

    ```sh
    iw dev | awk '$1=="Interface"{print $2}'
    ```

    It is usually something like `wlan0`, `wlo1` or `wlx12334c47dec3`. If you get blank response, it means your WiFi device / dongle is not supported by the kernel.

<!--- footer STOP from tools/include/markdown/NE002-footer.md --->



***

### Revert to Armbian defaults
**Command:** 
~~~
armbian-config --cmd NE003
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Show configuration
**Command:** 
~~~
armbian-config --cmd NE004
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

### Show active status
**Command:** 
~~~
armbian-config --cmd NE005
~~~

**Author:** @igorpecovnik

**Status:** Stable



***

