number=int(input("please input total number"))
lst=[]
for _ in range(number):
    x=float(input("please input a number:"))
    lst.append(x)
sumhh=0
for i in range(len(lst)):
    sumhh+=lst[i]
averge=sumhh/len(lst)
print(sumhh,len(lst),averge)