import json
import hashlib
from module.time import read_config_time, crate_config_time, wait_input


# 异常
class NoSuchFile(Exception):
    def __init__(self, code=1):
        self.code = code


class ConfigReader():

    def __init__(self, FilePos, hash, new, HashPos="config/md5.json"):
        """
        这个类是用来读取配置文件的。
        您应该使用一个for循环在类外来创建一个基于该类的对象，而不是在这个类中循环创建。
        在正常情况下，该类将会与config目录下的“MD5.json”的内容进行比对，以确保文件并未损坏。

        :param FilePos:文件位置，建议使用相对路径
        :param hash:是否要md5验证，TRUE/FALSE
        :param HashPos:md5文件位置，建议使用相对路径
        """
        self.FilePos = FilePos
        self.hash = hash
        self.HashPos = HashPos
        if new:
            self.change_md5()
        self.load()

    def load(self):
        with open(self.FilePos, mode='r', encoding="UTF-8") as file:
            self.file_content = json.load(file)
        if self.hash:
            self.md5_status = self.md5_hash()
        else:
            self.md5_status = ["Unknown", "Unknown"]

    def md5_hash(self):
        with open(self.HashPos, mode='r', encoding="UTF-8") as md5_file:
            md5_file_content = json.load(md5_file)
        self.md5 = get_md5(self.file_content)
        if md5_file_content[self.FilePos] == self.md5:
            return [0, self.md5]
        else:
            return [1, self.md5]

    def change_md5(self):
        with open(self.FilePos, mode='r', encoding="UTF-8") as file:
            file_content = json.load(file)
        try:
            with open(self.HashPos, mode='r', encoding="UTF-8") as md5_file:
                md5_file_content = json.load(md5_file)
        except FileNotFoundError:
            md5_file_content = {}
        md5_file_content[self.FilePos] = get_md5(file_content)
        with open(self.HashPos, mode='w', encoding="UTF-8") as md5_file:
            json.dump(md5_file_content, md5_file)


def add_md5(new_md5, FilePos, HashPos="config/md5.json"):
    with open(HashPos, mode='r', encoding="UTF-8") as md5_file:
        md5_file_content = json.load(md5_file)
    md5_file_content[FilePos] = new_md5
    with open(HashPos, mode='w', encoding="UTF-8") as md5_file:
        json.dump(md5_file_content, md5_file)


def delete_md5(FilePos, HashPos="config/md5.json"):
    with open(HashPos, mode='r', encoding="UTF-8") as md5_file:
        md5_file_content = json.load(md5_file)
    del md5_file_content[FilePos]
    with open(HashPos, mode='w', encoding="UTF-8") as md5_file:
        json.dump(md5_file_content, md5_file)


def get_md5(FileContent):
    return hashlib.md5(str(FileContent).encode(encoding="UTF-8")).hexdigest()


def detect():
    # 多个文件存在
    try:
        with open("config/md5.json", mode='r', encoding='UTF-8') as md5_file:
            md5_con = json.load(md5_file)
    except FileNotFoundError:
        # 用户和默认文件存在
        try:
            with open("config/user.json", mode='r', encoding='UTF-8') as user_file:
                user_con = json.load(user_file)
            with open("config/default.json", mode='r', encoding='UTF-8') as de_file:
                de_con = json.load(de_file)
        except FileNotFoundError:
            # 用户文件存在
            try:
                with open("config/user.json", mode='r', encoding="UTF-8") as user_file:
                    user_con = json.load(user_file)
            except FileNotFoundError:
                # 默认文件存在
                try:
                    with open("config/default.json", mode='r', encoding="UTF-8") as de_file:
                        de_con = json.load(de_file)
                except FileNotFoundError:
                    # 都不存在
                    raise NoSuchFile
                else:
                    return ["default", de_con]
            else:
                return ["user", user_con]
        else:
            return ["Single", de_file, user_file]
    else:
        # 检查是否有文件打不开的
        flag = True
        while flag:
            flag = False
            for n, v in md5_con.items():
                try:
                    with open(str(n), mode='r', encoding='UTF-8') as file:
                        temp = json.load(file)
                except FileNotFoundError:
                    del md5_con[n]
                    flag = True
                    break
                else:
                    if get_md5(temp) != v:
                        del md5_con[n]
                        flag = True
                        break
        with open("config/md5.json", mode='w', encoding='UTF-8') as file:
            json.dump(md5_con, file)
        return ["md5", md5_con]


