# -*- coding:utf-8 -*-
"""
@Author:tang
@File:demo_bs4.py
@Time:2022/5/27 19:04
说明：BeautifulSoup的demo，使用的是html.parser
"""
import time

from bs4 import BeautifulSoup

"""
<标签 属性="属性值">被标记内容</标签>

"""
import requests

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("ul", class_="pic-list after").find_all("a")
# print(alist)
for a in alist:
    # print(a)
    href = f"https://www.umeitu.com/" + a.get('href')  # 直接通过get就可以拿到属性的值
    # print(href)
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    section = child_page.find("section", class_="img-content")
    img = section.find("img")
    src = img.get("src")
    # print(src)
    # 下载图片
    img_resp = requests.get(src)
    img_resp.content
    img_name = src.split("/")[-1]  # 拿到url中最后一个/以后的内容
    with open("img/" + img_name, mode="wb") as f:
        f.write(img_resp.content)

    print("over!", img_name)
    time.sleep(1)
print("all over!!")
