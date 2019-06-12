# -*- coding: utf-8 -*-

"""侦测系统信息"""

__author__ = 'katherinelove'

import psutil, os

if __name__ == '__main__':
    print("============CPU=============")
    print(psutil.cpu_count())  # logical
    print(psutil.cpu_count(logical=False))  # physic
    # 统计CPU的用户／系统／空闲时间：
    print(psutil.cpu_times())
    print("============memory信息=============")
    print(psutil.virtual_memory())
    print(psutil.swap_memory())
    print("============disk信息=============")
    print(psutil.disk_partitions())
    print(psutil.disk_usage("f:"))
    print(psutil.disk_io_counters())
    print("============net信息=============")
    print(psutil.net_io_counters())
    print(psutil.net_if_addrs())
    print(psutil.net_if_stats())
    print(psutil.net_connections())
    print("============Process信息=============")
    print(psutil.pids())  # 所有进程ID
    print(os.getpid())
    p = psutil.Process(os.getpid())  # # 获取指定进程ID=6844，其实就是当前Python交互环境
    print(p.name())  # 进程名称
    print(p.exe())  # 进程exe路径
    print(p.cwd())  # 进程工作目录
    print(p.cmdline())  # 进程启动的命令行
    print(p.ppid())  # 父进程ID
    print(p.children())  # 子进程列表
    print(p.status())  # 进程状态
    print(p.username())  # 进程用户名\
    print(p.create_time())  # 进程创建时间
    # print(p.terminal())  # 进程终端
    print(p.cpu_times)  # 进程使用的CPU时间
    print(p.memory_info)  # 进程使用的内存
    print(p.open_files())  # 进程打开的文件
    print(p.connections())  # 进程相关网络连接
    print(p.num_threads())  # 进程的线程数量
    print(p.threads())  # 所有线程信息
    # p.terminate  # 结束进程
