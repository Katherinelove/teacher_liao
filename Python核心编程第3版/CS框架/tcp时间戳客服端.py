# -*- coding: utf-8 -*-

"""
tcp服务器模板
注意接收和发生的信息是二进制对象
两种方式  ''.encode('utf-8')   或者bytes(data,encode('utf-8'))
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
    tcpCliSock.send(data.encode('utf-8'))
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()