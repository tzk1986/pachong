# -*- coding:utf-8 -*-
"""
@Author:tang
@File:test.py
@Time:2022/5/31 18:33
说明：
"""
url ="http://kr.shanghai-jiuxin.com/file/2022/0414/9e5827678bd12db0999a573254e40d1e.jpg"
text = url.rsplit("/")[0]
print(text)
print(url.rsplit("/"))
print(url.split("/"))