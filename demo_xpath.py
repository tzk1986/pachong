# -*- coding:utf-8 -*-
"""
@Author:tang
@File:demo_xpath.py
@Time:2022/5/27 20:42
说明：使用lxml，进行xpath定位
"""
from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="123">高</nick>
        <nick id="1234">蕾</nick>
        <nick class="joy">唐</nick>
        <nick class="jay">糕</nick>
        <div>
            <nick>累了</nick>
        </div>
        <span>
            <nick>累了2</nick>
            <div>
                <nick>累了3</nick>
            </div>
        </span>
    </author>
</book>
"""
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    Hello jinja2
    <br>
{{ age }}
<br>
    开头字母大写  {{ name|title }}
<br>
    自定义过滤器 {{ age|test(2) }}
<br>
<li><a href="/bizhitupian/weimeibizhi/245899.htm"><img 
data-src="http://kr.shanghai-jiuxin.com/file/2022/0414/small9e5827678bd12db0999a573254e40d1e.jpg" 
src="/d/style/lazy.gif"/><span>美女侧脸 侧颜 背部 唯美好看2k动漫壁纸</span></a></li> 
<li><a href="/bizhitupian/weimeibizhi/245898.htm"><img 
data-src="http://kr.shanghai-jiuxin.com/file/2022/0414/small718c092b7239a6c185c2a0fc3167bef8.jpg" 
src="/d/style/lazy.gif"/><span>树叶 夕阳 海 山 秋天唯美意境高清电脑壁纸</span></a></li> 
<li><a href="/bizhitupian/weimeibizhi/245897.htm"><img 
data-src="http://kr.shanghai-jiuxin.com/file/2022/0414/small26291c282da777b06d9ca389cad82d7f.jpg" 
src="/d/style/lazy.gif"/><span>美女背影吉它 城市 夜晚 唯美壁纸</span></a></li> 
<link rel="stylesheet" href="/static/test.css">
</body>
</html>
"""
tree = etree.XML(xml)  # 使用的XML方式
# result = tree.xpath("/book")  # /表示层级关系，第一个/是根节点
# result = tree.xpath("/book/name")
# result = tree.xpath("/book/name/text()")  # text()拿文本
result = tree.xpath("/book/author/nick/text()")
result = tree.xpath("/book/author/div/nick/text()")
result = tree.xpath("/book/author//nick/text()")  # 使用//找到全部的nick
result = tree.xpath("/book/author/*/nick/text()")  # * 任意的节点，通配符，找到author下一个节点的所有nick
result = tree.xpath("/book//nick/text()")  # book下所有的nick
# print(result)

"""
etree.html是将爬取的网页数据再生成标准网页格式数据，因为有些网页不规范写的时候

etree.parse是对标准网页格式数据进行解析用的
"""
# tree = etree.parse(html)  # parse可以直接解析本地文件
tree = etree.HTML(html)  # html是parse的封装，parse经常报错，先转化为text再用html转化进行解析
result = tree.xpath('/html/body/li/a[@href="/bizhitupian/weimeibizhi/245899.htm"]')  # xpath的顺序是从1开始数的，[]表示索引
list = tree.xpath('/html/body/li')
# print(list)
for li in list:
    result = li.xpath("./a/text()")
    result = li.xpath("./a/@href")  # 拿到属性值：@属性
    print(result)

print(tree.xpath('/html/body/li/a/@href'))