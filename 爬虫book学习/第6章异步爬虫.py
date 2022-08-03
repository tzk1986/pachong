# -*- coding:utf-8 -*-
"""
@Author:tang
@File:第6章异步爬虫.py
@Time:2022/7/8 16:53
说明：aiohttp的使用
"""

# import aiohttp
# import asyncio
#
#
# async def main():
#     data = {'name': 'germey', 'age': 25}
#     async with aiohttp.ClientSession() as session:
#         async with session.post('https://httpbin.org/post', json=data) as response:
#             print(await response.text())
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())


# import aiohttp
# import asyncio
#
#
# async def main():
#     data = {'name': 'germey', 'age': 25}
#     async with aiohttp.ClientSession() as session:
#         async with session.post('https://httpbin.org/post', data=data) as response:
#             print('status:', response.status)
#             print('headers:', response.headers)
#             print('body:', await response.text())
#             print('bytes:', await response.read())
#             print('json:', await response.json())
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())

"""
超时设置
"""

# import aiohttp
# import asyncio
#
#
# async def main():
#     timeout = aiohttp.ClientTimeout(total=0.1)
#     async with aiohttp.ClientSession(timeout=timeout) as session:
#         async with session.get('https://httpbin.org/get') as response:
#             print('status:', response.status)
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())

"""
6.3
"""
import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 1
CONCURRENCY = 5

session = None

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'books'

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

semaphore = asyncio.Semaphore(CONCURRENCY)


async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)


async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)


async def save_data(data):
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one({
            'id': data.get('id')
        }, {
            '$set': data
        }, upsert=True)


async def main():
    # index tasks
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    # detail tasks
    print('results', results)
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_detail_tasks)
    await session.close()


if __name__ == '__main__':
    loop.run_until_complete(main())

