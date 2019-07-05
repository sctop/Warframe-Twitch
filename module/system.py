import psutil
import os
import platform
from time import sleep

class ThreadExitError(Exception):
    def __init__(self, code=1, message="Process unexpectedly quits", args=("Process unexpectedly quits",)):
        self.args = args
        self.message = message
        self.code = code


class Thread():
    def __init__(self, thread_name, thread_pos):
        self.__THREAD__ = str(thread_name)
        self.__THREADPOS__ = str(thread_pos)

    def check(self):
        found = False
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            # get process name according to pid
            process_name = p.name()
            # kill process "sleep_test1"
            if str(self.__THREAD__) == process_name:
                found = True
        return found

    def kill(self):
        os.popen("taskkill /T /F /IM " + self.__THREAD__)

    def start(self, url):
        os.popen('"' + str(self.__THREADPOS__) + '" "' + url + '"')

    def all_thread(self):
        thread_pid = []
        sleep(2)
        pids = psutil.pids()
        for pid in pids:
            try:
                p = psutil.Process(pid)
                # get process name according to pid
                process_name = p.name()
                if str(self.__THREAD__) == process_name:
                    thread_pid.append(int(p.pid))
            except Exception as e:
                print(e)
        return thread_pid


def get_info(content):
    """
    一个获取系统CPU 内存 IP MAC SYSTEM的函数

    :param content: 可以传入带“CPU”“MEM”“NET”“SYSTEM”内容的列表以获得需要的数据
    :return: 返回所需要的数据
    """
    cpu = "Unknown"
    mem = "Unknown"
    ip = "Unknown"
    mac = "Unknown"
    system = "Unknown"
    if "CPU" in content or content == "ALL":
        # 返回{逻辑核心 物理核心 使用率}
        cpu = {"logical": int(psutil.cpu_count()), "physical": int(psutil.cpu_count(logical=False)),
               "used": psutil.cpu_percent()}
    if "MEM" in content or content == "ALL":
        # virtual(虚拟内存)返回 {总计 可用 使用率 使用值}
        # swap(交换内存)返回 {总计 使用率 使用值}
        mem = {"virtual": {}, "swap": {}}
        temp = list(psutil.virtual_memory())
        mem["virtual"]["total"] = temp[0]
        mem["virtual"]["available"] = temp[1]
        mem["virtual"]["used_per"] = temp[2]
        mem["virtual"]["used"] = temp[3]
        temp = list(psutil.swap_memory())
        mem["swap"]["total"] = temp[0]
        mem["swap"]["used"] = temp[1]
        mem["swap"]["used_per"] = temp[3]
    if "NET" in content or content == "ALL":
        # 由于系统版本不同可能引发错误
        try:
            ip = list(psutil.net_if_addrs()["以太网"][1])[1]
            mac = psutil.net_if_addrs()["以太网"][0][1]
        except KeyError:
            try:
                ip = list(psutil.net_if_addrs()["本地连接"][1])[1]
                mac = psutil.net_if_addrs()["本地连接"][0][1]
            except Exception:
                ip = "0.0.0.0"
                mac = "000000000000"
    if "SYS" in content or content == "ALL":
        temp = platform.uname()
        temp = list(temp)
        system = {"OS": temp[0], "version": temp[3],
                  "machine": temp[4]}
    return {"cpu": cpu, "mem": mem, "network": {"ip": ip, "mac": mac}, "system": system}
