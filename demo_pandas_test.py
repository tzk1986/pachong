# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:demo_pandas_test.py
@Time:2022/5/23 17:49
说明：使用pandas写入excel数据
"""
import pandas as pd

# df = pd.DataFrame([[1, "1001", "test1"],
#                    [2, "1002", "测试2"],
#                    [3, "1003", "测试3"]],
#                   columns=[u'序号', u'编码', u'名称'])
new = pd.DataFrame({'name': 'lisa', 'gender': 'F', 'city': '北京'}, index=[1])
df = new
df = pd.concat([df, new])
print(df)
# df.to_excel('sample02.xlsx', '列表1', index=False)
