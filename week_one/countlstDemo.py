# -*- coding: utf-8 -*-

"""count 运用"""

__author__ = 'katherinelove'
import random
import pygal

class Die():
    def __init__(self,side=6):
        self.side=side

    def roll(self):
        return random.randint(1,self.side)


if __name__ == '__main__':
    die=Die()
    results=[]
    for _ in range(500):
        result=die.roll()
        results.append(result)
    #分析数据
    frequences=[]
    for i in range(1,die.side+1):
        frequence=results.count(i)
        frequences.append(frequence)
    #print(frequences)

    #显示数据
    hist=pygal.Bar()
    hist._title="500 die roll"
    hist.x_labels=["1","2","3","4","5","6"]
    hist._x_title="result"
    hist._y_title="frequence of result"

    hist.add("D6",frequences)
    hist.render_to_file("d6.svg")