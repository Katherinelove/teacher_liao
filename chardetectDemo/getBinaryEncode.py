# -*- coding: utf-8 -*-

"""检查二进制编码，语言"""

__author__ = 'katherinelove'

import chardet

if __name__ == '__main__':
    print("=================二进制默认ASCII编码==================")
    str=b"love you"
    print(chardet.detect(str))
    print("=================中文utf-8编码==================")
    name="曾帅".encode("utf-8")
    print(chardet.detect(name))