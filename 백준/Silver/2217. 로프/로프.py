import sys

n = int(sys.stdin.readline())
l = []
w = 0

for i in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

for i in range(n-1, -1, -1):
    if w < l[i]*(n-i):
        w = l[i]*(n-i)

print(w)