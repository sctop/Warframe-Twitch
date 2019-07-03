import pytz
import datetime


# 这个错误用于给开发者调试[滑稽]
class WhatTheFuckError(Exception):
    def __init__(self, code=1, message="It should be fine!", args=("It should be fine!",)):
        self.args = args
        self.message = message
        self.code = code


def format_time(tz, mode):
    """
    此函数用于格式化基于现在时间的一个时间字符串

    :param tz: 传入一个时区。对于中国地区请使用“Asia/Taipei”，可使用简写
    :param space: 是否需要空格，一般情况下作文件名。
    :return: 非不需要空格情况下，函数将返回格式为“YY-MM-DD HH-MM-SS 时区”
    """
    # 本地时间时区设定
    tz_set = pytz.timezone(tz)
    # 年月日，格式“YY-MM-DD”
    if mode == "nospace":
        yymmdd = datetime.datetime.now(tz_set).strftime("%Y-%m-%d")
    else:
        yymmdd = datetime.datetime.now(tz_set).strftime("%Y-%m-%d ")
    # 时分秒
    if mode == "nospace":
        hhmmss = datetime.datetime.now(tz_set).strftime("%H%M%S")
    else:
        hhmmss = datetime.datetime.now(tz_set).strftime("%H:%M:%S")
    if mode == "log":
        timezone = datetime.datetime.now(tz_set).strftime(" %z")
    else:
        timezone = ""
    return yymmdd + hhmmss + timezone


def date_format(year=0, month=0, day=0, hour=0, min=0, second=0, ms=0):
    flag = True
    temp1 = [int(day), int(hour), int(min), int(second), int(ms)]
    while flag:
        # 毫秒
        if temp1[4] >= 1000:
            addsecond = temp1[4] // 1000
            leftms = temp1[4] % 1000
            temp1[4] = leftms
            temp1[3] += addsecond
        # 秒
        if temp1[3] >= 60:
            addmin = temp1[3] // 60
            leftsecond = temp1[3] % 60
            temp1[3] = leftsecond
            temp1[2] += addmin
        # 分
        if temp1[2] >= 60:
            addhour = temp1[2] // 60
            leftmin = temp1[2] % 60
            temp1[2] = leftmin
            temp1[1] += addhour
        # 时
        if temp1[1] >= 24:
            addday = temp1[1] // 24
            lefthour = temp1[1] % 24
            temp1[1] = lefthour
            temp1[0] += addday
        if temp1[1] <= 23 and temp1[2] <= 59 and temp1[3] <= 59 and temp1[4] <= 999:
            flag = False
    # 日期
    flag = True
    temp2 = [int(year), int(month), int(temp1[0])]
    while flag:
        day31 = [1, 3, 5, 7, 8, 10, 12]
        day30 = [4, 6, 9, 11]
        # 如果月份大于13
        if temp2[1] >= 13:
            yearadd = temp2[1] // 12
            monthleft = temp2[1] % 12
            temp2[0] += yearadd
            temp2[1] == monthleft
            # 应该正常
            if temp2[1] >= 12 and temp2[1] < 24:
                temp2[0] += 1
                temp2[1] -= 12
            else:
                raise WhatTheFuckError
        # 下个月是31天的
        if (temp2[1] + 1) in day31 and temp2[2] > 31:
            temp2[2] = temp2[2] - 31
            temp2[1] = temp2[1] + 1
        # 下个月是30天
        elif (temp2[1] + 1) in day30 and temp2[2] > 30:
            temp2[2] = temp2[2] - 30
            temp2[1] = temp2[1] + 1
        # 闰年1月份问题
        elif (temp2[2] > 31 and temp2[1] + 1 == 2) and (
                (temp2[0] % 100 == 0 and temp2[0] % 400 == 0) or temp2[0] % 4 == 0):
            temp2[2] = temp2[2] - 31
            temp2[1] = temp2[1] + 1
        # 整百的闰年，如果日大于29
        elif (temp2[0] % 100 == 0 and temp2[0] % 400 == 0 and (temp2[2] > 29 and (temp2[1] == 2 or temp2[1] + 1 == 2))):
            temp2[2] = temp2[2] - 29
            temp2[1] = temp2[1] + 1
        # 非整百的闰年，如果日大于29
        elif temp2[0] % 4 == 0 and temp2[2] > 29 and (temp2[1] == 2 or temp2[1] + 1 == 2):
            temp2[2] = temp2[2] - 29
            temp2[1] = temp2[1] + 1
        # 非闰年二月份问题，如果日大于28
        elif temp2[2] > 28 and (temp2[1] + 1 == 3 and temp2[0] % 4 != 0):
            temp2[2] = temp2[2] - 28
            temp2[1] = temp2[1] + 1
        # 非闰年但整百年二月份问题，如果日大于28
        elif temp2[2] > 28 and (temp2[1] + 1 == 3 and temp2[0] % 400 != 0):
            temp2[2] = temp2[2] - 28
            temp2[1] = temp2[1] + 1
        # 检测是否正常
        if temp2[1] <= 12:
            # 当月是31日的月份
            if temp2[2] <= 31 and temp2[1] in day31:
                flag = False
            # 当月是30日的月份
            elif temp2[2] <= 30 and temp2[1] in day30:
                flag = False
            # 整百年闰年 2月
            elif (temp2[0] % 100 == 0 and temp2[0] % 400 == 0 and temp2[0] % 4 == 0) and temp2[2] <= 29 and temp2[
                1] == 2:
                flag = False
            # 非整百年但闰年 2月
            elif temp2[0] % 4 == 0 and temp2[2] <= 29 and temp2[1] == 2:
                flag = False
            # 不是闰年 2月
            elif temp2[0] % 4 != 0 and temp2[2] <= 28 and temp2[1] == 2:
                flag = False
            else:
                flag = True
    return temp2[0], temp2[1], temp2[2], temp1[1], temp1[2], temp1[3], temp1[4]


