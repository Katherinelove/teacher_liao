# -*- coding: utf-8 -*-

"""socket"""

__author__ = 'katherinelove'

import socket,threading,time

def client():
    #创建一个基于IPv4和TCP协议的Socket：
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 监听端口:
    s.bind(("127.0.0.1",9999))
    #调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
    s.listen(5)
    print("waitting for connection")
    #服务器程序通过一个永久循环来接受来自客户端的连接，accept()
    #会等待并返回一个客户端的连接:
    while True:
        # 接受一个新连接:
        sock,addr=s.accept()
        print(socket,addr)
        # 创建新线程来处理TCP连接:
        t=threading.Thread(target=tcpLinked,args=(sock,addr))
        t.start()

def tcpLinked(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')   #向Client发送信息
    while True:
        data,addr=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8")=="exit":
            break
        sock.send(("hello %s"%data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    client()