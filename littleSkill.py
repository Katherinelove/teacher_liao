# -*- coding: utf-8 -*-

"""
不为人知的小秘密，一般人我不告诉它
"""

__author__ = 'katherinelove'

from PIL import Image


#如何根据变量获取字典对象  dict[key]
def get_value(rank):
    name={"11":"J","12":"Q","13":"K"}[rank]
    return name

def get_image_load():
    img=Image.open(r'D:\GoogleDown\1000.jpg')
    print(img.load()[3,3])

if __name__ == '__main__':
    # print(get_value("13"))
    get_image_load()