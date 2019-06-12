
while True:
    number = int(input("please input a number:[1~100 or 0 to exit]"))
    if number!=0:
        sum = 0
        for i in range(1, number+1, 2):
            sum += i
        print("{:>4}".format(sum))
    if number==0:
        break
