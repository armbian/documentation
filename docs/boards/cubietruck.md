## Cubietruck ##

- [PWM ready](https://github.com/dwilkins/pwm-sunxi) on pin PB2
- bluetooth working with on-board device / enabled by default
- total memory is 2000Mb (disabled all memory reservations for GPU on CLI images)
- due to bad PCB placement, there is [some crosstalk between Wifi and VGA in certain videomodes](http://linux-sunxi.org/Cubietruck#VGA)
- make sure you power the board via power connector otherwise your USB port won’t be powered