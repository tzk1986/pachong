# -*- coding:utf-8 -*-
"""
@Author:tang
@File:selenium入门.py
@Time:2022/6/2 12:43
说明：
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, Keys

web = Chrome()
web.get('https://www.lagou.com/')
web.find_element(By.XPATH, value='//*[@id="changeCityBox"]/p[1]/a').click()
time.sleep(1)
web.find_element(By.XPATH, value='//*[@id="search_input"]').send_keys('python', Keys.ENTER)

# li_list = web.find_elements(By.XPATH, value='//*[@id="jobList"]/div[1]/div')
# print(li_list)
# for li in li_list:
#     name = li.find_element(By.XPATH, value='./div/div/div/a').text
#     print(name)
time.sleep(1)
# 窗口之间的切换
web.find_element(By.XPATH, value='//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

web.switch_to.window(web.window_handles[-1])  # 切换到新的窗口
time.sleep(1)
s = web.find_element(By.XPATH, value='//*[@id="job_detail"]/dd[2]/div').text
print(s)
web.close()
web.switch_to.window(web.window_handles[0])  # 切换到原窗口

# 处理iframe的话，必须先拿到iframe的id，然后再切换到iframe
# web.switch_to.frame('iframe_158888')  # 切换到iframe
# web.switch_to.default_content() # 切换到默认的窗口

