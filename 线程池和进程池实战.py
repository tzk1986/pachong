# -*- coding:utf-8 -*-
"""
@Author:tang
@File:线程池和进程池实战.py
@Time:2022/5/31 09:58
说明：使用线程池进行新发地菜价的爬取
"""
# 1.提取单个页面的数据
# 2.上线程池，多个页面同时抓取
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", "w", encoding="utf-8", newline="")
csvwriter = csv.writer(f)

# 现在网站与视频教学中数据展示方式已经不一致，需要进行逆向反爬
def download_one_page(url):
    headers = {
        "Referer": "http://xinfadi.com.cn/priceDetail.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/102.0.5005.61 Safari/537.36 "
    }
    data = {
        "limit": "",
        "current": "",
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": "",
    }
    resp = requests.post(url, headers=headers, data=data)
    resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    print(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    trs = table.xpath("./tr")[1:]  # 从第一个开始，不要第0个数据
    trs = table.xpath("./tr[position()>1]")  # 从大于1的开始，不要第1个数据的另一个方式
    for tr in trs:
        txt = tr.xpath("./td[1]/text()")[0]
        # 对数据做简单处理：去除/ \\
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        # 将数据写入csv文件
        csvwriter.writerow(txt)
    print(url, "提取完毕")


if __name__ == '__main__':
    # for i in range(1, 10):
    #     download_one_page(f"http://xinfadi.com.cn/priceDetail{i}.html")

    for i in range(1, 10):
        with ThreadPoolExecutor(max_workers=50) as t:
            for i in range(1, 200):
                t.submit(download_one_page, f"http://xinfadi.com.cn/priceDetail{i}.html")
    print("提取完毕")
