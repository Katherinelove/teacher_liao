# -*- coding: utf-8 -*-

"""自由漫游"""

__author__ = 'katherinelove'

import random
import matplotlib.pyplot as plt

class Randwalk():
    def __init__(self,times=5000):
        self.times=times

        self.x_values=[0]
        self.y_values=[0]

    def walk(self):
        while len(self.x_values)<self.times:
            x_direction=random.choice([1,-1])
            x_distance=random.choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction=random.choice([1,-1])
            y_distance = random.choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step==0 and y_step==0:
                continue
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


if __name__ == '__main__':
    randwalk=Randwalk()
    randwalk.walk()
    points=list(range(randwalk.times))
    plt.scatter(randwalk.x_values,randwalk.y_values,c=points,cmap=plt.cm.Blues,s=3)

    plt.scatter(0,0,c="red",s=10)
    plt.scatter(randwalk.x_values[-1],randwalk.y_values[-1],c="green",s=10)

    plt.title("randwalk",fontsize=15)
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.axis([])
    plt.show()