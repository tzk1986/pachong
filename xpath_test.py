# -*- coding:utf-8 -*-
"""
@Author:tang
@File:xpath_test.py
@Time:2022/5/28 12:40
说明：使用xpath爬取猪八戒网站信息
"""
import re

from bs4 import BeautifulSoup
import requests
from lxml import etree

url = "https://shanghai.zbj.com/search/f/?kw=saas"

response = requests.get(url=url)
html = etree.HTML(response.text)
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")

# html = response.content.decode('utf-8')  # 根据页面编码，传入相应的值
#
# soup = BeautifulSoup(html, 'lxml')  # 使用lxml的方法来分析页面，也可以使用其他方式
# print(soup.prettify())
# divs = soup.find_all("div", class_="witkey-item grid-box")

# print(divs)
# for div in divs:
#     title = div.find("p", class_="title").text
#     price = div.find("span", class_="price").text
#     print(title)
#     print(price)
for div in divs:

    title = "saas".join(div.xpath("./div/div/a[@class='service-top-wrap j_ocpc']/div[2]/div[2]/p/text()"))
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")  # 去除符号
    cpname = div.xpath("./div/div/a[1]/div[1]/p/text()")
    city = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    print(title)
    print(price)
    print(cpname)
    print(city)

