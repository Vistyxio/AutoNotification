# -*- coding: utf-8 -*-

import sys
import time
import json
import urllib
import requests
import re
from bs4 import BeautifulSoup

def SendNotification(data):
    url = "https://maker.ifttt.com/trigger/someting_new/with/key/*********************"
    
    headers = {
        'Content-Type': "application/json"
    }
    response = requests.post(url, headers=headers, data = json.dumps(data))
    response.encoding = 'utf-8'
    return(response.text)
    
    

url = 'http://www16.zzu.edu.cn/msgs/vmsgisapi.dll/vmsglist?mtype=m&lan=101,102,103&ds6=3252989F38A865C9E4793824547EA08E'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, from_encoding="utf8", features="html.parser")
list = soup.find_all("div", "zzj_5a")

old_list = []
with open(r"/home/pi/Code/runtime_folder/AutoNotification") as file_obj:
    for content in file_obj:
        old_list.append(content.rstrip())

FILE = open(r"/home/pi/Code/runtime_folder/AutoNotification",'w+')

title_pattern = re.compile(r'(?<=("zzj_f6_c">)).*?(?=(</span></a>))')
url_pattern = re.compile(r'(?<=(<a href=")).*?(?=(\s"\starget))')
sub_title_pattern = re.compile(r'(?<=(<span\sclass="zzj_f7">)).*?(?=(</span></div>))')

once = 0

for value in list:
    
    title = re.search(title_pattern, str(value))
    title = title.string[title.start():title.end()]

    url = re.search(url_pattern, str(value))
    url = url.string[url.start():url.end()]

    sub_title = re.search(sub_title_pattern, str(value))
    sub_title = sub_title.string[sub_title.start():sub_title.end()]
    
    if old_list[0] == title:
        if once == 0:
            for i in old_list:
                print(i, file = FILE)
            print("None")
        break
    
    if once == 0:
        print(title, file = FILE)
        print(url, file = FILE)
        print(sub_title, file = FILE)
        once = 1

    data = {
        "value1": title,
        "value2": sub_title,
        "value3": url
    }
    
    SendNotification(data)
    print(title)
    time.sleep(1)

    
FILE.close()
print()
sys.exit()
