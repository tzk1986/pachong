# -*- coding:utf-8 -*-
"""
@Author:tang
@File:多进程.py
@Time:2022/5/31 09:18
说明：多进程样例学习，比多线程消耗的资源更多，与多线程一样有两种方式
"""
from multiprocessing import Process


def func():
    for i in range(1000):
        print("子进程", i)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    for i in range(1000):
        print("主进程", i)
