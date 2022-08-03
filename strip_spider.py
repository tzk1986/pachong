# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:strip_spider.py
@Time:2022/5/21 14:18
说明：
"""
import csv
from lxml import etree
from utils.soup import *

url = 'https://vacations.ctrip.com/list/grouptravel/sc2.html?from=do&st={}&sv={}' \
      '&startcity=2 '

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 ',
    'Referer': 'https://vacations.ctrip.com/',
}

# search_city = input('请输入你想要搜索的城市：')
# url = 'https://kuwo.cn/api/www/search/searchKey?key={}&httpsStatus=1&reqId=6148d920-d737-11ec-ad33-6577d86144a9'.format(
#     search_city, search_city)

url = 'https://vacations.ctrip.com/list/grouptravel/sc2.html?from=do&st=%E5%8C%97%E4%BA%AC&sv=%E5%8C%97%E4%BA%AC' \
      '&startcity=2 '
# response = requests.get(url, headers=headers)
# print(response)

# soup = Soup().get_soup(url=url, headers=headers)
# print(soup.prettify())
# data_list = soup.find_all('div', attrs={"class": "list_product_item_border"})
# print(data_list)

res = requests.get(url=url, headers=headers).text
# print(res)

# 数据转成html格式
data = etree.HTML(res)
print(res)