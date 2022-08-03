# -*- coding:utf-8 -*-
"""
@Author:tang
@File:第5章Ajax分析与爬取实战.py
@Time:2022/7/8 15:59
说明：
"""

import requests

# url = 'http://spa1.scrape.center/'
# html = requests.get(url).text
# print(html)

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'


def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


LIMIT = 10


def scrap_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'


def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


TOTAL_PAGE = 10


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrap_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)


if __name__ == '__main__':
    main()
