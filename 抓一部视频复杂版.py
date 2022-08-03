# -*- coding:utf-8 -*-
"""
@Author:tang
@File:抓一部视频复杂版.py
@Time:2022/6/1 16:13
说明：
"""
import os
import re

"""
url="https://91kanju2.com/vod-play/541-2-1.html"
拿到主页面的页面源代码，找到ifreme的src属性
从iframe的页面源代码中拿到m3u8的文件地址
下载第一层m3u8文件 -> 获取第二层m3u8文件(视频存放路径)
下载视频
下载密钥，进行解密操作
合并所有ts文件为一个mp4文件
  
"""
import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import aiofiles
from crypto.Cipher import AES


def get_iframe_src(url):
    # resp = requests.get(url)
    # soup = BeautifulSoup(resp.text, 'lxml')
    # iframe = soup.find('iframe')["src"]
    # print(iframe)
    # return iframe
    return "https://boba.52kuyun.com/share/xfPs9NPHvYGhNzFp"  # 测试用直接返回


def get_first_m3u8_url(url):
    # resp = requests.get(url)
    # # print(resp.text)
    # obj = re.compile(r'var main = "(?P<m3u8_url>.*?)"', re.S)
    # m3u8_url = obj.search(resp.text).group("m3u8_url")
    # print(m3u8_url)
    # return m3u8_url
    return "/20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af21aa18e1"


def download_m3u8_file(url, name):
    resp = requests.get(url)
    with open(name, "wb") as f:
        f.write(resp.content)


async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video2/{name}", "wb") as f:
            await f.write(await resp.content.read())  # 写入文件
    print(f"{name}下载完毕")


async def aio_download(up_url):
    tasks = []
    async with aiohttp.ClientSession() as session:  # 提前准备好session
        async with aiofiles.open("越狱第一季第一集_second_m3u8.txt", "r", encoding="utf-8") as f:
            async for line in f:
                if line.startswith("#"):
                    continue  # 跳过注释行
                else:
                    line = line.strip()
                    # 准备拼接第二层m3u8文件的下载路径
                    ts_url = up_url + line
                    task = asyncio.create_task(download_ts(ts_url, line, session))  # 创建异步任务
                    tasks.append(task)
            await asyncio.wait(tasks)  # 等待所有任务完成


def get_key(url):
    resp = requests.get(url)
    key = resp.text
    return key


async def dec_ts(name, key):
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video2/{name}", "rb") as f1, \
            aiofiles.open(f"video2/temp_{name}", "wb") as f2:
        bs = await f1.read()  # 从源文件读取数据
        # aes.decrypt(bs)  # 解密
        await f2.write(aes.decrypt(bs))  # 写入文件
        print(f"{name}解密完毕")


async def aio_dec(key):
    # 解密
    tasks = []
    async with open("越狱第一季第一集_second_m3u8.txt", "r", encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue  # 跳过注释行
            else:
                line = line.strip()
                task = asyncio.create_task(dec_ts(line, key))
                tasks.append(task)
        await asyncio.wait(tasks)


# mac: cat 1.ts 2.ts 3.ts > 1.mp4
# windows: copy /b 1.ts+2.ts+3.ts 1.mp4
def merge_ts():
    ts_lst = []
    with open("越狱第一季第一集_second_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue  # 跳过注释行
            line = line.strip()
            ts_lst.append(f"video2/temp_{line}")
    s = " ".join(ts_lst)
    os.system(f"cat {s} video2/越狱第一季第一集_second.mp4")


def main(url):
    # 1.拿到主页面的页面源代码，找到iframe的src属性
    iframe_src = get_iframe_src(url)
    # 2.从iframe的页面源代码中拿到m3u8的文件地址
    first_m3u8_url = get_first_m3u8_url(iframe_src)
    # 3.拿到iframe的域名
    iframe_domain = iframe_src.split("/share")[0]
    # 拼接出真正的m3u8的下载路径
    first_m3u8_url = iframe_domain + first_m3u8_url
    # print(first_m3u8_url)
    # 下载第一层m3u8文件
    download_m3u8_file(first_m3u8_url, "越狱第一季第一集_first_m3u8.txt")
    # 下载第二层m3u8文件
    with open("越狱第一季第一集_first_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue  # 跳过注释行
            else:
                line = line.strip()
                # 准备拼接第二层m3u8文件的下载路径
                second_m3u8_url = first_m3u8_url.split("index.m3u8")[0] + line
                download_m3u8_file(second_m3u8_url, "越狱第一季第一集_second_m3u8.txt")
    # 下载视频
    second_m3u8_url_up = second_m3u8_url.replace("index.m3u8", "")
    # 异步协程
    asyncio.run(aio_download(second_m3u8_url_up))

    # 拿到密钥
    key_url = second_m3u8_url_up + "key.key"
    key = get_key(key_url)
    # 解密
    asyncio.run(aio_dec(key))

    # 合并ts文件为mp4文件
    merge_ts()


if __name__ == '__main__':
    url = "https://91kanju2.com/vod-play/541-2-1.html"
    main(url)
