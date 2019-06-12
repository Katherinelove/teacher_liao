# -*- coding: utf-8 -*-

"""python image library"""

__author__ = 'katherinelove'
from PIL import Image,ImageFilter
import os
def imageOperate():
    print("==" * 50)
    os.chdir(r"E:\teacher_liao\files\images")
    im=Image.open("1.jpg")
    w,h=im.size
    print("origin size:(w:%s   h:%s)"%(w,h))
    im.thumbnail((w//2,h//2))
    print("thumbnail size:(w:%s   h:%s)"%(w//2,h//2))
    im.save("thumbnail.jpg","jpeg")

    print("=="*50)
    im=Image.open("2.jpg")
    im=im.filter(ImageFilter.BLUR)
    im.save("blur.jpg","jpeg")
    print("blur successful！")


if __name__ == '__main__':
    imageOperate()