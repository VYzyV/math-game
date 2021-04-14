# -*- coding：utf-8 -*-
# @Time : 2020/10/27 16:31
# @Author: Wong
# @file: imggetter.py
# @Software: PyCharm
import os
import re
from bs4 import BeautifulSoup
import requests
url="https://www.qiushibaike.com/imgrank/"
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
html=requests.get(url,headers=head).text
bs=BeautifulSoup(html,"html.parser")
findallimg=re.compile(r'<img.*? src="(.*?)" ')
list=bs.find_all('div',class_='thumb')
list=str(list)
imglist=re.findall(findallimg,list)
if not os.path.exists("../imglibs"):
    os.mkdir("../imglibs")
for src in  imglist:
    src="https:"+src
    res=requests.get(src,headers=head).content
    imgname=src.split('/')[-1]
    with open("./imglibs/"+imgname,'wb') as im:
        im.write(res)
        print(imgname+"下载成功")



