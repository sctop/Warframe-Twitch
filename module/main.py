from module.system import Thread, get_info
import subprocess
from time import sleep
from module.time import *
from module.mail import mail_format, mail
from module.log import *
from module.Config import crate_mail, add_md5, get_md5, ConfigReader
from module.log import *

class Main():
    def __init__(self, lang, con, log, mailenable):
        self.lang = lang
        self.content = ConfigReader(con, True, False).file_content
        self.thread = Thread(self.content["browser"]["thread_name"],
                             self.content["browser"]["pos"])
        self.logname = log
        self.mail = mailenable
        self.run()

    def run(self):
        self.enable_mail()
        new = self.crate()
        write(log_format("Asia/Taipei", "Detected the new threads of browser: "+str(new)+" (main.py)", "info"),self.logname)
        # 幻纹
        timer = 0
        self.temp = self.now_init(self.content["delay"]["live"]["timer"]["Ephemera"]["lasting"])
        while True:
            now = read_config_time(format_time("EST", mode="normal"))
            # 对比
            flag = time_check((now[0], now[1],now[2], now[3],
                              int(now[4]), now[5]),
                              self.temp)
            temp2 = self.anti_crash("Ephemera")
            if temp2:
                write(log_format("Asia/Taipei", "Browser crashed!", "info"),
                      self.logname)
                print(self.lang["Main_crashed"])
                timer = -1
            if timer > self.content["delay"]["live"]["timer"]["Ephemera"]["lasting"]:
                write(log_format("Asia/Taipei", "Finished the time of watching Ephemera!", "info"),
                      self.logname)
                print(self.lang["Main_finished"])
                break
            if flag == [False, True, False] or flag == [False, False, True]:
                write(log_format("Asia/Taipei", "Out of the time of watching for getting Ephemera!", "info"),
                      self.logname)
                print(self.lang["Main_outed"])
                break
            timer += 1
            sleep(0.5)
        # 循环等待
        while True:
            temp = format_time("EST", mode="normal")
            temp = read_config_time(temp)
            temp = date_format(temp[0], temp[1], temp[2], temp[3],
                               int(temp[4]), temp[5])
            flag = time_check((temp[0], temp[1], temp[2], temp[3],
                               int(temp[4]), temp[5]),
                              read_config_time(self.content["delay"]["live"]["timer"]["Warframe"]["begin"]))
            if flag == [False, True, False] or flag == [False, False, True]:
                write(log_format("Asia/Taipei", "The time for getting Warframe began!", "info"),
                      self.logname)
                print(self.lang["Main_beginnext"])
                break
        # Warframe
        timer = 0
        self.temp = self.now_init(self.content["delay"]["live"]["timer"]["Warframe"]["lasting"])
        while True:
            now = read_config_time(format_time("EST", mode="normal"))
            # 对比
            flag = time_check((now[0], now[1], now[2], now[3],
                               int(now[4]), now[5]),
                              self.temp)
            temp2 = self.anti_crash("Warframe")
            if temp2:
                write(log_format("Asia/Taipei", "Browser crashed!", "info"),
                      self.logname)
                print(self.lang["Main_crashed"])
                timer = -1
            if timer > self.content["delay"]["live"]["timer"]["Warframe"]["lasting"]:
                write(log_format("Asia/Taipei", "Finished the time of watching for getting Warframe!", "info"),
                      self.logname)
                print(self.lang["Main_finished"])
                break
            if flag == [False, True, False] or flag == [False, False, True]:
                write(log_format("Asia/Taipei", "Out of the time of watching for getting Warframe!", "info"),
                      self.logname)
                print(self.lang["Main_outed"])
                break
            timer += 1
            sleep(0.5)

    def crate(self):
        self.thread.start(self.content["link"]["WarframeAccount"])
        write(log_format("Asia/Taipei", "Successfully to open the Warframe Center page! (main.py)", "info"), self.logname)
        sleep(35)
        temp1 = self.thread.all_thread()
        self.thread.start(self.content["link"]["Twitch"])
        sleep(10)
        write(log_format("Asia/Taipei", "Successfully to open the Twitch page! (main.py)", "info"),self.logname)
        temp2 = self.thread.all_thread()
        temp3 = []
        for i in range(len(temp1)):
            if temp1[i] in temp2:
                temp3.append(temp1[i])
        for i in temp3:
            temp2.remove(i)
        print(self.lang["Main_new"] + str(temp2))
        return temp2

    def anti_crash(self, time):
        # 内存爆炸
        temp = get_info("MEM")
        if float(temp["mem"]["virtual"]["used_per"]) >= 80:
            self.anti_crash_sub(time)
            return True
        # 自己爆炸
        temp = self.thread.all_thread()
        if len(temp) < 4:
            self.anti_crash_sub(time)
            return True
        return False

    def anti_crash_sub(self, time):
        self.thread.kill()
        write(log_format("Asia/Taipei", "Browser crashed and killed all threads of the browser.", "warning"),
              self.logname)
        temp = read_config_time(format_time("EST", mode="normal"))
        flag = time_check(date_format(temp[0], temp[1], temp[2],
                                      temp[3], temp[4] + 30, temp[5]),
                          read_config_time(self.content["delay"]["live"]["timer"][str(time)]["end"]))
        if flag == [False, False, True] or flag == [False, True, False]:
            temp = log_format("Asia/Taipei", "The time is out of the range of the time", "warning")
            if self.mail != False:
                temp2 = mail_format([self.lang["Mail_hello"],
                                     self.lang["Mail_end"]], temp)
                self.mail.send_mail(temp2)
            write(str(temp), self.logname)
        self.thread.start(self.content["link"]["Twitch"])
        write(log_format("Asia/Taipei", "Crating a new end time...", "info"),
              self.logname)
        self.temp = self.now_init(self.content["delay"]["live"]["timer"][str(time)]["lasting"])

    def enable_mail(self):
        if self.content["mail"]["enable"] == "True" and self.content["mail"]["host"] != '':
            self.mail = mail(self.content["mail"]["host"],
                             self.content["mail"]["port"],
                             [self.content["mail"]["username"],
                              self.content["mail"]["address"]],
                             self.content["mail"]["password"])
        elif self.content["mail"]["enable"] == "True" and self.content["mail"]["host"] == '':
            crate_mail(self.lang, self.content)
            add_md5(get_md5(self.content), self.fp)
            write(log_format("Asia/Taipei", "Crated a mail object.", "info"), self.logname)
        else:
            self.mail = False
            write(log_format("Asia/Taipei", "User disabled the mail function.", "info"), self.logname)

    def now_init(self, lasting):
        temp = read_config_time(format_time("EST", mode="normal"))
        temp = date_format(temp[0], temp[1], temp[2], temp[3],
                           temp[4], temp[5] + lasting)
        write(log_format("Asia/Taipei", "The end time: "+str((temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]))+" (main.py)", "info"),
              self.logname)
        return temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]