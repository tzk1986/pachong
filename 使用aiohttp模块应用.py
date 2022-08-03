# -*- coding:utf-8 -*-
"""
@Author:tang
@File:使用aiohttp模块应用.py
@Time:2022/5/31 15:09
说明：requests的异步操作
"""
# requests.get() 同步的代码 -> aiohttp.ClientSession().get() 异步的代码
# pip install aiohttp
import aiohttp
import asyncio

urls = {
    "http://kr.shanghai-jiuxin.com/file/2022/0414/9e5827678bd12db0999a573254e40d1e.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0414/ba34fff6a58897cc5362b79e477c06d8.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0414/33f06e321d65146414aefd830013dfe7.jpg",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}


async def aiodownload(url):
    name = url.rsplit("/")[6]  # 反向分隔后取第0个元素
    print(name)
    # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64,verify_ssl=False)) as session:
    #     async with session.get(url, headers=headers) as resp:
    #         # 将图片保存到本地
    #         # 可以使用aiofiles模块，异步的文件读写
    #         with open(f"{name}.jpg", "wb") as f:
    #             f.write(await resp.content.read())  # 异步操作需要加await挂起
    #         print(f"{name}下载完成")
    # 发送请求
    # 得到图片内容


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
