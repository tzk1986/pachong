# -*- coding:utf-8 -*-
"""
@Author:tang
@File:协程.py
@Time:2022/5/31 11:53
说明：协程样例学习，如何使用协程
"""

# 协程：当程序遇到IO操作的时候，可以选择性的切换到其他任务上
# 协程的特点： 协程是一个线程，可以跨越多个函数调用
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们能看到的其实是多个任务一起执行
# 多任务异步操作
# 以上都是在单线程的条件下
import asyncio


# async def func():
#     print("你好")
#
#
# if __name__ == '__main__':
#     g = func()  # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     # print("程序结束")
#     asyncio.run(g)  # 协程对象可以被调用需要asyncio模块支持，调用的时候会返回一个协程对象
# import time
#
#
# async def func1():
#     print("你好，我叫高蕾")
#     # time.sleep(3)  # 当程序出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(3)  # 异步操作的代码，加上await等待异步操作的结果
#     print("我是高蕾，我爱你")
#
#
# async def func2():
#     print("你好，我叫唐仲凯")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("我是唐仲凯，我爱你")
#
#
# async def func3():
#     print("你好，我叫糖糕")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("我是糖糕，我爱你")
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]
#     t1 = time.time()
#     # 一次性启动多个任务（协程）
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print("总共耗时：", t2 - t1)
import time


async def func1():
    print("你好，我叫高蕾")
    # time.sleep(3)  # 当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(3)  # 异步操作的代码，加上await等待异步操作的结果
    print("我是高蕾，我爱你")


async def func2():
    print("你好，我叫唐仲凯")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("我是唐仲凯，我爱你")


async def func3():
    print("你好，我叫糖糕")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("我是糖糕，我爱你")


async def main():
    # 第一种写法
    # f1 = func1()
    # await f1  # 一般await挂起操作放在协程对象前面
    # 第二种写法（推荐）
    tasks = [asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())]
    await asyncio.wait(tasks)  # 同时执行多个协程


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    # 一次性启动多个任务（协程）
    t2 = time.time()
    print("总共耗时：", t2 - t1)

# 在爬虫中应用
# async def download(url):
#     print("开始下载")
#     await asyncio.sleep(2)  # 代表网络请求，必须是异步的，不能直接是requests.get()，会报错
#     print("下载完成")
#
#
# async def main():
#     urls = [
#         "http://www.baidu.com"
#         "http://www.bilibili.com"
#         "http://www.163.com"
#     ]
#     tasks = []
#     for url in urls:
#         d = asyncio.create_task(download(url))
#         tasks.append(d)
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())