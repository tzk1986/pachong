# -*- coding:utf-8 -*-
"""
@Author:tang
@File:第8章验证码的识别.py
@Time:2022/7/13 17:42
说明：
"""
"""
tesserocr库，使用该库进行简单验证码的识别
"""
# import tesserocr
# from PIL import Image
#
# image = Image.open('captcha.png')
# result = tesserocr.image_to_text(image)
# print(result)

"""
简便版本
"""
# import tesserocr
#
# print(tesserocr.file_to_text('captcha.png'))

"""
解决噪点对验证码的识别
"""
# import tesserocr
# from PIL import Image
# import numpy as np
#
# image = Image.open('captcha2.png')
# image = image.convert('L') # 转化为灰度图片
# threshold = 50  # 灰度的阀值
# array = np.array(image)
# array = np.where(array > threshold, 255, 0)  # 大于255表示白色，否者设置为0，表示黑色
# image = Image.fromarray(array.astype('uint8'))
# print(tesserocr.image_to_text(image))

"""
识别jpg，识别时有误差，需要根据图片进行图片处理
"""
# import tesserocr
# from PIL import Image
#
# image = Image.open('code2.jpg')
# result = tesserocr.image_to_text(image)
# print(result)
"""
简化，识别时有误差
"""
# import tesserocr
#
# print(tesserocr.file_to_text('code.jpg'))
"""
当图片是条状水印且是彩色验证码时，通过图片灰度，阀值设置进行判断，读取正确信息
"""
# import tesserocr
# from PIL import Image
#
# image = Image.open('code2.jpg')
#
# image = image.convert('L')
# threshold = 127
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# image = image.point(table, '1')
# image.show()
#
# result = tesserocr.image_to_text(image)
# print(result)
"""
通过selenium完成验证码登录，会进行验证码的重复识别，当识别正确登录成功后，关闭浏览器
"""
# import time
# import re
# import tesserocr
# from selenium import webdriver
# from io import BytesIO
# from PIL import Image
# from retrying import retry
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# import numpy as np
#
#
# def preprocess(image):
#     image = image.convert('L')
#     array = np.array(image)
#     array = np.where(array > 50, 255, 0)
#     image = Image.fromarray(array.astype('uint8'))
#     return image
#
#
# @retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
# def login():
#     browser.get('https://captcha7.scrape.center/')
#     browser.find_element_by_css_selector('.username input[type="text"]').send_keys('admin')
#     browser.find_element_by_css_selector('.password input[type="password"]').send_keys('admin')
#     captcha = browser.find_element_by_css_selector('#captcha')
#     image = Image.open(BytesIO(captcha.screenshot_as_png))
#     image = preprocess(image)
#     captcha = tesserocr.image_to_text(image)
#     captcha = re.sub('[^A-Za-z0-9]', '', captcha)
#     browser.find_element_by_css_selector('.captcha input[type="text"]').send_keys(captcha)
#     browser.find_element_by_css_selector('.login').click()
#     try:
#         WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(., "登录成功")]')))
#         time.sleep(10)
#         browser.close()
#         return True
#     except TimeoutException:
#         return False
#
#
# if __name__ == '__main__':
#     browser = webdriver.Chrome()
#     login()

"""
滑动验证码识别
"""
