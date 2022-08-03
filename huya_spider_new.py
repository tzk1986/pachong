# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:huya_spider_new.py
@Time:2022/5/20 18:15
说明：使用BeautifulSoup进行html页面解析
"""
import os
import re
import requests
from bs4 import BeautifulSoup

if not os.path.exists('./newgirl'):
    os.mkdir('./newgirl')

url = 'https://www.huya.com/g/1663'
# 准备请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 '
}

res = requests.get(url=url, headers=header)
data = res.content.decode('utf-8')
# print(data)

# print(res)
soup = BeautifulSoup(data, 'lxml')

# 遍历 HTML 文档标签
# for child in soup.recursiveChildGenerator():
#     if child.name:
#         print(child.name)

# soup.prettify()美化代码显示
# print(soup.prettify())

# 找li的方式1：通过attrs指定属性
# foundLiList = soup.find_all('li', attrs={"class": "clearfix"})
# pic_list = soup.find_all('img', attrs={"class": "pic"})
# 找li的方式2：class 在Python中是保留字 -> BeautifulSoup >4.1.1后，用class_指定CSS的类名
pic_list = soup.find_all('img', class_='pic')
# print(pic_list)

for girl in pic_list:
    img_url = girl['data-original']
    img_url = img_url.split('?')[0]
    name = girl['alt']

    if re.search('https:', img_url) is None:
        img_url = 'https:' + img_url
    # print(img_url)
    # print(name)

    image = requests.get(img_url, headers=header)
    # 使用文件处理 进行下载
    with open('./newgirl/%s.jpg' % name, 'wb') as jpg:
        # 二进制写入图片内容
        jpg.write(image.content)
        print('{%s}下载完毕！' % name)

