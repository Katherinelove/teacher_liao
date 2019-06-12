# -*- coding: utf-8 -*-

"""
测试
"""

__author__ = 'katherinelove'

from multiprocessing import Process
import time

def get_session(session=20):
    lst=list(range(100))
    for i in range(0,100,session):
        se=lst[i:i+session]
        print(se)
def while_true():
    while True:
        print("1")

def hello():
    print('hello')

def haha():
    for i in range(10):
        print(i)

if __name__ == '__main__':
    # get_session()
    if True:
        p1=Process(target=while_true)
        p1.start()
        time.sleep(50)

    if True:
        p2=Process(target=hello)
        p2.start()
    if True:
        p3=Process(target=haha)
        p3.start()

