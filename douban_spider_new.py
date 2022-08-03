# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:douban_spider_new.py
@Time:2022/5/21 07:55
说明：使用工具方式使用soup
"""
import csv

from tqdm import tqdm

from utils.soup import *
from openpyxl import Workbook

# url = 'https://movie.douban.com/top250?start=0&filter='
#
# # 请求头 -- http协议 request 请求的一部分 反爬机制
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/101.0.4951.64 Safari/537.36 '
# }
# res = requests.get(url=url, headers=headers)
# data = res.content.decode('utf-8')
# # print(data)
#
# # print(res)
# soup = BeautifulSoup(data, 'lxml')
# print(soup)


# url = 'https://movie.douban.com/top250?start=0&filter='
#
# # 请求头 -- http协议 request 请求的一部分 反爬机制
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/101.0.4951.64 Safari/537.36 '
# }
#
# # html = Soup().get_html(url=url, headers=headers)
# # 数据准备，从页面获取
# soup = Soup().get_soup(url=url, headers=headers)
# # print(soup.prettify())
#
# # 准备可重复提取数据的来源容器
# data_list = soup.find_all('div', attrs={"class": "info"})
# # select查询会查询数据中的所有值与find_all类似，不过是css选择器，标签名用.name，id用#name，选择器与find相似
# # data_list = soup.select('.info')
# # data_list = soup.find_all('span', attrs={"class": "title"})
# # data_list = soup.find('div', attrs={"class": "info"})
# print(data_list)


# data_list = soup.find_all('div', attrs={"class": "info"})
# for item in data_list:
#     # 根据节点条件查询需要信息，直接返回第一个取到的值
#     # title = item.find('span', attrs={"class": "title"}).text
#     # 直接使用节点标签名查询信息，直接返回第一个去到的值
#     title = item.span.text
#     # title = item.select('span')[0].text
#     # 相同标签名称，使用select查询选择元素
#     title2 = item.select('span')[1].text
#     other = item.find('span', attrs={"class": "other"}).text
#     # 链接
#     link = item.a['href']
#     # 评分
#     star = item.find('span', attrs={"class": "rating_num"}).text
#     # 简介
#     quote = item.find('span', attrs={"class": "inq"}).text
#
#     print(title, title2, other, star, quote, link)
# 准备一个容器装每个电影数据
movieList = []

count = 0
while count <= 225:
    url = 'https://movie.douban.com/top250?start={}&filter='.format(count)

    # 请求头 -- http协议 request 请求的一部分 反爬机制
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.64 Safari/537.36 '
    }

    # html = Soup().get_html(url=url, headers=headers)
    # 数据准备，从页面获取
    soup = Soup().get_soup(url=url, headers=headers)
    # print(soup.prettify())

    # 准备可重复提取数据的来源容器
    data_list = soup.find_all('div', attrs={"class": "info"})
    for item in tqdm(data_list):
        # 根据节点条件查询需要信息，直接返回第一个取到的值
        # title = item.find('span', attrs={"class": "title"}).text
        # 直接使用节点标签名查询信息，直接返回第一个去到的值

        title = item.span.text
        # title = item.select('span')[0].text
        # 相同标签名称，使用select查询选择元素
        title2 = item.select('span')[1].text
        other = item.find('span', attrs={"class": "other"}).text
        # 链接
        link = item.a['href']
        # 评分
        star = item.find('span', attrs={"class": "rating_num"}).text
        # 简介
        # 判断现有元素是否存在，如果不存在则给默认值，存在则执行
        if item.find('span', attrs={"class": "inq"}) is None:
            quote = ''
        else:
            quote = item.find('span', attrs={"class": "inq"}).text

        # print(title, title2, other, star, quote, link)
        # 准备一个字典 保存每部的信息
        # movieDict = {}
        #
        # movieDict['title'] = ''.join(title + title2 + other)
        # movieDict['star'] = star
        # movieDict['quote'] = quote
        # movieDict['link'] = link
        movieDict = {'title': ''.join(title + title2 + other), 'star': star, 'quote': quote, 'link': link}

        # 把每部电影填充进容器 movieList
        movieList.append(movieDict)
    count = count + 25

# print(movieList)

# 通过文件I/O保存数据
# with open('doubanMovie01.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=['title', 'star', 'quote', 'link'])
#     # 写数据头
#     writer.writeheader()
#     for each in movieList:
#         # 写每一行
#         writer.writerow(each)

# 使用openpyxl方式把数据写入excel
# for data in movieList:
#     print(list(data.values()))
#     print(data.values())
# wb = Workbook()
#
# sheet = wb.active
# title = ["title", "star", "quote", "link"]
# sheet.append(title)
# for data in movieList:
#     sheet.append(list(data.values()))
#
# wb.save('openpyxl_sample.xlsx')
# wb.close()

# 使用xlwings方式把数据写入excel
# 准备数据容器，格式[[],[],...]
# moviedatalist = []
# for data in movieList:
#     datalist = list(data.values())
#     moviedatalist.append(datalist)
# # print(moviedatalist)
# import xlwings as xw
#
# app = xw.App(visible=False, add_book=False)  # 程序可见，只打开不新建工作薄
# app.display_alerts = False  # 警告关闭
# app.screen_updating = False  # 屏幕更新关闭
#
# wb = app.books.add()
#
# # 类似 openpyxl 中的 sheet = workbook.active
# sht = wb.sheets.active
# sht.range('A1').options(expand='table').value = ['title', 'star', 'quote', 'link']
#
# sht.range('A2').options(expand='table').value = moviedatalist
#
# wb.save('./xlwings_sample.xlsx')  # 保存文件
# wb.close()  # 关闭文件
# app.quit()  # 关闭程序


# 使用pandas写入execl
# 第一种方式，一次性准备全部数据
# 准备数据容器，格式[[],[],...]
import pandas as pd

# moviedatalist = []
# for data in movieList:
#     datalist = list(data.values())
#     moviedatalist.append(datalist)
# # print(moviedatalist)
# df = pd.DataFrame(moviedatalist,
#                   columns=[u'title', u'star', u'quote', u'link'])
# print(df)

# 第二种方式，使用循环，逐次加入数据
# 定义数据框，为后续concat数据做准备
# df = pd.DataFrame(
#     columns=[u'title', u'star', u'quote', u'link']
# )
# 可以直接为空创建
df = pd.DataFrame()
for data in tqdm(movieList):
    # print(data)
    new = pd.DataFrame(data, index=[1])
    df = pd.concat([df, new])

print(df)
# df.to_excel('pandas_sample01.xlsx', '列表1', index=False)
