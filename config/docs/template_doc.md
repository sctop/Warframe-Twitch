# 配置文件配置指南

如大家所见，配置文件拥有default和许多其它由用户创建的文件。

如果你不想进入程序编辑文件，而是转而自行编辑的话，这里会提供一些帮助给你。

## 结构
下面的内容将分逐个大层来讲解
### link 链接
"WarframeAccount"：指的是进入Warframe官网后查看你的个人信息（或者说个人中心）的网页地址

"Twitch"：Warframe TennoLive在Twitch上的直播地址

---
### delay 延迟
这是一个来管理程序延迟运行的层
#### loading
这里是用于等待网页加载完毕的。请注意，这里均为秒且为int。

"WarframeAccount"：需要等待多少秒以等待Warframe官网个人中心页面载入

"Twitch"：需要等待多少秒以等待Twitch直播页面载入
#### sleep
这里是管理程序等待多少秒后再进行下一次的网页载入操作（防止Cookies失效），均为int

"time"：等待多少秒

"range"：这是一个列表用于控制载入时间具有随机性。范围1用于控制随机开始的范围，范围2用于控制随机结束的范围。请注意均只能是整数而不能是小数，也不能带小数点。
#### live
这里是用于直播开始/结束的相关事宜的。除非未表明，否则格式都应该为string类型的，格式为“YY-MM-DD HH-MM-SS 星期 时区”

注意，这里的时间都需要自己计算。一旦输入错误就需要自行更改配置文件。

#####"EST_in"
进入直播间的时间。美国东部时间EST。此处应该是夏令时，因此与北京时间相差12小时；冬令时为13小时。
##### timer
直播每一个阶段的控制。这是为了防止浏览器因故炸掉导致问题。

***注意，这里的都是东部时间***
###### Ephemera 幻纹
"begin"：何时开始掉落

"end"：何时结束掉落

"lasting"：持续时间，秒
###### Warframe “Nekros Prime”
"begin"：何时开始可以获取

"end"：何时结束可以获取

"lasting"：持续时间，秒

---

### browser 浏览器
此处用于控制浏览器的开关。

"name"：浏览器名称

"thread_name"：浏览器的进程名

"command_format"：命令行格式，一般为一个空格（“ ”）

"pos"：浏览器在系统的绝对位置

---

### mail 邮箱
此处用于邮件的发送。用于通知用户程序的运行情况。

"address"：邮件地址