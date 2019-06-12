# -*- coding: utf-8 -*-

"""
通过继承Thread父类，重写run方法即可
"""

__author__ = 'katherinelove'



from threading import Thread
from time import ctime,sleep

class MyThread(Thread):
    def __init__(self,func,args,name=''):
        Thread.__init__(self)
        self.name=name
        self.func=func       #调用的是函数地址
        self.args=args
    #继承后重写run方法
    def run(self):
        #run回到函数即可
        self.func(*self.args)    #解析参数

    # def __call__(self, *args, **kwargs):
    #     self.func(*self.args)   #确定那个函数可以回调，并传入解析的参数




loops=[4,2]   #休眠时间

def loop(nloop,nsec):
    '''
    一个休眠函数
    :param nloop:线程编号
    :param nsec: 线程休眠时间
    :return:
    '''
    print('start loop:',nloop,'at:',ctime())
    sleep(nsec)
    print('end loop:', nloop, 'done at:', ctime())

def main():
    threads=[]   #相当于线程池
    nloops=range(len(loops))
    print('主线程开始于',ctime())
    for i in nloops:
        #实例线程对象
        t=MyThread(loop,(i,loops[i]),loop.__name__)    #传入自定义的类
        threads.append(t)

    #同步开始
    for i in nloops:
        threads[i].start()

    #主线程等待子线程完成
    for i in nloops:
        threads[i].join()
    print('主线程终止于', ctime())
if __name__ == '__main__':
    main()