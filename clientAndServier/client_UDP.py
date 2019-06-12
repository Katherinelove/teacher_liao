# -*- coding: utf-8 -*-

"""UPD编程"""

__author__ = 'katherinelove'

import socket

if __name__ == '__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        #send
        s.sendto(data,("127.0.0.1",9999))
        #recive
        print(s.recv(1024).decode("utf-8"))
    s.close()