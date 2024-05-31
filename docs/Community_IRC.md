# IRC Channel / Discord / Matrix

## 👏 Overview

As announced in the [forums](https://forum.armbian.com/topic/12803-armbian-irc-channel/) everyone interested can communicate in realtime using the [internet relay chat (or *IRC* for short)](https://de.wikipedia.org/wiki/Internet_Relay_Chat).
Well known IRC clients for CLI are [Weechat](https://weechat.org/) or [Irssi](https://irssi.org/) and for GUI [Hexchat](https://hexchat.github.io/) or [Konversation](https://konversation.kde.org/).  
Mature clients for Matrix: [Element](https://element.io/download) or [FluffyChat](https://fluffychat.im).  

Besides that communication is also possible via *Discord* or *Matrix* (closed beta).

## 🔌 How to connect

### IRC

Libera network:

- Server: `irc.libera.chat`  
- Ports: `6697` / non-encrypted: `6667`  
- Channels: as listed below

OFTC network:

- Server: `irc.oftc.net`  
- Ports: `6697` / non-encrypted: `6667`  
- Channels: `#armbian` and `#armbian-announcements` are available only

In order to enter main `#armbian` channels registration with Nickserv is mandatory on Libera. Check [Libera Chat documentation](https://libera.chat/guides/registration) for further information.

### Discord

Simply click here: [https://discord.com/invite/armbian](https://discord.com/invite/armbian)  

Channels starting with `#armbian-` are relayed between Discord and Libera IRC so it does not matter if you join IRC or Discord as both ends receive your messages. Check `#welcome-and-rules` for more information.
The main `#armbian` channel and `#armbian-announcements` are relayed between Discord, Libera, OFTC and Matrix.

### Matrix (closed beta)

- Server: `matrix.armbian.com`
- Channels: `#armbian:matrix.armbian.com` and `#armbian-announcements:matrix.armbian.com` are available only
- To receive an invitation for former please ping either Lanefu or Werner with your Matrix handle in any known ways to communicate like the chat options above or forums. Once in feel free to invite others by yourself.

## 🛑 Rules

Forums registration terms and rules apply for our chats: [https://forum.armbian.com/terms](https://forum.armbian.com/terms)

## 💬 Channels (depending on platform only a limited selection might be available)

- **`#armbian`** is the project's main channel. Issue tracking, peer-to-peer user support or [upcoming release planning talks](https://docs.armbian.com/Process_Release-Model/#release-planning).
- **`#armbian-announcements`** : important messages from the Armbian team. You definitely want to idle here. Moderated channel
- **`#armbian-devel`** : build engine development topics
- **`#armbian-desktop`** : desktop environment development
- **`#armbian-csc`** unsupported/stating board talk
- **`#armbian-allwinner`** Allwinner-related SoC talk
- **`#armbian-amlogic`** Amlogic-related SoC talk
- **`#armbian-broadcom`** Broadcom-related SoC talk
- **`#armbian-rockchip`** Rockchip-related SoC talk
- **`#armbian-offtopic`** General chit chat, whatever that does not fit other channels
- **`#armbian-commits`** Whenever a new interaction with a [repository on Github](https://github.com/armbian/) happens it will be announced. Moderated channel

## 👮 Services

Besides the services offered by IRC (like Nickserv or Chanserv) Armbian has set up some own services (on Libera only).  

**`ArmbianGithub`**

- Has the purpose to fill #armbian-commits channel

**`DC-IRC`**

- Has the purpose to relay messages between the IRC networks and Discord. Applies for all channels beginning with `#armbian-` as well as `#armbian`.

**`ArmbianHelper`**

- Allows searching forums via Google API (not very precise though)
  - Example: `,g Allwinner H6 panfrost`
- A few more minor commands, mostly used by staff or do not need introduction
  - `.nonprofit`, `.sed`, `.contribute`, `.rtfm`, `.fortune`, `.sunxi`, `.meson`, `help`, `help irc`, `.tvboxes`
- Translation for non-native English speakers
  - Simply start your sentence with `--` at the beginning and the bot will translate your message regardless of the source language into English.  
          *Note*: This services will be activated manually on demand (like planned meetings for example) since its backend generates cost.

## ❔ FAQ

- Why are there so many people in the channel and nobody is talking?  
  - It is pretty common for community IRC channels for people to simply *idle* there. Many also using so called IRC bouncers <https://en.wikipedia.org/wiki/BNC_(software>) that keeps their connection to the channel alive to act like an answering machine.

- I wrote 'Hi' but nobody answered. How do I get support there?
  - Probably there is nobody around at the time. Keep in mind that all users are spread around the globe and therefore living in many different time zones.  
  It is a common habit to simply state your question or issue and then wait patiently for an answer. Depending how complex this may take up to a few hours because most Armbian contributors have detailed knowledge in a specific board family only.
- Is the chat history public as well?
  - Yes. All conversation is logged. These logs are open to the public. You can find them here: [http://irc.armbian.com](http://irc.armbian.com)
- Why do some people have odd hostnames like `@armbian/staff/lanefu` or `@user/username`?
  - These *hostnames* are so called project affiliation cloaks. These are meant to show a users affiliation to a specific project and their role there.
- Can I have that too?
  - Yes. An Armbian affiliation cloak can be requested from *Werner* either via [forums](https://forum.armbian.com/profile/9032-werner/) or IRC. They usually will be granted if you are a well known member in forums, a contributor via Github or donated to the project. Make sure you identified yourself to Nickserv beforehand.  
- How can I protect my nickname so nobody can spoof me?  
  - Register your nick with Libera's Nickserv service. Check [https://libera.chat/guides/registration](https://libera.chat/guides/registration)  
    Even though it is not mandatory you should register and identify with the services as other channels for example may not allow unregistered users to chat or join at all as anti-spam measure.
- Why do some users have voice (+v) in channel?
  - As mentioned in [forums](https://forum.armbian.com/topic/12803-armbian-irc-chat/?tab=comments#comment-96828) "all contributors to the project, regardless if forums staff, contributor on Github or well known and longtime active user" may get voice on request.

- Should I add **away** to my nick if I am AFK? Like **Werner|away**
  - No. Please use the `/away [reason]` command as intended. For an explanation please have a look at the [ZNC Wiki](https://wiki.znc.in/Awaynick).

## 👉 Bottom line

If you have any questions, comments regarding the IRC channels and/or services or found an issue in this documentation for think you can enhance it get in touch with *Werner* either via [forums](https://forum.armbian.com/profile/9032-werner/), IRC or Discord.
