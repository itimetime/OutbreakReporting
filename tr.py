#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Colin
@file: tr.py
@time: 2020/01/{DAY}
"""
def c(func):
    def wrapper():
        func()
        with open("r.txt",'r') as f:
            # print(f.read())
            return f.read()
    return wrapper()
@c
def a():
    with open("r.txt",'w') as f:
        f.write("hahahah415456")

keyword = "神农架林区"
search_result = ''
for i in range(2, len(keyword)+1):
    if i > len(keyword) or i > 5:
        break
    temp_keyword = keyword[:i]
    print(temp_keyword)
    search_result = ''
    if search_result != '':
        break
    else:
        search_result = ''
        if search_result != '':
            break
        else:
            continue