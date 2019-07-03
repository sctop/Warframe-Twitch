"""
Just for basic function.
"""
from module.init import Init
from sys import exit
from module.time import format_time

__LOG__ = format_time("Asia/Taipei", mode="nospace")
status = Init(__LOG__)
if status == 1:
    exit()
