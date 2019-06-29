import json
import hashlib


# 异常
class NoSuchFile(Exception):
    def __init__(self, code=1):
        self.code = code


class ConfigReader():

    def __init__(self, FilePos, hash, HashPos):
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
        self.md5 = hashlib.md5(str(self.content).encode(encoding="UTF-8")).hexdigest()
        if md5_file_content[self.FilePos] == self.md5:
            return [0, self.md5]
        else:
            return [1, self.md5]

    def change_md5(self):
        with open(self.FilePos, mode='r', encoding="UTF-8") as file:
            file_content = json.load(file)
        with open(self.HashPos, mode='r', encoding="UTF-8") as md5_file:
            md5_file_content = json.load(md5_file)
        md5_file_content[self.FilePos] = hashlib.md5(str(file_content).encode(encoding="UTF-8")).hexdigest()
        with open(self.HashPos, mode='w', encoding="UTF-8") as md5_file:
            json.dump(md5_file_content, md5_file)


def add_md5(new_md5, FilePos, HashPos):
    with open(HashPos, mode='r', encoding="UTF-8") as md5_file:
        md5_file_content = json.load(md5_file)
    md5_file_content[FilePos] = new_md5
    with open(HashPos, mode='w', encoding="UTF-8") as md5_file:
        json.dump(md5_file_content, md5_file)


def delete_md5(FilePos, HashPos):
    with open(HashPos, mode='r', encoding="UTF-8") as md5_file:
        md5_file_content = json.load(md5_file)
    del md5_file_content[FilePos]
    with open(HashPos, mode='w', encoding="UTF-8") as md5_file:
        json.dump(md5_file_content, md5_file)


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
            with open("config/default.json", mode - 'r', encoding='UTF-8') as de_file:
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
        return md5_con
