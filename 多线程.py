# -*- coding:utf-8 -*-
"""
@Author:tang
@File:多线程.py
@Time:2022/5/30 19:16
说明：多线程样例使用
"""
from threading import Thread


# 主线程和子线程同时工作
# def func():
#     for i in range(1000):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     t = Thread(target=func)  # 创建线程并给线程安排任务
#     t.start()  # 多线程状态为可以开始工作状态，具体的执行时间由CPU决定
#     for i in range(1000):
#         print("main", i)

# 第二种多线程，需要重写run方法
class MyThread(Thread):
    def run(self) -> None:  # 固定的
        for i in range(1000):
            print("子线程", i)


if __name__ == '__main__':
    t = MyThread()
    # t.run()  # 方法调用，单线程？
    t.start()  # 开启线程
    for i in range(1000):
        print("主线程", i)


# 多线程开启多个，命名传参
def func():
    for i in range(1000):
        print("func", i)


if __name__ == '__main__':
    t1 = Thread(target=func, args=("线程1",))  # 传递参数必须是元组
    t1.start()
    t2 = Thread(target=func, args=("线程2",))
    t2.start()
    for i in range(1000):
        print("main", i)