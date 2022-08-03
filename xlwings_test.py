# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:xlwings_test.py
@Time:2022/5/23 15:18
说明：使用xlwings写入Excel，mac下使用一直报错，并且创建文件不成功，只能终端去执行
"""
# xlwings：需要安装有 Excel 软件，支持 .xls和 .xlsx 格式；可以调用 Excel 文件中 VBA 写好的程序；
# 和 matplotlib 以及 pandas 的兼容性强
# openpyxl：不需要 Excel 软件，仅支持 .xlsx 格式
import xlwings as xw

app = xw.App(visible=True, add_book=False)  # 程序可见，只打开不新建工作薄
app.display_alerts = False  # 警告关闭
app.screen_updating = False  # 屏幕更新关闭

wb = app.books.add()

# 类似 openpyxl 中的 sheet = workbook.active
sheet = wb.sheets.active
# 纵向写入A1:A3
sheet.range('A1').options(transpose=True).value = [1, 2, 3]

sheet.range('A1').options(expand='table').value = [[1, 2, 3], [4, 5, 6]]

wb.save('./sample01.xlsx')  # 保存文件
wb.close()  # 关闭文件
app.quit()  # 关闭程序
