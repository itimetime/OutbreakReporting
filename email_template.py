#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Colin
@file: email_template.py
@time: 2020/01/{DAY}
"""

from get_html_data import Get_html_data
import get_json_data
content = """
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <style type="text/css">
        div, tr, td, p, a, h1, h2, h3, h4, h5, h6, ul, li {
            margin: 0;
            padding: 0;
        }

        a {
            text-decoration: none;
        }

        img {
            max-width: 100%;
            border: none;
            outline: none;
            text-decoration: none;
            -ms-interpolation-mode: bicubic;
        }

        a img {
            border: none;
        }
    </style>
</head>

<body>
    <div style="font:Verdana normal 14px;color:#000;">
        <table cellpadding="0" cellspacing="0" border="0" width="100%" style="padding:0px;  background:#F2F2F2;">
            <tbody>
                <tr>
                    <td align="center" style="background-color: #eeeeee;padding-top: 30px;padding-bottom:60px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="600">
                            <tbody>
                                <tr>
                                    <td align="center" style="padding: 20px 0px; background-color:#eeeeee;" valign="middle">
                                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td width="170" style="width:170px" valign="top">
                                                            <span style="display: block;width:170px;color: rgb(50, 50, 50); background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">
                                                   </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center" valign="top">
                                        <table border="0" cellpadding="0" cellspacing="0" style="" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td align="center" valign="top">
                                                        <table border="0" cellpadding="0" cellspacing="0" style="background-color:#3e9de1; padding:25px 45px;" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td valign="top">
                                                                        <table cellpadding="0" cellspacing="0">
                                                                            <tbody>
                                                                            <tr>
                                                                                <td width="160" style="width:160px; padding-right:20px;" align="right">
                                                                                    <img width="153" title="疫情播报（以下数据均来自官方通报）" src="http://13269944.s21i.faiusr.com/4/ABUIABAEGAAgyc2w8QUo5dfI5gQwuAI4ggM.png">
                                                                                </td>
                                                                                <td>
                                                                                    <div style="font-family:Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; font-size:13px; text-align:left; color:#fff;">
                                                                                        <h3 style="font-size: 22px;">肺炎疫情实时动态播报</h3>
                                                                                        <p style="font-size: 18px; ">大爱无疆，武汉加油!</p><div style="text-decoration: none; outline: none; background-color: rgb(253, 216, 22); float: left; border-bottom: 2px solid rgb(246, 174, 18); color: rgb(51, 51, 51); margin-top: 8px; cursor: pointer; width: 200px; height: 20px; line-height: 20px; text-align: center; padding: 5px 9px;">
                                                                                        <a style="color: rgb(51, 51, 51);">{%data_time%}</a></div>
                                                                                    </div>
                                                                                </td>
                                                                            </tr>
                                                                           </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="center" valign="top">
                                                        <table border="0" cellpadding="0" cellspacing="0" style="background-color: #fff;" width="100%">
                                                            <tbody>
                                                            <tr>
                                                                <td valign="top" style="padding: 25px 40px;">
                                                                    <h1 style=" font-family:Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; font-size:20px; font-weight:600; color:#363c43; margin:0px 0px 10px; text-align: left;">疫情总况：</h1>
                                                                    <div style="font-family:Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; font-size:15px; text-align:left;  margin-bottom:5px; color:#323232; line-height:25px;">
                                                                    {%condation_total%}</div>
                                                                </td>
                                                            </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="padding:25px 40px 0px; background-color:#f6f7fb;">
                                                        <div style="font-family:Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; color:#323232; font-size:18px; font-weight:600; padding-bottom:10px;">各省市情况通报:</div>
                                                        <ul style="padding: 5px 0px 10px 35px; margin: 0px; font-family: Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; line-height:25px; font-size: 14px;">
                                                        {%contation_detail%}
                                                        </ul>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="center" valign="top" style="background-color: #fff;">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td valign="top" style="padding: 25px 40px 5px;">
                                                                        <div style="text-align: left; font-family:Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; font-size: 15px; margin-bottom: 5px; color: #323232; line-height: 25px;">
                                                                            如果你有任何问题都可以回复本邮件<br> 我会很乐意在我能力范围之内为您提供帮助
                                                                            <br>同时，您也可以回复省名、城市名、区名（限北京）<br>查询更多信息
                                                                        </div>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="center" valign="top" width="650" style="padding: 15px 40px; background-color: #fff;">
                                                        <div style="text-align: left; font-family: Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; font-size: 15px; margin-bottom: 5px; color: #323232; line-height: 25px;"><br></div><div style="text-align: left; font-family: Lucida Grande,Lucida Sans,Lucida Sans Unicode,Arial,Helvetica,Verdana,sans-serif; font-size: 15px; margin-bottom: 5px; color: #323232; line-height: 25px;"><br></div><div style=" text-align: right ; ; ; ; ; ; ; ; ; ; "><span style="font-size: x-small;"><a rel="unsubscribe">Python Developer</a> | <a rel="webversion">ck</a></span></div>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
"""



def get_new_content():
    data_time, condation_total = Get_html_data().data_general()
    condation_detail = get_json_data.get_Condition()
    content1 = content.replace("{%data_time%}",data_time)
    content2 = content1.replace('{%contation_detail%}',condation_detail)
    content3 = content2.replace('{%condation_total%}',condation_total)
    return content3

def get_request_content(keyword):
    print("正在搜索相关内容")
    json_data = get_json_data.get_Date()
    data_time, condation_total = Get_html_data().data_general()
    search_result = ''
    for i in range(2, len(keyword)+1):
        if i > len(keyword) or i > 5:
            break
        temp_keyword = keyword[:i]
        search_result = get_json_data.search_Province(temp_keyword,json_data)
        print(search_result)
        if search_result != '':
            break
        else:
            search_result = get_json_data.search_City(temp_keyword,json_data)
            if search_result != '':
                break
            else:
                continue

    if search_result != '':
        content1 = content.replace("{%data_time%}", data_time)
        content2 = content1.replace('{%contation_detail%}', search_result)
        content3 = content2.replace('{%condation_total%}', condation_total)
        content4 = content3.replace('各省市情况通报:','查询结果：')
        return content4,temp_keyword
    else:
        content1 = content.replace("{%data_time%}", data_time)
        content2 = content1.replace('{%contation_detail%}', "未查询到，请检查输入内容")
        content3 = content2.replace('{%condation_total%}', condation_total)
        content4 = content3.replace('各省市情况通报:', '查询结果：')
        return content4,temp_keyword



