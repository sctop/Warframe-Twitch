# Warframe TennoCon-2019
对每一位来到这里的Tenno与其它人表示感谢！

**此程序已经开发完毕！请敬请享受！**

# 概述
2019年的TennoCon即将到来。根据[DE官网上的消息](https://www.warframe.com/zh-hans/news/warframe-empyrean-e3-teaser-trailer)，其显示DE将在[Twitch](https://www.twitch.tv/warframe)和Mixer（详细链接不详）上进行直播。如果新闻无误，Tenno将可以在Twitch或者Mixer上在美国东部时间（简称EST）2019年7月6日晚上5:59前通过观看超过30分钟来获得一个Lotus幻纹。随后，在美国东部时间晚上6:00到7:00，连续观看30分钟将可以获得一个Warframe槽位和一个Nekros Prime。

因为存在时区问题（以及其它不可抗力问题），致使TennoCon的在线直播对于一些Tenno来说并不是一个很好的观看时间......但是鉴于DE这次看直播给的东西比较多，因此我觉得大多数人都不会不想不要的。

一个比较好的选择租赁一个VPS，并在VPS上挂机网页。但由于长时间无人操作，登录用的Cookies可能会失效，致使“观看”时不被计入后台中。

所以，这个程序产生了。

# 它如何运作？
在使它正常工作前，请务必按照提示进行操作。在进入正式运作后，程序将间歇性打开页面以防止Cookies失效。每一次打开，程序调用系统命令行，使用“[预先设定好的浏览器路径] [链接]”的格式加载页面。

在直播开始前35分钟，程序将进入一个单独的循环以等待直播开始后break循环；直播前10分钟，直接break循环。所有的break循环的操作都会导向主运行函数。在主运行函数运行时，程序除了显示信息和写入日志外，不会做任何额外的操作（除非您的VPS内存占用超过80%，因为在这时Chrome极度容易崩溃，程序将自动结束浏览器进程并重启；或您的浏览器自己爆炸了）。到达时间后，程序将显示最终界面。

# 如何使用？
首先，您需要从一个VPS提供商开启一个Windows服务器。注意，此程序因为需要开启浏览器的窗口，因此使用Linux效果可能会完全失效；另外，请租赁一个在中国大陆以外的服务器，因为Twitch和Mixer在中国大陆并不稳定（Twitch已被禁止访问）。

为了使用该程序，您首先需要在[GitHub上](https://github.com/sctop/Warframe-Tennocon)下载源代码。然后，解压压缩包，并从[Python官方网站](https://www.python.org/)下载[最新安装包(3.7.3)](https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe)。Python安装完毕后，打开命令行提示符（cmd），并逐个输入以下代码：

```cmd
py -m pip install psutil
py -m pip install pytz
```

如果看到"successfully"等的字样，则表明此程序所依赖的包已经安装。接下来只需要打开源代码中的main文件即可。然后，根据提示新建或使用已经存在的配置文件内容。

# 其它问题？
敬请参阅该项目下的“_doc”文件夹下的内容。

如果仍不能自行解决问题，请在请在[GitHub页面](https://github.com/sctop/Warframe-Tennocon)提交一个issue。作者会不定时查看。