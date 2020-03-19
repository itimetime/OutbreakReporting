#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Colin
@file: 新型肺炎感染人数获取.py
@time: 2020/01/{DAY}
"""
from bs4 import BeautifulSoup
import requests
import time
import logging
urls = ['https://news.163.com/special/epidemic/?spssid=8e975c7badf7f88d954ef3941767221f&spsw=6&spss=other&from=singlemessage&isappinstalled=0',
       ]


class Get_html_data():

    # h2 = soup.find('h2').text
    # h1 = soup.find('h1').text
    # title = soup.find(class_='tit').text
    # general_condication = soup.find_all('p')
    # province_condicetion = soup.find_all('li')



    def data_general(self):
        response = requests.get(urls[0], )
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find(class_='tit').text
        general_condication = soup.find_all('p')
        # print(self.h2 + '-----' + self.h1)
        # print("="*50)
        # print(self.title)
        # print("="*50)
        content = '<div style="font-family:Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; font-size:15px; text-align:left;  margin-bottom:5px; color:#323232; line-height:25px;">'
        # print('本次请求时间' + time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time())))
        # print('=' * 60)
        # print("疫情总况（以下数据均来自官方通报）")
        for x in general_condication:
            if '单击' in x.text:
                break
            else:
                content += '<li>' +x.text +'</li>'
                logging.debug(x.text)
        content += '</div>'
        return title, content

    def data_province(self):
        print("=" * 60)
        print('各省市情况通报')
        for item in self.province_condicetion:
            if "山东" in item.text:
                print("其中你所在的省市：" + item.text + "请注意防护")
        for item in self.province_condicetion:
            if 'overseas' not in str(item):
                print(item.text)

    def data_foreign(self):
        print("=" * 60)
        print('海外情况通报')
        for item in self.province_condicetion:
            if 'overseas' in str(item):
                print(item.text)


