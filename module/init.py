from module.Translation import get_lang, TranslationFile
from module.Config import detect, NoSuchFile, ConfigReader, crate
import subprocess
from module.time import wait_input
import json
from module.log import log_format, write
from module.system import get_info


class Init():
    def __init__(self, log):
        self.logname = "log/" + log + ".log"
        self.main()

    def main(self):
        # 全局配置文件
        try:
            glfile = ConfigReader("global.json", False, "")
        except FileNotFoundError:
            print("Init Error with exit code 1")
            print("Information: Can't open the global config file!")
            print("Re-download the file or the whole project!")
            input()
            return 1
        if glfile.file_content["new"] == "True" or glfile.file_content["lang"] == '':
            temp = self.lang()
            with open("global.json", mode='r', encoding='UTF-8') as file:
                temp2 = json.load(file)
            temp2["lang"] = temp
            with open("global.json", mode='w', encoding='UTF-8') as file:
                json.dump(temp2, file)
        else:
            self.content = TranslationFile(glfile.file_content["lang"]).content
        # 读取配置文件
        try:
            temp = detect()
        except NoSuchFile:
            temp = wait_input(self.content("NoSuchFile"), self.content("InvaidInput"))
        if temp == "New":
            crate()
        elif temp == "Open":
            print(self.content["NoSuchFile_open"], self.content("InvaidInput"))
            while True:
                temp = input()
                try:
                    temp = ConfigReader("config/" + temp, False, True)
                except FileNotFoundError:
                    print(self.content("InvaidInput"))
                else:
                    break
        elif temp == "Exit":
            return 1
        # 日志
        try:
            write(log_format("Asia/Taipei", "Init test", "info"), self.logname)
        except Exception as e:
            print("Init Error with exit code 1")
            print("Information: Can't crate and write the log file!")
            print(e)
            input()
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
        write(log_format("Asia/Taipei", "\n" + temp3, "info"), self.logname)
        return 0

    def lang(self):
        print("Select Language:")
        try:
            alllang = get_lang()
        except Exception as e:
            print("Error:", e)
            print("Check your program if it is complete!")
            input()
        for n, v in alllang.items():
            print(n, v)
        while True:
            temp = input()
            if int(temp) > len(alllang) or int(temp) <= 0:
                print("Invaid Input! Try again:", end="")
            else:
                break
        print("Loading language file...")
        self.content = TranslationFile(alllang[str(temp)]).content
        subprocess.call("cls", shell=True)
        return alllang[str(temp)]
