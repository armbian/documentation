# IRC Channel


## 👏 --------------- Overview

As announced in the [forums](https://forum.armbian.com/topic/12803-armbian-irc-channel/) everyone interested can communicate in realtime using the [internet relay chat (or *IRC*)](https://de.wikipedia.org/wiki/Internet_Relay_Chat).
Well known clients for CLI are [Weechat](https://weechat.org/) or [Irssi](https://irssi.org/) and for GUI [Hexchat](https://hexchat.github.io/). 
  <br/><br/>
  
## 🔌 --------------- Connect

If you have a desktop environment with properly installed IRC client simply put this URL into your internet browser: `irc://chat.freenode.net/armbian` (Unfortunately Markdown does not allow to create clickable irc:// links)  
Or put the data in your client manually:
- Server: `chat.freenode.net`
- Ports: `6697` / non-encrypted: 6667
- Channel: `#armbian`

Or simply use Freenode's webirc client: https://webchat.freenode.net/?channels=armbian
<br/><br/>

## 💬 --------------- Channels

- **#armbian** is the project's main channel. As for now all user interaction happens there, regardless if chit-chat, issue tracking, peer-to-peer user support or even [upcoming release planning talks](https://docs.armbian.com/Process_Release-Model/#release-planning).
- **#armbian-commits** is a moderated channel. Whenever a new interaction with the build repository on Github happens it will be announced. Also newly added issues on Jira will be pasted. User chat is not possible.
- **#armbian-rss** is a live forum feed. Whenever a new post in the Armbian Forums is made it will be announced here. User chat is not possible.
Of course you can also enable desktop notification in your favorite browser for the forums.

Everybody is free to join any of these channels.
We may or may not add more channels in future depending on the needs.
<br/><br/>

## 👮 --------------- Services

Besides the services offered by Freenode (like Nickserv or Chanserv) Armbian has set up some own services.  
- **ArmbianGithub**  
Has the purpose to fill #armbian-commits and #armbian-rss like described above
- **ArmbianTwitter**  
Recurringly searches on Twitter for new Tweets from [*@armbian*](https://twitter.com/armbian) and when people are actually mentioning *Armbian*
- **ArmbianHelper**  
    - Allows to search for Issues and Task on [Jira](https://armbian.atlassian.net/projects/AR/issues)
        - If you know the actual task id simply write it to the channel and the bot will look it up. Like `AR-123`
        - Search issue by keyword/s in the summary. Like `,searchissue Allwinner H6` (Take note of the `,`)  
        Will output up to three results
    - Allows to query the Armbian apt repository
        - Search for package names with wildcards. Like `,package search linux-image*sunxi*`
        - Get info about a package like version and size. `,package info linux-image-current-sunxi`
        - Get the packages description. `,package description linux-image-current-sunxi`
    - Allows to search forums via Google API (not very precise though)
        - Example: `,g Allwinner H6 panfrost`
    - A few more minor commands, mostly used by staff or do not need introduction
        - `.nonprofit` `.contribute` `.rtfm` `.fortune` `.sunxi` `.meson`
<br/><br/>

## ❔ --------------- FAQ
- *Why are there so many people in the channel and nobody is talking?*
    - It is pretty common for community IRC channels for people to simply *idle* there. Many also using so called IRC bouncers https://en.wikipedia.org/wiki/BNC_(software) that keeps their connection to the channel alive.
- *I wrote 'Hi' but nobody answered. How do I get support there?*  
    - Probably there is nobody around at the time. Keep in mind that all users are spread around the globe and therefore living in many different time zones.  
It is a common habit to simply state your question or issue and then wait patiently for an answer. Depending how complex this may take up to a few hours because most Armbian contributors have detailed knowledge in a specific board family only.
- *Is the chat history public as well?*  
    - Yes. All conversation is redundantly logged. These logs are open to the public. You can find them here: http://irc.armbian.com
- *Why do some people have odd hostnames like '@armbian/staff/lanefu' or '@unaffiliated/username'?*  
    - These *hostnames* are so called project affiliation cloaks. These are meant to show a users affiliation to a specific project and their role there. You can find more information about that here: [https://freenode.net/kb/answer/cloaks](https://freenode.net/kb/answer/cloaks)
- *Can I have that too?*  
    - Yes. An Armbian affiliation cloak can be requested from *Werner* either via [forums](https://forum.armbian.com/profile/9032-werner/) or IRC. They usually will be granted if you are a well known member in forums, a contributor via Github or donated to the project. Make sure you identified yourself to Nickserv beforehand.
If you cannot find yourself in the list above you are free to request an unaffiliated cloak from Freenode staff. Check the link above for information.
- *How can I protect my nickname so nobody can spoof me?*  
    - Register your nick with Freenode's Nickserv service. Check [https://freenode.net/kb/answer/registration](https://freenode.net/kb/answer/registration)  
    Even though it is not mandatory you should register and identify with the services as other channels for example may not allow unregistered users to chat or join at all as anti-spam measure. If the situation demands Armbian will enforce this as well.
<br/><br/>

## 👉 --------------- Bottom line
If you have any questions, comments regarding the IRC channels and/or services or found an issue in this documentation for think you can enhance it get in touch with *Werner* either via [forums](https://forum.armbian.com/profile/9032-werner/) or IRC.
