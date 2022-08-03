# -*- coding:utf-8 -*-
"""
@Author:tang
@File:wangyi163_spider.py
@Time:2022/5/30 15:06
说明：网易云音乐评论爬取
"""
# 找到未加密的参数
# 想办法把参数进行加密（参考网易的逻辑），params，encSecKey
# 请求到网易，拿到评论信息

url="https://music.163.com/#/song?id=1951513623"

# 请求方式post
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1951513623",
    "threadId": "R_SO_4_1951513623"
}
import requests

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"

response = requests.get(url=url)
response.content