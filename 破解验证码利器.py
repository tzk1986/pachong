# -*- coding:utf-8 -*-
"""
@Author:tang
@File:破解验证码利器.py
@Time:2022/6/2 18:32
说明：登录12306
"""
import time

"""
图像识别
选择互联网上成熟的验证码破解工具
超级鹰   
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get('https://kyfw.12306.cn/otn/resources/login.html')

time.sleep(2)
web.find_element(By.XPATH, value='//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()
time.sleep(2)
web.find_element(By.XPATH, value='//*[@id="J-userName"]').send_keys('tzk1986')
web.find_element(By.XPATH, value='//*[@id="J-password"]').send_keys('TZK1986')
web.find_element(By.XPATH, value='//*[@id="J-login"]').click()