# 创建新配置文件
def crate(object):
    dictionary = {}
    # 文件名
    print(object.content("Crate_filename"))
    filename = str(input())
    # Warframe个人中心链接
    print(object.content("Crate_WFAccount"))
    temp = str(input())
    dictionary["link"]["WarframeAccount"] = temp
    # Twitch直播链接
    print(object.content("Crate_Twitch"))
    temp = str(input())
    dictionary["link"]["Twitch"] = temp
    # 加载页面的延迟
    print(object.content("Crate_delay_loading1"))
    temp = str(input())
    dictionary["delay"]["loading"]["WarframeAccount"] = temp
    print(object.content("Crate_delay_loading2"))
    temp = str(input())
    dictionary["delay"]["loading"]["Twitch"] = temp
    # 周期等待时间
    print(object.content("Crate_delay_sleep1"))
    temp = str(input())
    dictionary["sleep"]["time"] = temp
    print(object.content("Crate_delay_sleep2"))
    temp = str(input())
    dictionary["sleep"]["range"][0] = temp
    print(object.content("Crate_delay_sleep3"))
    temp = str(input())
    dictionary["sleep"]["range"][1] = temp
    # 进入Twitch直播的时间
    print(object.content("Crate_live_estin"))
    while True:
        temp = input()
        if len(temp) != 18:
            print(object.content("InvaidInput"))
        else:
            dictionary["live"]["EST_in"] = temp
            break
    # 其它直播用时间
    dictionary["live"]["timer"]["Ephemera"]["begin"] = "2019-07-06 10:00:00"
    dictionary["live"]["timer"]["Ephemera"]["end"] = "2019-07-07 17:59:00"
    dictionary["live"]["timer"]["Ephemera"]["lasting"] = 1800
    dictionary["live"]["timer"]["Warframe"]["begin"] = "2019-07-06 18:00:00"
    dictionary["live"]["timer"]["Warframe"]["end"] = "2019-07-06 19:00:00"
    dictionary["live"]["timer"]["Warframe"]["lasting"] = 1800
    # 浏览器
    print(object.content("Crate_browser1"))
    temp = str(input())
    if temp[-4:] != ".exe":
        temp = temp + ".exe"
    dictionary["browser"]["pos"] = temp
    temp2 = temp[::-1]
    for i in range(len(temp2)):
        if temp2[i] == "\\":
            break
    temp = temp2[0:i][::-1]
    dictionary["browser"]["thread_name"] = temp
    with open("module/thread.json", mode='r', encoding='UTF-8') as file:
        con = json.load(file)
    dictionary["browser"]["name"] = con[temp]
    # 邮件
    crate_mail(object, dictionary)
    # 写入文件
    try:
        with open("config/" + filename, mode='r', encoding='UTF-8') as file:
            temp = json.load(file)
    except FileNotFoundError:
        pass
    else:
        temp = object.content("Crate_overwrite"), object.content("InvaidInput")
    if temp == "No":
        return 0
    with open("config/" + filename, mode='w', encoding='UTF-8') as file:
        json.dump(dictionary, file)
    # 文件md5
    temp = get_md5(str(dictionary))
    add_md5(temp, "config/" + filename)
    return 0


def crate_mail(object, dictionary):
    temp = wait_input(object.content("Crate_mail1"), object.content("InvaidInput"))
    if temp == "enable":
        print(object.content("Crate_mailwarn"))
        print(object.content("Crate_mail2"))
        temp = str(input())
        dictionary["mail"]["host"] = temp
        print(object.content("Crate_mail3"))
        temp = int(input())
        dictionary["mail"]["port"] = temp
        print(object.content("Crate_mail4"))
        temp = str(input())
        dictionary["mail"]["username"] = temp
        print(object.content("Crate_mail5"))
        temp = str(input())
        dictionary["mail"]["username"] = temp
        print(object.content("Crate_mail6"))
        temp = str(input())
        dictionary["mail"]["address"] = temp
        dictionary["mail"]["enable"] = "True"
    else:
        dictionary["mail"]["address"] = ""
        dictionary["mail"]["password"] = ""
        dictionary["mail"]["host"] = ""
        dictionary["mail"]["port"] = ""
        dictionary["mail"]["username"] = ""
        dictionary["mail"]["enable"] = "False"
