# -*- coding:utf-8 -*-
"""
@Author:tang
@File:demo_bs4_new.py
@Time:2022/5/27 19:31
说明：使用的是lxml
"""
import time

from bs4 import BeautifulSoup
import requests

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"

response = requests.get(url=url)
html = response.content.decode('utf-8')  # 根据页面编码，传入相应的值
# print(html)
soup = BeautifulSoup(html, 'lxml')  # 使用lxml的方法来分析页面，也可以使用其他方式
# print(soup.prettify())
alist = soup.find("ul", class_="pic-list after").find_all("a")
# print(alist)
for a in alist:
    # print(a)
    href = f"https://www.umeitu.com/" + a['href']
    # print(href)
    child_page_resp = requests.get(href)
    child = child_page_resp.content.decode('utf-8')
    child_page = BeautifulSoup(child, 'lxml')
    section = child_page.find("section", attrs={"class": "img-content"})
    resp = section.contents[0]
    time.sleep(1)
    print(resp)
#     img = section.img['src']
#     print(img)
#     img_resp = requests.get(img)
#     img_resp.content
#     img_name = img.split("/")[-1]  # 拿到url中最后一个/以后的内容
#     with open("img/" + img_name, mode="wb") as f:
#         f.write(img_resp.content)
#
#     print("over!", img_name)
#     time.sleep(1)
# print("all over!!")
