from socket import *
from time import ctime


HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('wating for connection')
    tcpCliSock,addr=tcpSerSock.accept()
    print('connected from ',addr)

    while True:
        try:
            data=tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send(('[%s]%s'%(ctime(),data.decode('utf-8'))).encode('utf-8'))
        except:
            print('单独客服通话套接字（通讯）关闭')
        # finally:
            #由于套接字不能重复关闭，每次循环都会关闭tcpCliSock.close()  所以会报错，故而用try catch避免多次关闭
            tcpCliSock.close()

    tcpSerSock.close()
