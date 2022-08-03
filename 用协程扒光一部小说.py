# -*- coding:utf-8 -*-
"""
@Author:tang
@File:用协程扒光一部小说.py
@Time:2022/5/31 17:03
说明：用协程扒光一部小说
"""
import requests
import asyncio
import aiohttp
import aiofiles
import json

"""
1. 同步操作 拿到所有章节
2. 异步操作 下载所有的文章内容
"""


async def aiodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1,
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            content = dic['data']['novel']['content']
            async with aiofiles.open(f"./xiaoshuo/{title}.txt", "w", encoding="utf-8") as f:
                await f.write(content)


async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for a in dic['data']['novel']['items']:
        title = a['title']
        cid = a['cid']
        # 准备异步任务
        tasks.append(asyncio.create_task(aiodownload(cid, b_id, title)))
        # print(title, cid)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    b_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    print(url)
    asyncio.run(getCatalog(url))
