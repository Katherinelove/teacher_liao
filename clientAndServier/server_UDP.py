# -*- coding: utf-8 -*-

"""使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。

虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。"""

__author__ = 'katherinelove'

import socket

if __name__ == '__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    #SOCK_DGRAM指定了这个Socket的类型是UDP
    # 绑定端口:
    s.bind(("127.0.0.1",9999))
    ###绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
    print('Bind UDP on 9999...')
    while True:
        # 接收数据:
        data,addr = s.recvfrom(1024)
        print('Received from %s:%s.' %addr)
        s.sendto(b'Hello, %s!'%data,addr)    #sendto("msg",(addr))
    s.close()
    print('Connection from %s:%s closed.' % addr)

