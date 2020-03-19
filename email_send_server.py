#! /usr/bin/env python
#coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email_template import get_new_content,get_request_content
import time


host_server = 'smtp.qq.com'
sender_qq = 'icktime@qq.com'
pwd = 'czizkaacaupwbbdf'
sender_qq_mail = 'icktime@qq.com'
receivers = ['itimetime@qq.com',]#'905819139@qq.com']#,'itimeyoyo@gmail.com']
mail_title = '疫情实时动态播报'
def login_mail_stmp():
    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
    print("登录成功")
    return smtp

def send_regularly():
    while True:
        print("开始连接smtp服务器")
        smtp = login_mail_stmp()
        msg = MIMEMultipart()
        # 可选择发送html 和 plain
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = formataddr(["疫情播报小助手", sender_qq_mail])
        msg["To"] = Header("订阅用户",'UTF-8')  ## 接收者的别名

        # 邮件正文内容
        mail_content = get_new_content()
        msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
        try:
            smtp.sendmail(sender_qq_mail, receivers, msg.as_string())
            print("等待两个小时，再次发送")
            time.sleep(7200)
            continue
        except Exception as e:
            print("发送失败",e)
            time.sleep(7200)
            continue

def send_request_mail(receiver,keyword):
    print("开始连接smtp服务并进行登录")
    smtp = login_mail_stmp()
    mail_content,keyword = get_request_content(keyword)
    msg = MIMEMultipart()
    print("内容获取成功",msg)
    mail_title = str(keyword) + "查询结果"
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = formataddr(["疫情播报小助手", sender_qq_mail])
    msg["To"] = Header(receiver, 'utf-8')
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    try:
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        print("发送成功，接收人：",receiver)
    except Exception as e:
        print("发送失败",e,"重新登录并开始发送")
        smtp = login_mail_stmp()
        print("成功进行登录")
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())






















    # 构造附件1，传送当前目录下的 test.txt 文件
    # att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # att1["Content-Disposition"] = 'attachment; filename="123.txt"'
    # msg.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('tools.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="yiibai.txt"'
    # msg.attach(att2)



# smtp.quit()

