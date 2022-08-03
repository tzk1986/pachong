# -*- coding:utf-8 -*-
"""
@Author:tang
@File:demo_requests.py
@Time:2022/5/28 16:44
说明：requests 概述 抓取网易云音乐评论信息
"""
import requests

# url = ""
# data = {
#
# }
#
# session = requests.session()  # 在一个会话中进行，保证登录状态
# resp = session.post(url=url, data=data)  # 登录
# # 使用登录的状态，会带上cookie请求后续链接
# resp = session.get()
#
# # 或者请求方式中，加上header，并在里面放入cookie
# resp = requests.get(headers={
#     "cookie": ""
# })

# # 梨视频下载，请求链接后，找到相应参数，还原视频原始链接
# url = "https://www.pearvideo.com/video_1763645"
# countId = url.split("_")[1]
# print(countId)
# videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={countId}&mrd=0.8656763888191372"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/102.0.5005.61 Safari/537.36 ",
#     # 防盗链 溯源
#     "Referer": "https://www.pearvideo.com/video_1763645",
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "Host": "www.pearvideo.com",
#     "X-Requested-With": "XMLHttpRequest",
#     "Cookie": "__secdyid=c512695018d6ae73134d255cda90ee8465e0843b3e27e108021653880567; "
#               "acw_tc=2f624a0916538805676465239e5508649067edd1a51236f29ea29f7b4c919f; "
#               "JSESSIONID=8366A7EC1E19A35BFCB5D2276D9FA731; PEAR_UUID=2dd5d16e-ba4c-4a8c-bdcf-45073a6df3dd; "
#               "_uab_collina=165388056780408756642526; p_h5_u=83B08025-20CE-41A8-AB11-88489DEDEB80; "
#               "Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1653880569; "
#               "Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1653880569; "
#               "SERVERID=ed8d5ad7d9b044d0dd5993c7c771ef48|1653880582|1653880567 ",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Connection": "keep-alive",
#     "Sec-Fetch-Site": "same-origin",
# }
# resp = requests.get(videoStatusUrl, headers=headers)
# print(resp)
# # 现有请求还需要加如其他参数才能获取数据，现在只返回状态码200
# # 后续操作记录
# # 把返回数据，进行字典处理，获取需要的参数
# dic = resp.json()
# srcUrl = dic['videoInfo']['videos']['srcUrl']
# systemTime = dic['systemTime']
# system = srcUrl.replace(systemTime, f"cont-{countId}")
# # 下载视频
# with open("a.mp4", mode="wb") as f:
#     f.write(requests.get(srcUrl).content)

#  代理 例如IP是218.60.8.83:3129，是哪个用哪个
# proxies = {
#     "http": "",
#     "https": "https://218.60.8.83:3129"
# }
# resp = requests.get("url", proxies=proxies)

