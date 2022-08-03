# -*- coding:utf-8 -*-
"""
@Author:tang
@File:如何抓一部视频简单版.py
@Time:2022/6/1 09:00
说明：简单视频练手
"""

"""
<video src="mp4"></video>，正常的，但是太慢
一般视频网站是怎么做的？
用户上传 -> 转码（把视频做处理，2k，1080，标清）-> 切片处理（把视频切割成一个一个的小片段）
-> 分发（把小片段分发到各个网站）

需要一个文件记录：1 视频播放顺序 2 视频存放的路径
M3U文件通过"utf-8"编码后，M3U8文件是一个字符串，每一行是一个视频的地址
所以需要解读M3U文件，把每一行的地址拿出来，拼接成一个完整的视频地址

想要抓取一个视频：
找到m3u8文件
通过m3u8文件，下载到ts文件
通过各种手段（不仅是编程手段）把ts文件合并成一个mp4文件

流程
1. 拿到url="https://91kanju2.com/vod-play/60768-1-1.html"的源代码
2. 从源代码中提取到m3u8的url
3. 把m3u8的url下载到本地
4. 下载视频
5. 合并视频

"""
import requests
import re
import asyncio
import aiohttp
import aiofiles

# obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 匹配url
#
# # url = "https://91kanju2.com/vod-play/63416-1-1.html"
# url = "https://91kanju2.com/vod-play/60768-1-1.html"
# # url = "https://m3api.awenhao.com/index.php?note=kkRa3j16rw8gsdhtfek24&raw=1&n.m3u8"
# resp = requests.get(url)
# m3u8_url = obj.search(resp.text).group("url")
# print(m3u8_url)
# # 下载m3u8文件
# resp2 = requests.get(m3u8_url)
# with open("鱿鱼游戏.m3u8", "wb") as f:
#     f.write(resp2.content)
#
# resp2.close()
# print("下载完成")

# 解析m3u8文件
# n = 1
# with open("鱿鱼游戏.m3u8", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()  # 去掉每一行的空格，空白，换行符
#         if line.startswith("#"):  # 如果是#开头，不要
#             continue
#         # print(line)
#         # 下载视频片段
#         resp3 = requests.get(line)
#         f = open(f"video/{n}.ts", "wb")
#         f.write(resp3.content)
#         f.close()
#         resp3.close()
#         print(f"下载完成{n}个")
#         n += 1


async def download(line, n, session):
    async with session.get(line) as resp:
        async with aiofiles.open(f"video/{n}.ts", "wb") as f:
            await f.write(await resp.content.read())
            f.close()
            resp.close()
#
#
#
#
async def main():
    n = 1
    tasks = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with aiofiles.open("鱿鱼游戏.m3u8", "r", encoding="utf-8") as f:
            async for line in f:
                line = line.strip()  # 去掉每一行的空格，空白，换行符
                if line.startswith("#"):  # 如果是#开头，不要
                    continue
                else:
                    # print(line)
                    tasks.append(asyncio.create_task(download(line, n, session)))
                    n += 1
            await asyncio.wait(tasks)
#
if __name__ == '__main__':
    asyncio.run(main())
    print("下载完成")