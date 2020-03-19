#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Colin
@file: process_start.py
@time: 2020/01/{DAY}
"""
from email_check_unseen_server import GetMail
import threading
from email_send_server import send_regularly
def process_start():
    print("正在运行")
    GetMail.mail_login(mail_type='imap.qq.com', mail_ssl=993, mail_username='icktime@qq.com',
                                 mail_password='czizkaacaupwbbdf')#ccfgciozczzhbeig



if __name__ == "__main__":
    # 执行程序
    print("开始运行主程序")
    print("???")
    process_start()



