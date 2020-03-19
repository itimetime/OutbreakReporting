#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Colin
@file: th.py
@time: 2020/01/{DAY}
"""

import threading
import time

def cd():

    for i in range(5):
        print('test ',i)
        time.sleep(1)


thread = threading.Thread(target=cd)
thread.start()

for i in range(5):
    print('main ', i)
    time.sleep(1)


