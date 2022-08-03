# -*- coding:utf-8 -*-
"""
@Author:tang
@File:进程池.py
@Time:2022/5/31 09:34
说明：线程池和进程池，线程池一次性开辟一些线程，用户直接给线程池提交任务，线程任务的调度由线程池负责
"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    # 创建线程池,如果是创建进程池，替换ProcessPoolExecutor即可
    with ThreadPoolExecutor(max_workers=50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")
    # 等待线程池中的所有任务完成，才继续执行（守护）
    print("线程池执行完毕")
