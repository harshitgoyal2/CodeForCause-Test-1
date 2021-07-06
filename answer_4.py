num = int(input("Enter the limit = "))
list = []
for i in range(0,num):
    list.append(i+1)
for j in range(i,0,-1):
    list.append(j)
count = 1
for i in range(0,num):
    for j in list:
        if j <= count:
            print(str(j)+' ',end="")
        else:
            print(" "*2,end="")
    count+=1
    print("\r")
