# -*- coding: utf-8 -*-

"""
异步io用法，同一线程不用 理会读取io的时间，直接用结果
"""

__author__ = 'katherinelove'

import asyncio

@asyncio.coroutine
def hello():
    print("1")
    print("2")
    print("3")
    r=yield from asyncio.sleep(1)  #模拟内存读取
    print("4")
    print("5")
    print("6")
    r = yield from asyncio.sleep(2)  # 模拟内存读取
    print("7")
    print("8")
    print("9")
    print("===========================================")

if __name__ == '__main__':
    # 获取EventLoop:
    loop=asyncio.get_event_loop()
    #获取任务
    tasks=[hello(),hello()]
    # 执行coroutine
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()