# -*- coding:utf-8 -*-
"""
@Author:tang
@File:无头浏览器.py
@Time:2022/6/2 17:30
说明：让浏览器后台运行
"""
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


# 准备好配置参数
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')


web = webdriver.Chrome(options=opt)  # 把参数设置到浏览器中
web.get("http://www.baidu.com")

sel = Select(web.find_element_by_id("nr"))
for i in range(len(sel.options)):  # i就是每一个下拉框选项的索引位置
    sel.select_by_index(i)  # 按照索引进行切换
    time.sleep(1)
    print(web.page_source)