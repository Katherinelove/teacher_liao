# -*- coding: utf-8 -*-

"""
timeit 模块
"""

__author__ = 'katherinelove'

from timeit import timeit,repeat

def func():
    s = 0
    for i in range(1000):
        s += i
    print(s)

if __name__ == '__main__':
    print(timeit("[x*x for x in range(1,10)]",number=10))
    print(repeat("[x*x for x in range(1,10)]",number=10,repeat=10))
    # timeit(函数名_字符串，运行环境_字符串，number=运行次数)
    print(timeit("func()","from __main__ import func",number=1))
    print(repeat("func()","from __main__ import func",number=100,repeat=5))