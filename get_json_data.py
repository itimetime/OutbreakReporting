#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Colin
@file: 新型肺炎感染人数状况.py
@time: 2020/01/{DAY}
"""

import requests
import json


def get_Condition():
    json_data = get_Date()
    #所在省市提醒
    conent = ''
    content = '<li style="color:#323232;">其中您所在的' + search_Province('山东', json_data,1) +  ',菏泽确诊'+str(search_City('菏泽',json_data,1))+'例,请注意防护</li>'
    # 打印各省市的状况
    dic = {'香港': '', '澳门': '', '台湾': ''}

    for btc_dict in json.loads(json_data):
        province = btc_dict['provinceShortName']
        confirmed_count = btc_dict['confirmedCount']
        suspected_count = btc_dict['suspectedCount']
        cured_count = btc_dict['curedCount']
        dead_count = btc_dict['deadCount']
        # cities = btc_dict['cities']
        if confirmed_count != 0:
            if province not in dic.keys():
                content += '<li style="color:#323232;">' + province + ' 确诊%d例' % confirmed_count
                print(province + ' 确诊%d例' % confirmed_count, end='')
                if dead_count != 0:
                    content += "，死亡%d例" % dead_count
                    print("，死亡%d例" % dead_count, end='')
                if cured_count != 0:
                    content += "，治愈%d例" % cured_count
                    print("，治愈%d例" % cured_count, end='')
                content += '</li>'
                print()
            else:
                dic[province] = province + ' 确诊%d例 ' % confirmed_count
    for j in dic.items():
        content += '<li style="color:#323232;">' + j[1] + '</li>'
        print(j[1])
    return content

def search_Province(keyword,json_data,model=0,):
    search_keyword = keyword
    content = ''
    for btc_dict in json.loads(json_data):

        if btc_dict['provinceShortName'] == search_keyword:
            if model == 1:
                content += search_keyword + '共确诊%d例' %btc_dict['confirmedCount']
            if model == 0:
                content += '<li style="color:#323232;">' + search_keyword + '共确诊%d例' % btc_dict[
                    'confirmedCount'] + '</li>'
                for city in btc_dict['cities']:
                    confirmed_count = city['confirmedCount']
                    suspected_count = city['suspectedCount']
                    cured_count = city['curedCount']
                    dead_count = city['deadCount']
                    city_name = city['cityName']
                    if confirmed_count != 0:
                        content += '<li style="color:#323232;">' + city_name + ' 确诊%d例' % confirmed_count
                        if dead_count != 0:
                            content += '死亡%d例' % dead_count
                        if cured_count != 0:
                            content +=  "，治愈%d例" % cured_count

                        content += '</li>'
            return content
    print("%s 查询省份未查询到，请检查输入内容"%keyword)
    return ''

def search_City(keyword,json_data,model = 0):
    content = ''
    for btc_dict in json.loads(json_data):
        for city in btc_dict['cities']:
            if keyword == city['cityName']:
                if model == 0:
                    confirmed_count = city['confirmedCount']
                    cured_count = city['curedCount']
                    dead_count = city['deadCount']
                    content += '<li style="color:#323232;">' + keyword + ' 确诊%d例' % confirmed_count
                    if dead_count != 0:
                        content += "，死亡%d例" % dead_count
                    if cured_count != 0:
                        content += "，治愈%d例" % dead_count
                    content += '</li>'
                    return content
                if model == 1:
                    return city['confirmedCount']
    print("%s 查询城市未查询到，请检查输入内容"%keyword)
    return content


def end_Method():
    print("=" * 60)
    choice = input('1.刷新2.查询省市下各城市概况3.查询单个城市 其他退出')

    if choice == '1':
        get_Condition()
    elif choice == '2':
        province_keyword = input("请输入省市：")
        search_Province(province_keyword)
    elif choice == '3':
        city_keyword = input("请输入市或区，例 菏泽 :")
        search_City(city_keyword)
    else:
        exit()
def get_Date():
    # 获取json数据，来自网易
    json_url = 'https://news.163.com/special/00018IRU/data_from_dxy.js'
    req = requests.get(json_url)
    print("请求数据")
    json_array = []
    json_data = req.text
    for i in range(2):
        left = json_data.index('[{')
        right = json_data.index('}catch')
        json_array.append(json_data[left:right])
        json_data = json_data[right + 4:]
    return json_array[1]
def get_province_condition():
    #对当前数据进行查询
    get_Condition()
    #查询后的退出操作
    while True:
        end_Method()





