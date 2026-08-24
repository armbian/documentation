---
description: "Set the timezone, system locale, language, keyboard layout and hostname on Armbian single-board computers with the armbian-config utility."
comments: true
---

# Localisation

## Change Global timezone


<!--- section image START from tools/include/images/GTZ001.png --->
![Change Global timezone](/images/GTZ001.png)
<!--- section image STOP from tools/include/images/GTZ001.png --->


~~~ bash title="Change Global timezone"
armbian-config --cmd GTZ001
~~~


## Change Locales reconfigure the language and character set


~~~ bash title="Change Locales reconfigure the language and character set"
armbian-config --cmd LOC001
~~~


## Change Keyboard layout


~~~ bash title="Change Keyboard layout"
armbian-config --cmd KEY001
~~~


## Change System Hostname


~~~ bash title="Change System Hostname"
armbian-config --cmd HOS001
~~~

