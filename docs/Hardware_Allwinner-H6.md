# Allwinner H6

**Overview**

[See the generic Allwinner page](https://docs.armbian.com/Hardware_Allwinner/)

The H6 CPU frequency has ben soft-capped at 1,48 GHz to avoid thermal throttling too fast. This limit can be lifted by editing
`/etc/default/cpufrequtils` and set `MAX_SPEED` to `1810000`.

**Warning**
Adding proper cooling is highly recommended.

