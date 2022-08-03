# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:soup.py
@Time:2022/5/21 07:57
说明：
"""
import requests
from bs4 import BeautifulSoup


class Soup:
    # def __init__(self, url, headers):
    #     self.headers = headers
    #     self.url = url

    def get_html(self, url, headers):
        response = requests.get(url=url, headers=headers)
        html = response.content.decode('utf-8')
        return html

    def get_soup(self, url, headers):
        html = self.get_html(url=url, headers=headers)
        soup = BeautifulSoup(html, 'lxml')
        return soup

    # 显示页面标签attrs
    def get_attrs(self):
        pass


