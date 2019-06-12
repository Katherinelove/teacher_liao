# -*- coding: utf-8 -*-

"""
hashlib apllications
    常见摘要算法   MD5和SHA1
"""

__author__ = 'katherinelove'

import hashlib

def main():
    md5Case()
    sha1Case()

def sha1Case():
    sha11=hashlib.sha1()
    sha11.update("lvoe".encode("utf-8"))
    print(sha11.hexdigest())

def md5Case():
    md5_1 = hashlib.md5()
    content1 = "kate I love you!"
    content2 = "kate I love you."
    md5_1.update(content1.encode("utf-8"))
    print(md5_1.hexdigest())
    md5_2 = hashlib.md5()
    md5_2.update(content2.encode("utf-8"))
    print(md5_2.hexdigest())


if __name__ == '__main__':
    main()