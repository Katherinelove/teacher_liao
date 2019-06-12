# -*- coding: utf-8 -*-

"""
由于我们的Web App建立在asyncio的基础上，因此用aiohttp写一个基本的app.py：
"""

__author__ = 'katherinelove'

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type="text/html")

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


# import logging;logging.basicConfig(level=logging.INFO)
# import asyncio,time,os,json
# from datetime import datetime
# from aiohttp import web
#
# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>')
#
# @asyncio.coroutine
# def init(loop):
#     app=web.Application(loop=loop)
#     app.router.add_route('GET','/',index)
#     srv=yield from loop.create_server(app.make_handler(),"127.0.0.1",9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv
# if __name__ == '__main__':
#     loop=asyncio.get_event_loop()
#     loop.run_until_complete(init(loop))
#     loop.run_forever()