# IRC Channel / Matrix / Discord


## 👏 --------------- Overview

As announced in the [forums](https://forum.armbian.com/topic/12803-armbian-irc-channel/) everyone interested can communicate in realtime using the [internet relay chat (or *IRC*)](https://de.wikipedia.org/wiki/Internet_Relay_Chat).
Well known clients for CLI are [Weechat](https://weechat.org/) or [Irssi](https://irssi.org/) and for GUI [Hexchat](https://hexchat.github.io/).  
  
Besides that communication is also possible via Matrix or our (unofficial) Discord server.

  <br/><br/>
  
## 🔌 --------------- Connect
### IRC
If you have a desktop environment with properly installed IRC client simply put this URL into your internet browser: `irc://irc.libera.chat/armbian` (Unfortunately Markdown does not allow to create clickable irc:// links)  
Or put the data in your client manually:

+ Server: `irc.libera.chat`  
+ Ports: `6697` / non-encrypted: `6667`  
+ Channel: `#armbian`  

Or simply use Libera.Chat's webirc client: [https://web.libera.chat/#armbian](https://web.libera.chat/#armbian)


### Discord
Simply click here: [https://discord.gg/gNJ2fPZKvc](https://discord.gg/gNJ2fPZKvc)  
Some of these channels are relayed to our IRC channel so it does not matter if you join IRC or Discord as both received your messages. Check `#welcome-and-rules` for more info.

### Matrix
Simply join this room with our Matrix client: `#armbian:libera.chat`  
Channel names are the same as for IRC mentioned below.

<br/><br/>
## 💬 --------------- Channels

- **#armbian** is the project's main channel. As for now all user interaction happens there, regardless if chit-chat, issue tracking, peer-to-peer user support or even [upcoming release planning talks](https://docs.armbian.com/Process_Release-Model/#release-planning).
- **#armbian-devel** is the project's channel dedicated for build engine development topics.
- **#armbian-commits** is a moderated channel. Whenever a new interaction with a [repository on Github](https://github.com/armbian/) happens it will be announced. Also newly added issues on [Jira](https://armbian.atlassian.net/projects/AR/issues/?filter=allissues) will be pasted. User chat is not possible.
- **#armbian-rss** is a live forum and Twitter feed. Whenever a new post in the Armbian Forums is made or somebody mentions Armbian on Twitter it will be announced here. User chat is not possible.
Of course you can also enable desktop notification in your favorite browser for the forums.

Everybody is free to join any of these channels.
We may or may not add more channels in future depending on the needs.
<br/><br/>

## 👮 --------------- Services

Besides the services offered by Libera (like Nickserv or Chanserv) Armbian has set up some own services.  

- **ArmbianGithub**
    - Has the purpose to fill #armbian-commits and #armbian-rss like described above
- **Armbian-Discord**
    - Has the purpose to relay messages from and to our Discord server in certain channels
- **ArmbianTwitter**
    - Recurringly searches on Twitter for new Tweets from [*@armbian*](https://twitter.com/armbian) and when people are actually mentioning *Armbian*
- **ArmbianHelper**
    - Allows to search for Issues and Task on [Jira](https://armbian.atlassian.net/projects/AR/issues)
        - If you know the actual task id simply write it to the channel and the bot will look it up. Like `AR-123`
        - Search issue by keyword/s in the summary. Like `,searchissue Allwinner H6`  
          Take note of the `,`. Will output up to three results.
    - Allows to search forums via Google API (not very precise though)
        - Example: `,g Allwinner H6 panfrost`
    - A few more minor commands, mostly used by staff or do not need introduction
        - `.nonprofit`, `.sed`, `.contribute`, `.rtfm`, `.fortune`, `.sunxi`, `.meson`, `help`, `help irc`, `.tvboxes`
    - Translation for non-native English speakers
        - Simply start your sentence with `--` at the beginning and the bot will translate your message regardless of the source language into English.  
          *Note*: This services will be activated manually on demand (like planned meetings for example) since its backend generates cost.
        
<br/><br/>

## ❔ --------------- FAQ
- *Why are there so many people in the channel and nobody is talking?*
    - It is pretty common for community IRC channels for people to simply *idle* there. Many also using so called IRC bouncers https://en.wikipedia.org/wiki/BNC_(software) that keeps their connection to the channel alive.
- *I wrote 'Hi' but nobody answered. How do I get support there?*  
    - Probably there is nobody around at the time. Keep in mind that all users are spread around the globe and therefore living in many different time zones.  
It is a common habit to simply state your question or issue and then wait patiently for an answer. Depending how complex this may take up to a few hours because most Armbian contributors have detailed knowledge in a specific board family only.
- *Is the chat history public as well?*  
    - Yes. All conversation is redundantly logged. These logs are open to the public. You can find them here: [http://irc.armbian.com](http://irc.armbian.com)
- *Why do some people have odd hostnames like '@armbian/staff/lanefu' or '@user/username'?*  
    - These *hostnames* are so called project affiliation cloaks. These are meant to show a users affiliation to a specific project and their role there.
- *Can I have that too?*  
    - Yes. An Armbian affiliation cloak can be requested from *Werner* either via [forums](https://forum.armbian.com/profile/9032-werner/) or IRC. They usually will be granted if you are a well known member in forums, a contributor via Github or donated to the project. Make sure you identified yourself to Nickserv beforehand.
If you cannot find yourself in the list above you are free to request an unaffiliated cloak from Libera staff. Join #libera for that.
- *How can I protect my nickname so nobody can spoof me?*  
    - Register your nick with Libera's Nickserv service. Check [https://libera.chat/guides/registration](https://libera.chat/guides/registration)  
    Even though it is not mandatory you should register and identify with the services as other channels for example may not allow unregistered users to chat or join at all as anti-spam measure. If the situation demands Armbian will enforce this as well.
- *Why do some users have voice (+v) in channel?*  
    - As mentioned in [forums](https://forum.armbian.com/topic/12803-armbian-irc-chat/?tab=comments#comment-96828) "all contributors to the project, regardless if forums staff, contributor on Github or well known and longtime active user" may get voice on request.
- *Should I add __away__ to my nick if I am AFK? Like __Werner|away__*  
    - No. Please use the `/away [reason]` command as intended. For an explanation please have a look at the [ZNC Wiki](https://wiki.znc.in/Awaynick).
<br/><br/>

## 👉 --------------- Bottom line
If you have any questions, comments regarding the IRC channels and/or services or found an issue in this documentation for think you can enhance it get in touch with *Werner* either via [forums](https://forum.armbian.com/profile/9032-werner/) or IRC.

By the way if you like to have a free IRC bouncer to always be up-to-date and never miss a conversation again you should check out [this thread](https://forum.armbian.com/topic/13943-irc-bouncer-giveaway/).
