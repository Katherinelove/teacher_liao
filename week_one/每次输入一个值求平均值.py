count=0
sum=0

while True:
    num= input(">>>")
    if num=='quit':
        break
    count+=1
    sum+=float(num)
    averge=sum/count
    print(averge)