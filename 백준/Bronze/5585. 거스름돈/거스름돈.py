import sys

a = 1000 - int(sys.stdin.readline())
b=[500, 100, 50, 10, 5, 1]
c = 0
i = 0
while a > 0:
    if a >= b[i]:
        c+=a//b[i]
        a-=a//b[i]*b[i]
    i+=1

print(c)