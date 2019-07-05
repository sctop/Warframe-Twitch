from module.Translation import get_lang, TranslationFile
from module.Config import detect, NoSuchFile, ConfigReader, crate
import subprocess
from module.time import wait_input
import json
from module.log import log_format, write
from module.system import get_info


class Init():
    def __init__(self, log):
        """
        返回配置文件信息

        :param log:
        """
        self.logname = "log/" + log + ".log"
        self.main()

    def main(self):
        # 日志
        try:
            write(log_format("Asia/Taipei", "Init test (init.py)", "info"), self.logname)
        except Exception as e:
            print("Init Error with exit code 1")
            print("Information: Can't crate and write the log file!")
            print(e)
            input()
            return 1
        # 全局配置文件
        try:
            glfile = ConfigReader("global.json", False, "")
        except FileNotFoundError:
            write(log_format("Asia/Taipei","Can't open the global config file! (init.py)","error"),self.logname)
            print("Init Error with exit code 1")
            print("Information: Can't open the global config file!")
            print("Re-download the file or the whole project!")
            input()
            return 1
        if glfile.file_content["new"] == "True" or glfile.file_content["lang"] == '':
            write(log_format("Asia/Taipei", "An new user or can't reach the language information. (init.py)", "info"), self.logname)
            temp = self.lang()
            with open("global.json", mode='r', encoding='UTF-8') as file:
                temp2 = json.load(file)
            temp2["lang"] = temp
            temp2["new"] = "False"
            with open("global.json", mode='w', encoding='UTF-8') as file:
                json.dump(temp2, file)
            self.content = TranslationFile(temp2["lang"]).content
        else:
            write(log_format("Asia/Taipei", "Loading the language information. (init.py)", "info"),self.logname)
            self.content = TranslationFile(glfile.file_content["lang"]).content
        write(log_format("Asia/Taipei", "Successfully to load the language information! (init.py)", "info"), self.logname)
        write(log_format("Asia/Taipei", "Global File: " + str(glfile.file_content) + " (init.py)", "info"), self.logname)
        # 读取配置文件
        try:
            self.temp = detect()
        except NoSuchFile:
            self.temp = wait_input(self.content["NoSuchFile"], self.content["InvaidInput"])
        if self.temp == "New":
            crate(self.content)
        elif self.temp == "Open":
            print(self.content["NoSuchFile_open"], self.content["InvaidInput"])
            while True:
                self.temp = input()
                try:
                    self.temp = ConfigReader("config/" + self.temp, False, True)
                except FileNotFoundError:
                    print(self.content["InvaidInput"])
                else:
                    break
        elif self.temp == "Exit":
            return 1
        # 系统信息
        temp2 = get_info("ALL")
        temp3 = "CPU: " + str(temp2["cpu"]["physical"]) + "/" + \
                str(temp2["cpu"]["logical"]) + " " + str(temp2["cpu"]["used"])
        temp3 = temp3 + "\n" + "Memory: " + str(temp2["mem"]["virtual"]["total"]) + \
                "/" + str(temp2["mem"]["virtual"]["used"]) + "(" + \
                str(temp2["mem"]["virtual"]["used_per"]) + ")" + \
                "/" + str(temp2["mem"]["virtual"]["available"])
        temp3 = temp3 + "\n" + "Network: " + str(temp2["network"]["ip"]) + \
                " @ " + str(temp2["network"]["mac"])
        temp3 = temp3 + "\n" + "System: " + str(temp2["system"]["OS"]) + " " + \
                str(temp2["system"]["version"]) + " on " + str(temp2["system"]["machine"])
        write(log_format("Asia/Taipei", "\n" + str(temp3) + " (init.py)", "info"), self.logname)
        return self.temp

    def lang(self):
        print("Select Language:")
        try:
            alllang = get_lang()
        except Exception as e:
            write(log_format("Asia/Taipei", str(e) + " (init.py)", "error"), self.logname)
            print("Error:", e)
            print("Check your program if it is complete!")
            input()
        for n, v in alllang.items():
            print(str(n)+'. '+ v)
        print("\nSelect: ",end='')
        while True:
            temp = input()
            if int(temp) > len(alllang) or int(temp) <= 0:
                print("Invaid Input! Try again:", end="")
            else:
                break
        print("Loading language file...")
        self.content = TranslationFile(alllang[str(temp)]).content
        write(log_format("Asia/Taipei", "Load the file of Translation successfully! (init.py)", "info"), self.logname)
        subprocess.call("cls", shell=True)
        return alllang[str(temp)]
