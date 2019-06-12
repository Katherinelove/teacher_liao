#简略

def function1(num):
    #num = int(input("please input numbner:"))
    sum = 0
    mutiply = 1
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            mutiply *= j  # 每行的阶乘
        sum += mutiply
        mutiply=1  #必须清零
    print(sum)
def function2(num):
    #num = int(input("please input numbner:"))
    sum = 0
    mutiply = 1
    for i in range(1,num+1):
        mutiply*=i
        sum+=mutiply
    print(sum)

function1(5)
function2(5)