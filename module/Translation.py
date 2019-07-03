import json


class TranslationFile():
    def __init__(self, FilePos):
        self.__FilePos__ = FilePos
        self.load()

    def load(self):
        with open(self.__FilePos__, mode='r', encoding="UTF-8") as transfile:
            self.content = json.load(transfile)

    def get(self, id):
        return [self.content[str(id)][0], self.content[str(id)][1]]


def add_translation(LangPos, LangName, AllPos="../lang/all.json"):
    # 测试文件
    try:
        with open(LangPos, mode='r', encoding="UTF-8") as file:
            content = json.load(file)
    except FileNotFoundError:
        return 1
    # 写入json
    with open(AllPos, mode='r', encoding="UTF-8") as file:
        content = json.load(file)
    content[str(LangName)] = LangPos
    with open(AllPos, mode='w', encoding="UTF-8") as file:
        json.dump(content, file)
    return 0


def del_translation(LangName, AllPos="../lang/all.json"):
    with open(AllPos, mode='r', encoding="UTF-8") as file:
        content = json.load(file)
    del content[str(LangName)]
    with open(AllPos, mode='w', encoding="UTF-8") as file:
        json.dump(content, file)


def get_lang(AllPos="lang/all.json"):
    with open(AllPos, mode='r', encoding="UTF-8") as file:
        content = json.load(file)
    print(content)
    flag = True
    while flag:
        flag = False
        for n, v in content.items():
            try:
                with open(v, mode='r', encoding='UTF-8') as lang_file:
                    temp = json.load(lang_file)
            except FileNotFoundError:
                del content[n]
                flag = True
                break
    name = {}
    num = 1
    for v in content.values():
        name[str(num)] = v
        num += 1
    return name
