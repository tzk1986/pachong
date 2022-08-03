# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:music_spider.py
@Time:2022/5/19 13:10
说明：
"""
# 导包
import os
import requests

# 伪造浏览器身份信息, 隐藏爬虫身份，以免访问时被拒绝
# 以下信息有有效时间，当需要执行时，需要进行更新替换
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 ',
    'Referer': 'https://kuwo.cn/',  # 可以简略，直接使用官网地址
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1652938284; '
              'Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1652938284; _ga=GA1.2.474290747.1652938285; '
              '_gid=GA1.2.1202743575.1652938285; kw_token=T3M3HDEO11N ',
    'csrf': 'T3M3HDEO11N',
}
# response = requests.get('https://www.bilibili.com/video/BV1s341187jv?p=53', headers=headers)
# print(response.request.headers)

# 创建一个文件夹来存储保存下来的信息
if not os.path.exists('./music'):
    os.mkdir('./music')

# 酷我音乐网站破解下载，新版本网站已不能使用
search_music = input('请输入你想要搜索的歌曲/歌手：')
url = 'https://kuwo.cn/api/www/search/searchKey?key={}&httpsStatus=1&reqId=6148d920-d737-11ec-ad33-6577d86144a9'.format(
    search_music)
response = requests.get(url, headers=headers).json()
print(response)
music_data = response['data']['list']
for music in music_data:

    music_name = music_data['name']
    music_rid = music_data['rid']
    print(music_name, music_rid)

    music_api = 'https://cs-sycdn.kuwo.cn/88e78d9ee5be4cffa61a620bd8e38e12/{}/resource/n2/72/35/827305221.mp3'.format(
        str(music_rid))
    with open('./music' + music_name + '.mp3', 'wb') as f:
        music_play_url = requests.get(music_api, headers=headers).json()['url']
        # 获取的是音乐文件 二进制文件 content
        music_data = requests.get(music_play_url, headers=headers).content
        f.write(music_data)
        print('下载成功：', music_name)
