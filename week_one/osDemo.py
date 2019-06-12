# -*- coding: utf-8 -*-

"""OS模块操作"""

__author__ = 'katherinelove'

import os

def start():
    print("os name:"+os.name)
    print(os.environ)
    print(os.environ.get("Path"))
    print(os.getcwd())

    print("=="*20)

    lst=os.listdir(r"E:\teacher_liao")
    print(lst)
    #path  一部分在os模块中，一部分在os.path模块中
    lst=os.path.split(r"E:\teacher_liao\week_one\99乘法表右上角.py")
    #这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
    print(lst)
    #获取后缀
    lst = os.path.splitext(r"E:\teacher_liao\week_one\99乘法表右上角.py")
    print(lst)
    #只获取目录列表
    lst2=[x for x in os.listdir(".")]
    print(lst2)
    #筛选.py
    lst2=[x for x in os.listdir(".") if os.path.splitext(x)[1]==".py"]
    print(lst2)

    print("absPath ："+os.path.abspath("."))
    os.path.join(r"E:\teacher_liao\files","txt")

    print("==" * 20)
    os.mkdir(r"E:\teacher_liao\files\javas")
    print("创建目录成功！")
    os.rmdir(r"E:\teacher_liao\files\javas")
    print("删除目录成功！")



if __name__ == '__main__':
    start()