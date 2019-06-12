# -*- coding: utf-8 -*-

"""图片验证"""

__author__ = 'katherinelove'

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

def rnd_Char():
    return chr(random.randint(65,90))
def rnd_color1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rnd_color2():
    return  (random.randint(32,127),random.randint(32,127),random.randint(32,127))


def img_check():
    width=60*4
    height=60

    image=Image.new("RGB",(width,height),(255,255,255))
    font=ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
    draw=ImageDraw.Draw(image)
    #填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rnd_color1())
    # 输出文字:
    for t in range(4):
        draw.text((60*t+10,10),rnd_Char(),fill=rnd_color2(),font=font)
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    #image.show()
    image.save("code.jpg","jpeg")
if __name__ == '__main__':
    img_check()