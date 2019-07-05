from module.time import wait_input
from module.time import WhatTheFuckError
import subprocess
import json
from module.Config import crate
from module.log import *


class Start():
    def __init__(self, lang, check,log):
        """
        返回文件名

        :param lang:
        :param check:
        """
        self.lang = lang
        self.content = check
        self.log = log
        subprocess.call("cls", shell=True)
        self.run()

    def run(self):
        self.welcome()
        if self.content[0] == "md5":
            print(self.lang["Main1"])
            while True:
                temp = input()
                if int(temp) > 4 or int(temp) < 1:
                    print(self.lang["InvaidInput"])
                else:
                    subprocess.call("cls", shell=True)
                    if int(temp) == 1:
                        crate(self.lang)
                    elif int(temp) == 2:
                        self.open()
                    elif int(temp) == 3:
                        self.filename = "config/default.json"
                    break
        write(log_format("Asia/Taipei", "Get the name of the config file: "+str(self.filename)+" (start.py)", "info"), self.log)


    def open(self):
        print(self.lang["OpenFileTitle"])
        if self.content[0] == "md5":
            write(log_format("Asia/Taipei","Multi-file detected! (start.py)","info"),self.log)
            num = 1
            select = {}
            for n, v in self.content[1].items():
                select[str(num)] = n
                num += 1
            for n, v in select.items():
                print(str(n) + ": " + str(v))
            print(str(num) + ": " + str(self.lang["OpenFile"]))
            print("------------------------")
            while True:
                temp = input()
                if int(temp) > len(select) + 1 or int(temp) < 1:
                    print(self.lang["InvaidInput"])
                else:
                    if int(temp) == num:
                        temp = self.open_other()
                    else:
                        temp = select[str(temp)]
                    break
        elif self.content[0] == "Single":
            write(log_format("Asia/Taipei", "Default and user file detected! (start.py)", "info"), self.log)
            print("1. config/default.json")
            print("2. config/user.json")
            print("3. " + self.lang["OpenFile"])
            while True:
                temp = input()
                if int(temp) < 1 or int(temp) > 3:
                    print(self.lang["InvaidInput"])
                else:
                    if int(temp) == 1:
                        temp = "config/default.json"
                    elif int(temp) == 2:
                        temp = "config/user.json"
                    elif int(temp) == 3:
                        temp = self.open_other()
                    break
        elif self.content[0] == "user":
            write(log_format("Asia/Taipei", "User file detected! (start.py)", "info"), self.log)
            print("1. config/user.json")
            print("2. " + self.lang["OpenFile"])
            while True:
                temp = input()
                if int(temp) < 1 or int(temp) > 3:
                    print(self.lang["InvaidInput"])
                else:
                    if int(temp) == 1:
                        temp = "config/user.json"
                    elif int(temp) == 2:
                        temp = self.open_other()
                    break
        elif self.content[0] == "default":
            write(log_format("Asia/Taipei", "Default file detected! (start.py)", "info"), self.log)
            print("1. config/default.json")
            print("2. " + self.lang["OpenFile"])
            while True:
                temp = input()
                if int(temp) < 1 or int(temp) > 3:
                    print(self.lang["InvaidInput"])
                else:
                    if int(temp) == 1:
                        temp = "config/default.json"
                    elif int(temp) == 2:
                        temp = self.open_other()
                    break
        else:
            raise WhatTheFuckError
        self.filename = temp
        subprocess.call("cls", shell=True)

    def open_other(self):
        subprocess.call("cls", shell=True)
        write(log_format("Asia/Taipei", "Skip to 'open_other' function (start.py)", "info"), self.log)
        print(self.lang["OpenFileTip"])
        while True:
            temp = str(input())
            try:
                with open("config/" + temp + ".json", mode='r', encoding='UTF-8') as file:
                    temp2 = json.load(file)
            except FileNotFoundError:
                print(self.lang["InvaidInput"])
            else:
                return "config/" + temp + ".json"

    def welcome(self):
        print(self.lang["PreWarning"])
        print(self.lang["About_program"])
        input()
        subprocess.call("cls", shell=True)
