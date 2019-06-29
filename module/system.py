import psutil
import os


class ThreadExitError(Exception):
    def __init__(self, code=1, message="Process unexpectedly quits", args=("Process unexpectedly quits",)):
        self.args = args
        self.message = message
        self.code = code


class ThreadCheck():
    def __init__(self, thread_name, thread_pos, config, url):
        self.__THREAD__ = str(thread_name)
        self.__THREADPOS__ = str(thread_pos)
        self.__URL__ = str(url)

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
        if self.check() == False:
            os.popen("taskkill /T /F /IM " + self.__THREAD__)

    def restart(self):
        os.popen('"' + str(self.__THREADPOS__) + '"' + self.config.file_content["browser"]["command_format"] + self.url)
        raise ThreadExitError("Thread exit in unknown case")

    def all_thread(self):
        thread_pid = []
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            # get process name according to pid
            process_name = p.name()
            # kill process "sleep_test1"
            if str(self.__THREAD__) == process_name:
                thread_pid.append(int(p.pid))
        return thread_pid


def get_info(content):
    """
    一个获取系统CPU 内存 IP MAC的函数

    :param content: 可以传入带“CPU”“MEM”“NET”内容的列表以获得需要的数据
    :return: 返回所需要的数据
    """
    cpu = "Unknown"
    mem = "Unknown"
    ip = "Unknown"
    mac = "Unknown"
    if "CPU" in content or content == "ALL":
        cpu = {"logical": psutil.cpu_count(), "physical": psutil.cpu_count(logical=False),
               "used": {}}
        temp = list(psutil.cpu_percent(percpu=True))
        for i in range(len(temp)):
            cpu["used"][i] = temp[i]
    if "MEM" in content or content == "ALL":
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
        ip = list(psutil.net_if_addrs()["以太网"][1])[1]
        mac = psutil.net_if_addrs()["以太网"][0][1]
    return {"cpu": cpu, "mem": mem, "network": {"ip": ip, "mac": mac}}
