# -*- coding:utf-8 -*-
"""
@Author:tang
@File:demo_tqdm_sample.py
@Time:2022/5/24 12:29
说明：tqdm样例  可以进行程序进度的显示
"""
from time import sleep
from tqdm import tqdm

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    pbar.set_description("Processing %s" % char)


# for i in tqdm(range(10000)):
#      sleep(0.01)
