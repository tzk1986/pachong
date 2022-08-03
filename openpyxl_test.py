# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:openpyxl_test.py
@Time:2022/5/23 14:55
说明：openpyxl测试
"""

import openpyxl
from openpyxl import Workbook

wb = Workbook()

sheet = wb.active
title = ["title", "star", "quote", "link"]
sheet.append(title)
sheet.append([1, 2, 3])

wb.save('sample00.xlsx')
wb.close()
