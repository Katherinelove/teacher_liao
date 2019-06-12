# -*- coding: utf-8 -*-

"""
socketserver高级模块
"""

__author__ = 'katherinelove'
from socket import *

HOST='localhost'
PORT=21567     #服务器端口
BUFSIZ=1024
ADDR=(HOST,PORT)


tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=input('>>>')
    if not data:
        break
    tcpCliSock.send(('%s\r\n'%data).encode('utf-8'))
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8').strip())
tcpCliSock.close()