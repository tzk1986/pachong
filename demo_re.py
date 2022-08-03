# -*- coding:utf-8 -*-
"""
@Author:tang
@File:demo_re.py
@Time:2022/5/27 17:26
说明：正则表达式demo
"""
import re

# findall：匹配字符串中所有的符合正则的内容
lst = re.findall(r"\d+", "我的电话号码是：10086，我女朋友的电话是：10010")
print(lst)
# finditer：匹配字符串中所有的内容 返回的是迭代器, 从迭代器中拿到的内容需要.group()
it = re.finditer(r"\d+", "我的电话号码是：10086，我女朋友的电话是：10010")
for i in it:
    print(i.group())
# search找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
s = re.search(r"\d+", "我的电话号码是：10086，我女朋友的电话是：10010")
print(s.group())
# match 从头开始匹配
s = re.match(r"\d+", "10086，我女朋友的电话是：10010")
print(s.group())

# 预加载正则表达式
obj = re.compile(r"\d+")
res = obj.finditer("我的电话号码是：10086，我女朋友的电话是：10010")
for i in res:
    print(i.group())

s = """
<div class='jay'><span id='1'>高蕾</span></div>
<div class='jj'><span id='2'>松江</span></div>
<div class='jolin'><span id='3'>唐仲凯</span></div>
"""
# (?P<分组名称>正则) 用这种方式，把正则匹配的数据赋值到分组名称中
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)  # re.S:让.能匹配换行符
res = obj.finditer(s)
for it in res:
    print(it.group("name"))
    print(it.group("id"))



p = "18888888888"

"""
    基于正则表达式的字符串
        1、正则表达式对于\d这类正则表达,前面是否加r都不影响结果【正则内部已做了兼容】
        2、但是如果对于\d这类特殊字符,如果不加r,会有一条灰色的警告线【PEP 8：W605 无效的转义序列 '\d'】
        3、基于正则表达式【\d、\s】这些都是一个特殊的字符,这里的\不是一个转义字符【而是代表一个特殊的元素】为此这里建议前面加r
"""
print(re.fullmatch(r"\d{4}-" + f"{p}", "08101-18888888888"))

"""
    基于普通的字符串
        1、\n前面加了r代表【\】不是一个有效转义字符
        2、\n前面如果不加r【\】代表是有效转义字符
"""
print(r"\n23342")  # 这里\n代表是一个字符串
print("\n2343423")  # 这里\n代表是一个转义字符
