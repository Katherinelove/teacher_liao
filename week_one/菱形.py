while True:
    row=input("please input a row:")
    if row=="quit":
        break
    row=int(row)
    for i in range(-row, row+1):
        if i < 0:
            i = -i
        else:
            i = i
        print(" " * i + "*" * ((2*row-1)- 2 * i))

    for i in range(-row, row+1):
        if i < 0:
            i = -i
        else:
            i = i
        print(" " * i + "*" * (row+1 - i))

    for i in range(-row, row+1):
        if i == 0:
            print("#" *((2*(row+1))-1))
        else:
            if i < 0:
                print(" " * (-i) + "#" * (row+1+ i))
            else:
                print(" " * row + "#" * (row+1 - i))

