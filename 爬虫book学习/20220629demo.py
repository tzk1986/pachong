# -*- coding:utf-8 -*-
"""
@Author:tang
@File:20220629demo.py
@Time:2022/6/29 14:58
说明：学习开始，urllib，requests，httpx
"""
import urllib.parse
import urllib.request
import requests

# data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
#
# proxies = { "http": None, "https": None}
#
# response = requests.get('https://www.httpbin.org/get', proxies=proxies)
# print(response.read())

# r = urllib.request.Request('https://python.org')
# res = urllib.request.urlopen(r)
# print(res.read().decode('utf-8'))

# from urllib import request, error
#
# try:
#     res = request.urlopen('https://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# import ssl
# print(ssl.get_default_verify_paths())

# from urllib.parse import  urlparse
# res = urlparse('https://wwww.baidu.com/index.html;user?id=5#comment')
# print(type(res))
# print(res)

# from urllib.parse import quote
# keyword='壁纸'
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)
# from urllib.parse import unquote
# url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))

# from urllib.robotparser import RobotFileParser
# rp = RobotFileParser()
# rp.set_url('https://www.baidu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
# print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
# print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))


# data = {
#     'name': 'germey',
#     'age': 25
# }
# r = requests.get('https://www.httpbin.org/get', params=data)
# print(r.text)
# print(r.json())

# r = requests.get('https://scrape.center/favicon.ico')
# print(r.text)
# print(r.content)

# r = requests.post('https://www.httpbin.org/post', data=data)
# print(r.text)

import httpx

# r = httpx.get('https://www.httpbin.org/get')
# print(r.status_code)
# print(r.headers)
# print(r.text)
client = httpx.Client(http2=True)
r = client.get('https://spa16.scrape.center/')
print(r.text)