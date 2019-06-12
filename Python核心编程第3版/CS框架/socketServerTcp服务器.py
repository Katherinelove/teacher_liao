# -*- coding: utf-8 -*-

"""
socketserver高级模块
"""

__author__ = 'katherinelove'

from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime


HOST=''
PORT=21567
ADDR=(HOST,PORT)

class MyRequsetHandler(SRH):
    '''
    发送wirte()/接收readline()信息类似文件系统
    处理程序用重写handler
    '''

    def handle(self):
        print('...connected from :',self.client_address)
        self.wfile.write(('[%s] %s'%(ctime(),self.rfile.readline().decode('utf-8'))).encode('utf-8'))

tcp=TCP(ADDR,MyRequsetHandler)
print('wattting for connection')
tcp.serve_forever()
