# -*- coding: utf-8 -*-

"""test"""

__author__ = 'katherinelove'
import os

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath=os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

if __name__ == '__main__':
    print_directory_contents(r"E:\teacher_liao")