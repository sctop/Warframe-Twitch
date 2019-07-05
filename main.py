"""
Just for basic function.
"""
from module.init import Init
from sys import exit
from module.time import format_time
from module.start import Start
from module.wait import Wait
from module.main import Main
import subprocess
from module.log import *

__LOG__ = "log/"+format_time("Asia/Taipei", mode="nospace")
init = Init(__LOG__)
if init == 1:
    exit()

__Lang__ = init.content
__ConfigFileMode__ = init.temp

__fp__ = Start(__Lang__, __ConfigFileMode__, __LOG__).filename

__file_content__ = Wait(__Lang__, __fp__,__LOG__).file

Main(__Lang__, __fp__, __LOG__)

# 最后的
subprocess.call("cls",shell=True)
write(log_format("Asia/Taipei","Finished the whole program!","info"),__LOG__)
print(__Lang__["End"])
junk = input()
exit()
