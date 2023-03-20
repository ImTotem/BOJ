import sys
c = int(sys.stdin.readline())
a=0
for i in range(c):
    a+=int(sys.stdin.readline())

print(a-(c-1))
