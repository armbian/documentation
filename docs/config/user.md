---
description: "Change the default login shell and customise the MOTD login banner on Armbian single-board computers with the armbian-config utility."
comments: true
---

# Shell and MOTD


Change shell, adjust MOTD

## Change shell


Change shell system wide to ZSH


<!--- section image START from tools/include/images/SHELL1.png --->
![Change shell](/images/SHELL1.png)
<!--- section image STOP from tools/include/images/SHELL1.png --->


<!--- header START from tools/include/markdown/SHELL1-header.md --->
ZSH is a powerful and customizable shell designed to be an enhanced replacement for BASH. When combined with Oh My Zsh, which is integrated in `armbian-zsh`, it offers an extensive plugin system, beautiful themes, and productivity features like autosuggestions, syntax highlighting, and easier navigation.

<!--- header STOP from tools/include/markdown/SHELL1-header.md --->


~~~ bash title="Change shell"
armbian-config --cmd SHELL1
~~~


~~~ bash title="Change shell system wide to BASH"
armbian-config --cmd SHELL2
~~~



## Adjust MOTD


Adjust welcome screen (motd)


<!--- section image START from tools/include/images/MOTD01.png --->
![Adjust MOTD](/images/MOTD01.png)
<!--- section image STOP from tools/include/images/MOTD01.png --->


~~~ bash title="Adjust MOTD"
armbian-config --cmd MOTD01
~~~

