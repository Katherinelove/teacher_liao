# -*- coding: utf-8 -*-

"""context applications"""

__author__ = 'katherinelove'

from contextlib import contextmanager,closing
from urllib.request import urlopen

class Person():
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("吃了吗？%s"%self.name)

@contextmanager
def print_eat(name):
    print("start")
    p=Person(name)
    yield p
    print("end")

@contextmanager
def html(name):
    print("<%s>"%name)
    yield
    print("</%s>"%name)

if __name__ == '__main__':
        with print_eat("name") as p:
            p.eat()
        with html("h1"):
            print("<p>伊娃不</p>")
            print("<p>shabu不</p>")
        with closing(urlopen("http://www.baidu.com")) as page:
            for line in page:
                print(line)