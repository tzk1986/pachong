# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:douban_spider.py
@Time:2022/5/19 16:57
说明：
"""
import requests  # 发起网络请求工具
from lxml import etree  # 数据转换类库
import csv  # 文字类库

# 数据在哪里？
url = 'https://movie.douban.com/top250?start=0&filter='

# 请求头 -- http协议 request 请求的一部分 反爬机制
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 '
}

#  访问网站，拿取数据
res = requests.get(url=url, headers=headers).text
# print(res)

# 数据转成html格式
data = etree.HTML(res)

# 拿到装所有数据的大盒子
movieItemList = data.xpath('//div[@class="info"]')

# 准备一个容器装每个电影数据
movieList = []
for movieItem in movieItemList:
    # 准备一个字典 保存每部的信息
    movieDict = {}

    # 标题
    title = movieItem.xpath('div[@class="hd"]/a/span[@class="title"]/text()')
    # 别名
    otherTitle = movieItem.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
    # 链接
    link = movieItem.xpath('div[@class="hd"]/a/@href')[0]
    # 评分
    star = movieItem.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
    # 简介
    quote = movieItem.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')

    # 填充字典
    movieDict['title'] = ''.join(title + otherTitle)
    movieDict['link'] = link
    movieDict['star'] = star
    movieDict['quote'] = quote

    # print(movieDict)
    # 把每部电影填充进容器 movieList
    movieList.append(movieDict)
# print(type(movieDict))
# 通过文件I/O保存数据
with open('doubanMovie.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'star', 'quote', 'link'])
    # 写数据头
    writer.writeheader()
    for each in movieList:
        # 写每一行
        writer.writerow(each)