def time_check(time1, time2):
    """
    此程序用于检测time1是否大于、小于或等于time2。
    两个参数必须均为一个由 年、月、日、小时、分钟、秒、毫秒 组成的元组。

    :param time1:
    :param time2:
    :return: 一个列表。第0项元素为time1小于time2，第1项为大于，第2项为一样
    """
    if len(time1) != len(time2):
        return 1
    less = [True, False, False]
    great = [False, True, False]
    same = [False, False, True]
    for i in range(len(time1)):
        if time1[i] > time2[i]:
            return great
        if time1[i] < time2[i]:
            return less
        if time1[i] == time2[i] and i == (len(time1) - 1):
            return same


def read_config_time(object):
    """
    创建一个符合python规范的时间内容

    :param object: 必须经过例如crate_config_time之类的操作
    :return:
    """
    temp = list(object)
    temp2 = []
    temp2.append(int(temp[0:4]))  # 年
    temp2.append(int(temp[4:7]))  # 月
    temp2.append(int(temp[7:9]))  # 日
    temp2.append(int(temp[10:13]))  # 小时
    temp2.append(int(temp[13:15]))  # 分钟
    temp2.append(int(temp[15:17]))  # 秒
    return temp2


def crate_config_time(object):
    """
    创建一个用于配置的文件的时间string字符串。包含年月日小时分钟秒

    :param object: 必须经过read_config_time函数或相似的处理
    :return: 将“8”转换为“08”的一个列表
    """
    temp = list(object)
    temp2 = []
    if len(temp) == 6:
        for i in range(len(temp)):
            if i < 1:
                temp2.append(str(temp[i]))
            else:
                temp3 = str(temp[i])
                if int(temp3) < 10 and len(temp3) != 2:
                    temp3 = "0" + temp3
                    temp2.append(temp3)
                else:
                    temp2.append(str(temp[i]))
    else:
        return 1
    return temp2


def wait_input(object, lang):
    content = object[0]
    if object[1] == "None":
        inputs = ""
    else:
        inputs = object[1]
    print(content)
    if inputs != "":
        flag = True
        while flag:
            flag = False
            temp = input()
            if temp <= 0 or temp > len(object[1]):
                print(lang)
                flag = True
    return object[1][str(temp)]
