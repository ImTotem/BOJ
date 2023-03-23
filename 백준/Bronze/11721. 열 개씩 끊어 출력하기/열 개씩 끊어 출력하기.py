from math import ceil as c

n = input()
for i in range(c(len(n)/10)):
    print(n[i*10:10*(i+1)])
