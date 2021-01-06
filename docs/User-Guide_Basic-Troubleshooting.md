# Hardware troubleshooting guide

If you are experiencing at least one of these problems:

- board does not boot
- board freezes, crashes or reboots randomly or when connecting USB devices
- plugged in USB devices are not detected (not listed in `lsusb` output)
- error changing the root password at first boot (Authentication token manipulation error)
- error installing or updating packages due to read-only file system

and you are using a stable Armbian image, then most likely you have one of two common problems - **powering issue** or **SD card issue**.

Note that

- _"I know that my power supply is good", "it worked yesterday", "it works with a different device",_ etc. are **not objective reasons** to skip powering related diagnostics
- _"I know that my SD card is good", "it worked yesterday", "it works with a different device",_ etc. are **not objective reasons** to skip storage related diagnostics
- undervoltage can cause symptoms related to SD card problems such as filesystem corruptions and data loss, so powering has to be checked first

## Powering notes

- Most boards, even ones fitted with PMIC (power management integrated circuit) do not have any measures to react to undervoltage that could prevent instability
- It does not matter what voltage your power supply outputs, it matters what voltage will reach the onboard voltage regulators
- Peak power consumption of popular boards can vary from 0.9A at 5V (H3 based Orange Pi PC) to 1.7A at 5V (RK3288 based Tinkerboard), both without any attached peripherials like USB devices
- Due to the Ohm's law voltage drop due to cable and connector resistance will be proportional to the electric current, so most of the time problems will be experienced at current spikes caused by CPU load or peripherials like spinning up HDDs

### Power supply

- Cheap phone chargers may not provide the current listed on their label, especially for long time periods
- Some cheap phone chargers don't have proper feedback based stabilization, so output voltage may change depending on load
- Power supplies will degrade over time (especially when working 24/7)
- Some problems like degraded output filtering capacitors cannot be diagnosed even with a multimeter because of the non-linear voltage form

### Cable

- The longer and thinner the cable - the higher its resistance - the greater the voltage drop will be under load
- Even thick looking cable can have thin wires inside, so do not trust the outside cable diameter

### Connector

- MicroUSB connector is rated for the maximum current of 1.8A, but even this number cannot be guaranteed. Trying to pass larger current (even momentarily) may result in a voltage dropping below USB specifications
- Most of the boards can also be powered through GPIO pins. This can be used to bypass the microUSB connector and thus to improve stability

## SD card notes

- A SD card is a complex storage device with an embedded controller that processes read, erase and write operations, wear leveling, error and corruption detection, but it does not provide any diagnostic protocols like S.M.A.R.T.
- SD cards will degrade over time and may fail in the end in different ways - become completely or partially read-only or cause a silent data corruption

### SD card brand

- Based on current prices and performance tests done by Armbian users Samsung Evo, Samsung Evo Plus and Sandisk Ultra cards are recommended
- Other good alternatives may be added to this page in the future

### SD card size and speed class

- SD card speed class and size does not influence the reliability directly, but larger size means larger amount of lifetime data written, even if you are using 10-20% of the cards space

### SD card testing

- There are many fake SD card around. eBay and Amazon Marketplace are notorious for selling fakes, but sometimes even reputable retailers get fooled.
- Most commonly low capacity cards will be reprogrammed to appear as bigger, but any files written beyond the true capacity will be lost or corrupted.
- We recommend to always [test the capacity of each new SD cards using f3](https://fight-flash-fraud.readthedocs.io/en/latest/usage.html).

### Writing images to the SD card

- If you wrote an image to the card it does not mean that it was written successfully without any errors
- so always verify images after write using some tools like _balenaEtcher_ which is currently the only popular and cross-platform tool that does mandatory verify on write (more lightweight alternatives may be added to this page in the future)
- "Check for bad blocks" function available in some tools is mostly useless when dealing with SD cards
- Note that _balenaEtcher_ verifies only 1-2GB that are occupied by the initial unresized image, it does not verify the whole SD card

## Configuration

- Some boards require the setup of the correct device tree file or they will not boot. Check the board specific documentation for details.

## How to report bugs properly

- Follow instructions on [https://armbian.com/bugs](https://armbian.com/bugs)
