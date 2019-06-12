# -*- coding: utf-8 -*-

"""
plus
"""

__author__ = 'katherinelove'

import  asyncio

async def hello():
    print("hello world")
    r=await asyncio.sleep(1)
    print("hello kate")

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    tasks=[hello(),hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

