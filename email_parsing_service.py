#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Colin
@file: MailParsingService.py
@time: 2020/01/{DAY}
"""

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


import poplib
import os

def login_method_pop3():
    # 输入邮件地址, 口令和POP3服务器地址:
    email = 'icktime@qq.com'
    password = 'czizkaacaupwbbdf'
    pop3_server = 'pop.qq.com'

    # 连接到POP3服务器:
    server = poplib.POP3(pop3_server)
    # 可以打开或关闭调试信息:
    server.set_debuglevel(0)
    # 可选:打印POP3服务器的欢迎文字:
    print(server.getwelcome().decode('utf-8'))

    # 身份认证:
    server.user(email)
    server.pass_(password)

    # stat()返回邮件数量和占用空间:
    print('Messages: %s. Size: %s' % server.stat())
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    # print(index)
    resp, lines, octets = server.retr(index)
    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)

    # server.dele(index)
    # 关闭连接:
    server.quit()
    return msg

# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, decode_str(addr))
            #       这里有点问题 把addr也进行解析，原版是只把hdr进行解析
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)

    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))
# def deco(func):
#     def wrapper(*args, **kwargs):
#         func(*args,**kwargs)
#         try:
#             with open('search.temp','r') as f:
#                 data = f.read()
#                 print("成功解析并读取"+data)
#                 os.remove("search.temp")
#                 return data
#         except:
#             return None
#     return wrapper
def get_request_content(*args,**kwargs):
    print("开始进行解析")
    get_request_content1(*args,**kwargs)
    with open('search.temp','r') as f:
        data = f.read()
        print("成功解析"+data)
        return data


def get_request_content1(msg, indent):
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%s--------------------' % ('  ' * indent))
            if n == 0:
                get_request_content1(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
                print("截取到的请求内容为："+str(content).split('\r')[0])
                a = str(content).split('\r')[0]
                if a != None:
                    with open('search.temp','w') as f:
                        f.write(a)


        #     print('%sText: %s' % ('  ' * indent, content + '...'))
        # else:
        #     print('%sAttachment: %s' % ('  ' * indent, content_type))

def get_send_mail(msg):
    value = msg.get('From', '')
    hdr, addr = parseaddr(value)
    return addr

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
