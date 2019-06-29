# Warframe TennoCon-2019
对每一位来到这里的Tenno与其它人表示感谢！

We are very welcome that the Tenno and people who come here.

**注意：本程序暂未开发完毕！！！**

**WARNING: This program has not been to fully develop!**
## 概述 Overview
2019年的TennoCon即将到来。根据[DE官网上的消息](https://www.warframe.com/zh-hans/news/warframe-empyrean-e3-teaser-trailer)，其显示DE将在[Twitch](https://www.twitch.tv/warframe)和Mixer（详细链接不详）上进行直播。如果新闻无误，Tenno将可以在Twitch或者Mixer上在美国东部时间（简称EST）2019年7月6日晚上5:59前通过观看超过30分钟来获得一个Lotus幻纹。随后，在美国东部时间晚上6:00到7:00，连续观看30分钟将可以获得一个Warframe槽位和一个Nekros Prime。

TennoCon in 2019 is coming soon. According to the [News On the DE's official website](https://www.warframe.com/news/warframe-empyrean-e3-teaser-trailer), it said that DE will be in [Twitch](https://www.twitch.tv/warframe) and Mixer (Unknown link) stream online. If the news is correct, Tenno can be able to get a Lotus Ephemera by watching 30 minutes' streaming on Twitch or Mixer before 5:59 pm on July 6, 2019. Later, at 6:00 pm to 7:00 EST, by watching the streaming 30-minutes continuously, it will add a Warframe slot and a Nekros Prime to your Warframe account.

因为存在时区问题（以及其它不可抗力问题），致使TennoCon的在线直播对于一些Tenno来说并不是一个很好的观看时间......但是鉴于DE这次看直播给的东西比较多，因此我觉得大多数人都不会不想不要的。

Because of the time zone problem (and other problem), the live stream of TennoCon is not a good viewing time for some people...but given that DE will give a bunch of good things, I don't think most people would not want to lose the streaming.

一个比较好的选择租赁一个VPS，并在VPS上挂机网页。但由于长时间无人操作，登录用的Cookies可能会失效，致使“观看”时不被计入后台中。

A better option to rent a VPS and hang up the webpage on the VPS. However, due to long periods of unattended operation, the cookies used for login may be invalidated, so that "watching" may not be counted in the background of the server.

所以，这个程序产生了。

So, this program out.

## 如何使用  How to use
首先，您需要从一个VPS提供商开启一个Windows服务器。注意，此程序因为需要开启浏览器的窗口，因此使用Linux效果可能会完全失效；另外，请租赁一个在中国大陆以外的服务器，因为Twitch和Mixer在中国大陆并不稳定（Twitch已被禁止访问）。

First, you need to open a Windows server from a VPS provider. Note that this program may completely fail in Linux due to the need to open the browser window. In addition, please rent a server outside mainland China, because Twitch and Mixer are unstable in mainland China (Twitch has been banned from access).

为了使用该程序，您首先需要在[GitHub上](https://github.com/sctop/Warframe-Tennocon)下载源代码。然后，解压压缩包，并从[Python官方网站](https://www.python.org/)下载[最新安装包(3.7.3)](https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe)。Python安装完毕后，打开命令行提示符（cmd），并逐个输入以下代码：

In order to use this program, first, you need to download the source code on [GitHub](https://github.com/sctop/Warframe-Tennocon). Then, extract the archive, and download [latest installation package (3.7.3)](https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe) from [Python official website](https://www.python.org/). Once Python is installed, open a cmd window and enter the following code one by one:

```cmd
py -m pip install hashlib
py -m pip install pytz
```

如果看到"successfully"等的字样，则表明此程序所依赖的包已经安装。接下来只需要打开源代码中的main文件即可。然后，根据提示新建或使用已经存在的配置文件内容。

If you see the words "successfully", etc., it means that the package that this program depends on is already installed. Next, just open the "main" file in the source code. Then, follow the prompts to create or use an existing profile content.

# 其它问题？ Other Question?
请在[GitHub页面](https://github.com/sctop/Warframe-Tennocon)提交一个issue。

Please submit an issue on the [GitHub page](https://github.com/sctop/Warframe-Tennocon).
