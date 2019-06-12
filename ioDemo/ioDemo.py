# -*- coding: utf-8 -*-

"""todo"""

__author__ = 'katherinelove'


import os
from io import StringIO  # 读取字符到内存中
from io import BytesIO   # 读取二进制到内存中

def start():
    io_optiom()
    stringIo_option()
    bytes_io()

def bytes_io():
    fs=BytesIO()
    fs.write("中文".encode("utf-8"))    #str.encode设置编码格式
    print(fs.getvalue())

def stringIo_option():
    """直接写入内存"""
    f=StringIO()
    f.write("sb,你在干啥子！")
    f.write("\n")
    f.write("yeye zaici")
    print(f.getvalue())

    # 从内存中读取
    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())

def io_optiom():
    print(os.getcwd())
    os.chdir(r"E:\teacher_liao\files")
    print(os.getcwd())
    with open("1.txt", "w") as f:
        f.write("love you!")
    with open("1.txt", "r") as f:
        print(f.read(1024))  # 按内存读取


if __name__ == '__main__':
    start()
