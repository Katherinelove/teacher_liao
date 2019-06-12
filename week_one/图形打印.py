def maian():
    while True:
        num=int(input("please input a number:[1-9 or 0 to exit]"))
        if num!=0:
            for row in range(1,num):
                for col in range(1,row+1):
                    sum=row*col
                    print("{0}*{1}={2}".format(col,row,sum),end="\t")
                print()
        else:
            break

maian()