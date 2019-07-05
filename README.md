# Warframe TennoCon-2019
We are very welcome that the Tenno and people who come here.

**This program has been fully developed! Enjoy it!**

***（此文档有中文简体版本！请查看根目录下的“README_cn.md”文件！）***
## Overview
TennoCon in 2019 is coming soon. According to the [News On the DE's official website](https://www.warframe.com/news/warframe-empyrean-e3-teaser-trailer), it said that DE will be in [Twitch](https://www.twitch.tv/warframe) and Mixer (Unknown link) stream online. If the news is correct, Tenno can be able to get a Lotus Ephemera by watching 30 minutes' streaming on Twitch or Mixer before 5:59 pm on July 6, 2019. Later, at 6:00 pm to 7:00 EST, by watching the streaming 30-minutes continuously, it will add a Warframe slot and a Nekros Prime to your Warframe account.

Because of the time zone problem (and other problem), the live stream of TennoCon is not a good viewing time for some people...but given that DE will give a bunch of good things, I don't think most people would not want to lose the streaming.

A better option to rent a VPS and hang up the webpage on the VPS. However, due to long periods of unattended operation, the cookies used for login may be invalidated, so that "watching" may not be counted in the background of the server.

So, this program out.

## How does it work

Be sure to follow the prompts before making it work. After entering the main function, the program will open the page intermittently to prevent cookies from failing. Each time it is opened, the program calls the system command line and loads the page using the format "[pre-configured browser path] [link]".

When the time ticks to the 35 minutes before the start of the live broadcast, the program will enter a separate loop to wait for the break loop after the live broadcast starts; if the time between the live-time and now less than 10 minutes, the direct break loop. All break loop operations are directed to the main run function. When the main run function runs, the program does not do any extra work except display information and write logs (unless your VPS memory usage exceeds 80%, because at this time Chrome is extremely vulnerable to crashing, the program will automatically end the browser and  restart; or your browser has crashed by itself). After the arrival time, the program will display the final interface.

## How to use
First, you need to open a Windows server from a VPS provider. Note that this program may completely fail in Linux due to the need to open the browser window. In addition, please rent a server outside mainland China, because Twitch and Mixer are unstable in mainland China (Twitch has been banned from access).

In order to use this program, first, you need to download the source code on [GitHub](https://github.com/sctop/Warframe-Tennocon). Then, extract the archive, and download [latest installation package (3.7.3)](https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe) from [Python official website](https://www.python.org/). Once Python is installed, open a cmd window and enter the following code one by one:

```cmd
py -m pip install psutil
py -m pip install pytz
```

If you see the words "successfully", etc., it means that the package that this program depends on is already installed. Next, just open the "main" file in the source code. Then, follow the prompts to create or use an existing profile content.

# Other Question?
Please refer to the "_doc" folder under this project.

If you still can't solve the problem by yourself, please submit an issue at [GitHub page](https://github.com/sctop/Warframe-Tennocon). I will check it from time to time.
