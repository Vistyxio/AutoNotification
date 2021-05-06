# -*- coding: utf-8 -*-

#使用sys.exit()必要
import sys
#使用time.sleep()必要
import time
#使用json必要
import json
#使用urllib.request.urlopen()必要
import urllib
#使用requests.post()必要
import requests
#使用正则表达式必要
import re
#使用BeautifulSoup()必要
from bs4 import BeautifulSoup

#发送通知的函数
def SendNotification(data):
    #在IFTTT中获取的链接
    url = "https://maker.ifttt.com/trigger/someting_new/with/key/*********************"
    
    #发送json格式数据
    headers = {
        'Content-Type': "application/json"
    }
    #使用requests.post发送
    response = requests.post(url, headers=headers, data = json.dumps(data))
    response.encoding = 'utf-8'
    #返回发送结果
    return(response.text)
    
    

#要监控的网站链接
url = 'http://www16.zzu.edu.cn/msgs/vmsgisapi.dll/vmsglist?mtype=m&lan=101,102,103&ds6=3252989F38A865C9E4793824547EA08E'
#使用urllib
page = urllib.request.urlopen(url)
#使用BeautifulSoup
soup = BeautifulSoup(page, from_encoding="utf8", features="html.parser")
#根据网页源码查询新闻列表
list = soup.find_all("div", "zzj_5a")

#存放上一次查询的最新的新闻信息
old_list = []
#打开存放的文本读取并存入old_list
with open(r"/home/pi/Code/runtime_folder/AutoNotification") as file_obj:
    for content in file_obj:
        old_list.append(content.rstrip())

#清空并重新打开存放的文本
FILE = open(r"/home/pi/Code/runtime_folder/AutoNotification",'w+')

#根据源码确定标题的正则 链接的正则 子标题的正则
title_pattern = re.compile(r'(?<=("zzj_f6_c">)).*?(?=(</span></a>))')
url_pattern = re.compile(r'(?<=(<a href=")).*?(?=(\s"\starget))')
sub_title_pattern = re.compile(r'(?<=(<span\sclass="zzj_f7">)).*?(?=(</span></div>))')

#只执行一次的标识
once = 0

#循环遍历新闻列表
for value in list:
    
    #以下进行正则匹配并截取出相应内容
    title = re.search(title_pattern, str(value))
    title = title.string[title.start():title.end()]

    url = re.search(url_pattern, str(value))
    url = url.string[url.start():url.end()]

    sub_title = re.search(sub_title_pattern, str(value))
    sub_title = sub_title.string[sub_title.start():sub_title.end()]
    
    #判断是否为上次已经查询过的新闻
    if old_list[0] == title:
        #如果第一次进入循环
        if once == 0:
            #则证明没有新的新闻 将上次已查询过的新闻重新写入文件
            for i in old_list:
                print(i, file = FILE)
            print("None")
        #退出循环
        break
    
    #如果是新的新闻 且第一次进入循环
    if once == 0:
        #因为从上到下按顺序查找 所以第一个新闻即为最新的新闻
        #将其写入到文件
        print(title, file = FILE)
        print(url, file = FILE)
        print(sub_title, file = FILE)
        #once置1 下次不会进入
        once = 1

    #发送的json格式
    data = {
        #title 标题 通知显示的标题
        "value1": title,
        #message 信息 标题下方的小字
        "value2": sub_title,
        #link_url 链接 点击通知跳转的链接
        "value3": url
    }
    
    #发送通知
    SendNotification(data)
    #输出发送的新闻的标题
    print(title)
    #延迟一秒 防止IFTTT无法快速响应
    time.sleep(1)

    
#关闭文件读写
FILE.close()
#输出回车 方便log查看
print()
#结束程序
sys.exit()
