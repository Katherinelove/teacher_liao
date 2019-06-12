import math
def sort_M_N(m,n):
    if m>n:
        t=m
        m=n
        n=t
    return m,n

def mainn():
    """求M与N之间素数之和"""
    m=int(input("please input a number:"))
    n= int(input("please input a number:"))

    m,n=sort_M_N(m,n)
    #print(m,n)
    sum=0
    for i in  range(m,n+1):
        for j in range(2, int(i ** (0.5)) + 1):
            if i % j == 0:
                print('{}不是素数'.format(i))
                break
        else:
            print('{}是素数'.format(i))
            sum += i
    print("{}--{}之间素数之和为{}".format(m, n, sum))



mainn()