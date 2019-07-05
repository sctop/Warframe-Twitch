import os, subprocess
from module.Config import ConfigReader
from random import randint
from module.time import *
from time import sleep
from module.system import Thread
from module.log import *


class Wait():
    def __init__(self, lang, fp, log):
        """
        等待直播开始的部分，程序主要部分
        """
        self.lang = lang
        self.fp = fp
        self.log = log
        subprocess.call("cls", shell=True)
        self.run()

    def run(self):
        self.file = ConfigReader(self.fp, True, False)
        write(log_format("Asia/Taipei","Successfully to read the config file! (wait.py)","info"),self.log)
        self.content = self.file.file_content
        self.mail_enable()
        # Cookies
        print(self.lang["OpenPageTip"])
        print(self.lang["OpenPageWarframe"])
        junk = input()
        os.popen('"' + self.content["browser"]["pos"] + '" ' + \
                 self.content["link"]["WarframeAccount"])
        write(log_format("Asia/Taipei", "Successfully to open the Warframe Center page! (wait.py)", "info"), self.log)
        print(self.lang["OpenPageTwitch"])
        junk = input()
        os.popen('"' + self.content["browser"]["pos"] + '" ' + \
                 self.content["link"]["Twitch"])
        write(log_format("Asia/Taipei", "Successfully to open the Twitch page! (wait.py)", "info"), self.log)
        junk = input()
        self.thread = Thread(self.content["browser"]["thread_name"], self.content["browser"]["pos"])
        self.thread.kill()
        write(log_format("Asia/Taipei", "Successfully to kill threads of browser! (wait.py)", "info"), self.log)
        subprocess.call("cls",shell=True)
        # 主循环
        time = read_config_time(self.content["delay"]["live"]["EST_in"])
        time_temp = time[:]  # 加计时器
        time_temp2 = ()  # 上方格式化后的
        time_temp3 = time[:]  # 直播标准时间
        sleep(3)
        write(log_format("Asia/Taipei", "The loop of waiting is starting!", "info"), self.log)
        print(self.lang["wait_loop1"])
        while True:
            # 获取下一循环时间
            timer = self.content["delay"]["sleep"]["time"]
            timer_add = randint(self.content["delay"]["sleep"]["range"][0],
                                self.content["delay"]["sleep"]["range"][0])
            timer = timer + timer_add
            time_temp[5] += timer
            time_temp2 = date_format(time_temp[0], time_temp[1],
                                     time_temp[2], time_temp[3],
                                     time_temp[4], time_temp[5])
            time_temp4 = date_format(time_temp2[0], time_temp2[1],
                                     time_temp2[2], time_temp2[3],
                                     time_temp2[4] + 5, time_temp2[5])
            flag = time_check((time_temp4[0],time_temp4[1],time_temp4[2],
                               time_temp4[3],time_temp4[4],time_temp4[5]),
                              time_temp3)
            if flag == [False, False, True] or flag == [False, True, False]:
                now = str(format_time("Asia/Taipei",mode="normal"))
                write(log_format("Asia/Taipei", "Begin soon detected (in 35min)! (wait.py)", "info"), self.log)
                write(log_format("Asia/Taipei", "The time of now: "+ str(now), "info"), self.log)
                print(self.lang["wait_loop2"]+now)
                while True:
                    now = read_config_time(format_time("EST", "normal"))
                    flag = time_check((now[0], now[1],now[2],
                                       now[3], now[4], now[5]),
                                      time_temp3)
                    if flag == [False, False, True] or flag == [False, True, False]:
                        break
                    sleep(0.5)
                write(write(log_format("Asia/Taipei", "Time out! Break the loop. (wait.py)", "info"), self.log))
                print(self.lang["wait_loop3"])
                break
            else:
                print(timer, time_temp2)
                sleep(timer)
            # 确认时间
            now = read_config_time(format_time("EST", mode="normal"))
            total_loading = int(self.content["delay"]["loading"]["WarframeAccount"] + \
                                self.content["delay"]["loading"]["Twitch"])
            flag = time_check(date_format(time_temp[0], time_temp[1],
                                          time_temp[2], time_temp[3],
                                          time_temp[4] + 10, time_temp[5] + total_loading),
                              time_temp3)
            if flag == [False, False, True] or flag == [False, True, False]:
                write(log_format("Asia.Taipei","Begin soon detected (in 10min)! (wait.py)","info"),self.log)
                write(log_format("Asia/Taipei", "The time of now: " + str(format_time("Asia/Taipei", mode="normal")), "info"),self.log)
                print(self.lang["wait_loop4"]+str(now))
                break
            else:
                self.open()


    def open(self):
        os.popen(self.content["browser"]["pos"] + \
                 self.content["link"]["WarframeAccount"])
        write(log_format("Asia/Taipei", "Successfully to open the Warframe Center page! (wait.py)", "info"), self.log)
        print(self.lang["sf_warframe"])
        sleep(self.content["delay"]["loading"]["WarframeAccount"] + 15)
        os.popen(self.content["browser"]["pos"] + \
                 self.content["link"]["Twitch"])
        write(log_format("Asia/Taipei", "Successfully to open the Twitch page! (wait.py)", "info"), self.log)
        print(self.lang["sf_twitch"])
        sleep(self.content["delay"]["loading"]["Twitch"])
        self.thread.kill()
        write(log_format("Asia/Taipei", "Successfully to kill threads of browser! (wait.py)", "info"), self.log)
        print(self.lang["sf_killthread"])

    def mail_enable(self):
        print(self.lang["Thread_enablemail"])
        temp =input()
        if temp == "1":
            self.mail = True
        else:
            self.mail = False
        subprocess.call("cls",shell=True)