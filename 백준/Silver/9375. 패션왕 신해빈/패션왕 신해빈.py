count=0

for i in range(int(input())):
    list = {}
    sum=1
    for j in range(int(input())):
        a,b = input().split()
        if not b in list:
            list[b] = 1
        else:
            list[b] +=1
    for k in list.keys():
        sum =sum * (list[k]+1)
    print(sum-1)