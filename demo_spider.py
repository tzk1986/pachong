# -*- coding:utf-8 -*-
"""
@Author:tang
@File:demo_spider.py
@Time:2022/5/27 16:47
说明：
"""
import requests
from bs4 import BeautifulSoup

url = ""
headers = {

}
response = requests.get(url=url, headers=headers, verify=False)  # 安全性验证跳过verify=False
html = response.content.decode('utf-8')  # 根据页面编码，传入相应的值
soup = BeautifulSoup(html, 'lxml')  # 使用lxml的方法来分析页面，也可以使用其他方式
