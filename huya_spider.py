# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:huya_spider.py
@Time:2022/5/20 16:17
说明：爬取虎牙星秀主播图片
"""
import os

import re

import requests
from lxml import etree

if not os.path.exists('./girl'):
    os.mkdir('./girl')

url = 'https://www.huya.com/g/1663'

# 准备请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 '
}

res = requests.get(url=url, headers=header).text
# print(res)

data = etree.HTML(res)
# print(data)
# result = etree.tostring(data).decode('utf-8')
# print(result)
girlItemList = data.xpath('//img[@class="pic"]')

print(girlItemList)

for girl in girlItemList:
    img_url = girl.xpath('./@data-original')[0]
    # print(img_url)
    # 图片二次处理
    img_url = img_url.split('?')[0]
    # 主播名字
    name = girl.xpath('./@alt')[0]
    # 访问资源服务器 对数据进行处理
    # 添加判断，链接是否有https前缀，没有的话加上
    if re.search('https:', img_url) is None:
        img_url = 'https:' + img_url
    print(img_url)

    image = requests.get(img_url, headers=header)
    # 使用文件处理 进行下载
    with open('./girl/%s.jpg' % name, 'wb') as jpg:
        # 二进制写入图片内容
        jpg.write(image.content)
        print('{%s}下载完毕！' % name)
