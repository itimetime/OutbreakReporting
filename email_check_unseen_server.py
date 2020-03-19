#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Colin
@file: 邮箱未读邮件自动回复.py
@time: 2020/01/{DAY}
"""

# coding:utf-8
import email
import time
import imaplib
from email_parsing_service import  get_send_mail,get_request_content
from email_send_server import send_request_mail, login_mail_stmp


class GetMail(object):
    @classmethod
    def mail_login(self, mail_type, mail_ssl, mail_username, mail_password):
        while True:
            """邮箱登录,并检索目标人未读邮件"""
            print("正在和imap服务器建立连接")
            get_server = imaplib.IMAP4_SSL(mail_type, mail_ssl)
            print("进行登录")
            get_server.login(mail_username, mail_password)
            cnt = 0
            while True and cnt <= 160:
                get_server.select()#("INBOX")  # 默认收件夹是INBOX
                print("登录成功并检查未读邮件")
                typ, data = get_server.search(None, 'unseen') # SEEN--已读邮件,UNSEEN--未读邮件,ALL--全部邮件
                if data[0]:
                    number_list = data[0].split()
                    # 邮件列表,使用空格分割得到邮件索引
                    for the_mail_number in number_list:
                        print("获取到未读邮件")
                        print(number_list)
                        # 将邮件标记为已读
                        get_server.store(the_mail_number, '+FLAGS', '\\SEEN')
                        # 邮件内容详情
                        mail_data = get_server.fetch(the_mail_number, '(RFC822)')[1]
                        #  使用utf-8解码
                        text_data = mail_data[0][1].decode('utf8')
                        # 转换为email.message对象解析出邮件
                        message = email.message_from_string(text_data)
                        # msg = Parser().parsestr(msg_content)
                        print("进行解析对方邮件内容")
                        search_keyword = get_request_content(message,0)
                        print("成功读取内容："+str(search_keyword))
                        #获取邮件对象
                        if search_keyword != None:
                            receiver = get_send_mail(message)
                            print("解析发件人成功:"+receiver)
                            send_request_mail(receiver,search_keyword)
                    cnt += 1
                    print("休眠三十秒",cnt)
                    time.sleep(20)
                    continue
                # get_server.logout()
                else:
                    cnt +=1
                    print("未检索到未读邮件:次数",cnt)
                    print("休眠三十秒")
                    time.sleep(20)
                    continue


